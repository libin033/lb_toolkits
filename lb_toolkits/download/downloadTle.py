# -*- coding:utf-8 -*-
'''
@Project     : lb_toolkits

@File        : downloadTle.py

@Modify Time :  2023/6/28 9:22   

@Author      : Lee    

@Version     : 1.0   

@Description :

'''
import os
import sys
import time

import numpy as np
import datetime

try:
    from urllib2 import urlopen
except ImportError:
    from urllib.request import urlopen


# TLE_URLS = ('http://www.celestrak.com/NORAD/elements/active.txt',
#             'http://celestrak.com/NORAD/elements/weather.txt',
#             'http://celestrak.com/NORAD/elements/resource.txt',
#             'https://www.celestrak.com/NORAD/elements/cubesat.txt',
#             'http://celestrak.com/NORAD/elements/stations.txt',
#             'https://www.celestrak.com/NORAD/elements/sarsat.txt',
#             'https://www.celestrak.com/NORAD/elements/noaa.txt',
#             'https://www.celestrak.com/NORAD/elements/amateur.txt',
#             'https://www.celestrak.com/NORAD/elements/engineering.txt')
#

TLE_GROUPS = ('active',
              'weather',
              'resource',
              'cubesat',
              'stations',
              'sarsat',
              'noaa',
              'amateur',
              'engineering')

TLE_URLS = [f'https://celestrak.org/NORAD/elements/gp.php?GROUP={group}&FORMAT=tle'
            for group in TLE_GROUPS]

class downloadTle():

    def __init__(self, outdir):
        # print("Fetch TLE from the internet.")
        # urls = TLE_URLS

        for group in TLE_GROUPS:
            url = f'https://celestrak.org/NORAD/elements/gp.php?GROUP={group}&FORMAT=tle'

            # basename = os.path.basename(url)
            basename = '%s.txt' %(group)
            nowdate = datetime.datetime.utcnow()
            outname = os.path.join(outdir,
                                   nowdate.strftime('%Y'),
                                   nowdate.strftime('%Y%m%d'),
                                   basename)
            if not os.path.isfile(outname) :
                print('正在下载：【%s】' %(outname))
                self.spidertile(outname, url)
            else:
                print('文件已存在：【%s】' %(outname))

    def spidertile(self, outname, url):

        outdir = os.path.dirname(outname)
        if not os.path.isdir(outdir) :
            os.makedirs(outdir)

        if os.path.isfile(outname) :
            return None

        with open(outname, 'w') as fp :
            fid = urlopen(url)
            for l_0 in fid:
                l_0 = l_0.decode('utf-8')
                l_0=l_0.replace('\n','')
                l_0=l_0.replace('\r','')
                fp.write('%s\n' %l_0)
        fid.close()



if __name__ == '__main__':

    while True :
        nowdate = datetime.datetime.utcnow()
    
        print('开始处理：', nowdate)

        if nowdate.hour == 8 :
            try:
                downloadTle(outdir=r'./data/tle')
            except BaseException as e:
                print(e)
        print('开始休眠20分钟')
        time.sleep(20*60)

