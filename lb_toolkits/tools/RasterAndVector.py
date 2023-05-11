# -*- coding:utf-8 -*-
'''
@Project  : lb_toolkits

@File     : RasterAndVector.py

@Modify Time : 2022/8/11 15:34

@Author : Lee

@Version : 1.0

@Description :
栅格和矢量数据文件操作

'''
import glob
import os
import sys
import numpy as np
import shapefile
from .jsonpro import writejson
from tqdm import tqdm
from osgeo import gdal, ogr, osr, gdalconst


class RasterPro() :

    def __init__(self, encoding='GBK'):
        gdal.SetConfigOption("GDAL_FILENAME_IS_UTF8", "YES")
        gdal.SetConfigOption("SHAPE_ENCODING", encoding)
        gdal.UseExceptions()
        ogr.RegisterAll()

    def mask(self, InRaster, MaskShp, burn_name=None, burn_values=None):
        '''
        根据参考的tiff文件创建同等投影类型和数据维度的掩膜文件
        ref_tif--参考模板的geotiff文件
        input_shp--待转换的掩膜矢量文件
        burn_name--栅格化的属性字段名称
        :param InRaster:
        :param MaskShp:
        :param burn_name:
        :param burn_values:
        :return:
        '''
        ref_info=gdal.Open(InRaster)
        ref_data=ref_info.GetRasterBand(1).ReadAsArray()
        y_size,x_size=ref_data.shape

        geotransform=ref_info.GetGeoTransform()
        srs=ref_info.GetProjection()
        ref_info=None
        ref_data=None
        vector=ogr.Open(MaskShp)
        vl=vector.GetLayer(0)
        dst_ds = gdal.GetDriverByName('MEM').Create('',x_size,y_size,1,gdal.GDT_Byte)
        dst_ds.SetGeoTransform(geotransform)  # specify gettransform
        dst_ds.SetProjection(srs)  # export coords to file
        if burn_name is not None :
            gdal.RasterizeLayer(dst_ds,[1],vl,options=["ATTRIBUTE=%s"%burn_name])
        if burn_values is not None :
            gdal.RasterizeLayer(dst_ds,[1],vl,burn_values=burn_values)
        vector=None
        bd=dst_ds.GetRasterBand(1)
        dd=bd.ReadAsArray()
        # dst_ds.FlushCache()
        dst_ds=None

        return dd

    def resample(self):
        raise Exception('本功能待开发，请耐心等待')

    def clip(self, dsttif, srctif, shpname, fillvalue=None, resolution=None):
        # raise Exception('本功能待开发，请耐心等待')
        vec = ogr.Open(shpname)
        layer = vec.GetLayer()
        extent = layer.GetExtent()
        minX, maxX, minY, maxY = extent
        gdal.Warp(
            dsttif, srctif,
            format = 'GTiff',
            outputBounds=(minX, minY, maxX, maxY) ,  # (minX, minY, maxX, maxY)
            cutlineDSName=shpname, cropToCutline=True,
            xRes=resolution, yRes=resolution,
            dstNodata=fillvalue, creationOptions=["COMPRESS=LZW"]
        )

    def merge(self, filelist, outname=None, resolution=None, fillvalue=None,
              epsg=4326, extent=None, resampleAlg=0):

        if resampleAlg == 0:
            resampleType = gdalconst.GRA_NearestNeighbour
        elif resampleAlg == 1:
            resampleType = gdalconst.GRA_Bilinear
        else:
            resampleType = gdalconst.GRA_Cubic

        if outname is None :
            mode = 'MEM'
            outname=''
        else:
            mode = 'GTiff'
        options = gdal.WarpOptions(
            dstSRS='EPSG:%d' %(epsg),
            format=mode,
            outputBounds=extent,    # (minX, minY, maxX, maxY)
            resampleAlg=resampleType,
            xRes=resolution, yRes=resolution,
            dstNodata=fillvalue,
            creationOptions=["COMPRESS=LZW"])
        ds = gdal.Warp(outname, filelist, options=options)

        if outname is None :
            im_data = ds.ReadAsArray(0, 0, ds.RasterXSize, ds.RasterYSize)#获取数据
            ds = None

            return im_data
        else:
            return outname

    def to_vector(self, shpname, rastername, layername=None, field=None, geom_type=ogr.wkbMultiPolygon):
        '''
        栅格转矢量
        :param shpname: 输出的矢量文件名
        :param rastername: 输入的栅格数据名
        :param layername: option, 待转图层名称
        :param field: option，图层属性字段名
        :return:
        '''
        rasterid = gdal.Open(rastername)
        inband = rasterid.GetRasterBand(1)
        maskband = inband.GetMaskBand()

        prj = osr.SpatialReference()
        prj.ImportFromWkt(rasterid.GetProjection())

        drv = ogr.GetDriverByName('ESRI Shapefile')
        if os.path.isfile(shpname) :
            drv.DeleteDataSource(shpname)

        polygon = drv.CreateDataSource(shpname)
        if layername is not None :
            poly_layer = polygon.CreateLayer(layername, srs=prj,
                                             geom_type=geom_type)
        else:
            poly_layer = polygon.CreateLayer(rastername[:-4], srs=prj,
                                             geom_type=geom_type)

        if field is not None :
            newfield = ogr.FieldDefn(field, ogr.OFTReal)
        else:
            newfield = ogr.FieldDefn('value', ogr.OFTReal)
        poly_layer.CreateField(newfield)

        gdal.FPolygonize(inband, maskband, poly_layer, 0)
        polygon.SyncToDisk()
        polygon = None

