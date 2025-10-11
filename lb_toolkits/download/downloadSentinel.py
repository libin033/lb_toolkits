# -*- coding:utf-8 -*-
'''
@Project  : lb_toolkits

@File     : downloadSentinel.py

@Modify Time : 2022/8/11 15:34

@Author : Lee

@Version : 1.0

@Description :

'''
import datetime
from lb_toolkits.utils.sentinel import SentinelAPI, read_geojson, geojson_to_wkt

# Sentinel-1
s1prodtype =  ['SLC', 'GRD', 'OCN', 'RAW']

# Sentinel-2
s2prodtype = ['S2MSI2A', 'S2MSI1C', 'S2MS2Ap']

# Sentinel-3
s3prodtype = ['SR_1_SRA___', 'SR_1_SRA_A_', 'SR_1_SRA_BS',
              'SR_2_LAN___', 'OL_1_EFR___', 'OL_1_ERR___', 'OL_2_LFR___',
              'OL_2_LRR___', 'SL_1_RBT___', 'SL_2_LST___', 'SY_2_SYN___',
              'SY_2_V10___', 'SY_2_VG1___', 'SY_2_VGP___']

# Sentinel-5P
s5pprodtype = ['L1B_IR_SIR', 'L1B_IR_UVN', 'L1B_RA_BD1', 'L1B_RA_BD2',
               'L1B_RA_BD3', 'L1B_RA_BD4', 'L1B_RA_BD5', 'L1B_RA_BD6',
               'L1B_RA_BD7', 'L1B_RA_BD8', 'L2__AER_AI', 'L2__AER_LH',
               'L2__CH4___', 'L2__CLOUD_', 'L2__CO____', 'L2__HCHO__',
               'L2__NO2___', 'L2__NP_BD3', 'L2__NP_BD6',
               'L2__NP_BD7', 'L2__O3_TCL', 'L2__O3____', 'L2__SO2___']


