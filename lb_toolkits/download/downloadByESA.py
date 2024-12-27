# -*- coding:utf-8 -*-
'''
@Project     : lb_toolkits  
----------------------------------------
@File        : downloadByESA.py  
----------------------------------------
@Modify Time : 2024/11/15  
----------------------------------------
@Author      : Lee  
----------------------------------------
@Desciption
----------------------------------------

接口说明：  https://documentation.dataspace.copernicus.eu/APIs/OData.html
 
'''
import os
import sys
import numpy as np
import datetime

import hashlib
import logging
import re
import xml.etree.ElementTree as ET
from collections import OrderedDict, defaultdict, namedtuple
from copy import copy
from datetime import date, datetime, timedelta
from urllib.parse import quote_plus, urljoin
import json
import geojson
import geomet.wkt
import html2text
import requests
from tqdm.auto import tqdm

import concurrent.futures
import enum
import itertools
import shutil
import threading
import time
import traceback
from collections import namedtuple
from concurrent.futures import ThreadPoolExecutor
from contextlib import closing
from pathlib import Path
from typing import Any, Dict
from xml.etree import ElementTree as etree


sentinelsat_version = "1.2.1"
URL_LOGIN    = 'https://identity.dataspace.copernicus.eu/auth/realms/CDSE/protocol/openid-connect/token'
URL_SEARCH   = 'https://catalogue.dataspace.copernicus.eu/'
URL_DOWNLOAD = 'https://download.dataspace.copernicus.eu/'

class SentinelAPIError(Exception):
    """Invalid response from DataHub. Base class for more specific exceptions.

    Attributes
    ----------
    msg: str
        The error message.
    response: requests.Response
        The response from the server as a `requests.Response` object.
    """

    def __init__(self, msg="", response=None):
        self.msg = msg
        self.response = response

    def __str__(self):
        if self.response is None:
            return self.msg
        if self.response.reason:
            reason = " " + self.response.reason
        else:
            reason = ""
        return "HTTP status {}{}: {}".format(
            self.response.status_code,
            reason,
            ("\n" if "\n" in self.msg else "") + self.msg,
            )


class LTAError(SentinelAPIError):
    """Error raised when retrieving a product from the Long Term Archive"""

    pass


class LTATriggered(SentinelAPIError):
    """Download failed due to product being in the Long Term Archive and retrieval from LTA was triggered"""

    def __init__(self, uuid):
        self.uuid = uuid
        super().__init__(
            f"Product {uuid} is not online. Triggered retrieval from the Long Term Archive."
        )


class ServerError(SentinelAPIError):
    """Error raised when the server responded in an unexpected manner, typically due to undergoing maintenance"""

    pass


class UnauthorizedError(SentinelAPIError):
    """Error raised when attempting to retrieve a product with incorrect credentials"""

    def __str__(self):
        return self.msg


class QuerySyntaxError(SentinelAPIError, SyntaxError):
    """Error raised when the query string could not be parsed on the server side"""

    def __init__(self, msg, response):
        SentinelAPIError.__init__(self, msg, response)
        SyntaxError.__init__(self, msg)

    def __str__(self):
        return self.msg


class QueryLengthError(SentinelAPIError):
    """Error raised when the query string length was excessively long"""

    def __str__(self):
        return self.msg


class InvalidKeyError(SentinelAPIError, KeyError):
    """Error raised when product with given key was not found on the server"""

    def __init__(self, msg, response):
        SentinelAPIError.__init__(self, msg, response)
        KeyError.__init__(self, msg)

    def __str__(self):
        return self.msg


class InvalidChecksumError(Exception):
    """MD5 checksum of a local file does not match the one from the server."""

    pass


