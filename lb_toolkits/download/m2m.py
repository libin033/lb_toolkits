# -*- coding:utf-8 -*-
'''
@Project     : lb_toolkits  
----------------------------------------
@File        : m2m.py  
----------------------------------------
@Modify Time : 2024/8/22  
----------------------------------------
@Author      : Lee  
----------------------------------------
@Desciption
----------------------------------------
采用M2M API进行查询、检索、下载
 
'''
import os
import sys
import json
from urllib.parse import urljoin
import string
import random
import datetime
from dateutil import parser
import time
import re
import requests
from shapely.geometry import Point, shape
import logging
import shutil
from tqdm import tqdm


API_URL         = "https://m2m.cr.usgs.gov/api/api/json/stable/"
USGS_ROOT_URL   = "https://ers.cr.usgs.gov/"
USGS_LOGIN_URL  = "https://ers.cr.usgs.gov/login/"
USGS_LOGOUT_URL = "https://ers.cr.usgs.gov/logout/"
EE_DOWNLOAD_URL = "https://earthexplorer.usgs.gov/download/{data_product_id}/{entity_id}/EE/"

# IDs of GeoTIFF data product for each dataset
DATA_PRODUCTS = {
    # Level 1 datasets
    "landsat_tm_c2_l1": ["5e81f14f92acf9ef", "5e83d0a0f94d7d8d", "63231219fdd8c4e5"],
    "landsat_etm_c2_l1":[ "5e83d0d0d2aaa488", "5e83d0d08fec8a66"],
    "landsat_ot_c2_l1": ["5e81f14ff4f9941c", "5e81f14f92acf9ef"],
    # Level 2 datasets
    "landsat_tm_c2_l2": ["5e83d11933473426", "5e83d11933473426", "632312ba6c0988ef"],
    "landsat_etm_c2_l2": ["5e83d12aada2e3c5", "5e83d12aed0efa58", "632311068b0935a8"],
    "landsat_ot_c2_l2": ["5e83d14f30ea90a9", "5e83d14fec7cae84", "632210d4770592cf"]
}


