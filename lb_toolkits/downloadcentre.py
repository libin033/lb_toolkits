# -*- coding:utf-8 -*-
'''
@Project     : lb_toolkits
----------------------------------------
@File        : download.py
----------------------------------------
@Modify Time : 2024/11/15
----------------------------------------
@Author      : Lee
----------------------------------------
@Desciption
----------------------------------------


'''

import logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

from lb_toolkits.download import downloadByCMR
from lb_toolkits.download import downloadByM2M
from lb_toolkits.download import downloadByESA
from lb_toolkits.download import downloadLandcover
from lb_toolkits.download import downloadGOSAT, downloadH8
from lb_toolkits.download import downloadFY
class DownloadCentre :
    def __init__(self, collection, username=None, password=None):
        self.collection = collection
        self.username = username
        self.password = password

        if collection.api_id in ['CMR'] :
            self.down = downloadByCMR(username, password)
        elif collection.api_id in ['M2M'] :
            self.down = downloadByM2M(username, password)
        elif collection.api_id in ['ESA'] :
            self.down = downloadByESA(username, password)
        elif collection.api_id in ['LC'] :
            self.down = downloadLandcover()
        elif collection.api_id in ['GOSAT'] :
            self.down = downloadGOSAT(username, password)
        elif collection.api_id in ['AHI'] :
            self.down = downloadH8(username, password)
        elif collection.api_id in ['FY'] :
            self.down = downloadFY(username, password)
        else :
            raise Exception('暂不支持该collection【%s】' %(self.collection.api_id))

    def searchfile(
            self,
            startDate,
            endDate=None,
            bbox=None,
            cloud_cover_max=None,
            months=None,
            max_results=None,
            **kwargs) :

        api_id = self.collection.api_id
        collection = self.collection.collections
        bands = self.collection.bands
        productType = self.collection.productType
        has_cloud_coverage = self.collection.has_cloud_coverage

        provider = self.collection.provider
        shortname = self.collection.shortname
        version = self.collection.version

        if self.collection.api_id in ['CMR'] :
            return self.down.searchfile(shortname=shortname, starttime=startDate, endtime=endDate,
                                        provider=provider, version=version, bbox=bbox, **kwargs)
        elif self.collection.api_id in ['M2M'] :
            return self.down.searchfile(startdate=startDate, enddate=endDate,
                                        bbox=bbox,
                                        cloud_cover_max=cloud_cover_max,
                                        months=months,
                                        max_results=max_results,
                                        **kwargs)
        elif self.collection.api_id in ['ESA'] :
            if bbox is not None :
                footprint = "POLYGON(({minX} {minY},{minX} {maxY},{maxX} {maxY},{maxX} {minY},{minX} {minY}))".format(
                    minX=bbox[0],
                    minY=bbox[1],
                    maxX=bbox[2],
                    maxY=bbox[3],
                )
            else:
                footprint = None
            return self.down.searchfile(startdate=startDate, enddate=endDate,
                                        collection=collection,
                                        productType=productType,
                                        footprint=footprint,
                                        area_relation="Intersects",
                                        cloudCover=cloud_cover_max,
                                        limit=max_results,
                                        offset=0,
                                        **kwargs)
        elif self.collection.api_id in ['LC'] :
            return self.down.searchfile(startdate=startDate, enddate=endDate, bbox=bbox)

        elif self.collection.api_id in ['GOSAT'] :
            return self.down.searchfile(startDate=startDate, endDate=endDate,
                                        prod=shortname, level=collection, version=version)
        elif self.collection.api_id in ['AHI'] :
            return self.down.searchfile(startdate=startDate, enddate=endDate,
                                        collection=collection,
                                        bands=bands, version=version, **kwargs)
        elif self.collection.api_id in ['FY'] :
            return self.down.searchfile(**kwargs)

        else :
            raise Exception('暂不支持该collection【%s】' %(self.collection.api_id))


    def download(self, outdir, url, tries=3, timeout=5*60, skip_download=False, cover=False, continuing=True, **kwargs):

        return self.down.download(outdir=outdir,
                                  url=url,
                                  tries=tries,
                                  timeout=timeout,
                                  skip_download=skip_download,
                                  cover=cover,
                                  continuing=continuing,
                                  **kwargs)
