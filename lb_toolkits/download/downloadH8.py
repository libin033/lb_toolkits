# -*- coding:utf-8 -*-
'''
@Project  : lb_toolkits

@File     : downloadH8.py

@Modify Time : 2022/8/11 15:34

@Author : Lee

@Version : 1.0

@Description :

'''
import os
import datetime
import re
import time
import logging
logger = logging.getLogger(__name__)

from lb_toolkits.utils import ftppro
from .config import H8_FTP_URL

# TODO 待增加L3级数据下载

class downloadH8():

    def __init__(self, username, password):

        self.ftp = ftppro(H8_FTP_URL, username, password)

    def searchfile(
            self,
            startdate,
            enddate=None,
            collection=None,
            shortname=None,
            blockids:list=None,
            bands:list=None,
            version:str='NC',
            everyday=False,
            hoursflag=False,
            **kwargs
    ):
        '''
        查询L1 NC/HSD文件
        NC_H09_20250514_0800_R21_FLDK.02401_02401.nc
        /jma/netcdf/202505/21/                  NC_H09_20250521_1150_R21_FLDK.06001_06001.nc
        /jma/hsd/202504/23/21/                  HS_H09_20250423_2150_B08_R304_R20_S0101.DAT.bz2
        /pub/himawari/L2/CLP/010/202504/13/12/  NC_H09_20250413_1250_L2CLP010_FLDK.02401_02401.nc

        Parameters
        ----------
        startdate : datetime.datetime
            起始日期
        enddate : datetime.datetime, options
            结束日期
        collection : str
            数据标识
        shortname : str
            产品标识
        blockids : list
            分块索引
        bands :
            波段索引
        version
        everyday : bool
            只下载每天固定时间段的数据，通过传入的起始结束的小时字段进行处理
        hoursflag : bool
            下载整点数据
        kwargs

        Returns
        -------
            list
            匹配条件的数据下载链接列表
        '''
        if enddate is None:
            enddate = startdate

        urls = []

        nowdate = startdate
        while nowdate <= enddate :
            # 拼接ftp目录
            if collection in ['L1NC'] :
                srcdir = os.path.join('/jma/netcdf',
                                      nowdate.strftime("%Y%m"),
                                      nowdate.strftime("%d"))
            elif collection in ['L1HSD'] :
                srcdir = os.path.join('/jma/hsd',
                                      nowdate.strftime("%Y%m"),
                                      nowdate.strftime("%d"),
                                      nowdate.strftime("%H"))
            elif collection in ['L2'] :
                if shortname in ['ARP'] :
                    if nowdate < datetime.datetime(2022, 9, 27) :
                        version = '030'
                    else:
                        version = '031'

                srcdir = os.path.join('/pub/himawari/L2/',
                                      shortname,
                                      version,
                                      nowdate.strftime('%Y%m'),
                                      nowdate.strftime('%d'),
                                      nowdate.strftime('%H'))
            else:
                logger.error('暂不支持其他产品【%s】' %(collection))
                return None

            srcdir = srcdir.replace('\\','/')
            filelist = self.ftp.listdir(srcdir)
            filelist.sort()

            for filename in filelist:
                basename = os.path.basename(filename)
                basename = basename.replace('.','_')

                if 'FLDK' not in basename :
                    continue

                if collection in ['L1NC'] :
                    if shortname not in basename :
                        continue
                elif collection in ['L1HSD'] :
                    if not basename.endswith('bz2') :
                        continue

                    if bands is not None :
                        search = None
                        for band in bands:
                            search = re.search('B%02d' %(band), basename)
                            if search :
                                break

                        if not search:
                            continue
                    # HS_H09_20250518_1400_B14_FLDK_R20_S0610.DAT.bz2
                    if blockids is not None :
                        search = None
                        for blockid in blockids:
                            search = re.search('S%02d' %(blockid), basename)
                            if search :
                                break

                        if not search:
                            continue

                namelist = basename.split('_')
                ntime = datetime.datetime.strptime(namelist[2]+namelist[3], '%Y%m%d%H%M')
                if hoursflag :  # 仅下载整点
                    if ntime.minute != 0 :
                        continue

                if everyday :
                    stime = datetime.datetime(nowdate.year, nowdate.month, nowdate.day, startdate.hour, startdate.minute, startdate.second)
                    etime = datetime.datetime(nowdate.year, nowdate.month, nowdate.day, enddate.hour, enddate.minute, enddate.second)
                    if ntime < stime or ntime > etime :
                        continue
                else:
                    if ntime < startdate or ntime > enddate :
                        continue
                srcfile = os.path.join(srcdir, filename)
                srcfile = srcfile.replace('\\','/')
                urls.append(srcfile)

            if version in ['L1NC'] :
                nowdate += datetime.timedelta(days=1)
            else:
                if everyday :
                    nowdate += datetime.timedelta(hours=1)
                    if nowdate.hour > enddate.hour :
                        nowdate = datetime.datetime(nowdate.year, nowdate.month, nowdate.day,
                                                    startdate.hour, startdate.minute, startdate.second) \
                                  + datetime.timedelta(days=1)
                else:
                    nowdate += datetime.timedelta(hours=1)

        return urls

    def download(self, outdir, url, tries=3, timeout=5*60, skip_download=False, cover=False, continuing=True, blocksize=1*1024, **kwargs):
        """通过ftp接口下载H8 L1数据文件"""

        if not os.path.isdir(outdir):
            os.makedirs(outdir)

        if isinstance(url, list) :
            count = len(url)
            for srcname in url:
                count -= 1
                self._download(outdir, srcname, blocksize=blocksize, skip_download=skip_download, count=count + 1)

        elif isinstance(url, str) :
            self._download(outdir, url, blocksize=blocksize, skip_download=skip_download)

    def _download(self, outdir, url, blocksize=1 * 1024, skip_download=False, count=1):

        url = url.replace('\\','/')

        print('='*100)
        basename = os.path.basename(url)
        dstname = os.path.join(outdir, basename)

        if skip_download :
            return dstname

        if os.path.isfile(dstname) :
            logger.info('文件已存在，跳过下载>>【%s】' %(dstname))
            return dstname

        stime = time.time()
        logger.info('开始下载文件【%d】: %s' % (count, url))

        if self.ftp.downloadFile(url, outdir, blocksize=blocksize):
            logger.info('成功下载文件【%s】:%s' %(count, dstname))
        else:
            logger.error('下载文件失败【%s】:%s' %(count, dstname))

        etime = time.time()
        logger.info('下载文件共用%.2f秒' %(etime - stime))

        return dstname