class M2M():
    """M2M API."""

    def __init__(self, username, password):
        """EarthExplorer API.

        Parameters
        ----------
        username : str
            USGS EarthExplorer username.
        password : str
            USGS EarthExplorer password.
        """

        self.url = API_URL
        self.session = requests.Session()
        self.token = password
        self.login(username, password)

    def search(
            self,
            dataset,
            longitude=None,
            latitude=None,
            bbox=None,
            max_cloud_cover=None,
            start_date=None,
            end_date=None,
            months=None,
            max_results=100,
    ):
        """Search for scenes.

        Parameters
        ----------
        dataset : str
            Case-insensitive dataset alias (e.g. landsat_tm_c1).
        longitude : float, optional
            Longitude of the point of interest.
        latitude : float, optional
            Latitude of the point of interest.
        bbox : tuple, optional
            (xmin, ymin, xmax, ymax) of the bounding box.
        max_cloud_cover : int, optional
            Max. cloud cover in percent (1-100).
        start_date : str, optional
            YYYY-MM-DD
        end_date : str, optional
            YYYY-MM-DD. Equal to start_date if not provided.
        months : list of int, optional
            Limit results to specific months (1-12).
        max_results : int, optional
            Max. number of results. Defaults to 100.

        Returns
        -------
        scenes : list of dict
            Matching scenes as a list of dict containing metadata.
        """
        spatial_filter = None
        if longitude and latitude:
            spatial_filter = SpatialFilterMbr(*Point(longitude, latitude).bounds)
        elif bbox:
            spatial_filter = SpatialFilterMbr(*bbox)

        acquisition_filter = None
        if start_date and end_date:
            acquisition_filter = AcquisitionFilter(start_date, end_date)

        cloud_cover_filter = None
        if max_cloud_cover:
            cloud_cover_filter = CloudCoverFilter(
                max=max_cloud_cover, include_unknown=False
            )

        scene_filter = SceneFilter(
            acquisition_filter, spatial_filter, cloud_cover_filter, months=months
        )

        r = self.request(
            "scene-search",
            params={
                "datasetName": dataset,
                "sceneFilter": scene_filter,
                "maxResults": max_results,
                "metadataType": "full",
            },
        )
        return [_parse_metadata(scene) for scene in r.get("results")]

    @staticmethod
    def raise_api_error(response):
        """Parse API response and return the appropriate exception.

        Parameters
        ----------
        response : requests response
            Response from USGS API.
        """
        data = response.json()
        error_code = data.get("errorCode")
        error_msg = data.get("errorMessage")
        if error_code:
            if error_code in ("AUTH_INVALID", "AUTH_UNAUTHROIZED", "AUTH_KEY_INVALID"):
                raise Exception(f"{error_code}: {error_msg}.")
            elif error_code == "RATE_LIMIT":
                raise Exception(f"{error_code}: {error_msg}.")
            else:
                raise Exception(f"{error_code}: {error_msg}.")

    def request(self, endpoint, params=None):
        """Perform a request to the USGS M2M API.

        Parameters
        ----------
        endpoint : str
            API endpoint.
        params : dict, optional
            API parameters.

        Returns
        -------
        data : dict
            JSON data returned by the USGS API.

        Raises
        ------
        USGSAuthenticationError
            If credentials are not valid of if user lacks permission.
        USGSError
            If the USGS API returns a non-null error code.
        """
        url = urljoin(self.url, endpoint)
        data = json.dumps(params)
        r = self.session.get(url, data=data)
        try:
            self.raise_api_error(r)
        except BaseException:
            time.sleep(3)
            r = self.session.get(url, data=data)
        self.raise_api_error(r)
        return r.json().get("data")

    def login(self, username, token):
        """Get an API key.

        Parameters
        ----------
        username : str
            EarthExplorer username.
        password : str
            EarthExplorer password.
        """

        # 通过Token进行登录
        login_url = urljoin(self.url, "login-token")
        payload = {
            "username": username,
            "token": token
        }
        r = self.session.post(login_url, json.dumps(payload))
        self.raise_api_error(r)
        self.session.headers["X-Auth-Token"] = r.json().get("data")

    def logout(self):
        """Logout from USGS M2M API."""
        self.request("logout")
        self.session = requests.Session()

    def get_entity_id(self, display_id, dataset):
        """Get scene ID from product ID.

        Note
        ----
        As the lookup endpoint has been removed in API v1.5, the function makes
        successive calls to scene-list-add and scene-list-get in order to retrieve
        the scene IDs. A temporary sceneList is created and removed at the end of the
        process.

        Parameters
        ----------
        display_id : str or list of str
            Input product ID. Can also be a list of product IDs.
        dataset : str
            Dataset alias.

        Returns
        -------
        entity_id : str or list of str
            Output entity ID. Can also be a list of entity IDs depending on input.
        """
        # scene-list-add support both entityId and entityIds input parameters
        param = "entityId"
        if isinstance(display_id, list):
            param = "entityIds"

        # a random scene list name is created -- better error handling is needed
        # to ensure that the temporary scene list is removed even if scene-list-get
        # fails.
        list_id = _random_string()
        self.request(
            "scene-list-add",
            params={
                "listId": list_id,
                "datasetName": dataset,
                "idField": "displayId",
                param: display_id,
            },
        )
        r = self.request("scene-list-get", params={"listId": list_id})
        entity_id = [scene["entityId"] for scene in r]
        self.request("scene-list-remove", params={"listId": list_id})

        if param == "entityId":
            return entity_id[0]
        else:
            return entity_id

    def metadata(self, entity_id, dataset, browse=False):
        """Get metadata for a given scene.

        Parameters
        ----------
        entity_id : str
            Landsat Scene ID or Sentinel Entity ID.
        dataset : str
            Dataset alias.
        browse : bool, optional
            Include browse (LandsatLook URLs) metadata items.

        Returns
        -------
        meta : dict
            Scene metadata.
        """
        r = self.request(
            "scene-metadata",
            params={
                "datasetName": dataset,
                "entityId": entity_id,
                "metadataType": "full",
            },
        )
        return _parse_metadata(r, parse_browse_field=browse)

    def get_display_id(self, entity_id, dataset):
        """Get display ID from entity ID.

        Parameters
        ----------
        entity_id : str
            LLandsat Scene ID or Sentinel Entity ID.
        dataset : str
            Dataset alias.

        Returns
        -------
        display_id : str
            Landsat Product ID or Sentinel Display ID.
        """
        meta = self.metadata(entity_id, dataset)
        return meta["display_id"]


    def _download(self, url, outdir, timeout, chunk_size=1024, skip_download=False, cover=False):
        """Download remote file given its URL."""
        # Check availability of the requested product
        # EarthExplorer should respond with JSON
        with self.session.get(
                url, allow_redirects=False, stream=True, timeout=timeout
        ) as r:
            r.raise_for_status()
            error_msg = r.json().get("errorMessage")
            if error_msg:
                raise Exception(error_msg)
            download_url = r.json().get("url")

        try:
            local_filename, filesize = self._get_fileinfo(
                download_url, timeout=timeout, output_dir=outdir
            )

            if skip_download:
                return local_filename

            if os.path.isfile(local_filename) :
                logging.warning('文件已存在，跳过下载【%s】' %(local_filename))
                return local_filename

            basename = os.path.basename(local_filename)
            tempfile = os.path.join(outdir, basename + '.download')

            headers = {}
            file_mode = "wb"
            downloaded_bytes = 0
            file_exists = os.path.exists(tempfile)

            if file_exists and not cover:
                downloaded_bytes = os.path.getsize(tempfile)
                headers = {"Range": f"bytes={downloaded_bytes}-"}
                file_mode = "ab"
            if file_exists and downloaded_bytes == filesize:
                # assert file is already complete
                shutil.move(tempfile, local_filename)
                return local_filename


            with self.session.get(
                    download_url,
                    stream=True,
                    allow_redirects=True,
                    headers=headers,
                    timeout=timeout,
            ) as r:
                with tqdm(
                        total=filesize,
                        unit_scale=True,
                        unit="B",
                        desc=f"正在下载【{basename}】",
                        unit_divisor=1024,
                        initial=downloaded_bytes
                ) as pbar:
                    with open(tempfile, file_mode) as f:
                        for chunk in r.iter_content(chunk_size=chunk_size):
                            if chunk:
                                f.write(chunk)
                                pbar.update(chunk_size)

            shutil.move(tempfile, local_filename)
            return local_filename

        except requests.exceptions.Timeout:
            logging.error(
                "连接超时【{}秒】".format(timeout)
            )

    def _get_fileinfo(self, download_url, timeout, output_dir):
        """Get file name and size given its URL."""
        try:
            with self.session.get(
                    download_url, stream=True, allow_redirects=True, timeout=timeout
            ) as r:
                file_size = int(r.headers.get("Content-Length"))
                local_filename = r.headers["Content-Disposition"].split("=")[-1]
                local_filename = local_filename.replace('"', "")
                local_filename = os.path.join(output_dir, local_filename)
        except requests.exceptions.Timeout:
            logging.error(
                "连接超时【{}秒】.".format(timeout)
            )
        return local_filename, file_size

    def download1(
            self,
            outdir,
            identifier,
            dataset=None,
            timeout=300,
            skip_download=False,
            cover=False,
    ):
        """Download a Landsat scene.

        Parameters
        ----------
        identifier : str
            Scene Entity ID or Display ID.
        outdir : str
            Output directory. Automatically created if it does not exist.
        dataset : str, optional
            Dataset name. If not provided, automatically guessed from scene id.
        timeout : int, optional
            Connection timeout in seconds.
        skip_download : bool, optional
            Skip download, only returns the remote filename.

        Returns
        -------
        filename : str
            Path to downloaded file.
        """
        os.makedirs(outdir, exist_ok=True)
        if not dataset:
            dataset = guess_dataset(identifier)
        if is_display_id(identifier):
            entity_id = self.get_entity_id(identifier, dataset)
        else:
            entity_id = identifier
        # Cycle through the available dataset ids until one works
        dataset_id_list = DATA_PRODUCTS[dataset]
        id_num = len(dataset_id_list)
        for id_count, dataset_id in enumerate(dataset_id_list):
            try:
                url = EE_DOWNLOAD_URL.format(
                    data_product_id=dataset_id, entity_id=entity_id
                )
                filename = self._download(
                    url, outdir, timeout=timeout, skip_download=skip_download, cover=cover
                )
            except BaseException as e :
                if id_count+1 < id_num:
                    # print('Download failed with dataset id {:d} of {:d}. Re-trying with the next one.'.format(id_count+1, id_num))
                    pass
                else:
                    # print('None of the archived ids succeeded! Update necessary!')
                    # raise EarthExplorerError()
                    return None
        return filename



