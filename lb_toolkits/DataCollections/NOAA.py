# -*- coding:utf-8 -*-
'''
@Project     : lb_toolkits  
----------------------------------------
@File        : NOAA.py  
----------------------------------------
@Modify Time : 2025/7/26  
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

class DataCollectionNOAA :

    ABI_INCAL_NOAA = DataCollectionDefinition(
        api_id='NOAA',
        collections="ABIINCAL",
        productType='',
        description='ABI Instrument Calibration Data'
    )

    ABI_L1ALG_NOAA = DataCollectionDefinition(
        api_id='NOAA',
        collections="ABIL1ALG",
        productType='',
        description='ABI L1b Algorithm Package'
    )

    ABIL1PARM_NOAA = DataCollectionDefinition(
        api_id='NOAA',
        collections="ABIL1PARM",
        productType='',
        description='ABI Llb Processing Parameters'
    )

    ABI_L1RAD_NOAA = DataCollectionDefinition(
        api_id='NOAA',
        collections="ABIL1RAD",
        productType=["ACHA","ACHA2KM","ACHP2KM","ACHT",
                     "ACM","ACTP","ADP","AICE","AIM",
                     "AITA","AOD","BRF","CCL","CMIP",
                     "COD","COD2KM","CPS","CTP",
                     "DMW","DMWDIAG","DMWPQI",
                     "DMWV","DMWVDIAG","DMWVPQI",
                     "DSI","DSR","FDC","FSC",
                     "LSA","LST","LST2KM","LVMP","LVTP",
                     "MCMIP","PAR","Rad","RRQPE","RSR","SST","TPW"],
        description='ABI L2+ Fog/Low Stratus'
    )

    AFMIDAYE_NOAA = DataCollectionDefinition(
        api_id='NOAA',
        collections="AFMIDAYE",
        productType='',
        description='ABI L2 Flood Map 1-Day Gridded Composite (GOEs-East)'
    )

    AFMIDAYW_NOAA = DataCollectionDefinition(
        api_id='NOAA',
        collections="AFMIDAYW",
        productType='',
        description='ABI L2 Flood Map 1-Day Gridded Composite (GOES-West)'
    )

    ABIL2ALG_NOAA = DataCollectionDefinition(
        api_id='NOAA',
        collections="ABIL2ALG",
        productType='',
        description='ABI L2+ Algorithm Package'
    )

    ABIL2CMIP_NOAA = DataCollectionDefinition(
        api_id='NOAA',
        collections="ABIL2CMIP",
        productType='',
        description='ABI L2+ Cloud & Moisture Imagery Data'
    )


    ABI_GFLS_NOAA = DataCollectionDefinition(
        api_id='NOAA',
        collections="ABI_GFLS",
        productType=None,
        description='ABI L2+ Fog/Low Stratus'
    )

    ABIL2PARM_NOAA = DataCollectionDefinition(
        api_id='NOAA',
        collections="ABIL2PARM",
        productType='',
        description='ABI L2+ Processing Parameters'
    )

    ABIL2PROD_NOAA = DataCollectionDefinition(
        api_id='NOAA',
        collections="ABIL2PROD",
        productType='',
        description='ABI L2+ Product Data'
    )

    ADRSTROPCY_NOAA = DataCollectionDefinition(
        api_id='NOAA',
        collections="ADRSTROPCY",
        productType='',
        description='ADRS Ancillary Data - Atlantic Tropical Cyclone and Pacific Tropical Cyclone Discussion files'
    )

    ADRSNWP_NOAA = DataCollectionDefinition(
        api_id='NOAA',
        collections="ADRSNWP",
        productType='',
        description='ADRS Ancillary Data - Nwp Model 0utput X Cycle Xx-Hour Forecast'
    )
    ADRSNRTSIX_NOAA = DataCollectionDefinition(
        api_id='NOAA',
        collections="ADRSNRTSIX",
        productType='',
        description='ADRS Ancillary Data -Near Real-Time Snow and Ice Extent- DMSP Platform XX'
    )
    ADRSREYSST_NOAA = DataCollectionDefinition(
        api_id='NOAA',
        collections="ADRSREYSST",
        productType='',
        description='ADRS Ancillary Data -Reynolds Daily Sea Surface Temperature'
    )
    ADRSSNOICE_NOAA = DataCollectionDefinition(
        api_id='NOAA',
        collections="ADRSSNOICE",
        productType='',
        description='ADRS Ancillary Data- Snow/Ice Analysis'
    )
    EXISINCAL_NOAA = DataCollectionDefinition(
        api_id='NOAA',
        collections="EXISINCAL",
        productType='',
        description='EXIS Instrument Calibration Data'
    )

    EXISL1PARM_NOAA = DataCollectionDefinition(
        api_id='NOAA',
        collections="EXISL1PARM",
        productType='',
        description='EXIS Llb Processing Parameters'
    )
    EXISLISFEU_NOAA = DataCollectionDefinition(
        api_id='NOAA',
        collections="EXISLISFEU",
        productType='',
        description='EXIS Llb Solar Flux: Extreme Ultraviolet (EUV) Data'
    )
    EXISL1SFXR_NOAA = DataCollectionDefinition(
        api_id='NOAA',
        collections="EXISL1SFXR",
        productType='',
        description='EXIS L1b Solar Flux: X-Ray Sensor (XRS) Data'
    )
    GLMINCAL_NOAA = DataCollectionDefinition(
        api_id='NOAA',
        collections="GLMINCAL",
        productType='',
        description='GLM Instrument Calibration Data'
    )

    GLML1BALG_NOAA = DataCollectionDefinition(
        api_id='NOAA',
        collections="GLML1BALG",
        productType='',
        description='GLM LlB Algorithm Package'
    )
    GLML1PARM_NOAA = DataCollectionDefinition(
        api_id='NOAA',
        collections="GLML1PARM",
        productType='',
        description='GLM L1b Processing Parameters'
    )
    GLML2ALG_NOAA = DataCollectionDefinition(
        api_id='NOAA',
        collections="GLML2ALG",
        productType='',
        description='GLM L2+ Algorithm Package'
    )
    GLML2LCFA_NOAA = DataCollectionDefinition(
        api_id='NOAA',
        collections="GLML2LCFA",
        productType='',
        description='GLM L2+ Lightning Detection Data'
    )
    GLML2PARM_NOAA = DataCollectionDefinition(
        api_id='NOAA',
        collections="GLML2PARM",
        productType='',
        description='GLM L2+ Processing Parameters'
    )
    GRBINF0_NOAA = DataCollectionDefinition(
        api_id='NOAA',
        collections="GRBINF0",
        productType='',
        description='GRB Information Packets'
    )
    ISOSERIES_NOAA = DataCollectionDefinition(
        api_id='NOAA',
        collections="ISOSERIES",
        productType='',
        description='IS0 series level metadata'
    )

    MAGINCAL_NOAA = DataCollectionDefinition(
        api_id='NOAA',
        collections="MAGINCAL",
        productType='',
        description='MAG Instrument Calibration Data'
    )
    MAGL1GEOF_NOAA = DataCollectionDefinition(
        api_id='NOAA',
        collections="MAGL1GEOF",
        productType='',
        description='MAG Llb Geomagnetic Field Data'
    )

    MAGL1PARM_NOAA = DataCollectionDefinition(
        api_id='NOAA',
        collections="MAGL1PARM",
        productType='',
        description='MAG Llb Processing Parameters'
    )
    SEISINCAL_NOAA = DataCollectionDefinition(
        api_id='NOAA',
        collections="SEISINCAL",
        productType='',
        description='SEISS Instrument Calibration Data'
    )
    SEISL1EHIS_NOAA = DataCollectionDefinition(
        api_id='NOAA',
        collections="SEISL1EHIS",
        productType='',
        description='SEISS Llb Energetic Heavy lons Data'
    )
    SEISLIMPSL_NOAA = DataCollectionDefinition(
        api_id='NOAA',
        collections="SEISLIMPSL",
        productType='',
        description='SEISs Llb Magnetospheric Electrons AND Protons: Low Energy Data'
    )
    SEISLIMPSH_NOAA = DataCollectionDefinition(
        api_id='NOAA',
        collections="SEISLIMPSH",
        productType='',
        description='SEISs Llb Magnetospheric Electrons and Protons: Medium & High Energy Data'
    )
    SEISL1PARM_NOAA = DataCollectionDefinition(
        api_id='NOAA',
        collections="SEISL1PARM",
        productType='',
        description='SEISS L1b Processing Parameters'
    )
    SEISL1SGPS_NOAA = DataCollectionDefinition(
        api_id='NOAA',
        collections="SEISL1SGPS",
        productType='',
        description='SEISS Llb Solar and Galactic Protons Data'
    )
    SUVIINCAL_NOAA = DataCollectionDefinition(
        api_id='NOAA',
        collections="SUVIINCAL",
        productType='',
        description='SUVI Instrument Calibration Data'
    )
    SUVIL1PARM_NOAA = DataCollectionDefinition(
        api_id='NOAA',
        collections="SUVIL1PARM",
        productType='',
        description='SUVI Llb Processing Parameters'
    )
    SUVIL1SIXR_NOAA = DataCollectionDefinition(
        api_id='NOAA',
        collections="SUVIL1SIXR",
        productType='',
        description='SUVI Llb Solar Imagery X-Ray Iron/Helium in Angstroms Data'
    )
    SATINCAL_NOAA = DataCollectionDefinition(
        api_id='NOAA',
        collections="SATINCAL",
        productType='',
        description='Satellite Instrument Calibration Ephemeris Data'
    )
    VFM1DAY_NOAA = DataCollectionDefinition(
        api_id='NOAA',
        collections="VFM1DAY",
        productType='',
        description='VIIRS Flood Map 1-Day Gridded Composite'
    )
    VFM5DAY_NOAA = DataCollectionDefinition(
        api_id='NOAA',
        collections="VFM5DAY",
        productType='',
        description='VIIRS Flood Map 5-Day Gridded Composite'
    )
    RAVE13KM_NOAA = DataCollectionDefinition(
        api_id='NOAA',
        collections="RAVE13KM",
        productType='',
        description='VIIRS eFires RAVE Product at 13km Resolution'
    )
    RAVE3KM_NOAA = DataCollectionDefinition(
        api_id='NOAA',
        collections="RAVE3KM",
        productType='',
        description='VIIRS eFires RAVE Product at 3km Resolution'
    )
