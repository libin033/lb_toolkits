# -*- coding:utf-8 -*-

from lb_toolkits.DataCollections.DataCollectionDefinition import DataCollectionDefinition 

class DataCollectionOMINRT : 
    OMCLDRR_V003_OMINRT = DataCollectionDefinition(
            api_id="CMR",
            collections="OMINRT_OMCLDRR_003",
            provider="OMINRT", 
            shortname="OMCLDRR",
            version="003",
            description="OMI/Aura Cloud Pressure and Fraction (Raman Scattering) 1-Orbit L2 Swath 13x24 km V003 NRT version: 003"
        )

    OMAERUV_V003_OMINRT = DataCollectionDefinition(
            api_id="CMR",
            collections="OMINRT_OMAERUV_003",
            provider="OMINRT", 
            shortname="OMAERUV",
            version="003",
            description="OMI/Aura Near UV Aerosol Optical Depth and Single Scattering Albedo 1-orbit L2 Swath 13x24 km V003 NRT version: 003"
        )

    OMTO3_V003_OMINRT = DataCollectionDefinition(
            api_id="CMR",
            collections="OMINRT_OMTO3_003",
            provider="OMINRT", 
            shortname="OMTO3",
            version="003",
            description="OMI/Aura Ozone (O3) Total Column 1-Orbit L2 Swath 13x24 km V003 NRT version: 003"
        )

    OMTO3E_V003_OMINRT = DataCollectionDefinition(
            api_id="CMR",
            collections="OMINRT_OMTO3e_003",
            provider="OMINRT", 
            shortname="OMTO3e",
            version="003",
            description="OMI/Aura Ozone (O3) Total Column Daily L3 Global 0.25deg Lat/Lon Grid NRT version: 003"
        )

    OMSO2_V003_OMINRT = DataCollectionDefinition(
            api_id="CMR",
            collections="OMINRT_OMSO2_003",
            provider="OMINRT", 
            shortname="OMSO2",
            version="003",
            description="OMI/Aura Sulphur Dioxide (SO2) Total Column 1-orbit L2 Swath 13x24 km V003 NRT version: 003"
        )

    OMPS_N20_NMUVAI_L2_NRT_V2_OMINRT = DataCollectionDefinition(
            api_id="CMR",
            collections="OMINRT_OMPS_N20_NMUVAI_L2_NRT_2",
            provider="OMINRT", 
            shortname="OMPS_N20_NMUVAI_L2_NRT",
            version="2",
            description="OMPS-N20 L2 NM Aerosol Index swath orbital NRT version: 2"
        )

    OMPS_N20_NMSO2_PCA_L2_STEP1_NRT_V1_OMINRT = DataCollectionDefinition(
            api_id="CMR",
            collections="OMINRT_OMPS_N20_NMSO2_PCA_L2_Step1_NRT_1",
            provider="OMINRT", 
            shortname="OMPS_N20_NMSO2_PCA_L2_Step1_NRT",
            version="1",
            description="OMPS-N20 NM PCA SO2 Step 1 Total Column 1-Orbit L2 Swath 17x13km NRT version: 1"
        )

    OMPS_N21_NMUVAI_L2_NRT_V2_OMINRT = DataCollectionDefinition(
            api_id="CMR",
            collections="OMINRT_OMPS_N21_NMUVAI_L2_NRT_2",
            provider="OMINRT", 
            shortname="OMPS_N21_NMUVAI_L2_NRT",
            version="2",
            description="OMPS-N21 L2 NM Aerosol Index swath orbital NRT version: 2"
        )

    OMPS_N21_LP_NRT_AER_V1_OMINRT = DataCollectionDefinition(
            api_id="CMR",
            collections="OMINRT_OMPS_N21_LP_NRT_AER_1",
            provider="OMINRT", 
            shortname="OMPS_N21_LP_NRT_AER",
            version="1",
            description="OMPS-N21 LP NRT Aerosol Extinction Vertical Profile swath multi-wavelength orbital 3slit version: 1"
        )

    OMPS_N21_LP_L2_O3_NRT_V1_OMINRT = DataCollectionDefinition(
            api_id="CMR",
            collections="OMINRT_OMPS_N21_LP_L2_O3_NRT_1",
            provider="OMINRT", 
            shortname="OMPS_N21_LP_L2_O3_NRT",
            version="1",
            description="OMPS-N21 LP NRT L2 LP Ozone (O3) Vertical Profile swath daily Center slit V2.6 version: 1"
        )

    NMMIEAI_L2_NRT_V2_OMINRT = DataCollectionDefinition(
            api_id="CMR",
            collections="OMINRT_NMMIEAI-L2-NRT_2",
            provider="OMINRT", 
            shortname="NMMIEAI-L2-NRT",
            version="2",
            description="OMPS-NPP L2 NM Aerosol Index swath orbital NRT version: 2"
        )

    NMTO3NRT_V2_OMINRT = DataCollectionDefinition(
            api_id="CMR",
            collections="OMINRT_NMTO3NRT_2",
            provider="OMINRT", 
            shortname="NMTO3NRT",
            version="2",
            description="OMPS-NPP L2 NM Ozone (O3) Total Column swath orbital NRT version: 2"
        )

    NPBUVO3_L2_NRT_V2_OMINRT = DataCollectionDefinition(
            api_id="CMR",
            collections="OMINRT_NPBUVO3-L2-NRT_2",
            provider="OMINRT", 
            shortname="NPBUVO3-L2-NRT",
            version="2",
            description="OMPS-NPP L2 NP Ozone (O3) Vertical Profile swath orbital NRT version: 2"
        )

    OMPS_NPP_LP_NRT_AER_V1_OMINRT = DataCollectionDefinition(
            api_id="CMR",
            collections="OMINRT_OMPS_NPP_LP_NRT_AER_1",
            provider="OMINRT", 
            shortname="OMPS_NPP_LP_NRT_AER",
            version="1",
            description="OMPS-NPP LP NRT Aerosol Extinction Vertical Profile swath multi-wavelength orbital 3slit version: 1"
        )

    OMPS_NPP_LP_L2_O3_NRT_V1_OMINRT = DataCollectionDefinition(
            api_id="CMR",
            collections="OMINRT_OMPS_NPP_LP_L2_O3_NRT_1",
            provider="OMINRT", 
            shortname="OMPS_NPP_LP_L2_O3_NRT",
            version="1",
            description="OMPS-NPP LP NRT L2 LP Ozone (O3) Vertical Profile swath daily Center slit V2.6 version: 1"
        )

    NMSO2_PCA_L2_NRT_V2_OMINRT = DataCollectionDefinition(
            api_id="CMR",
            collections="OMINRT_NMSO2-PCA-L2-NRT_2",
            provider="OMINRT", 
            shortname="NMSO2-PCA-L2-NRT",
            version="2",
            description="OMPS/NPP PCA SO2 Total Column 1-Orbit L2 Swath 50x50km NRT version: 2"
        )

    OMICOL3NRT_V3_OMINRT = DataCollectionDefinition(
            api_id="CMR",
            collections="OMINRT_OMICOL3NRT_3",
            provider="OMINRT", 
            shortname="OMICOL3NRT",
            version="3",
            description="Ozone Monitoring Instrument Near Real Time Data for v3 version: 3"
        )