class VectorPro():
    '''
    https://blog.csdn.net/summer_dew/article/details/87930241
    '''
    def __init__(self, encoding='GBK'):
        gdal.SetConfigOption("GDAL_FILENAME_IS_UTF8", "YES")  # 支持文件名称和文件路径中文
        gdal.SetConfigOption("SHAPE_ENCODING", encoding)      # 支持属性字段中的中文
        gdal.UseExceptions()
        ogr.RegisterAll()


    def split(self, outpath, shapefilename, field):
        """
        拆分矢量文件为多个单要素矢量文件,注意拆分后的fid需要重置。
        :param shapefilename: 要拆分的矢量文件
        :param outpath: 生成的矢量文件保存目录
        :param field: 根据提供的字段进行矢量拆分
        :return:
        """
        if not os.path.isdir(outpath) :
            os.makedirs(outpath)

        data = ogr.Open(shapefilename)
        layer = data.GetLayer()
        spatial = layer.GetSpatialRef()
        geomType = layer.GetGeomType()
        layerDefn = layer.GetLayerDefn()
        fieldCount = layerDefn.GetFieldCount()
        feature = layer.GetNextFeature()
        while feature:
            fid = feature.GetFieldAsString(field)
            fileName, layerName = str(fid), str(fid)
            driverName = "ESRI Shapefile"
            driver = ogr.GetDriverByName(driverName)
            outShapeFileName = fileName + ".shp"
            outShapeFilePath = os.path.join(outpath, outShapeFileName)
            outData = driver.CreateDataSource(outShapeFilePath)
            gdal.SetConfigOption("SHAPE_ENCODING", "CP936")
            outLayer = outData.CreateLayer(layerName, spatial, geomType)
            for fieldIndex in range(fieldCount):
                fieldDefn = layerDefn.GetFieldDefn(fieldIndex)
                outLayer.CreateField(fieldDefn)
            outLayer = outData.GetLayer()
            feature.SetFID(0)
            outLayer.CreateFeature(feature)
            outData.Destroy()
            feature = layer.GetNextFeature()
        data.Destroy()

        return True

    def to_raster(self, outname, shpname, field, resolution,
                  fillvalue=None, all_touch=False):
        '''
        矢量转栅格
        :param outname: 输出栅格文件的名称
        :param shpname: 输入矢量文件的名称
        :param resolution: 输出栅格数据的分辨率
        :param field: str, 矢量文件中的字段信息转换成栅格数据的像元值
        :param fillvalue: 输出tif的填充值（NoData）
        :param all_touch: bool，是否进行八方向处理
        :return:
        '''
        vec = ogr.Open(shpname)
        layer = vec.GetLayer()

        extent = layer.GetExtent()
        srs = layer.GetSpatialRef()

        feature = layer.GetFeature(0)
        # for feat in layer.schema :
        #     name = feat.GetName()#获取字段名称
        #     if name == field :
        #         type = feat.GetTypeName()#获取字段类型
        #         type = feat.GetField(field)#获取字段类型
        #         print('字段名称：%s ,字段类型：%s'%(name, type))

        fid = feature.GetField(field)
        dtype = str(type(fid))

        dtype = getNPDType(dtype)

        lonmin, lonmax, latmin, latmax = extent

        line = int(np.ceil((latmax - latmin)/resolution))
        pixel = int(np.ceil((lonmax - lonmin)/resolution))
        band = 1

        trans = [lonmin, resolution, 0, latmax, 0, -resolution]

        driver = gdal.GetDriverByName('GTiff')
        ds = driver.Create(outname, pixel, line, band, dtype)

        ds.SetGeoTransform(trans)
        ds.SetProjection(str(srs))

        bands = ds.GetRasterBand(1)
        if fillvalue is not None :
            bands.SetNoDataValue(fillvalue)

        # bands.FlushCache()

        if all_touch :
            all_touch = 'True'
        else:
            all_touch = 'False'

        if field :
            gdal.RasterizeLayer(ds, [1], layer,
                                options=["ALL_TOUCHED="+all_touch, "ATTRIBUTE="+field])
        else:
            gdal.RasterizeLayer(ds, [1], layer,
                                options=["ALL_TOUCHED="+all_touch])

    def to_geojson(self, outname, shapename, shp_encoding='utf-8', json_encoding='utf-8'):

        reader = shapefile.Reader(shapename, encoding=shp_encoding)
        fields = reader.fields[1:]
        fieldname = [field[0] for field in fields]
        buffer = []
        for sr in tqdm(reader.shapeRecords()) :
            record = sr.record

            record = [r.decode('gb2312', 'ignore') if isinstance(r, bytes) else r for r in record]

            attr = dict(zip(fieldname, record))

            geom = sr.shape.__geo_interface__

            buffer.append(dict(type='Feature',
                               geometry=geom,
                               properties=attr))

        writejson(outname, dict(type= 'FeatureCollection', features=buffer))

    def VectorTranslate(self, shpname, outdir,
                        format="GeoJSON", accessMode=None, dstSrsESPG=4326,
                        selectFields=None, geometryType="POLYGON", dim="XY"):
        '''
        转换矢量文件，包括坐标系，名称，格式，字段，类型，纬度等。

        Parameters
        ----------
        shpname : str
            要转换的矢量文件
        outdir : str
            生成矢量文件保存目录
        format : str
            矢量文件格式，强烈建议不要使用ESRI Shapefile格式。
        accessMode : str
            None代表creation,'update','append','overwrite'
        dstSrsESPG : str
            目标坐标系EPSG代码，4326是wgs84地理坐标系
        selectFields : str
            需要保留的字段列表如果都保留，则为None
        geometryType : str
            几何类型,"POLYGON","POINT"。。。
        dim : str
            新矢量文件坐标纬度,建议查阅官方API。
        Returns
        -------

        '''

        data = ogr.Open(shpname)
        layer = data.GetLayer()
        spatial = layer.GetSpatialRef()
        layerName = layer.GetName()
        data.Destroy()
        dstSRS = osr.SpatialReference()
        dstSRS.ImportFromEPSG(int(dstSrsESPG))
        if format == "GeoJSON":
            destDataName = layerName + ".geojson"
            destDataPath = os.path.join(outdir, destDataName)
        elif format == "ESRI Shapefile":
            destDataName = os.path.join(outdir, layerName)
            flag = os.path.exists(destDataName)
            os.makedirs(destDataName) if not flag else None
            destDataPath = os.path.join(destDataName, layerName + ".shp")
        else:
            print("不支持该格式！")
            return
        options = gdal.VectorTranslateOptions(
            format=format,
            accessMode=accessMode,
            srcSRS=spatial,
            dstSRS=dstSRS,
            reproject=True,
            selectFields=selectFields,
            layerName=layerName,
            geometryType=geometryType,
            dim=dim
        )
        gdal.VectorTranslate(
            destDataPath,
            srcDS=shpname,
            options=options
        )
        return destDataPath

    def createPoint(self, shpname, coords, dictfield={}, layername=None, epsg=4326):
        '''
        利用GDAL 创建点矢量，将point转换成矢量数据

        Parameters
        ----------
        shpname : str
            输出文件名
        coords: list
            eg. [[lon1, lat1], [lon2, lat2],... ]
        epsg: int

        Returns
        -------
            None
        '''

        driver = ogr.GetDriverByName('ESRI Shapefile')
        # 如果文件存在，则删除后再创建
        if os.access(shpname, os.F_OK) :
            driver.DeleteDataSource(shpname)

        srs = osr.SpatialReference()
        srs.ImportFromEPSG(int(epsg))

        if layername is None :
            layername = os.path.basename(shpname).replace('.shp','')

        ds = driver.CreateDataSource(shpname)
        lyr = ds.CreateLayer(layername, srs, ogr.wkbPoint)
        for key in dictfield :
            fieldName = ogr.FieldDefn(key, ogr.OFTString)
            lyr.CreateField(fieldName)

        if isinstance(coords, list) :
            for item in coords:
                val_lat = float(item[1])
                val_lon = float(item[0])

                wkt = 'POINT(%f %f)' %(val_lon, val_lat)

                geom = ogr.CreateGeometryFromWkt(wkt)
                feature = ogr.Feature(lyr.GetLayerDefn())
                feature.SetGeometry(geom)
                lyr.CreateFeature(feature)
        else:
            raise Exception('coords类型必须是list')

        ds = None
        driver =None

    def createPolyline(self, shpname, coords, dictfield={}, layername=None, epsg=4326):
        '''
        利用GDAL 创建线矢量，将polyline转换成矢量数据

        Parameters
        ----------
        shpname : str
            输出文件名
        coords: list
            eg. [
                    [[lon11, lat11], [lon12, lat12],... ],  # line1
                    [[lon21, lat21], [lon22, lat22],... ],  # line2
                ]
        epsg: int

        Returns
        -------
            None
        '''

        driver = ogr.GetDriverByName('ESRI Shapefile')
        if os.access(shpname, os.F_OK) :
            driver.DeleteDataSource(shpname)

        srs = osr.SpatialReference()
        srs.ImportFromEPSG(int(epsg))

        if layername is None :
            layername = os.path.basename(shpname).replace('.shp','')

        ds = driver.CreateDataSource(shpname)
        lyr = ds.CreateLayer(layername, srs, ogr.wkbLineString)

        for key in dictfield :
            fieldName = ogr.FieldDefn(key, ogr.OFTString)
            lyr.CreateField(fieldName)

        if isinstance(coords, list) :
            # 逐线创建
            for coord in coords :
                count = len(coord)
                wkt = 'LINESTRING('
                for i in range(count) :
                    if i == count-1:
                        wkt += '%f %f' %(coord[i][0], coord[i][1])
                    else:
                        wkt += '%f %f,' %(coord[i][0], coord[i][1])
                wkt += ')'
                geom = ogr.CreateGeometryFromWkt(wkt)
                feature = ogr.Feature(lyr.GetLayerDefn())
                feature.SetGeometry(geom)
                lyr.CreateFeature(feature)
        else:
            raise Exception('coords类型必须是list')

        ds = None
        driver =None

    def createPolygon(self, shpname, coords, dictfield={}, layername=None, epsg=4326):
        '''
        利用GDAL 创建面矢量，将polygon转换成矢量数据

        Parameters
        ----------
        shpname : str
            输出文件名
        coords: list
            eg. [
                    [[lon11, lat11], [lon12, lat12],... ],  # polygon1
                    [[lon21, lat21], [lon22, lat22],... ],  # polygon2
                ]
        epsg: int

        Returns
        -------
            None
        '''

        driver = ogr.GetDriverByName('ESRI Shapefile')
        if os.access(shpname, os.F_OK) :
            driver.DeleteDataSource(shpname)

        srs = osr.SpatialReference()
        srs.ImportFromEPSG(int(epsg))

        if layername is None :
            layername = os.path.basename(shpname).replace('.shp','')

        ds = driver.CreateDataSource(shpname)
        lyr = ds.CreateLayer(layername, srs, ogr.wkbPolygon)

        for key in dictfield :
            fieldName = ogr.FieldDefn(key, ogr.OFTString)
            lyr.CreateField(fieldName)

        if isinstance(coords, list) :
            # 逐个面对象创建
            for coord in coords :
                count = len(coord)
                wkt = 'POLYGON(('
                for i in range(count) :
                    if i == count-1:
                        wkt += '%f %f' %(coord[i][0], coord[i][1])
                    else:
                        wkt += '%f %f,' %(coord[i][0], coord[i][1])

                # 为了形成闭合圆环，最后一个点必须是第一个点位置
                if coord[count-1][0] != coord[0][0] and coord[count-1][1] != coord[0][1] :
                    wkt += ',%f %f' %(coord[0][0], coord[0][1])

                wkt = wkt + '))'

                geom = ogr.CreateGeometryFromWkt(wkt)
                feature = ogr.Feature(lyr.GetLayerDefn())
                feature.SetGeometry(geom)
                lyr.CreateFeature(feature)
        else:
            raise Exception('coords类型必须是list')

        ds = None
        driver =None

    def intersect(self, outname, srcfile, clipfile, layername=None):
        '''
        矢量求交，裁剪

        Parameters
        ----------
        outname : str
            输出裁剪结果文件
        srcfile ： str
            被裁剪对象
        clipfile ：str
            掩膜对象
        layername ： str, optional
            输出文件名图层名称

        Returns
        -------

        '''
        tempfiles = None
        outdir = os.path.dirname(outname)
        if not os.path.isdir(outdir) :
            os.makedirs(outdir)

        driver = ogr.GetDriverByName('ESRI Shapefile')
        srcds1 = driver.Open(srcfile, gdalconst.GA_ReadOnly)
        srcds2 = driver.Open(clipfile, gdalconst.GA_ReadOnly)
        src_layer1 = srcds1.GetLayer()
        src_layer2 = srcds2.GetLayer()
        srs1 = src_layer1.GetSpatialRef()
        srs2 = src_layer2.GetSpatialRef()
        if srs1.GetAttrValue('AUTHORITY',1) != srs2.GetAttrValue('AUTHORITY',1):
            print("空间参考不一致!将进行投影转换投影转换")

            # 对clip文件进行投影转换
            dstpatialRef = self.get_spatialref(srcfile)
            tempfile = os.path.join(outdir, os.path.basename(clipfile))
            tempfiles = glob.glob(tempfile.replace('.shp', '.*'))
            for item in tempfiles :
                try:
                    os.remove(item)
                except BaseException as e :
                    continue
            self.transform(tempfile, clipfile, dstpatialRef=dstpatialRef)

            srcds2.Destroy()
            # 获取转换后的结果
            srcds2 = driver.Open(tempfile, gdalconst.GA_ReadOnly)
            src_layer2 = srcds2.GetLayer()
            srs2 = src_layer2.GetSpatialRef()
            if srs1.GetAttrValue('AUTHORITY',1) != srs2.GetAttrValue('AUTHORITY',1):
                raise Exception("空间参考不一致!将进行投影转换投影转换")

            tempfiles = glob.glob(tempfile.replace('.shp', '.*'))

        # 创建输出文件
        target_ds = ogr.GetDriverByName('ESRI Shapefile').CreateDataSource(outname)
        target_layer = target_ds.CreateLayer(layername, srs1,
                                             geom_type=src_layer1.GetGeomType(),
                                             options=["ENCODING=UTF-8"]) # 设置编码为UTF-8，防止中文出现乱码

        # 定义输出属性表信息
        feature = src_layer1.GetFeature(0)
        field_count = feature.GetFieldCount()
        field_names = []
        for attr in range(field_count):
            field_defn = feature.GetFieldDefnRef(attr)
            field_names.append(field_defn.GetName())
            target_layer.CreateField(field_defn)

        for feat1 in src_layer1:
            geom1 = feat1.GetGeometryRef()
            for feat2 in src_layer2:
                geom2 = feat2.GetGeometryRef()
                # 判断两个feature是否相交
                if not geom1.Intersects(geom2):
                    continue
                # intersect = geom1.Intersection(geom1)
                feature = ogr.Feature(target_layer.GetLayerDefn())
                feature.SetGeometry(geom1)
                # 将源文件中的字段信息写入匹配feature中
                for field_name in field_names:
                    feature.SetField(field_name, feat1.GetField(field_name))
                target_layer.CreateFeature(feature)

                feat1.Destroy()
                feat2.Destroy()
                break

        # 清理引用
        target_ds.Destroy()
        srcds1.Destroy()
        srcds2.Destroy()
        if tempfiles is not None :
            for item in tempfiles :
                try:
                    os.remove(item)
                except BaseException as e :
                    continue

    def transform(self, outname, srcshp, dstpatialRef):
        # 当前地理参考
        srcpatialRef = self.get_spatialref(srcshp)
        # dstpatialRef = self.get_spatialref(dstshp)

        ds = ogr.Open(srcshp)
        srclayer = ds.GetLayer(0)

        basename = os.path.basename(outname)
        driver = ogr.GetDriverByName('ESRI Shapefile')
        out_ds = driver.CreateDataSource(outname)
        outlayer = out_ds.CreateLayer(basename[:-4], geom_type=srclayer.GetGeomType())

        # 投影转换
        coordinate_transfor = osr.CoordinateTransformation(srcpatialRef, dstpatialRef)

        # 定义输出属性表信息
        feature = srclayer.GetFeature(0)
        field_count = feature.GetFieldCount()
        field_names = []
        for attr in range(field_count):
            field_defn = feature.GetFieldDefnRef(attr)
            field_names.append(field_defn.GetName())
            outlayer.CreateField(field_defn)

        out_fielddefn = outlayer.GetLayerDefn()

        for feature in srclayer:
            geometry = feature.GetGeometryRef()
            geometry.Transform(coordinate_transfor)

            out_feature = ogr.Feature(out_fielddefn)
            out_feature.SetGeometry(geometry)
            for field_name in field_names:
                out_feature.SetField(field_name,feature.GetField(field_name))
            outlayer.CreateFeature(out_feature)

            feature.Destroy()
            out_feature.Destroy()

        # 清除缓存
        ds.Destroy()
        out_ds.Destroy()
        # 保存投影文件
        dstpatialRef.MorphFromESRI()
        prjname = outname.replace(".shp",".prj")
        fn = open(prjname,'w')
        fn.write(dstpatialRef.ExportToWkt())
        fn.close()

    def fishgrid(self, outname, extent, xRes, yRes):
        ''' https://blog.csdn.net/weixin_42924891/article/details/85865260
        https://zhuanlan.zhihu.com/p/403957133
        '''
        minX = extent[0]
        minY = extent[1]
        maxX = extent[2]
        maxY = extent[3]

        Height = int(np.ceil((maxY - minY) / yRes))
        Width = int(np.ceil((maxX - minX) / xRes))




    def get_spatialref(self, shpname):
        ds = ogr.Open(shpname)
        layer = ds.GetLayer(0)

        # 当前地理参考
        spatialRef = layer.GetFeature(0).GetGeometryRef().GetSpatialReference()
        # 清除缓存
        ds.Destroy()

        return spatialRef


