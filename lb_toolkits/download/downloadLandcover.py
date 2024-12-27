# -*- coding:utf-8 -*-
'''
@Project     : lb_toolkits

@File        : downloadLandcover.py

@Modify Time :  2022/11/11 17:11   

@Author      : Lee    

@Version     : 1.0   

@Description :

'''
import os
import numpy as np
from dateutil.relativedelta import relativedelta
from lb_toolkits.utils import spiderdownload

class downloadLandcover(spiderdownload):

    def searchfile(
            self,
            startdate,
            enddate=None,
            bbox=None,
            shapename=None,
            **kwargs
    ):
        if enddate is None:
            enddate = startdate

        if shapename is not None :
            bbox = self.get_bbox(shapename)

        colid, rowid = self.get_extent(bbox)

        # 从public替换为v003
        # root_url = r'https://lulctimeseries.blob.core.windows.net/lulctimeseriespublic/lc{year}/' \
        #            r'{colid}{rowid}_{sdate}-{edate}.tif'
        root_url = r'https://lulctimeseries.blob.core.windows.net/lulctimeseriesv003/lc{year}/' \
                   r'{colid}{rowid}_{sdate}-{edate}.tif'


        urllist = []

        nowdate = startdate
        while nowdate <= enddate:
            for row, col in zip(rowid, colid) :
                url = root_url.format(
                    year=nowdate.strftime('%Y'),
                    colid = '%02d' %(col),
                    rowid = row,
                    sdate = nowdate.strftime('%Y0101'),
                    edate = (nowdate+relativedelta(years=1)).strftime('%Y0101'),
                )
                urllist.append(url)
            nowdate += relativedelta(years=1)

        return urllist

    def download(self, outdir, url, tries=3, timeout=5*60, skip_download=False, cover=True, continuing=False, **kwargs):
        try:
            os.makedirs(outdir, exist_ok=True)

            if isinstance(url, list):
                filename = []
                for url1 in url:
                    filename1 = self._download(outdir, url1, timeout=timeout, skip_download=skip_download, cover=cover, continuing=continuing)
                    filename.append(filename1)
            elif isinstance(url, str):
                filename = self._download(outdir, url, timeout=timeout, skip_download=skip_download, cover=cover, continuing=continuing)
            return filename
        except BaseException as e :
            print('下载失败【%s】' %(url))
            return None


    def from_tsinghua(self, outdir,  minX=70, minY=10, maxX=140, maxY=55, skip=False):

        urllist = []
        for lat in np.arange(int(np.floor(minY)/2)*2, np.ceil(maxY), step=2) :
            for lon in np.arange(int(np.floor(minX)), np.ceil(maxX), step=2) :
                if lat < -90 or lat > 90 :
                    continue

                if lon < -180 or lat > 180 :
                    continue

                if lat >= 0 :
                    strlat = 'N%02d' %(lat)
                else:
                    strlat = 'S%02d' %(lat)

                if lon >= 0 :
                    strlon = 'E%03d' %(lon)
                else:
                    strlon = 'W%03d' %(lon)

                url = r'http://data.ess.tsinghua.edu.cn/data/fromglc10_2017v01/' \
                      r'fromglc10v01_%d_%d.tif' %(lat, lon)
                urllist.append(url)
                try:
                    self.download(outdir, url=url, skip=skip)
                except BaseException as e :
                    print('下载失败【%s】' %(url))
        return urllist

    def from_esri(self, outdir, nowdate, extent=None, shapename=None, skip=False):
        '''

        :param nowdate:
        :param extent: (minX, minY, maxX, maxY)
        :param shapename:
        :return:
        '''


        if shapename is not None :
            extent = self.get_bbox(shapename)

        colid, rowid = self.get_extent(extent)

        # 从public替换为v003
        # root_url = r'https://lulctimeseries.blob.core.windows.net/lulctimeseriespublic/lc{year}/' \
        #            r'{colid}{rowid}_{sdate}-{edate}.tif'
        root_url = r'https://lulctimeseries.blob.core.windows.net/lulctimeseriesv003/lc{year}/' \
                   r'{colid}{rowid}_{sdate}-{edate}.tif'


        urllist = []
        for row, col in zip(rowid, colid) :
            url = root_url.format(
                year=nowdate.strftime('%Y'),
                colid = '%02d' %(col),
                rowid = row,
                sdate = nowdate.strftime('%Y%m%d'),
                edate = (nowdate+relativedelta(years=1)).strftime('%Y%m%d'),
            )
            urllist.append(url)
            try:
                self.download(outdir, url=url, skip=skip)
            except BaseException as e :
                print('下载失败【%s】' %(url))

        return urllist


    def get_extent(self, extent) :
        ''' (minX, minY, maxX, maxY) '''

        rowinfo = {
            'C' : -72,
            'D' : -64,
            'E' : -56,
            'F' : -48,
            'G' : -40,
            'H' : -32,
            'J' : -24,
            'K' : -16,
            'L' : -8,
            'M' : 0,
            'N' : 8,
            'P' : 16,
            'Q' : 24,
            'R' : 32,
            'S' : 40,
            'T' : 48,
            'U' : 56,
            'V' : 64,
            'W' : 72,
            'X' : 84
        }

        scol = int((extent[0] - (-180)) / 6.0)
        ecol = int((extent[2] - (-180)) / 6.0)
        col = np.arange(scol, ecol+1)+1

        for key in rowinfo :
            if extent[1] < rowinfo[key] :
                srow = key
                break

        for key in rowinfo :
            if extent[3] < rowinfo[key] :
                erow = key
                break
            if extent[3] >= 84 :
                erow = 'X'
                break

        row = []
        for i in range(ord(srow),ord(erow)+1) :
            if chr(i) in rowinfo :
                row.append(chr(i))

        colid, rowid = np.meshgrid(col, row)

        return colid.reshape(-1), rowid.reshape(-1)

    def get_bbox(self, shapename, encoding='gbk'):
        import shapefile

        shpfp = shapefile.Reader(shapename, encoding=encoding)

        return shpfp.bbox