class downloadByESA :
    logger = logging.getLogger(__name__)

    def __init__(
            self,
                 username,
                 password,
                 show_progressbars=True,
            timeout=60
    ):
        self.session = requests.Session()
        # if user and password:
        #     self.session.auth = (user, password)
        # # self.user_agent = "sentinelsat/" + sentinelsat_version
        # # self.session.headers["User-Agent"] = self.user_agent
        # self.session.headers["Content-Type"] = 'application/x-www-form-urlencoded'
        # self.session.data = {
        #     "username" : user,
        #     "password" : password,
        #     "grant_type" : "password",
        #     "client_id" : "cdse-public"
        # }
        self.session.timeout = timeout
        self.show_progressbars = show_progressbars
        self.token = self.getToken(username, password)
        # print(self.token)
        # self.api_url = api_url if api_url.endswith("/") else api_url + "/"
        self.api_url = URL_SEARCH if URL_SEARCH.endswith("/") else URL_SEARCH + "/"
        self.page_size = 100

        self.show_progressbars = True
        self._dhus_version = None
        # For unit tests
        self._last_query = None
        self._last_response = None
        self._online_attribute_used = True

        self._concurrent_dl_limit = 4
        self._concurrent_lta_trigger_limit = 10

        # The number of allowed concurrent GET requests is limited on the server side.
        # We use a bounded semaphore to ensure we stay within that limit.
        # Notably, LTA trigger requests also count against that limit.
        self._dl_limit_semaphore = threading.BoundedSemaphore(self._concurrent_dl_limit)
        self._lta_limit_semaphore = threading.BoundedSemaphore(self._concurrent_lta_trigger_limit)

        self.downloader = Downloader(self)

    def getToken(self, username, password):
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
        }
        data = {
            "username" : username,
            "password" : password,
            "grant_type" : "password",
            "client_id" : "cdse-public"
        }
        resp = requests.post(URL_LOGIN, headers=headers, data=data)
        if resp.status_code == 200 :
            res = json.loads(resp.text)
            token = res["access_token"]
            # print('成功创建token【%s】' %(token))

            return token
        else:
            print('创建token失败')
            return None

    def searchfile(
            self,
            startdate,
            enddate,
            collection,
            footprint=None,
            Options=None,
            area_relation="Intersects",
            order_by='-ContentDate/Start',
            limit=None,
            offset=0,
            **keywords
    ):
        """Query the OpenSearch API with the coordinates of an area, a date interval
        and any other search keywords accepted by the API.

        Parameters
        ----------
        footprint : str, optional
            The area of interest formatted as a Well-Known Text string.
        Options : str, optional
            Additional query text that will be appended to the query.
        area_relation : {'Intersects', 'Contains', 'IsWithin'}, optional
            What relation to use for testing the AOI. Case insensitive.

                - Intersects: true if the AOI and the footprint intersect (default)
                - Contains: true if the AOI is inside the footprint
                - IsWithin: true if the footprint is inside the AOI

        order_by: str, optional
            A comma-separated list of fields to order by (on server side).
            Prefix the field name by '+' or '-' to sort in ascending or descending order,
            respectively. Ascending order is used if prefix is omitted.
            Example: "cloudcoverpercentage, -beginposition".
        limit: int, optional
            Maximum number of products returned. Defaults -1 to no limit.
        offset: int, optional
            The number of results to skip. Defaults to 0.
        **keywords
            Additional keywords can be used to specify other query parameters,
            e.g. `relativeorbitnumber=70`.
            See https://scihub.copernicus.eu/twiki/do/view/SciHubUserGuide/3FullTextSearch
            for a full list.

        Returns
        -------
        dict[string, dict]
            Products returned by the query as a dictionary with the product ID as the key and
            the product's attributes (a dictionary) as the value.
        """

        query = self.format_query(collection, startdate,
                                  enddate, Options=Options, footprint=footprint,
                                  area_relation=area_relation, order_by=order_by,
                                  limit=limit, offset=offset, **keywords)
        if query.strip() == "":
            # An empty query should return the full set of products on the server, which is a bit unreasonable.
            # The server actually raises an error instead and it's better to fail early in the client.
            raise ValueError("Empty query.")

        # check query length - often caused by complex polygons
        if self.check_query_length(query) > 1.0:
            self.logger.warning(
                "The query string is too long and will likely cause a bad DHuS response."
            )

        self.logger.debug(
            "Running query: order_by=%s, limit=%s, offset=%s, query=%s",
            order_by,
            limit,
            offset,
            query,
        )
        formatted_order_by = self._format_order_by(order_by)
        response, count = self._load_query(query, formatted_order_by, limit, offset)
        self.logger.info('共检索产品文件个数：【%d】' %(count))

        return response

        return self._parse_opensearch_response(response)

    def download(self, outdir, url, checksum=True, nodefilter=None, skip_download=False, **kwargs):
        """Download a product.

        Uses the filename on the server for the downloaded file, e.g.
        "S1A_EW_GRDH_1SDH_20141003T003840_20141003T003920_002658_002F54_4DD1.zip".

        Incomplete downloads are continued and complete files are skipped.

        Parameters
        ----------
        url : string
            UUID of the product, e.g. 'a8dd0cfd-613e-45ce-868c-d79177b916ed'
        outdir : string, optional
            Where the file will be downloaded
        checksum : bool, default True
            If True, verify the downloaded file's integrity by checking its checksum.
            Throws InvalidChecksumError if the checksum does not match.
        nodefilter : callable, optional
            The callable is used to select which files of each product will be downloaded.
            If None (the default), the full products will be downloaded.
            See :mod:`sentinelsat.products` for sample node filters.

        Returns
        -------
        product_info : dict
            Dictionary containing the product's info from get_product_odata() as well as
            the path on disk.

        Raises
        ------
        InvalidChecksumError
            If the MD5 checksum does not match the checksum on the server.
        LTATriggered
            If the product has been archived and its retrieval was successfully triggered.
        LTAError
            If the product has been archived and its retrieval failed.
        """
        downloader = copy(self.downloader)
        downloader.node_filter = nodefilter
        downloader.verify_checksum = checksum
        downloader.token = self.token

        if isinstance(url, list):
            for item in url :
                downloader.download(item, outdir, skip_download=skip_download)
        else:
            return downloader.download(url, outdir, skip_download=skip_download)

    def format_query(self, collection, startdate, enddate,
                     Options=None, footprint=None, area_relation="Intersects", **keywords):
        """Create a OpenSearch API query string."""

        # OpenSearch :
        # "https://catalogue.dataspace.copernicus.eu/resto/api/collections/Sentinel2/search.json?cloudCover=[0,10]&startDate=2022-06-11T00:00:00Z&completionDate=2022-06-22T23:59:59Z&maxRecords=10"
        # https://catalogue.dataspace.copernicus.eu/resto/api/collections/search.json?cloudCover=[0,10]&startDate=2022-06-11T00:00:00Z&completionDate=2022-06-22T23:59:59Z&maxRecords=10

        # OData
        # https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name eq 'CCM' and OData.CSC.Intersects(area=geography'SRID=4326;POLYGON((12.655118166047592 47.44667197521409,21.39065656328509 48.347694733853245,28.334291357162826 41.877123516783655,17.47086198383573 40.35854475076158,12.655118166047592 47.44667197521409))') and ContentDate/Start gt 2021-05-20T00:00:00.000Z and ContentDate/Start lt 2021-07-21T00:00:00.000Z

        if Options is None :
            Options = []
        elif isinstance(Options, str):
            Options = [Options]
        elif isinstance(Options, list):
            Options = Options
        else:
            raise ValueError("Options must be a string or a list of strings.")

        Options.append("Collection/Name eq '{}'".format(collection.upper()))

        Options.extend(self._format_date(startdate, enddate,))
        # Options.extend(self._format_orderby(order_by))

        if area_relation.lower() not in {"intersects", "contains", "iswithin"}:
            raise ValueError("Incorrect AOI relation provided ({})".format(area_relation))

        if footprint is not None and area_relation.lower() in {"intersects", "contains", "iswithin"}:
            Options.append("OData.CSC.{area_relation}(area=geography'SRID=4326;{footprint}')".format(area_relation=area_relation,
                                                                                        footprint=footprint))
        converters = {
            'string' : str,
            "date": self._parse_iso_date,
            "int": int,
            "integer": int,
            "long": int,
            "float": float,
            "double": float
        }

        # Keep the string type by default
        def default_converter(x):
            return x

        attributes = self._get_attributes_info(collection.upper())
        for attr, value in sorted(keywords.items()) :
            if value is None :
                continue

            if attr not in attributes[collection.upper()] :
                continue

            key = attributes[collection.upper()][attr]
            if key.lower() not in converters:
                print('类型不支持【%s】' %(attributes[collection.upper()][attr]))
                continue

            if key.lower() == 'string' :
                Options.append("Attributes/OData.CSC.StringAttribute/any(att:att/Name eq '{Name}' and " \
                               "att/OData.CSC.StringAttribute/Value eq '{Value}')".format(Name=attr, Value=value))

            else:
                f = converters.get(key.lower(), default_converter)
                if isinstance(value, list) or isinstance(value, tuple):
                    Options.append("Attributes/OData.CSC.{key}Attribute/any(att:att/Name eq '{Name}' " \
                                   "and att/OData.CSC.{key}Attribute/Value ge {Value})".format(key=key, Name=attr,
                                                                                               Value=f(value[0])))
                    Options.append("Attributes/OData.CSC.{key}Attribute/any(att:att/Name eq '{Name}' " \
                                   "and att/OData.CSC.{key}Attribute/Value le {Value})".format(key=key, Name=attr,
                                                                                               Value=f(value[1])))
                else:
                    Options.append("Attributes/OData.CSC.{key}Attribute/any(att:att/Name eq '{Name}' and " \
                                   "att/OData.CSC.{key}Attribute/Value le {Value})".format(key=key, Name=attr, Value=f(value)))
        #     if isinstance(value, set):
        #         if len(value) == 0:
        #             continue
        #         sub_parts = []
        #         for sub_value in value:
        #             sub_value = _format_query_value(attr, sub_value)
        #             if sub_value is not None:
        #                 sub_parts.append(f"{attr}:{sub_value}")
        #         sub_parts = sorted(sub_parts)
        #         query_parts.append("({})".format(" OR ".join(sub_parts)))
        #     else:
        #         value = _format_query_value(attr, value)
        #         if value is not None:
        #             query_parts.append(f"{attr}:{value}")
        #
        # if Options is not None:
        #     query_parts.append(Options)
        #
        # if area is not None:
        #     query_parts.append('footprint:"{}({})"'.format(area_relation, area))

        return ' and '.join(Options)

    def _get_attributes_info(self, collection=None):
        '''
        Attributes :
        https://catalogue.dataspace.copernicus.eu/odata/v1/Attributes
        https://catalogue.dataspace.copernicus.eu/odata/v1/Attributes(SENTINEL-2)
        Attributes/OData.CSC.StringAttribute/any(att:att/Name eq ‘[Attribute.Name]’ and att/OData.CSC.StringAttribute/Value eq ‘[Attribute.Value]’)
        [Attribute.Name] is the attribute name which can take multiple values depending on collection; acceptable values for the attribute name can be checked at the specified endpoints for each collection, as provided in List of OData query attributes.
        eq before [Attribute.Value] can be substituted with le, lt, ge, gt in case of Integer, Double or DateTimeOffset Attributes
        [Attribute.Value] is the specific value that the user is searching for
        '''

        if collection is not None:
            attr_url = URL_SEARCH + 'odata/v1/Attributes({collection})'.format(collection=collection.upper())
        else:
            attr_url = URL_SEARCH + 'odata/v1/Attributes'

        resp = self.session.get(attr_url)

        self._check_scihub_response(resp)
        data = resp.json()

        attrs = {}
        if isinstance(data, dict) :
            for collection in data :
                attrs[collection.upper()] = {}
                for item in data[collection] :
                    attrs[collection.upper()][item['Name']] = item['ValueType']
        elif isinstance(data, list):

            attrs[collection.upper()] = {}
            for item in data :
                attrs[collection.upper()][item['Name']] = item['ValueType']

        return attrs

    def _format_date(self, startdate, enddate):
        if startdate is None:
            return []

        if enddate is None:
            return [
                "ContentDate/Start ge %s" %(startdate.strftime('%Y-%m-%dT%H:%M:%S.%fZ'))
            ]

        return [
                "ContentDate/Start ge %s" %(startdate.strftime('%Y-%m-%dT%H:%M:%S.%fZ')),
                "ContentDate/End lt %s"   %(enddate.strftime('%Y-%m-%dT%H:%M:%S.%fZ'))
            ]

    def _format_orderby(self, orderby):
        # orderby:
        # ContentDate/Start, ContentDate/End, PublicationDate, ModificationDate, in directions: asc, desc.
        if orderby is None:
            return []
        elif orderby in ['ContentDate/Start, ContentDate/End, PublicationDate, ModificationDate'] :
            return [orderby]
        else:
            return []

    @property
    def concurrent_dl_limit(self):
        """int: Maximum number of concurrent downloads allowed by the server."""
        return self._concurrent_dl_limit

    @concurrent_dl_limit.setter
    def concurrent_dl_limit(self, value):
        self._concurrent_dl_limit = value
        self._lta_limit_semaphore = threading.BoundedSemaphore(self._concurrent_dl_limit)

    @property
    def concurrent_lta_trigger_limit(self):
        """int: Maximum number of concurrent Long Term Archive retrievals allowed."""
        return self._concurrent_lta_trigger_limit

    @concurrent_lta_trigger_limit.setter
    def concurrent_lta_trigger_limit(self, value):
        self._concurrent_lta_trigger_limit = value
        self._dl_limit_semaphore = threading.BoundedSemaphore(self._concurrent_lta_trigger_limit)

    @property
    def dl_retry_delay(self):
        """float, default 10: Number of seconds to wait between retrying of failed downloads."""
        return self.downloader.dl_retry_delay

    @dl_retry_delay.setter
    def dl_retry_delay(self, value):
        self.downloader.dl_retry_delay = value

    @property
    def lta_retry_delay(self):
        """float, default 60: Number of seconds to wait between requests to the Long Term Archive."""
        return self.downloader.lta_retry_delay

    @lta_retry_delay.setter
    def lta_retry_delay(self, value):
        self.downloader.lta_retry_delay = value

    @property
    def lta_timeout(self):
        """float, optional: Maximum number of seconds to wait for triggered products to come online.
        Defaults to no timeout."""
        return self.downloader.lta_timeout

    @lta_timeout.setter
    def lta_timeout(self, value):
        self.downloader.lta_timeout = value

    @property
    def dl_limit_semaphore(self):
        return self._dl_limit_semaphore

    @property
    def lta_limit_semaphore(self):
        return self._lta_limit_semaphore

    @staticmethod
    def _api2dhus_url(api_url):
        url = re.sub("apihub/$", "dhus/", api_url)
        url = re.sub("apihub.copernicus.eu", "scihub.copernicus.eu", url)
        return url

    def _req_dhus_stub(self):
        try:
            with self.dl_limit_semaphore:
                resp = self.session.get(self.api_url + "api/stub/version")
            resp.raise_for_status()
        except requests.exceptions.HTTPError as err:
            self.logger.error("HTTPError: %s", err)
            self.logger.error("Are you trying to get the DHuS version of APIHub?")
            self.logger.error("Trying again after conversion to DHuS URL")
            with self.dl_limit_semaphore:
                resp = self.session.get(self._api2dhus_url(self.api_url) + "api/stub/version")
            resp.raise_for_status()
        return resp.json()["value"]

    @property
    def dhus_version(self):
        if self._dhus_version is None:
            self._dhus_version = self._req_dhus_stub()
        return self._dhus_version

    def count(self, area=None, date=None, raw=None, area_relation="Intersects", **keywords):
        """Get the number of products matching a query.

        Accepted parameters are identical to :meth:`SentinelAPI.query()`.

        This is a significantly more efficient alternative to doing `len(api.query())`,
        which can take minutes to run for queries matching thousands of products.

        Returns
        -------
        int
            The number of products matching a query.
        """
        for kw in ["order_by", "limit", "offset"]:
            # Allow these function arguments to be included for compatibility with query(),
            # but ignore them.
            if kw in keywords:
                del keywords[kw]
        query = self.format_query(area, date, raw, area_relation, **keywords)
        _, total_count = self._load_query(query, limit=0)
        return total_count

    def _load_query(self, query, order_by=None, limit=None, offset=0):

        progress = self._tqdm(
            desc="正在查询产品",
            # initial=self.page_size,
            # total=max_offset - offset,
            unit="个",
        )
        nextLink = ''
        products = []
        count = 0
        while nextLink is not None and offset < 10000:
            product, nextLink = self._load_subquery(query, order_by, limit, offset)
            count += len(product)
            offset = count

            progress.update(len(product))
            products.extend(product)
        progress.close()

        if count >= 10000:
            self.logger.info('检索数据文件超过10000个，超出限制，请重置参数或者减小研究区范围')
        return products, count

    def _load_subquery(self, query, order_by=None, limit=None, offset=0):
        # store last query (for testing)
        self._last_query = query
        self.logger.debug("Sub-query: offset=%s, limit=%s", offset, limit)

        # load query results
        url = self._format_url(query, order_by, limit, offset)
        self.logger.debug('产品请求地址【%s】' %(url))

        # Unlike POST, DHuS only accepts latin1 charset in the GET params
        with self.dl_limit_semaphore:
            # response = self.session.get(url, params={"q": query.encode("latin1")})
            response = self.session.get(url)
        self._check_scihub_response(response, query_string=query)

        # store last status code (for testing)
        self._last_response = response

        # parse response content
        try:
            if '@odata.nextLink' in response.json() :
                nextLink = response.json()["@odata.nextLink"]
            else:
                nextLink = None
            json_feed = response.json()["value"]
            if "error" in json_feed:
                message = json_feed["error"]["message"]
                message = message.replace("org.apache.solr.search.SyntaxError: ", "")
                raise QuerySyntaxError(message, response)
            # total_results = int(json_feed["opensearch:totalResults"])
        except (ValueError, KeyError):
            raise ServerError("API response not valid. JSON decoding failed.", response)

        products = json_feed
        # this verification is necessary because if the query returns only
        # one product, self.products will be a dict not a list
        if isinstance(products, dict):
            products = [products]

        products = self._parse_odata_response(products)


        return products, nextLink

    def _format_url(self, query, order_by=None, limit=None, offset=0):  # TODO 根据最新版本更新API
        if limit is None:
            limit = self.page_size
        limit = min(limit, self.page_size)
        url = ''
        url += "&$top={}".format(limit)
        url += "&$skip={}".format(offset)
        if order_by :
            url += "&$orderby=%s" %(order_by)

        return URL_SEARCH + f"odata/v1/Products?$filter=" + query + url

    @staticmethod
    def to_geojson(products):
        """Return the products from a query response as a GeoJSON with the values in their
        appropriate Python types.
        """
        feature_list = []
        for i, (product_id, props) in enumerate(products.items()):
            props = props.copy()
            props["id"] = product_id
            poly = geomet.wkt.loads(props["footprint"])
            del props["footprint"]
            del props["gmlfootprint"]
            # Fix "'datetime' is not JSON serializable"
            for k, v in props.items():
                if isinstance(v, (date, datetime)):
                    props[k] = v.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
            feature_list.append(geojson.Feature(geometry=poly, id=i, properties=props))
        return geojson.FeatureCollection(feature_list)

    @staticmethod
    def to_dataframe(products):
        """Return the products from a query response as a Pandas DataFrame
        with the values in their appropriate Python types.
        """
        try:
            import pandas as pd
        except ImportError:
            raise ImportError("to_dataframe requires the optional dependency Pandas.")

        return pd.DataFrame.from_dict(products, orient="index")


    def to_geodataframe(self, products):
        """Return the products from a query response as a GeoPandas GeoDataFrame
        with the values in their appropriate Python types.
        """
        try:
            import geopandas as gpd
            import shapely.wkt
        except ImportError:
            raise ImportError(
                "to_geodataframe requires the optional dependencies GeoPandas and Shapely."
            )

        crs = "EPSG:4326"  # WGS84
        if len(products) == 0:
            return gpd.GeoDataFrame(crs=crs, geometry=[])

        df = self.to_dataframe(products)
        geometry = [shapely.wkt.loads(fp) for fp in df["footprint"]]
        # remove useless columns
        df.drop(["footprint", "gmlfootprint"], axis=1, inplace=True)
        return gpd.GeoDataFrame(df, crs=crs, geometry=geometry)

    def get_product_odata(self, id, full=False):
        """Access OData API to get info about a product.

        Returns a dict containing the id, title, size, md5sum, date, footprint and download url
        of the product. The date field corresponds to the Start ContentDate value.

        If `full` is set to True, then the full, detailed metadata of the product is returned
        in addition to the above.

        Parameters
        ----------
        id : string
            The UUID of the product to query
        full : bool
            Whether to get the full metadata for the Product. False by default.

        Returns
        -------
        dict[str, Any]
            A dictionary with an item for each metadata attribute

        Notes
        -----
        For a full list of mappings between the OpenSearch (Solr) and OData attribute names
        see the following definition files:
        https://github.com/SentinelDataHub/DataHubSystem/blob/master/addon/sentinel-1/src/main/resources/META-INF/sentinel-1.owl
        https://github.com/SentinelDataHub/DataHubSystem/blob/master/addon/sentinel-2/src/main/resources/META-INF/sentinel-2.owl
        https://github.com/SentinelDataHub/DataHubSystem/blob/master/addon/sentinel-3/src/main/resources/META-INF/sentinel-3.owl
        """
        # 'https://catalogue.dataspace.copernicus.eu/odata/v1/Products(db0c8ef3-8ec0-5185-a537-812dad3c58f8)/$value'
        # url = self._get_odata_url(id, "?$format=json")
        url = self._get_nodes_url(id)
        if full:
            url += "&$expand=Attributes"
        with self.dl_limit_semaphore:
            response = self.session.get(url)
        self._check_scihub_response(response)
        values = self._parse_odata_response(response.json())
        if values["title"].startswith("S3"):
            values["manifest_name"] = "xfdumanifest.xml"
            values["product_root_dir"] = values["title"] + ".SEN3"
        else:
            values["manifest_name"] = "manifest.safe"
            # values["product_root_dir"] = values["title"] + ".SAFE"
        values["url"] = self._get_download_url(id)
        values["quicklook_url"] = self._get_odata_url(id, "/Products('Quicklook')/$value")
        return values

    def is_online(self, id):
        """Returns whether a product is online

        Parameters
        ----------
        id : string
            UUID of the product, e.g. 'a8dd0cfd-613e-45ce-868c-d79177b916ed'

        Returns
        -------
        bool
            True if online, False if in LTA

        See Also
        --------
        :meth:`SentinelAPI.trigger_offline_retrieval()`
        """
        # Check https://scihub.copernicus.eu/userguide/ODataAPI#Products_entity for more information

        if not self._online_attribute_used:
            return True
        url = self._get_odata_url(id, "/Online/$value")
        with self.dl_limit_semaphore:
            r = self.session.get(url)
        try:
            self._check_scihub_response(r)
        except ServerError as e:
            # Handle DHuS versions that do not set the Online attribute
            if "Could not find property with name: 'Online'" in e.msg:
                self._online_attribute_used = False
                return True
            raise
        return r.json()



    def _get_filename(self, product_info):

        return product_info['Name'] + '.zip'

        if product_info["Online"]:
            with self.dl_limit_semaphore:
                req = self.session.head(product_info["url"])
            self._check_scihub_response(req, test_json=False)
            cd = req.headers.get("Content-Disposition")
            if cd is not None:
                filename = cd.split("=", 1)[1].strip('"')
                return filename
        with self.dl_limit_semaphore:
            req = self.session.get(
                product_info["url"].replace("$value", "Attributes('Filename')/Value/$value")
            )
        self._check_scihub_response(req, test_json=False)
        filename = req.text
        # This should cover all currently existing file types: .SAFE, .SEN3, .nc and .EOF
        filename = filename.replace(".SAFE", ".zip")
        filename = filename.replace(".SEN3", ".zip")
        return filename

    def trigger_offline_retrieval(self, uuid):
        """Triggers retrieval of an offline product from the Long Term Archive.

        Parameters
        ----------
        uuid : string
            UUID of the product

        Returns
        -------
        bool
            True, if the product retrieval was successfully triggered.
            False, if the product is already online.

        Raises
        ------
        LTAError
            If the request was not accepted due to exceeded user quota or server overload.
        ServerError
            If an unexpected response was received from server.
        UnauthorizedError
            If the provided credentials were invalid.

        Notes
        -----
        https://scihub.copernicus.eu/userguide/LongTermArchive
        """
        return self.downloader.trigger_offline_retrieval(uuid)

    def download_all(
            self,
            products,
            directory_path=".",
            max_attempts=10,
            checksum=True,
            n_concurrent_dl=None,
            lta_retry_delay=None,
            fail_fast=False,
            nodefilter=None,
    ):
        """Download a list of products.

        Takes a list of product IDs as input. This means that the return value of query() can be
        passed directly to this method.

        File names on the server are used for the downloaded files, e.g.
        "S1A_EW_GRDH_1SDH_20141003T003840_20141003T003920_002658_002F54_4DD1.zip".

        In case of interruptions or other exceptions, downloading will restart from where it left
        off. Downloading is attempted at most max_attempts times to avoid getting stuck with
        unrecoverable errors.

        Parameters
        ----------
        products : list
            List of product IDs
        directory_path : string
            Directory where the downloaded files will be downloaded
        max_attempts : int, default 10
            Number of allowed retries before giving up downloading a product.
        checksum : bool, default True
            If True, verify the downloaded files' integrity by checking its MD5 checksum.
            Throws InvalidChecksumError if the checksum does not match.
            Defaults to True.
        n_concurrent_dl : integer, optional
            Number of concurrent downloads. Defaults to :attr:`SentinelAPI.concurrent_dl_limit`.
        lta_retry_delay : float, default 60
            Number of seconds to wait between requests to the Long Term Archive.
        fail_fast : bool, default False
            if True, all other downloads are cancelled when one of the downloads fails.
        nodefilter : callable, optional
            The callable is used to select which files of each product will be downloaded.
            If None (the default), the full products will be downloaded.
            See :mod:`sentinelsat.products` for sample node filters.

        Notes
        -----
        By default, raises the most recent downloading exception if all downloads failed.
        If ``fail_fast`` is set to True, raises the encountered exception on the first failed
        download instead.

        Returns
        -------
        dict[string, dict]
            A dictionary containing the return value from download() for each successfully
            downloaded product.
        dict[string, dict]
            A dictionary containing the product information for products successfully
            triggered for retrieval from the long term archive but not downloaded.
        dict[string, dict]
            A dictionary containing the product information of products where either
            downloading or triggering failed. "exception" field with the exception info
            is included to the product info dict.
        """
        downloader = copy(self.downloader)
        downloader.verify_checksum = checksum
        downloader.fail_fast = fail_fast
        downloader.max_attempts = max_attempts
        if n_concurrent_dl:
            downloader.n_concurrent_dl = n_concurrent_dl
        if lta_retry_delay:
            downloader.lta_retry_delay = lta_retry_delay
        downloader.node_filter = nodefilter
        statuses, exceptions, product_infos = downloader.download_all(products, directory_path)

        # Adapt results to the old download_all() API
        downloaded_prods = {}
        retrieval_triggered = {}
        failed_prods = {}
        for pid, status in statuses.items():
            if pid not in product_infos:
                product_infos[pid] = {}
            if pid in exceptions:
                product_infos[pid]["exception"] = exceptions[pid]
            if status == DownloadStatus.DOWNLOADED:
                downloaded_prods[pid] = product_infos[pid]
            elif status == DownloadStatus.TRIGGERED:
                retrieval_triggered[pid] = product_infos[pid]
            else:
                failed_prods[pid] = product_infos[pid]
        ResultTuple = namedtuple("ResultTuple", ["downloaded", "retrieval_triggered", "failed"])
        return ResultTuple(downloaded_prods, retrieval_triggered, failed_prods)

    def download_all_quicklooks(self, products, directory_path=".", n_concurrent_dl=4):
        """Download quicklook for a list of products.

        Takes a dict of product IDs: product data as input. This means that the return value of
        query() can be passed directly to this method.

        File names on the server are used for the downloaded images, e.g.
        "S2A_MSIL1C_20200924T104031_N0209_R008_T35WMV_20200926T135405.jpeg".

        Parameters
        ----------
        products : dict
            Dict of product IDs, product data
        directory_path : string
            Directory where the downloaded images will be downloaded
        n_concurrent_dl : integer
            Number of concurrent downloads

        Returns
        -------
        dict[string, dict]
            A dictionary containing the return value from download_quicklook() for each
            successfully downloaded quicklook
        dict[string, dict]
            A dictionary containing the error of products where either
            quicklook was not available or it had an unexpected content type
        """
        downloader = copy(self.downloader)
        downloader.n_concurrent_dl = n_concurrent_dl
        return downloader.download_all_quicklooks(products, directory_path)

    def download_quicklook(self, id, directory_path="."):
        """Download a quicklook for a product.

        Uses the filename on the server for the downloaded image name, e.g.
        "S1A_EW_GRDH_1SDH_20141003T003840_20141003T003920_002658_002F54_4DD1.jpeg".

        Already downloaded images are skipped.

        Parameters
        ----------
        id : string
            UUID of the product, e.g. 'a8dd0cfd-613e-45ce-868c-d79177b916ed'
        directory_path : string, optional
            Where the image will be downloaded

        Returns
        -------
        quicklook_info : dict
            Dictionary containing the quicklooks's response headers as well as the path on disk.
        """
        return self.downloader.download_quicklook(id, directory_path)

    @staticmethod
    def get_products_size(products):
        """Return the total file size in GB of all products in the OpenSearch response."""
        size_total = 0
        for title, props in products.items():
            size_product = props["size"]
            size_value = float(size_product.split(" ")[0])
            size_unit = str(size_product.split(" ")[1])
            if size_unit == "MB":
                size_value /= 1024.0
            if size_unit == "KB":
                size_value /= 1024.0 * 1024.0
            size_total += size_value
        return round(size_total, 2)

    @staticmethod
    def check_query_length(query):
        """Determine whether a query to the OpenSearch API is too long.

        The length of a query string is limited to approximately 3898 characters but
        any special characters (that is, not alphanumeric or -_.*) will take up more space.

        Parameters
        ----------
        query : str
            The query string

        Returns
        -------
        float
            Ratio of the query length to the maximum length
        """
        # The server uses the Java's URLEncoder implementation internally, which we are replicating here
        effective_length = len(quote_plus(query, safe="-_.*").replace("~", "%7E"))

        return effective_length / 3898

    def _query_names(self, names):
        """Find products by their names, e.g.
        S1A_EW_GRDH_1SDH_20141003T003840_20141003T003920_002658_002F54_4DD1.

        Note that duplicates exist on server, so multiple products can be returned for each name.

        Parameters
        ----------
        names : list[string]
            List of product names.

        Returns
        -------
        dict[string, dict[str, dict]]
            A dictionary mapping each name to a dictionary which contains the products with
            that name (with ID as the key).
        """
        products = {}
        for name in names:
            products.update(self.query(identifier=name))

        # Group the products
        output = OrderedDict((name, dict()) for name in names)
        for id, metadata in products.items():
            name = metadata["identifier"]
            output[name][id] = metadata

        return output

    def check_files(self, paths=None, ids=None, directory=None, delete=False):
        """Verify the integrity of product files on disk.

        Integrity is checked by comparing the size and checksum of the file with the respective
        values on the server.

        The input can be a list of products to check or a list of IDs and a directory.

        In cases where multiple products with different IDs exist on the server for given product
        name, the file is considered to be correct if any of them matches the file size and
        checksum. A warning is logged in such situations.

        The corrupt products' OData info is included in the return value to make it easier to
        re-download the products, if necessary.

        Parameters
        ----------
        paths : list[string]
            List of product file paths.
        ids : list[string]
            List of product IDs.
        directory : string
            Directory where the files are located, if checking based on product IDs.
        delete : bool
            Whether to delete corrupt products. Defaults to False.

        Returns
        -------
        dict[str, list[dict]]
            A dictionary listing the invalid or missing files. The dictionary maps the corrupt
            file paths to a list of OData dictionaries of matching products on the server (as
            returned by :meth:`SentinelAPI.get_product_odata()`).
        """
        if not ids and not paths:
            raise ValueError("Must provide either file paths or product IDs and a directory")
        if ids and not directory:
            raise ValueError("Directory value missing")
        if directory is not None:
            directory = Path(directory)
        paths = [Path(p) for p in paths] if paths else []
        ids = ids or []

        # Get product IDs corresponding to the files on disk
        names = []
        if paths:
            names = [p.stem for p in paths]
            result = self._query_names(names)
            for product_dicts in result.values():
                ids += list(product_dicts)
        names_from_paths = set(names)
        ids = set(ids)

        # Collect the OData information for each product
        # Product name -> list of matching odata dicts
        product_infos = defaultdict(list)
        for id in ids:
            odata = self.get_product_odata(id)
            name = odata["title"]
            product_infos[name].append(odata)

            # Collect
            if name not in names_from_paths:
                paths.append(directory / self._get_filename(odata))

        # Now go over the list of products and check them
        corrupt = {}
        for path in paths:
            name = path.stem

            if len(product_infos[name]) > 1:
                self.logger.warning("%s matches multiple products on server", path)

            if not path.exists():
                # We will consider missing files as corrupt also
                self.logger.info("%s does not exist on disk", path)
                corrupt[str(path)] = product_infos[name]
                continue

            is_fine = False
            for product_info in product_infos[name]:
                if path.stat().st_size == product_info["size"] and self._checksum_compare(
                        path, product_info
                ):
                    is_fine = True
                    break
            if not is_fine:
                self.logger.info("%s is corrupt", path)
                corrupt[str(path)] = product_infos[name]
                if delete:
                    path.unlink()

        return corrupt

    def _checksum_compare(self, file_path, product_info, block_size=2**13):
        """Compare a given MD5 checksum with one calculated from a file."""
        if "sha3-256" in product_info:
            checksum = product_info["sha3-256"]
            algo = hashlib.sha3_256()
        elif "md5" in product_info:
            checksum = product_info["md5"][0]
            algo = hashlib.md5()
        else:
            raise InvalidChecksumError("No checksum information found in product information.")
        file_path = Path(file_path)
        file_size = file_path.stat().st_size
        with self._tqdm(
                desc=f"{algo.name.upper()} checksumming",
                total=file_size,
                unit="B",
                unit_scale=True,
                leave=False,
        ) as progress:
            with open(file_path, "rb") as f:
                while True:
                    block_data = f.read(block_size)
                    if not block_data:
                        break
                    algo.update(block_data)
                    progress.update(len(block_data))
            return algo.hexdigest().lower() == checksum.lower()

    def _tqdm(self, **kwargs):
        """tqdm progressbar wrapper. May be overridden to customize progressbar behavior"""
        kwargs.update({"disable": not self.show_progressbars})
        return tqdm(**kwargs)

    def get_stream(self, id, **kwargs):
        """Exposes requests response ready to stream product to e.g. S3.

        Parameters
        ----------
        id : string
            UUID of the product, e.g. 'a8dd0cfd-613e-45ce-868c-d79177b916ed'
        **kwargs
            Any additional parameters for :func:`requests.get()`

        Raises
        ------
        LTATriggered
            If the product has been archived and its retrieval was successfully triggered.
        LTAError
            If the product has been archived and its retrieval failed.

        Returns
        -------
        requests.Response:
            Opened response object
        """
        return self.downloader.get_stream(id, **kwargs)

    def _get_odata_url(self, uuid, suffix=""):
        return URL_SEARCH + f"odata/v1/Products({uuid})" + suffix

    def _get_nodes_url(self, uuid):
        return URL_DOWNLOAD + f"odata/v1/Products({uuid})" + "/Nodes"

    def _get_download_url(self, uuid):
        # return URL_DOWNLOAD + f"odata/v1/Products({uuid})" + "/$zip"
        return URL_DOWNLOAD + f"odata/v1/Products({uuid})" + "/$value"

    def _check_scihub_response(self, response, test_json=True, query_string=None):
        """Check that the response from server has status code 2xx and that the response is valid JSON."""
        # Prevent requests from needing to guess the encoding
        # SciHub appears to be using UTF-8 in all of their responses
        response.encoding = "utf-8"
        try:
            response.raise_for_status()
            if test_json:
                response.json()
        except (requests.HTTPError, ValueError):
            msg = None
            try:
                msg = response.json()["error"]["message"]["value"]
            except Exception:
                try:
                    msg = response.headers["cause-message"]
                except Exception:
                    if not response.text.lstrip().startswith("{"):
                        try:
                            h = html2text.HTML2Text()
                            h.ignore_images = True
                            h.ignore_anchors = True
                            msg = h.handle(response.text).strip()
                        except Exception:
                            pass

            if msg is None:
                raise ServerError("Invalid API response", response)
            elif response.status_code == 401:
                msg = "Invalid user name or password"
                if "apihub.copernicus.eu/apihub" in response.url:
                    msg += (
                        ". Note that account creation and password changes may take up to a week "
                        "to propagate to the 'https://documentation.dataspace.copernicus.eu/' API URL you are using. "
                        "Consider switching to 'https://dataspace.copernicus.eu/' instead in the mean time."
                    )
                raise UnauthorizedError(msg, response)
            elif "Request Entity Too Large" in msg or "Request-URI Too Long" in msg:
                msg = "Server was unable to process the query due to its excessive length"
                if query_string is not None:
                    length = self.check_query_length(query_string)
                    msg += (
                        " (approximately {:.3}x times the maximum allowed). "
                        "Consider using SentinelAPI.check_query_length() for "
                        "client-side validation of the query string length.".format(length)
                    )
                raise QueryLengthError(msg, response) from None
            elif "Invalid key" in msg:
                msg = msg.split(" : ", 1)[-1]
                raise InvalidKeyError(msg, response)
            elif 500 <= response.status_code < 600 or msg:
                # 5xx: Server Error
                raise ServerError(msg, response)
            else:
                raise SentinelAPIError(msg, response)

    def _path_to_url(self, product_info, path, urltype=None):
        id = product_info["id"]
        root_dir = product_info["product_root_dir"]
        path = "/".join(["Nodes('{}')".format(item) for item in path.split("/")])
        if urltype == "value":
            urltype = "/$value"
        elif urltype == "json":
            urltype = "?$format=json"
        elif urltype == "full":
            urltype = "?$format=json&$expand=Attributes"
        elif urltype is None:
            urltype = ""
        # else: pass urltype as is
        return self._get_odata_url(id, f"/Nodes('{root_dir}')/{path}{urltype}")

    def _get_manifest(self, product_info, path=None):
        path = Path(path) if path else None
        manifest_name = product_info["manifest_name"]
        url = self._path_to_url(product_info, manifest_name, "value")
        node_info = product_info.copy()
        node_info["url"] = url
        node_info["node_path"] = f"./{manifest_name}"
        del node_info["md5"]

        if path and path.exists():
            self.logger.debug("Manifest file already available (%s), skipping download", path)
            data = path.read_bytes()
            node_info["size"] = len(data)
            return node_info, data

        url = self._path_to_url(product_info, manifest_name, "json")
        with self.dl_limit_semaphore:
            response = self.session.get(url)
        self._check_scihub_response(response)
        info = response.json()["d"]

        node_info["size"] = int(info["ContentLength"])
        with self.dl_limit_semaphore:
            response = self.session.get(node_info["url"])
        self._check_scihub_response(response, test_json=False)
        data = response.content
        if len(data) != node_info["size"]:
            raise SentinelAPIError("File corrupt: data length do not match")

        if path:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)

        return node_info, data


    def read_geojson(self, geojson_file):
        """Read a GeoJSON file into a GeoJSON object."""
        with open(geojson_file) as f:
            return geojson.load(f)


    def geojson_to_wkt(self, geojson_obj, decimals=4):
        """Convert a GeoJSON object to Well-Known Text. Intended for use with OpenSearch queries.
        3D points are converted to 2D.

        Parameters
        ----------
        geojson_obj : dict
            a GeoJSON object
        decimals : int, optional
            Number of decimal figures after point to round coordinate to. Defaults to 4 (about 10
            meters).

        Returns
        -------
        str
            Well-Known Text string representation of the geometry
        """
        if "coordinates" in geojson_obj:
            geometry = geojson_obj
        elif "geometry" in geojson_obj:
            geometry = geojson_obj["geometry"]
        else:
            geometry = {"type": "GeometryCollection", "geometries": []}
            for feature in geojson_obj["features"]:
                geometry["geometries"].append(feature["geometry"])

        def ensure_2d(geometry):
            if isinstance(geometry[0], (list, tuple)):
                return list(map(ensure_2d, geometry))
            else:
                return geometry[:2]

        def check_bounds(geometry):
            if isinstance(geometry[0], (list, tuple)):
                return list(map(check_bounds, geometry))
            else:
                if geometry[0] > 180 or geometry[0] < -180:
                    raise ValueError("Longitude is out of bounds, check your JSON format or data")
                if geometry[1] > 90 or geometry[1] < -90:
                    raise ValueError("Latitude is out of bounds, check your JSON format or data")

        # Discard z-coordinate, if it exists
        if geometry["type"] == "GeometryCollection":
            for idx, geo in enumerate(geometry["geometries"]):
                geometry["geometries"][idx]["coordinates"] = ensure_2d(geo["coordinates"])
                check_bounds(geo["coordinates"])
        else:
            geometry["coordinates"] = ensure_2d(geometry["coordinates"])
            check_bounds(geometry["coordinates"])

        wkt = geomet.wkt.dumps(geometry, decimals=decimals)
        # Strip unnecessary spaces
        wkt = re.sub(r"(?<!\d) ", "", wkt)
        return wkt

    def _format_query_value(self, attr, value):
        """Format the value of a Solr query parameter."""

        # Handle spaces by adding quotes around the string, if appropriate
        if isinstance(value, str):
            value = value.strip()
            if value == "":
                raise ValueError(f"Trying to filter '{attr}' with an empty string")
            # Handle strings surrounded by brackets specially to allow the user to make use of Solr syntax directly.
            # The string must not be quoted for that to work.
            if (
                    not any(
                        value.startswith(s[0]) and value.endswith(s[1])
                        for s in ["[]", "{}", "//", "()", '""']
                    )
                    and "*" not in value
                    and "?" not in value
            ):
                value = re.sub(r"\s", " ", value, re.M)
                value = f'"{value}"'

        # Handle date keywords
        # Keywords from https://github.com/SentinelDataHub/DataHubSystem/search?q=text/date+iso8601
        is_date_attr = attr.lower() in [
            "beginposition",
            "endposition",
            "date",
            "creationdate",
            "ingestiondate",
        ]
        if is_date_attr:
            # Automatically format date-type attributes
            if isinstance(value, str) and " TO " in value:
                # This is a string already formatted as a date interval,
                # e.g. '[NOW-1DAY TO NOW]'
                pass
            elif isinstance(value, (list, tuple)) and len(value) == 2:
                value = (self.format_query_date(value[0]), self.format_query_date(value[1]))
            else:
                raise ValueError(
                    f"Date-type query parameter '{attr}' expects either a two-element tuple of "
                    f"str or datetime objects or a '[<from> TO <to>]'-format string. Received {value}."
                )

        if isinstance(value, set):
            raise ValueError(f"Unexpected set-type value encountered with keyword '{attr}'")
        elif isinstance(value, (list, tuple)):
            # Handle value ranges
            if len(value) == 2:
                # Allow None or "*" to be used as an unlimited bound
                if any(x == "" for x in value):
                    raise ValueError(f"Trying to filter '{attr}' with an empty string")
                value = ["*" if x in (None, "*") else f'"{x}"' for x in value]
                if value == ["*", "*"] or (is_date_attr and value == ["*", "NOW"]):
                    # Drop this keyword if both sides are unbounded
                    return
                value = "[{} TO {}]".format(*value)
            else:
                raise ValueError(
                    f"Invalid number of elements in list. Expected 2, received {len(value)}"
                )
        return value

    def format_query_date(self, in_date):
        r"""
        Format a date, datetime or a YYYYMMDD string input as YYYY-MM-DDThh:mm:ssZ
        or validate a date string as suitable for the full text search interface and return it.

        `None` will be converted to '\*', meaning an unlimited date bound in date ranges.

        Parameters
        ----------
        in_date : str or datetime or date or None
            Date to be formatted

        Returns
        -------
        str
            Formatted string

        Raises
        ------
        ValueError
            If the input date type is incorrect or passed date string is invalid
        """
        if in_date is None:
            return "*"
        if isinstance(in_date, (datetime, date)):
            return in_date.strftime("%Y-%m-%dT%H:%M:%SZ")
        elif not isinstance(in_date, str):
            raise ValueError("Expected a string or a datetime object. Received {}.".format(in_date))

        in_date = in_date.strip()
        if in_date == "*":
            # '*' can be used for one-sided range queries e.g. ingestiondate:[* TO NOW-1YEAR]
            return in_date

        # Reference: https://cwiki.apache.org/confluence/display/solr/Working+with+Dates

        # ISO-8601 date or NOW
        valid_date_pattern = r"^(?:\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(?:\.\d+)?Z|NOW)"
        # date arithmetic suffix is allowed
        units = r"(?:YEAR|MONTH|DAY|HOUR|MINUTE|SECOND)"
        valid_date_pattern += r"(?:[-+]\d+{}S?)*".format(units)
        # dates can be rounded to a unit of time
        # e.g. "NOW/DAY" for dates since 00:00 today
        valid_date_pattern += r"(?:/{}S?)*$".format(units)
        in_date = in_date.strip()
        if re.match(valid_date_pattern, in_date):
            return in_date

        try:
            return datetime.strptime(in_date, "%Y%m%d").strftime("%Y-%m-%dT%H:%M:%SZ")
        except ValueError:
            raise ValueError("Unsupported date value {}".format(in_date))

    def _format_order_by(self, order_by):
        '''
        The acceptable arguments for this option: ContentDate/Start, ContentDate/End, PublicationDate, ModificationDate,
        in directions: asc, desc.
        '''
        if not order_by or not order_by.strip():
            return None
        output = []
        for part in order_by.split(","):
            part = part.strip()
            dir = " asc"
            if part[0] == "+":
                part = part[1:]
            elif part[0] == "-":
                dir = " desc"
                part = part[1:]

            if part not in ['ContentDate/Start',
                            'ContentDate/End',
                            'PublicationDate',
                            'ModificationDate'] :
                continue
            # if not part or not part.isalnum():
            #     raise ValueError("Invalid order by value ({})".format(order_by))
            output.append(part + dir)
        return ",".join(output)

    def _parse_gml_footprint(self, geometry_str):
        # workaround for https://github.com/sentinelsat/sentinelsat/issues/286
        if geometry_str is None:  # pragma: no cover
            return None
        geometry_xml = ET.fromstring(geometry_str)
        poly_coords_str = (
            geometry_xml.find("{http://www.opengis.net/gml}outerBoundaryIs")
            .find("{http://www.opengis.net/gml}LinearRing")
            .findtext("{http://www.opengis.net/gml}coordinates")
        )
        poly_coords = (coord.split(",")[::-1] for coord in poly_coords_str.split(" "))
        coord_string = ",".join(" ".join(coord) for coord in poly_coords)
        return "POLYGON(({}))".format(coord_string)


    def _parse_iso_date(self, content):
        if "." in content:
            return datetime.strptime(content, "%Y-%m-%dT%H:%M:%S.%fZ")
        else:
            return datetime.strptime(content, "%Y-%m-%dT%H:%M:%SZ")


    def _parse_odata_timestamp(self, in_date):
        """Convert the timestamp received from OData JSON API to a datetime object."""
        timestamp = int(in_date.replace("/Date(", "").replace(")/", ""))
        seconds = timestamp // 1000
        ms = timestamp % 1000
        return datetime.utcfromtimestamp(seconds) + timedelta(milliseconds=ms)


    def _parse_opensearch_response(self, products):
        """Convert a query response to a dictionary.

        The resulting dictionary structure is {<product id>: {<property>: <value>}}.
        The property values are converted to their respective Python types unless `parse_values`
        is set to `False`.
        """

        converters = {"date": self._parse_iso_date, "int": int, "long": int, "float": float, "double": float}

        # Keep the string type by default
        def default_converter(x):
            return x

        output = OrderedDict()
        for prod in products:
            product_dict = {}
            prod_id = prod["Id"]
            output[prod_id] = product_dict
            for key in prod:
                # if key == "Id":
                #     continue
                product_dict[key] = prod[key]

                continue

                if isinstance(prod[key], str):
                    product_dict[key] = prod[key]
                else:
                    properties = prod[key]
                    if isinstance(properties, dict):
                        properties = [properties]
                    if key == "links":
                        for p in properties:
                            name = "link"
                            if "rel" in p:
                                name = "link_" + p["rel"]
                            product_dict[name] = p["href"]
                    else:
                        f = converters.get(key, default_converter)
                        for p in properties:
                            if 'Name' not in p :
                                continue
                            try:
                                product_dict["name"] = f(p["Name"])
                            except KeyError:
                                # Sentinel-3 has one element 'arr'
                                # which violates the name:content convention
                                product_dict["name"] = f(p["Name"])
        return output


    def _parse_odata_response(self, products):

        outputs = []
        for product in products:
            # self._get_download_url(id)
            # output = {
            #     "id": product["Id"],
            #     "title": product["Name"],
            #     "size": int(product["ContentLength"]),
            #     # product["Checksum"]["Algorithm"].lower(): product["Checksum"]["Value"],
            #     # "date": _parse_odata_timestamp(product["ContentDate"]["Start"]),
            #     # "footprint": _parse_gml_footprint(product["ContentGeometry"]),
            #     # "url": product["__metadata"]["media_src"],
            #     # "Online": product.get("Online", True),
            #     # "Creation Date": _parse_odata_timestamp(product["CreationDate"]),
            #     # "Ingestion Date": _parse_odata_timestamp(product["IngestionDate"]),
            # }

            output = {
                "Id": product["Id"],
                "title": product["Name"],
                "Name": product["Name"],
                "size": int(product["ContentLength"]),

                "date": self._parse_iso_date(product["ContentDate"]["Start"]),
                # "footprint": _parse_gml_footprint(product["ContentGeometry"]),
                # "footprint": _parse_gml_footprint(product["Footprint"]),
                # "url": product["__metadata"]["media_src"],
                "Online": product.get("Online", True),
                # "Creation Date": _parse_iso_date(product["CreationDate"]),
                # "Ingestion Date": _parse_iso_date(product["IngestionDate"]),
            }
            for item in product["Checksum"] :
                if not 'Algorithm' in item :
                    continue
                output[item["Algorithm"].lower()] = item["Value"],


            # Parse the extended metadata, if provided
            # converters = [int, float, _parse_iso_date]
            # for attr in product["Attributes"].get("results", []):
            #     value = attr["Value"]
            #     for f in converters:
            #         try:
            #             value = f(attr["Value"])
            #             break
            #         except ValueError:
            #             pass
            #     output[attr["Name"]] = value

            outputs.append(output)
        return outputs


    def placename_to_wkt(self, place_name):
        """Geocodes the place name to rectangular bounding extents using Nominatim API and
           returns the corresponding 'ENVELOPE' form Well-Known-Text.

        Parameters
        ----------
        place_name : str
            the query to geocode

        Raises
        ------
        ValueError
            If no matches to the place name were found.

        Returns
        -------
        wkt_envelope : str
            Bounding box of the location as an 'ENVELOPE(minX, maxX, maxY, minY)' WKT string.
        info : Dict[str, any]
            Matched location's metadata returned by Nominatim.
        """
        rqst = requests.get(
            "https://nominatim.openstreetmap.org/search",
            params={"q": place_name, "format": "geojson"},
            headers={"User-Agent": "sentinelsat/" + sentinelsat_version},
        )
        rqst.raise_for_status()
        features = rqst.json()["features"]
        if len(features) == 0:
            raise ValueError('Unable to find a matching location for "{}"'.format(place_name))
        # Get the First result's bounding box and description.
        feature = features[0]
        minX, minY, maxX, maxY = feature["bbox"]
        # ENVELOPE is a non-standard WKT format supported by Solr
        # https://lucene.apache.org/solr/guide/6_6/spatial-search.html#SpatialSearch-BBoxField
        wkt_envelope = "ENVELOPE({}, {}, {}, {})".format(minX, maxX, maxY, minY)
        info = feature["properties"]
        info["bbox"] = feature["bbox"]
        return wkt_envelope, info


    def is_wkt(self, possible_wkt):
        pattern = r"^((MULTI)?(POINT|LINESTRING|POLYGON)|GEOMETRYCOLLECTION|ENVELOPE)\s*\(.+\)$"
        return re.match(pattern, possible_wkt.strip().upper()) is not None


