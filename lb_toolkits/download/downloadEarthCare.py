# -*- coding:utf-8 -*-
'''
@Project     : lb_toolkits  
----------------------------------------
@File        : downloadEarthCare.py  
----------------------------------------
@Modify Time : 2025/9/22  
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

import requests


baseurl = 'https://ec-pdgs-discovery.eo.esa.int/socat/'
# https://ec-pdgs-discovery.eo.esa.int/socat/EarthCAREL1Validated/

'''
service=SimpleOnlineCatalogue&version=1.2&request=search&format=text%2Fhtml&pageCount=10&query.orbitNumber.min=&query.orbitNumber.max=&query.beginAcquisition.start=&query.beginAcquisition.stop=&query.endAcquisition.start=&query.endAcquisition.stop=&query.wrsLongitudeGrid=&query.footprint.minlat=&query.footprint.minlon=&query.footprint.maxlat=&query.footprint.maxlon=
service=SimpleOnlineCatalogue&version=1.2&request=search&format=text%2Fhtml%3B+type%3Dbulk-download&pageCount=10&query.orbitNumber.min=&query.orbitNumber.max=&query.beginAcquisition.start=&query.beginAcquisition.stop=&query.endAcquisition.start=&query.endAcquisition.stop=&query.wrsLongitudeGrid=&query.footprint.minlat=&query.footprint.minlon=&query.footprint.maxlat=&query.footprint.maxlon=
service=SimpleOnlineCatalogue&version=1.2&request=search&format=text%2Ftab-separated-values&pageCount=10&query.orbitNumber.min=&query.orbitNumber.max=&query.beginAcquisition.start=2025-09-01&query.beginAcquisition.stop=2025-09-23&query.endAcquisition.start=&query.endAcquisition.stop=&query.wrsLongitudeGrid=&query.footprint.minlat=0.000&query.footprint.minlon=70.000&query.footprint.maxlat=55.000&query.footprint.maxlon=140.000&query.productType=CPR_FMR_2A
'''

class downloadEarthCare :

    def __init__(self, username, password):

        self.username = username
        self.password = password

    def searchfile(self, shortname, starttime, endtime=None,
                   version=None, **kwargs):

        pass

