# -*- coding:utf-8 -*-

from lb_toolkits.DataCollections.DataCollectionDefinition import DataCollectionDefinition 

class DataCollectionLANCEMODIS : 
    AM1EPHNE_V61NRT_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_AM1EPHNE_6.1NRT",
            provider="LANCEMODIS", 
            shortname="AM1EPHNE",
            version="6.1NRT",
            description="Files containing only extrapolated orbital metadata, to be read via SDP Toolkit, Binary Format version: 6.1NRT"
        )

    PM1EPHND_NRT_V61NRT_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_PM1EPHND_NRT_6.1NRT",
            provider="LANCEMODIS", 
            shortname="PM1EPHND_NRT",
            version="6.1NRT",
            description="MODIS/Aqua 24-hour Spacecraft ephemeris/orbit data files to be read via SDP Toolkit Binary Format - NRT version: 6.1NRT"
        )

    MYDGB0_V61NRT_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_MYDGB0_6.1NRT",
            provider="LANCEMODIS", 
            shortname="MYDGB0",
            version="6.1NRT",
            description="MODIS/Aqua 5-minute GBAD data in L0 format - NRT version: 6.1NRT"
        )

    MYD04_L2_V61NRT_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_MYD04_L2_6.1NRT",
            provider="LANCEMODIS", 
            shortname="MYD04_L2",
            version="6.1NRT",
            description="MODIS/Aqua Aerosol 5-Min L2 Swath 10km - NRT version: 6.1NRT"
        )

    MYD04_3K_V61NRT_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_MYD04_3K_6.1NRT",
            provider="LANCEMODIS", 
            shortname="MYD04_3K",
            version="6.1NRT",
            description="MODIS/Aqua Aerosol 5-Min L2 Swath 3km - NRT version: 6.1NRT"
        )

    MYD09CMA_V61NRT_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_MYD09CMA_6.1NRT",
            provider="LANCEMODIS", 
            shortname="MYD09CMA",
            version="6.1NRT",
            description="MODIS/Aqua Aerosol Optical Thickness Daily L3 Global 0.05-Deg CMA NRT version: 6.1NRT"
        )

    MYD09_V61NRT_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_MYD09_6.1NRT",
            provider="LANCEMODIS", 
            shortname="MYD09",
            version="6.1NRT",
            description="MODIS/Aqua Atmospherically Corrected Surface Reflectance 5-Min L2 Swath 250m, 500m, 1km NRT version: 6.1NRT"
        )

    MYD021KM_V61NRT_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_MYD021KM_6.1NRT",
            provider="LANCEMODIS", 
            shortname="MYD021KM",
            version="6.1NRT",
            description="MODIS/Aqua Calibrated Radiances 5-Min L1B Swath 1km - NRT version: 6.1NRT"
        )

    MYD02QKM_V61NRT_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_MYD02QKM_6.1NRT",
            provider="LANCEMODIS", 
            shortname="MYD02QKM",
            version="6.1NRT",
            description="MODIS/Aqua Calibrated Radiances 5-Min L1B Swath 250m - NRT version: 6.1NRT"
        )

    MYD02HKM_V61NRT_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_MYD02HKM_6.1NRT",
            provider="LANCEMODIS", 
            shortname="MYD02HKM",
            version="6.1NRT",
            description="MODIS/Aqua Calibrated Radiances 5-Min L1B Swath 500m - NRT version: 6.1NRT"
        )

    MYD35_L2_V61NRT_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_MYD35_L2_6.1NRT",
            provider="LANCEMODIS", 
            shortname="MYD35_L2",
            version="6.1NRT",
            description="MODIS/Aqua Cloud Mask and Spectral Test Results 5-Min L2 Swath 250m and 1km - NRT version: 6.1NRT"
        )

    MYD06_L2_V61NRT_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_MYD06_L2_6.1NRT",
            provider="LANCEMODIS", 
            shortname="MYD06_L2",
            version="6.1NRT",
            description="MODIS/Aqua Clouds 5-Min L2 Swath 1km and 5km - NRT version: 6.1NRT"
        )

    MYD03_V61NRT_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_MYD03_6.1NRT",
            provider="LANCEMODIS", 
            shortname="MYD03",
            version="6.1NRT",
            description="MODIS/Aqua Geolocation Fields 5-Min L1A Swath 1km - NRT version: 6.1NRT"
        )

    MYD00F_V61NRT_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_MYD00F_6.1NRT",
            provider="LANCEMODIS", 
            shortname="MYD00F",
            version="6.1NRT",
            description="MODIS/Aqua L0 PDS Data, 5-Min Swath - NRT version: 6.1NRT"
        )

    MYDAODHD_V61NRT_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_MYDAODHD_6.1NRT",
            provider="LANCEMODIS", 
            shortname="MYDAODHD",
            version="6.1NRT",
            description="MODIS/Aqua L3 Value-added Aerosol Optical Depth - NRT version: 6.1NRT"
        )

    MYD21_V61NRT_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_MYD21_6.1NRT",
            provider="LANCEMODIS", 
            shortname="MYD21",
            version="6.1NRT",
            description="MODIS/Aqua Land Surface Temperature/3-Band Emissivity 5-Min L2 1km NRT version: 6.1NRT"
        )

    MYD11_L2_V61NRT_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_MYD11_L2_6.1NRT",
            provider="LANCEMODIS", 
            shortname="MYD11_L2",
            version="6.1NRT",
            description="MODIS/Aqua Land Surface Temperature/Emissivity 5-Min L2 Swath 1km NRT version: 6.1NRT"
        )

    MYD02SSH_V61NRT_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_MYD02SSH_6.1NRT",
            provider="LANCEMODIS", 
            shortname="MYD02SSH",
            version="6.1NRT",
            description="MODIS/Aqua Level 1B Subsampled Calibrated Radiance 5Km - NRT version: 6.1NRT"
        )

    MYD01_V61NRT_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_MYD01_6.1NRT",
            provider="LANCEMODIS", 
            shortname="MYD01",
            version="6.1NRT",
            description="MODIS/Aqua Raw Radiances in Counts 5-Min L1A Swath - NRT version: 6.1NRT"
        )

    MYD29_V61NRT_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_MYD29_6.1NRT",
            provider="LANCEMODIS", 
            shortname="MYD29",
            version="6.1NRT",
            description="MODIS/Aqua Sea Ice Extent 5-Min L2 Swath 1km NRT version: 6.1NRT"
        )

    MYD10_L2_V61NRT_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_MYD10_L2_6.1NRT",
            provider="LANCEMODIS", 
            shortname="MYD10_L2",
            version="6.1NRT",
            description="MODIS/Aqua Snow Cover 5-Min L2 Swath 500m NRT version: 6.1NRT"
        )

    MYD09GA_V61NRT_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_MYD09GA_6.1NRT",
            provider="LANCEMODIS", 
            shortname="MYD09GA",
            version="6.1NRT",
            description="MODIS/Aqua Surface Reflectance Daily L2G Global 1km and 500m SIN Grid NRT version: 6.1NRT"
        )

    MYD09GQ_V61NRT_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_MYD09GQ_6.1NRT",
            provider="LANCEMODIS", 
            shortname="MYD09GQ",
            version="6.1NRT",
            description="MODIS/Aqua Surface Reflectance Daily L2G Global 250 m SIN Grid NRT version: 6.1NRT"
        )

    MYD09GQK_V61NRT_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_MYD09GQK_6.1NRT",
            provider="LANCEMODIS", 
            shortname="MYD09GQK",
            version="6.1NRT",
            description="MODIS/Aqua Surface Reflectance Daily L2G Global 250m SIN Grid NRT version: 6.1NRT"
        )

    MYD09GHK_V61NRT_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_MYD09GHK_6.1NRT",
            provider="LANCEMODIS", 
            shortname="MYD09GHK",
            version="6.1NRT",
            description="MODIS/Aqua Surface Reflectance Daily L2G Global 500m SIN Grid NRT version: 6.1NRT"
        )

    MYD09CMG_V61NRT_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_MYD09CMG_6.1NRT",
            provider="LANCEMODIS", 
            shortname="MYD09CMG",
            version="6.1NRT",
            description="MODIS/Aqua Surface Reflectance Daily L3 Global 0.05Deg CMG NRT version: 6.1NRT"
        )

    MYD09GST_V61NRT_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_MYD09GST_6.1NRT",
            provider="LANCEMODIS", 
            shortname="MYD09GST",
            version="6.1NRT",
            description="MODIS/Aqua Surface Reflectance Quality Daily L2G Global 1km SIN Grid NRT version: 6.1NRT"
        )

    MYD07_L2_V61NRT_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_MYD07_L2_6.1NRT",
            provider="LANCEMODIS", 
            shortname="MYD07_L2",
            version="6.1NRT",
            description="MODIS/Aqua Temperature and Water Vapor Profiles 5-Min L2 Swath 5km - NRT version: 6.1NRT"
        )

    MCD14DL_V61NRT_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_MCD14DL_6.1NRT",
            provider="LANCEMODIS", 
            shortname="MCD14DL",
            version="6.1NRT",
            description="MODIS/Aqua Terra Thermal Anomalies/Fire locations 1km FIRMS NRT (Vector data) version: 6.1NRT"
        )

    MYD14_V61NRT_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_MYD14_6.1NRT",
            provider="LANCEMODIS", 
            shortname="MYD14",
            version="6.1NRT",
            description="MODIS/Aqua Thermal Anomalies/Fire 5-Min L2 Swath 1km NRT version: 6.1NRT"
        )

    MYD05_L2_V61NRT_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_MYD05_L2_6.1NRT",
            provider="LANCEMODIS", 
            shortname="MYD05_L2",
            version="6.1NRT",
            description="MODIS/Aqua Total Precipitable Water Vapor 5-Min L2 Swath 1km and 5km - NRT version: 6.1NRT"
        )

    MCDWD_L3_NRT_V61_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_MCDWD_L3_NRT_6.1",
            provider="LANCEMODIS", 
            shortname="MCDWD_L3_NRT",
            version="6.1",
            description="MODIS/Aqua+Terra Global Flood Product L3 NRT 250m version: 6.1"
        )

    MCDWD_L3_F1C_NRT_V61_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_MCDWD_L3_F1C_NRT_6.1",
            provider="LANCEMODIS", 
            shortname="MCDWD_L3_F1C_NRT",
            version="6.1",
            description="MODIS/Aqua+Terra Global Flood Product L3 NRT 250m 1-day CS GeoTIFF version: 6.1"
        )

    MCDWD_L3_F1_NRT_V61_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_MCDWD_L3_F1_NRT_6.1",
            provider="LANCEMODIS", 
            shortname="MCDWD_L3_F1_NRT",
            version="6.1",
            description="MODIS/Aqua+Terra Global Flood Product L3 NRT 250m 1-day GeoTIFF version: 6.1"
        )

    MCDWD_L3_F2_NRT_V61_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_MCDWD_L3_F2_NRT_6.1",
            provider="LANCEMODIS", 
            shortname="MCDWD_L3_F2_NRT",
            version="6.1",
            description="MODIS/Aqua+Terra Global Flood Product L3 NRT 250m 2-day GeoTIFF version: 6.1"
        )

    MCDWD_L3_F3_NRT_V61_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_MCDWD_L3_F3_NRT_6.1",
            provider="LANCEMODIS", 
            shortname="MCDWD_L3_F3_NRT",
            version="6.1",
            description="MODIS/Aqua+Terra Global Flood Product L3 NRT 250m 3-day GeoTIFF version: 6.1"
        )

    MOD04_L2_V61NRT_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_MOD04_L2_6.1NRT",
            provider="LANCEMODIS", 
            shortname="MOD04_L2",
            version="6.1NRT",
            description="MODIS/Terra Aerosol 5-Min L2 Swath 10km - NRT version: 6.1NRT"
        )

    MOD04_3K_V61NRT_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_MOD04_3K_6.1NRT",
            provider="LANCEMODIS", 
            shortname="MOD04_3K",
            version="6.1NRT",
            description="MODIS/Terra Aerosol 5-Min L2 Swath 3km - NRT version: 6.1NRT"
        )

    MOD09CMA_V61NRT_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_MOD09CMA_6.1NRT",
            provider="LANCEMODIS", 
            shortname="MOD09CMA",
            version="6.1NRT",
            description="MODIS/Terra Aerosol Optical Thickness Daily L3 Global 0.05Deg CMA NRT version: 6.1NRT"
        )

    MOD09_V61NRT_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_MOD09_6.1NRT",
            provider="LANCEMODIS", 
            shortname="MOD09",
            version="6.1NRT",
            description="MODIS/Terra Atmospherically Corrected Surface Reflectance 5-Min L2 Swath 250m, 500m, 1km NRT version: 6.1NRT"
        )

    MOD021KM_V61NRT_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_MOD021KM_6.1NRT",
            provider="LANCEMODIS", 
            shortname="MOD021KM",
            version="6.1NRT",
            description="MODIS/Terra Calibrated Radiances 5-Min L1B Swath 1km - NRT version: 6.1NRT"
        )

    MOD02QKM_V61NRT_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_MOD02QKM_6.1NRT",
            provider="LANCEMODIS", 
            shortname="MOD02QKM",
            version="6.1NRT",
            description="MODIS/Terra Calibrated Radiances 5-Min L1B Swath 250m - NRT version: 6.1NRT"
        )

    MOD02HKM_V61NRT_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_MOD02HKM_6.1NRT",
            provider="LANCEMODIS", 
            shortname="MOD02HKM",
            version="6.1NRT",
            description="MODIS/Terra Calibrated Radiances 5-Min L1B Swath 500m - NRT version: 6.1NRT"
        )

    MOD35_L2_V61NRT_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_MOD35_L2_6.1NRT",
            provider="LANCEMODIS", 
            shortname="MOD35_L2",
            version="6.1NRT",
            description="MODIS/Terra Cloud Mask and Spectral Test Results 5-Min L2 Swath 250m and 1km - NRT version: 6.1NRT"
        )

    MOD06_L2_V61NRT_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_MOD06_L2_6.1NRT",
            provider="LANCEMODIS", 
            shortname="MOD06_L2",
            version="6.1NRT",
            description="MODIS/Terra Clouds 5-Min L2 Swath 1km and 5km - NRT version: 6.1NRT"
        )

    MOD03_V61NRT_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_MOD03_6.1NRT",
            provider="LANCEMODIS", 
            shortname="MOD03",
            version="6.1NRT",
            description="MODIS/Terra Geolocation Fields 5-Min L1A Swath 1km - NRT version: 6.1NRT"
        )

    MOD00F_V61NRT_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_MOD00F_6.1NRT",
            provider="LANCEMODIS", 
            shortname="MOD00F",
            version="6.1NRT",
            description="MODIS/Terra L0 PDS Data 5-Min Swath - NRT version: 6.1NRT"
        )

    MODAODHD_V61NRT_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_MODAODHD_6.1NRT",
            provider="LANCEMODIS", 
            shortname="MODAODHD",
            version="6.1NRT",
            description="MODIS/Terra L3 Value-added Aerosol Optical Depth - NRT version: 6.1NRT"
        )

    MOD21_V61NRT_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_MOD21_6.1NRT",
            provider="LANCEMODIS", 
            shortname="MOD21",
            version="6.1NRT",
            description="MODIS/Terra Land Surface Temperature/3-Band Emissivity 5-Min L2 1km NRT version: 6.1NRT"
        )

    MOD11_L2_V61NRT_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_MOD11_L2_6.1NRT",
            provider="LANCEMODIS", 
            shortname="MOD11_L2",
            version="6.1NRT",
            description="MODIS/Terra Land Surface Temperature/Emissivity 5-Min L2 Swath 1km NRT version: 6.1NRT"
        )

    MOD02SSH_V61NRT_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_MOD02SSH_6.1NRT",
            provider="LANCEMODIS", 
            shortname="MOD02SSH",
            version="6.1NRT",
            description="MODIS/Terra Level 1B Subsampled Calibrated Radiance 5Km - NRT version: 6.1NRT"
        )

    MOD01_V61NRT_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_MOD01_6.1NRT",
            provider="LANCEMODIS", 
            shortname="MOD01",
            version="6.1NRT",
            description="MODIS/Terra Raw Radiances in Counts 5-Min L1A Swath - NRT version: 6.1NRT"
        )

    MOD29_V61NRT_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_MOD29_6.1NRT",
            provider="LANCEMODIS", 
            shortname="MOD29",
            version="6.1NRT",
            description="MODIS/Terra Sea Ice Extent 5-Min L2 Swath 1km NRT version: 6.1NRT"
        )

    MOD10_L2_V61NRT_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_MOD10_L2_6.1NRT",
            provider="LANCEMODIS", 
            shortname="MOD10_L2",
            version="6.1NRT",
            description="MODIS/Terra Snow Cover 5-Min L2 Swath 500m NRT version: 6.1NRT"
        )

    MOD09GA_V61NRT_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_MOD09GA_6.1NRT",
            provider="LANCEMODIS", 
            shortname="MOD09GA",
            version="6.1NRT",
            description="MODIS/Terra Surface Reflectance Daily L2G Global 1km and 500m SIN Grid NRT version: 6.1NRT"
        )

    MOD09GQ_V61NRT_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_MOD09GQ_6.1NRT",
            provider="LANCEMODIS", 
            shortname="MOD09GQ",
            version="6.1NRT",
            description="MODIS/Terra Surface Reflectance Daily L2G Global 250 m SIN Grid NRT version: 6.1NRT"
        )

    MOD09CMG_V61NRT_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_MOD09CMG_6.1NRT",
            provider="LANCEMODIS", 
            shortname="MOD09CMG",
            version="6.1NRT",
            description="MODIS/Terra Surface Reflectance Daily L3 Global 0.05Deg CMG NRT version: 6.1NRT"
        )

    MOD09Q1N_V61NRT_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_MOD09Q1N_6.1NRT",
            provider="LANCEMODIS", 
            shortname="MOD09Q1N",
            version="6.1NRT",
            description="MODIS/Terra Surface Reflectance Rolling-8-Day L3 Global 250m SIN Grid NRT version: 6.1NRT"
        )

    MOD09A1N_V61NRT_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_MOD09A1N_6.1NRT",
            provider="LANCEMODIS", 
            shortname="MOD09A1N",
            version="6.1NRT",
            description="MODIS/Terra Surface Reflectance Rolling-8-Day L3 Global 500m SIN Grid NRT version: 6.1NRT"
        )

    MOD07_L2_V61NRT_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_MOD07_L2_6.1NRT",
            provider="LANCEMODIS", 
            shortname="MOD07_L2",
            version="6.1NRT",
            description="MODIS/Terra Temperature and Water Vapor Profiles 5-Min L2 Swath 5km - NRT version: 6.1NRT"
        )

    MOD14_V61NRT_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_MOD14_6.1NRT",
            provider="LANCEMODIS", 
            shortname="MOD14",
            version="6.1NRT",
            description="MODIS/Terra Thermal Anomalies/Fire 5-Min L2 Swath 1km NRT version: 6.1NRT"
        )

    MOD05_L2_V61NRT_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_MOD05_L2_6.1NRT",
            provider="LANCEMODIS", 
            shortname="MOD05_L2",
            version="6.1NRT",
            description="MODIS/Terra Total Precipitable Water Vapor 5-Min L2 Swath 1km and 5km - NRT version: 6.1NRT"
        )

    MOD13Q4N_V61NRT_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_MOD13Q4N_6.1NRT",
            provider="LANCEMODIS", 
            shortname="MOD13Q4N",
            version="6.1NRT",
            description="MODIS/Terra Vegetation Indices Daily Rolling-8-Day L3 Global 250m SIN Grid NRT version: 6.1NRT"
        )

    MOD13A4N_V61NRT_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_MOD13A4N_6.1NRT",
            provider="LANCEMODIS", 
            shortname="MOD13A4N",
            version="6.1NRT",
            description="MODIS/Terra Vegetation Indices Daily Rolling-8-Day L3 Global 500m SIN Grid NRT version: 6.1NRT"
        )

    MCD43A3N_V61NRT_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_MCD43A3N_6.1NRT",
            provider="LANCEMODIS", 
            shortname="MCD43A3N",
            version="6.1NRT",
            description="MODIS/Terra+Aqua Albedo Daily L3 Global 500 m SIN Grid version: 6.1NRT"
        )

    MCD19A3DN_V61NRT_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_MCD19A3DN_6.1NRT",
            provider="LANCEMODIS", 
            shortname="MCD19A3DN",
            version="6.1NRT",
            description="MODIS/Terra+Aqua BRDF Model Parameters Daily NRT L3 Global 1km SIN Grid version: 6.1NRT"
        )

    MCD43A1N_V61NRT_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_MCD43A1N_6.1NRT",
            provider="LANCEMODIS", 
            shortname="MCD43A1N",
            version="6.1NRT",
            description="MODIS/Terra+Aqua BRDF/Albedo Model Parameters Daily L3 Global 500 m SIN Grid version: 6.1NRT"
        )

    MCD43A2N_V61NRT_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_MCD43A2N_6.1NRT",
            provider="LANCEMODIS", 
            shortname="MCD43A2N",
            version="6.1NRT",
            description="MODIS/Terra+Aqua BRDF/Albedo Quality Daily L3 Global 500 m SIN Grid version: 6.1NRT"
        )

    MCDAODHD_V61NRT_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_MCDAODHD_6.1NRT",
            provider="LANCEMODIS", 
            shortname="MCDAODHD",
            version="6.1NRT",
            description="MODIS/Terra+Aqua L3 Value-added Aerosol Optical Depth - NRT version: 6.1NRT"
        )

    MCD19A2N_V61NRT_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_MCD19A2N_6.1NRT",
            provider="LANCEMODIS", 
            shortname="MCD19A2N",
            version="6.1NRT",
            description="MODIS/Terra+Aqua Land Aerosol Optical Depth Daily L2G Global 1km SIN Grid NRT version: 6.1NRT"
        )

    MCD19A1N_V61NRT_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_MCD19A1N_6.1NRT",
            provider="LANCEMODIS", 
            shortname="MCD19A1N",
            version="6.1NRT",
            description="MODIS/Terra+Aqua Land Surface BRF Daily L2G Global 500m and 1km SIN Grid NRT version: 6.1NRT"
        )

    MCD43A4N_V61NRT_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_MCD43A4N_6.1NRT",
            provider="LANCEMODIS", 
            shortname="MCD43A4N",
            version="6.1NRT",
            description="MODIS/Terra+Aqua Nadir BRDF-Adjusted Reflectance Daily L3 Global 500 m SIN Grid version: 6.1NRT"
        )

    VNP09_NRT_V2_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_VNP09_NRT_2",
            provider="LANCEMODIS", 
            shortname="VNP09_NRT",
            version="2",
            description="NPP/VIIRS Atmospherically Corrected Surface Reflectance 6-Min L2 Swath 375m, 750m version: 2"
        )

    VNP02GDC_NRT_V2_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_VNP02GDC_NRT_2",
            provider="LANCEMODIS", 
            shortname="VNP02GDC_NRT",
            version="2",
            description="NPP/VIIRS Moderate-Resolution Dual Gain Bands Calibrated Radiance 6 Min L1B Swath 750m NRT version: 2"
        )

    VNP09GA_NRT_V2_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_VNP09GA_NRT_2",
            provider="LANCEMODIS", 
            shortname="VNP09GA_NRT",
            version="2",
            description="NPP/VIIRS Surface Reflectance Daily L2G Global 1km and 500m SIN Grid version: 2"
        )

    PM1ATTNR_NRT_V61NRT_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_PM1ATTNR_NRT_6.1NRT",
            provider="LANCEMODIS", 
            shortname="PM1ATTNR_NRT",
            version="6.1NRT",
            description="PM1 5-min Spacecraft attitude data from GBAD - NRT version: 6.1NRT"
        )

    VJ214IMGTDL_NRT_V1_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_VJ214IMGTDL_NRT_1",
            provider="LANCEMODIS", 
            shortname="VJ214IMGTDL_NRT",
            version="1",
            description="VIIRS (NOAA 21) I Band 375 m Active Fire Product NRT (Vector data) version: 1"
        )

    VJ114IMGTDL_NRT_V2_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_VJ114IMGTDL_NRT_2",
            provider="LANCEMODIS", 
            shortname="VJ114IMGTDL_NRT",
            version="2",
            description="VIIRS (NOAA-20/JPSS-1) I Band 375 m Active Fire Product NRT (Vector data) version: 2"
        )

    VNP14IMGTDL_NRT_V2_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_VNP14IMGTDL_NRT_2",
            provider="LANCEMODIS", 
            shortname="VNP14IMGTDL_NRT",
            version="2",
            description="VIIRS (S-NPP) I Band 375 m Active Fire Product NRT (Vector data) version: 2"
        )

    VJ114IMGT_NRT_V2_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_VJ114IMGT_NRT_2",
            provider="LANCEMODIS", 
            shortname="VJ114IMGT_NRT",
            version="2",
            description="VIIRS NOAA-20 (JPSS-1) 375m, I-Band Active Fire Product NRT (Vector Data) version: 2"
        )

    VJ114IMG_NRT_V2_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_VJ114IMG_NRT_2",
            provider="LANCEMODIS", 
            shortname="VJ114IMG_NRT",
            version="2",
            description="VIIRS/JPSS1 Active Fires 6-Min L2 Swath 375m NRT version: 2"
        )

    VJ143MA3N_V2_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_VJ143MA3N_2",
            provider="LANCEMODIS", 
            shortname="VJ143MA3N",
            version="2",
            description="VIIRS/JPSS1 Albedo Daily L3 Global 1km SIN Grid NRT version: 2"
        )

    VJ143IA3N_V2_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_VJ143IA3N_2",
            provider="LANCEMODIS", 
            shortname="VJ143IA3N",
            version="2",
            description="VIIRS/JPSS1 Albedo Daily L3 Global 500m SIN Grid NRT version: 2"
        )

    VJ109_NRT_V2_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_VJ109_NRT_2",
            provider="LANCEMODIS", 
            shortname="VJ109_NRT",
            version="2",
            description="VIIRS/JPSS1 Atmospherically Corrected Surface Reflectance 6-Min L2 Swath IP 375m, 750m NRT version: 2"
        )

    VJ143MA1N_V2_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_VJ143MA1N_2",
            provider="LANCEMODIS", 
            shortname="VJ143MA1N",
            version="2",
            description="VIIRS/JPSS1 BRDF/Albedo Model Parameters Daily L3 Global 1km SIN Grid NRT version: 2"
        )

    VJ143IA1N_V2_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_VJ143IA1N_2",
            provider="LANCEMODIS", 
            shortname="VJ143IA1N",
            version="2",
            description="VIIRS/JPSS1 BRDF/Albedo Model Parameters Daily L3 Global 500 m SIN Grid NRT version: 2"
        )

    VJ143MA2N_V2_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_VJ143MA2N_2",
            provider="LANCEMODIS", 
            shortname="VJ143MA2N",
            version="2",
            description="VIIRS/JPSS1 BRDF/Albedo Quality Daily L3 Global 1km SIN Grid NRT version: 2"
        )

    VJ143IA2N_V2_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_VJ143IA2N_2",
            provider="LANCEMODIS", 
            shortname="VJ143IA2N",
            version="2",
            description="VIIRS/JPSS1 BRDF/Albedo Quality Daily L3 Global 500 m SIN Grid NRT version: 2"
        )

    VJ146A1_NRT_V2_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_VJ146A1_NRT_2",
            provider="LANCEMODIS", 
            shortname="VJ146A1_NRT",
            version="2",
            description="VIIRS/JPSS1 Daily Gridded Day Night Band 500m Linear Lat Lon Grid Night NRT version: 2"
        )

    VJ102DNB_NRT_V21_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_VJ102DNB_NRT_2.1",
            provider="LANCEMODIS", 
            shortname="VJ102DNB_NRT",
            version="2.1",
            description="VIIRS/JPSS1 Day/Night Band 6 Min L1B Swath 750m NRT version: 2.1"
        )

    VJ102DNB_NRT_V2_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_VJ102DNB_NRT_2",
            provider="LANCEMODIS", 
            shortname="VJ102DNB_NRT",
            version="2",
            description="VIIRS/JPSS1 Day/Night Band 6-Min L1B Swath 750m NRT version: 2"
        )

    VJ103DNB_NRT_V21_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_VJ103DNB_NRT_2.1",
            provider="LANCEMODIS", 
            shortname="VJ103DNB_NRT",
            version="2.1",
            description="VIIRS/JPSS1 Day/Night Band Resolution Terrain Corrected Geolocation 6 Min L1 Swath 750m NRT version: 2.1"
        )

    VJ103DNB_NRT_V2_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_VJ103DNB_NRT_2",
            provider="LANCEMODIS", 
            shortname="VJ103DNB_NRT",
            version="2",
            description="VIIRS/JPSS1 Day/Night Band Resolution Terrain Corrected Geolocation 6-Min L1 Swath 750m NRT version: 2"
        )

    VJ146A1G_NRT_V2_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_VJ146A1G_NRT_2",
            provider="LANCEMODIS", 
            shortname="VJ146A1G_NRT",
            version="2",
            description="VIIRS/JPSS1 Granular Gridded Day Night Band 500m Linear Lat Lon Grid Night NRT version: 2"
        )

    VJ130_NRT_V2_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_VJ130_NRT_2",
            provider="LANCEMODIS", 
            shortname="VJ130_NRT",
            version="2",
            description="VIIRS/JPSS1 Ice Surface Temperature 6-Min L2 Swath 750m NRT version: 2"
        )

    VJ102IMG_NRT_V21_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_VJ102IMG_NRT_2.1",
            provider="LANCEMODIS", 
            shortname="VJ102IMG_NRT",
            version="2.1",
            description="VIIRS/JPSS1 Imagery Resolution 6 Min L1B Swath 375m NRT version: 2.1"
        )

    VJ102IMG_NRT_V2_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_VJ102IMG_NRT_2",
            provider="LANCEMODIS", 
            shortname="VJ102IMG_NRT",
            version="2",
            description="VIIRS/JPSS1 Imagery Resolution 6-Min L1B Swath 375m NRT version: 2"
        )

    VJ103IMG_NRT_V21_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_VJ103IMG_NRT_2.1",
            provider="LANCEMODIS", 
            shortname="VJ103IMG_NRT",
            version="2.1",
            description="VIIRS/JPSS1 Imagery Resolution Terrain Corrected Geolocation 6 Min L1 Swath 375m NRT version: 2.1"
        )

    VJ103IMG_NRT_V2_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_VJ103IMG_NRT_2",
            provider="LANCEMODIS", 
            shortname="VJ103IMG_NRT",
            version="2",
            description="VIIRS/JPSS1 Imagery Resolution Terrain Corrected Geolocation 6-Min L1 Swath 375m NRT version: 2"
        )

    VJ121IMG_NRT_V2_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_VJ121IMG_NRT_2",
            provider="LANCEMODIS", 
            shortname="VJ121IMG_NRT",
            version="2",
            description="VIIRS/JPSS1 Land Surface Temperature and Emissivity 6-Min L2 Swath 375m NRT version: 2"
        )

    VJ121_NRT_V2_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_VJ121_NRT_2",
            provider="LANCEMODIS", 
            shortname="VJ121_NRT",
            version="2",
            description="VIIRS/JPSS1 Land Surface Temperature and Emissivity 6-Min L2 Swath 750m version: 2"
        )

    VJ102MOD_NRT_V21_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_VJ102MOD_NRT_2.1",
            provider="LANCEMODIS", 
            shortname="VJ102MOD_NRT",
            version="2.1",
            description="VIIRS/JPSS1 Moderate Resolution 6 Min L1B Swath 750m NRT version: 2.1"
        )

    VJ102MOD_NRT_V2_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_VJ102MOD_NRT_2",
            provider="LANCEMODIS", 
            shortname="VJ102MOD_NRT",
            version="2",
            description="VIIRS/JPSS1 Moderate Resolution 6-Min L1B Swath 750m NRT version: 2"
        )

    VJ103MOD_NRT_V21_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_VJ103MOD_NRT_2.1",
            provider="LANCEMODIS", 
            shortname="VJ103MOD_NRT",
            version="2.1",
            description="VIIRS/JPSS1 Moderate Resolution Terrain Corrected Geolocation 6 Min L1 Swath 750m NRT version: 2.1"
        )

    VJ103MOD_NRT_V2_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_VJ103MOD_NRT_2",
            provider="LANCEMODIS", 
            shortname="VJ103MOD_NRT",
            version="2",
            description="VIIRS/JPSS1 Moderate Resolution Terrain Corrected Geolocation 6-Min L1 Swath 750m NRT version: 2"
        )

    VJ102GDC_NRT_V21_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_VJ102GDC_NRT_2.1",
            provider="LANCEMODIS", 
            shortname="VJ102GDC_NRT",
            version="2.1",
            description="VIIRS/JPSS1 Moderate-Resolution Dual Gain Bands Calibrated Radiance 6-Min L1B Swath 750 m NRT version: 2.1"
        )

    VJ102GDC_NRT_V2_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_VJ102GDC_NRT_2",
            provider="LANCEMODIS", 
            shortname="VJ102GDC_NRT",
            version="2",
            description="VIIRS/JPSS1 Moderate-Resolution Dual Gain Bands Calibrated Radiance 6-Min L1B Swath 750m -NRT version: 2"
        )

    VJ143MA4N_V2_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_VJ143MA4N_2",
            provider="LANCEMODIS", 
            shortname="VJ143MA4N",
            version="2",
            description="VIIRS/JPSS1 Nadir BRDF-Adjusted Reflectance Daily L3 Global 1 km SIN Grid NRT version: 2"
        )

    VJ143IA4N_V2_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_VJ143IA4N_2",
            provider="LANCEMODIS", 
            shortname="VJ143IA4N",
            version="2",
            description="VIIRS/JPSS1 Nadir BRDF-Adjusted Reflectance Daily L3 Global 500 m SIN Grid NRT version: 2"
        )

    VJ101_NRT_V21_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_VJ101_NRT_2.1",
            provider="LANCEMODIS", 
            shortname="VJ101_NRT",
            version="2.1",
            description="VIIRS/JPSS1 Raw Radiances in Counts 6 Min L1A Swath NRT version: 2.1"
        )

    VJ101_NRT_V2_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_VJ101_NRT_2",
            provider="LANCEMODIS", 
            shortname="VJ101_NRT",
            version="2",
            description="VIIRS/JPSS1 Raw Radiances in Counts 6-Min L1A Swath -NRT version: 2"
        )

    VJ129_NRT_V2_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_VJ129_NRT_2",
            provider="LANCEMODIS", 
            shortname="VJ129_NRT",
            version="2",
            description="VIIRS/JPSS1 Sea Ice Extent 6-Min L2 Swath 375m NRT version: 2"
        )

    VJ110_NRT_V2_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_VJ110_NRT_2",
            provider="LANCEMODIS", 
            shortname="VJ110_NRT",
            version="2",
            description="VIIRS/JPSS1 Snow Cover 6-Min L2 Swath 375m NRT version: 2"
        )

    VJ109GA_NRT_V2_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_VJ109GA_NRT_2",
            provider="LANCEMODIS", 
            shortname="VJ109GA_NRT",
            version="2",
            description="VIIRS/JPSS1 Surface Reflectance Daily L2G Global 1km and 500m SIN Grid NRT version: 2"
        )

    VJ109CMG_NRT_V2_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_VJ109CMG_NRT_2",
            provider="LANCEMODIS", 
            shortname="VJ109CMG_NRT",
            version="2",
            description="VIIRS/JPSS1 Surface Reflectance Daily L3 Global 0.05 Deg CMG NRT version: 2"
        )

    VJ114_NRT_V2_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_VJ114_NRT_2",
            provider="LANCEMODIS", 
            shortname="VJ114_NRT",
            version="2",
            description="VIIRS/JPSS1 Thermal Anomalies/Fire 6-Min L2 Swath 750m NRT - V2 version: 2"
        )

    VJ214IMG_NRT_V2_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_VJ214IMG_NRT_2",
            provider="LANCEMODIS", 
            shortname="VJ214IMG_NRT",
            version="2",
            description="VIIRS/JPSS2 Active Fires 6-Min L2 Swath 375m NRT version: 2"
        )

    VJ202DNB_NRT_V2_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_VJ202DNB_NRT_2",
            provider="LANCEMODIS", 
            shortname="VJ202DNB_NRT",
            version="2",
            description="VIIRS/JPSS2 Day/Night Band 6-Min L1B Swath 750m NRT version: 2"
        )

    VJ203DNB_NRT_V2_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_VJ203DNB_NRT_2",
            provider="LANCEMODIS", 
            shortname="VJ203DNB_NRT",
            version="2",
            description="VIIRS/JPSS2 Day/Night Band Resolution Terrain Corrected Geolocation 6-Min L1 Swath 750m NRT version: 2"
        )

    VJ202IMG_NRT_V2_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_VJ202IMG_NRT_2",
            provider="LANCEMODIS", 
            shortname="VJ202IMG_NRT",
            version="2",
            description="VIIRS/JPSS2 Imagery Resolution 6-Min L1B Swath 375m NRT version: 2"
        )

    VJ203IMG_NRT_V2_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_VJ203IMG_NRT_2",
            provider="LANCEMODIS", 
            shortname="VJ203IMG_NRT",
            version="2",
            description="VIIRS/JPSS2 Imagery Resolution Terrain Corrected Geolocation 6-Min L1 Swath 375m NRT version: 2"
        )

    VJ202MOD_NRT_V2_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_VJ202MOD_NRT_2",
            provider="LANCEMODIS", 
            shortname="VJ202MOD_NRT",
            version="2",
            description="VIIRS/JPSS2 Moderate Resolution 6-Min L1B Swath 750m NRT version: 2"
        )

    VJ203MOD_NRT_V2_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_VJ203MOD_NRT_2",
            provider="LANCEMODIS", 
            shortname="VJ203MOD_NRT",
            version="2",
            description="VIIRS/JPSS2 Moderate Resolution Terrain Corrected Geolocation 6-Min L1 Swath 750m NRT version: 2"
        )

    VJ202GDC_NRT_V2_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_VJ202GDC_NRT_2",
            provider="LANCEMODIS", 
            shortname="VJ202GDC_NRT",
            version="2",
            description="VIIRS/JPSS2 Moderate-Resolution Dual Gain Bands Calibrated Radiance 6-Min L1B Swath 750m NRT version: 2"
        )

    VJ201_NRT_V2_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_VJ201_NRT_2",
            provider="LANCEMODIS", 
            shortname="VJ201_NRT",
            version="2",
            description="VIIRS/JPSS2 Raw Radiances in Counts 6-Min L1A Swath NRT version: 2"
        )

    VJ214_NRT_V2_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_VJ214_NRT_2",
            provider="LANCEMODIS", 
            shortname="VJ214_NRT",
            version="2",
            description="VIIRS/JPSS2 Thermal Anomalies/Fire 6-Min L2 Swath 750m NRT - V2 version: 2"
        )

    VNP14IMG_NRT_V2_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_VNP14IMG_NRT_2",
            provider="LANCEMODIS", 
            shortname="VNP14IMG_NRT",
            version="2",
            description="VIIRS/NPP Active Fires 6-Min L2 Swath 375m - NRT version: 2"
        )

    VNP43MA3N_V2_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_VNP43MA3N_2",
            provider="LANCEMODIS", 
            shortname="VNP43MA3N",
            version="2",
            description="VIIRS/NPP Albedo Daily L3 Global 1km SIN Grid NRT version: 2"
        )

    VNP43IA3N_V2_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_VNP43IA3N_2",
            provider="LANCEMODIS", 
            shortname="VNP43IA3N",
            version="2",
            description="VIIRS/NPP Albedo Daily L3 Global 500m SIN Grid NRT version: 2"
        )

    VNP43MA1N_V2_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_VNP43MA1N_2",
            provider="LANCEMODIS", 
            shortname="VNP43MA1N",
            version="2",
            description="VIIRS/NPP BRDF/Albedo Model Parameters Daily L3 Global 1km SIN Grid NRT version: 2"
        )

    VNP43IA1N_V2_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_VNP43IA1N_2",
            provider="LANCEMODIS", 
            shortname="VNP43IA1N",
            version="2",
            description="VIIRS/NPP BRDF/Albedo Model Parameters Daily L3 Global 500m SIN Grid NRT version: 2"
        )

    VNP43MA2N_V2_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_VNP43MA2N_2",
            provider="LANCEMODIS", 
            shortname="VNP43MA2N",
            version="2",
            description="VIIRS/NPP BRDF/Albedo Quality Daily L3 Global 1km SIN Grid NRT version: 2"
        )

    VNP43IA2N_V2_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_VNP43IA2N_2",
            provider="LANCEMODIS", 
            shortname="VNP43IA2N",
            version="2",
            description="VIIRS/NPP BRDF/Albedo Quality Daily L3 Global 500m SIN Grid NRT version: 2"
        )

    VNP46A1_NRT_V2_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_VNP46A1_NRT_2",
            provider="LANCEMODIS", 
            shortname="VNP46A1_NRT",
            version="2",
            description="VIIRS/NPP Daily Gridded Day Night Band 500m Linear Lat. Lon. Grid Night NRT version: 2"
        )

    VNP02DNB_NRT_V2_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_VNP02DNB_NRT_2",
            provider="LANCEMODIS", 
            shortname="VNP02DNB_NRT",
            version="2",
            description="VIIRS/NPP Day/Night Band 6-Min L1B Swath 750m NRT version: 2"
        )

    VNP03DNB_NRT_V2_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_VNP03DNB_NRT_2",
            provider="LANCEMODIS", 
            shortname="VNP03DNB_NRT",
            version="2",
            description="VIIRS/NPP Day/Night Band Moderate Resolution Terrain-Corrected Geolocation 6-Min L1 Swath 750m NRT version: 2"
        )

    VNP46A1G_NRT_V2_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_VNP46A1G_NRT_2",
            provider="LANCEMODIS", 
            shortname="VNP46A1G_NRT",
            version="2",
            description="VIIRS/NPP Granular Gridded Day Night Band 500m Linear Lat. Lon. Grid Night NRT version: 2"
        )

    VNP30_NRT_V2_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_VNP30_NRT_2",
            provider="LANCEMODIS", 
            shortname="VNP30_NRT",
            version="2",
            description="VIIRS/NPP Ice Surface Temperature 6-Min L2 Swath 750 m NRT version: 2"
        )

    VNP02IMG_NRT_V2_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_VNP02IMG_NRT_2",
            provider="LANCEMODIS", 
            shortname="VNP02IMG_NRT",
            version="2",
            description="VIIRS/NPP Imagery Resolution 6-Min L1B Swath 375m NRT version: 2"
        )

    VNP03IMG_NRT_V2_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_VNP03IMG_NRT_2",
            provider="LANCEMODIS", 
            shortname="VNP03IMG_NRT",
            version="2",
            description="VIIRS/NPP Imagery Resolution Terrain-Corrected Geolocation 6-Min L1 Swath 375m NRT version: 2"
        )

    VNP21IMG_NRT_V2_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_VNP21IMG_NRT_2",
            provider="LANCEMODIS", 
            shortname="VNP21IMG_NRT",
            version="2",
            description="VIIRS/NPP Land Surface Temperature and Emissivity 6-Min L2 Swath 375m NRT version: 2"
        )

    VNP21_NRT_V2_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_VNP21_NRT_2",
            provider="LANCEMODIS", 
            shortname="VNP21_NRT",
            version="2",
            description="VIIRS/NPP Land Surface Temperature and Emissivity 6-Min L2 Swath 750 m version: 2"
        )

    VNP02MOD_NRT_V2_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_VNP02MOD_NRT_2",
            provider="LANCEMODIS", 
            shortname="VNP02MOD_NRT",
            version="2",
            description="VIIRS/NPP Moderate Resolution Bands L1B 6-Min Swath 750 m NRT version: 2"
        )

    VNP03MOD_NRT_V2_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_VNP03MOD_NRT_2",
            provider="LANCEMODIS", 
            shortname="VNP03MOD_NRT",
            version="2",
            description="VIIRS/NPP Moderate Resolution Terrain-Corrected Geolocation 6-Min L1 Swath 750m NRT version: 2"
        )

    VNP43MA4N_V2_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_VNP43MA4N_2",
            provider="LANCEMODIS", 
            shortname="VNP43MA4N",
            version="2",
            description="VIIRS/NPP Nadir BRDF-Adjusted Reflectance Daily L3 Global 1km SIN Grid NRT version: 2"
        )

    VNP43IA4N_V2_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_VNP43IA4N_2",
            provider="LANCEMODIS", 
            shortname="VNP43IA4N",
            version="2",
            description="VIIRS/NPP Nadir BRDF-Adjusted Reflectance Daily L3 Global 500m SIN Grid NRT version: 2"
        )

    VNP01_NRT_V2_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_VNP01_NRT_2",
            provider="LANCEMODIS", 
            shortname="VNP01_NRT",
            version="2",
            description="VIIRS/NPP Raw Radiances in Counts 6-Min L1A Swath NRT version: 2"
        )

    VNP29_NRT_V2_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_VNP29_NRT_2",
            provider="LANCEMODIS", 
            shortname="VNP29_NRT",
            version="2",
            description="VIIRS/NPP Sea Ice Extent 6-Min L2 Swath 375m NRT version: 2"
        )

    VNP10_NRT_V2_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_VNP10_NRT_2",
            provider="LANCEMODIS", 
            shortname="VNP10_NRT",
            version="2",
            description="VIIRS/NPP Snow Cover 6-Min L2 Swath 375m NRT version: 2"
        )

    VNP09CMG_NRT_V2_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_VNP09CMG_NRT_2",
            provider="LANCEMODIS", 
            shortname="VNP09CMG_NRT",
            version="2",
            description="VIIRS/NPP Surface Reflectance Daily L3 Global 0.05 Deg CMG NRT version: 2"
        )

    VNP14_NRT_V2_LANCEMODIS = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEMODIS_VNP14_NRT_2",
            provider="LANCEMODIS", 
            shortname="VNP14_NRT",
            version="2",
            description="VIIRS/NPP Thermal Anomalies/Fire 6-Min L2 Swath 750m NRT - V2 version: 2"
        )

