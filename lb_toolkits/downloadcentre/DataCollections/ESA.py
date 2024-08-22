# -*- coding:utf-8 -*-
'''
@Project     : lb_toolkits  
----------------------------------------
@File        : ESA.py  
----------------------------------------
@Modify Time : 2024/8/22  
----------------------------------------
@Author      : Lee  
----------------------------------------
@Desciption
----------------------------------------
      
 https://browser.dataspace.copernicus.eu/
'''

from .DataCollectionDefinition import DataCollectionDefinition

class DataCollectionESA :

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

    ESA_SENTINEL1_SLC = DataCollectionDefinition(
        api_id='ESAAPI',
        collections="SENTINEL-1",
        bands=['SLC', 'GRD', 'OCN', 'RAW'],
        productType='SLC',
        has_cloud_coverage=True,
        description='SENTINEL-1 单视复数影像，Single Look Complex'
    )

    ESA_SENTINEL1_GRD = DataCollectionDefinition(
        api_id='ESAAPI',
        collections="SENTINEL-1",
        bands=['SLC', 'GRD', 'OCN', 'RAW'],
        productType='GRD',
        has_cloud_coverage=True,
        description='SENTINEL-1 地距多视影像，Ground Range Detected'
    )

    ESA_SENTINEL1_OCN = DataCollectionDefinition(
        api_id='ESAAPI',
        collections="SENTINEL-1",
        bands=['SLC', 'GRD', 'OCN', 'RAW'],
        productType='OCN',
        has_cloud_coverage=True,
        description='SENTINEL-1 OCN'
    )

    ESA_SENTINEL1_RAW = DataCollectionDefinition(
        api_id='ESAAPI',
        collections="SENTINEL-1",
        bands=[],
        productType='RAW',
        has_cloud_coverage=True,
        description='SENTINEL-1 原始影像'
    )

    ESA_SENTINEL2_S2MSI1C = DataCollectionDefinition(
        api_id='ESAAPI',
        collections="SENTINEL-2",
        bands=[],
        productType='S2MSI1C',
        has_cloud_coverage=True,
        description='SENTINEL-2 S2MSI1C 大气层顶部 (TOA) 反射率图像'
    )

    ESA_SENTINEL2_S2MSI2A = DataCollectionDefinition(
        api_id='ESAAPI',
        collections="SENTINEL-2",
        bands=[],
        productType='S2MSI2A',
        has_cloud_coverage=True,
        description='SENTINEL-2 S2MSI2A 经大气校正的表面反射率 (SR) 产品'
    )

    ESA_SENTINEL2_S2MS2Ap = DataCollectionDefinition(
        api_id='ESAAPI',
        collections="SENTINEL-2",
        bands=[],
        productType='S2MS2Ap',
        has_cloud_coverage=True,
        description='SENTINEL-2 S2MS2Ap '
    )

    ESA_SENTINEL3_SR_1_SRA = DataCollectionDefinition(
        api_id='ESAAPI',
        collections="SENTINEL-3",
        bands=[],
        productType='SR_1_SRA___',
        has_cloud_coverage=True,
        description='SENTINEL-3'
    )

    ESA_SENTINEL3_SR_1_SRA_A = DataCollectionDefinition(
        api_id='ESAAPI',
        collections="SENTINEL-3",
        bands=[],
        productType='SR_1_SRA_A_',
        has_cloud_coverage=True,
        description='SENTINEL-3'
    )

    ESA_SENTINEL3_SR_1_SRA_BS = DataCollectionDefinition(
        api_id='ESAAPI',
        collections="SENTINEL-3",
        bands=[],
        productType='SR_1_SRA_BS',
        has_cloud_coverage=True,
        description='SENTINEL-3'
    )

    ESA_SENTINEL3_SR_2_LAN = DataCollectionDefinition(
        api_id='ESAAPI',
        collections="SENTINEL-3",
        bands=[],
        productType='SR_2_LAN___',
        has_cloud_coverage=True,
        description='SENTINEL-3'
    )

    ESA_SENTINEL3_OL_1_EFR = DataCollectionDefinition(
        api_id='ESAAPI',
        collections="SENTINEL-3",
        bands=[],
        productType='OL_1_EFR___',
        has_cloud_coverage=True,
        description='SENTINEL-3 : 全分辨率 TOA 反射率'
    )

    ESA_SENTINEL3_OL_1_ERR = DataCollectionDefinition(
        api_id='ESAAPI',
        collections="SENTINEL-3",
        bands=[],
        productType='OL_1_ERR___',
        has_cloud_coverage=True,
        description='SENTINEL-3 : 降低分辨率 TOA 反射率'
    )

    ESA_SENTINEL3_OL_2_LFR = DataCollectionDefinition(
        api_id='ESAAPI',
        collections="SENTINEL-3",
        bands=[],
        productType='OL_2_LFR___',
        has_cloud_coverage=True,
        description='SENTINEL-3 全分辨率陆地和大气地球物理产品'
    )

    ESA_SENTINEL3_OL_2_LRR = DataCollectionDefinition(
        api_id='ESAAPI',
        collections="SENTINEL-3",
        bands=[],
        productType='OL_2_LRR___',
        has_cloud_coverage=True,
        description='SENTINEL-3 低分辨率陆地和大气地球物理产品'
    )
    ESA_SENTINEL3_SL_1_RBT = DataCollectionDefinition(
        api_id='ESAAPI',
        collections="SENTINEL-3",
        bands=[],
        productType='SL_1_RBT___',
        has_cloud_coverage=True,
        description='SENTINEL-3 亮度温度和辐射率'
    )

    ESA_SENTINEL3_SL_2_LST = DataCollectionDefinition(
        api_id='ESAAPI',
        collections="SENTINEL-3",
        bands=[],
        productType='SL_2_LST___',
        has_cloud_coverage=True,
        description='SENTINEL-3 : 地表温度参数'
    )

    ESA_SENTINEL3_SY_2_SYN = DataCollectionDefinition(
        api_id='ESAAPI',
        collections="SENTINEL-3",
        bands=[],
        productType='SY_2_SYN___',
        has_cloud_coverage=True,
        description='SENTINEL-3 : 陆地表面反射率和气溶胶参数'
    )

    ESA_SENTINEL3_SY_2_V10 = DataCollectionDefinition(
        api_id='ESAAPI',
        collections="SENTINEL-3",
        bands=[],
        productType='SY_2_V10___',
        has_cloud_coverage=True,
        description='SENTINEL-3'
    )

    ESA_SENTINEL3_SY_2_VG1 = DataCollectionDefinition(
        api_id='ESAAPI',
        collections="SENTINEL-3",
        bands=[],
        productType='SY_2_VG1___',
        has_cloud_coverage=True,
        description='SENTINEL-3 : 1 km 类植物产品 TOA 反射率'
    )

    ESA_SENTINEL3_SY_2_VGP = DataCollectionDefinition(
        api_id='ESAAPI',
        collections="SENTINEL-3",
        bands=[],
        productType='SY_2_VGP___',
        has_cloud_coverage=True,
        description='SENTINEL-3 : 1 km 类植物产品 1 天合成表面反射率和 NDVI'
    )

    ESA_SENTINEL5P_L1B_IR_SIR = DataCollectionDefinition(
        api_id='ESAAPI',
        collections="SENTINEL-5P",
        bands=[],
        productType='L1B_IR_SIR',
        has_cloud_coverage=True,
        description='SENTINEL-5P'
    )

    ESA_SENTINEL5P_L1B_IR_UVN = DataCollectionDefinition(
        api_id='ESAAPI',
        collections="SENTINEL-5P",
        bands=[],
        productType='L1B_IR_UVN',
        has_cloud_coverage=True,
        description='SENTINEL-5P'
    )

    ESA_SENTINEL5P_L1B_RA_BD1 = DataCollectionDefinition(
        api_id='ESAAPI',
        collections="SENTINEL-5P",
        bands=[],
        productType='L1B_RA_BD1',
        has_cloud_coverage=True,
        description='SENTINEL-5P'
    )

    ESA_SENTINEL5P_L1B_RA_BD2 = DataCollectionDefinition(
        api_id='ESAAPI',
        collections="SENTINEL-5P",
        bands=[],
        productType='L1B_RA_BD2',
        has_cloud_coverage=True,
        description='SENTINEL-5P'
    )

    ESA_SENTINEL5P_L1B_RA_BD3 = DataCollectionDefinition(
        api_id='ESAAPI',
        collections="SENTINEL-5P",
        bands=[],
        productType='L1B_RA_BD3',
        has_cloud_coverage=True,
        description='SENTINEL-5P'
    )

    ESA_SENTINEL5P_L1B_RA_BD4 = DataCollectionDefinition(
        api_id='ESAAPI',
        collections="SENTINEL-5P",
        bands=[],
        productType='L1B_RA_BD4',
        has_cloud_coverage=True,
        description='SENTINEL-5P'
    )

    ESA_SENTINEL5P_L1B_RA_BD5 = DataCollectionDefinition(
        api_id='ESAAPI',
        collections="SENTINEL-5P",
        bands=[],
        productType='L1B_RA_BD5',
        has_cloud_coverage=True,
        description='SENTINEL-5P'
    )

    ESA_SENTINEL5P_L1B_RA_BD6 = DataCollectionDefinition(
        api_id='ESAAPI',
        collections="SENTINEL-5P",
        bands=[],
        productType='L1B_RA_BD6',
        has_cloud_coverage=True,
        description='SENTINEL-5P'
    )

    ESA_SENTINEL5P_L1B_RA_BD7 = DataCollectionDefinition(
        api_id='ESAAPI',
        collections="SENTINEL-5P",
        bands=[],
        productType='L1B_RA_BD7',
        has_cloud_coverage=True,
        description='SENTINEL-5P'
    )

    ESA_SENTINEL5P_L1B_RA_BD8 = DataCollectionDefinition(
        api_id='ESAAPI',
        collections="SENTINEL-5P",
        bands=[],
        productType='L1B_RA_BD8',
        has_cloud_coverage=True,
        description='SENTINEL-5P'
    )

    ESA_SENTINEL5P_L2__AER_AI = DataCollectionDefinition(
        api_id='ESAAPI',
        collections="SENTINEL-5P",
        bands=[],
        productType='L2__AER_AI',
        has_cloud_coverage=True,
        description='SENTINEL-5P 紫外线气溶胶指数'
    )

    ESA_SENTINEL5P_L2__AER_LH = DataCollectionDefinition(
        api_id='ESAAPI',
        collections="SENTINEL-5P",
        bands=[],
        productType='L2__AER_LH',
        has_cloud_coverage=True,
        description='SENTINEL-5P 气溶胶层高度（中等气压）'
    )

    ESA_SENTINEL5P_L2__CH4 = DataCollectionDefinition(
        api_id='ESAAPI',
        collections="SENTINEL-5P",
        bands=[],
        productType='L2__CH4___',
        has_cloud_coverage=True,
        description='SENTINEL-5P 甲烷（CH4）总柱含量'
    )

    ESA_SENTINEL5P_L2__CLOUD = DataCollectionDefinition(
        api_id='ESAAPI',
        collections="SENTINEL-5P",
        bands=[],
        productType='L2__CLOUD_',
        has_cloud_coverage=True,
        description='SENTINEL-5P 云量、反照率、云顶大气压'
    )

    ESA_SENTINEL5P_L2__CO = DataCollectionDefinition(
        api_id='ESAAPI',
        collections="SENTINEL-5P",
        bands=[],
        productType='L2__CO____',
        has_cloud_coverage=True,
        description='SENTINEL-5P 一氧化碳（CO）总柱含量'
    )

    ESA_SENTINEL5P_L2__HCHO = DataCollectionDefinition(
        api_id='ESAAPI',
        collections="SENTINEL-5P",
        bands=[],
        productType='L2__HCHO__',
        has_cloud_coverage=True,
        description='SENTINEL-5P 甲醛（HCHO）总柱含量'
    )

    ESA_SENTINEL5P_L2__NO2 = DataCollectionDefinition(
        api_id='ESAAPI',
        collections="SENTINEL-5P",
        bands=[],
        productType='L2__NO2___',
        has_cloud_coverage=True,
        description='SENTINEL-5P 二氧化氮（NO2）总柱含量、对流层柱含量'
    )

    ESA_SENTINEL5P_L2__NP_BD3 = DataCollectionDefinition(
        api_id='ESAAPI',
        collections="SENTINEL-5P",
        bands=[],
        productType='L2__NP_BD3',
        has_cloud_coverage=True,
        description='SENTINEL-5P'
    )

    ESA_SENTINEL5P_L2__NP_BD6 = DataCollectionDefinition(
        api_id='ESAAPI',
        collections="SENTINEL-5P",
        bands=[],
        productType='L2__NP_BD6',
        has_cloud_coverage=True,
        description='SENTINEL-5P'
    )

    ESA_SENTINEL5P_L2__NP_BD7 = DataCollectionDefinition(
        api_id='ESAAPI',
        collections="SENTINEL-5P",
        bands=[],
        productType='L2__NP_BD7',
        has_cloud_coverage=True,
        description='SENTINEL-5P'
    )

    ESA_SENTINEL5P_L2__O3_TCL = DataCollectionDefinition(
        api_id='ESAAPI',
        collections="SENTINEL-5P",
        bands=[],
        productType='L2__O3_TCL',
        has_cloud_coverage=True,
        description='SENTINEL-5P'
    )

    ESA_SENTINEL5P_L2__O3 = DataCollectionDefinition(
        api_id='ESAAPI',
        collections="SENTINEL-5P",
        bands=[],
        productType='L2__O3____',
        has_cloud_coverage=True,
        description='SENTINEL-5P 臭氧（O3）总柱含量'
    )

    ESA_SENTINEL5P_L2__SO2 = DataCollectionDefinition(
        api_id='ESAAPI',
        collections="SENTINEL-5P",
        bands=[],
        productType='L2__SO2',
        has_cloud_coverage=True,
        description='SENTINEL-5P 二氧化硫（SO2）总柱含量'
    )
