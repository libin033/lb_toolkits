# -*- coding:utf-8 -*-
'''
@Project     : lb_toolkits  
----------------------------------------
@File        : __init__.py.py  
----------------------------------------
@Modify Time : 2024/8/21  
----------------------------------------
@Author      : Lee  
----------------------------------------
@Desciption
----------------------------------------
      
 
'''

from .DataCollectionDefinition import DataCollectionDefinition
from .ASF import DataCollectionASF
from .CDDIS import DataCollectionCDDIS
from .GES_DISC import DataCollectionGES_DISC
from .GHRC_DAAC import DataCollectionGHRC_DAAC
from .LAADS import DataCollectionLAADS
from .LANCEAMSR2 import DataCollectionLANCEAMSR2
from .LANCEMODIS import DataCollectionLANCEMODIS
from .LARC import DataCollectionLARC
from .LARC_ASDC import DataCollectionLARC_ASDC
from .LARC_CLOUD import DataCollectionLARC_CLOUD
from .LM_FIRMS import DataCollectionLM_FIRMS
from .LPCLOUD import DataCollectionLPCLOUD
from .LPDAAC_ECS import DataCollectionLPDAAC_ECS
from .NSIDCV0 import DataCollectionNSIDCV0
from .NSIDC_CPRD import DataCollectionNSIDC_CPRD
from .NSIDC_ECS import DataCollectionNSIDC_ECS
from .OB_DAAC import DataCollectionOB_DAAC
from .OMINRT import DataCollectionOMINRT
from .ORNL_CLOUD import DataCollectionORNL_CLOUD
from .POCLOUD import DataCollectionPOCLOUD
from .SEDAC import DataCollectionSEDAC
from .USGS_EROS import DataCollectionUSGS_EROS
from .USGS_LTA import DataCollectionUSGS_LTA

from .ESA import DataCollectionESA
from .USGS import DataCollectionUSGS


class DataCollectionLC :

    LANDCOVER_V003_ESRI = DataCollectionDefinition(
        api_id='LC',
        collections="esri_landcover",
        description='esri sentinel-2 10M landuse/landcover v003'
    )

class DataCollectionFY :

    FY_Order_NSMC = DataCollectionDefinition(
        api_id='FY',
        collections="FY_Products",
        description='通过订单号下载风云卫星数据产品'
    )

class DataCollectionAHI :

    AHI_L1_FLDK_NC_JMA = DataCollectionDefinition(
        api_id='AHI',
        collections="L1_6001",
        version='NC',
        description='AHI L1级Netcdf数据'
    )

    AHI_L1_FLDK_HSD_JMA = DataCollectionDefinition(
        api_id='AHI',
        collections="L1",
        version='HSD',
        blockid=[1,10],
        bands=['B01', 'B02', 'B03', 'B04', 'B05', 'B06', 'B07', 'B08',
               'B09', 'B10', 'B11', 'B12', 'B13', 'B14', 'B15', 'B16'],
        description='AHI L1级HSD数据'
    )

class DataCollectionHY :

    HY2B_OSDDS = DataCollectionDefinition(
        api_id='HY',
        collections="HY_Products",
        description='海洋卫星产品数据'
    )

class DataCollectionGFS :

    NOAA_NWP_GFS = DataCollectionDefinition(
        api_id='GFS',
        collections="GFS_NOAA",
        description='NOAA GFS预报数据'
    )

class DataCollectionERA5 :

    ECMWF_NWP_ERA5_Surf = DataCollectionDefinition(
        api_id='ERA5',
        collections="ERA5_Surf_ECMWF",
        description='ECMWF ERA5 陆表再分析资料'
    )

    ECMWF_NWP_ERA5_Prof = DataCollectionDefinition(
        api_id='ERA5',
        collections="ERA5_Prof_ECMWF",
        description='ECMWF ERA5 廓线再分析资料'
    )

class DataCollectionGOSAT :

    CO2_L3_V0305_GOSAT = DataCollectionDefinition(
        api_id='GOSAT',
        collections="L3",
        provider='GOSAT',
        shortname="CO2",
        version='V03.05',
        description='L3 global CO2 distribution (SWIR)'
    )

    CH4_L3_V0305_GOSAT = DataCollectionDefinition(
        api_id='GOSAT',
        collections="L3",
        provider='GOSAT',
        shortname="CH4",
        version='V03.05',
        description='L3 global CH4 distribution (SWIR)'
    )

    CO2_L2_V0305_GOSAT = DataCollectionDefinition(
        api_id='GOSAT',
        collections="L2",
        provider='GOSAT',
        shortname="CO2",
        version='V03.05',
        description='L2 CO2 column amount (SWIR)'
    )

    CO2_L2_V0298_GOSAT = DataCollectionDefinition(
        api_id='GOSAT',
        collections="L2",
        provider='GOSAT',
        shortname="CO2",
        version='V02.98',
        description='L2 CO2 column amount (SWIR)'
    )

    CO2_L2_V0297_GOSAT = DataCollectionDefinition(
        api_id='GOSAT',
        collections="L2",
        provider='GOSAT',
        shortname="CO2",
        version='V02.97',
        description='L2 CO2 column amount (SWIR)'
    )

    CH4_L2_V0305_GOSAT = DataCollectionDefinition(
        api_id='GOSAT',
        collections="L2",
        provider='GOSAT',
        shortname="CH4",
        version='V03.05',
        description='GOSAT FTS L2 CH4 column amount (SWIR)'
    )

    CH4_L2_V0296_GOSAT = DataCollectionDefinition(
        api_id='GOSAT',
        collections="L2",
        provider='GOSAT',
        shortname="CH4",
        version='V02.96',
        description='GOSAT FTS L2 CH4 column amount (SWIR)'
    )

    CH4_L2_V0295_GOSAT = DataCollectionDefinition(
        api_id='GOSAT',
        collections="L2",
        provider='GOSAT',
        shortname="CH4",
        version='V02.95',
        description='GOSAT FTS L2 CH4 column amount (SWIR)'
    )




class DataCollections(
    DataCollectionFY,
    DataCollectionHY,
    DataCollectionAHI,
    DataCollectionGFS,
    DataCollectionERA5,
    DataCollectionGOSAT,
    DataCollectionLC,
    DataCollectionASF,
    DataCollectionCDDIS,
    DataCollectionGES_DISC,
    DataCollectionGHRC_DAAC,
    DataCollectionLAADS,
    DataCollectionLANCEAMSR2,
    DataCollectionLANCEMODIS,
    DataCollectionLARC,
    DataCollectionLARC_ASDC,
    DataCollectionLARC_CLOUD,
    DataCollectionLM_FIRMS,
    DataCollectionLPCLOUD,
    DataCollectionLPDAAC_ECS,
    DataCollectionNSIDCV0,
    DataCollectionNSIDC_CPRD,
    DataCollectionNSIDC_ECS,
    DataCollectionOB_DAAC,
    DataCollectionOMINRT,
    DataCollectionORNL_CLOUD,
    DataCollectionPOCLOUD,
    DataCollectionSEDAC,
    DataCollectionUSGS_EROS,
    DataCollectionUSGS_LTA,
    DataCollectionESA,
    DataCollectionUSGS
) :

    def __init__(self):
        pass




