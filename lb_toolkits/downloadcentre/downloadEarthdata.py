# -*- coding:utf-8 -*-
'''
@Project     : lb_toolkits

@File        : downloadEarthdata.py

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

class downloadEarthdata(cmr):

    def __init__(self, username, password):

        self.username = username
        self.password = password

        self.token = self.get_tokens(username, password)

    def searchfile(
            self,
            starttime,
            endtime,
            shortname,
            provider=None,
            version=None,
            **kwargs
    ):
        '''
        利用cmr进行查询检索相关产品的下载地址

        Parameters
        ----------
        starttime : datetime
            起始时间
        endtime : datetime
            起始时间
        prodversion : str
            对应cmr中的short name
        provider : str, optional
            产品提供的组织结构
        Returns
        -------
            list
            根据条件所匹配到的产品下载链接
        '''

        # CMR_ProviderURL = 'https://cmr.earthdata.nasa.gov/search/site/' \
        #                   'collections/directory/{Provider}/gov.nasa.eosdis'.format(Provider=provider)

        if not self.cmr_check_provider(shortname=shortname, provider=provider, version=version) :
            raise Exception('请参考Short Name>>"%s"' %(
                'https://cmr.earthdata.nasa.gov/search/site/collections/directory/eosdis'))

        if endtime is None :
            endtime = starttime

        filelist = self.cmr_search(starttime=starttime,
                                   endtime=endtime,
                                   short_name=shortname,
                                   **kwargs)
        return filelist

    def download(self, outdir, url, timeout=5 * 60, skip=False, **kwargs):
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
                                     timeout=timeout, skip=skip, **kwargs)

        return filename
