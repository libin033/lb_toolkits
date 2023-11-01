# coding:utf-8
'''
@Project  : code
@File     : ncpro.py
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/3/22 10:20   Lee        1.0

'''
import os
import netCDF4
import numpy as np
from netCDF4 import num2date, date2num

def readnc(filename, sdsname, dictsdsinfo=None):

    if not os.path.isfile(filename) :
        print('%s is not exist, please check it...' %(filename))
        if dictsdsinfo is None :
            return None
        else:
            return None, None
    else:
        try:
            with netCDF4.Dataset(filename, 'r') as fp :
                if not sdsname in fp.variables:
                    print('%s is not a dataset in %s' % (sdsname, filename))

                    return None
                else:
                    dsetid = fp.variables[sdsname]
                    data = fp.variables[sdsname][:]

                    if not dictsdsinfo is None :
                        for key in dsetid.ncattrs() :
                            dictsdsinfo.update({key: dsetid.getncattr(key)})


                        return data, dictsdsinfo

        except BaseException as e :
            print(e)
            if dictsdsinfo is None :
                return None
            else:
                return None, None

        return data

def readnc_fileinfo(filename) :

    dictfileinfo = {}
    if not os.path.isfile(filename) :
        print('%s is not exist, please check it...' %(filename))
        return dictfileinfo
    else:
        try:
            with netCDF4.Dataset(filename, 'r') as fp :

                for key in fp.ncattrs():
                    dictfileinfo.update({key: fp.getncattr(key)})

                return  dictfileinfo
        except BaseException as e :
            print(e)
            return dictfileinfo

def readnc_sdsinfo(filename, sdsname) :

    dictsdsinfo = {}
    if not os.path.isfile(filename) :
        print('%s is not exist, please check it...' %(filename))
        return dictsdsinfo
    else:
        try:
            with netCDF4.Dataset(filename, 'r') as fp :

                if not sdsname in fp.variables:
                    print('%s is not a dataset in %s' %(sdsname, filename))
                    return dictsdsinfo
                else:
                    dsetid = fp.variables[sdsname]
                    for key in dsetid.ncattrs():
                        dictsdsinfo.update({key: dsetid.getncattr(key)})

                    return dictsdsinfo
        except BaseException as e :
            print(e)
            return dictsdsinfo

def writenc(filename, sdsname, srcdata, dimension=None, overwrite=1,
            complevel=9, dictsdsinfo=None, fill_value=None):
    '''
    写NC文件
    :param filename: 输出文件名
    :param sdsname: 数据集名
    :param srcdata: 数据
    :param dimension: tuple, 关联维度名，
    :param overwrite:
    :param complevel:
    :param dictfileinfo:
    :param dictsdsinfo:
    :return:
    '''
    data = np.array(srcdata)

    if overwrite :
        fp = netCDF4.Dataset(filename, 'w')
    else:
        fp = netCDF4.Dataset(filename, 'r+')

    dsetid = None
    # 如果没有对应的关联维度，则创建该维度
    if dimension is None :
        fp.createDimension(sdsname, data.shape[0])
        dsetid = fp.createVariable(sdsname, data.dtype, dimensions=sdsname,
                                  zlib=True, complevel=9)
        fp.variables[sdsname][:] = data
    else:
        # 判断数据集维度是否存在，如果不存在，则创建该维度，并赋值为0
        k = 0
        for item in dimension :
            if not item in fp.dimensions :
                fp.createDimension(item, data.shape[k])
                dsetid = fp.createVariable(item, np.int32, dimensions=item, zlib=True, complevel=9)
                fp.variables[item][:] = range(data.shape[k])
            k = k + 1
        dsetid = fp.createVariable(sdsname, data.dtype, dimensions=dimension, zlib=True,
                                   complevel=complevel, fill_value=fill_value)
        fp.variables[sdsname][:] = data

    if (not dictsdsinfo is None) and (not dsetid is None) :
        for key in dictsdsinfo :
            dsetid.setncattr(key, dictsdsinfo[key])

    fp.close()
    print('成功创建【%s】【%s】' %(filename, sdsname))


def writenc_fileinfo(filename, dictfileinfo, overwrite=1):

    try:
        if overwrite :
            fp = netCDF4.Dataset(filename, 'w')
        else:
            if os.path.isfile(filename) :
                fp = netCDF4.Dataset(filename, 'r+')
            else:
                print('文件不存在，将新建文件【%s】' %(filename))
                fp = netCDF4.Dataset(filename, 'w')

        if not dictfileinfo is None :
            for key in dictfileinfo:
                fp.setncattr(key, dictfileinfo[key])
        fp.close()
        return True

    except BaseException as e :
        print('write %s file information error!!!' %(filename))
        return False


def writenc_sdsinfo(filename, sdsname, dictsdsinfo, overwrite=1):
    try:
        if overwrite:
            fp = netCDF4.Dataset(filename, 'w')
        else:
            if os.path.isfile(filename):
                fp = netCDF4.Dataset(filename, 'r+')
            else:
                print('%s is not exist, will create it...' % (filename))
                fp = netCDF4.Dataset(filename, 'w')
        if not sdsname in fp.variables:
            print('%s is not a dataset in %s' %(sdsname, filename))
            fp.close()
            return False
        else:
            dsetid = fp.variables[sdsname]
            for key in dictsdsinfo:
                dsetid.setncattr(key, dictsdsinfo[key])
        fp.close()
        return True
    except BaseException as e:
        print('write %s dataset %s information error!!!' % (filename, sdsname))
        return False

def writencfortimes(filename, sdsname, srcdata, overwrite=1,
            complevel=9, dictsdsinfo=None):
    '''
    写NC文件
    :param filename: 输出文件名
    :param sdsname: 数据集名
    :param srcdata: 数据
    :param dimension: tuple, 关联维度名，
    :param overwrite:
    :param complevel:
    :param dictsdsinfo:
    :return:
    '''
    data = np.array(srcdata)

    if overwrite :
        fp = netCDF4.Dataset(filename, 'w')
    else:
        fp = netCDF4.Dataset(filename, 'r+')

    # 如果没有对应的关联维度，则创建该维度

    fp.createDimension(sdsname, data.shape[0])
    times = fp.createVariable(sdsname, 'f8', dimensions=sdsname,
                              zlib=True, complevel=complevel)
    times.units = 'hours since 1900-01-01 00:00:00.0'
    times.calendar = "gregorian"

    fp.variables[sdsname][:] = date2num(data,units=times.units,calendar=times.calendar)


    if (not dictsdsinfo is None) and (not times is None) :
        for key in dictsdsinfo :
            times.setncattr(key, dictsdsinfo[key])

    fp.close()
    print('成功创建【%s】【%s】' %(filename, sdsname))




