# -*- coding:utf-8 -*-
'''
@Project     : ANUSPLIN

@File        : StationsInterp.py

@Modify Time :  2022/9/27 13:37   

@Author      : Lee    

@Version     : 1.0   

@Description :

'''
import os
import sys
import numpy as np
import datetime
import time
import matplotlib.pyplot as plt
from lb_toolkits.tools.ncpro import readnc
from lb_toolkits.tools.tifpro import readtiff, gettype
from lb_toolkits.tools.jsonpro import readjson

from osgeo import gdal, osr, ogr

exepath = os.path.dirname(os.path.abspath(__file__))
# print('exepath:[%s]' %(exepath))
# os.chdir(exepath)

class StationsInterp(object) :

    def interp(self, lat, lon, data,
               minX, maxX, minY, maxY, resolution=0.01,
               vmax=None, vmin=None,  outname=None,
               prodname ='temp', shpname=None):

        srclat = np.array(lat)
        srclon = np.array(lon)
        srcdata = np.array(data)

        flag = np.isnan(srcdata) | np.isnan(srclat) | np.isnan(srclon)
        srclat  = srclat[~flag]
        srclon  = srclon[~flag]
        srcdata = srcdata[~flag]

        self.tempfile = []
        self.vmax = vmax
        self.vmin = vmin

        self.minX = minX
        self.maxX = maxX
        self.minY = minY
        self.maxY = maxY
        self.resolution = resolution
        self.rows = int(np.ceil((self.maxY - self.minY) / self.resolution))
        self.cols = int(np.ceil((self.maxX - self.minX) / self.resolution))

        print('输出网格  行数:【%d】 , 列数:【%d】' %(self.rows, self.cols))

        stime = time.time()
        outdir = os.path.dirname(outname)
        if len(outdir) != 0 :
            if not os.path.isdir(outdir) :
                os.makedirs(outdir)

        self.setoptions(outdir, prodname, os.path.basename(outname))

        covvar = self.demformat(self.covariatename, os.path.join(exepath, r'conf/global_dem.nc'),
        # covvar = self.demformat(self.covariatename, os.path.join(exepath, r'conf/DEM_A2022_1000M.tif'),
                             srclat, srclon)

        self.initdata(srclat, srclon, srcdata, covvar)

        self.selnot(outname, os.path.join(exepath,'bin'))
        self.splinb(outname, os.path.join(exepath,'bin'))
        self.lapgrd(outname, os.path.join(exepath,'bin'))

        self.grid2tiff(outname, self.gridname,
                       shpname=shpname)
        etime = time.time()
        print('成功输出【%s】' %(outname))
        print('运行耗时【%.2f秒】' %(etime - stime))

    def setoptions(self, outdir, prodname, name):

        self.prodname = prodname
        self.units = 5           # units code for surface value and fillvalue
        # 0:undefined    1:meters  2:feet
        # 3:kilometers   4:miles   5:degrees
        # 6:radians      7:millimetres   8:megajoules
        self.independentvar = 2  # 自变量（x, y ）, 最多10个
        self.covariatevar   = 1  # 协变量 dem
        self.sfc = 0             # 表面样条变量个数， 每个表面采用不同的样条变量
        self.sfcc = 0            # 表面协变量个数， 每个表面采用不同的样条变量
        # 对自变量范围设置
        # 每一个自变量的上下限、有无转换、单位，该项为拟合区域的X的最大值最小值坐标，即最左、最右边界的X值；
        # 0：不转换，1：转换；
        self.exchange = 0

        # units--> 1：m, 5:degree
        self.posunits = 5

        # 对协变量范围设置
        # 高程的上下限，
        self.covvar1_min = -500
        self.covvar1_max = 9000
        self.covvar1_units = 1

        # 自变量转换参数，0代表不转换
        self.independent_var_exchange = 1
        self.covariate_var_exchange = 0

        # 样条次数
        self.splinenum = 3

        # 输出表面个数
        self.sfcnum = 1

        # 所有的表面用相同的权重
        # 0：不需要
        # 1：采用不同权重，需要对各个表面所用权重进行设置
        self.weightforsfc = 0

        # 优化参数指标
        self.optimalparm = 1

        # 平滑参数选择方法
        # 1 ：GCV，2：MSE，3：固定值，4：GML
        self.smoothparm = 1

        # 输入数据
        self.datadir = os.path.join(outdir, '%s.in' %(name))
        self.tempfile.append(self.datadir)

        # 样本总数
        self.samplenum = 2420
        self.knotsnum = int(self.samplenum * 0.5)
        # 站点的label
        self.stationlabel = 0

        # 输入数据的变量存储格式
        self.format = '(4f10.3)'

        # 写变量文件
        self.covariatename = os.path.join(outdir, r'covfile')
        self.tempfile.append(self.covariatename)

        # 输出文件
        # 残差文件
        self.resname = os.path.join(outdir, '%s.res' %(name))

        # 表面文件，用于下一步LAPGRD的输入数据
        self.surname = os.path.join(outdir, '%s.sur' %(name))
        self.notname = os.path.join(outdir, '%s.not' %(name))

        self.ourdir = os.path.join(outdir, '%s.out' %(name))
        self.rejname = os.path.join(outdir, '%s.rej' %(name))

        ############################################################
        ############################################################

        # 表面个数
        self.sfcnum = 1

        # 1：转换恢复
        self.re_exchange = 1

        # 误差类型
        # 1：模型标准误差，2：预测标准误差
        self.biastype = 1

        # 掩摸方式
        # 0：不提供掩摸文件
        self.masktype = 0

        # 独立的协变量数据格式，2代表输入输出格式大小一致
        self.covformat = 2

        # 空值数据
        self.fillvalue = -9999.0

        # 输出文件名
        self.gridname = os.path.join(outdir, '%s.grd' %(name))

        # 输出数据格式
        self.gridformat = '(%df15.2)' %(self.cols)

        self.tempfile.append(self.resname)
        self.tempfile.append(self.surname)
        self.tempfile.append(self.notname)
        self.tempfile.append(self.ourdir)
        self.tempfile.append(self.rejname)
        self.tempfile.append(self.gridname)

    def selnot(self, outname, exedir):

        basename = os.path.basename(outname)
        outdir = os.path.dirname(outname)
        # step1
        selnot = os.path.join(exedir, 'selnot.exe')
        confname = os.path.join(outdir, '%s_selnot.conf' %(basename))
        logname = os.path.join(outdir, '%s_selnot.log' %(basename))

        self.tempfile.append(confname)
        self.tempfile.append(logname)

        self.createConfForSelnot(confname)


        cmd1 = '{exename} <{confname}> {logname}'.format(
            exename=selnot, confname=confname, logname=logname)

        print(cmd1)
        os.system(cmd1)

    def splinb(self, outname, exedir):
        basename = os.path.basename(outname)
        outdir = os.path.dirname(outname)
        # step2
        splinb = os.path.join(exedir, 'splinb.exe')
        confname = os.path.join(outdir, '%s_splinb.conf' %(basename))
        logname = os.path.join(outdir, '%s_splinb.log' %(basename))
        self.tempfile.append(confname)
        self.tempfile.append(logname)
        self.createConfForSpline(confname)


        cmd2 = '{exename} <{confname}> {logname}'.format(
            exename=splinb, confname=confname, logname=logname)

        print(cmd2)
        os.system(cmd2)

    def lapgrd(self, outname, exedir):

        basename = os.path.basename(outname)
        outdir = os.path.dirname(outname)

        # step3
        lapgrd = os.path.join(exedir, 'lapgrd.exe')
        confname = os.path.join(outdir, '%s_lapgrd.conf' %(basename))
        logname = os.path.join(outdir, '%s_lapgrd.log' %(basename))
        self.tempfile.append(confname)
        self.tempfile.append(logname)

        self.createConfForLapgrd(confname)
        cmd3 = '{exename} <{confname}> {logname}'.format(
            exename=lapgrd, confname=confname, logname=logname)

        print(cmd3)
        os.system(cmd3)

    def createConfForSelnot(self, confname):
        with open(confname, 'w') as fp :
            fp.write('%d\n' %(self.independentvar))                                                         # 1
            fp.write('%d\n' %(self.covariatevar))                                                           # 2
            fp.write('%d\n' %(self.sfc))                                                                    # 3
            fp.write('%d\n' %(self.sfcc))                                                                   # 4
            fp.write('%.3f %.3f %d %d\n' % (self.minX, self.maxX, self.exchange, self.posunits))      # 5
            fp.write('%.3f %.3f %d %d\n' % (self.minY, self.maxY, self.exchange, self.posunits))      # 6
            fp.write('%.3f %.3f %d %d\n' %(self.covvar1_min, self.covvar1_max, 1, self.posunits))           # 7
            fp.write('%d\n' %(self.independent_var_exchange))                                               # 8
            fp.write('%d\n' %(self.covariate_var_exchange))                                                 # 9
            fp.write('%d\n' %(self.sfcnum))                                                                 # 10
            fp.write('%d\n' %(self.weightforsfc))                                                           # 11
            fp.write('%s\n' %(self.datadir))                                                                # 12
            fp.write('%d\n' %(self.samplenum))                                                              # 13
            fp.write('%d\n' %(self.stationlabel))                                                           # 14
            fp.write('%s\n' %(self.format))                                                                 # 15
            fp.write('%s\n' %(self.notname))                                                                # 16
            fp.write('%s\n' %(self.rejname))                                                                # 17
            fp.write('%d\n' %(self.knotsnum))                                                      # 18

    def createConfForSpline(self, confname):
        with open(confname, 'w') as fp :
            # TITLE OF FITTED SURFACES (60 CHARS)
            fp.write('%s\n' %(self.prodname))                                                        # 1
            # SURFACE VALUE UNITS CODE AND MISSING DATA VALUE:
            # -----------------------------------------------
            # 0 - UNDEFINED        5 - DEGREES
            # 1 - METRES           6 - RADIANS
            # 2 - FEET             7 - MILLIMETRES
            # 3 - KILOMETRES       8 - MEGAJOULES5
            # 4 - MILES
            fp.write('%d\n' %(self.units))                                                           # 2
            # INDEPENDENT VARIABLES
            # ---------------------
            # NUMBER OF INDEPENDENT SPLINE VARIABLES (0 TO 10)
            fp.write('%d\n' %(self.independentvar))                                                  # 3
            # NUMBER OF INDEPENDENT COVARIATES (0 TO  8)
            fp.write('%d\n' %(self.covariatevar))                                                    # 4
            # NUMBER OF SURFACE SPLINE VARIABLES (0 TO  7)
            fp.write('%d\n' %(self.sfc))                                                             # 5
            # NUMBER OF SURFACE COVARIATES (0 TO  7)
            fp.write('%d\n' %(self.sfcc))                                                            # 6

            # TRANSFORMATION CODES            REFERENCE UNIT CODES
            # --------------------            --------------------
            # 0 - NO TRANSFORMATION           0 - UNDEFINED
            # 1 - X/A                         1 - METRES
            # 2 - X*A                         2 - FEET
            # 3 - A*LOG(X + B)                3 - KILOMETRES
            # 4 - (X/B)**A                    4 - MILES
            # 5 - A*EXP(X/B)                  5 - DEGREES
            # 6 - A*TANH(X/B)                 6 - RADIANS
            # 7 - ANISOTROPY ANGLE            7 - MILLIMETRES
            # 8 - ANISOTROPY FACTOR           8 - MEGAJOULES

            # LOWER & UPPER LIMITS, TRANSF CODE, REF UNIT, MARGIN(S) FOR VARIABLE
            fp.write('%.3f %.3f %d %d\n' % (self.minX, self.maxX, self.exchange, self.posunits))         # 7
            fp.write('%.3f %.3f %d %d\n' % (self.minY, self.maxY, self.exchange, self.posunits))         # 8
            fp.write('%.3f %.3f %d %d\n' %(self.covvar1_min, self.covvar1_max, 1, self.covvar1_units))         # 9
            # ENTER  1 TRANSFORMATION COEFFICIENT(S)
            # SURFACE DIRECTIVES
            # ------------------
            # DEPENDENT VARIABLE TRANSFORMATION:
            # 0 - NO TRANSFORMATION
            # 1 - NATURAL LOGARITHM
            # 2 - SQUARE ROOT
            # 5 - OCCURRENCE0
            fp.write('%d\n' %(self.independent_var_exchange))                                        # 10
            fp.write('%d\n' %(self.covariate_var_exchange))                                          # 11
            # ORDER OF SPLINE (AT LEAST 2)
            fp.write('%d\n' %(self.splinenum))                                                       # 12
            # NUMBER OF SURFACES (AT LEAST 1)
            fp.write('%d\n' %(self.sfcnum))                                                          # 13
            # NUMBER OF RELATIVE VARIANCES (0 OR 1)
            fp.write('%d\n' %(self.weightforsfc))                                                    # 14
            # OPTIMIZATION DIRECTIVE (NORMALLY 1):
            #   0 - COMMON SMOOTHING PARAMETER FOR ALL SURFACES
            #   1 - COMMON SMOOTHING DIRECTIVE FOR ALL SURFACES
            #   2 - DIFFERENT SMOOTHING DIRECTIVE FOR EACH SURFACE1
            fp.write('%d\n' %(self.optimalparm))                                                     # 15
            # SMOOTHING DIRECTIVE (NORMALLY 1):
            #   0 - FIXED SMOOTHING PARAMETER FOR EACH SURFACE
            #   1 - MINIMIZE GCV FOR EACH SURFACE
            #   2 - MINIMIZE TRUE MEAN SQUARE ERROR FOR EACH SURFACE
            #   3 - FIXED SIGNAL FOR EACH SURFACE
            #   4 - MINIMIZE GML FOR EACH SURFACE1
            fp.write('%d\n' %(self.smoothparm))                                                      # 16
            # DATA FILE NAME
            fp.write('%s\n' %(self.datadir))                                                         # 17
            # MAXIMUM NUMBER OF DATA POINTS (AT LEAST  7)
            fp.write('%d\n' %(self.samplenum))                                                       # 18
            # NO. OF CHARACTERS IN SITE LABEL (0 TO 20)
            fp.write('%d\n' %(self.stationlabel))                                                    # 19
            # DATA FORMAT (SITE LABEL,  3 INDEP VARS,  1 SURFACES,  0 REL VARIANCES)
            fp.write('%s\n' %(self.format))                                                          # 20
            # KNOT INDEX FILE NAME
            fp.write('%s\n' %(self.notname))                                                         # 21
            # MAXIMUM NUMBER OF DATA KNOTS (AT LEAST  1)
            fp.write('%d\n' %(self.knotsnum))                                                            # 22
            # INPUT BAD DATA FLAG FILE NAME (BLANK IF NOT REQUIRED)
            fp.write('\n')                                                                      # 23
            # OUTPUT BAD DATA FLAG FILE NAME (BLANK IF NOT REQUIRED)
            fp.write('\n')                                                                      # 24
            # OUTPUT LARGE RESIDUAL FILE NAME (BLANK IF NOT REQUIRED)
            fp.write('\n')                                                                      # 25
            # OUTPUT OPTIMIZATION PARAMETERS FILE NAME (BLANK IF NOT REQUIRED):
            fp.write('\n')                                                                      # 26
            # OUTPUT SURFACE COEFFICIENTS FILE NAME (BLANK IF NOT REQUIRED):
            fp.write('%s\n' %(self.surname))                                                         # 27
            # OUTPUT DATA LIST FILE NAME (BLANK IF NOT REQUIRED):
            fp.write('\n')                                                                      # 28
            # OUTPUT ERROR COVARIANCE FILE NAME (BLANK IF NOT REQUIRED):
            fp.write('\n')                                                                      # 29
            # OUTPUT ERROR COVARIANCE FILE NAME (BLANK IF NOT REQUIRED):
            fp.write('\n')                                                                      # 30
            # fp.write('%d\n' %(self.samplenum))                                                       # 31
            # fp.write('%d\n' %(self.stationlabel))                                                    # 32
            # fp.write('%s\n' %(self.format))                                                       # 33
            # fp.write('%s\n' %(self.ourdir))                                                          # 34

    def createConfForLapgrd(self, confname):
        with open(confname, 'w') as fp :
            fp.write('%s\n' %(self.surname))
            fp.write('%d\n' %(self.sfcnum))
            fp.write('%d\n' %(self.re_exchange))
            fp.write('\n')
            fp.write('%d\n' %(self.biastype))
            fp.write('%d\n' %(1))
            fp.write('%.3f %.3f %.4f\n' % (self.minX, self.maxX, self.resolution))
            fp.write('%d\n' %(2))
            fp.write('%.3f %.3f %.4f\n' % (self.minY, self.maxY, self.resolution))
            fp.write('%d\n' %(self.masktype))
            fp.write('%d\n' %(self.covformat))
            fp.write('%s\n' %(self.covariatename))
            fp.write('%d\n' %(2))                   # arcgis grid
            fp.write('%f\n' %(self.fillvalue))
            fp.write('%s\n' %(self.gridname))
            fp.write('%s\n' %(self.gridformat))

    def initdata(self, srclat, srclon, srcdata, srccovvar):
        '''
        按格式生成输入数据ASCII文件

        Args:
            srclat: array, 纬度
            srclon: array, 经度
            srcdata: array, 自变量

        Returns:

        '''

        # data, mtrans, mproj = readtiff(tiffname)

        # line, pixel = data.shape

        # x, y = np.meshgrid(np.arange(0, pixel), np.arange(0, line))
        #
        # lon = mtrans[0] + x * mtrans[1] + y * mtrans[2]
        # lat = mtrans[3] + x * mtrans[4] + y * mtrans[5]
        #
        flag = (srclon <= 180.0) & (srclon >= -180.0) \
               & (srclat <= 90.0) & (srclat >= -90.0)
        if self.vmax is not None and self.vmin is not None :
            flag = (srcdata >= self.vmin) & (srcdata <= self.vmax) \
                 & flag


        mdata = srcdata[flag]
        mlon = srclon[flag]
        mlat = srclat[flag]
        covvar = srccovvar[flag]

        if self.vmax is  None or self.vmin is None :
            self.vmax = np.nanmax(mdata)
            self.vmin = np.nanmin(mdata)

        self.samplenum = len(mdata)
        print('samplenum:', self.samplenum)

        self.knotsnum = int(self.samplenum * 0.5)
        if self.knotsnum > 3000:
            self.knotsnum = 3000

        result = np.array( [mlon, mlat, covvar, mdata], dtype=np.float64).T

        header = '%10s %10s %10s %10s' %('lon', 'lat', 'dem', 'data')
        np.savetxt(self.datadir, result, fmt='%10.3f',  comments='')

        print('成功格式化输入数据')

    def demformat(self, covariatename, demfile=None, srclat=None, srclon=None):
        '''
        对高程数据进行格式化处理

        Args:
            covariatename: 协变量文件名
            demfile: 高程静态数据

        Returns:

        '''
        srcdem = readnc(demfile, 'dem')
        # srcdem,_,_ = readtiff(demfile)

        res = 180.0 / srcdem.shape[0]
        lon, lat = np.meshgrid(np.arange(self.minX, self.maxX, self.resolution),
                               np.arange(self.maxY, self.minY, -self.resolution))

        row = np.array((90.0 - lat) / res, dtype=np.int32)
        col = np.array((lon + 180.0) / res, dtype=np.int32)

        dem = srcdem[row, col]
        if dem is not None :
            rows, cols = dem.shape

            header = 'ncols         %d\n' \
                     'nrows         %d\n' \
                     'xllcorner     %f\n' \
                     'yllcorner     %f\n' \
                     'cellsize      %f\n' \
                     'NODATA_value  %f' %(cols, rows, self.minX, self.minY,
                                          self.resolution, self.fillvalue)

            np.savetxt(covariatename, dem, fmt='%4d', header=header, comments='')

        row = np.array((90.0 - srclat) / res, dtype=np.int32)
        col = np.array((srclon + 180.0) / res, dtype=np.int32)
        covvar = srcdem[row, col]

        del srcdem

        return covvar

    def grid2tiff(self, outname, gridname, shpname):
        '''
        将模型输出的grid文件转换成tif文件

        Args:
            outname: 输出的TIFF文件名
            gridname: 输入的grid文件名

        Returns:

        '''
        if os.path.isfile(gridname) :
            try:
                dict_data = self.readgrid(gridname)
                toplat = dict_data['bottomlat'] + dict_data['rows'] * dict_data['resolution']
                trans = [dict_data['leftlon'], dict_data['resolution'], 0,
                         toplat, 0, -dict_data['resolution']]
                data = dict_data['data']
                flag = (data < self.vmin) | (data > self.vmax)
                data[flag] = dict_data['fillvalue']
                fillvalue = dict_data['fillvalue']
                # writetiff(outname, data, trans, fillvalue=dict_data['fillvalue'])

            except BaseException as e :
                print(e)
                return None

            data = np.array(data)
            if outname is not None :
                datatype = gettype(data.dtype)

                if len(data.shape) == 3:
                    im_bands, im_height, im_width = data.shape
                elif len(data.shape) == 2:
                    im_bands, (im_height, im_width) = 1,data.shape
                else:
                    im_bands, (im_height, im_width) = 1,data.shape
                    #创建文件
                driver = gdal.GetDriverByName("MEM")
                dataset = driver.Create('', im_width, im_height, im_bands, datatype)

                dataset.SetGeoTransform(trans) #写入仿射变换参数
                # 获取地理坐标系统信息，用于选取需要的地理坐标系统
                sr = osr.SpatialReference()
                sr.SetWellKnownGeogCS("EPSG:4326")
                # 给新建图层赋予投影信息
                dataset.SetProjection(sr.ExportToWkt())

                if im_bands == 1:
                    dataset.GetRasterBand(1).WriteArray(data)
                else:
                    for i in range(im_bands):
                        dataset.GetRasterBand(i+1).WriteArray(data[i])

                if fillvalue is not None :
                    dataset.GetRasterBand(1).SetNoDataValue(float(fillvalue))
                    # dataset.GetRasterBand(1).Fill(float(fillvalue))
                if shpname is not None and os.path.isfile(shpname) :
                    vec = ogr.Open(shpname)
                    layer = vec.GetLayer()

                    extent = layer.GetExtent()
                    minX, maxX, minY, maxY = extent
                    ds = gdal.Warp(
                        outname, dataset,
                        format = 'GTiff',
                        outputBounds=(minX, minY, maxX, maxY) ,  # (minX, minY, maxX, maxY)
                        cutlineDSName=shpname, cropToCutline=True,
                        xRes=self.resolution, yRes=self.resolution,
                        dstNodata=fillvalue, creationOptions=["COMPRESS=LZW"])
                    if ds is not None :
                        data = ds.ReadAsArray()
                    else:
                        return None
                else:
                    gdal.Warp(outname, dataset, format = 'GTiff',
                        dstNodata=fillvalue, creationOptions=["COMPRESS=LZW"])
            return data
        else:
            return None

    def readgrid(self, gridname):

        dict_data = {}

        with open(gridname, 'r') as fp :
            strNCOLS = fp.readline()
            strNROWS = fp.readline()
            strXLLCORNER = fp.readline()
            strYLLCORNER = fp.readline()
            strCELLSIZE = fp.readline()
            strNODATA_VALUE = fp.readline()

        dict_data['cols'] = np.int32(strNCOLS.split()[1])
        dict_data['rows'] = np.int32(strNROWS.split()[1])
        dict_data['leftlon'] = np.float32(strXLLCORNER.split()[1])
        dict_data['bottomlat'] = np.float32(strYLLCORNER.split()[1])
        dict_data['resolution'] = np.float32(strCELLSIZE.split()[1])
        dict_data['fillvalue'] = np.float32(strNODATA_VALUE.split()[1])


        data = np.loadtxt(gridname, dtype=np.float32, skiprows=6)

        # data[(data<390) | (data > 430)] = np.nan

        if (data.shape[0] != dict_data['rows']) | (data.shape[1] != dict_data['cols']) :
            raise Exception('The Row: %d, The Col: %d, but the data region size is [%d, %d]' %(
                dict_data['rows'], dict_data['cols'], data.shape[0], data.shape[1]))

        dict_data['data'] = data

        return dict_data

    def readStationTXT(self, filename):
        ''' 解析从天擎下载的TXT数据文件 '''
        dict_data = {}
        if not os.path.isfile(filename):
            print("文件不存在【%s】" %filename)
            return dict_data

        temp = []
        datasize = 0

        fin = open(filename, 'r')#, encoding='utf-8')
        data = fin.readlines()
        for item in data[1:]:
            # 剔除数据中的各种标识符，缺失位用NULL填充
            item = item.strip('\n')
            item = item.strip('\r')
            item_split = item.split(' ')
            item_split = ['999999' if i == '' else i for i in item_split]

            # 记录总共有多少个字段
            if datasize == 0 :
                datasize = len(item_split)

            # Note:为了解决Datetime字段的日期和时间分割开的情况(YYYY-MM-DD HH:MM:SS)而设置,
            # 常规情况为（YYYYMMDDhhmmss）,将不做此操作
            if len(item_split[0]) == 10 and len(item_split[1]) == 8 :
                item_split[0] = '%s %s' %( item_split[0],  item_split[1])  # 将日期和时间拼接
                del item_split[1]

            # 将有异常的行数据剔除
            if len(item_split) != datasize  or datasize == 0:
                continue
            temp.append(item_split)

        # 如果没有下载到数据，则退出，返回空字典
        temp = np.array(temp)
        if temp.shape[0] == 0:
            print('该文件未包含站点数据信息')
            return dict_data

        # 按气象要素字段进行写入字典中
        for i in range(temp.shape[1]):
            key = temp[0, i]
            temp_data = temp[1:, i]
            if key in ['Province', 'City', 'Cnty', 'Station_Name', 'Station_Id_C', ]:
                temp_data = temp[1:, i]
            elif "Datetime" in key:
                temp_data = np.array(temp_data, dtype= '<S20') # dtype=np.int64)
            elif key in ["", ]:
                continue
                # temp_data = np.array(temp_data, dtype=np.int64) # dtype= '<S20')
            else:
                try:
                    temp_data = np.array(temp_data, dtype=np.float32)
                    temp_data[temp_data>99999.0] = np.nan
                except BaseException as e:
                    print(e)
                    print(key, temp_data)
                    continue
            # 字典中没有该字段，则新增；否则， 在字段基础上增加数据
            if not key in dict_data.keys():
                dict_data.update({ key : temp_data})
            else:
                dict_data[key].extend(temp_data)

        return dict_data

    def __del__(self):
        # pass
        for filename in self.tempfile :
            if os.path.isfile(filename) :
                try:
                    os.remove(filename)
                except BaseException as e :
                    print('删除失败：%s' %(filename))