# def contourGenerate(dstLayer, srcBand, contourInterval, contourBase,
#                     fixedLevelCount, useNoData, noDataValue,  idField, elevField):
#     gdal.ContourGenerate()

def contour(srcfile, dstfile, attrname, interval, offset=0, band=1,
            srcNoData=None, polygons=False, format='ESRI Shapefile'):
    ''' 创建等值线 '''

    #  The gdal_contour generates a vector contour file
    #      from the input raster elevation model (DEM).
    #     The contour line-strings are oriented consistently
    #     and the high side will be on the right,
    #     i.e. a line string goes clockwise around a top.
    #

    # gdal_contour [-b <band>] [-a <attribute_name>] [-amin <attribute_name>] [-amax <attribute_name>]
    # [-3d] [-inodata]
    # [-snodata n] [-i <interval>]
    # [-f <formatname>] [[-dsco NAME=VALUE] ...] [[-lco NAME=VALUE] ...]
    # [-off <offset>] [-fl <level> <level>...] [-e <exp_base>]
    # [-nln <outlayername>] [-q] [-p]
    # <src_filename> <dst_filename>

    cmd = 'gdal_contour -f "{format}" {srcfile} {dstfile} ' \
          '-b {band} -a {attrname} -i {interval} -off {offset}'.format(
        format=format,
        srcfile = srcfile,
        dstfile = dstfile,
        band=band,
        attrname=attrname,
        interval=interval,
        offset=offset
    )
    if srcNoData is not None :
        cmd += f' -snodata {srcNoData}'

    if polygons :
        cmd += ' -p'
    print('执行下载命令: 【%s】' %(cmd))
    status = os.system(cmd)
    print(status)

