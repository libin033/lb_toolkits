#coding:utf-8
import sys
import os
import numpy as np
import json



def readjson(jsonname, **kwargs):
    '''
    读取JSON文件
    :param jsonname: JSON文件名
    :return: dict
    '''
    fp = open(jsonname, 'r', **kwargs)
    dict_info_in = json.load(fp, **kwargs)

    fp.close()

    return dict_info_in

def writejson(jsonname, dict_info, indent=4, chinese=False):

    if chinese :
        ensure_ascii = False
    else:
        ensure_ascii = True


    fp = open(jsonname, 'w')
    json.dump(dict_info, fp, indent=indent, ensure_ascii=ensure_ascii)
    fp.close()


def readbinary(filename, shape, dtype=np.float32, offset=0, encodine='utf-8'):
    '''
    读取二进制文件
    :param filename: 输入文件名
    :param shape: 获取的维度大小
    :param dtype: 数据类型
    :param offset: 偏移量
    :param encodine: 编码类型
    :return: numpy.array
    '''
    count = 1
    if os.path.isfile(filename) :
        for i in shape :
            count *= i
        data = np.fromfile(filename, dtype=dtype, count= count,offset=offset)

    return data.reshape(shape)


def writebinary(filename, data, overwrite=1, offset=0, encodine='utf-8'):
    '''
    二进制数据写入文件
    :param filename: 输出文件名
    :param data: numpy.array
    :param overwrite: 是否覆盖、新建文件
    :param offset: 偏移量
    :param encodine: 编码
    :return: None
    '''
    data = np.array(data)

    if overwrite:
        fp = open(filename, 'wb')
    else:
        fp = open(filename, 'ab')

    data.tofile(fp)

    fp.close()

def readascii(filename, dtype=float, comments='#', delimiter=None,
                     converters=None, skiprows=0, usecols=None, unpack=False,
                     ndmin=0, encoding='bytes', max_rows=None):
    '''
    读取ASCII文件
    :param filename:
    :param dtype:
    :param comments:
    :param delimiter:
    :param converters:
    :param skiprows:
    :param usecols:
    :param unpack:
    :param ndmin:
    :param encoding:
    :param max_rows:
    :return:
    '''
    return  np.loadtxt(filename, dtype=dtype, comments=comments, delimiter=delimiter,
                       converters=converters, skiprows=skiprows, usecols=usecols, unpack=unpack,
                       ndmin=ndmin, encoding=encoding, max_rows=max_rows)

def writeascii(filename, data,  fmt='%.18e', delimiter=' ', newline='\n', header='',
               footer='', comments='# ', encoding=None):
    '''
    写ASCII文件
    :param filename:
    :param data:
    :param fmt:
    :param delimiter:
    :param newline:
    :param header:
    :param footer:
    :param comments:
    :param encoding:
    :return:
    '''
    data = np.array(data)

    np.savetxt(filename, data, fmt, delimiter, newline, header,
               footer, comments, encoding)

def loadarray(file, mmap_mode=None, allow_pickle=False, fix_imports=True,
              encoding='ASCII'):
    '''
    读取numpy保存输出的.npy文件
    :param file:
    :param mmap_mode:
    :param allow_pickle:
    :param fix_imports:
    :param encoding:
    :return:
    '''
    return np.load(file, mmap_mode, allow_pickle, fix_imports, encoding)


def savearray(filename, data, allow_pickle=True, fix_imports=True):
    '''
    输出.npy文件
    :param filename:
    :param data: numpy.array
    :param allow_pickle:
    :param fix_imports:
    :return:
    '''
    return  np.save(filename, data, allow_pickle, fix_imports)