class DownloadStatus(enum.Enum):
    """Status info for :meth:`Downloader.download_all()`.

    Evaluates to True if status is :obj:`DOWNLOADED`.
    """

    UNAVAILABLE = enum.auto()
    OFFLINE = enum.auto()
    TRIGGERED = enum.auto()
    ONLINE = enum.auto()
    DOWNLOAD_STARTED = enum.auto()
    DOWNLOADED = enum.auto()

    def __bool__(self):
        return self == DownloadStatus.DOWNLOADED


class Downloader:
    """
    Manages downloading of products or parts of them.

    Intended for internal use, but may also be used directly if more fine-grained
    configuration or custom download logic is needed.

    Parameters
    ----------
    api : SentinelAPI
        A SentinelAPI instance.
    node_filter : callable, optional
        The callable is used to select which files of each product will be downloaded.
        If None (the default), the full products will be downloaded.
        See :mod:`sentinelsat.products` for sample node filters.
    verify_checksum : bool, default True
        If True, verify the downloaded files' integrity by checking its checksum.
        Throws InvalidChecksumError if the checksum does not match.
    fail_fast : bool, default False
        if True, all other downloads are cancelled when one of the downloads fails in :meth:`download_all()`.
    n_concurrent_dl : integer, optional
        Number of concurrent downloads.
        Defaults to the maximum allowed by :attr:`SentinelAPI.concurrent_dl_limit`.
    max_attempts : int, default 10
        Number of allowed retries before giving up downloading a product in :meth:`download_all()`.
    dl_retry_delay : float, default 10
        Number of seconds to wait between retrying of failed downloads.
    lta_retry_delay : float, default 60
        Number of seconds to wait between requests to the Long Term Archive.
    lta_timeout : float, optional
        Maximum number of seconds to wait for triggered products to come online.
        Defaults to no timeout.
    """

    def __init__(
            self,
            api,
            *,
            node_filter=None,
            verify_checksum=True,
            fail_fast=False,
            n_concurrent_dl=None,
            max_attempts=10,
            dl_retry_delay=10,
            lta_retry_delay=60,
            lta_timeout=None,
            token=None
    ):
        # from lb_toolkits.utils.sentinel import SentinelAPI

        self.api = api
        self.logger = self.api.logger
        self._tqdm = self.api._tqdm

        self.node_filter = node_filter
        self.verify_checksum = verify_checksum
        self.fail_fast = fail_fast
        self.max_attempts = max_attempts
        self.n_concurrent_dl = n_concurrent_dl or self.api.concurrent_dl_limit
        self.dl_retry_delay = dl_retry_delay
        self.lta_retry_delay = lta_retry_delay
        self.lta_timeout = lta_timeout
        self.chunk_size = 2**20  # download in 1 MB chunks by default
        self.token = token

    def download(self, product_info, directory=".", *, stop_event=None, skip_download=False):
        """Download a product.

        Parameters
        ----------
        product_info : string
            UUID of the product, e.g. 'a8dd0cfd-613e-45ce-868c-d79177b916ed'
        directory : string or Path, optional
            Where the file will be downloaded
        stop_event : threading.Event, optional
            An event object can be provided and set to interrupt the download.

        Returns
        -------
        product_info : dict
            Dictionary containing the product's info from get_product_odata() as well as
            the path on disk.

        Raises
        ------
        InvalidChecksumError
            If the checksum does not match the checksum on the server.
        LTATriggered
            If the product has been archived and its retrieval was successfully triggered.
        LTAError
            If the product has been archived and its retrieval failed.
        """

        id = product_info['Id']
        if self.node_filter:
            return self._download_with_node_filter(id, directory, stop_event)

        # product_info = self.api.get_product_odata(product_info)

        product_info["url"] = self.api._get_download_url(id)

        filename = self.api._get_filename(product_info)
        path = Path(directory) / filename
        product_info["path"] = str(path)
        product_info["downloaded_bytes"] = 0

        if skip_download :
            print('跳过下载【%s】' %(product_info["path"]))
            return product_info

        if path.exists():
            # We assume that the product has been downloaded and is complete
            return product_info

        # An incomplete download triggers the retrieval from the LTA if the product is not online
        # if not self.api.is_online(id):
        #     self.trigger_offline_retrieval(id)
        #     raise LTATriggered(id)

        self._download_common(product_info, path, stop_event, skip_download=skip_download)
        return product_info

    def _download_with_node_filter(self, id, directory, stop_event):
        product_info = self.api.get_product_odata(id)
        product_path = Path(directory) / (product_info["product_root_dir"])
        product_info["node_path"] = "./" + product_info["product_root_dir"]
        manifest_path = product_path / product_info["manifest_name"]
        if not manifest_path.exists() and self.trigger_offline_retrieval(id):
            raise LTATriggered(id)
        manifest_info, _ = self.api._get_manifest(product_info, manifest_path)
        product_info["nodes"] = {
            manifest_info["node_path"]: manifest_info,
        }
        node_infos = self._filter_nodes(manifest_path, product_info, self.node_filter)
        product_info["nodes"].update(node_infos)
        for node_info in node_infos.values():
            if stop_event and stop_event.is_set():
                raise concurrent.futures.CancelledError()
            node_path = node_info["node_path"]
            path = (product_path / node_path).resolve()
            node_info["path"] = path
            node_info["downloaded_bytes"] = 0

            self.logger.debug("Downloading %s node to %s", id, path)
            self.logger.debug("Node URL for %s: %s", id, node_info["url"])

            if path.exists():
                # We assume that the product node has been downloaded and is complete
                continue
            self._download_common(node_info, path, stop_event)
        return product_info

    def _download_common(self, product_info: Dict[str, Any], path: Path, stop_event, skip_download=False):
        # Use a temporary file for downloading

        temp_path = path.with_name(path.name + ".download")

        if temp_path.exists():
            size = temp_path.stat().st_size
            if size > product_info["size"]:
                self.logger.warning(
                    "Existing incomplete file %s is larger than the expected final size"
                    " (%s vs %s bytes). Deleting it.",
                    str(temp_path),
                    size,
                    product_info["size"],
                )
                temp_path.unlink()
            elif size == product_info["size"]:
                if self.verify_checksum and not self.api._checksum_compare(temp_path, product_info):
                    # Log a warning since this should never happen
                    self.logger.warning(
                        "Existing incomplete file %s appears to be fully downloaded but "
                        "its checksum is incorrect. Deleting it.",
                        str(temp_path),
                    )
                    temp_path.unlink()
                else:
                    skip_download = True
            else:
                # continue downloading
                self.logger.info(
                    "Download will resume from existing incomplete file %s.", temp_path
                )
                temp_path.unlink()

        if not skip_download:
            # Store the number of downloaded bytes for unit tests
            temp_path.parent.mkdir(parents=True, exist_ok=True)
            product_info["downloaded_bytes"] = self._download(
                product_info["url"],
                temp_path,
                product_info["size"],
                path.name,
                stop_event,
            )
        # Check integrity with MD5 checksum
        if self.verify_checksum is True:
            if not self.api._checksum_compare(temp_path, product_info):
                temp_path.unlink()
                raise InvalidChecksumError("File corrupt: checksums do not match")
        # Download successful, rename the temporary file to its proper name
        shutil.move(temp_path, path)
        return product_info

    def download_all(self, products, directory="."):
        """Download a list of products.

        Parameters
        ----------
        products : list
            List of product IDs
        directory : string or Path, optional
            Directory where the files will be downloaded

        Notes
        ------
        By default, raises the most recent downloading exception if all downloads failed.
        If :attr:`Downloader.fail_fast` is set to True, raises the encountered exception on the first failed
        download instead.

        Returns
        -------
        dict[string, DownloadStatus]
            The status of all products.
        dict[string, Exception]
            Exception info for any failed products.
        dict[string, dict]
            A dictionary containing the product information for each product
            (unless the product was unavailable).
        """

        ResultTuple = namedtuple("ResultTuple", ["statuses", "exceptions", "product_infos"])
        product_ids = list(set(products))
        assert self.n_concurrent_dl > 0
        if len(product_ids) == 0:
            return ResultTuple({}, {}, {})
        self.logger.info(
            "Will download %d products using %d workers", len(product_ids), self.n_concurrent_dl
        )

        statuses, online_prods, offline_prods, product_infos, exceptions = self._init_statuses(
            product_ids
        )

        # Skip already downloaded files.
        # Although the download method also checks, we do not need to retrieve such
        # products from the LTA and use up our quota.
        self._skip_existing_products(directory, offline_prods, product_infos, statuses, exceptions)

        stop_event = threading.Event()
        dl_tasks = {}
        trigger_tasks = {}

        # Two separate threadpools for downloading and triggering of retrieval.
        # Otherwise triggering might take up all threads and nothing is downloaded.
        dl_count = len(online_prods) + len(offline_prods)
        dl_executor = ThreadPoolExecutor(
            max_workers=max(1, min(self.n_concurrent_dl, dl_count)),
            thread_name_prefix="dl",
        )
        dl_progress = self._tqdm(
            total=dl_count,
            desc="Downloading products",
            unit="product",
        )
        if offline_prods:
            trigger_executor = ThreadPoolExecutor(
                max_workers=min(self.api.concurrent_lta_trigger_limit, len(offline_prods)),
                thread_name_prefix="trigger",
            )
            trigger_progress = self._tqdm(
                total=len(offline_prods),
                desc="LTA retrieval",
                unit="product",
                leave=True,
            )
        try:
            # First all online products are downloaded. Subsequently, offline products that might
            # have become available in the meantime are requested.
            for pid in itertools.chain(online_prods, offline_prods):
                future = dl_executor.submit(
                    self._download_online_retry,
                    product_infos[pid],
                    directory,
                    statuses,
                    exceptions,
                    stop_event,
                )
                dl_tasks[future] = pid

            for pid in offline_prods:
                future = trigger_executor.submit(
                    self._trigger_and_wait,
                    pid,
                    stop_event,
                    statuses,
                )
                trigger_tasks[future] = pid

            for task in concurrent.futures.as_completed(list(trigger_tasks) + list(dl_tasks)):
                pid = trigger_tasks.get(task) or dl_tasks[task]
                exception = exceptions.get(pid)
                if task.cancelled():
                    exception = concurrent.futures.CancelledError()
                if task.exception():
                    exception = task.exception()

                if task in dl_tasks:
                    if not exception:
                        product_infos[pid] = task.result()
                        statuses[pid] = DownloadStatus.DOWNLOADED
                    dl_progress.update()
                    # Keep the LTA progress fresh
                    if offline_prods:
                        trigger_progress.update(0)
                else:
                    trigger_progress.update()
                    if all(t.done() for t in trigger_tasks):
                        trigger_progress.close()

                if exception:
                    exceptions[pid] = exception
                    if self.fail_fast:
                        raise exception from None
                    else:
                        self.logger.error("%s failed: %s", pid, _format_exception(exception))
        except:
            stop_event.set()
            for t in list(trigger_tasks) + list(dl_tasks):
                t.cancel()
            raise
        finally:
            dl_executor.shutdown()
            dl_progress.close()
            if offline_prods:
                trigger_executor.shutdown()
                trigger_progress.close()

        if not any(statuses):
            if not exceptions:
                raise SentinelAPIError("Downloading all products failed for an unknown reason")
            exception = list(exceptions)[0]
            raise exception

        # Update Online status in product_infos
        for pid, status in statuses.items():
            if status in [DownloadStatus.OFFLINE, DownloadStatus.TRIGGERED]:
                product_infos[pid]["Online"] = False
            elif status != DownloadStatus.UNAVAILABLE:
                product_infos[pid]["Online"] = True

        return ResultTuple(statuses, exceptions, product_infos)

    def _init_statuses(self, product_ids):
        statuses = {pid: DownloadStatus.UNAVAILABLE for pid in product_ids}
        online_prods = set()
        offline_prods = set()
        product_infos = {}
        exceptions = {}
        # Get online status and product info.
        for pid in self._tqdm(
                iterable=product_ids, desc="Fetching archival status", unit="product", delay=2
        ):
            assert isinstance(pid, str)
            try:
                info = self.api.get_product_odata(pid)
            except UnauthorizedError:
                raise
            except SentinelAPIError as e:
                exceptions[pid] = e
                if self.fail_fast:
                    raise
                self.logger.error(
                    "Getting product info for %s failed, can't download: %s",
                    pid,
                    _format_exception(e),
                )
                continue
            product_infos[pid] = info
            if product_infos[pid]["Online"]:
                statuses[pid] = DownloadStatus.ONLINE
                online_prods.add(pid)
            else:
                statuses[pid] = DownloadStatus.OFFLINE
                offline_prods.add(pid)
        return statuses, online_prods, offline_prods, product_infos, exceptions

    def _skip_existing_products(self, directory, products, product_infos, statuses, exceptions):
        for pid in list(products):
            product_info = product_infos[pid]
            try:
                filename = self.api._get_filename(product_info)
            except SentinelAPIError as e:
                exceptions[pid] = e
                if self.fail_fast:
                    raise
                self.logger.error(
                    "Getting filename for %s (%s) failed: %s",
                    product_info["title"],
                    pid,
                    _format_exception(e),
                )
                continue
            path = Path(directory) / filename
            if path.exists():
                self.logger.info("Skipping already downloaded %s.", filename)
                product_info["path"] = str(path)
                statuses[pid] = DownloadStatus.DOWNLOADED
                products.remove(pid)
            else:
                self.logger.info(
                    "%s (%s) is in the LTA and retrieval will be triggered.",
                    product_info["title"],
                    pid,
                )

    def trigger_offline_retrieval(self, uuid):
        """Triggers retrieval of an offline product.

        Parameters
        ----------
        uuid : string
            UUID of the product

        Returns
        -------
        bool
            True, if the product retrieval was successfully triggered.
            False, if the product is already online.

        Raises
        ------
        LTAError
            If the request was not accepted due to exceeded user quota or server overload.
        ServerError
            If an unexpected response was received from server.
        UnauthorizedError
            If the provided credentials were invalid.

        Notes
        -----
        https://scihub.copernicus.eu/userguide/LongTermArchive
        """
        # Request just a single byte to avoid accidental downloading of the whole product.
        # Requesting zero bytes results in NullPointerException in the server.
        with self.api.dl_limit_semaphore:
            r = self.api.session.get(
                self.api._get_download_url(uuid), headers={"Range": "bytes=0-1"}
            )
        cause = r.headers.get("cause-message")
        # check https://scihub.copernicus.eu/userguide/LongTermArchive#HTTP_Status_codes
        if r.status_code in (200, 206):
            self.logger.debug("Product is online")
            return False
        elif r.status_code == 202:
            self.logger.debug("Accepted for retrieval")
            return True
        elif r.status_code == 403 and cause and "concurrent flows" in cause:
            # cause: 'An exception occured while creating a stream: Maximum number of 4 concurrent flows achieved by the user "username""'
            self.logger.debug("Product is online but concurrent downloads limit was exceeded")
            return False
        elif r.status_code == 403:
            # cause: 'User 'username' offline products retrieval quota exceeded (20 fetches max) trying to fetch product PRODUCT_FILENAME (BYTES_COUNT bytes compressed)'
            msg = f"User quota exceeded: {cause}"
            self.logger.error(msg)
            raise LTAError(msg, r)
        elif r.status_code == 503:
            msg = f"Request not accepted: {cause}"
            self.logger.error(msg)
            raise LTAError(msg, r)
        elif r.status_code < 400:
            msg = f"Unexpected response {r.status_code}: {cause}"
            self.logger.error(msg)
            raise ServerError(msg, r)
        self.api._check_scihub_response(r, test_json=False)

    def get_stream(self, id, **kwargs):
        """Exposes requests response ready to stream product to e.g. S3.

        Parameters
        ----------
        id : string
            UUID of the product, e.g. 'a8dd0cfd-613e-45ce-868c-d79177b916ed'
        **kwargs
            Any additional parameters for :func:`requests.get()`

        Raises
        ------
        LTATriggered
            If the product has been archived and its retrieval was successfully triggered.
        LTAError
            If the product has been archived and its retrieval failed.

        Returns
        -------
        requests.Response:
            Opened response object
        """
        if not self.api.is_online(id):
            self.trigger_offline_retrieval(id)
            raise LTATriggered(id)
        with self.api.dl_limit_semaphore:
            r = self.api.session.get(self.api._get_download_url(id), stream=True, **kwargs)
        self.api._check_scihub_response(r, test_json=False)
        return r

    def download_quicklook(self, id, directory="."):
        """Download a quicklook for a product.

        Parameters
        ----------
        id : string
            UUID of the product, e.g. 'a8dd0cfd-613e-45ce-868c-d79177b916ed'
        directory : string or Path, optional
            Where the image will be downloaded. Defaults to ".".

        Returns
        -------
        quicklook_info : dict
            Dictionary containing the quicklooks's response headers as well as the path on disk.
        """
        product_info = self.api.get_product_odata(id)
        url = product_info["quicklook_url"]

        path = Path(directory) / "{}.jpeg".format(product_info["title"])
        product_info["path"] = str(path)
        product_info["downloaded_bytes"] = 0
        product_info["error"] = ""

        self.logger.info("Downloading quicklook %s to %s", product_info["title"], path)

        with self.api.dl_limit_semaphore:
            r = self.api.session.get(url)
        self.api._check_scihub_response(r, test_json=False)

        product_info["quicklook_size"] = len(r.content)

        if path.exists():
            return product_info

        content_type = r.headers["content-type"]
        if content_type != "image/jpeg":
            product_info["error"] = "Quicklook is not jpeg but {}".format(content_type)

        if product_info["error"] == "":
            with open(path, "wb") as fp:
                fp.write(r.content)
                product_info["downloaded_bytes"] = len(r.content)

        return product_info

    def download_all_quicklooks(self, products, directory="."):
        """Download quicklook for a list of products.

        Parameters
        ----------
        products : dict
            Dict of product IDs, product data
        directory : string or Path, optional
            Directory where the downloaded images will be downloaded
        n_concurrent_dl : integer
            Number of concurrent downloads

        Returns
        -------
        dict[string, dict]
            A dictionary containing the return value from download_quicklook() for each
            successfully downloaded quicklook
        dict[string, dict]
            A dictionary containing the error of products where either
            quicklook was not available or it had an unexpected content type
        """

        self.logger.info("Will download %d quicklooks", len(products))

        downloaded_quicklooks = {}
        failed_quicklooks = {}

        with ThreadPoolExecutor(max_workers=self.n_concurrent_dl) as dl_exec:
            dl_tasks = {}
            for pid in products:
                future = dl_exec.submit(self.download_quicklook, pid, directory)
                dl_tasks[future] = pid

            completed_tasks = concurrent.futures.as_completed(dl_tasks)

            for future in completed_tasks:
                product_info = future.result()
                if product_info["error"] == "":
                    downloaded_quicklooks[dl_tasks[future]] = product_info
                else:
                    failed_quicklooks[dl_tasks[future]] = product_info["error"]

        ResultTuple = namedtuple("ResultTuple", ["downloaded", "failed"])
        return ResultTuple(downloaded_quicklooks, failed_quicklooks)

    def _trigger_and_wait(self, uuid, stop_event, statuses):
        """Continuously triggers retrieval of offline products

        This function is supposed to be called in a separate thread. By setting stop_event it can be stopped.
        """
        with self.api.lta_limit_semaphore:
            t0 = time.time()
            while True:
                if stop_event.is_set():
                    raise concurrent.futures.CancelledError()
                if self.lta_timeout and time.time() - t0 >= self.lta_timeout:
                    raise LTAError(
                        f"LTA retrieval for {uuid} timed out (lta_timeout={self.lta_timeout} seconds)"
                    )
                try:
                    if self.api.is_online(uuid):
                        break
                    if statuses[uuid] == DownloadStatus.OFFLINE:
                        # Trigger
                        triggered = self.trigger_offline_retrieval(uuid)
                        if triggered:
                            statuses[uuid] = DownloadStatus.TRIGGERED
                            self.logger.info(
                                "%s accepted for retrieval, waiting for it to come online...", uuid
                            )
                        else:
                            # Product is online
                            break
                except (LTAError, ServerError) as e:
                    self.logger.info(
                        "%s retrieval was not accepted: %s. Retrying in %d seconds",
                        uuid,
                        e.msg,
                        self.lta_retry_delay,
                    )
                _wait(stop_event, self.lta_retry_delay)
            self.logger.info("%s retrieval from LTA completed", uuid)
            statuses[uuid] = DownloadStatus.ONLINE

    def _download_online_retry(self, product_info, directory, statuses, exceptions, stop_event):
        """Thin wrapper around download with retrying and checking whether a product is online

        Parameters
        ----------
        product_info : dict
        directory : string, optional
        statuses : dict of DownloadStatus
        exceptions : dict of Exception
        stop_event : threading.Event
        """
        if self.max_attempts <= 0:
            return

        uuid = product_info["id"]
        title = product_info["title"]

        # Wait for the triggering and retrieval to complete first
        while (
                statuses[uuid] != DownloadStatus.ONLINE
                and uuid not in exceptions
                and not stop_event.is_set()
        ):
            _wait(stop_event, 1)
        if uuid in exceptions:
            return

        last_exception = None
        for cnt in range(self.max_attempts):
            if stop_event.is_set():
                raise concurrent.futures.CancelledError()
            try:
                if cnt > 0:
                    _wait(stop_event, self.dl_retry_delay)
                statuses[uuid] = DownloadStatus.DOWNLOAD_STARTED
                return self.download(uuid, directory, stop_event=stop_event)
            except (concurrent.futures.CancelledError, KeyboardInterrupt, SystemExit):
                raise
            except Exception as e:
                if isinstance(e, InvalidChecksumError):
                    self.logger.warning(
                        "Invalid checksum. The downloaded file for '%s' is corrupted.",
                        title,
                    )
                else:
                    self.logger.exception("There was an error downloading %s", title)
                retries_remaining = self.max_attempts - cnt - 1
                if retries_remaining > 0:
                    self.logger.info(
                        "%d retries left, retrying in %s seconds...",
                        retries_remaining,
                        self.dl_retry_delay,
                    )
                else:
                    self.logger.info("Downloading %s failed. No retries left.", title)
                last_exception = e
        raise last_exception

    def _download(self, url, path, file_size, title, stop_event):
        # print(self.token)
        headers = {"Authorization": f"Bearer %s" %(self.token)}
        continuing = path.exists()
        if continuing:
            already_downloaded_bytes = path.stat().st_size
            headers["Range"] = "bytes={}-{}".format(already_downloaded_bytes, file_size)
        else:
            already_downloaded_bytes = 0
        downloaded_bytes = 0
        self.api.session.headers.update(headers)
        with self.api.dl_limit_semaphore:
            print(url)
            r = self.api.session.get(url, headers=headers, stream=True)

        with self._tqdm(
                desc="正在下载【%s】" %(title),
                total=file_size,
                unit="B",
                unit_scale=True,
                initial=already_downloaded_bytes,
        ) as progress, closing(r):
            self.api._check_scihub_response(r, test_json=False)
            mode = "ab" if continuing else "wb"
            with open(path, mode) as f:
                iterator = r.iter_content(chunk_size=self.chunk_size)
                while True:
                    if stop_event and stop_event.is_set():
                        raise concurrent.futures.CancelledError()
                    try:
                        with self.api.dl_limit_semaphore:
                            chunk = next(iterator)
                    except StopIteration:
                        break
                    if chunk:  # filter out keep-alive new chunks
                        f.write(chunk)
                        progress.update(len(chunk))
                        downloaded_bytes += len(chunk)
            # Return the number of bytes downloaded
            return downloaded_bytes

    def _dataobj_to_node_info(self, dataobj_info, product_info):
        path = dataobj_info["href"]
        if path.startswith("./"):
            path = path[2:]

        node_info = product_info.copy()
        node_info["url"] = self.api._path_to_url(product_info, path, "value")
        node_info["size"] = dataobj_info["size"]
        if "md5" in dataobj_info:
            node_info["md5"] = dataobj_info["md5"]
        if "sha3-256" in dataobj_info:
            node_info["sha3-256"] = dataobj_info["sha3-256"]
        node_info["node_path"] = path
        # node_info["parent"] = product_info

        return node_info

    def _filter_nodes(self, manifest, product_info, nodefilter=None):
        nodes = {}
        xmldoc = etree.parse(manifest)
        data_obj_section_elem = xmldoc.find("dataObjectSection")
        for elem in data_obj_section_elem.iterfind("dataObject"):
            dataobj_info = _xml_to_dataobj_info(elem)
            node_info = self._dataobj_to_node_info(dataobj_info, product_info)
            if nodefilter is not None and not nodefilter(node_info):
                continue
            node_path = node_info["node_path"]
            nodes[node_path] = node_info
        return nodes


def _xml_to_dataobj_info(element):
    assert etree.iselement(element)
    assert element.tag == "dataObject"
    data = dict(
        id=element.attrib["ID"],
    )
    elem = element.find("byteStream")
    # data["mime_type"] = elem.attrib['mimeType']
    data["size"] = int(elem.attrib["size"])
    elem = element.find("byteStream/fileLocation")
    data["href"] = elem.attrib["href"]
    # data['locator_type'] = elem.attrib["locatorType"]
    # assert data['locator_type'] == "URL"

    elem = element.find("byteStream/checksum")
    assert elem.attrib["checksumName"].upper() in ["MD5", "SHA3-256"]
    data[elem.attrib["checksumName"].lower()] = elem.text

    return data


def _format_exception(ex):
    return "".join(traceback.TracebackException.from_exception(ex).format())


def _wait(event, timeout):
    """Wraps event.wait so it can be disabled for testing."""
    return event.wait(timeout)

