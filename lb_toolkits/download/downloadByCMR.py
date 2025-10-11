# -*- coding:utf-8 -*-
'''
@Project     : lb_toolkits

@File        : downloadByCMR.py

@Modify Time :  2023/5/6 16:34   

@Author      : Lee    

@Version     : 1.0   

@Description :

'''
import os
import sys
import numpy as np
import datetime
from .cmr import cmr

class downloadByCMR(cmr):

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

    def download(self, outdir, url, tries=3, timeout=5*60, skip_download=False, cover=True, wgetpath=None, continuing=True, **kwargs):
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
        skip_download : bool
            是否不做数据下载，直接返回文件名。默认是FALSE，下载文件。
        Returns
        -------
            str
            下载数据的文件名
        '''

        if not os.path.isdir(outdir) :
            os.makedirs(outdir, exist_ok=True)

        if isinstance(url, list):
            files = []
            for url1 in url:
                filename = self.cmr_download(outdir, url1,
                                             token=self.token,
                                             username=self.username,
                                             password=self.password,
                                             timeout=timeout,
                                             skip_download=skip_download,
                                             cover=cover,
                                             tries=tries,
                                             continuing=continuing,
                                             wgetpath=wgetpath, **kwargs)
                files.append(filename)

            return files
        elif isinstance(url, str):
            filename = self.cmr_download(outdir, url,
                                         token=self.token,
                                         username=self.username,
                                         password=self.password,
                                         timeout=timeout,
                                         skip_download=skip_download,
                                         cover=cover,
                                         tries=tries,
                                         continuing=continuing,
                                         wgetpath=wgetpath, **kwargs)

            return filename
