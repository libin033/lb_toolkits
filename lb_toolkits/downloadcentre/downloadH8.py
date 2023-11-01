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
import sys
import datetime
import time

from lb_toolkits.tools import ftppro
from lb_toolkits.tools import writejson


FTPHOST='ftp.ptree.jaxa.jp'

class downloadH8(object):

    def __init__(self, username, password):

        self.ftp = ftppro(FTPHOST, username, password)

    def search_ahi8_l1_netcdf(self, starttime, endtime=None, pattern=None, skip=False):
        '''
        下载葵花8号卫星L1 NetCDF数据文件

        Parameters
        ----------
        starttime : datetime
            下载所需数据的起始时间
        endtime : datetime
            下载所需数据的起始时间
        pattern: list, optional
            模糊匹配参数

        Returns
        -------
            list
            下载的文件列表
        '''

        if endtime is None :
            endtime = starttime

        downfilelist = []

        nowdate = starttime
        while nowdate <= endtime :
            # 拼接H8 ftp 目录
            sourceRoot = os.path.join('/jma/netcdf', nowdate.strftime("%Y%m"), nowdate.strftime("%d"))
            sourceRoot = sourceRoot.replace('\\','/')

            # 获取文件列表
            filelist = self.GetFileList(starttime, endtime, sourceRoot, pattern)
            if len(filelist) == 0 :
                nowdate += datetime.timedelta(days=1)
                print('未匹配当前时间【%s】的文件' %(nowdate.strftime('%Y-%m-%d')))
                continue

            nowdate += datetime.timedelta(days=1)
            downfilelist.extend(filelist)

        return downfilelist


    def search_ahi8_l1_hsd(self, starttime, endtime=None, pattern=[], skip=False):
        '''
        ## Available Himawari Standard Data

        ## Full-disk

         Observation area: Full-disk
         Temporal resolution: 10-minutes
         Spatial resolution: 0.5km (band 3), 1km (band 1,2,4), 2km (band 5-16)

        ## Japan Area

         Observation area: Japan area (Region 1 & 2)
         Temporal resolution: 2.5-minutes
         Spatial resolution: 0.5km (band 3), 1km (band 1,2,4), 2km (band 5-16)

        ## Target Area

         Observation area: Target area (Region 3)
         Temporal resolution: 2.5-minutes
         Spatial resolution: 0.5km (band 3), 1km (band 1,2,4), 2km (band 5-16)

        ## Color Image Data

         png images of Full-disk, Japan area and Target area, compositing three visible
         bands (blue: 0.47 micron; green: 0.51 micron; red: 0.64 micron).

        ## Structure of FTP Directories

         - /jma/hsd

         -       +---/[YYYYMM]

         -              +---/[DD]

         -                     +---/[hh]

         where YYYY: 4-digit year of observation start time (timeline);
               MM: 2-digit month of timeline;
               DD: 2-digit day of timeline; and
               hh: 2-digit hour of timeline.

        Parameters
        ----------
        starttime : datetime
            下载所需数据的起始时间
        endtime : datetime
            下载所需数据的起始时间
        pattern: list, optional
            模糊匹配参数
        skip: bool

        Returns
        -------
            list
            下载文件列表
        '''
        if endtime is None :
            endtime = starttime

        downfilelist = []

        nowdate = starttime
        while nowdate <= endtime :
            # 拼接H8 ftp 目录
            sourceRoot = os.path.join('/jma/hsd',
                                      nowdate.strftime("%Y%m"),
                                      nowdate.strftime("%d"),
                                      nowdate.strftime("%H"))
            sourceRoot = sourceRoot.replace('\\','/')
            # 获取文件列表
            filelist = self.GetFileList(starttime, endtime, sourceRoot, pattern)
            if len(filelist) == 0 :
                nowdate += datetime.timedelta(days=1)
                print('未匹配当前时间【%s】的文件' %(nowdate.strftime('%Y-%m-%d')))
                continue

            nowdate += datetime.timedelta(days=1)
            downfilelist.extend(filelist)

        return downfilelist

    def download(self, outdir, srcfile, blocksize=1*1024, skip=False):
        """通过ftp接口下载H8 L1数据文件"""

        if not os.path.exists(outdir):
            os.makedirs(outdir)
            print('成功创建路径：%s' %(outdir))

        if isinstance(srcfile, list) :
            count = len(srcfile)
            for srcname in srcfile:
                count -= 1
                self._download(outdir, srcname, blocksize=blocksize, skip=skip, count=count+1)

        elif isinstance(srcfile, str) :
            self._download(outdir, srcfile, blocksize=blocksize, skip=skip)

    def _download(self, outdir, srcname, blocksize=1*1024, skip=False, count=1):

        print('='*100)
        basename = os.path.basename(srcname)
        dstname = os.path.join(outdir, basename)

        if skip :
            return srcname

        if os.path.isfile(dstname) :
            print('文件已存在，跳过下载>>【%s】' %(dstname))
            return srcname

        stime = time.time()
        print(datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),
              '开始下载文件【%d】: %s'%(count, srcname))

        if self.ftp.downloadFile(srcname, outdir, blocksize=blocksize):
            print(datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),
                  '成功下载文件【%s】:%s' %(count, dstname))
        else:
            print(datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),
                  '下载文件失败【%s】:%s' %(count, dstname))

        etime = time.time()
        print('下载文件共用%.2f秒' %(etime - stime))

        return srcname

    def GetFileList(self, starttime, endtime, srcpath, pattern=None):
        ''' 根据输入时间，匹配获取H8 L1数据文件名  '''
        downfiles = []

        srcpath = srcpath.replace('\\', '/')

        filelist = self.ftp.listdir(srcpath)
        filelist.sort()
        for filename in filelist :
            namelist = filename.split('_')
            nowdate = datetime.datetime.strptime('%s %s' %(namelist[2], namelist[3]), '%Y%m%d %H%M')

            if (nowdate < starttime) | (nowdate > endtime) :
                continue

            downflag = True
            # 根据传入的匹配参数，匹配文件名中是否包含相应的字符串
            if pattern is not None :
                if isinstance(pattern, list) :
                    for item in pattern :
                        if item in filename :
                            downflag = True
                            # break
                        else:
                            downflag = False
                            break
                elif isinstance(pattern, str) :
                    if pattern in filename :
                        downflag = True
                    else:
                        downflag = False

            if downflag :
                srcname = os.path.join(srcpath, filename)
                srcname = srcname.replace('\\','/')

                downfiles.append(srcname)

        return downfiles

    def writeok(self, okname, info):

        writejson(okname, info)



