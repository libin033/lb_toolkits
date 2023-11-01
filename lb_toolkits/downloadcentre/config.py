# -*- coding:utf-8 -*-
'''
@Project     : lb_toolkits

@File        : config.py

@Modify Time :  2022/10/21 17:26   

@Author      : Lee    

@Version     : 1.0   

@Description :

'''

import os
import numpy as np
import datetime
import platform

from lb_toolkits import parm

exedir = os.path.abspath(list(parm.__path__)[0])
from lb_toolkits.downloadcentre import downwgetfromgithub

if platform.system().lower() == 'windows' :
    WGET = os.path.join(exedir, 'bin', 'windows', 'wget.exe')
    if not os.path.isfile(WGET) :
        downwgetfromgithub(WGET)
        if not os.path.isfile(WGET) :
            raise Exception('wget工具不可用')
else:
    WGET = os.path.join(exedir, 'bin', 'linux', 'wget')
    if not os.path.isfile(WGET) :
        downwgetfromgithub(WGET)
        if not os.path.isfile(WGET) :
            raise Exception('wget工具不可用')


#########################################################################################################
# FTP
## 风云卫星近实时FTP站点
FY_FTP_URL = 'ftp.nsmc.org.cn'

## 葵花8号卫星近实时FTP站点
H8_FTP_URL = 'ftp.ptree.jaxa.jp'

## 海洋卫星
HY_FTP_URL = 'osdds-ftp.nsoas.org.cn'

#########################################################################################################
# CMR查询根节点
CMR_URL = 'https://cmr.earthdata.nasa.gov'

# 登录NASA
LOGIN_NASA_URL = 'https://urs.earthdata.nasa.gov/home'

#########################################################################################################
# CALIPSO
CALIPSO_URL = 'https://asdc.larc.nasa.gov/data/'

# OCO-2/3
OCO_URL = 'https://oco2.gesdisc.eosdis.nasa.gov/data/OCO2_DATA/'

# 哨兵数据
S5PHUB_URL = 'https://s5phub.copernicus.eu/dhus/'
SCIHUB_URL = 'https://scihub.copernicus.eu/dhus/'

# MODIS数据
## https://e4ftl01.cr.usgs.gov/
EarthData_URL = 'https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/'
EarthSearch_URL = 'https://search.earthdata.nasa.gov/search'

# GFS
GFS_URL = 'https://nomads.ncep.noaa.gov/cgi-bin/filter_gfs_0p25.pl'
GFS_URL1 = 'https://nomads.ncep.noaa.gov/pub/data/nccf/com/gfs/prod/'

# ERA5
ERA5_Rely_URL = 'https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-land?tab=form'
ERA5_API_URL = 'https://confluence.ecmwf.int/display/CKB/The+family+of+ERA5+datasets'
#########################################################################################################