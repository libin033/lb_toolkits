# -*- coding:utf-8 -*-
'''
@Project     : code

@File        : interplate.py

@Modify Time :  2022/11/1 17:25   

@Author      : Lee    

@Version     : 1.0   

@Description :

'''
import os
import sys
import numpy as np
import datetime

import glob
from arspy.ncpro import readnc
from arspy.jsonpro import readjson

from osgeo import gdal

from .anusplin import anusplin
from dateutil.relativedelta import relativedelta


exepath = os.path.dirname(os.path.abspath(__file__))
# parm = readjson(os.path.join(exepath, 'config.json'))

def setcovdem():
    demfile = os.path.join(exepath,'conf\global_dem.nc')
    srcdem = readnc(demfile, 'dem')

    dict_cov = {
        'cov1' : {
            'covname' : 'dem',
            'data' : np.zeros_like(srcdem, dtype=np.float32),
            'extent' : [-180.0, -90.0, 180.0, 90.0], #(minX, minY, maxX, maxY)
            'vmin' : 0.0,
            'vmax' : 10000.0
        },
    }

    return dict_cov

def setcovpop(parm):
    popfile = os.path.join(exepath,'conf', 'ppp_2020_1km_Aggregated.tif')

    ds = gdal.Warp('', popfile, format='MEM',
                        xRes=parm["resolution"], yRes=parm["resolution"], resampleAlg=gdal.GRA_Max,
                        dstNodata=0.0, outputBounds=(-180.0, -90.0, 180.0, 90.0))

    # gdal.Warp('./conf/pop.tif', popfile, format='GTiff',
    #                xRes=parm["resolution"], yRes=parm["resolution"], resampleAlg=gdal.GRA_Max,
    #                dstNodata=0.0, outputBounds=(parm['minX'], parm['minY'], parm['maxX'], parm['maxY']))
    # exit()
    covdata = ds.ReadAsArray()

    dict_cov = {
        'cov1' : {
            'covname' : 'pop',
            'data' : covdata,
            'extent' : [-180.0, -90.0, 180.0, 90.0], #(minX, minY, maxX, maxY)
            'vmin' : 0.0,
            'vmax' : 100000.0
        },
    }

    return dict_cov

def interplation(outname, xco2, lat, lon,  dict_cov,
                 minX=-180.0, maxX=180.0,
                 minY=-70.0, maxY=70.0, resolution=0.25):

    dirname = os.path.dirname(outname)
    if not os.path.isdir(dirname) :
        os.makedirs(dirname)

    mpro = anusplin(outname, data=xco2, lat=lat,
                    lon=lon, dict_cov=dict_cov,
                    minX=minX, maxX=maxX,
                    minY=minY, maxY=maxY,
                    resolution=resolution)
    del mpro
    mpro= None

    if os.path.isfile(outname) :
        return True
    else:
        return False


def monthpro(outdir, filelist, dict_cov, startdate=None, enddate=None, satid='OCO-2', prodid='CO2', Bias=0.0):
    ''' 按月进行处理 '''

    if enddate is None :
        enddate = startdate + relativedelta(months=1, seconds=-1)

    outname = os.path.join(outdir, prodid, satid, 'POAM', 'interp', startdate.strftime('%Y%m%d'),
                           '{satid}_{prodid}_{sdate}_{edate}_POAM.tif'.format(
                               satid=satid, prodid=prodid,
                               sdate = startdate.strftime('%Y%m%d'),
                               edate = enddate.strftime('%Y%m%d')))
    # if os.path.isfile(outname) :
    #     return None

    all_xco2 = []
    all_lat = []
    all_lon = []

    for filename in filelist :
        if not os.path.isfile(filename) :
            print('%s 文件不存在' % (filename))
            continue

        xco2 = readnc(filename, 'xco2')
        lat = readnc(filename, 'latitude')
        lon = readnc(filename, 'longitude')
        qcflag = readnc(filename, 'xco2_quality_flag')
        flag = (qcflag == 0) #| (qcflag != 0)

        all_xco2.extend(xco2[flag])
        all_lat.extend(lat[flag])
        all_lon.extend(lon[flag])

    all_xco2 = np.array(all_xco2) - Bias
    all_lat  = np.array(all_lat)
    all_lon  = np.array(all_lon)

    interplation(outname, all_xco2, all_lat, all_lon, dict_cov)


def dayspro(outdir, filename, dict_cov, startdate, enddate=None, satid='OCO-2', prodid='CO2'):
    ''' 按天进行合成处理 '''

    if enddate is None :
        enddate = startdate + relativedelta(days=1, seconds=-1)

    outname = os.path.join(outdir, prodid, satid, 'POAD', 'interp', startdate.strftime('%Y'),
                           '{satid}_{prodid}_{sdate}_{edate}_POAD.tif'.format(
                               satid=satid, prodid=prodid,
                               sdate = startdate.strftime('%Y%m%d'),
                               edate = enddate.strftime('%Y%m%d')))
    # if os.path.isfile(outname) :
    #     return None

    if not os.path.isfile(filename) :
        print('%s 文件不存在' % (filename))
        return None

    xco2 = readnc(filename, 'xco2')
    lat = readnc(filename, 'latitude')
    lon = readnc(filename, 'longitude')
    qcflag = readnc(filename, 'xco2_quality_flag')
    flag = (qcflag == 0) #| (qcflag != 0)

    interplation(outname, xco2[flag], lat[flag], lon[flag], dict_cov)


if __name__ == '__main__':
    pass
    # argv = sys.argv
    #
    # if len(argv) == 3:
    #     outname = argv[1]
    #     filename = argv[2]
    # else:
    #     outname = r'E:\CO2\ANUSPLIN\result\co2\2020_intp202003.tif'
    #     filename = r'E:\CO2\ANUSPLIN\data\co2-2020\co2_202003.tif'

    # filename = r'E:\QH6\data\OCO2\202001\oco2_LtCO2_200101_B10206Ar_200728183348s.nc4'
    # outname = r'E:\QH6\result\oco2\oco2_LtCO2_200101_B10206Ar_200728183348s.tif'

    # path_in = r'D:\DATA\OCO3'
    # outpath = r'E:\QH6\result\oco3'

    # dict_cov = setcovpop()
    # dict_cov = setcovdem()
    #
    # for item in ['202001','202004','202007','202010',] :
    #     filelist = glob.glob(os.path.join(path_in, item, '*.nc4'))
    #     nowdate = datetime.datetime.strptime(item, '%Y%m')
    #     monthpro(filelist, dict_cov, nowdate)

        # for filename in filelist :
        #     namelist = os.path.basename(filename).split('_')
        #     nowdate = datetime.datetime.strptime(namelist[2], '%y%m%d')
        #     print(nowdate)
        #     dayspro(filename, dict_cov=dict_cov, nowdate=nowdate)