def _is_landsat_product_id(id):
    return len(id) == 40 and id.startswith("L")


def _is_landsat_scene_id(id):
    return len(id) == 21 and id.startswith("L")


def _is_sentinel_display_id(id):
    return len(id) == 34 and id.startswith("L")


def _is_sentinel_entity_id(id):
    return len(id) == 8 and id.isdecimal()


def is_display_id(id):
    return _is_landsat_product_id(id) or _is_sentinel_display_id(id)


def is_entity_id(id):
    return _is_landsat_scene_id(id) or _is_sentinel_entity_id(id)


def is_product_id(identifier):
    """Check if a given identifier is a product identifier
    as opposed to a legacy scene identifier.
    """
    return len(identifier) == 40 and identifier.startswith("L")


def parse_product_id(product_id):
    """Retrieve information from a product identifier.

    Parameters
    ----------
    product_id : str
        Landsat product identifier (also referred as Display ID).

    Returns
    -------
    meta : dict
        Retrieved information.
    """
    elements = product_id.split("_")
    return {
        "product_id": product_id,
        "sensor": elements[0][1],
        "satellite": elements[0][2:4],
        "processing_level": elements[1],
        "satellite_orbits": elements[2],
        "acquisition_date": elements[3],
        "processing_date": elements[4],
        "collection_number": elements[5],
        "collection_category": elements[6],
    }


