# -*- coding:utf-8 -*-
'''
@Project  : lb_toolkits

@File     : downloadGFS.py

@Modify Time : 2022/8/11 15:34

@Author : Lee

@Version : 1.0

@Description :

'''

import os
import shutil
import datetime
from lb_toolkits.utils import spiderdownload
from lb_toolkits.utils import wget

class downloadGFS():

    def __init__(self):
        pass

    def searchfile(
            self,
            startdate,
            enddate=None,
            issuetime=0,
            forecasttime=[0],
            bbox=None,
    ) :
        '''
        参考：“https://nomads.ncep.noaa.gov/cgi-bin/filter_gfs_0p25.pl”
             “https://nomads.ncep.noaa.gov/pub/data/nccf/com/gfs/prod/”

        Parameters
        ----------

        nowdate: datetime
            下载时间
        issuetime: int
            发布时间，GFS是0、6、12、18点起始预报
        forecasttime: list
            根据预报时间往后多少小时
        bbox: list
            区域范围，[minX, minY, maxX, maxY]

        Returns
        -------

        '''

        issuetime = int(issuetime)
        if not issuetime in [0, 6, 12, 18] :
            raise Exception('forecast[%d] is not "0, 6, 12, 18", please check it...' %(issuetime))

        if enddate is None:
            enddate = startdate

        urls = []
        nowdate = startdate
        while nowdate <= enddate:
            for mhour in forecasttime :
                if bbox is None :
                    url = r'https://nomads.ncep.noaa.gov/pub/data/nccf/com/gfs/prod/' \
                          r'gfs.{YYYYMMDD}/{issuetime}/atmos/gfs.t{issuetime}z.pgrb2.0p25.f{forecasttime}'.format(
                        issuetime='%02d' %(issuetime),
                        forecasttime='%03d' %(mhour),
                        YYYYMMDD=nowdate.strftime('%Y%m%d')
                    )

                else:
                    url = r'https://nomads.ncep.noaa.gov/cgi-bin/filter_gfs_0p25.pl?' \
                          r'file=gfs.t{issuetime}z.pgrb2.0p25.f{forecasttime}&lev_100_mb=on&lev_2_mb=on&var_UGRD=on&subregion=&' \
                          r'leftlon={minX}&rightlon={maxX}&toplat={maxY}&bottomlat={minY}&' \
                          r'dir=%2Fgfs.{YYYYMMDD}%2F{issuetime}%2Fatmos'.format(
                        issuetime='%02d' %(issuetime),
                        forecasttime='%03d' %(mhour),
                        minX=bbox[0], maxX=bbox[2],
                        minY=bbox[1], maxY=bbox[3],
                        YYYYMMDD=nowdate.strftime('%Y%m%d'))

                outname = 'gfs.t{issuetime}z.pgrb2.0p25.f{forecasttime}'.format(
                    issuetime='%02d' %(issuetime),
                    forecasttime='%03d' %(mhour))

                urls.append((url, outname))
                nowdate += datetime.timedelta(days=1)

        return urls


    def download(self, outdir, urls, timeout=5*60, skip=False, cover=False, wgetpath=None):

        if not os.path.isdir(outdir):
            os.makedirs(outdir)

        for url, name in urls :
            outname = os.path.join(outdir, name)
            try:
                filename = wget(outdir,
                                url=url,
                                timeout=timeout,
                                skip_download=skip,
                                cover=cover,
                                wgetpath=wgetpath)
                if os.path.isfile(filename) :
                    shutil.move(filename, outname)
            except BaseException as e:
                print(e)



