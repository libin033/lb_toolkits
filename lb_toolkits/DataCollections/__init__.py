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

from .OTHER import *



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
    DataCollectionUSGS,
) :

    def __init__(self):
        pass




