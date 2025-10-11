# -*- coding:utf-8 -*-
'''
@Project     : lb_toolkits  
----------------------------------------
@File        : EARTHCARE.py  
----------------------------------------
@Modify Time : 2025/9/22  
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

from .DataCollectionDefinition import DataCollectionDefinition

class DataCollectionEARTHCARE :

    ATL_NOM_1B_EarthCare_ESA = DataCollectionDefinition(
        api_id="earthcare",
        collections="EarthCAREL1Validated",
        provider="ESA",
        shortname="ATL_NOM_1B",
        version="1.2",
        description="ATL_NOM_1B"
    )

    BBR_NOM_1B_EarthCare_ESA = DataCollectionDefinition(
        api_id="earthcare",
        collections="EarthCAREL1Validated",
        provider="ESA",
        shortname="BBR_NOM_1B",
        version="1.2",
        description="BBR_NOM_1B"
    )

    BBR_SNG_1B_EarthCare_ESA = DataCollectionDefinition(
        api_id="earthcare",
        collections="EarthCAREL1Validated",
        provider="ESA",
        shortname="BBR_SNG_1B",
        version="1.2",
        description="BBR_SNG_1B"
    )

    MSI_NOM_1B_EarthCare_ESA = DataCollectionDefinition(
        api_id="earthcare",
        collections="EarthCAREL1Validated",
        provider="ESA",
        shortname="MSI_NOM_1B",
        version="1.2",
        description="MSI_NOM_1B"
    )

    MSI_RGR_1C_EarthCare_ESA = DataCollectionDefinition(
        api_id="earthcare",
        collections="EarthCAREL1Validated",
        provider="ESA",
        shortname="MSI_RGR_1C",
        version="1.2",
        description="MSI_RGR_1C"
    )

    AUX_JSG_1D_EarthCare_ESA = DataCollectionDefinition(
        api_id="earthcare",
        collections="EarthCAREL1Validated",
        provider="ESA",
        shortname="AUX_JSG_1D",
        version="1.2",
        description="AUX_JSG_1D"
    )

    CPR_NOM_1B_EarthCare_ESA = DataCollectionDefinition(
        api_id="earthcare",
        collections="EarthCAREL1Validated",
        provider="ESA",
        shortname="CPR_NOM_1B",
        version="1.2",
        description="CPR_NOM_1B"
    )

    AC_TC_2B_EarthCare_ESA = DataCollectionDefinition(
        api_id="earthcare",
        collections="EarthCAREL2Validated",
        provider="ESA",
        shortname="AC__TC__2B",
        version="1.2",
        description="AC__TC__2B"
    )

    AM_ACD_2B_EarthCare_ESA = DataCollectionDefinition(
        api_id="earthcare",
        collections="EarthCAREL2Validated",
        provider="ESA",
        shortname="AM__ACD_2B",
        version="1.2",
        description="AM__ACD_2B"
    )

    AM_CTH_2B_EarthCare_ESA = DataCollectionDefinition(
        api_id="earthcare",
        collections="EarthCAREL2Validated",
        provider="ESA",
        shortname="AM__CTH_2B",
        version="1.2",
        description="AM__CTH_2B"
    )

    ATL_AER_2A_EarthCare_ESA = DataCollectionDefinition(
        api_id="earthcare",
        collections="EarthCAREL2Validated",
        provider="ESA",
        shortname="ATL_AER_2A",
        version="1.2",
        description="ATL_AER_2A"
    )

    ATL_ALD_2A_EarthCare_ESA = DataCollectionDefinition(
        api_id="earthcare",
        collections="EarthCAREL2Validated",
        provider="ESA",
        shortname="ATL_ALD_2A",
        version="1.2",
        description="ATL_ALD_2A"
    )

    ATL_CTH_2A_EarthCare_ESA = DataCollectionDefinition(
        api_id="earthcare",
        collections="EarthCAREL2Validated",
        provider="ESA",
        shortname="ATL_CTH_2A",
        version="1.2",
        description="ATL_CTH_2A"
    )

    ATL_EBD_2A_EarthCare_ESA = DataCollectionDefinition(
        api_id="earthcare",
        collections="EarthCAREL2Validated",
        provider="ESA",
        shortname="ATL_EBD_2A",
        version="1.2",
        description="ATL_EBD_2A"
    )

    ATL_FM_2A_EarthCare_ESA = DataCollectionDefinition(
        api_id="earthcare",
        collections="EarthCAREL2Validated",
        provider="ESA",
        shortname="ATL_FM__2A",
        version="1.2",
        description="ATL_FM__2A"
    )

    ATL_ICE_2A_EarthCare_ESA = DataCollectionDefinition(
        api_id="earthcare",
        collections="EarthCAREL2Validated",
        provider="ESA",
        shortname="ATL_ICE_2A",
        version="1.2",
        description="ATL_ICE_2A"
    )

    ATL_TC_2A_EarthCare_ESA = DataCollectionDefinition(
        api_id="earthcare",
        collections="EarthCAREL2Validated",
        provider="ESA",
        shortname="ATL_TC__2A",
        version="1.2",
        description="ATL_TC__2A"
    )

    BM_RAD_2B_EarthCare_ESA = DataCollectionDefinition(
        api_id="earthcare",
        collections="EarthCAREL2Validated",
        provider="ESA",
        shortname="BM__RAD_2B",
        version="1.2",
        description="BM__RAD_2B"
    )

    CPR_CD_2A_EarthCare_ESA = DataCollectionDefinition(
        api_id="earthcare",
        collections="EarthCAREL2Validated",
        provider="ESA",
        shortname="CPR_CD__2A",
        version="1.2",
        description="CPR_CD__2A"
    )

    CPR_CLD_2A_EarthCare_ESA = DataCollectionDefinition(
        api_id="earthcare",
        collections="EarthCAREL2Validated",
        provider="ESA",
        shortname="CPR_CLD_2A",
        version="1.2",
        description="CPR_CLD_2A"
    )

    CPR_FMR_2A_EarthCare_ESA = DataCollectionDefinition(
        api_id="earthcare",
        collections="EarthCAREL2Validated",
        provider="ESA",
        shortname="CPR_FMR_2A",
        version="1.2",
        description="CPR_FMR_2A"
    )

    CPR_TC_2A_EarthCare_ESA = DataCollectionDefinition(
        api_id="earthcare",
        collections="EarthCAREL2Validated",
        provider="ESA",
        shortname="CPR_TC__2A",
        version="1.2",
        description="CPR_TC__2A"
    )

    MSI_AOT_2A_EarthCare_ESA = DataCollectionDefinition(
        api_id="earthcare",
        collections="EarthCAREL2Validated",
        provider="ESA",
        shortname="MSI_AOT_2A",
        version="1.2",
        description="MSI_AOT_2A"
    )

    MSI_CM__2A_EarthCare_ESA = DataCollectionDefinition(
        api_id="earthcare",
        collections="EarthCAREL2Validated",
        provider="ESA",
        shortname="MSI_CM__2A",
        version="1.2",
        description="MSI_CM__2A"
    )

    MSI_COP_2A_EarthCare_ESA = DataCollectionDefinition(
        api_id="earthcare",
        collections="EarthCAREL2Validated",
        provider="ESA",
        shortname="MSI_COP_2A",
        version="1.2",
        description="MSI_COP_2A"
    )

