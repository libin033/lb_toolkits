# -*- coding:utf-8 -*-
'''
@Project  : lb_toolkits

@File     : downloadERA5.py

@Modify Time : 2022/8/11 15:34

@Author : Lee

@Version : 1.0

@Description :
下载ERA5 再分析廓线数据和地面分析资料
'''
import sys
import os
import cdsapi
import datetime

def checkkeys(url, key) :
    keyfile = os.environ.get("CDSAPI_RC", os.path.expanduser("~/.cdsapirc"))
    if not os.path.isfile(keyfile):
        print('【%s】不存在，将创建它' %(keyfile))
        if url is None or key is None :
            raise Exception('请输入cdsapi账号的链接和密钥')
        tempfile = os.environ.get("CDSAPI_RC", os.path.expanduser("~/temp.txt"))
        fp = open(tempfile, 'w')
        fp.write('url: %s\n' %(url))
        fp.write('key: %s\n' %(key))
        fp.close()
        os.rename(tempfile, keyfile)
    else:
        with open(keyfile) as fp :
            lines = fp.readlines()
            fp.close()
            print(lines)


def download_era5_profile(outname, nowtime, variable, pressure, area_info=None,
                          format='netcdf', m_client=None, redownload=False,
                          url=None, key=None):
    '''
    下载ERA5 再分析的廓线数据

    Parameters
    ----------
    outname: str
            输出文件名
    strdate:  datetime
            下载的数据时间
    variable: list
            下载廓线的要素信息
    pressure: list
            下载廓线的气压层信息
    area_info: dict or list
                [maxlat, minlon, minlat, maxlon],所需下载的区域范围，默认为全球
    format: str
            默认是“netcdf”, 支持"grib"格式下载
    m_client: str
            登录官网连接
    redownload : bool
            重新下载标识
    url: str, optional
        cdsapi账号的密钥链接, 如果本地账号目录下没有该文件，
        可通过传入该参数进行创建“.cdsapirc”
    key: str, optional
        cdsapi账号的密钥, 如果本地账号目录下没有该文件，
        可通过传入该参数进行创建“.cdsapirc”
    Returns
    -------

    '''

    checkkeys(url, key)

    # 文件是否重复下载
    if os.path.isfile(outname) and not redownload:
        return None

    if m_client is None:
        m_client = cdsapi.Client()

    downinfo = {}
    downinfo['product_type'] = 'reanalysis'
    if isinstance(variable, list) :
        downinfo['variable'] = variable

    if isinstance(pressure, list) :
        downinfo['pressure_level'] = pressure

    downinfo['year']  = nowtime.strftime('%Y')
    downinfo['month'] = nowtime.strftime('%m')
    downinfo['day']   = nowtime.strftime('%d')
    downinfo['time']  = [nowtime.strftime('%H:%M'), ]

    if area_info is not None :
        if isinstance(area_info, dict) :
            downinfo['area'] = [
                area_info['maxlat'],
                area_info['minlon'],
                area_info['minlat'],
                area_info['maxlon'],
            ]
        elif isinstance(area_info, list) :
            downinfo['area'] = area_info
        else:
            raise Exception('area_info need to include "maxlat, minlon, minlat, maxlon"')

    downinfo['format'] = format

    m_client.retrieve(
        'reanalysis-era5-pressure-levels',
        downinfo,
        outname)
    print('download ==>[%s]  success...' %(outname))

def download_era5_surface(outname, nowtime, variable, area_info=None,
                          format='netcdf', m_client=None, redownload=False,
                          url=None, key=None):
    '''
    下载ERA5 再分析的地面数据

    Parameters
    ----------
    outname: string
            输出文件名
    startdate: datetime
            下载的数据时间
    variable : list
            需要下载的要素信息
    area_info : dict or list
            [maxlat, minlon, minlat, maxlon],
            所需下载的区域范围，默认为全球
    format: str
            默认是“netcdf”, 支持"grib"格式下载
    m_client: str
            登录官网连接
    redownload :bool
            重新下载标识
    url: str, optional
        cdsapi账号的密钥链接, 如果本地账号目录下没有该文件，
        可通过传入该参数进行创建“.cdsapirc”
    key: str, optional
        cdsapi账号的密钥, 如果本地账号目录下没有该文件，
        可通过传入该参数进行创建“.cdsapirc”
    Returns
    -------

    '''

    checkkeys(url, key)

    # 文件是否重复下载
    if os.path.isfile(outname)  and not redownload:
        return None

    if m_client is None :
        m_client = cdsapi.Client()

    downinfo = {}
    downinfo['product_type'] = 'reanalysis'
    if isinstance(variable, list) :
        downinfo['variable'] = variable

    downinfo['year']  = nowtime.strftime('%Y')
    downinfo['month'] = nowtime.strftime('%m')
    downinfo['day']   = nowtime.strftime('%d')
    downinfo['time']  = [nowtime.strftime('%H:%M'), ]

    if area_info is not None :
        if isinstance(area_info, dict) :
            downinfo['area'] = [
                area_info['maxlat'],
                area_info['minlon'],
                area_info['minlat'],
                area_info['maxlon'],
            ]
        elif isinstance(area_info, list) :
            downinfo['area'] = area_info
        else:
            raise Exception('area_info need to include "maxlat, minlon, minlat, maxlon"')

    downinfo['format'] = format

    m_client.retrieve(
        'reanalysis-era5-single-levels',
        downinfo,
        outname )
    print('download ==>[%s]  success...' %(outname))