def parse_scene_id(scene_id):
    """Retrieve information from a scene identifier.

    Parameters
    ----------
    scene_id : str
        Landsat scene identifier (also referred as Entity ID).

    Returns
    -------
    meta : dict
        Retrieved information.
    """
    return {
        "scene_id": scene_id,
        "sensor": scene_id[1],
        "satellite": scene_id[2],
        "path": scene_id[3:6],
        "row": scene_id[6:9],
        "year": scene_id[9:13],
        "julian_day": scene_id[13:16],
        "ground_station": scene_id[16:19],
        "archive_version": scene_id[19:21],
    }


def landsat_dataset(satellite, collection="c2", level="l1"):
    """Get landsat dataset name."""
    if satellite == 5:
        sensor = "tm"
        collection = "c2"
    elif satellite == 7:
        sensor = "etm"
    elif satellite in (8, 9) and collection == "c1":
        raise ValueError('Collection 1 was decommissioned!')
    elif satellite in [8, 9] and collection == "c2":
        sensor = "ot"
    else:
        raise Exception("Failed to guess dataset from identifier.")
    dataset = f"landsat_{sensor}_{collection}"
    if collection == "c2":
        dataset += f"_{level}"
    return dataset



def guess_dataset(identifier):
    """Guess data set based on a scene identifier."""
    # Landsat Product Identifier
    if _is_landsat_product_id(identifier):
        meta = parse_product_id(identifier)
        satellite = int(meta["satellite"])
        collection = "c" + meta["collection_number"][-1]
        level = meta["processing_level"][:2].lower()
        return landsat_dataset(satellite, collection, level)
    elif _is_landsat_scene_id(identifier):
        meta = parse_scene_id(identifier)
        satellite = int(meta["satellite"])
        return landsat_dataset(satellite)
    elif _is_sentinel_display_id(identifier) or _is_sentinel_entity_id(identifier):
        return "sentinel_2a"
    else:
        raise Exception("Failed to guess dataset from identifier.")




def _random_string(length=10):
    """Generate a random string."""
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))


def _title_to_snake(src_string):
    """Convert title case to snake_case."""
    return src_string.lower().replace(" ", "_").replace("/", "-")


