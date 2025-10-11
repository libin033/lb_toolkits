# -*- coding:utf-8 -*-
'''
@Project     : lb_toolkits  
----------------------------------------
@File        : JMA.py  
----------------------------------------
@Modify Time : 2025/4/6  
----------------------------------------
@Author      : Lee  
----------------------------------------
@Desciption
----------------------------------------
      
 
'''
import os
import sys
import numpy as np
import datetime

from docutils.nodes import description

from .DataCollectionDefinition import DataCollectionDefinition


class DataCollectionAHI :

    AHI_L1_FLDK_2KM_NC_JMA = DataCollectionDefinition(
        api_id='AHI',
        collections="L1NC",
        shortname='06001_06001',
        version='L1NC',
        description='AHI L1级 2KM Netcdf数据'
    )

    AHI_L1_FLDK_5KM_NC_JMA = DataCollectionDefinition(
        api_id='AHI',
        collections='L1NC',
        shortname="02401_02401",
        version='L1NC',
        description='AHI L1级 5KM Netcdf数据'
    )

    AHI_L1_FLDK_HSD_JMA = DataCollectionDefinition(
        api_id='AHI',
        collections="L1HSD",
        version='L1',
        blockid=np.arange(1,10+1),
        bands=np.arange(1,16+1),
        description='AHI L1级HSD数据'
    )

    AHI_L2_CLP_NC_JMA = DataCollectionDefinition(
        api_id='AHI',
        collections='L2',
        shortname="CLP",
        version='010',
        description='AHI L2级5KM云产品'
    )

    AHI_L2_ARP_NC_JMA = DataCollectionDefinition(
        api_id='AHI',
        collections='L2',
        shortname="ARP",
        version='031',
        description='AHI L2级 ARP'
    )

    AHI_L2_PAR_NC_JMA = DataCollectionDefinition(
        api_id='AHI',
        collections='L2',
        shortname="PAR",
        version='021',
        description='AHI L2级 PAR'
    )

    AHI_L2_WLF_NC_JMA = DataCollectionDefinition(
        api_id='AHI',
        collections='L2',
        shortname="WLF",
        version='010',
        description='AHI L2级 WLF'
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