def getGDALType(datatype):
    '''
    根据numpy的数据类型，匹配GDAL中的数据类型

    Parameters
    ----------
    datatype

    Returns
    -------
        GDAL数据类型
    '''

    if datatype == np.byte or datatype == np.uint8:
        return gdal.GDT_Byte
    elif datatype == np.uint16 :
        return gdal.GDT_UInt16
    elif datatype == np.int16 :
        return gdal.GDT_Int16
    elif datatype == np.uint32 :
        return gdal.GDT_UInt32
    elif datatype == np.int32 :
        return gdal.GDT_Int32
    elif datatype == np.float32 :
        return gdal.GDT_Float32
    elif datatype == np.float64 :
        return gdal.GDT_Float64
    else:
        return gdal.GDT_Unknown


def getOGRType(dtype) :
    '''
    根据numpy的数据类型，匹配OGR中的数据类型

    Parameters
    ----------
    dtype

    Returns
    -------
        OGR数据类型
    '''

    if dtype == np.byte or dtype == np.uint8:
        return ogr.OFTString
    elif dtype == np.uint16 or dtype == np.int16 :
        return ogr.OFSTInt16
    elif dtype == np.uint32 or dtype == np.int32  :
        return ogr.OFTInteger
    elif dtype == np.int64 :
        return ogr.OFTInteger64
    elif dtype == np.float32 :
        return ogr.OFSTFloat32
    elif dtype == np.float64 :
        return ogr.OFTReal
    else:
        return ogr.OJUndefined

def getNPDType(datatype) :
    '''将numpy.dtype转换成 gdal Type'''
    if 'int' in datatype:
        return gdal.GDT_Int32
    elif 'float' in datatype:
        return gdal.GDT_Float32
    else:
        return gdal.GDT_Unknown