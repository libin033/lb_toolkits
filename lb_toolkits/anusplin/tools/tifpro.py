# -*- coding:utf-8 -*-
'''
@Project  : lb_toolkits
@File     : tifpro.py
------------------------------------
@Modify Time      @Author    @Version
--------------    -------    --------
2022/7/12 17:43      Lee       1.0
@Description
------------------------------------
对geotiff文件读、写操作
'''



import numpy as np
try:
    from osgeo import gdal, gdalconst, osr, ogr
except ImportError:
    try:
        import gdal, gdalconst, osr, ogr
    except ImportError:
        raise ImportError('Python GDAL library not found, please install python-gdal')


def readtiff(filename):
    '''
    读取TIFF文件
    :param filename: 输入TIFF文件名
    :return: 数据、仿射函数、投影参数
    '''

    dataset = gdal.Open(filename, gdal.GA_ReadOnly)
    if dataset == None:
        print(filename+"文件无法打开")
        return None, None, None
    width = dataset.RasterXSize #栅格矩阵的列数
    height = dataset.RasterYSize #栅格矩阵的行数
    im_bands = dataset.RasterCount #波段数

    im_data = dataset.ReadAsArray(0, 0, width, height)#获取数据
    im_geotrans = dataset.GetGeoTransform()#获取仿射矩阵信息
    im_proj = dataset.GetProjection()#获取投影信息

    del dataset

    return im_data, im_geotrans, im_proj




def writetiff(outname, data, im_geotrans=None, im_proj=None, fillvalue=None):
    '''
    输出geotiff文件
    :param outname: 输出文件名
    :param data: 输出数据
    :param im_geotrans: 仿射函数
    :param im_proj: 投影信息
    :param fillvalue: 填充值，作为Nodata
    :return: None
    '''
    im_data = data.copy()
    im_data = np.array(im_data)
    if fillvalue :
        im_data[np.isnan(im_data)] = fillvalue

    datatype = gettype(im_data.dtype)

    if len(im_data.shape) == 3:
        im_bands, im_height, im_width = im_data.shape
    elif len(im_data.shape) == 2:
        im_bands, (im_height, im_width) = 1,im_data.shape
    else:
        im_bands, (im_height, im_width) = 1,im_data.shape
        #创建文件
    driver = gdal.GetDriverByName("GTiff")
    dataset = driver.Create(outname, im_width, im_height, im_bands, datatype,  options=["COMPRESS=LZW"])
    if(dataset!= None):

        if not im_geotrans is None :
            dataset.SetGeoTransform(im_geotrans) #写入仿射变换参数

        if im_proj is None :
            # 获取地理坐标系统信息，用于选取需要的地理坐标系统
            sr = osr.SpatialReference()
            sr.SetWellKnownGeogCS("EPSG:4326")
            # 给新建图层赋予投影信息
            dataset.SetProjection(sr.ExportToWkt())
        else:
            dataset.SetProjection(im_proj) #写入投影

    if im_bands == 1:
        dataset.GetRasterBand(1).WriteArray(im_data)
    else:
        for i in range(im_bands):
            dataset.GetRasterBand(i+1).WriteArray(im_data[i])

    if fillvalue is not None:
        dataset.GetRasterBand(1).SetNoDataValue(float(fillvalue))
        # dataset.GetRasterBand(1).Fill(float(fillvalue))

    del dataset

def gettype(datatype):
    '''
    根据numpy的数据类型，匹配GDAL中的数据类型
    :param datatype:
    :return: GDAL数据类型
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
