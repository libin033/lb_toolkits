# -*- coding:utf-8 -*-
'''
@Project  : lb_toolkits

@File     : downloadFY.py

@Modify Time : 2022/8/11 15:34

@Author : Lee

@Version : 1.0

@Description :

'''
import glob
import os
import time
import datetime
import tempfile

from lb_toolkits.utils import ftppro
from lb_toolkits.utils import spiderdownload


from .config import FY_FTP_URL

FYProdInfo = {
    'FY4A' : {
        'AGRI' : ['ACI', 'AMV',
                               'CFR', 'CIX', 'CLM', 'CLP', 'CLT', 'CTH', 'CTP', 'CTT',
                               'DLR', 'DSD', 'FHS', 'FOG', 'LPW', 'LSE', 'LST', 'OLR',
                               'QPE', 'RSR', 'SSI', 'SST', 'TBB', 'TFP', 'ULR'],
        'GIIRS' : ['AVP'],
    },
    'FY4B' : {
        'AGRI' : ['CTH', 'CTP', 'CTT', 'QPE'],
    },
    'FY3D' : {
        'MERSI' : ['CLA', 'NVI', 'PWS', 'PWV'],
    }

}

# FY3 10度块 编码对应关系
FY3Block10CoefX = {
    "00": 0.0,
    "10": 10.0,
    "20": 20.0,
    "30": 30.0,
    "40": 40.0,
    "50": 50.0,
    "60": 60.0,
    "70": 70.0,
    "80": 80.0,
    "90": 90.0,
    "A0": 100.0,
    "B0": 110.0,
    "C0": 120.0,
    "D0": 130.0,
    "E0": 140.0,
    "F0": 150.0,
    "G0": 160.0,
    "H0": 170.0,
    "I0": -10.0,
    "J0": -20.0,
    "K0": -30.0,
    "L0": -40.0,
    "M0": -50.0,
    "N0": -60.0,
    "O0": -70.0,
    "P0": -80.0,
    "Q0": -90.0,
    "R0": -100.0,
    "S0": -110.0,
    "T0": -120.0,
    "U0": -130.0,
    "V0": -140.0,
    "W0": -150.0,
    "X0": -160.0,
    "Y0": -170.0,
    "Z0": -180.0,
}

FY3Block10CoefY = {
    "80":  90.0,
    "70":  80.0,
    "60":  70.0,
    "50":  60.0,
    "40":  50.0,
    "30":  40.0,
    "20":  30.0,
    "10":  20.0,
    "00":  10.0,
    "90":   0.0,
    "A0": -10.0,
    "B0": -20.0,
    "C0": -30.0,
    "D0": -40.0,
    "E0": -50.0,
    "F0": -60.0,
    "G0": -70.0,
    "H0": -80.0,
}


