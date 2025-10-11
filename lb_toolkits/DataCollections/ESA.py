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

    SENTINEL1_SLC_ESA = DataCollectionDefinition(
        api_id='ESA',
        collections="SENTINEL-1",
        bands=['SLC', 'GRD', 'OCN', 'RAW'],
        productType='SLC',
        has_cloud_coverage=True,
        description='SENTINEL-1 单视复数影像，Single Look Complex'
    )

    SENTINEL1_GRD_ESA = DataCollectionDefinition(
        api_id='ESA',
        collections="SENTINEL-1",
        bands=['SLC', 'GRD', 'OCN', 'RAW'],
        productType='GRD',
        has_cloud_coverage=True,
        description='SENTINEL-1 地距多视影像，Ground Range Detected'
    )

    SENTINEL1_OCN_ESA = DataCollectionDefinition(
        api_id='ESA',
        collections="SENTINEL-1",
        bands=['SLC', 'GRD', 'OCN', 'RAW'],
        productType='OCN',
        has_cloud_coverage=True,
        description='SENTINEL-1 OCN'
    )

    SENTINEL1_RAW_ESA = DataCollectionDefinition(
        api_id='ESA',
        collections="SENTINEL-1",
        bands=[],
        productType='RAW',
        has_cloud_coverage=True,
        description='SENTINEL-1 原始影像'
    )

    SENTINEL2_S2MSI1C_ESA = DataCollectionDefinition(
        api_id='ESA',
        collections="SENTINEL-2",
        bands=[],
        productType='S2MSI1C',
        has_cloud_coverage=True,
        description='SENTINEL-2 S2MSI1C 大气层顶部 (TOA) 反射率图像'
    )

    SENTINEL2_S2MSI2A_ESA = DataCollectionDefinition(
        api_id='ESA',
        collections="SENTINEL-2",
        bands=[],
        productType='S2MSI2A',
        has_cloud_coverage=True,
        description='SENTINEL-2 S2MSI2A 经大气校正的表面反射率 (SR) 产品'
    )

    SENTINEL2_S2MS2Ap_ESA = DataCollectionDefinition(
        api_id='ESA',
        collections="SENTINEL-2",
        bands=[],
        productType='S2MS2Ap',
        has_cloud_coverage=True,
        description='SENTINEL-2 S2MS2Ap '
    )

    SENTINEL3_SR_1_SRA_ESA = DataCollectionDefinition(
        api_id='ESA',
        collections="SENTINEL-3",
        bands=[],
        productType='SR_1_SRA___',
        has_cloud_coverage=True,
        description='SENTINEL-3'
    )

    SENTINEL3_SR_1_SRA_A_ESA = DataCollectionDefinition(
        api_id='ESA',
        collections="SENTINEL-3",
        bands=[],
        productType='SR_1_SRA_A_',
        has_cloud_coverage=True,
        description='SENTINEL-3'
    )

    SENTINEL3_SR_1_SRA_BS_ESA = DataCollectionDefinition(
        api_id='ESA',
        collections="SENTINEL-3",
        bands=[],
        productType='SR_1_SRA_BS',
        has_cloud_coverage=True,
        description='SENTINEL-3'
    )

    SENTINEL3_SR_2_LAN_ESA = DataCollectionDefinition(
        api_id='ESA',
        collections="SENTINEL-3",
        bands=[],
        productType='SR_2_LAN___',
        has_cloud_coverage=True,
        description='SENTINEL-3'
    )

    SENTINEL3_OL_1_EFR_ESA = DataCollectionDefinition(
        api_id='ESA',
        collections="SENTINEL-3",
        bands=[],
        productType='OL_1_EFR___',
        has_cloud_coverage=True,
        description='SENTINEL-3 : 全分辨率 TOA 反射率'
    )

    SENTINEL3_OL_1_ERR_ESA = DataCollectionDefinition(
        api_id='ESA',
        collections="SENTINEL-3",
        bands=[],
        productType='OL_1_ERR___',
        has_cloud_coverage=True,
        description='SENTINEL-3 : 降低分辨率 TOA 反射率'
    )

    SENTINEL3_OL_2_LFR_ESA = DataCollectionDefinition(
        api_id='ESA',
        collections="SENTINEL-3",
        bands=[],
        productType='OL_2_LFR___',
        has_cloud_coverage=True,
        description='SENTINEL-3 全分辨率陆地和大气地球物理产品'
    )

    SENTINEL3_OL_2_LRR_ESA = DataCollectionDefinition(
        api_id='ESA',
        collections="SENTINEL-3",
        bands=[],
        productType='OL_2_LRR___',
        has_cloud_coverage=True,
        description='SENTINEL-3 低分辨率陆地和大气地球物理产品'
    )
    SENTINEL3_SL_1_RBT_ESA = DataCollectionDefinition(
        api_id='ESA',
        collections="SENTINEL-3",
        bands=[],
        productType='SL_1_RBT___',
        has_cloud_coverage=True,
        description='SENTINEL-3 亮度温度和辐射率'
    )

    SENTINEL3_SL_2_LST_ESA = DataCollectionDefinition(
        api_id='ESA',
        collections="SENTINEL-3",
        bands=[],
        productType='SL_2_LST___',
        has_cloud_coverage=True,
        description='SENTINEL-3 : 地表温度参数'
    )

    SENTINEL3_SY_2_SYN_ESA = DataCollectionDefinition(
        api_id='ESA',
        collections="SENTINEL-3",
        bands=[],
        productType='SY_2_SYN___',
        has_cloud_coverage=True,
        description='SENTINEL-3 : 陆地表面反射率和气溶胶参数'
    )

    SENTINEL3_SY_2_V10_ESA = DataCollectionDefinition(
        api_id='ESA',
        collections="SENTINEL-3",
        bands=[],
        productType='SY_2_V10___',
        has_cloud_coverage=True,
        description='SENTINEL-3'
    )

    SENTINEL3_SY_2_VG1_ESA = DataCollectionDefinition(
        api_id='ESA',
        collections="SENTINEL-3",
        bands=[],
        productType='SY_2_VG1___',
        has_cloud_coverage=True,
        description='SENTINEL-3 : 1 km 类植物产品 TOA 反射率'
    )

    SENTINEL3_SY_2_VGP_ESA = DataCollectionDefinition(
        api_id='ESA',
        collections="SENTINEL-3",
        bands=[],
        productType='SY_2_VGP___',
        has_cloud_coverage=True,
        description='SENTINEL-3 : 1 km 类植物产品 1 天合成表面反射率和 NDVI'
    )

    SENTINEL5P_L1B_IR_SIR_ESA = DataCollectionDefinition(
        api_id='ESA',
        collections="SENTINEL-5P",
        bands=[],
        productType='L1B_IR_SIR',
        has_cloud_coverage=True,
        description='SENTINEL-5P'
    )

    SENTINEL5P_L1B_IR_UVN_ESA = DataCollectionDefinition(
        api_id='ESA',
        collections="SENTINEL-5P",
        bands=[],
        productType='L1B_IR_UVN',
        has_cloud_coverage=True,
        description='SENTINEL-5P'
    )

    SENTINEL5P_L1B_RA_BD1_ESA = DataCollectionDefinition(
        api_id='ESA',
        collections="SENTINEL-5P",
        bands=[],
        productType='L1B_RA_BD1',
        has_cloud_coverage=True,
        description='SENTINEL-5P'
    )

    SENTINEL5P_L1B_RA_BD2_ESA = DataCollectionDefinition(
        api_id='ESA',
        collections="SENTINEL-5P",
        bands=[],
        productType='L1B_RA_BD2',
        has_cloud_coverage=True,
        description='SENTINEL-5P'
    )

    SENTINEL5P_L1B_RA_BD3_ESA = DataCollectionDefinition(
        api_id='ESA',
        collections="SENTINEL-5P",
        bands=[],
        productType='L1B_RA_BD3',
        has_cloud_coverage=True,
        description='SENTINEL-5P'
    )

    SENTINEL5P_L1B_RA_BD4_ESA = DataCollectionDefinition(
        api_id='ESA',
        collections="SENTINEL-5P",
        bands=[],
        productType='L1B_RA_BD4',
        has_cloud_coverage=True,
        description='SENTINEL-5P'
    )

    SENTINEL5P_L1B_RA_BD5_ESA = DataCollectionDefinition(
        api_id='ESA',
        collections="SENTINEL-5P",
        bands=[],
        productType='L1B_RA_BD5',
        has_cloud_coverage=True,
        description='SENTINEL-5P'
    )

    SENTINEL5P_L1B_RA_BD6_ESA = DataCollectionDefinition(
        api_id='ESA',
        collections="SENTINEL-5P",
        bands=[],
        productType='L1B_RA_BD6',
        has_cloud_coverage=True,
        description='SENTINEL-5P'
    )

    SENTINEL5P_L1B_RA_BD7_ESA = DataCollectionDefinition(
        api_id='ESA',
        collections="SENTINEL-5P",
        bands=[],
        productType='L1B_RA_BD7',
        has_cloud_coverage=True,
        description='SENTINEL-5P'
    )

    SENTINEL5P_L1B_RA_BD8_ESA = DataCollectionDefinition(
        api_id='ESA',
        collections="SENTINEL-5P",
        bands=[],
        productType='L1B_RA_BD8',
        has_cloud_coverage=True,
        description='SENTINEL-5P'
    )

    SENTINEL5P_L2_AER_AI_ESA = DataCollectionDefinition(
        api_id='ESA',
        collections="SENTINEL-5P",
        bands=[],
        productType='L2__AER_AI',
        has_cloud_coverage=True,
        description='SENTINEL-5P 紫外线气溶胶指数'
    )

    SENTINEL5P_L2_AER_LH_ESA = DataCollectionDefinition(
        api_id='ESA',
        collections="SENTINEL-5P",
        bands=[],
        productType='L2__AER_LH',
        has_cloud_coverage=True,
        description='SENTINEL-5P 气溶胶层高度（中等气压）'
    )

    SENTINEL5P_L2_CH4_ESA = DataCollectionDefinition(
        api_id='ESA',
        collections="SENTINEL-5P",
        bands=[],
        productType='L2__CH4___',
        has_cloud_coverage=True,
        description='SENTINEL-5P 甲烷（CH4）总柱含量'
    )

    SENTINEL5P_L2_CLOUD_ESA = DataCollectionDefinition(
        api_id='ESA',
        collections="SENTINEL-5P",
        bands=[],
        productType='L2__CLOUD_',
        has_cloud_coverage=True,
        description='SENTINEL-5P 云量、反照率、云顶大气压'
    )

    SENTINEL5P_L2_CO_ESA = DataCollectionDefinition(
        api_id='ESA',
        collections="SENTINEL-5P",
        bands=[],
        productType='L2__CO____',
        has_cloud_coverage=True,
        description='SENTINEL-5P 一氧化碳（CO）总柱含量'
    )

    SENTINEL5P_L2_HCHO_ESA = DataCollectionDefinition(
        api_id='ESA',
        collections="SENTINEL-5P",
        bands=[],
        productType='L2__HCHO__',
        has_cloud_coverage=True,
        description='SENTINEL-5P 甲醛（HCHO）总柱含量'
    )

    SENTINEL5P_L2_NO2_ESA = DataCollectionDefinition(
        api_id='ESA',
        collections="SENTINEL-5P",
        bands=[],
        productType='L2__NO2___',
        has_cloud_coverage=True,
        description='SENTINEL-5P 二氧化氮（NO2）总柱含量、对流层柱含量'
    )

    SENTINEL5P_L2_NP_BD3_ESA = DataCollectionDefinition(
        api_id='ESA',
        collections="SENTINEL-5P",
        bands=[],
        productType='L2__NP_BD3',
        has_cloud_coverage=True,
        description='SENTINEL-5P'
    )

    SENTINEL5P_L2_NP_BD6_ESA = DataCollectionDefinition(
        api_id='ESA',
        collections="SENTINEL-5P",
        bands=[],
        productType='L2__NP_BD6',
        has_cloud_coverage=True,
        description='SENTINEL-5P'
    )

    SENTINEL5P_L2_NP_BD7_ESA = DataCollectionDefinition(
        api_id='ESA',
        collections="SENTINEL-5P",
        bands=[],
        productType='L2__NP_BD7',
        has_cloud_coverage=True,
        description='SENTINEL-5P'
    )

    SENTINEL5P_L2_O3_TCL_ESA = DataCollectionDefinition(
        api_id='ESA',
        collections="SENTINEL-5P",
        bands=[],
        productType='L2__O3_TCL',
        has_cloud_coverage=True,
        description='SENTINEL-5P'
    )

    SENTINEL5P_L2_O3_ESA = DataCollectionDefinition(
        api_id='ESA',
        collections="SENTINEL-5P",
        bands=[],
        productType='L2__O3____',
        has_cloud_coverage=True,
        description='SENTINEL-5P 臭氧（O3）总柱含量'
    )

    SENTINEL5P_L2_SO2_ESA = DataCollectionDefinition(
        api_id='ESA',
        collections="SENTINEL-5P",
        bands=[],
        productType='L2__SO2___',
        has_cloud_coverage=True,
        description='SENTINEL-5P 二氧化硫（SO2）总柱含量'
    )

    SENTINEL6_ESA = DataCollectionDefinition(
        api_id='ESA',
        collections="SENTINEL-6",
        bands=[],
        productType='',
        has_cloud_coverage=True,
        description='SENTINEL-6'
    )

    SENTINEL6_ESA = DataCollectionDefinition(
        api_id='ESA',
        collections="SENTINEL-6",
        bands=[],
        productType='',
        has_cloud_coverage=True,
        description='SENTINEL-6'
    )

    SENTINEL1_RTC_ESA = DataCollectionDefinition(
        api_id='ESA',
        collections="SENTINEL-1-RTC",
        bands=[],
        productType='',
        has_cloud_coverage=True,
        description='SENTINEL-1-RTC'
    )

    GLOBAL_MOSAICS_ESA = DataCollectionDefinition(
        api_id='ESA',
        collections="GLOBAL-MOSAICS",
        bands=[],
        productType='',
        has_cloud_coverage=True,
        description='GLOBAL-MOSAICS'
    )

    SMOS_ESA = DataCollectionDefinition(
        api_id='ESA',
        collections="SMOS",
        bands=[],
        productType='',
        has_cloud_coverage=True,
        description='SMOS'
    )

    ENVISAT_ESA = DataCollectionDefinition(
        api_id='ESA',
        collections="ENVISAT",
        bands=[],
        productType='',
        has_cloud_coverage=True,
        description='ENVISAT'
    )

    LANDSAT5_ESA = DataCollectionDefinition(
        api_id='ESA',
        collections="LANDSAT-5",
        bands=[],
        productType='',
        has_cloud_coverage=True,
        description='LANDSAT-5'
    )

    LANDSAT7_ESA = DataCollectionDefinition(
        api_id='ESA',
        collections="LANDSAT-7",
        bands=[],
        productType='',
        has_cloud_coverage=True,
        description='LANDSAT-7'
    )

    LANDSAT8_ESA = DataCollectionDefinition(
        api_id='ESA',
        collections="LANDSAT-8",
        bands=[],
        productType='',
        has_cloud_coverage=True,
        description='LANDSAT-8'
    )

    COP_DEM_ESA = DataCollectionDefinition(
        api_id='ESA',
        collections="COP-DEM",
        bands=[],
        productType='',
        has_cloud_coverage=True,
        description='COP-DEM'
    )

    TERRAAQUA_ESA = DataCollectionDefinition(
        api_id='ESA',
        collections="TERRAAQUA",
        bands=[],
        productType='',
        has_cloud_coverage=True,
        description='TERRAAQUA'
    )

    S2GLC_ESA = DataCollectionDefinition(
        api_id='ESA',
        collections="S2GLC",
        bands=[],
        productType='',
        has_cloud_coverage=True,
        description='S2GLC'
    )
