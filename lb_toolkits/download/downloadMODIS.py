# -*- coding:utf-8 -*-
'''
@Project  : lb_toolkits

@File     : downloadMODIS.py

@Modify Time : 2022/8/11 15:34

@Author : Lee

@Version : 1.0

@Description :
 https://wiki.earthdata.nasa.gov/display/EDSC/Earthdata+Search+URL+Parameters
 https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/
'''
import os
# import platform
# import sys
# import re
# import numpy as np
# import requests
# from bs4 import BeautifulSoup

# URL_LOGIN = 'https://urs.earthdata.nasa.gov/home'
# URL_ROOT = 'https://e4ftl01.cr.usgs.gov/'
# URL_ROOT = 'https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/'
# URL_ROOT = 'https://search.earthdata.nasa.gov/search'

from .cmr import cmr



class downloadMODIS(cmr):

    def __init__(self, username, password):

        self.username = username
        self.password = password
        self.token = self.get_tokens(username, password)

    def searchfile(self, shortname, starttime, endtime=None,
                   provider=None, version=None, **kwargs):
        '''
        利用cmr进行查询检索相关产品的下载地址

        Parameters
        ----------
        starttime : datetime
            起始时间
        endtime : datetime, optional
            起始时间
        shortname : str
            对应cmr中的short name
        provider : str, optional
            产品提供的组织结构
        pattern : str or list
            预留接口，对文件名进行模糊匹配（未实现改功能）
        Returns
        -------
            list
            根据条件所匹配到的产品下载链接
        '''

        if not self.cmr_check_provider(shortname=shortname, provider=provider, version=version) :
            return []

        if endtime is None :
            endtime = starttime

        filelist = self.cmr_search(starttime=starttime, endtime=endtime,
                                   short_name=shortname, version=version, **kwargs)
        return filelist

    def download(self, outdir, url, timeout=5 * 60, skip=False, wgetpath=None):
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