class downloadFY :

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
            self.ftp = ftppro(FY_FTP_URL, username, password)
            self.connect()

        self.dstfilelist = []

    def connect(self):
        try:
            self.ftp.connect()
            # self.ftp.close()
        except BaseException :
            raise Exception('登录失败，请连接并进行FTP账号注册。http://fy4.nsmc.org.cn/data/en/data/realtime.html')

    def searchfile(self, orderfile=None, orderID=None, skip_download=False, cover=False, **kwargs):
        '''
        根据在风云官网提交的订单号或者订单文件信息，
        对风云卫星数据进行下载

        Parameters
        ----------
        orderfile : str
        orderID : str
        skip_download : bool
            是否跳过下载，默认为TRUE
            文件存在，如果skip为TRUE，就跳过该文件下载，
            如果skip为FALSE，则删除原文件后重新下载

        Returns
        -------

        '''
        if orderID is not None :
            orderurl = 'http://file.nsmc.org.cn/ORDERFILELIST/{orderid}.txt'.format(orderid=orderID)
            print(orderurl)
            tempdir = tempfile.gettempdir()

            spider = spiderdownload()
            orderfile = spider.download(tempdir, orderurl)

        if orderfile is None or not os.path.isfile(orderfile)  :
            raise Exception('订单文件不存在【%s】' %(orderfile))

        orderlist = self.readorderfile(orderfile)

        if orderID is not None :
            try:
                os.remove(orderfile)
            except BaseException :
                pass

        return orderlist


    def download(self, outdir, url, skip_download=False, cover=False, **kwargs):

        if isinstance(url, str) :
            urls = [url]
        elif isinstance(url, list) :
            urls = url

        user = None
        passwd = None
        host = None
        for url in urls :

            dict_info = self._spliturl(url)
            if 'user' not in dict_info :
                continue
            if 'passwd' not in dict_info :
                continue
            if 'host' not in dict_info :
                continue
            if 'filepath' not in dict_info :
                continue

            if user is None or passwd is None or host is None :
                user = dict_info['user']
                passwd = dict_info['passwd']
                host = dict_info['host']

                mc = ftppro(host, user=user, password=passwd)

            if user != dict_info['user'] or passwd != dict_info['passwd'] or host != dict_info['host'] :
                print('将切换账号：【%s】-->【%s】' %(user, dict_info['user']))
                user = dict_info['user']
                passwd = dict_info['passwd']
                host = dict_info['host']

                del mc
                mc = ftppro(host, user=user, password=passwd)

            mc.downloadFile(dict_info['filepath'], outdir, skip_download=skip_download, cover=cover)

    def download_fy_l1(self, dstpath, starttime, endtime=None, satid='FY4A',
                   instid='AGRI', regionid='DISK',resolution=0.04,
                   geoflag=False, pattern=None, skip=False, cover=False):
        '''
        下载FY3D MERSI、FY4A AGRI、GIITS、LMI L1数据文件

        Parameters
        ----------
        dstpath: str
            下载存储路径
        starttime: datetime
            数据下载时间(UTC)
        endtime: datetime
            数据下载时间(UTC)
        satid: str
            卫星名, FY3D/FY4A/FY4B
        instid: str
            载荷名 MERSI/AGRI/GIIRS/LMI
        regionid: str
            观测区域，DISK/REGC
        resolution: float
            degree，数据分辨率
        geoflag : bool
            default False,是否需要
            下载对应时间的GEO文件，默认是不下载，
            如果需要下载对应的GEO，需要将geoflag=True
        pattern: str
            模糊匹配条件
        skip: bool
            默认为False。如果为True，则跳过下载，直接返回文件名

        Returns
        -------
        list
        下载文件名列表
        '''

        # /FY4A/AGRI/L1/FDI/DISK/4000M/2022/20220609
        # /FY4A/GIIRS/L1/IRD/REGX/2022/20220609

        if endtime is None :
            endtime = starttime

        # 拼接目录
        if satid in ['FY4A'] :
            L1FileList = self._PathForFY4AL1(starttime, endtime,
                                                  satid=satid, instid=instid,
                                                  regionid=regionid, resolution=resolution,
                                                  pattern=pattern, geoflag=geoflag)

        elif satid in ['FY4B'] :
            raise Exception('官方暂未发布FY4B L1数据')
        elif satid in ['FY3D'] :
            L1FileList = self._PathForFY3DMERSIL1(starttime, endtime,
                                                       satid=satid, instid=instid,
                                                       regionid=regionid, resolution=resolution,
                                                       pattern=pattern, geoflag=geoflag)
        else:
            raise Exception('暂不支持【%s / %s】L1数据下载' %(satid, instid))


        return self.download(dstpath, L1FileList, skip_download=skip, cover=cover)

    def download_fy_l2(self, dstpath, starttime, endtime=None,
                       satid='FY4A', instid='AGRI', prodid='CLM',
                       regionid='DISK', resolution=0.04,
                       FY3Block10Flag=False, extent=None, shpname=None,
                       pattern=None, skip=False, cover=False):
        '''
        下载FY3D MERSI、FY4A AGRI、GIITS、LMI L1数据文件

        Parameters
        ----------
        dstpath: str
            下载存储路径
        starttime: datetime
            数据下载时间(UTC)
        endtime: datetime, optional
            数据下载时间(UTC)
        satid: str
            卫星名, FY3D/FY4A/FY4B
        instid: str
            载荷名 MERSI/AGRI/GIIRS/LMI
        prodid: str
            观测区域，DISK/REGC
        regionid: str
            观测区域，DISK/REGC
        resolution: float, optional
            degree，数据分辨率
        pattern: str, optional
        skip: bool
            默认为False。如果为True，则跳过下载，直接返回文件名

        Returns
        -------
        list
        下载文件名列表
        '''

        if endtime is None :
            endtime = starttime

        # 拼接目录
        if satid in ['FY4A'] :
            L2FileList = self._PathForFY4AL2(starttime, endtime,
                                             satid=satid, instid=instid,
                                             prodid=prodid, regionid=regionid,  pattern=pattern)

        elif satid in ['FY4B'] :
            L2FileList = self._PathForFY4BL2(starttime, endtime,
                                             satid=satid, instid=instid,
                                             prodid=prodid, regionid=regionid,  pattern=pattern)
        elif satid in ['FY3D'] :
            L2FileList = self._PathForFY3DMERSIL2(starttime, endtime,
                                                  satid=satid, instid=instid, prodid=prodid,
                                                  regionid=regionid, resolution=resolution,
                                                  FY3Block10=FY3Block10Flag, extent=extent, shpname=shpname,
                                                  pattern=pattern)
        else:
            raise Exception('暂不支持【%s %s】产品【%s】下载' %(satid, instid, prodid))


        if skip :
            return L2FileList
        else:
            self.download(dstpath, L2FileList, cover=cover)
            return L2FileList


    def _PathForFY4AL1(self, starttime, endtime,
                       satid='FY4A', instid='AGRI',
                       regionid='DISK', resolution=0.04,
                       pattern=None, geoflag=False):

        matchfiles = []

        strRes = '%dM' %(int(resolution * 100 * 1000))
        if not strRes in ['500M', '1000M', '2000M', '4000M'] :
            raise Exception("请确认输入的分辨率是否正确，只支持下载【'500M', '1000M', '2000M', '4000M'】")

        nowdate = starttime
        while nowdate <= endtime :

            if instid in ['AGRI'] :
                L1Path = os.path.join('/FY4A/AGRI/L1/FDI', regionid, strRes,
                                          nowdate.strftime("%Y"), nowdate.strftime("%Y%m%d"))
                GeoPath = os.path.join('/FY4A/AGRI/L1/FDI', regionid, 'GEO',
                                       nowdate.strftime("%Y"), nowdate.strftime("%Y%m%d"))
            elif instid in ['GIIRS'] :
                L1Path = os.path.join('/FY4A/GIIRS/L1/IRD/REGX/',
                                          nowdate.strftime("%Y"), nowdate.strftime("%Y%m%d"))
                GeoPath = None
            else:
                raise Exception('只支持下载FY4A AGRI和GIIRS L1近实时数据')

            files = self.getFileList(L1Path,
                                     pattern='*%s*%s*' %(nowdate.strftime('%Y%m%d%H'), strRes))
            matchfiles = self._checktime(matchfiles, starttime, endtime, files, satid)

            if geoflag :
                files = self.getFileList(GeoPath,
                                         pattern='*%s*%s*' %(nowdate.strftime('%Y%m%d%H'), strRes))
                matchfiles = self._checktime(matchfiles, starttime, endtime, files, satid)

            nowdate += datetime.timedelta(hours=1)

        return matchfiles

    def _PathForFY4AL2(self, starttime, endtime,
                       satid='FY4A', instid='AGRI', prodid=None,
                       regionid='DISK', resolution=0.04,
                       pattern=None):

        matchfiles = []

        self._checkprodid(satid, instid, prodid)

        nowdate = starttime
        while nowdate <= endtime :

            if instid in ['AGRI'] :
                L1Path = os.path.join('/', satid, instid, 'L2/', prodid, regionid, 'NOM',
                                      nowdate.strftime("%Y"), nowdate.strftime("%Y%m%d"))
            elif instid in ['GIIRS'] :
                L1Path = os.path.join('/', satid, instid, 'L2/', prodid, 'DWELL',
                                      nowdate.strftime("%Y"), nowdate.strftime("%Y%m%d"))
            else:
                raise Exception('只支持下载FY4A AGRI和GIIRS L2近实时数据')

            files = self.getFileList(L1Path,
                                     pattern='*%s*' %(nowdate.strftime('%Y%m%d%H')))
            matchfiles = self._checktime(matchfiles, starttime, endtime, files, satid)

            nowdate += datetime.timedelta(hours=1)

        return matchfiles

    def _PathForFY4BL2(self, starttime, endtime,
                       satid='FY4B', instid='AGRI', prodid=None,
                       regionid='DISK', resolution=0.04,
                       pattern=None):

        matchfiles = []

        self._checkprodid(satid, instid, prodid)

        nowdate = starttime
        while nowdate <= endtime :

            if instid in ['AGRI'] :
                L1Path = os.path.join('/', satid, instid, 'L2/', prodid, regionid, 'NOM',
                                      nowdate.strftime("%Y"), nowdate.strftime("%Y%m%d"))
            elif instid in ['GIIRS'] :
                L1Path = os.path.join('/', satid, instid, 'L2/', prodid, 'DWELL',
                                      nowdate.strftime("%Y"), nowdate.strftime("%Y%m%d"))
            else:
                raise Exception('只支持下载FY4B AGRI L2近实时数据')

            files = self.getFileList(L1Path,
                                     pattern='*%s*' %(nowdate.strftime('%Y%m%d%H')))
            matchfiles = self._checktime(matchfiles, starttime, endtime, files, satid)

            nowdate += datetime.timedelta(hours=1)

        return matchfiles

    def _PathForFY3DMERSIL1(self, starttime, endtime,
                            satid='FY3D', instid='MERSI',
                            regionid='GBAL', resolution=0.01,
                            pattern=None, geoflag=False):
        matchfiles = []
        strRes = '%dM' %(int(resolution * 100 * 1000))
        if not strRes in ['250M', '1000M'] :
            raise Exception("请确认输入的分辨率是否正确，只支持下载【'250M', '1000M'】")

        nowdate = starttime
        while nowdate <= endtime :
            if instid in ['MERSI'] :
                L1Path = os.path.join('/L1/', nowdate.strftime("%Y%m%d"))
                GeoPath = os.path.join('/L1/', nowdate.strftime("%Y%m%d"))
            else:
                raise Exception('只支持下载FY3D MERSI L1 近实时数据')

            files = self.getFileList(L1Path,
                                     pattern='*%s*%s*' %(nowdate.strftime('%Y%m%d_%H'), strRes))
            matchfiles = self._checktime(matchfiles, starttime, endtime, files, satid)

            if geoflag :
                if strRes in ['250M'] :
                    geoRes = 'GEOQK'
                elif strRes in ['1000M'] :
                    geoRes = 'GEO1K'

                files = self.getFileList(GeoPath,
                                         pattern='*%s*%s*' %(nowdate.strftime('%Y%m%d_%H'), geoRes))
                matchfiles = self._checktime(matchfiles, starttime, endtime, files, satid)

            nowdate += datetime.timedelta(hours=1)

        return matchfiles

    def _PathForFY3DMERSIL2(self, starttime, endtime,
                            satid='FY3D', instid='MERSI',
                            regionid='GBAL', resolution=0.01,
                            FY3Block10=False, extent=None, shpname=None,
                            pattern=None, prodid=None):

        self._checkprodid(satid, instid, prodid)

        matchfiles = []
        strRes = '%dM' %(int(resolution * 100 * 1000))
        if not strRes in ['250M', '1000M', '5000M'] :
            raise Exception("请确认输入的分辨率是否正确，只支持下载【'250M', '1000M', '5000M'】")

        nowdate = starttime
        while nowdate <= endtime :
            if instid in ['MERSI'] :
                L2Path = os.path.join('/L2L3/', prodid, '10DAY', strRes,
                                      nowdate.strftime("%Y"), nowdate.strftime("%Y%m%d"))
            else:
                raise Exception('只支持下载FY3D MERSI L2 近实时数据')

            files = self.getFileList(L2Path)
            matchfiles = self._checktime(matchfiles, starttime, endtime, files, satid)
            # blockid = self.maskBlock10(extent=extent, shpname=shpname)
            #
            # for item in blockid :
            #     for filename in files :
            #         basename = os.path.basename(filename)
            #         if item in basename :
            #             matchfiles.append(filename)

            nowdate += datetime.timedelta(days=1)

        return matchfiles

    def maskBlock10(self, extent=None, shpname=None):

        mpro = VectorPro()

        tmp_file = tempfile.NamedTemporaryFile(prefix="tmp_lb_toolkits_fishgrid_", delete=True)
        gridshp = tmp_file.name + '.shp'
        mpro.fishgrid(gridshp, extent=[-180, -90, 180, 90], xRes=10, yRes=10,
                      xindex=list(FY3Block10CoefX.keys()),
                      yindex=list(FY3Block10CoefY.keys()))

        if shpname is not None :
            tmp_file = tempfile.NamedTemporaryFile(prefix="tmp_lb_toolkits_clip_", delete=True)
            clipshp = tmp_file.name + '.shp'
            mpro.intersect(clipshp, srcfile=gridshp, clipfile=shpname)
        elif extent is not None :
            mpro.createPolygon()

        fieldvaluex = mpro.getField(clipshp, 'xindex')
        fieldvaluey = mpro.getField(clipshp, 'yindex')
        # print(clipshp)
        matchgrid = []
        for xitem, yitem in zip(fieldvaluex, fieldvaluey) :
            matchgrid.append(yitem+xitem)

        self._deltempshp(gridshp)
        self._deltempshp(clipshp)

        return matchgrid


    def readorderfile(self, filename):

        if not os.path.isfile(filename) :
            raise Exception('订单信息文件不存在【%s】' %(filename))


        with open(filename, 'r', encoding='gbk') as fp :
            lines = fp.readlines()
        order_list = []
        count = 0
        for line in lines :
            if len(line) <= 10 :
                continue

            line = line.replace('\n', '')
            order_list.append(line)

            count+=1

        print('共获取到【%d】个文件下载ID' %(count))

        return order_list

    def _spliturl(self, url):
        url = url.replace('\n','')
        if 'ftp://' in url :
            try:
                url = url.replace('ftp://', '')
                user = url.split(':')[0]

                index_usr = url.index(':')
                index_pwd = url.index('@')
                index_host = url.index('.cn')

                user = url[:index_usr]
                passwd = url[index_usr+1:index_pwd]
                host = url[index_pwd+1:index_host+3]
                filepath = url[index_host+3:]

                return {
                    'user' : user,
                    'passwd' : passwd,
                    'host' : host,
                    'filepath' : filepath,
                }
            except BaseException as e :
                return {}
        else:
            return {}

    # def download(self, outdir, url, skip_download=False, cover=False):
    #     '''
    #     下载数据文件
    #     :param outdir:
    #     :param url:
    #     :return:
    #     '''
    #
    #     if not os.path.exists(outdir):
    #         os.makedirs(outdir)
    #         print('成功创建路径【%s】' % (outdir))
    #
    #     count = len(url)
    #     for srcname in url:
    #         print('='*100)
    #         count -= 1
    #         file = os.path.basename(srcname)
    #         dstname = os.path.join(outdir, file)
    #
    #         self.dstfilelist.append(dstname)
    #         if skip_download :
    #             continue
    #         stime = time.time()
    #         print(datetime.datetime.utcnow().strftime('【%Y-%m-%d %H:%M:%S(UTC)】'),
    #               '开始下载文件【%d】:【%s】' %(count, srcname))
    #
    #         if self.ftp.downloadFile(srcname, outdir, cover=cover):
    #
    #             print(datetime.datetime.utcnow().strftime('【%Y-%m-%d %H:%M:%S(UTC)】'),
    #                   '成功下载文件【%d】:【%s】' %(count, dstname))
    #
    #         etime = time.time()
    #         print('耗时【%.2f秒】' %(etime - stime))
    #
    #     return self.dstfilelist

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
            # 根据传入的匹配参数，匹配文件名中是否包含相应的字符串
            # if pattern is not None and isinstance(pattern, list) :
            #     for item in pattern :
            #         if not item in file :
            #             downflag = False
            #             break
            # if pattern is not None and isinstance(pattern, list) :
            #     for item in pattern :
            #         if item in file :
            #             downflag = True
            #             break
            #         else:
            #             downflag = False

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
            if 'FY4' in satid :
                basename = os.path.basename(file)
                namelist = basename.split('_')
                for item in namelist :
                    if starttime.strftime('%Y%m%d') in item :
                        if len(item) == 14 :
                            nowdate = datetime.datetime.strptime(item, '%Y%m%d%H%M%S')
                            if (nowdate >= starttime) and (nowdate <= endtime) :
                                matchfiles.append(file)
                                break
                        elif len(item) == 8 :
                            nowdate = datetime.datetime.strptime(item, '%Y%m%d')
                            if (nowdate >= starttime) and (nowdate <= endtime) :
                                matchfiles.append(file)
                                break
            elif 'FY3' in satid :
                basename = os.path.basename(file)
                namelist = basename.split('_')
                for i in range(len(namelist)) :
                    item = namelist[i]
                    if starttime.strftime('%Y%m%d') in item :
                        if len(item) == 8 and len(namelist[i+1]) == 4 :
                            nowdate = datetime.datetime.strptime('%s_%s' %(item, namelist[i+1]),
                                                                 '%Y%m%d_%H%M')
                            if (nowdate >= starttime) and (nowdate <= endtime) :
                                matchfiles.append(file)
                                break


        return matchfiles

    def _checkprodid(self, satid, instid, prodid):
        if satid in FYProdInfo :
            SatInfo = FYProdInfo[satid]
            if instid in SatInfo :
                if prodid in SatInfo[instid] :
                    return True
                else:
                    raise Exception('产品【%s】不在官方发布【%s/%s】的产品范围内，请参考风云官网发布产品详情！'
                                    %(prodid, satid, instid), SatInfo[instid])
                    return False
            else:
                raise Exception('暂不支持【%s/%s】下载' %(satid, instid), '当前支持', list(SatInfo.keys()))
        else:
            raise Exception('暂不支持【%s】卫星下载' %(satid), '当前支持', list(FYProdInfo.keys()))

    def _deltempshp(self, shpname):
        filelist = glob.glob(shpname.replace('.shp', '.*'))
        for filename in filelist :
            if os.path.isfile(filename) :
                os.remove(filename)