def _camel_to_snake(src_string):
    """Convert camelCase string to snake_case."""
    dst_string = [src_string[0].lower()]
    for c in src_string[1:]:
        if c in ("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            dst_string.append("_")
            dst_string.append(c.lower())
        else:
            dst_string.append(c)
    return "".join(dst_string)


def _to_num(src_string):
    """Convert string to int or float if possible.

    Original value is returned if conversion failed.
    """
    if not isinstance(src_string, str):
        return src_string
    src_string = src_string.strip()
    try:
        return int(src_string)
    except ValueError:
        try:
            return float(src_string)
        except ValueError:
            return src_string


def _to_date(src_string):
    """Convert string to datetime if possible.

    Original value is returned if conversion failed.
    """
    if not isinstance(src_string, str):
        return src_string
    try:
        return parser.parse(src_string)
    except parser.ParserError:
        try:
            # Specific date format for start_time and end_time
            nofrag, frag = src_string.split(".")
            dtime = datetime.datetime.strptime(nofrag, "%Y:%j:%H:%M:%S")
            dtime = dtime.replace(microsecond=int(frag[:6]))
            return dtime
        except ValueError:
            pass
    return src_string


def _parse_value(src_value):
    """Try to convert value to numeric or date if possible.

    Original value is returned if conversion failed.
    """
    dst_value = src_value
    if isinstance(dst_value, str):
        dst_value = dst_value.strip()
        dst_value = _to_num(dst_value)
        dst_value = _to_date(dst_value)
    return dst_value


def _parse_browse_metadata(src_meta):
    """Parse the browse field returned by the API."""
    dst_meta = {}
    for product in src_meta:
        name = _title_to_snake(product["browseName"])
        dst_meta[name] = {}
        for field, value in product.items():
            dst_meta[name][_camel_to_snake(field)] = value
    return dst_meta


def _parse_metadata_field(src_meta):
    """Parse the metadata field returned by the API."""
    dst_meta = {}
    for meta in src_meta:
        # Convert field name to snake case
        name = _title_to_snake(meta["fieldName"])
        # Abbreviate "identifier" by "id" for shorter names
        name = name.replace("identifier", "id")
        # Always use "acquisition_date" instead of "acquired_date" for consistency
        if name == "date_acquired":
            name = "acquisition_date"
        # Remove processing-level information in field names for consistency
        name = name.replace("_l1", "")
        name = name.replace("_l2", "")
        # Dictionary link URL also provides some information on the field
        dict_id = meta.get("dictionaryLink").split("#")[-1].strip()
        # Do not process this field
        if dict_id == "coordinates_degrees":
            continue
        # Sentinel metadata has an "Entity ID" field that would
        # conflict with the API entityId field
        if name == "entity_id":
            name = "sentinel_entity_id"
        # Do not parse numeric IDs. Keep them as strings.
        if name.endswith("_id"):
            dst_meta[name] = str(meta.get("value")).strip()
        else:
            dst_meta[name] = _parse_value(meta.get("value"))
    return dst_meta


def _parse_metadata(response, parse_browse_field=False):
    """Parse the full response returned by the API when requesting metadata."""
    metadata = {}
    for key, value in response.items():
        name = _camel_to_snake(key)
        if key == "browse":
            if parse_browse_field:
                metadata[name] = _parse_browse_metadata(value)
            else:
                continue
        elif key == "spatialCoverage":
            metadata[name] = shape(value)
        elif key == "spatialBounds":
            metadata[name] = shape(value).bounds
        elif key == "temporalCoverage":
            start, end = value["endDate"], value["startDate"]
            metadata[name] = [_to_date(start), _to_date(end)]
        elif key == "metadata":
            metadata.update(_parse_metadata_field(value))
        else:
            # Do not parse numeric IDs. Keep them as strings.
            if name.endswith("_id"):
                metadata[name] = str(value).strip()
            else:
                metadata[name] = _parse_value(value)
    if "acquisition_date" not in metadata:
        metadata["acquisition_date"] = metadata["temporal_coverage"][0]
    return metadata


class Coordinate(dict):
    """A coordinate object as expected by the USGS M2M API.

    Parameters
    ----------
    longitude : float
        Decimal longitude.
    latitude : float
        Decimal latitude.
    """

    def __init__(self, longitude, latitude):
        self["longitude"] = longitude
        self["latitude"] = latitude


class GeoJson(dict):
    """A GeoJSON object as expected by the USGS M2M API.

    Parameters
    ----------
    shape : dict
        Input geometry as a geojson-like dict.
    """

    def __init__(self, shape):
        self["type"] = shape["type"]
        self["coordinates"] = self.transform(shape["type"], shape["coordinates"])

    @staticmethod
    def transform(type, coordinates):
        """Convert geojson-like coordinates as expected by the USGS M2M API.

        Essentially converts tuples of coordinates to api.Coordinate objects.
        """
        if type == "MultiPolygon":
            return [
                [Coordinate(*point) for point in polygon] for polygon in coordinates[0]
            ]
        elif type == "Polygon":
            return [Coordinate(*point) for point in coordinates[0]]
        elif type == "LineString":
            return [Coordinate(*point) for point in coordinates]
        elif type == "Point":
            return Coordinate(*coordinates)
        else:
            raise ValueError(f"Geometry type `{type}` not supported.")


class SpatialFilterMbr(dict):
    """Bounding box spatial filter.

    Parameters
    ----------
    xmin : float
        Min. decimal longitude.
    ymin : float
        Min. decimal latitude.
    xmax : float
        Max. decimal longitude.
    ymax : float
        Max. decimal latitude.
    """

    def __init__(self, xmin, ymin, xmax, ymax):
        self["filterType"] = "mbr"
        self["lowerLeft"] = Coordinate(xmin, ymin)
        self["upperRight"] = Coordinate(xmax, ymax)


class SpatialFilterGeoJSON(dict):
    """GeoJSON-based spatial filter.

    Parameters
    ----------
    shape : dict
        Input shape as a geojson-like dict.
    """

    def __init__(self, shape):
        self["filterType"] = "geoJson"
        self["geoJson"] = GeoJson(shape)


class AcquisitionFilter(dict):
    """Acquisition date filter.

    Parameters
    ----------
    start : str
        ISO 8601 start date.
    end : str
        ISO 8601 end date.
    """

    def __init__(self, start, end):
        self["start"] = start
        self["end"] = end


class CloudCoverFilter(dict):
    """Cloud cover filter.

    Parameters
    ----------
    min : int, optional
        Min. cloud cover in percents (default=0).
    max : int, optional
        Max. cloud cover in percents (default=100).
    include_unknown : bool, optional
        Include scenes with unknown cloud cover (default=False).
    """

    def __init__(self, min=0, max=100, include_unknown=False):
        self["min"] = min
        self["max"] = max
        self["includeUnknown"] = include_unknown


class MetadataValue(dict):
    """Metadata filter.

    Parameters
    ----------
    field_id : str
        ID of the field.
    value : str, float or int
        Value of the field.
    """

    def __init__(self, field_id, value):
        self["filterType"] = "value"
        self["filterId"] = field_id
        self["value"] = value
        if isinstance(value, str):
            self["operand"] = "like"
        else:
            self["operand"] = "="


class SceneFilter(dict):
    """Scene search filter.

    Parameters
    ----------
    acquisition_filter : AcquisitionFilter, optional
        Acquisition date filter.
    spatial_filter : SpatialFilterMbr or SpatialFilterGeoJson, optional
        Spatial filter.
    cloud_cover_filter : CloudCoverFilter, optional
        Cloud cover filter.
    metadata_filter : MetadataValue, optional
        Metadata filter.
    months : list of int, optional
        Seasonal filter (month numbers from 1 to 12).
    """

    def __init__(
            self,
            acquisition_filter=None,
            spatial_filter=None,
            cloud_cover_filter=None,
            metadata_filter=None,
            months=None,
    ):
        if acquisition_filter:
            self["acquisitionFilter"] = acquisition_filter
        if spatial_filter:
            self["spatialFilter"] = spatial_filter
        if cloud_cover_filter:
            self["cloudCoverFilter"] = cloud_cover_filter
        if metadata_filter:
            self["metadataFilter"] = metadata_filter
        if months:
            self["seasonalFilter"] = months

