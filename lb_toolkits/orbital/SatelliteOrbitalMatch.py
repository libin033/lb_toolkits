# -*- coding:utf-8 -*-
'''
@Project     : lb_toolkits

@File        : SatelliteOrbitalMatch.py

@Modify Time :  2023/1/10 17:26   

@Author      : Lee    

@Version     : 1.0   

@Description :

'''
import os
import sys
import numpy as np
import datetime

from orbital import Orbital
from tlefile import SATELLITES

Deg2Rad = np.pi / 180.0
Rad2Deg = 180.0 / np.pi

class SatelliteOrbitalMatch():

    def __init__(self):
        pass

    def matchPos(self, satid, starttime, endtime, pos, tilefile=None, distance=5000.0, timestep=2.0):

        sat_orbit_lon, sat_orbit_lat, mtime = self.getOrbitPos(satid, starttime, endtime, tilefile, timestep)

        dist = self.calc_earth_distance(lat1=pos[1], lon1=pos[0], lat2=sat_orbit_lat, lon2=sat_orbit_lon)

        flag = dist<=distance

        bias = mtime[dist<=distance]

        def diftime(x1, x2):
            return (x2 - x1).total_seconds()

        diftimelist = np.array(list(map(diftime, bias[:-1], bias[1:])))
        index = np.where(diftimelist>timestep)

        count = len(index[0])
        if count == 0 :
            print('未匹配卫星观测时间')
            return None
        print(count)
        for i in range(count+1) :
            if i == 0 :
                print(bias[0], bias[index[0][i]])
            elif i == count:
                print(bias[index[0][i-1]+1], bias[-1])
            else:
                print([bias[index[0][i-1]]], bias[index[0][i]])

        # from lb_toolkits.tools import writenc, writencfortimes
        # outname = r'D:\DATA\test.nc'
        # writencfortimes(outname, 'time', mtime, overwrite=1)
        # writenc(outname, 'latitude', sat_orbit_lat, dimension=('time', ), overwrite=0)
        # writenc(outname, 'longitude', sat_orbit_lon, dimension=('time', ), overwrite=0)
        # writenc(outname, 'distance', dist, dimension=('time', ),
        #         dictsdsinfo={'coordinate': 'latitude longitude'}, overwrite=0)

    # def getcrosstime(self, distance, diftime):



    def registerSatID(self, satid, id):
        if satid.upper() in SATELLITES :
            print('卫星【%s】已注册卫星匹配，将跳过' %(satid.upper()))
            return None

        PKG_CONFIG_DIR = os.path.join(os.path.realpath(os.path.dirname(__file__)), 'parm')

        """Add platform numbers to platforms.txt."""
        os.getenv('PPP_CONFIG_DIR', PKG_CONFIG_DIR)
        platform_file = None
        if 'PPP_CONFIG_DIR' in os.environ:
            platform_file = os.path.join(os.environ['PPP_CONFIG_DIR'], 'platforms.txt')
        if not platform_file or not os.path.isfile(platform_file):
            platform_file = os.path.join(PKG_CONFIG_DIR, 'platforms.txt')

        try:
            fid = open(platform_file, 'a')
            fid.write('%s %s\n' %(satid.upper(), id))
            fid.close()
            SATELLITES[satid.upper()] = id
            print('成功注册卫星【%s %s】' %(satid.upper(), id))
        except IOError:
            raise Exception("Platform file %s not found.", platform_file)

    def check(self, satid, starttime, tilefile):

        if not satid.upper() in SATELLITES :
            raise Exception('该卫星【%s】不在处理范围，请先通过registerSatID进行卫星匹配注册' %(satid))

        if tilefile is not None :
            if not os.path.isfile(tilefile) :
                tilefile = None

        difftime = (datetime.datetime.utcnow() - starttime).total_seconds()
        threshold = 7 * 24 * 60 * 60  # 只能计算近7天
        if difftime > threshold or difftime < -threshold :
            if tilefile is None :
                raise Exception('输入的匹配时间与当前时间超过7日，请输入有效的tile文件')

    def getOrbitPos(self, satid, starttime, endtime, tilefile=None, timestep=2.0):
        self.check(satid, starttime, tilefile)

        orb = Orbital(satid, tle_file=tilefile)

        # difftime = (endtime-starttime).total_seconds()*1000
        #
        # def timechange(i):
        #     return starttime+datetime.timedelta(milliseconds=i)
        #
        # timelist = np.arange(0, difftime, 100)

        difftime = (endtime-starttime).total_seconds()

        def timechange(i):
            return starttime+datetime.timedelta(seconds=i)

        timelist = np.arange(0, difftime, timestep)
        mtime = np.array(list(map(timechange, timelist)))

        lon, lat, alt = orb.get_lonlatalt(mtime)

        return lon, lat, mtime

    def calc_earth_distance(self, lat1, lon1, lat2, lon2) :
        '''  计算球面两点之间距离（KM） '''
        lon11 = lon1 * Deg2Rad
        lat11 = lat1 * Deg2Rad
        lon21 = lon2 * Deg2Rad
        lat21 = lat2 * Deg2Rad

        dlon = lon21 - lon11
        dlat = lat21 - lat11
        h = np.sin(dlat/2)**2 + np.cos(lat11) * np.cos(lat21) * np.sin(dlon/2)**2
        distance = 2 * 6371.009 * np.arcsin(np.sqrt( h )) # 地球平均半径，6371km

        return distance

if __name__ == '__main__':

    startdate = datetime.datetime.strptime('20230110', '%Y%m%d')
    enddate   = datetime.datetime.strptime('20230111', '%Y%m%d')

    mpro = SatelliteOrbitalMatch()
    mpro.registerSatID('FY-3D', '43010')
    mpro.matchPos('FY-3D', startdate, enddate, pos=[105.0, 30.0], tilefile=None)



