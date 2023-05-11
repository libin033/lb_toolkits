# -*- coding:utf-8 -*-
'''
@Project  : lb_toolkits

@File     : downloadOCO.py

@Modify Time : 2022/8/11 15:34

@Author : Lee

@Version : 1.0

@Description :

'''
import datetime
import os
import platform
import sys
import re
import numpy as np
import requests
from tqdm import tqdm
from bs4 import BeautifulSoup
import shutil

# LOGIN_URL = 'https://urs.earthdata.nasa.gov/home'
#
# URL_ROOT = 'https://oco2.gesdisc.eosdis.nasa.gov/data'


from .cmr import cmr
from .config import WGET

class downloadOCO(cmr):

    def __init__(self, username, password):

        self.username = username
        self.password = password

    def searchfile(self, starttime, endtime=None,
                   shortname='OCO2_L2_Standard.10r',
                   provider='LARC_ASDC',
                   **kwargs):
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
        Returns
        -------
            list
            根据条件所匹配到的产品下载链接
        '''

        if endtime is None :
            endtime = starttime

        CMR_ProviderURL = 'https://cmr.earthdata.nasa.gov/search/site/' \
                          'collections/directory/{Provider}/gov.nasa.eosdis'.format(Provider=provider)

        if not self.cmr_check_provider(shortname=shortname) :
            raise Exception('请参考Short Name>>"%s"' %(CMR_ProviderURL))

        # 调用cmr进行产品查询
        filelist = self.cmr_search(starttime=starttime, endtime=endtime,
                                   short_name=shortname, **kwargs)

        return filelist

    def download(self, outdir, url, timeout=5*60, skip=False):
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

        if not  os.path.isdir(outdir) :
            os.makedirs(outdir, exist_ok=True)

        filename = self._download(outdir, url, timeout=timeout, skip=skip)

        return filename

    def _download(self, outdir, url, timeout, chunk_size=1024, skip=False):
        local_filename = os.path.basename(url)
        local_filename = os.path.join(outdir, local_filename)
        if skip :
            return local_filename

        if os.path.isfile(local_filename) :
            return local_filename

        tempfile = local_filename + '.download'

        if platform.system().lower() == 'windows' :
            cmd = f'{WGET} {url} -c --tries=3 ' \
                  f'--http-user={self.username} ' \
                  f'--http-passwd={self.password} ' \
                  f'--timeout={timeout}' \
                  f'  -O {tempfile}'
        else:
            cmd = f'{WGET} {url}  -c --tries=3 ' \
                  f'--http-user={self.username} ' \
                  f'--http-passwd={self.password} ' \
                  f'--timeout={timeout}' \
                  f'  -O {tempfile}'
        print('执行下载命令: 【%s】' %(cmd))
        os.system(cmd)

        if os.path.isfile(local_filename) :
            os.remove(local_filename)

        if os.path.isfile(tempfile) :
            shutil.move(tempfile, local_filename)

        return local_filename