class downloadSentinel :

    SENTINEL_1     = 'SENTINEL-1'
    SENTINEL_2     = 'SENTINEL-2'
    SENTINEL_3     = 'SENTINEL-3'
    SENTINEL_5P    = 'SENTINEL-5P'
    SENTINEL_6     = 'SENTINEL-6'
    SENTINEL_1_RTC = 'SENTINEL-1-RTC'
    GLOBAL_MOSAICS = 'GLOBAL-MOSAICS'
    SMOS           = 'SMOS'
    ENVISAT        = 'ENVISAT'
    LANDSAT_5      = 'LANDSAT-5'
    LANDSAT_7      = 'LANDSAT-7'
    LANDSAT_8      = 'LANDSAT-8'
    COP_DEM        = 'COP-DEM'
    TERRAAQUA      = 'TERRAAQUA'
    S2GLC          = 'S2GLC'


    def __init__(self, username, password):

        self.username = username
        self.password = password
        self.api = SentinelAPI(self.username, self.password)

    def searchfile(self, starttime, endtime=None, collection=None, producttype=None,
                   bbox=None, footprint=None, geojson=None, filename='*', **kwargs):
        '''
        see 'https://scihub.copernicus.eu/twiki/do/view/SciHubUserGuide/3FullTextSearch'

        Parameters
        ----------
        starttime : datetime
            起始时间
        endtime: datetime, optional
            结束时间
        collection : str
             Sentinel-1/Sentinel-2/Sentinel-3/Sentinel-5P,其他参考Landsat
        producttype: str
            - Sentinel-1: SLC, GRD, OCN, RAW
            - Sentinel-2: S2MSI2A,S2MSI1C, S2MS2Ap
            - Sentinel-3: SR_1_SRA___, SR_1_SRA_A_, SR_1_SRA_BS,
                          SR_2_LAN___, OL_1_EFR___, OL_1_ERR___, OL_2_LFR___,
                          OL_2_LRR___, SL_1_RBT___, SL_2_LST___, SY_2_SYN___,
                          SY_2_V10___, SY_2_VG1___, SY_2_VGP___.
            - Sentinel-5P: L1B_IR_SIR, L1B_IR_UVN, L1B_RA_BD1, L1B_RA_BD2,
                           L1B_RA_BD3, L1B_RA_BD4, L1B_RA_BD5, L1B_RA_BD6,
                           L1B_RA_BD7, L1B_RA_BD8, L2__AER_AI, L2__AER_LH,
                           L2__CH4___, L2__CLOUD_, L2__CO____, L2__HCHO__,
                           L2__NO2___, L2__NP_BD3, L2__NP_BD6,
                           L2__NP_BD7, L2__O3_TCL, L2__O3____, L2__SO2___.
        bbox : minX, minY, maxX, maxY(must be WGS84(epgs:4326))
        footprint: str
        geojson: str, optional
            geogson format
        filename: str
            模糊匹配文件名，eg.*1SD?_20141003T003840*
        keywords:
            processinglevel='L2'
            processingmode='Near real time'
            cloudcoverpercentage : e.g. [0 TO 9.4] or float
        Returns
        -------

        '''
        #创建SentinelAPI，使用copernicus的账号和密码，注册链接：
        # https://identity.dataspace.copernicus.eu/auth/realms/CDSE/login-actions/registration?client_id=cdse-public&tab_id=mpk-ZhY-bY0
        if endtime is None :
            endtime = starttime+datetime.timedelta(days=1, seconds=-1)

        #读入某地区的geojson文件并转换为wkt格式的文件对象，相当于足迹
        if footprint is None and geojson is not None:
            footprint =geojson_to_wkt(read_geojson(geojson))

        if bbox is not None :
            footprint = "POLYGON(({minX} {minY},{minX} {maxY},{maxX} {maxY},{maxX} {minY},{minX} {minY}))".format(
                minX=bbox[0],
                minY=bbox[1],
                maxX=bbox[2],
                maxY=bbox[3],
            )

        #通过设置OpenSearch API查询参数筛选符合条件的所有数据
        products = self.api.query(
            collection=collection,        #卫星平台名，Sentinel-2
            area=footprint,                        #Area范围
            date=(starttime, endtime),        #搜索的日期范围
            productType=producttype,            #
            filename=filename,
            **kwargs)

        return products

        # collection, producttype = self.CheckParm(collection, producttype)
        # if collection in ['Sentinel-1', 's1', 'S1'] :
        #     return self.searchS1()
        # elif collection in ['Sentinel-2', 's2', 'S2']:
        #     return self.searchS2(starttime, endtime, collection, producttype, footprint, filename, **kwargs)
        # elif collection in ['Sentinel-3', 's3', 'S3'] :
        #     return self.searchS3(starttime, endtime, collection, producttype, footprint, filename, **kwargs)
        # elif collection in ['Sentinel-5', 'Sentinel-5P', 's5', 'S5', 'Sentinel-5 Precursor']:
        #     return self.searchS5P(starttime, endtime, collection, producttype, footprint, filename, **kwargs)
        # else:
        #     raise Exception('请检查参数platformname【%s】不是指定卫星【Sentinel-1、Sentinel-2、Sentinel-3、Sentinel-5】')

    def download(self, outdir, product_info, timeout=5 * 60, skip_download=False):
        '''
        根据输入url下载相应的文件

        Parameters
        ----------
        outdir: str
            输出路径
        product_info : str
            下载链接
        token : str
            EarthData账号的APP Keys
        timeout : int
            时间限制
        skip : bool
            是否不做数据下载，直接返回文件名。默认是FALSE，下载文件。
        Returns
        -------
            str
            下载数据的文件名
        '''

        # #通过OData API获取单一产品数据的主要元数据信息
        # product_info = self.api.get_product_odata(url)
        #
        # #打印下载的产品数据文件名
        # print('下载文件【%s】' %(product_info['title']))
        # if skip :
        #     # print(product_info['Online'])
        #     return product_info['title']

        #下载产品id为product的产品数据
        return self.api.download(product_info, directory_path=outdir, checksum=False, skip_download=skip_download)
        # self.api.download_quicklook(url, directory_path=outdir)

    def searchS1(self, starttime, endtime, platformname, producttype, footprint=None, filename='*',
                 polarisationmode=None, sensoroperationalmode=None):

        if polarisationmode is not None :
            if not polarisationmode in ['HH', 'VV', 'HV', 'VH', 'HH+HV', 'VV+VH'] :
                raise Exception('请确认参数polarisationmode【%s】' %(polarisationmode))

        if sensoroperationalmode is not None :
            if not sensoroperationalmode in ['SM', 'IW', 'EW', 'WV'] :
                raise Exception('请确认参数sensoroperationalmode【%s】' %(sensoroperationalmode))

        #通过设置OpenSearch API查询参数筛选符合条件的所有Sentinel-2
        products = self.api.query(area=footprint,                        #Area范围
                                  date=(starttime, endtime),        #搜索的日期范围
                                  platformname=platformname,        #卫星平台名，Sentinel-2
                                  producttype=producttype,            #
                                  filename=filename,
                                  polarisationmode=polarisationmode,
                                  sensoroperationalmode=sensoroperationalmode)

        return products

    def searchS2(self, starttime, endtime, platformname, producttype, footprint=None, filename='*',
                 relativeorbitnumber=None, cloudcoverpercentage=None):

        if relativeorbitnumber is not None :
            if (relativeorbitnumber < 1) or (relativeorbitnumber > 143) :
                raise Exception('请确认参数relativeorbitnumber【%d】' %(relativeorbitnumber))

        #通过设置OpenSearch API查询参数筛选符合条件的所有Sentinel-2
        products = self.api.query(area=footprint,                        #Area范围
                                  date=(starttime, endtime),        #搜索的日期范围
                                  platformname=platformname,        #卫星平台名，Sentinel-2
                                  producttype=producttype,            #
                                  filename=filename,
                                  relativeorbitnumber=relativeorbitnumber,
                                  cloudcoverpercentage=cloudcoverpercentage)

        return products

    def searchS3(self, starttime, endtime, platformname, producttype, footprint=None, filename='*',
                 timeliness=None, instrumentshortname=None, productlevel=None):

        if timeliness is not None :
            if not timeliness in ['Near Real Time', 'Short Time Critical', 'Non Time Critical'] :
                raise Exception("请确认参数timeliness【%s】, "
                                "'Near Real Time', 'Short Time Critical', 'Non Time Critical'" %(timeliness))

        if productlevel is not None :
            if not productlevel in ['L1', 'L2'] :
                raise Exception('请确认参数productlevel【%s】' %(productlevel))

        if instrumentshortname is not None :
            if not instrumentshortname in ['OLCI', 'SRAL', 'SLSTR', 'SYNERGY'] :
                raise Exception('请确认参数instrumentshortname【%s】' %(instrumentshortname))

        #通过设置OpenSearch API查询参数筛选符合条件的所有Sentinel-2
        products = self.api.query(area=footprint,                        #Area范围
                                  date=(starttime, endtime),        #搜索的日期范围
                                  platformname=platformname,        #卫星平台名，Sentinel-2
                                  producttype=producttype,            #
                                  filename=filename,
                                  timeliness=timeliness,
                                  instrumentshortname=instrumentshortname,
                                  productlevel=productlevel)

        return products

    def searchS5P(self, starttime, endtime, platformname, producttype, footprint=None, filename='*',
                  processinglevel=None, processingmode=None):
        if processinglevel is not None :
            if not processinglevel in ['L1B', 'L2'] :
                raise Exception("请确认参数processinglevel【%s】" %(processinglevel))

        if processingmode is not None :
            if not processingmode in ['Near real time', 'Offline', 'Reprocessing'] :
                raise Exception('请确认参数processingmode【%s】, "【Near real time】, 【Offline】, 【Reprocessing】"'
                                %(processingmode))

        #通过设置OpenSearch API查询参数筛选符合条件的所有Sentinel-2
        products = self.api.query(area=footprint,                        #Area范围
                                  date=(starttime, endtime),        #搜索的日期范围
                                  platformname=platformname,        #卫星平台名，Sentinel-2
                                  producttype=producttype,            #
                                  filename=filename,
                                  processinglevel=processinglevel,
                                  processingmode=processingmode)

        return products

    def CheckParm(self, platformname, producttype):

        # 根据传入的平台和产品名，检查是否合理
        platformname, producttype = self.Checkproducttype(platformname, producttype)

        self.api =SentinelAPI(self.username, self.password)

        # if platformname in ['Sentinel-5 Precursor', 'Sentinel-5'] :
        #     self.platformname = 'Sentinel-5'
        #     self.api =SentinelAPI(self.username, self.password,'https://s5phub.copernicus.eu/dhus/')
        # else:
        #     self.api =SentinelAPI(self.username, self.password, 'https://scihub.copernicus.eu/dhus/')
        # self.api =SentinelAPI(self.username, self.password, 'https://scihub.copernicus.eu/apihub/')

        return platformname, producttype

    def Checkproducttype(self, platformname, producttype):
        if platformname in ['Sentinel-1', 's1', 'S1'] :
            platformname = 'Sentinel-1'
            if producttype in s1prodtype :
                return platformname, producttype
            else:
                print('请在以下参数中选择', s1prodtype)
                raise Exception('请确认产品类型【%s】！！！' %(producttype))

        elif platformname in ['Sentinel-2', 's2', 'S2']:
            platformname = 'Sentinel-2'
            if producttype in s2prodtype:
                return platformname, producttype
            else:
                print('请在以下参数中选择', s2prodtype)
                raise Exception('请确认产品类型【%s】！！！' %(producttype))

        elif platformname in ['Sentinel-3', 's3', 'S3'] :
            platformname = 'Sentinel-3'
            if producttype in s3prodtype:
                return platformname, producttype
            else:
                print('请在以下参数中选择', s3prodtype)
                raise Exception('请确认产品类型【%s】！！！' %(producttype))
        elif platformname in ['Sentinel-5', 'Sentinel-5P', 's5', 'S5', 'Sentinel-5 Precursor']:
            platformname = 'Sentinel-5'
            if producttype in s5pprodtype:
                return platformname, producttype
            else:
                print('请在以下参数中选择', s5pprodtype)
                raise Exception('请确认产品类型【%s】！！！' %(producttype))
        else:
            raise Exception('请检查参数platformname【%s】不是指定卫星【Sentinel-1、Sentinel-2、Sentinel-3、Sentinel-5】')





