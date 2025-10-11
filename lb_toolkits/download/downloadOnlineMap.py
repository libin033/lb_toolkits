# -*- coding:utf-8 -*-
'''
@Project     : lb_toolkits  
----------------------------------------
@File        : downloadOnlineMap.py  
----------------------------------------
@Modify Time : 2025/1/10  
----------------------------------------
@Author      : Lee  
----------------------------------------
@Desciption
----------------------------------------
      
 
'''
import os
import sys
import numpy as np
import datetime

import math
import os
import datetime
import shutil
import time
import requests
from tqdm import tqdm

from math import floor, pi, log, tan, atan, exp
from PIL import Image
from osgeo import gdal, osr


MAP_URLS = {
    "高德街道": "http://webrd02.is.autonavi.com/appmaptile?lang=zh_cn&size=1&scale=1&style=7&x={x}&y={y}&z={z}",
    "高德卫星图": "http://webst02.is.autonavi.com/appmaptile?lang=zh_cn&size=1&scale=1&style=6&x={x}&y={y}&z={z}",
    "GeoQ彩色": "https://map.geoq.cn/ArcGIS/rest/services/ChinaOnlineCommunity/MapServer/tile/{z}/{y}/{x}",
    "GeoQ灰色": "http://map.geoq.cn/arcgis/rest/services/ChinaOnlineStreetGray/MapServer/tile/{z}/{y}/{x}",
    "OpenStreetMap Mapnick" : "http://tile.openstreetmap.org/{z}/{x}/{y}.png",
    "OSM Cycle Map" : "http://tile.thunderforest.com/cycle/{z}/{x}/{y}.png",
    "OSM Black and White": "http://tiles.wmflabs.org/bw-mapnik/{z}/{x}/{y}.png",
    "ESRI Image": "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
    "ESRI Streets": "https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}",
    "ESRI Topo": "https://server.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/{z}/{y}/{x}",
    "World Light Gray Base": "https://server.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Base/MapServer/tile/{z}/{y}/{x}",
    "Carto Positron": "https://cartodb-basemaps-a.global.ssl.fastly.net/light_all/{z}/{x}/{y}.png",
    "cartocdn light nolabels": "https://basemaps.cartocdn.com/light_nolabels/{z}/{x}/{y}{r}.png",
    "Stamen Terrain": "http://a.tile.stamen.com/terrain/{z}/{x}/{y}.png",
}


