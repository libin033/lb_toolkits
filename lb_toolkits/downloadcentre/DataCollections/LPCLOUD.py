from lb_toolkits.downloadcentre.DataCollections.DataCollectionDefinition import DataCollectionDefinition 

class DataCollectionLPCLOUD : 
    LPCLOUD_ASTGTM_NUMNC_V30 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_ASTGTM_NUMNC_3.0",
            provider="LPCLOUD", 
            shortname="ASTGTM_NUMNC",
            version="3.0",
            description="ASTER Global Digital Elevation Model Attributes NetCDF V003 version: 3.0"
        )

    LPCLOUD_ASTGTM_NC_V30 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_ASTGTM_NC_3.0",
            provider="LPCLOUD", 
            shortname="ASTGTM_NC",
            version="3.0",
            description="ASTER Global Digital Elevation Model NetCDF V003 version: 3.0"
        )

    LPCLOUD_ASTGTM_V30 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_ASTGTM_3.0",
            provider="LPCLOUD", 
            shortname="ASTGTM",
            version="3.0",
            description="ASTER Global Digital Elevation Model V003 version: 3.0"
        )

    LPCLOUD_WaterBalance_Daily_Historical_GRIDMET_V15 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_WaterBalance_Daily_Historical_GRIDMET_1.5",
            provider="LPCLOUD", 
            shortname="WaterBalance_Daily_Historical_GRIDMET",
            version="1.5",
            description="Daily Historical Water Balance Products for the CONUS version: 1.5"
        )

    LPCLOUD_ECO_L2G_CLOUD_V20 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_ECO_L2G_CLOUD_2.0",
            provider="LPCLOUD", 
            shortname="ECO_L2G_CLOUD",
            version="2.0",
            description="ECOSTRESS Gridded Cloud Mask Instantaneous L2 Global 70 m V002 version: 2.0"
        )

    LPCLOUD_ECO_L3G_MET_V20 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_ECO_L3G_MET_2.0",
            provider="LPCLOUD", 
            shortname="ECO_L3G_MET",
            version="2.0",
            description="ECOSTRESS Gridded Downscaled Meteorology Instantaneous L3 Global 70 m V002 version: 2.0"
        )

    LPCLOUD_ECO_L3G_SM_V20 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_ECO_L3G_SM_2.0",
            provider="LPCLOUD", 
            shortname="ECO_L3G_SM",
            version="2.0",
            description="ECOSTRESS Gridded Downscaled Soil Moisture Instantaneous L3 Global 70 m V002 version: 2.0"
        )

    LPCLOUD_ECO_L4G_ESI_V20 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_ECO_L4G_ESI_2.0",
            provider="LPCLOUD", 
            shortname="ECO_L4G_ESI",
            version="2.0",
            description="ECOSTRESS Gridded Evaporative Stress Index PT-JPL Instantaneous L4 Global 70 m version: 2.0"
        )

    LPCLOUD_ECO_L3G_JET_V20 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_ECO_L3G_JET_2.0",
            provider="LPCLOUD", 
            shortname="ECO_L3G_JET",
            version="2.0",
            description="ECOSTRESS Gridded Evapotranspiration Instantaneous and Daytime L3 Global 70 m V002 version: 2.0"
        )

    LPCLOUD_ECO_L2G_LSTE_V20 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_ECO_L2G_LSTE_2.0",
            provider="LPCLOUD", 
            shortname="ECO_L2G_LSTE",
            version="2.0",
            description="ECOSTRESS Gridded Land Surface Temperature and Emissivity Instantaneous L2 Global 70 m V002 version: 2.0"
        )

    LPCLOUD_ECO_L3G_SEB_V20 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_ECO_L3G_SEB_2.0",
            provider="LPCLOUD", 
            shortname="ECO_L3G_SEB",
            version="2.0",
            description="ECOSTRESS Gridded Surface Energy Balance Instantaneous L3 Global 70 m V002 version: 2.0"
        )

    LPCLOUD_ECO_L1CG_RAD_V20 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_ECO_L1CG_RAD_2.0",
            provider="LPCLOUD", 
            shortname="ECO_L1CG_RAD",
            version="2.0",
            description="ECOSTRESS Gridded Top of Atmosphere Calibrated Radiance Instantaneous L1C Global 70 m V002 version: 2.0"
        )

    LPCLOUD_ECO_L4G_WUE_V20 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_ECO_L4G_WUE_2.0",
            provider="LPCLOUD", 
            shortname="ECO_L4G_WUE",
            version="2.0",
            description="ECOSTRESS Gridded Water Use Efficiency Instantaneous L4 Global 70 m V002 version: 2.0"
        )

    LPCLOUD_ECO_L1B_ATT_V20 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_ECO_L1B_ATT_2.0",
            provider="LPCLOUD", 
            shortname="ECO_L1B_ATT",
            version="2.0",
            description="ECOSTRESS Swath Attitude and Ephemeris Instantaneous L1B Global V002 version: 2.0"
        )

    LPCLOUD_ECO_L2_CLOUD_V20 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_ECO_L2_CLOUD_2.0",
            provider="LPCLOUD", 
            shortname="ECO_L2_CLOUD",
            version="2.0",
            description="ECOSTRESS Swath Cloud Mask Instantaneous L2 Global 70 m V002 version: 2.0"
        )

    LPCLOUD_ECO_L1B_GEO_V20 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_ECO_L1B_GEO_2.0",
            provider="LPCLOUD", 
            shortname="ECO_L1B_GEO",
            version="2.0",
            description="ECOSTRESS Swath Geolocation Instantaneous L1B Global 70 m V002 version: 2.0"
        )

    LPCLOUD_ECO_L2_LSTE_V20 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_ECO_L2_LSTE_2.0",
            provider="LPCLOUD", 
            shortname="ECO_L2_LSTE",
            version="2.0",
            description="ECOSTRESS Swath Land Surface Temperature and Emissivity Instantaneous L2 Global 70 m V002 version: 2.0"
        )

    LPCLOUD_ECO_L1B_RAD_V20 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_ECO_L1B_RAD_2.0",
            provider="LPCLOUD", 
            shortname="ECO_L1B_RAD",
            version="2.0",
            description="ECOSTRESS Swath Top of Atmosphere Calibrated Radiance Instantaneous L1B Global 70 m V002 version: 2.0"
        )

    LPCLOUD_ECO_L2T_STARS_V20 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_ECO_L2T_STARS_2.0",
            provider="LPCLOUD", 
            shortname="ECO_L2T_STARS",
            version="2.0",
            description="ECOSTRESS Tiled Ancillary NDVI and Albedo L2 Global 70 m V002 version: 2.0"
        )

    LPCLOUD_ECO_L3T_MET_V20 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_ECO_L3T_MET_2.0",
            provider="LPCLOUD", 
            shortname="ECO_L3T_MET",
            version="2.0",
            description="ECOSTRESS Tiled Downscaled Meteorology Instantaneous L3 Global 70 m V002 version: 2.0"
        )

    LPCLOUD_ECO_L3T_SM_V20 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_ECO_L3T_SM_2.0",
            provider="LPCLOUD", 
            shortname="ECO_L3T_SM",
            version="2.0",
            description="ECOSTRESS Tiled Downscaled Soil Moisture Instantaneous L3 Global 70 m V002 version: 2.0"
        )

    LPCLOUD_ECO_L4T_ESI_V20 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_ECO_L4T_ESI_2.0",
            provider="LPCLOUD", 
            shortname="ECO_L4T_ESI",
            version="2.0",
            description="ECOSTRESS Tiled Evaporative Stress Index PT-JPL Instantaneous L4 Global 70 m V002 version: 2.0"
        )

    LPCLOUD_ECO_L3T_JET_V20 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_ECO_L3T_JET_2.0",
            provider="LPCLOUD", 
            shortname="ECO_L3T_JET",
            version="2.0",
            description="ECOSTRESS Tiled Evapotranspiration Instantaneous and Daytime L3 Global 70 m V002 version: 2.0"
        )

    LPCLOUD_ECO_L2T_LSTE_V20 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_ECO_L2T_LSTE_2.0",
            provider="LPCLOUD", 
            shortname="ECO_L2T_LSTE",
            version="2.0",
            description="ECOSTRESS Tiled Land Surface Temperature and Emissivity Instantaneous L2 Global 70 m V002 version: 2.0"
        )

    LPCLOUD_ECO_L3T_SEB_V20 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_ECO_L3T_SEB_2.0",
            provider="LPCLOUD", 
            shortname="ECO_L3T_SEB",
            version="2.0",
            description="ECOSTRESS Tiled Surface Energy Balance Instantaneous L3 Global 70 m V002 version: 2.0"
        )

    LPCLOUD_ECO_L1CT_RAD_V20 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_ECO_L1CT_RAD_2.0",
            provider="LPCLOUD", 
            shortname="ECO_L1CT_RAD",
            version="2.0",
            description="ECOSTRESS Tiled Top of Atmosphere Calibrated Radiance Instantaneous L1C Global 70 m V002 version: 2.0"
        )

    LPCLOUD_ECO_L4T_WUE_V20 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_ECO_L4T_WUE_2.0",
            provider="LPCLOUD", 
            shortname="ECO_L4T_WUE",
            version="2.0",
            description="ECOSTRESS Tiled Water Use Efficiency Instantaneous L4 Global 70 m version: 2.0"
        )

    LPCLOUD_EMITL1BRAD_V10 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_EMITL1BRAD_1.0",
            provider="LPCLOUD", 
            shortname="EMITL1BRAD",
            version="1.0",
            description="EMIT L1B At-Sensor Calibrated Radiance and Geolocation Data 60 m V001 version: 1.0"
        )

    LPCLOUD_EMITL1BATT_V10 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_EMITL1BATT_1.0",
            provider="LPCLOUD", 
            shortname="EMITL1BATT",
            version="1.0",
            description="EMIT L1B Corrected Spacecraft Attitude and Ephemeris V001 version: 1.0"
        )

    LPCLOUD_EMITL2ARFL_V10 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_EMITL2ARFL_1.0",
            provider="LPCLOUD", 
            shortname="EMITL2ARFL",
            version="1.0",
            description="EMIT L2A Estimated Surface Reflectance and Uncertainty and Masks 60 m V001 version: 1.0"
        )

    LPCLOUD_EMITL2BMIN_V10 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_EMITL2BMIN_1.0",
            provider="LPCLOUD", 
            shortname="EMITL2BMIN",
            version="1.0",
            description="EMIT L2B Estimated Mineral Identification and Band Depth and Uncertainty 60 m V001 version: 1.0"
        )

    LPCLOUD_EMITL3ASA_V10 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_EMITL3ASA_1.0",
            provider="LPCLOUD", 
            shortname="EMITL3ASA",
            version="1.0",
            description="EMIT L3 Aggregated Mineral Spectral Abundance and Uncertainty 0.5 Deg V001 version: 1.0"
        )

    LPCLOUD_EMITL4ESM_V10 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_EMITL4ESM_1.0",
            provider="LPCLOUD", 
            shortname="EMITL4ESM",
            version="1.0",
            description="EMIT L4 Earth System Model Products V001 version: 1.0"
        )

    LPCLOUD_GEDI01_B_V20 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_GEDI01_B_2.0",
            provider="LPCLOUD", 
            shortname="GEDI01_B",
            version="2.0",
            description="GEDI L1B Geolocated Waveform Data Global Footprint Level V002 version: 2.0"
        )

    LPCLOUD_GEDI02_A_V20 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_GEDI02_A_2.0",
            provider="LPCLOUD", 
            shortname="GEDI02_A",
            version="2.0",
            description="GEDI L2A Elevation and Height Metrics Data Global Footprint Level V002 version: 2.0"
        )

    LPCLOUD_GEDI02_B_V20 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_GEDI02_B_2.0",
            provider="LPCLOUD", 
            shortname="GEDI02_B",
            version="2.0",
            description="GEDI L2B Canopy Cover and Vertical Profile Metrics Data Global Footprint Level V002 version: 2.0"
        )

    LPCLOUD_HLSL30_V20 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_HLSL30_2.0",
            provider="LPCLOUD", 
            shortname="HLSL30",
            version="2.0",
            description="HLS Landsat Operational Land Imager Surface Reflectance and TOA Brightness Daily Global 30m v2.0 version: 2.0"
        )

    LPCLOUD_HLSS30_V20 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_HLSS30_2.0",
            provider="LPCLOUD", 
            shortname="HLSS30",
            version="2.0",
            description="HLS Sentinel-2 Multi-spectral Instrument Surface Reflectance Daily Global 30m v2.0 version: 2.0"
        )

    LPCLOUD_MYD17A2H_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MYD17A2H_61.0",
            provider="LPCLOUD", 
            shortname="MYD17A2H",
            version="61.0",
            description="MODIS/Aqua Gross Primary Productivity 8-Day L4 Global 500m SIN Grid V061 version: 61.0"
        )

    LPCLOUD_MYD17A2HGF_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MYD17A2HGF_61.0",
            provider="LPCLOUD", 
            shortname="MYD17A2HGF",
            version="61.0",
            description="MODIS/Aqua Gross Primary Productivity Gap-Filled 8-Day L4 Global 500m SIN Grid V061 version: 61.0"
        )

    LPCLOUD_MYD21_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MYD21_61.0",
            provider="LPCLOUD", 
            shortname="MYD21",
            version="61.0",
            description="MODIS/Aqua Land Surface Temperature/3-Band Emissivity 5-Min L2 1km V061 version: 61.0"
        )

    LPCLOUD_MYD21C2_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MYD21C2_61.0",
            provider="LPCLOUD", 
            shortname="MYD21C2",
            version="61.0",
            description="MODIS/Aqua Land Surface Temperature/3-Band Emissivity 8-Day L3 Global 0.05Deg CMG V061 version: 61.0"
        )

    LPCLOUD_MYD21A2_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MYD21A2_61.0",
            provider="LPCLOUD", 
            shortname="MYD21A2",
            version="61.0",
            description="MODIS/Aqua Land Surface Temperature/3-Band Emissivity 8-Day L3 Global 1km SIN Grid V061 version: 61.0"
        )

    LPCLOUD_MYD21C1_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MYD21C1_61.0",
            provider="LPCLOUD", 
            shortname="MYD21C1",
            version="61.0",
            description="MODIS/Aqua Land Surface Temperature/3-Band Emissivity Daily L3 Global 0.05Deg CMG V061 version: 61.0"
        )

    LPCLOUD_MYD21A1D_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MYD21A1D_61.0",
            provider="LPCLOUD", 
            shortname="MYD21A1D",
            version="61.0",
            description="MODIS/Aqua Land Surface Temperature/3-Band Emissivity Daily L3 Global 1km SIN Grid Day V061 version: 61.0"
        )

    LPCLOUD_MYD21A1N_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MYD21A1N_61.0",
            provider="LPCLOUD", 
            shortname="MYD21A1N",
            version="61.0",
            description="MODIS/Aqua Land Surface Temperature/3-Band Emissivity Daily L3 Global 1km SIN Grid Night V061 version: 61.0"
        )

    LPCLOUD_MYD21C3_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MYD21C3_61.0",
            provider="LPCLOUD", 
            shortname="MYD21C3",
            version="61.0",
            description="MODIS/Aqua Land Surface Temperature/3-Band Emissivity Monthly L3 Global 0.05Deg CMG V061 version: 61.0"
        )

    LPCLOUD_MYD11_L2_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MYD11_L2_61.0",
            provider="LPCLOUD", 
            shortname="MYD11_L2",
            version="61.0",
            description="MODIS/Aqua Land Surface Temperature/Emissivity 5-Min L2 Swath 1km V061 version: 61.0"
        )

    LPCLOUD_MYD11C2_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MYD11C2_61.0",
            provider="LPCLOUD", 
            shortname="MYD11C2",
            version="61.0",
            description="MODIS/Aqua Land Surface Temperature/Emissivity 8-Day L3 Global 0.05Deg CMG V061 version: 61.0"
        )

    LPCLOUD_MYD11A2_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MYD11A2_61.0",
            provider="LPCLOUD", 
            shortname="MYD11A2",
            version="61.0",
            description="MODIS/Aqua Land Surface Temperature/Emissivity 8-Day L3 Global 1km SIN Grid V061 version: 61.0"
        )

    LPCLOUD_MYD11B2_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MYD11B2_61.0",
            provider="LPCLOUD", 
            shortname="MYD11B2",
            version="61.0",
            description="MODIS/Aqua Land Surface Temperature/Emissivity 8-Day L3 Global 6km SIN Grid V061 version: 61.0"
        )

    LPCLOUD_MYD11C1_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MYD11C1_61.0",
            provider="LPCLOUD", 
            shortname="MYD11C1",
            version="61.0",
            description="MODIS/Aqua Land Surface Temperature/Emissivity Daily L3 Global 0.05Deg CMG V061 version: 61.0"
        )

    LPCLOUD_MYD11A1_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MYD11A1_61.0",
            provider="LPCLOUD", 
            shortname="MYD11A1",
            version="61.0",
            description="MODIS/Aqua Land Surface Temperature/Emissivity Daily L3 Global 1km SIN Grid V061 version: 61.0"
        )

    LPCLOUD_MYD11B1_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MYD11B1_61.0",
            provider="LPCLOUD", 
            shortname="MYD11B1",
            version="61.0",
            description="MODIS/Aqua Land Surface Temperature/Emissivity Daily L3 Global 6km SIN Grid V061 version: 61.0"
        )

    LPCLOUD_MYD11C3_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MYD11C3_61.0",
            provider="LPCLOUD", 
            shortname="MYD11C3",
            version="61.0",
            description="MODIS/Aqua Land Surface Temperature/Emissivity Monthly L3 Global 0.05Deg CMG V061 version: 61.0"
        )

    LPCLOUD_MYD11B3_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MYD11B3_61.0",
            provider="LPCLOUD", 
            shortname="MYD11B3",
            version="61.0",
            description="MODIS/Aqua Land Surface Temperature/Emissivity Monthly L3 Global 6km SIN Grid V061 version: 61.0"
        )

    LPCLOUD_MYD15A2H_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MYD15A2H_61.0",
            provider="LPCLOUD", 
            shortname="MYD15A2H",
            version="61.0",
            description="MODIS/Aqua Leaf Area Index/FPAR 8-Day L4 Global 500m SIN Grid V061 version: 61.0"
        )

    LPCLOUD_MYD16A2_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MYD16A2_61.0",
            provider="LPCLOUD", 
            shortname="MYD16A2",
            version="61.0",
            description="MODIS/Aqua Net Evapotranspiration 8-Day L4 Global 500m SIN Grid V061 version: 61.0"
        )

    LPCLOUD_MYD16A2GF_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MYD16A2GF_61.0",
            provider="LPCLOUD", 
            shortname="MYD16A2GF",
            version="61.0",
            description="MODIS/Aqua Net Evapotranspiration Gap-Filled 8-Day L4 Global 500m SIN Grid V061 version: 61.0"
        )

    LPCLOUD_MYD16A3GF_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MYD16A3GF_61.0",
            provider="LPCLOUD", 
            shortname="MYD16A3GF",
            version="61.0",
            description="MODIS/Aqua Net Evapotranspiration Gap-Filled Yearly L4 Global 500m SIN Grid V061 version: 61.0"
        )

    LPCLOUD_MYD17A3HGF_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MYD17A3HGF_61.0",
            provider="LPCLOUD", 
            shortname="MYD17A3HGF",
            version="61.0",
            description="MODIS/Aqua Net Primary Production Gap-Filled Yearly L4 Global 500m SIN Grid V061 version: 61.0"
        )

    LPCLOUD_MYD09Q1_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MYD09Q1_61.0",
            provider="LPCLOUD", 
            shortname="MYD09Q1",
            version="61.0",
            description="MODIS/Aqua Surface Reflectance 8-Day L3 Global 250m SIN Grid V061 version: 61.0"
        )

    LPCLOUD_MYD09A1_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MYD09A1_61.0",
            provider="LPCLOUD", 
            shortname="MYD09A1",
            version="61.0",
            description="MODIS/Aqua Surface Reflectance 8-Day L3 Global 500m SIN Grid V061 version: 61.0"
        )

    LPCLOUD_MYD09GA_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MYD09GA_61.0",
            provider="LPCLOUD", 
            shortname="MYD09GA",
            version="61.0",
            description="MODIS/Aqua Surface Reflectance Daily L2G Global 1km and 500m SIN Grid V061 version: 61.0"
        )

    LPCLOUD_MYD09GQ_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MYD09GQ_61.0",
            provider="LPCLOUD", 
            shortname="MYD09GQ",
            version="61.0",
            description="MODIS/Aqua Surface Reflectance Daily L2G Global 250m SIN Grid V061 version: 61.0"
        )

    LPCLOUD_MYD09CMG_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MYD09CMG_61.0",
            provider="LPCLOUD", 
            shortname="MYD09CMG",
            version="61.0",
            description="MODIS/Aqua Surface Reflectance Daily L3 Global 0.05Deg CMG V061 version: 61.0"
        )

    LPCLOUD_MYD14_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MYD14_61.0",
            provider="LPCLOUD", 
            shortname="MYD14",
            version="61.0",
            description="MODIS/Aqua Thermal Anomalies/Fire 5-Min L2 Swath 1km V061 version: 61.0"
        )

    LPCLOUD_MYD14A2_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MYD14A2_61.0",
            provider="LPCLOUD", 
            shortname="MYD14A2",
            version="61.0",
            description="MODIS/Aqua Thermal Anomalies/Fire 8-Day L3 Global 1km SIN Grid V061 version: 61.0"
        )

    LPCLOUD_MYD14A1_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MYD14A1_61.0",
            provider="LPCLOUD", 
            shortname="MYD14A1",
            version="61.0",
            description="MODIS/Aqua Thermal Anomalies/Fire Daily L3 Global 1km SIN Grid V061 version: 61.0"
        )

    LPCLOUD_MYD13C1_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MYD13C1_61.0",
            provider="LPCLOUD", 
            shortname="MYD13C1",
            version="61.0",
            description="MODIS/Aqua Vegetation Indices 16-Day L3 Global 0.05Deg CMG V061 version: 61.0"
        )

    LPCLOUD_MYD13A2_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MYD13A2_61.0",
            provider="LPCLOUD", 
            shortname="MYD13A2",
            version="61.0",
            description="MODIS/Aqua Vegetation Indices 16-Day L3 Global 1km SIN Grid V061 version: 61.0"
        )

    LPCLOUD_MYD13Q1_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MYD13Q1_61.0",
            provider="LPCLOUD", 
            shortname="MYD13Q1",
            version="61.0",
            description="MODIS/Aqua Vegetation Indices 16-Day L3 Global 250m SIN Grid V061 version: 61.0"
        )

    LPCLOUD_MYD13A1_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MYD13A1_61.0",
            provider="LPCLOUD", 
            shortname="MYD13A1",
            version="61.0",
            description="MODIS/Aqua Vegetation Indices 16-Day L3 Global 500m SIN Grid V061 version: 61.0"
        )

    LPCLOUD_MYD13C2_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MYD13C2_61.0",
            provider="LPCLOUD", 
            shortname="MYD13C2",
            version="61.0",
            description="MODIS/Aqua Vegetation Indices Monthly L3 Global 0.05Deg CMG V061 version: 61.0"
        )

    LPCLOUD_MYD13A3_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MYD13A3_61.0",
            provider="LPCLOUD", 
            shortname="MYD13A3",
            version="61.0",
            description="MODIS/Aqua Vegetation Indices Monthly L3 Global 1km SIN Grid V061 version: 61.0"
        )

    LPCLOUD_MYD28C2_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MYD28C2_61.0",
            provider="LPCLOUD", 
            shortname="MYD28C2",
            version="61.0",
            description="MODIS/Aqua Water Reservoir 8-Day L3 Global V061 version: 61.0"
        )

    LPCLOUD_MYD28C3_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MYD28C3_61.0",
            provider="LPCLOUD", 
            shortname="MYD28C3",
            version="61.0",
            description="MODIS/Aqua Water Reservoir Monthly L3 Global V061 version: 61.0"
        )

    LPCLOUD_MOD17A2H_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MOD17A2H_61.0",
            provider="LPCLOUD", 
            shortname="MOD17A2H",
            version="61.0",
            description="MODIS/Terra Gross Primary Productivity 8-Day L4 Global 500m SIN Grid V061 version: 61.0"
        )

    LPCLOUD_MOD17A2HGF_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MOD17A2HGF_61.0",
            provider="LPCLOUD", 
            shortname="MOD17A2HGF",
            version="61.0",
            description="MODIS/Terra Gross Primary Productivity Gap-Filled 8-Day L4 Global 500m SIN Grid V061 version: 61.0"
        )

    LPCLOUD_MOD21_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MOD21_61.0",
            provider="LPCLOUD", 
            shortname="MOD21",
            version="61.0",
            description="MODIS/Terra Land Surface Temperature/3-Band Emissivity 5-Min L2 1km V061 version: 61.0"
        )

    LPCLOUD_MOD21C2_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MOD21C2_61.0",
            provider="LPCLOUD", 
            shortname="MOD21C2",
            version="61.0",
            description="MODIS/Terra Land Surface Temperature/3-Band Emissivity 8-Day L3 Global 0.05Deg CMG V061 version: 61.0"
        )

    LPCLOUD_MOD21A2_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MOD21A2_61.0",
            provider="LPCLOUD", 
            shortname="MOD21A2",
            version="61.0",
            description="MODIS/Terra Land Surface Temperature/3-Band Emissivity 8-Day L3 Global 1km SIN Grid V061 version: 61.0"
        )

    LPCLOUD_MOD21C1_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MOD21C1_61.0",
            provider="LPCLOUD", 
            shortname="MOD21C1",
            version="61.0",
            description="MODIS/Terra Land Surface Temperature/3-Band Emissivity Daily L3 Global 0.05Deg CMG V061 version: 61.0"
        )

    LPCLOUD_MOD21A1D_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MOD21A1D_61.0",
            provider="LPCLOUD", 
            shortname="MOD21A1D",
            version="61.0",
            description="MODIS/Terra Land Surface Temperature/3-Band Emissivity Daily L3 Global 1km SIN Grid Day V061 version: 61.0"
        )

    LPCLOUD_MOD21A1N_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MOD21A1N_61.0",
            provider="LPCLOUD", 
            shortname="MOD21A1N",
            version="61.0",
            description="MODIS/Terra Land Surface Temperature/3-Band Emissivity Daily L3 Global 1km SIN Grid Night V061 version: 61.0"
        )

    LPCLOUD_MOD21C3_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MOD21C3_61.0",
            provider="LPCLOUD", 
            shortname="MOD21C3",
            version="61.0",
            description="MODIS/Terra Land Surface Temperature/3-Band Emissivity Monthly L3 Global 0.05Deg CMG V061 version: 61.0"
        )

    LPCLOUD_MOD11_L2_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MOD11_L2_61.0",
            provider="LPCLOUD", 
            shortname="MOD11_L2",
            version="61.0",
            description="MODIS/Terra Land Surface Temperature/Emissivity 5-Min L2 Swath 1km V061 version: 61.0"
        )

    LPCLOUD_MOD11C2_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MOD11C2_61.0",
            provider="LPCLOUD", 
            shortname="MOD11C2",
            version="61.0",
            description="MODIS/Terra Land Surface Temperature/Emissivity 8-Day L3 Global 0.05Deg CMG V061 version: 61.0"
        )

    LPCLOUD_MOD11A2_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MOD11A2_61.0",
            provider="LPCLOUD", 
            shortname="MOD11A2",
            version="61.0",
            description="MODIS/Terra Land Surface Temperature/Emissivity 8-Day L3 Global 1km SIN Grid V061 version: 61.0"
        )

    LPCLOUD_MOD11B2_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MOD11B2_61.0",
            provider="LPCLOUD", 
            shortname="MOD11B2",
            version="61.0",
            description="MODIS/Terra Land Surface Temperature/Emissivity 8-Day L3 Global 6km SIN Grid V061 version: 61.0"
        )

    LPCLOUD_MOD11C1_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MOD11C1_61.0",
            provider="LPCLOUD", 
            shortname="MOD11C1",
            version="61.0",
            description="MODIS/Terra Land Surface Temperature/Emissivity Daily L3 Global 0.05Deg CMG V061 version: 61.0"
        )

    LPCLOUD_MOD11A1_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MOD11A1_61.0",
            provider="LPCLOUD", 
            shortname="MOD11A1",
            version="61.0",
            description="MODIS/Terra Land Surface Temperature/Emissivity Daily L3 Global 1km SIN Grid V061 version: 61.0"
        )

    LPCLOUD_MOD11B1_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MOD11B1_61.0",
            provider="LPCLOUD", 
            shortname="MOD11B1",
            version="61.0",
            description="MODIS/Terra Land Surface Temperature/Emissivity Daily L3 Global 6km SIN Grid V061 version: 61.0"
        )

    LPCLOUD_MOD11C3_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MOD11C3_61.0",
            provider="LPCLOUD", 
            shortname="MOD11C3",
            version="61.0",
            description="MODIS/Terra Land Surface Temperature/Emissivity Monthly L3 Global 0.05Deg CMG V061 version: 61.0"
        )

    LPCLOUD_MOD11B3_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MOD11B3_61.0",
            provider="LPCLOUD", 
            shortname="MOD11B3",
            version="61.0",
            description="MODIS/Terra Land Surface Temperature/Emissivity Monthly L3 Global 6km SIN Grid V061 version: 61.0"
        )

    LPCLOUD_MOD44W_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MOD44W_61.0",
            provider="LPCLOUD", 
            shortname="MOD44W",
            version="61.0",
            description="MODIS/Terra Land Water Mask Derived from MODIS and SRTM L3 Global 250m SIN Grid V061 version: 61.0"
        )

    LPCLOUD_MOD15A2H_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MOD15A2H_61.0",
            provider="LPCLOUD", 
            shortname="MOD15A2H",
            version="61.0",
            description="MODIS/Terra Leaf Area Index/FPAR 8-Day L4 Global 500m SIN Grid V061 version: 61.0"
        )

    LPCLOUD_MOD16A2_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MOD16A2_61.0",
            provider="LPCLOUD", 
            shortname="MOD16A2",
            version="61.0",
            description="MODIS/Terra Net Evapotranspiration 8-Day L4 Global 500m SIN Grid V061 version: 61.0"
        )

    LPCLOUD_MOD16A2GF_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MOD16A2GF_61.0",
            provider="LPCLOUD", 
            shortname="MOD16A2GF",
            version="61.0",
            description="MODIS/Terra Net Evapotranspiration Gap-Filled 8-Day L4 Global 500m SIN Grid V061 version: 61.0"
        )

    LPCLOUD_MOD16A3GF_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MOD16A3GF_61.0",
            provider="LPCLOUD", 
            shortname="MOD16A3GF",
            version="61.0",
            description="MODIS/Terra Net Evapotranspiration Gap-Filled Yearly L4 Global 500m SIN Grid V061 version: 61.0"
        )

    LPCLOUD_MOD17A3HGF_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MOD17A3HGF_61.0",
            provider="LPCLOUD", 
            shortname="MOD17A3HGF",
            version="61.0",
            description="MODIS/Terra Net Primary Production Gap-Filled Yearly L4 Global 500m SIN Grid V061 version: 61.0"
        )

    LPCLOUD_MOD09Q1_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MOD09Q1_61.0",
            provider="LPCLOUD", 
            shortname="MOD09Q1",
            version="61.0",
            description="MODIS/Terra Surface Reflectance 8-Day L3 Global 250m SIN Grid V061 version: 61.0"
        )

    LPCLOUD_MOD09A1_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MOD09A1_61.0",
            provider="LPCLOUD", 
            shortname="MOD09A1",
            version="61.0",
            description="MODIS/Terra Surface Reflectance 8-Day L3 Global 500m SIN Grid V061 version: 61.0"
        )

    LPCLOUD_MOD09GA_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MOD09GA_61.0",
            provider="LPCLOUD", 
            shortname="MOD09GA",
            version="61.0",
            description="MODIS/Terra Surface Reflectance Daily L2G Global 1km and 500m SIN Grid V061 version: 61.0"
        )

    LPCLOUD_MOD09GQ_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MOD09GQ_61.0",
            provider="LPCLOUD", 
            shortname="MOD09GQ",
            version="61.0",
            description="MODIS/Terra Surface Reflectance Daily L2G Global 250m SIN Grid V061 version: 61.0"
        )

    LPCLOUD_MOD09CMG_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MOD09CMG_61.0",
            provider="LPCLOUD", 
            shortname="MOD09CMG",
            version="61.0",
            description="MODIS/Terra Surface Reflectance Daily L3 Global 0.05Deg CMG V061 version: 61.0"
        )

    LPCLOUD_MOD14_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MOD14_61.0",
            provider="LPCLOUD", 
            shortname="MOD14",
            version="61.0",
            description="MODIS/Terra Thermal Anomalies/Fire 5-Min L2 Swath 1km V061 version: 61.0"
        )

    LPCLOUD_MOD14A2_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MOD14A2_61.0",
            provider="LPCLOUD", 
            shortname="MOD14A2",
            version="61.0",
            description="MODIS/Terra Thermal Anomalies/Fire 8-Day L3 Global 1km SIN Grid V061 version: 61.0"
        )

    LPCLOUD_MOD14A1_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MOD14A1_61.0",
            provider="LPCLOUD", 
            shortname="MOD14A1",
            version="61.0",
            description="MODIS/Terra Thermal Anomalies/Fire Daily L3 Global 1km SIN Grid V061 version: 61.0"
        )

    LPCLOUD_MOD44B_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MOD44B_61.0",
            provider="LPCLOUD", 
            shortname="MOD44B",
            version="61.0",
            description="MODIS/Terra Vegetation Continuous Fields Yearly L3 Global 250m SIN Grid V061 version: 61.0"
        )

    LPCLOUD_MOD13C1_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MOD13C1_61.0",
            provider="LPCLOUD", 
            shortname="MOD13C1",
            version="61.0",
            description="MODIS/Terra Vegetation Indices 16-Day L3 Global 0.05Deg CMG V061 version: 61.0"
        )

    LPCLOUD_MOD13A2_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MOD13A2_61.0",
            provider="LPCLOUD", 
            shortname="MOD13A2",
            version="61.0",
            description="MODIS/Terra Vegetation Indices 16-Day L3 Global 1km SIN Grid V061 version: 61.0"
        )

    LPCLOUD_MOD13Q1_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MOD13Q1_61.0",
            provider="LPCLOUD", 
            shortname="MOD13Q1",
            version="61.0",
            description="MODIS/Terra Vegetation Indices 16-Day L3 Global 250m SIN Grid V061 version: 61.0"
        )

    LPCLOUD_MOD13A1_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MOD13A1_61.0",
            provider="LPCLOUD", 
            shortname="MOD13A1",
            version="61.0",
            description="MODIS/Terra Vegetation Indices 16-Day L3 Global 500m SIN Grid V061 version: 61.0"
        )

    LPCLOUD_MOD13C2_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MOD13C2_61.0",
            provider="LPCLOUD", 
            shortname="MOD13C2",
            version="61.0",
            description="MODIS/Terra Vegetation Indices Monthly L3 Global 0.05Deg CMG V061 version: 61.0"
        )

    LPCLOUD_MOD13A3_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MOD13A3_61.0",
            provider="LPCLOUD", 
            shortname="MOD13A3",
            version="61.0",
            description="MODIS/Terra Vegetation Indices Monthly L3 Global 1km SIN Grid V061 version: 61.0"
        )

    LPCLOUD_MOD28C2_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MOD28C2_61.0",
            provider="LPCLOUD", 
            shortname="MOD28C2",
            version="61.0",
            description="MODIS/Terra Water Reservoir 8-Day L3 Global V061 version: 61.0"
        )

    LPCLOUD_MOD28C3_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MOD28C3_61.0",
            provider="LPCLOUD", 
            shortname="MOD28C3",
            version="61.0",
            description="MODIS/Terra Water Reservoir Monthly L3 Global V061 version: 61.0"
        )

    LPCLOUD_MCD19A2CMG_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD19A2CMG_61.0",
            provider="LPCLOUD", 
            shortname="MCD19A2CMG",
            version="61.0",
            description="MODIS/Terra+Aqua AOD and Water Vapor from MAIAC, Daily L3 Global 0.05Deg CMG V061 version: 61.0"
        )

    LPCLOUD_MCD19A3D_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD19A3D_61.0",
            provider="LPCLOUD", 
            shortname="MCD19A3D",
            version="61.0",
            description="MODIS/Terra+Aqua BRDF Model Parameters Daily L3 Global 1km SIN Grid V061 version: 61.0"
        )

    LPCLOUD_MCD43A3_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD43A3_61.0",
            provider="LPCLOUD", 
            shortname="MCD43A3",
            version="61.0",
            description="MODIS/Terra+Aqua BRDF/Albedo Albedo Daily L3 Global - 500m V061 version: 61.0"
        )

    LPCLOUD_MCD43C3_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD43C3_61.0",
            provider="LPCLOUD", 
            shortname="MCD43C3",
            version="61.0",
            description="MODIS/Terra+Aqua BRDF/Albedo Albedo Daily L3 Global 0.05Deg CMG V061 version: 61.0"
        )

    LPCLOUD_MCD43D42_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD43D42_61.0",
            provider="LPCLOUD", 
            shortname="MCD43D42",
            version="61.0",
            description="MODIS/Terra+Aqua BRDF/Albedo Black Sky Albedo Band1 Daily L3 Global 30ArcSec CMG V061 version: 61.0"
        )

    LPCLOUD_MCD43D43_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD43D43_61.0",
            provider="LPCLOUD", 
            shortname="MCD43D43",
            version="61.0",
            description="MODIS/Terra+Aqua BRDF/Albedo Black Sky Albedo Band2 Daily L3 Global 30ArcSec CMG V061 version: 61.0"
        )

    LPCLOUD_MCD43D44_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD43D44_61.0",
            provider="LPCLOUD", 
            shortname="MCD43D44",
            version="61.0",
            description="MODIS/Terra+Aqua BRDF/Albedo Black Sky Albedo Band3 Daily L3 Global 30ArcSec CMG V061 version: 61.0"
        )

    LPCLOUD_MCD43D45_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD43D45_61.0",
            provider="LPCLOUD", 
            shortname="MCD43D45",
            version="61.0",
            description="MODIS/Terra+Aqua BRDF/Albedo Black Sky Albedo Band4 Daily L3 Global 30ArcSec CMG V061 version: 61.0"
        )

    LPCLOUD_MCD43D46_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD43D46_61.0",
            provider="LPCLOUD", 
            shortname="MCD43D46",
            version="61.0",
            description="MODIS/Terra+Aqua BRDF/Albedo Black Sky Albedo Band5 Daily L3 Global 30ArcSec CMG V061 version: 61.0"
        )

    LPCLOUD_MCD43D47_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD43D47_61.0",
            provider="LPCLOUD", 
            shortname="MCD43D47",
            version="61.0",
            description="MODIS/Terra+Aqua BRDF/Albedo Black Sky Albedo Band6 Daily L3 Global 30ArcSec CMG V061 version: 61.0"
        )

    LPCLOUD_MCD43D48_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD43D48_61.0",
            provider="LPCLOUD", 
            shortname="MCD43D48",
            version="61.0",
            description="MODIS/Terra+Aqua BRDF/Albedo Black Sky Albedo Band7 Daily L3 Global 30ArcSec CMG V061 version: 61.0"
        )

    LPCLOUD_MCD43D50_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD43D50_61.0",
            provider="LPCLOUD", 
            shortname="MCD43D50",
            version="61.0",
            description="MODIS/Terra+Aqua BRDF/Albedo Black Sky Albedo NIR Daily L3 Global 30ArcSec CMG V061 version: 61.0"
        )

    LPCLOUD_MCD43D51_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD43D51_61.0",
            provider="LPCLOUD", 
            shortname="MCD43D51",
            version="61.0",
            description="MODIS/Terra+Aqua BRDF/Albedo Black Sky Albedo Shortwave Daily L3 Global 30ArcSec CMG V061 version: 61.0"
        )

    LPCLOUD_MCD43D49_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD43D49_61.0",
            provider="LPCLOUD", 
            shortname="MCD43D49",
            version="61.0",
            description="MODIS/Terra+Aqua BRDF/Albedo Black Sky Albedo VIS Daily L3 Global 30ArcSec CMG V061 version: 61.0"
        )

    LPCLOUD_MCD43A1_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD43A1_61.0",
            provider="LPCLOUD", 
            shortname="MCD43A1",
            version="61.0",
            description="MODIS/Terra+Aqua BRDF/Albedo Model Parameters Daily L3 Global - 500m V061 version: 61.0"
        )

    LPCLOUD_MCD43C1_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD43C1_61.0",
            provider="LPCLOUD", 
            shortname="MCD43C1",
            version="61.0",
            description="MODIS/Terra+Aqua BRDF/Albedo Model Parameters Daily L3 Global 0.05Deg CMG V061 version: 61.0"
        )

    LPCLOUD_MCD43D62_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD43D62_61.0",
            provider="LPCLOUD", 
            shortname="MCD43D62",
            version="61.0",
            description="MODIS/Terra+Aqua BRDF/Albedo Nadir BRDF-Adjusted Ref Band1 Daily L3 Global 30ArcSec CMG V061 version: 61.0"
        )

    LPCLOUD_MCD43D63_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD43D63_61.0",
            provider="LPCLOUD", 
            shortname="MCD43D63",
            version="61.0",
            description="MODIS/Terra+Aqua BRDF/Albedo Nadir BRDF-Adjusted Ref Band2 Daily L3 Global 30ArcSec CMG V061 version: 61.0"
        )

    LPCLOUD_MCD43D64_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD43D64_61.0",
            provider="LPCLOUD", 
            shortname="MCD43D64",
            version="61.0",
            description="MODIS/Terra+Aqua BRDF/Albedo Nadir BRDF-Adjusted Ref Band3 Daily L3 Global 30ArcSec CMG V061 version: 61.0"
        )

    LPCLOUD_MCD43D65_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD43D65_61.0",
            provider="LPCLOUD", 
            shortname="MCD43D65",
            version="61.0",
            description="MODIS/Terra+Aqua BRDF/Albedo Nadir BRDF-Adjusted Ref Band4 Daily L3 Global 30ArcSec CMG V061 version: 61.0"
        )

    LPCLOUD_MCD43D66_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD43D66_61.0",
            provider="LPCLOUD", 
            shortname="MCD43D66",
            version="61.0",
            description="MODIS/Terra+Aqua BRDF/Albedo Nadir BRDF-Adjusted Ref Band5 Daily L3 Global 30ArcSec CMG V061 version: 61.0"
        )

    LPCLOUD_MCD43D67_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD43D67_61.0",
            provider="LPCLOUD", 
            shortname="MCD43D67",
            version="61.0",
            description="MODIS/Terra+Aqua BRDF/Albedo Nadir BRDF-Adjusted Ref Band6 Daily L3 Global 30ArcSec CMG V061 version: 61.0"
        )

    LPCLOUD_MCD43D68_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD43D68_61.0",
            provider="LPCLOUD", 
            shortname="MCD43D68",
            version="61.0",
            description="MODIS/Terra+Aqua BRDF/Albedo Nadir BRDF-Adjusted Ref Band7 Daily L3 Global 30ArcSec CMG V061 version: 61.0"
        )

    LPCLOUD_MCD43A4_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD43A4_61.0",
            provider="LPCLOUD", 
            shortname="MCD43A4",
            version="61.0",
            description="MODIS/Terra+Aqua BRDF/Albedo Nadir BRDF-Adjusted Ref Daily L3 Global - 500m V061 version: 61.0"
        )

    LPCLOUD_MCD43C4_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD43C4_61.0",
            provider="LPCLOUD", 
            shortname="MCD43C4",
            version="61.0",
            description="MODIS/Terra+Aqua BRDF/Albedo Nadir BRDF-Adjusted Ref Daily L3 Global 0.05Deg CMG V061 version: 61.0"
        )

    LPCLOUD_MCD43D01_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD43D01_61.0",
            provider="LPCLOUD", 
            shortname="MCD43D01",
            version="61.0",
            description="MODIS/Terra+Aqua BRDF/Albedo Parameter 1 Band 1 Daily L3 Global 30 ArcSec CMG V061 version: 61.0"
        )

    LPCLOUD_MCD43D04_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD43D04_61.0",
            provider="LPCLOUD", 
            shortname="MCD43D04",
            version="61.0",
            description="MODIS/Terra+Aqua BRDF/Albedo Parameter 1 Band 2 Daily L3 Global 30 ArcSec CMG V061 version: 61.0"
        )

    LPCLOUD_MCD43D02_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD43D02_61.0",
            provider="LPCLOUD", 
            shortname="MCD43D02",
            version="61.0",
            description="MODIS/Terra+Aqua BRDF/Albedo Parameter 2 Band 1 Daily L3 Global 30 ArcSec CMG V061 version: 61.0"
        )

    LPCLOUD_MCD43D05_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD43D05_61.0",
            provider="LPCLOUD", 
            shortname="MCD43D05",
            version="61.0",
            description="MODIS/Terra+Aqua BRDF/Albedo Parameter 2 Band 2 Daily L3 Global 30 ArcSec CMG V061 version: 61.0"
        )

    LPCLOUD_MCD43D03_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD43D03_61.0",
            provider="LPCLOUD", 
            shortname="MCD43D03",
            version="61.0",
            description="MODIS/Terra+Aqua BRDF/Albedo Parameter 3 Band 1 Daily L3 Global 30 ArcSec CMG V061 version: 61.0"
        )

    LPCLOUD_MCD43D06_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD43D06_61.0",
            provider="LPCLOUD", 
            shortname="MCD43D06",
            version="61.0",
            description="MODIS/Terra+Aqua BRDF/Albedo Parameter 3 Band 2 Daily L3 Global 30 ArcSec CMG V061 version: 61.0"
        )

    LPCLOUD_MCD43D07_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD43D07_61.0",
            provider="LPCLOUD", 
            shortname="MCD43D07",
            version="61.0",
            description="MODIS/Terra+Aqua BRDF/Albedo Parameter1 Band3 Daily L3 Global 30ArcSec CMG V061 version: 61.0"
        )

    LPCLOUD_MCD43D10_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD43D10_61.0",
            provider="LPCLOUD", 
            shortname="MCD43D10",
            version="61.0",
            description="MODIS/Terra+Aqua BRDF/Albedo Parameter1 Band4 Daily L3 Global 30ArcSec CMG V061 version: 61.0"
        )

    LPCLOUD_MCD43D13_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD43D13_61.0",
            provider="LPCLOUD", 
            shortname="MCD43D13",
            version="61.0",
            description="MODIS/Terra+Aqua BRDF/Albedo Parameter1 Band5 Daily L3 Global 30ArcSec CMG V061 version: 61.0"
        )

    LPCLOUD_MCD43D16_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD43D16_61.0",
            provider="LPCLOUD", 
            shortname="MCD43D16",
            version="61.0",
            description="MODIS/Terra+Aqua BRDF/Albedo Parameter1 Band6 Daily L3 Global 30ArcSec CMG V061 version: 61.0"
        )

    LPCLOUD_MCD43D19_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD43D19_61.0",
            provider="LPCLOUD", 
            shortname="MCD43D19",
            version="61.0",
            description="MODIS/Terra+Aqua BRDF/Albedo Parameter1 Band7 Daily L3 Global 30ArcSec CMG V061 version: 61.0"
        )

    LPCLOUD_MCD43D25_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD43D25_61.0",
            provider="LPCLOUD", 
            shortname="MCD43D25",
            version="61.0",
            description="MODIS/Terra+Aqua BRDF/Albedo Parameter1 NIR Daily L3 Global 30ArcSec CMG V061 version: 61.0"
        )

    LPCLOUD_MCD43D28_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD43D28_61.0",
            provider="LPCLOUD", 
            shortname="MCD43D28",
            version="61.0",
            description="MODIS/Terra+Aqua BRDF/Albedo Parameter1 Shortwave Daily L3 Global 30ArcSec CMG V061 version: 61.0"
        )

    LPCLOUD_MCD43D22_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD43D22_61.0",
            provider="LPCLOUD", 
            shortname="MCD43D22",
            version="61.0",
            description="MODIS/Terra+Aqua BRDF/Albedo Parameter1 VIS Daily L3 Global 30ArcSec CMG V061 version: 61.0"
        )

    LPCLOUD_MCD43D08_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD43D08_61.0",
            provider="LPCLOUD", 
            shortname="MCD43D08",
            version="61.0",
            description="MODIS/Terra+Aqua BRDF/Albedo Parameter2 Band3 Daily L3 Global 30ArcSec CMG V061 version: 61.0"
        )

    LPCLOUD_MCD43D11_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD43D11_61.0",
            provider="LPCLOUD", 
            shortname="MCD43D11",
            version="61.0",
            description="MODIS/Terra+Aqua BRDF/Albedo Parameter2 Band4 Daily L3 Global 30ArcSec CMG V061 version: 61.0"
        )

    LPCLOUD_MCD43D14_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD43D14_61.0",
            provider="LPCLOUD", 
            shortname="MCD43D14",
            version="61.0",
            description="MODIS/Terra+Aqua BRDF/Albedo Parameter2 Band5 Daily L3 Global 30ArcSec CMG V061 version: 61.0"
        )

    LPCLOUD_MCD43D17_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD43D17_61.0",
            provider="LPCLOUD", 
            shortname="MCD43D17",
            version="61.0",
            description="MODIS/Terra+Aqua BRDF/Albedo Parameter2 Band6 Daily L3 Global 30ArcSec CMG V061 version: 61.0"
        )

    LPCLOUD_MCD43D20_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD43D20_61.0",
            provider="LPCLOUD", 
            shortname="MCD43D20",
            version="61.0",
            description="MODIS/Terra+Aqua BRDF/Albedo Parameter2 Band7 Daily L3 Global 30ArcSec CMG V061 version: 61.0"
        )

    LPCLOUD_MCD43D26_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD43D26_61.0",
            provider="LPCLOUD", 
            shortname="MCD43D26",
            version="61.0",
            description="MODIS/Terra+Aqua BRDF/Albedo Parameter2 NIR Daily L3 Global 30ArcSec CMG V061 version: 61.0"
        )

    LPCLOUD_MCD43D29_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD43D29_61.0",
            provider="LPCLOUD", 
            shortname="MCD43D29",
            version="61.0",
            description="MODIS/Terra+Aqua BRDF/Albedo Parameter2 Shortwave Daily L3 Global 30ArcSec CMG V061 version: 61.0"
        )

    LPCLOUD_MCD43D23_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD43D23_61.0",
            provider="LPCLOUD", 
            shortname="MCD43D23",
            version="61.0",
            description="MODIS/Terra+Aqua BRDF/Albedo Parameter2 VIS Daily L3 Global 30ArcSec CMG V061 version: 61.0"
        )

    LPCLOUD_MCD43D09_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD43D09_61.0",
            provider="LPCLOUD", 
            shortname="MCD43D09",
            version="61.0",
            description="MODIS/Terra+Aqua BRDF/Albedo Parameter3 Band3 Daily L3 Global 30ArcSec CMG V061 version: 61.0"
        )

    LPCLOUD_MCD43D12_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD43D12_61.0",
            provider="LPCLOUD", 
            shortname="MCD43D12",
            version="61.0",
            description="MODIS/Terra+Aqua BRDF/Albedo Parameter3 Band4 Daily L3 Global 30ArcSec CMG V061 version: 61.0"
        )

    LPCLOUD_MCD43D15_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD43D15_61.0",
            provider="LPCLOUD", 
            shortname="MCD43D15",
            version="61.0",
            description="MODIS/Terra+Aqua BRDF/Albedo Parameter3 Band5 Daily L3 Global 30ArcSec CMG V061 version: 61.0"
        )

    LPCLOUD_MCD43D18_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD43D18_61.0",
            provider="LPCLOUD", 
            shortname="MCD43D18",
            version="61.0",
            description="MODIS/Terra+Aqua BRDF/Albedo Parameter3 Band6 Daily L3 Global 30ArcSec CMG V061 version: 61.0"
        )

    LPCLOUD_MCD43D21_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD43D21_61.0",
            provider="LPCLOUD", 
            shortname="MCD43D21",
            version="61.0",
            description="MODIS/Terra+Aqua BRDF/Albedo Parameter3 Band7 Daily L3 Global 30ArcSec CMG V061 version: 61.0"
        )

    LPCLOUD_MCD43D27_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD43D27_61.0",
            provider="LPCLOUD", 
            shortname="MCD43D27",
            version="61.0",
            description="MODIS/Terra+Aqua BRDF/Albedo Parameter3 NIR Daily L3 Global 30ArcSec CMG V061 version: 61.0"
        )

    LPCLOUD_MCD43D30_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD43D30_61.0",
            provider="LPCLOUD", 
            shortname="MCD43D30",
            version="61.0",
            description="MODIS/Terra+Aqua BRDF/Albedo Parameter3 Shortwave Daily L3 Global 30ArcSec CMG V061 version: 61.0"
        )

    LPCLOUD_MCD43D24_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD43D24_61.0",
            provider="LPCLOUD", 
            shortname="MCD43D24",
            version="61.0",
            description="MODIS/Terra+Aqua BRDF/Albedo Parameter3 VIS Daily L3 Global 30ArcSec CMG V061 version: 61.0"
        )

    LPCLOUD_MCD43D31_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD43D31_61.0",
            provider="LPCLOUD", 
            shortname="MCD43D31",
            version="61.0",
            description="MODIS/Terra+Aqua BRDF/Albedo QA BRDFQuality Daily L3 Global 30ArcSec CMG V061 version: 61.0"
        )

    LPCLOUD_MCD43D32_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD43D32_61.0",
            provider="LPCLOUD", 
            shortname="MCD43D32",
            version="61.0",
            description="MODIS/Terra+Aqua BRDF/Albedo QA LocalSolarNoon Daily L3 Global 30ArcSec CMG V061 version: 61.0"
        )

    LPCLOUD_MCD43D40_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD43D40_61.0",
            provider="LPCLOUD", 
            shortname="MCD43D40",
            version="61.0",
            description="MODIS/Terra+Aqua BRDF/Albedo QA SnowStatus Daily L3 Global 30ArcSec CMG V061 version: 61.0"
        )

    LPCLOUD_MCD43D41_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD43D41_61.0",
            provider="LPCLOUD", 
            shortname="MCD43D41",
            version="61.0",
            description="MODIS/Terra+Aqua BRDF/Albedo QA Uncertainty Daily L3 Global 30ArcSec CMG V061 version: 61.0"
        )

    LPCLOUD_MCD43D33_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD43D33_61.0",
            provider="LPCLOUD", 
            shortname="MCD43D33",
            version="61.0",
            description="MODIS/Terra+Aqua BRDF/Albedo QA ValidobsBand1 Daily L3 Global 30ArcSec CMG V061 version: 61.0"
        )

    LPCLOUD_MCD43D34_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD43D34_61.0",
            provider="LPCLOUD", 
            shortname="MCD43D34",
            version="61.0",
            description="MODIS/Terra+Aqua BRDF/Albedo QA ValidobsBand2 Daily L3 Global 30ArcSec CMG V061 version: 61.0"
        )

    LPCLOUD_MCD43D35_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD43D35_61.0",
            provider="LPCLOUD", 
            shortname="MCD43D35",
            version="61.0",
            description="MODIS/Terra+Aqua BRDF/Albedo QA ValidobsBand3 Daily L3 Global 30ArcSec CMG V061 version: 61.0"
        )

    LPCLOUD_MCD43D36_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD43D36_61.0",
            provider="LPCLOUD", 
            shortname="MCD43D36",
            version="61.0",
            description="MODIS/Terra+Aqua BRDF/Albedo QA ValidobsBand4 Daily L3 Global 30ArcSec CMG V061 version: 61.0"
        )

    LPCLOUD_MCD43D37_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD43D37_61.0",
            provider="LPCLOUD", 
            shortname="MCD43D37",
            version="61.0",
            description="MODIS/Terra+Aqua BRDF/Albedo QA ValidobsBand5 Daily L3 Global 30ArcSec CMG V061 version: 61.0"
        )

    LPCLOUD_MCD43D38_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD43D38_61.0",
            provider="LPCLOUD", 
            shortname="MCD43D38",
            version="61.0",
            description="MODIS/Terra+Aqua BRDF/Albedo QA ValidobsBand6 Daily L3 Global 30ArcSec CMG V061 version: 61.0"
        )

    LPCLOUD_MCD43D39_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD43D39_61.0",
            provider="LPCLOUD", 
            shortname="MCD43D39",
            version="61.0",
            description="MODIS/Terra+Aqua BRDF/Albedo QA ValidobsBand7 Daily L3 Global 30ArcSec CMG V061 version: 61.0"
        )

    LPCLOUD_MCD43A2_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD43A2_61.0",
            provider="LPCLOUD", 
            shortname="MCD43A2",
            version="61.0",
            description="MODIS/Terra+Aqua BRDF/Albedo Quality Daily L3 Global - 500m V061 version: 61.0"
        )

    LPCLOUD_MCD43C2_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD43C2_61.0",
            provider="LPCLOUD", 
            shortname="MCD43C2",
            version="61.0",
            description="MODIS/Terra+Aqua BRDF/Albedo Snow-free Model Parameters Daily L3 Global 0.05Deg CMG V061 version: 61.0"
        )

    LPCLOUD_MCD43D52_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD43D52_61.0",
            provider="LPCLOUD", 
            shortname="MCD43D52",
            version="61.0",
            description="MODIS/Terra+Aqua BRDF/Albedo White Sky Albedo Band1 Daily L3 Global 30ArcSec CMG V061 version: 61.0"
        )

    LPCLOUD_MCD43D53_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD43D53_61.0",
            provider="LPCLOUD", 
            shortname="MCD43D53",
            version="61.0",
            description="MODIS/Terra+Aqua BRDF/Albedo White Sky Albedo Band2 Daily L3 Global 30ArcSec CMG V061 version: 61.0"
        )

    LPCLOUD_MCD43D54_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD43D54_61.0",
            provider="LPCLOUD", 
            shortname="MCD43D54",
            version="61.0",
            description="MODIS/Terra+Aqua BRDF/Albedo White Sky Albedo Band3 Daily L3 Global 30ArcSec CMG V061 version: 61.0"
        )

    LPCLOUD_MCD43D55_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD43D55_61.0",
            provider="LPCLOUD", 
            shortname="MCD43D55",
            version="61.0",
            description="MODIS/Terra+Aqua BRDF/Albedo White Sky Albedo Band4 Daily L3 Global 30ArcSec CMG V061 version: 61.0"
        )

    LPCLOUD_MCD43D56_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD43D56_61.0",
            provider="LPCLOUD", 
            shortname="MCD43D56",
            version="61.0",
            description="MODIS/Terra+Aqua BRDF/Albedo White Sky Albedo Band5 Daily L3 Global 30ArcSec CMG V061 version: 61.0"
        )

    LPCLOUD_MCD43D57_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD43D57_61.0",
            provider="LPCLOUD", 
            shortname="MCD43D57",
            version="61.0",
            description="MODIS/Terra+Aqua BRDF/Albedo White Sky Albedo Band6 Daily L3 Global 30ArcSec CMG V061 version: 61.0"
        )

    LPCLOUD_MCD43D58_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD43D58_61.0",
            provider="LPCLOUD", 
            shortname="MCD43D58",
            version="61.0",
            description="MODIS/Terra+Aqua BRDF/Albedo White Sky Albedo Band7 Daily L3 Global 30ArcSec CMG V061 version: 61.0"
        )

    LPCLOUD_MCD43D60_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD43D60_61.0",
            provider="LPCLOUD", 
            shortname="MCD43D60",
            version="61.0",
            description="MODIS/Terra+Aqua BRDF/Albedo White Sky Albedo NIR Daily L3 Global 30ArcSec CMG V061 version: 61.0"
        )

    LPCLOUD_MCD43D61_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD43D61_61.0",
            provider="LPCLOUD", 
            shortname="MCD43D61",
            version="61.0",
            description="MODIS/Terra+Aqua BRDF/Albedo White Sky Albedo Shortwave Daily L3 Global 30ArcSec CMG V061 version: 61.0"
        )

    LPCLOUD_MCD43D59_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD43D59_61.0",
            provider="LPCLOUD", 
            shortname="MCD43D59",
            version="61.0",
            description="MODIS/Terra+Aqua BRDF/Albedo White Sky Albedo VIS Daily L3 Global 30ArcSec CMG V061 version: 61.0"
        )

    LPCLOUD_MCD64A1_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD64A1_61.0",
            provider="LPCLOUD", 
            shortname="MCD64A1",
            version="61.0",
            description="MODIS/Terra+Aqua Direct Broadcast Burned Area Monthly L3 Global 500m SIN Grid V061 version: 61.0"
        )

    LPCLOUD_MCD18C1_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD18C1_61.0",
            provider="LPCLOUD", 
            shortname="MCD18C1",
            version="61.0",
            description="MODIS/Terra+Aqua Downward Shortwave Radiation Daily/3-Hour L3 Global 0.05Deg CMG V061 version: 61.0"
        )

    LPCLOUD_MCD18C1_V620 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD18C1_62.0",
            provider="LPCLOUD", 
            shortname="MCD18C1",
            version="62.0",
            description="MODIS/Terra+Aqua Downward Shortwave Radiation Daily/3-Hour L3 Global 0.05Deg CMG V062 version: 62.0"
        )

    LPCLOUD_MCD19A2_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD19A2_61.0",
            provider="LPCLOUD", 
            shortname="MCD19A2",
            version="61.0",
            description="MODIS/Terra+Aqua Land Aerosol Optical Depth Daily L2G Global 1km SIN Grid V061 version: 61.0"
        )

    LPCLOUD_MCD12Q2_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD12Q2_61.0",
            provider="LPCLOUD", 
            shortname="MCD12Q2",
            version="61.0",
            description="MODIS/Terra+Aqua Land Cover Dynamics Yearly L3 Global 500m SIN Grid V061 version: 61.0"
        )

    LPCLOUD_MCD12C1_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD12C1_61.0",
            provider="LPCLOUD", 
            shortname="MCD12C1",
            version="61.0",
            description="MODIS/Terra+Aqua Land Cover Type Yearly L3 Global 0.05Deg CMG V061 version: 61.0"
        )

    LPCLOUD_MCD12Q1_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD12Q1_61.0",
            provider="LPCLOUD", 
            shortname="MCD12Q1",
            version="61.0",
            description="MODIS/Terra+Aqua Land Cover Type Yearly L3 Global 500m SIN Grid V061 version: 61.0"
        )

    LPCLOUD_MCD19A1_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD19A1_61.0",
            provider="LPCLOUD", 
            shortname="MCD19A1",
            version="61.0",
            description="MODIS/Terra+Aqua Land Surface BRF Daily L2G Global 500m and 1km SIN Grid V061 version: 61.0"
        )

    LPCLOUD_MCD15A3H_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD15A3H_61.0",
            provider="LPCLOUD", 
            shortname="MCD15A3H",
            version="61.0",
            description="MODIS/Terra+Aqua Leaf Area Index/FPAR 4-Day L4 Global 500m SIN Grid V061 version: 61.0"
        )

    LPCLOUD_MCD15A2H_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD15A2H_61.0",
            provider="LPCLOUD", 
            shortname="MCD15A2H",
            version="61.0",
            description="MODIS/Terra+Aqua Leaf Area Index/FPAR 8-Day L4 Global 500m SIN Grid V061 version: 61.0"
        )

    LPCLOUD_MCD18C2_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD18C2_61.0",
            provider="LPCLOUD", 
            shortname="MCD18C2",
            version="61.0",
            description="MODIS/Terra+Aqua Photosynthetically Active Radiation Daily/3-Hour L3 Global 0.05Deg CMG V061 version: 61.0"
        )

    LPCLOUD_MCD18C2_V620 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD18C2_62.0",
            provider="LPCLOUD", 
            shortname="MCD18C2",
            version="62.0",
            description="MODIS/Terra+Aqua Photosynthetically Active Radiation Daily/3-Hour L3 Global 0.05Deg CMG V062 version: 62.0"
        )

    LPCLOUD_MCD18A2_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD18A2_61.0",
            provider="LPCLOUD", 
            shortname="MCD18A2",
            version="61.0",
            description="MODIS/Terra+Aqua Photosynthetically Active Radiation Daily/3-Hour L3 Global 1km SIN Grid V061 version: 61.0"
        )

    LPCLOUD_MCD18A2_V620 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD18A2_62.0",
            provider="LPCLOUD", 
            shortname="MCD18A2",
            version="62.0",
            description="MODIS/Terra+Aqua Photosynthetically Active Radiation Daily/3-Hour L3 Global 1km SIN Grid V062 version: 62.0"
        )

    LPCLOUD_MCD18A1_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD18A1_61.0",
            provider="LPCLOUD", 
            shortname="MCD18A1",
            version="61.0",
            description="MODIS/Terra+Aqua Surface Radiation Daily/3-Hour L3 Global 1km SIN Grid V061 version: 61.0"
        )

    LPCLOUD_MCD18A1_V620 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD18A1_62.0",
            provider="LPCLOUD", 
            shortname="MCD18A1",
            version="62.0",
            description="MODIS/Terra+Aqua Surface Radiation Daily/3-Hour L3 Global 1km SIN Grid V062 version: 62.0"
        )

    LPCLOUD_MCD19A1CMGL_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD19A1CMGL_61.0",
            provider="LPCLOUD", 
            shortname="MCD19A1CMGL",
            version="61.0",
            description="MODIS/Terra+Aqua Surface Reflectance (Bands 1-7) from MAIAC, Daily L3 Global 0.05Deg CMG V061 version: 61.0"
        )

    LPCLOUD_MCD19A1CMGO_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD19A1CMGO_61.0",
            provider="LPCLOUD", 
            shortname="MCD19A1CMGO",
            version="61.0",
            description="MODIS/Terra+Aqua Surface Reflectance (Bands 8-12) from MAIAC, Daily L3 Global 0.05Deg CMG V061 version: 61.0"
        )

    LPCLOUD_MCD19A3CMG_V610 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_MCD19A3CMG_61.0",
            provider="LPCLOUD", 
            shortname="MCD19A3CMG",
            version="61.0",
            description="MODIS/Terra+Aqua Vegetation Index from MAIAC, Daily L3 Global 0.05Deg CMG V061 version: 61.0"
        )

    LPCLOUD_WaterBalance_Monthly_Historical_GRIDMET_V15 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_WaterBalance_Monthly_Historical_GRIDMET_1.5",
            provider="LPCLOUD", 
            shortname="WaterBalance_Monthly_Historical_GRIDMET",
            version="1.5",
            description="Monthly Historical Water Balance Products for the CONUS version: 1.5"
        )

    LPCLOUD_OPERA_L3_DIST_ALERT_HLS_PROVISIONAL_V0_V00 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_OPERA_L3_DIST-ALERT-HLS_PROVISIONAL_V0_0.0",
            provider="LPCLOUD", 
            shortname="OPERA_L3_DIST-ALERT-HLS_PROVISIONAL_V0",
            version="0.0",
            description="OPERA Land Surface Disturbance Alert from Harmonized Landsat Sentinel-2 provisional product (Version 0) version: 0.0"
        )

    LPCLOUD_OPERA_L3_DIST_ANN_HLS_V1_V10 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_OPERA_L3_DIST-ANN-HLS_V1_1.0",
            provider="LPCLOUD", 
            shortname="OPERA_L3_DIST-ANN-HLS_V1",
            version="1.0",
            description="OPERA Land Surface Disturbance Annual from Harmonized Landsat Sentinel-2 product (Version 1) version: 1.0"
        )

    LPCLOUD_VJ121_V20 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_VJ121_2.0",
            provider="LPCLOUD", 
            shortname="VJ121",
            version="2.0",
            description="VIIRS/JPSS1 Land Surface Temperature and Emissivity 6-Min L2 Swath 750m V002 version: 2.0"
        )

    LPCLOUD_VJ121C2_V20 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_VJ121C2_2.0",
            provider="LPCLOUD", 
            shortname="VJ121C2",
            version="2.0",
            description="VIIRS/JPSS1 Land Surface Temperature/Emissivity 8-Day L3 Global 0.05Deg CMG V002 version: 2.0"
        )

    LPCLOUD_VJ121A2_V20 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_VJ121A2_2.0",
            provider="LPCLOUD", 
            shortname="VJ121A2",
            version="2.0",
            description="VIIRS/JPSS1 Land Surface Temperature/Emissivity 8-Day L3 Global 1km SIN Grid V002 version: 2.0"
        )

    LPCLOUD_VJ121C1_V20 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_VJ121C1_2.0",
            provider="LPCLOUD", 
            shortname="VJ121C1",
            version="2.0",
            description="VIIRS/JPSS1 Land Surface Temperature/Emissivity Daily L3 Global 0.05Deg CMG V002 version: 2.0"
        )

    LPCLOUD_VJ121A1D_V20 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_VJ121A1D_2.0",
            provider="LPCLOUD", 
            shortname="VJ121A1D",
            version="2.0",
            description="VIIRS/JPSS1 Land Surface Temperature/Emissivity Daily L3 Global 1km SIN Grid Day V002 version: 2.0"
        )

    LPCLOUD_VJ121A1N_V20 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_VJ121A1N_2.0",
            provider="LPCLOUD", 
            shortname="VJ121A1N",
            version="2.0",
            description="VIIRS/JPSS1 Land Surface Temperature/Emissivity Daily L3 Global 1km SIN Grid Night V002 version: 2.0"
        )

    LPCLOUD_VJ121C3_V20 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_VJ121C3_2.0",
            provider="LPCLOUD", 
            shortname="VJ121C3",
            version="2.0",
            description="VIIRS/JPSS1 Land Surface Temperature/Emissivity Monthly L3 Global 0.05Deg CMG V002 version: 2.0"
        )

    LPCLOUD_VJ115A2H_V20 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_VJ115A2H_2.0",
            provider="LPCLOUD", 
            shortname="VJ115A2H",
            version="2.0",
            description="VIIRS/JPSS1 Leaf Area Index/FPAR 8-Day L4 Global 500m SIN Grid V002 version: 2.0"
        )

    LPCLOUD_VJ103MODLL_V210 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_VJ103MODLL_21.0",
            provider="LPCLOUD", 
            shortname="VJ103MODLL",
            version="21.0",
            description="VIIRS/JPSS1 Moderate Resolution Terrain Corrected Geolocation 6-Min L1 Swath 750m Light V021 version: 21.0"
        )

    LPCLOUD_VJ109A1_V20 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_VJ109A1_2.0",
            provider="LPCLOUD", 
            shortname="VJ109A1",
            version="2.0",
            description="VIIRS/JPSS1 Surface Reflectance 8-Day L3 Global 1km SIN Grid V002 version: 2.0"
        )

    LPCLOUD_VJ109H1_V20 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_VJ109H1_2.0",
            provider="LPCLOUD", 
            shortname="VJ109H1",
            version="2.0",
            description="VIIRS/JPSS1 Surface Reflectance 8-Day L3 Global 500m SIN Grid V002 version: 2.0"
        )

    LPCLOUD_VJ109GA_V20 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_VJ109GA_2.0",
            provider="LPCLOUD", 
            shortname="VJ109GA",
            version="2.0",
            description="VIIRS/JPSS1 Surface Reflectance Daily L2G Global 1km and 500m SIN Grid V002 version: 2.0"
        )

    LPCLOUD_VJ109CMG_V20 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_VJ109CMG_2.0",
            provider="LPCLOUD", 
            shortname="VJ109CMG",
            version="2.0",
            description="VIIRS/JPSS1 Surface Reflectance Daily L3 Global 0.05Deg CMG V002 version: 2.0"
        )

    LPCLOUD_VJ114A1_V20 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_VJ114A1_2.0",
            provider="LPCLOUD", 
            shortname="VJ114A1",
            version="2.0",
            description="VIIRS/JPSS1 Thermal Anomalies and Fire Daily L3 Global 1km SIN Grid V002 version: 2.0"
        )

    LPCLOUD_VJ114_V20 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_VJ114_2.0",
            provider="LPCLOUD", 
            shortname="VJ114",
            version="2.0",
            description="VIIRS/JPSS1 Thermal Anomalies/Fire 6-Min L2 Swath 750m V002 version: 2.0"
        )

    LPCLOUD_VJ113C1_V20 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_VJ113C1_2.0",
            provider="LPCLOUD", 
            shortname="VJ113C1",
            version="2.0",
            description="VIIRS/JPSS1 Vegetation Indices 16-Day L3 Global 0.05Deg CMG V002 version: 2.0"
        )

    LPCLOUD_VJ113A2_V20 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_VJ113A2_2.0",
            provider="LPCLOUD", 
            shortname="VJ113A2",
            version="2.0",
            description="VIIRS/JPSS1 Vegetation Indices 16-Day L3 Global 1km SIN Grid V002 version: 2.0"
        )

    LPCLOUD_VJ113A1_V20 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_VJ113A1_2.0",
            provider="LPCLOUD", 
            shortname="VJ113A1",
            version="2.0",
            description="VIIRS/JPSS1 Vegetation Indices 16-Day L3 Global 500m SIN Grid V002 version: 2.0"
        )

    LPCLOUD_VJ113C2_V20 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_VJ113C2_2.0",
            provider="LPCLOUD", 
            shortname="VJ113C2",
            version="2.0",
            description="VIIRS/JPSS1 Vegetation Indices Monthly L3 Global 0.05Deg CMG V002 version: 2.0"
        )

    LPCLOUD_VJ113A3_V20 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_VJ113A3_2.0",
            provider="LPCLOUD", 
            shortname="VJ113A3",
            version="2.0",
            description="VIIRS/JPSS1 Vegetation Indices Monthly L3 Global 1km SIN Grid V002 version: 2.0"
        )

    LPCLOUD_VJ128C3_V20 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_VJ128C3_2.0",
            provider="LPCLOUD", 
            shortname="VJ128C3",
            version="2.0",
            description="VIIRS/JPSS1 Water Reservoir Monthly L3 Global V002 version: 2.0"
        )

    LPCLOUD_VNP21_V20 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_VNP21_2.0",
            provider="LPCLOUD", 
            shortname="VNP21",
            version="2.0",
            description="VIIRS/NPP Land Surface Temperature and Emissivity 6-Min L2 Swath 750m V002 version: 2.0"
        )

    LPCLOUD_VNP21C2_V20 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_VNP21C2_2.0",
            provider="LPCLOUD", 
            shortname="VNP21C2",
            version="2.0",
            description="VIIRS/NPP Land Surface Temperature/Emissivity 8-Day L3 Global 0.05Deg CMG V002 version: 2.0"
        )

    LPCLOUD_VNP21A2_V20 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_VNP21A2_2.0",
            provider="LPCLOUD", 
            shortname="VNP21A2",
            version="2.0",
            description="VIIRS/NPP Land Surface Temperature/Emissivity 8-Day L3 Global 1km SIN Grid V002 version: 2.0"
        )

    LPCLOUD_VNP21C1_V20 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_VNP21C1_2.0",
            provider="LPCLOUD", 
            shortname="VNP21C1",
            version="2.0",
            description="VIIRS/NPP Land Surface Temperature/Emissivity Daily L3 Global 0.05Deg CMG V002 version: 2.0"
        )

    LPCLOUD_VNP21A1D_V20 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_VNP21A1D_2.0",
            provider="LPCLOUD", 
            shortname="VNP21A1D",
            version="2.0",
            description="VIIRS/NPP Land Surface Temperature/Emissivity Daily L3 Global 1km SIN Grid Day V002 version: 2.0"
        )

    LPCLOUD_VNP21A1N_V20 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_VNP21A1N_2.0",
            provider="LPCLOUD", 
            shortname="VNP21A1N",
            version="2.0",
            description="VIIRS/NPP Land Surface Temperature/Emissivity Daily L3 Global 1km SIN Grid Night V002 version: 2.0"
        )

    LPCLOUD_VNP21C3_V20 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_VNP21C3_2.0",
            provider="LPCLOUD", 
            shortname="VNP21C3",
            version="2.0",
            description="VIIRS/NPP Land Surface Temperature/Emissivity Monthly L3 Global 0.05Deg CMG V002 version: 2.0"
        )

    LPCLOUD_VNP15A2H_V20 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_VNP15A2H_2.0",
            provider="LPCLOUD", 
            shortname="VNP15A2H",
            version="2.0",
            description="VIIRS/NPP Leaf Area Index/FPAR 8-Day L4 Global 500m SIN Grid V002 version: 2.0"
        )

    LPCLOUD_VNP03MODLL_V20 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_VNP03MODLL_2.0",
            provider="LPCLOUD", 
            shortname="VNP03MODLL",
            version="2.0",
            description="VIIRS/NPP Moderate Resolution Terrain Corrected Geolocation 6-Min L1 Swath 750m Light V002 version: 2.0"
        )

    LPCLOUD_VNP09A1_V20 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_VNP09A1_2.0",
            provider="LPCLOUD", 
            shortname="VNP09A1",
            version="2.0",
            description="VIIRS/NPP Surface Reflectance 8-Day L3 Global 1km SIN Grid V002 version: 2.0"
        )

    LPCLOUD_VNP09H1_V20 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_VNP09H1_2.0",
            provider="LPCLOUD", 
            shortname="VNP09H1",
            version="2.0",
            description="VIIRS/NPP Surface Reflectance 8-Day L3 Global 500m SIN Grid V002 version: 2.0"
        )

    LPCLOUD_VNP09GA_V20 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_VNP09GA_2.0",
            provider="LPCLOUD", 
            shortname="VNP09GA",
            version="2.0",
            description="VIIRS/NPP Surface Reflectance Daily L2G Global 1km and 500m SIN Grid V002 version: 2.0"
        )

    LPCLOUD_VNP09CMG_V20 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_VNP09CMG_2.0",
            provider="LPCLOUD", 
            shortname="VNP09CMG",
            version="2.0",
            description="VIIRS/NPP Surface Reflectance Daily L3 Global 0.05Deg CMG V002 version: 2.0"
        )

    LPCLOUD_VNP14A1_V20 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_VNP14A1_2.0",
            provider="LPCLOUD", 
            shortname="VNP14A1",
            version="2.0",
            description="VIIRS/NPP Thermal Anomalies and Fire Daily L3 Global 1km SIN Grid V002 version: 2.0"
        )

    LPCLOUD_VNP14_V20 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_VNP14_2.0",
            provider="LPCLOUD", 
            shortname="VNP14",
            version="2.0",
            description="VIIRS/NPP Thermal Anomalies/Fire 6-Min L2 Swath 750m V002 version: 2.0"
        )

    LPCLOUD_VNP13C1_V20 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_VNP13C1_2.0",
            provider="LPCLOUD", 
            shortname="VNP13C1",
            version="2.0",
            description="VIIRS/NPP Vegetation Indices 16-Day L3 Global 0.05Deg CMG V002 version: 2.0"
        )

    LPCLOUD_VNP13A2_V20 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_VNP13A2_2.0",
            provider="LPCLOUD", 
            shortname="VNP13A2",
            version="2.0",
            description="VIIRS/NPP Vegetation Indices 16-Day L3 Global 1km SIN Grid V002 version: 2.0"
        )

    LPCLOUD_VNP13A1_V20 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_VNP13A1_2.0",
            provider="LPCLOUD", 
            shortname="VNP13A1",
            version="2.0",
            description="VIIRS/NPP Vegetation Indices 16-Day L3 Global 500m SIN Grid V002 version: 2.0"
        )

    LPCLOUD_VNP13C2_V20 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_VNP13C2_2.0",
            provider="LPCLOUD", 
            shortname="VNP13C2",
            version="2.0",
            description="VIIRS/NPP Vegetation Indices Monthly L3 Global 0.05Deg CMG V002 version: 2.0"
        )

    LPCLOUD_VNP13A3_V20 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_VNP13A3_2.0",
            provider="LPCLOUD", 
            shortname="VNP13A3",
            version="2.0",
            description="VIIRS/NPP Vegetation Indices Monthly L3 Global 1km SIN Grid V002 version: 2.0"
        )

    LPCLOUD_VNP28C2_V20 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_VNP28C2_2.0",
            provider="LPCLOUD", 
            shortname="VNP28C2",
            version="2.0",
            description="VIIRS/NPP Water Reservoir Area 8-day L3 Global V002 version: 2.0"
        )

    LPCLOUD_VNP28C3_V20 = DataCollectionDefinition(
            api_id="CMR",
            collections="LPCLOUD_VNP28C3_2.0",
            provider="LPCLOUD", 
            shortname="VNP28C3",
            version="2.0",
            description="VIIRS/NPP Water Reservoir Monthly L3 Global V002 version: 2.0"
        )

