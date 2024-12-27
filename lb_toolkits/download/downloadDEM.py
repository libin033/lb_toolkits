# -*- coding:utf-8 -*-
'''
@Project     : lb_toolkits

@File        : downloadDEM.py

@Modify Time :  2022/11/11 14:18   

@Author      : Lee    

@Version     : 1.0   

@Description :

'''
import os
import sys
import numpy as np
import datetime

from .cmr import cmr

class downloadDEM(cmr) :

    def __init__(self, username, password):

        self.username = username
        self.password = password

        self.token = self.get_tokens(username, password)


    def searchfile(self, shortname='ASTGTM_NC', provider='LPDAAC_ECS', version=None,
                   bounding_box=[-180, -90, 180, 90], **kwargs):
        '''
        利用cmr进行查询检索相关产品的下载地址

        Parameters
        ----------
        starttime : datetime
            起始时间
        endtime : datetime, optional
            起始时间
        satid : str, optional
            卫星名
        shortname : str
            对应cmr中的short name
        provider : str, optional
            产品提供的组织结构
        pattern : str
            对文件名进行模糊匹配
        bounding_box: list
            [minX, minY, maxX, maxY]
            lower left longitude, lower left latitude,
            upper right longitude, upper right latitude.

        Returns
        -------
            list
            根据条件所匹配到的产品下载链接
        '''

        CMR_ProviderURL = 'https://cmr.earthdata.nasa.gov/search/site/' \
                          'collections/directory/{Provider}/gov.nasa.eosdis'.format(Provider=provider)

        if not self.cmr_check_provider(shortname=shortname) :
            raise Exception('请参考Short Name>>"%s"' %(CMR_ProviderURL))

        filelist = self.cmr_search(starttime=None, endtime=None,
                                   short_name=shortname,
                                   bounding_box=bounding_box,
                                   **kwargs)

        return filelist

    def download(self, outdir, url, timeout=5*60, skip=False, wgetpath=None):
        '''
        根据输入url下载相应的文件

        Parameters
        ----------
        outdir: str
            输出路径
        url : str
            下载链接
        token : str
            EarthData账号的APP Keys
        timeout : int
            时间限制
        skip : bool
            是否不做数据下载，直接返回文件名。默认是FALSE，下载文件。
        Returns
        -------
            str
            下载数据的文件名
        '''

        if not os.path.isdir(outdir) :
            os.makedirs(outdir, exist_ok=True)

        filename = self.cmr_download(outdir, url, token=self.token,
                                     username=self.username, password=self.password,
                                     timeout=timeout, skip_download=skip, wgetpath=wgetpath)

        return filename

    def searchDEM30M(self, minX=70, minY=10, maxX=140, maxY=55):

        urllist = []
        for lat in np.arange(np.floor(minY), np.ceil(maxY)) :
            for lon in np.arange(np.floor(minX), np.ceil(maxX)) :
                if lat < -90 or lat > 90 :
                    continue

                if lon < -180 or lat > 180 :
                    continue

                if lat >= 0 :
                    strlat = 'N%02d' %(lat)
                else:
                    strlat = 'S%02d' %(lat)

                if lon >= 0 :
                    strlon = 'E%03d' %(lon)
                else:
                    strlon = 'W%03d' %(lon)


                url = r'https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/ASTGTM.003/' \
                      'ASTGTMV003_{lat}{lon}_dem.tif'.format(lat=strlat, lon=strlon)

                urllist.append(url)

        return urllist



