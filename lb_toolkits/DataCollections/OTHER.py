# -*- coding:utf-8 -*-
'''
@Project     : lb_toolkits  
----------------------------------------
@File        : OTHER.py  
----------------------------------------
@Modify Time : 2024/12/30  
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
from .DataCollectionDefinition import DataCollectionDefinition


class DataCollectionLC :

    LANDCOVER_V003_ESRI = DataCollectionDefinition(
        api_id='LC',
        collections="esri_landcover",
        description='esri sentinel-2 10M landuse/landcover v003'
    )

class DataCollectionFY :

    FY_Order_NSMC = DataCollectionDefinition(
        api_id='FY',
        collections="FY_Products",
        description='通过订单号下载风云卫星数据产品'
    )

    FY3D_MERSI_L1_NSMC = DataCollectionDefinition(
        api_id='FY',
        collections="FY3D_MERSI_L1",
        description='通过订单号下载FY3D_MERSI_L1'
    )


class DataCollectionHY :

    HY2B_OSDDS = DataCollectionDefinition(
        api_id='HY',
        collections="HY_Products",
        description='海洋卫星产品数据'
    )

class DataCollectionGFS :

    NOAA_NWP_GFS = DataCollectionDefinition(
        api_id='GFS',
        collections="GFS_NOAA",
        description='NOAA GFS预报数据'
    )




