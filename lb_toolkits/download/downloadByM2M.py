# -*- coding:utf-8 -*-
'''
@Project     : lb_toolkits  
----------------------------------------
@File        : downloadByM2M.py  
----------------------------------------
@Modify Time : 2024/11/15  
----------------------------------------
@Author      : Lee  
----------------------------------------
@Desciption
----------------------------------------
      
 
'''
import os
import sys
import numpy as np
import datetime
import re
import requests
from urllib.parse import urljoin
from lb_toolkits.download import M2M
from lb_toolkits.utils.landsat import EarthExplorer, DATA_PRODUCTS

import logging
logger = logging.getLogger(__name__)


USGS_ROOT_URL   = "https://ers.cr.usgs.gov/"
USGS_LOGIN_URL  = "https://ers.cr.usgs.gov/login/"
USGS_LOGOUT_URL  = "https://ers.cr.usgs.gov/logout/"

# EE_ROOT_URL     = "https://earthexplorer.usgs.gov/"
# EE_LOGOUT_URL   = "https://earthexplorer.usgs.gov/logout"
# EE_DOWNLOAD_URL = "https://earthexplorer.usgs.gov/download/{data_product_id}/{entity_id}/EE/"
#

class downloadByM2M():

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def searchfile(
            self,
            product,
            startdate,
            enddate=None,
            longitude=None,
            latitude=None,
            bbox=None,
            cloud_cover_max=None,
            months=None,
            max_results=100,
            **kwargs
    ):
        '''
        Search for scenes.

        - Dataset Name	                         >>        Dataset ID
        - Landsat 5 TM Collection 2 Level 1	     >>      landsat_tm_c2_l1
        - Landsat 5 TM Collection 2 Level 2	     >>      landsat_tm_c2_l2
        - Landsat 7 ETM+ Collection 2 Level 1	 >>      landsat_etm_c2_l1
        - Landsat 7 ETM+ Collection 2 Level 2	 >>      landsat_etm_c2_l2
        - Landsat 8 Collection 2 Level 1	     >>      landsat_ot_c2_l1
        - Landsat 8 Collection 2 Level 2	     >>      landsat_ot_c2_l2
        - Landsat 9 Collection 2 Level 1	     >>      landsat_ot_c2_l1
        - Landsat 9 Collection 2 Level 2	     >>      landsat_ot_c2_l2

        Parameters
        ----------
        product: str
                Case-insensitive dataset alias (e.g. landsat_tm_c1).
                LANDSAT_TM_C1、LANDSAT_ETM_C1和LANDSAT_8_C1
        longitude : float, optional
                Longitude of the point of interest.
        latitude : float, optional
                Latitude of the point of interest.
        bbox : tuple, optional
                (xmin, ymin, xmax, ymax) of the bounding box.
        cloud_cover_max: int, optional
                Max. cloud cover in percent (1-100).
        startdate: datetime
                YYYY-MM-DD
        enddate : datetime, optional
                YYYY-MM-DD. Equal to startdate if not provided.
        months: list of int, optional
                Limit results to specific months (1-12).
        max_results: int, optional
                Max. number of results. Defaults to 100.

        Returns
        -------
            list of dict
                Matching scenes as a list of dict containing metadata.
        '''
        if enddate is None :
            enddate = startdate

        start_date = startdate.strftime('%Y-%m-%d')
        end_date   = enddate.strftime('%Y-%m-%d')
        api = M2M(self.username, self.password)

        scenes = api.search(dataset=product,
                            latitude=latitude,     longitude=longitude,
                            start_date=start_date, end_date=end_date,
                            bbox = bbox,           max_cloud_cover=cloud_cover_max,
                            months=months,         max_results=max_results)

        logger.info('检索到【%d】景影像' %(len(scenes)))
        api.logout()

        return scenes

    def download(self, outdir, url, scene_id=None, tries=3, timeout=5*60, skip_download=False, cover=True, continuing=True, **kwargs):
        '''
        Download a Landsat scene.

        Parameters
        ----------
        url
        outdir: str;
            Output directory. Automatically created if it does not exist.
        scene_id: str, optional
        tries: int, optional
            尝试失败次数
        timeout : int, optional
        Connection timeout in seconds.:

        Returns
        -------
            str
            Path to downloaded file.
        '''

        if scene_id is not None:
            Earth_Down = EarthExplorer(self.username, self.password)
            Earth_Down.download(identifier=scene_id, outdir=outdir, timeout=timeout)
            Earth_Down.logout()

            return None
        Earth_Down = EarthExplorer(self.username, self.password)
        for scene in url:
            ID = scene['entity_id']
            for i in range(tries) :
                try:
                    Earth_Down = EarthExplorer(self.username, self.password)

                    filename = Earth_Down.download(identifier=ID, outdir=outdir, timeout=timeout)
                    if filename :
                        logger.info('成功下载【%s】' %(filename))
                    else:
                        logger.error('下载失败【%s】' %(ID))
                    break
                except BaseException as e :
                    logger.error('下载失败1【%s】' %(ID))
                    break
        Earth_Down.logout()



