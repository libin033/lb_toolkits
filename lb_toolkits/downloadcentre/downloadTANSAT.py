# -*- coding:utf-8 -*-
'''
@Project     : lb_toolkits

@File        : downloadTANSAT.py

@Modify Time :  2023/3/13 10:53   

@Author      : Lee    

@Version     : 1.0   

@Description :

'''
import os
import sys
import numpy as np
import datetime

import requests
from lb_toolkits.tools import spiderdownload


class downloadTANSAT():

    def __init__(self, outdir=None, startdate=None, enddate=None, obstype='ND',
                 timeout=5 * 60, skip=False, cover=False):
        if startdate is not None and enddate is not None :
            filelist = self.searchfile(startdate, enddate, obstype=obstype)
            for item in filelist :
                self.download(outdir, item, timeout=timeout, skip=skip, cover=cover)

    def searchfile(self, startdate, enddate, obstype='ND'):

        downfilelist = []

        nowdate = startdate
        while nowdate <= enddate :
            url = 'https://zheda.oss-cn-beijing.aliyuncs.com/casa_data/TanSat/L2_XCO2/{YYYY}{MM}/' \
                      'TanSat_ACGS_SCI_{obstype}_L2_XCO2_lite_{YYYY}{MM}{DD}.nc'.format(
                YYYY=nowdate.strftime('%Y'),
                MM=nowdate.strftime('%m'),
                DD=nowdate.strftime('%d'),
                obstype=obstype)
            nowdate += datetime.timedelta(days=1)

            downfilelist.append(url)

            # res=requests.get(url, timeout=60)
            # if res.status_code == 200:
            #     print(url)
                # downfilelist.append(url)
            # else:
            #     pass
            #     print('未匹配到文件', nowdate)


        return downfilelist

    def download(self, outdir, url, timeout=5 * 60, skip=False, cover=False):
        '''
        根据输入url下载相应的文件

        Parameters
        ----------
        outdir: str
            输出路径
        url : str
            下载链接
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

        down = spiderdownload()
        filename = down.download(outdir, url, timeout=timeout, skip=skip, cover=cover)

        try:
            filesize = os.path.getsize(filename)
            if filesize < 500 :
                os.remove(filename)
            return filename
        except BaseException :
            pass