class OnlineMap :

    def __init__(self, bbox=None, zoom=18, centre=None, radius=5, server="ESRI Image"):
        """
        """
        self.session = requests.Session()
        self.bbox = bbox
        self.centre = centre
        self.zoom = zoom
        self.server = server

        if centre is not None and bbox is None :
            self.centre = self.adjust_coordinates(centre, radius)


    def geturls(self, outname, zoom, server="ESRI Image"):

        outdir = os.path.dirname(outname)
        if not os.path.isdir(outdir):
            os.makedirs(outdir)

        x1, y1, x2, y2 = self.bbox
        pos1x, pos1y = self.wgs_to_tile(x1, y1, zoom)
        pos2x, pos2y = self.wgs_to_tile(x2, y2, zoom)

        lenx = pos2x - pos1x + 1
        leny = pos2y - pos1y + 1
        print("Total tiles number：{x} X {y}".format(x=lenx, y=leny))
        files = []

        outpic = Image.new('RGB', (lenx * 256, leny * 256))
        for j in range(int(pos1y), int(pos1y) + int(leny)) :
            for i in range(int(pos1x), int(pos1x) + int(lenx)) :
                url = self.get_url(server, i, j, zoom)
                outname = os.path.join(outdir, '%s_%s_%s.jpeg' %(i, j, zoom))
                if not os.path.isfile(outname) :
                    filename = self.download(outdir, url)
                    shutil.move(filename, outname)
                print(outname)
                try:
                    small_pic = Image.open(outname)
                except BaseException as e:
                    print(e)
                    continue
                outpic.paste(small_pic, ((i-pos1x) * 256, (j-pos1y) * 256))
                files.append(outname)
        for filename in files :
            os.remove(filename)

        outpic.save(outname)
        print('Tiles merge completed')


    def get_url(self, source, x, y, z):

        return MAP_URLS[source].format(x=x, y=y, z=z)

    def wgs_to_mercator(self, x, y):
        y = 85.0511287798 if y > 85.0511287798 else y
        y = -85.0511287798 if y < -85.0511287798 else y

        x2 = x * 20037508.34 / 180
        y2 = log(tan((90 + y) * pi / 360)) / (pi / 180)
        y2 = y2 * 20037508.34 / 180
        return x2, y2

    def mercator_to_wgs(self, x, y):
        x2 = x / 20037508.34 * 180
        y2 = y / 20037508.34 * 180
        y2 = 180 / pi * (2 * atan(exp(y2 * pi / 180)) - pi / 2)
        return x2, y2


    # --------------------------------------------------------------------------------------

    # -----------------Interchange between GCJ-02 to WGS-84---------------------------
    # All public geographic data in mainland China need to be encrypted with GCJ-02, introducing random bias
    # This part of the code is used to remove the bias
    def transformLat(self, x, y):
        ret = -100.0 + 2.0 * x + 3.0 * y + 0.2 * y * y + 0.1 * x * y + 0.2 * math.sqrt(abs(x))
        ret += (20.0 * math.sin(6.0 * x * math.pi) + 20.0 * math.sin(2.0 * x * math.pi)) * 2.0 / 3.0
        ret += (20.0 * math.sin(y * math.pi) + 40.0 * math.sin(y / 3.0 * math.pi)) * 2.0 / 3.0
        ret += (160.0 * math.sin(y / 12.0 * math.pi) + 320 * math.sin(y * math.pi / 30.0)) * 2.0 / 3.0
        return ret

    def transformLon(self, x, y):
        ret = 300.0 + x + 2.0 * y + 0.1 * x * x + 0.1 * x * y + 0.1 * math.sqrt(abs(x))
        ret += (20.0 * math.sin(6.0 * x * math.pi) + 20.0 * math.sin(2.0 * x * math.pi)) * 2.0 / 3.0
        ret += (20.0 * math.sin(x * math.pi) + 40.0 * math.sin(x / 3.0 * math.pi)) * 2.0 / 3.0
        ret += (150.0 * math.sin(x / 12.0 * math.pi) + 300.0 * math.sin(x / 30.0 * math.pi)) * 2.0 / 3.0
        return ret


    def delta(self, lat, lon):
        '''
        Krasovsky 1940
        //
        // a = 6378245.0, 1/f = 298.3
        // b = a * (1 - f)
        // ee = (a^2 - b^2) / a^2;
        '''
        a = 6378245.0
        ee = 0.00669342162296594323
        dLat = self.transformLat(lon - 105.0, lat - 35.0)
        dLon = self.transformLon(lon - 105.0, lat - 35.0)
        radLat = lat / 180.0 * math.pi
        magic = math.sin(radLat)
        magic = 1 - ee * magic * magic
        sqrtMagic = math.sqrt(magic)
        dLat = (dLat * 180.0) / ((a * (1 - ee)) / (magic * sqrtMagic) * math.pi)
        dLon = (dLon * 180.0) / (a / sqrtMagic * math.cos(radLat) * math.pi)

        return {'lat': dLat, 'lon': dLon}

    def outOfChina(self, lat, lon):
        if (lon < 72.004 or lon > 137.8347):
            return True
        if (lat < 0.8293 or lat > 55.8271):
            return True

        return False

    def gcj_to_wgs(self, gcjLon, gcjLat):
        if self.outOfChina(gcjLat, gcjLon):
            return (gcjLon, gcjLat)

        d = self.delta(gcjLat, gcjLon)

        return (gcjLon - d["lon"], gcjLat - d["lat"])


    def wgs_to_gcj(self, wgsLon, wgsLat):

        if self.outOfChina(wgsLat, wgsLon):
            return wgsLon, wgsLat

        d = self.delta(wgsLat, wgsLon)

        return wgsLon + d["lon"], wgsLat + d["lat"]

    def wgs_to_tile(self, j, w, z):

        isnum = lambda x: isinstance(x, int) or isinstance(x, float)
        if not (isnum(j) and isnum(w)):
            raise TypeError("j and w must be int or float!")

        if not isinstance(z, int) or z < 0 or z > 22:
            raise TypeError("z must be int and between 0 to 22.")

        if j < 0:
            j = 180 + j
        else:
            j += 180
        j /= 360  # make j to (0,1)

        w = 85.0511287798 if w > 85.0511287798 else w
        w = -85.0511287798 if w < -85.0511287798 else w
        w = log(tan((90 + w) * pi / 360)) / (pi / 180)
        w /= 180  # make w to (-1,1)
        w = 1 - (w + 1) / 2  # make w to (0,1) and left top is 0-point

        num = 2 ** z
        x = floor(j * num)
        y = floor(w * num)
        return x, y

    def pixls_to_mercator(self, zb):
        # Get the web Mercator projection coordinates of the four corners of the area according to the four corner coordinates of the tile
        inx, iny = zb["LT"]  # left top
        inx2, iny2 = zb["RB"]  # right bottom
        length = 20037508.3427892
        sum = 2 ** zb["z"]
        LTx = inx / sum * length * 2 - length
        LTy = -(iny / sum * length * 2) + length

        RBx = (inx2 + 1) / sum * length * 2 - length
        RBy = -((iny2 + 1) / sum * length * 2) + length

        # LT=left top,RB=right buttom
        # Returns the projected coordinates of the four corners
        res = {'LT': (LTx, LTy), 'RB': (RBx, RBy),
               'LB': (LTx, RBy), 'RT': (RBx, LTy)}
        return res

    def tile_to_pixls(self, zb):
        # Tile coordinates are converted to pixel coordinates of the four corners
        out = {}
        width = (zb["RT"][0] - zb["LT"][0] + 1) * 256
        height = (zb["LB"][1] - zb["LT"][1] + 1) * 256
        out["LT"] = (0, 0)
        out["RT"] = (width, 0)
        out["LB"] = (0, -height)
        out["RB"] = (width, -height)

        return out

    def saveTiff(self, outname, r, g, b, trans):

        driver = gdal.GetDriverByName('GTiff')
        dset_output = driver.Create(outname, r.shape[1], r.shape[0], 3, gdal.GDT_Byte)
        dset_output.SetGeoTransform(trans)

        proj = osr.SpatialReference()
        proj.ImportFromEPSG(4326)
        dset_output.SetSpatialRef(proj)

        dset_output.GetRasterBand(1).WriteArray(r)
        dset_output.GetRasterBand(2).WriteArray(g)
        dset_output.GetRasterBand(3).WriteArray(b)
        dset_output.FlushCache()
        dset_output = None


    def adjust_coordinates(self, centre=None, radius=5):

        center_x, center_y = centre

        x1 = center_x - radius/100.0
        x2 = center_x + radius/100.0
        y1 = center_y - radius/100.0
        y2 = center_y + radius/100.0

        return (x1, y1, x2, y2)

    def download(self, outdir, url, timeout=5*60, chunk_size=1024, skip_download=False, cover=False, continuing=False):
        """ 根据url连接下载远程文件 """

        download_url = url
        basename = os.path.basename(download_url)
        local_filename = os.path.join(outdir, basename)
        tempfile = local_filename + '.download'
        if skip_download:
            return local_filename

        if os.path.isfile(local_filename) :
            if cover :
                os.remove(local_filename)
                print('文件已存在，删除该文件后重新下载【%s】' %(local_filename))
            else:
                print('文件已存在，跳过下载该文件【%s】' %(local_filename))
                return local_filename

        file_size = self._getremotefilesize(url, timeout)

        headers = {}

        if continuing and os.path.isfile(tempfile) and file_size > 0:
            already_downloaded_bytes = os.path.getsize(tempfile)
            if already_downloaded_bytes < file_size :
                headers = {"Range": "bytes={}-".format(already_downloaded_bytes)}
                print('将继续断点续传：原数据【%dB】, 已下载【%dB】' %(file_size, already_downloaded_bytes))
            else:
                already_downloaded_bytes = 0
                continuing = False
        else:
            already_downloaded_bytes = 0
            continuing = False

        try:
            with self.session.get(
                    download_url, stream=True, allow_redirects=True,
                    timeout=timeout, headers=headers
            ) as r:
                if r.status_code != 200 :
                    return None

                nowtime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                with tqdm(
                        total=file_size, unit_scale=True, unit="B", desc=f"【{nowtime}】正在下载【{basename}】",
                        unit_divisor=1024, initial=already_downloaded_bytes,
                ) as pbar:

                    mode = "ab" if continuing else "wb"
                    with open(tempfile, mode) as f:
                        for chunk in r.iter_content(chunk_size=chunk_size):
                            if chunk:
                                f.write(chunk)
                                pbar.update(len(chunk))
            print(file_size, os.path.getsize(tempfile))
            time.sleep(0.5)
            if file_size == os.path.getsize(tempfile):
                shutil.move(tempfile, local_filename)
                print('成功下载【%s】' %(local_filename))
            elif file_size == -1 :
                shutil.move(tempfile, local_filename)
                print('成功下载【%s】' %(local_filename))
            # elif file_size <  os.path.getsize(tempfile) :
            #     print('下载错误，重新下载【%s】' %(local_filename))
            #     os.remove(local_filename)
            #     self._download(outdir, url, timeout, chunk_size=chunk_size, skip=skip, cover=cover)
            else:
                print('下载失败【%s】' %(local_filename))
        except requests.exceptions.Timeout:
            print("连接超时【{}】".format(timeout))
            return None

        return local_filename

    def _getremotefilesize(self, url, timeout):
        try:
            with self.session.get(
                    url, stream=True, allow_redirects=True,
                    timeout=timeout) as r:
                return int(r.headers.get("Content-Length"))
        except BaseException as e :
            return -1

