# -*- coding:utf-8 -*-
'''
@Project  : lb_toolkits

@File     : downloadHY.py

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

from .config import HY_FTP_URL

HY_Info = {
    'CFOSAT' : {
        'SCA' : ['L2A', 'L2B'],
        'SWI' : ['L1B']},
    'HY-2B' : {
        'ALT' : ['GDR', 'IDR_2M', 'SDR_2M'],
        'SCA' : ['L2B']},
    'HY-2C' : {
        'ALT' : ['GDR', 'IDR'],
        'SCA' : ['L2B']},
    'HY-2D' : {
        'ALT' : ['GDR', 'IDR'],
        'SCA' : ['L2B']},
}

class downloadHY(object):

    def __init__(self, username=None, password=None):
        '''
        支持下载FY3D、FY4A、FY4B的L1、L2级数据产品

        Parameters
        ----------
        username: str
            用户名
        password: str
            密码
        '''
        if username is not None and password is not None :
            self.ftp = ftppro(HY_FTP_URL, username, password)
            self.connect()

        self.dstfilelist = []

    def connect(self):
        try:
            self.ftp.connect()
            # self.ftp.close()
        except BaseException :
            raise Exception('登录失败，请连接并进行FTP账号注册。【https://osdds.nsoas.org.cn/】')

    def search(self, starttime, endtime=None, satid='HY-2B', instid='SCA', prodid='L2A',
               pattern=None):
        '''

        Parameters
        ----------
        starttime: datetime
            数据下载时间(UTC)
        endtime: datetime
            数据下载时间(UTC)
        satid: str
            卫星名, FY3D/FY4A/FY4B
        pattern: str
            模糊匹配条件
        skip: bool
            默认为False。如果为True，则跳过下载，直接返回文件名
        cover : bool
            默认为False。如果为True，则跳过下载，直接返回文件名

        Returns
        -------
        list
        下载文件名列表
        '''

        satid = self.CheckInfo(satid, instid, prodid)

        if endtime is None :
            endtime = starttime

        # 拼接目录
        matchfiles = []

        nowdate = starttime
        while nowdate <= endtime :

            searchpath = os.path.join('/', satid, instid, prodid)
            searchpath = searchpath.replace('\\','/')

            files = self.getFileList(searchpath, pattern='*%s*' %(nowdate.strftime('%Y%m%d')))

            matchfiles = self._checktime(matchfiles, starttime, endtime, files, satid)

            nowdate += datetime.timedelta(days=1)

        return matchfiles

    def CheckInfo(self, satid, instid, prodid):
        ''' 根据输入的卫星、载荷、产品ID，检查其规范性 '''
        if satid in ['HY-2B', 'HY2B', 'H2B']:
            SatID = 'HY-2B'
        elif satid in ['HY-2C', 'HY2C', 'H2C']:
            SatID = 'HY-2C'
        elif satid in ['HY-2D', 'HY2D', 'H2D']:
            SatID = 'HY-2D'
        elif satid in ['HY-2F', 'HY2F', 'H2F']:
            SatID = 'HY-2F'
        elif satid in ['CFOSAT']:
            SatID = 'CFOSAT'
        else:
            raise Exception('暂不支持该卫星【%s】数据下载。卫星名参考-->' %(satid), HY_Info.keys())

        if not instid in HY_Info[SatID] :
            raise Exception('暂不支持该卫星载荷【%s】【%s】数据下载。载荷名参考-->' %(satid, instid),
                            HY_Info[SatID].keys())

        if not prodid in HY_Info[SatID][instid] :
            raise Exception('暂不支持该卫星产品【%s】【%s】【%s】数据下载。产品ID参考-->' %(satid, instid, prodid),
                            HY_Info[SatID][instid])

        return SatID

    def download(self, outdir, filelist, skip=False, cover=False):
        ''' 下载数据文件 '''

        if not os.path.exists(outdir):
            os.makedirs(outdir)
            print('成功创建路径【%s】' %(outdir))

        count = len(filelist)
        for srcname in filelist:
            print('='*100)
            count -= 1
            file = os.path.basename(srcname)
            dstname = os.path.join(outdir, file)

            self.dstfilelist.append(dstname)
            if skip :
                continue
            stime = time.time()
            print(datetime.datetime.utcnow().strftime('【%Y-%m-%d %H:%M:%S(UTC)】'),
                  '开始下载文件【%d】:【%s】' %(count, srcname))

            if self.ftp.downloadFile(srcname, outdir, cover=cover):

                print(datetime.datetime.utcnow().strftime('【%Y-%m-%d %H:%M:%S(UTC)】'),
                      '成功下载文件【%d】:【%s】' %(count, dstname))

            etime = time.time()
            # print('cost %.2f sec...' %(etime - stime))

        return self.dstfilelist

    def listDir(self, path, pattern=None):
        '''
        列出远程路径下的文件或者文件夹
        Parameters
        ----------
        path: str
            远程路径
        pattern: str
            模糊匹配字段

        Returns
        -------
        list
        返回远程路径下的文件或文件夹
        '''

        files = self.ftp.listdir(path, pattern)
        files.sort()

        return files

    def getFileList(self, srcpath, pattern=None):
        '''
        获取下载文件列表
        Parameters
        ----------
        srcpath: str
            远程路径
        pattern : str
            模糊匹配参数

        Returns
        -------
        list
        所需下载的远程文件列表
        '''
        downfiles = []

        srcpath = srcpath.replace('\\', '/')

        files = self.ftp.listdir(srcpath, pattern)
        files.sort()
        for file in files :
            downflag = True

            if downflag :
                srcname = os.path.join(srcpath, file)
                srcname = srcname.replace('\\','/')

                downfiles.append(srcname)

        return downfiles

    def _checktime(self, matchfiles, starttime, endtime, files, satid, pattern=None):
        '''
        通过起始结束时间匹配满足条件的文件名
        :param matchfiles:
        :param starttime:
        :param endtime:
        :param files:
        :param pattern:
        :return:
        '''

        for file in files :
            if file in matchfiles :
                continue

            basename = os.path.basename(file)
            namelist = basename.split('_')
            for item in namelist :
                if starttime.strftime('%Y%m%d') in item :
                    if len(item) == 15 :
                        nowdate = datetime.datetime.strptime(item, '%Y%m%dT%H%M%S')
                        if (nowdate >= starttime) and (nowdate <= endtime) :
                            matchfiles.append(file)
                            break

        return matchfiles