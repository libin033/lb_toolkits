# -*- coding:utf-8 -*-

from lb_toolkits.DataCollections.DataCollectionDefinition import DataCollectionDefinition 

class DataCollectionEUMDAC : 
    GLOBAL_L3C_AVHRR_SEA_SURFACE_TEMPERATURE_GHRSST_METOP_EUMDAC = DataCollectionDefinition(
            api_id="EUMDAC",
            collections="EUMDAC_GLOBAL_L3C_AVHRR_SEA_SURFACE_TEMPERATURE_GHRSST_METOP_EUMDAC",
            provider="EUMDAC", 
            shortname="EO:EUM:DAT:METOP:GLB-SST-NC",
            description="Global L3C AVHRR Sea Surface Temperature (GHRSST) - Metop"
        )

    CLOUD_MASK_MSG_INDIAN_OCEAN_EUMDAC = DataCollectionDefinition(
            api_id="EUMDAC",
            collections="EUMDAC_CLOUD_MASK_MSG_INDIAN_OCEAN_EUMDAC",
            provider="EUMDAC", 
            shortname="EO:EUM:DAT:MSG:CLM-IODC",
            description="Cloud Mask - MSG - Indian Ocean"
        )

    CLOUD_MASK_MSG_0_DEGREE_EUMDAC = DataCollectionDefinition(
            api_id="EUMDAC",
            collections="EUMDAC_CLOUD_MASK_MSG_0_DEGREE_EUMDAC",
            provider="EUMDAC", 
            shortname="EO:EUM:DAT:MSG:CLM",
            description="Cloud Mask - MSG - 0 degree"
        )

    POSEIDON_4_LEVEL_2P_WIND_WAVE_PRODUCTS_LOW_RESOLUTION_IN_NRT_SENTINEL_6_EUMDAC = DataCollectionDefinition(
            api_id="EUMDAC",
            collections="EUMDAC_POSEIDON_4_LEVEL_2P_WIND_WAVE_PRODUCTS_LOW_RESOLUTION_IN_NRT_SENTINEL_6_EUMDAC",
            provider="EUMDAC", 
            shortname="EO:EUM:DAT:0142",
            description="Poseidon-4 Level 2P Wind/Wave Products Low Resolution in NRT - Sentinel-6"
        )

    POSEIDON_4_LEVEL_3_WIND_WAVE_PRODUCTS_LOW_RESOLUTION_IN_NRT_SENTINEL_6_EUMDAC = DataCollectionDefinition(
            api_id="EUMDAC",
            collections="EUMDAC_POSEIDON_4_LEVEL_3_WIND_WAVE_PRODUCTS_LOW_RESOLUTION_IN_NRT_SENTINEL_6_EUMDAC",
            provider="EUMDAC", 
            shortname="EO:EUM:DAT:0143",
            description="Poseidon-4 Level 3 Wind/Wave Products Low Resolution in NRT - Sentinel-6"
        )

    COMMERCIAL_RADIO_OCCULTATION_LEVEL_1B_DATA_MULTIMISSION_EUMDAC = DataCollectionDefinition(
            api_id="EUMDAC",
            collections="EUMDAC_COMMERCIAL_RADIO_OCCULTATION_LEVEL_1B_DATA_MULTIMISSION_EUMDAC",
            provider="EUMDAC", 
            shortname="EO:EUM:DAT:0374",
            description="Commercial Radio Occultation Level 1B data - Multimission"
        )

    SRAL_LEVEL_1B_SENTINEL_3_EUMDAC = DataCollectionDefinition(
            api_id="EUMDAC",
            collections="EUMDAC_SRAL_LEVEL_1B_SENTINEL_3_EUMDAC",
            provider="EUMDAC", 
            shortname="EO:EUM:DAT:0406",
            description="SRAL Level 1B - Sentinel-3"
        )

    OLCI_LEVEL_2_OCEAN_COLOUR_FULL_RESOLUTION_SENTINEL_3_EUMDAC = DataCollectionDefinition(
            api_id="EUMDAC",
            collections="EUMDAC_OLCI_LEVEL_2_OCEAN_COLOUR_FULL_RESOLUTION_SENTINEL_3_EUMDAC",
            provider="EUMDAC", 
            shortname="EO:EUM:DAT:0407",
            description="OLCI Level 2 Ocean Colour Full Resolution - Sentinel-3"
        )

    OLCI_LEVEL_2_OCEAN_COLOUR_REDUCED_RESOLUTION_SENTINEL_3_EUMDAC = DataCollectionDefinition(
            api_id="EUMDAC",
            collections="EUMDAC_OLCI_LEVEL_2_OCEAN_COLOUR_REDUCED_RESOLUTION_SENTINEL_3_EUMDAC",
            provider="EUMDAC", 
            shortname="EO:EUM:DAT:0408",
            description="OLCI Level 2 Ocean Colour Reduced Resolution - Sentinel-3"
        )

    OLCI_LEVEL_1B_FULL_RESOLUTION_SENTINEL_3_EUMDAC = DataCollectionDefinition(
            api_id="EUMDAC",
            collections="EUMDAC_OLCI_LEVEL_1B_FULL_RESOLUTION_SENTINEL_3_EUMDAC",
            provider="EUMDAC", 
            shortname="EO:EUM:DAT:0409",
            description="OLCI Level 1B Full Resolution - Sentinel-3"
        )

    OLCI_LEVEL_1B_REDUCED_RESOLUTION_SENTINEL_3_EUMDAC = DataCollectionDefinition(
            api_id="EUMDAC",
            collections="EUMDAC_OLCI_LEVEL_1B_REDUCED_RESOLUTION_SENTINEL_3_EUMDAC",
            provider="EUMDAC", 
            shortname="EO:EUM:DAT:0410",
            description="OLCI Level 1B Reduced Resolution - Sentinel-3"
        )

    SLSTR_LEVEL_1B_RADIANCES_AND_BRIGHTNESS_TEMPERATURES_SENTINEL_3_EUMDAC = DataCollectionDefinition(
            api_id="EUMDAC",
            collections="EUMDAC_SLSTR_LEVEL_1B_RADIANCES_AND_BRIGHTNESS_TEMPERATURES_SENTINEL_3_EUMDAC",
            provider="EUMDAC", 
            shortname="EO:EUM:DAT:0411",
            description="SLSTR Level 1B Radiances and Brightness Temperatures - Sentinel-3"
        )

    SLSTR_LEVEL_2_SEA_SURFACE_TEMPERATURE_SST_SENTINEL_3_EUMDAC = DataCollectionDefinition(
            api_id="EUMDAC",
            collections="EUMDAC_SLSTR_LEVEL_2_SEA_SURFACE_TEMPERATURE_SST_SENTINEL_3_EUMDAC",
            provider="EUMDAC", 
            shortname="EO:EUM:DAT:0412",
            description="SLSTR Level 2 Sea Surface Temperature (SST) - Sentinel-3"
        )

    SRAL_LEVEL_1A_UNPACKED_L0_COMPLEX_ECHOS_SENTINEL_3_EUMDAC = DataCollectionDefinition(
            api_id="EUMDAC",
            collections="EUMDAC_SRAL_LEVEL_1A_UNPACKED_L0_COMPLEX_ECHOS_SENTINEL_3_EUMDAC",
            provider="EUMDAC", 
            shortname="EO:EUM:DAT:0413",
            description="SRAL Level 1A Unpacked L0 Complex echos - Sentinel-3"
        )

    SRAL_LEVEL_1B_STACK_ECHOES_SENTINEL_3_EUMDAC = DataCollectionDefinition(
            api_id="EUMDAC",
            collections="EUMDAC_SRAL_LEVEL_1B_STACK_ECHOES_SENTINEL_3_EUMDAC",
            provider="EUMDAC", 
            shortname="EO:EUM:DAT:0414",
            description="SRAL Level 1B stack echoes - Sentinel-3"
        )

    SRAL_LEVEL_2_ALTIMETRY_GLOBAL_SENTINEL_3_EUMDAC = DataCollectionDefinition(
            api_id="EUMDAC",
            collections="EUMDAC_SRAL_LEVEL_2_ALTIMETRY_GLOBAL_SENTINEL_3_EUMDAC",
            provider="EUMDAC", 
            shortname="EO:EUM:DAT:0415",
            description="SRAL Level 2 Altimetry Global - Sentinel-3"
        )

    SLSTR_LEVEL_2_AEROSOL_OPTICAL_DEPTH_SENTINEL_3_EUMDAC = DataCollectionDefinition(
            api_id="EUMDAC",
            collections="EUMDAC_SLSTR_LEVEL_2_AEROSOL_OPTICAL_DEPTH_SENTINEL_3_EUMDAC",
            provider="EUMDAC", 
            shortname="EO:EUM:DAT:0416",
            description="SLSTR Level 2 Aerosol Optical Depth - Sentinel-3"
        )

    SLSTR_LEVEL_2_FIRE_RADIATIVE_POWER_SENTINEL_3_EUMDAC = DataCollectionDefinition(
            api_id="EUMDAC",
            collections="EUMDAC_SLSTR_LEVEL_2_FIRE_RADIATIVE_POWER_SENTINEL_3_EUMDAC",
            provider="EUMDAC", 
            shortname="EO:EUM:DAT:0417",
            description="SLSTR Level 2 Fire Radiative Power - Sentinel 3"
        )

    ATMOSPHERIC_MOTION_VECTORS_NETCDF_MTG_0_DEGREE_EUMDAC = DataCollectionDefinition(
            api_id="EUMDAC",
            collections="EUMDAC_ATMOSPHERIC_MOTION_VECTORS_NETCDF_MTG_0_DEGREE_EUMDAC",
            provider="EUMDAC", 
            shortname="EO:EUM:DAT:0676",
            description="Atmospheric Motion Vectors (netCDF) - MTG - 0 degree"
        )

    POSEIDON_4_LEVEL_3_ALTIMETRY_LOW_RESOLUTION_IN_NTC_SENTINEL_6_EUMDAC = DataCollectionDefinition(
            api_id="EUMDAC",
            collections="EUMDAC_POSEIDON_4_LEVEL_3_ALTIMETRY_LOW_RESOLUTION_IN_NTC_SENTINEL_6_EUMDAC",
            provider="EUMDAC", 
            shortname="EO:EUM:DAT:0601",
            description="Poseidon-4 Level 3 Altimetry Low Resolution in NTC - Sentinel-6"
        )

    ALL_SKY_RADIANCE_NETCDF_MTG_0_DEGREE_EUMDAC = DataCollectionDefinition(
            api_id="EUMDAC",
            collections="EUMDAC_ALL_SKY_RADIANCE_NETCDF_MTG_0_DEGREE_EUMDAC",
            provider="EUMDAC", 
            shortname="EO:EUM:DAT:0677",
            description="All Sky Radiance (netCDF) - MTG - 0 degree"
        )

    CLOUD_MASK_MTG_0_DEGREE_EUMDAC = DataCollectionDefinition(
            api_id="EUMDAC",
            collections="EUMDAC_CLOUD_MASK_MTG_0_DEGREE_EUMDAC",
            provider="EUMDAC", 
            shortname="EO:EUM:DAT:0678",
            description="Cloud Mask - MTG - 0 degree"
        )

    GLOBAL_INSTABILITY_INDICES_MTG_0_DEGREE_EUMDAC = DataCollectionDefinition(
            api_id="EUMDAC",
            collections="EUMDAC_GLOBAL_INSTABILITY_INDICES_MTG_0_DEGREE_EUMDAC",
            provider="EUMDAC", 
            shortname="EO:EUM:DAT:0683",
            description="Global Instability Indices - MTG - 0 degree"
        )

    OPTIMAL_CLOUD_ANALYSIS_MTG_0_DEGREE_EUMDAC = DataCollectionDefinition(
            api_id="EUMDAC",
            collections="EUMDAC_OPTIMAL_CLOUD_ANALYSIS_MTG_0_DEGREE_EUMDAC",
            provider="EUMDAC", 
            shortname="EO:EUM:DAT:0684",
            description="Optimal Cloud Analysis - MTG - 0 degree"
        )

    OUTGOING_LW_RADIATION_AT_TOA_MTG_0_DEGREE_EUMDAC = DataCollectionDefinition(
            api_id="EUMDAC",
            collections="EUMDAC_OUTGOING_LW_RADIATION_AT_TOA_MTG_0_DEGREE_EUMDAC",
            provider="EUMDAC", 
            shortname="EO:EUM:DAT:0685",
            description="Outgoing LW radiation at TOA - MTG - 0 degree"
        )

    LI_ACCUMULATED_FLASHES_MTG_0_DEGREE_EUMDAC = DataCollectionDefinition(
            api_id="EUMDAC",
            collections="EUMDAC_LI_ACCUMULATED_FLASHES_MTG_0_DEGREE_EUMDAC",
            provider="EUMDAC", 
            shortname="EO:EUM:DAT:0686",
            description="LI Accumulated Flashes - MTG - 0 degree"
        )

    LI_LIGHTNING_EVENTS_FILTERED_MTG_0_DEGREE_EUMDAC = DataCollectionDefinition(
            api_id="EUMDAC",
            collections="EUMDAC_LI_LIGHTNING_EVENTS_FILTERED_MTG_0_DEGREE_EUMDAC",
            provider="EUMDAC", 
            shortname="EO:EUM:DAT:0690",
            description="LI Lightning Events Filtered - MTG - 0 degree"
        )

    LI_LIGHTNING_FLASHES_MTG_0_DEGREE_EUMDAC = DataCollectionDefinition(
            api_id="EUMDAC",
            collections="EUMDAC_LI_LIGHTNING_FLASHES_MTG_0_DEGREE_EUMDAC",
            provider="EUMDAC", 
            shortname="EO:EUM:DAT:0691",
            description="LI Lightning Flashes - MTG - 0 degree"
        )

    LI_LIGHTNING_GROUPS_MTG_0_DEGREE_EUMDAC = DataCollectionDefinition(
            api_id="EUMDAC",
            collections="EUMDAC_LI_LIGHTNING_GROUPS_MTG_0_DEGREE_EUMDAC",
            provider="EUMDAC", 
            shortname="EO:EUM:DAT:0782",
            description="LI Lightning Groups - MTG - 0 degree"
        )

    ALL_SKY_RADIANCE_BUFR_MTG_0_DEGREE_EUMDAC = DataCollectionDefinition(
            api_id="EUMDAC",
            collections="EUMDAC_ALL_SKY_RADIANCE_BUFR_MTG_0_DEGREE_EUMDAC",
            provider="EUMDAC", 
            shortname="EO:EUM:DAT:0799",
            description="All Sky Radiance (BUFR) - MTG - 0 degree"
        )

    POSEIDON_4_LEVEL_3_ALTIMETRY_HIGH_RESOLUTION_SENTINEL_6_EUMDAC = DataCollectionDefinition(
            api_id="EUMDAC",
            collections="EUMDAC_POSEIDON_4_LEVEL_3_ALTIMETRY_HIGH_RESOLUTION_SENTINEL_6_EUMDAC",
            provider="EUMDAC", 
            shortname="EO:EUM:DAT:0859",
            description="Poseidon-4 Level 3 Altimetry High Resolution - Sentinel-6"
        )

    POSEIDON_4_ALTIMETRY_LEVEL_1A_HIGH_RESOLUTION_SENTINEL_6_EUMDAC = DataCollectionDefinition(
            api_id="EUMDAC",
            collections="EUMDAC_POSEIDON_4_ALTIMETRY_LEVEL_1A_HIGH_RESOLUTION_SENTINEL_6_EUMDAC",
            provider="EUMDAC", 
            shortname="EO:EUM:DAT:0850",
            description="Poseidon-4 Altimetry Level 1A High Resolution - Sentinel-6"
        )

    POSEIDON_4_ALTIMETRY_LEVEL_1B_HIGH_RESOLUTION_SENTINEL_6_EUMDAC = DataCollectionDefinition(
            api_id="EUMDAC",
            collections="EUMDAC_POSEIDON_4_ALTIMETRY_LEVEL_1B_HIGH_RESOLUTION_SENTINEL_6_EUMDAC",
            provider="EUMDAC", 
            shortname="EO:EUM:DAT:0851",
            description="Poseidon-4 Altimetry Level 1B High Resolution - Sentinel-6"
        )

    POSEIDON_4_ALTIMETRY_LEVEL_1B_LOW_RESOLUTION_SENTINEL_6_EUMDAC = DataCollectionDefinition(
            api_id="EUMDAC",
            collections="EUMDAC_POSEIDON_4_ALTIMETRY_LEVEL_1B_LOW_RESOLUTION_SENTINEL_6_EUMDAC",
            provider="EUMDAC", 
            shortname="EO:EUM:DAT:0852",
            description="Poseidon-4 Altimetry Level 1B Low Resolution - Sentinel-6"
        )

    RADIO_OCCULTATION_LEVEL_1B_PRODUCTS_SENTINEL_6_EUMDAC = DataCollectionDefinition(
            api_id="EUMDAC",
            collections="EUMDAC_RADIO_OCCULTATION_LEVEL_1B_PRODUCTS_SENTINEL_6_EUMDAC",
            provider="EUMDAC", 
            shortname="EO:EUM:DAT:0853",
            description="Radio Occultation Level 1B Products - Sentinel-6"
        )

    POSEIDON_4_ALTIMETRY_LEVEL_2_LOW_RESOLUTION_SENTINEL_6_EUMDAC = DataCollectionDefinition(
            api_id="EUMDAC",
            collections="EUMDAC_POSEIDON_4_ALTIMETRY_LEVEL_2_LOW_RESOLUTION_SENTINEL_6_EUMDAC",
            provider="EUMDAC", 
            shortname="EO:EUM:DAT:0854",
            description="Poseidon-4 Altimetry Level 2 Low Resolution - Sentinel-6"
        )

    POSEIDON_4_ALTIMETRY_LEVEL_2_HIGH_RESOLUTION_SENTINEL_6_EUMDAC = DataCollectionDefinition(
            api_id="EUMDAC",
            collections="EUMDAC_POSEIDON_4_ALTIMETRY_LEVEL_2_HIGH_RESOLUTION_SENTINEL_6_EUMDAC",
            provider="EUMDAC", 
            shortname="EO:EUM:DAT:0855",
            description="Poseidon-4 Altimetry Level 2 High Resolution - Sentinel-6"
        )

    CLIMATE_QUALITY_ADVANCED_MICROWAVE_RADIOMETER_LEVEL_2_PRODUCTS_SENTINEL_6_EUMDAC = DataCollectionDefinition(
            api_id="EUMDAC",
            collections="EUMDAC_CLIMATE_QUALITY_ADVANCED_MICROWAVE_RADIOMETER_LEVEL_2_PRODUCTS_SENTINEL_6_EUMDAC",
            provider="EUMDAC", 
            shortname="EO:EUM:DAT:0856",
            description="Climate-quality Advanced Microwave Radiometer Level 2 Products - Sentinel-6"
        )

    POSEIDON_4_ALTIMETRY_LEVEL_2P_LOW_RESOLUTION_SENTINEL_6_EUMDAC = DataCollectionDefinition(
            api_id="EUMDAC",
            collections="EUMDAC_POSEIDON_4_ALTIMETRY_LEVEL_2P_LOW_RESOLUTION_SENTINEL_6_EUMDAC",
            provider="EUMDAC", 
            shortname="EO:EUM:DAT:0857",
            description="Poseidon-4 Altimetry Level 2P Low Resolution - Sentinel-6"
        )

    POSEIDON_4_ALTIMETRY_LEVEL_2P_HIGH_RESOLUTION_SENTINEL_6_EUMDAC = DataCollectionDefinition(
            api_id="EUMDAC",
            collections="EUMDAC_POSEIDON_4_ALTIMETRY_LEVEL_2P_HIGH_RESOLUTION_SENTINEL_6_EUMDAC",
            provider="EUMDAC", 
            shortname="EO:EUM:DAT:0858",
            description="Poseidon-4 Altimetry Level 2P High Resolution - Sentinel-6"
        )

    LI_ACCUMULATED_FLASH_AREA_MTG_0_DEGREE_EUMDAC = DataCollectionDefinition(
            api_id="EUMDAC",
            collections="EUMDAC_LI_ACCUMULATED_FLASH_AREA_MTG_0_DEGREE_EUMDAC",
            provider="EUMDAC", 
            shortname="EO:EUM:DAT:0687",
            description="LI Accumulated Flash Area - MTG - 0 degree"
        )

    LI_ACCUMULATED_FLASH_RADIANCE_MTG_0_DEGREE_EUMDAC = DataCollectionDefinition(
            api_id="EUMDAC",
            collections="EUMDAC_LI_ACCUMULATED_FLASH_RADIANCE_MTG_0_DEGREE_EUMDAC",
            provider="EUMDAC", 
            shortname="EO:EUM:DAT:0688",
            description="LI Accumulated Flash Radiance - MTG - 0 degree"
        )

    ATMOSPHERIC_MOTION_VECTORS_BUFR_MTG_0_DEGREE_EUMDAC = DataCollectionDefinition(
            api_id="EUMDAC",
            collections="EUMDAC_ATMOSPHERIC_MOTION_VECTORS_BUFR_MTG_0_DEGREE_EUMDAC",
            provider="EUMDAC", 
            shortname="EO:EUM:DAT:0998",
            description="Atmospheric Motion Vectors (BUFR) - MTG - 0 degree"
        )

    AMSU_A_LEVEL_1B_METOP_GLOBAL_EUMDAC = DataCollectionDefinition(
            api_id="EUMDAC",
            collections="EUMDAC_AMSU_A_LEVEL_1B_METOP_GLOBAL_EUMDAC",
            provider="EUMDAC", 
            shortname="EO:EUM:DAT:METOP:AMSUL1",
            description="AMSU-A Level 1B - Metop - Global"
        )

    ASCAT_LEVEL_1_SIGMA0_FULL_RESOLUTION_METOP_GLOBAL_EUMDAC = DataCollectionDefinition(
            api_id="EUMDAC",
            collections="EUMDAC_ASCAT_LEVEL_1_SIGMA0_FULL_RESOLUTION_METOP_GLOBAL_EUMDAC",
            provider="EUMDAC", 
            shortname="EO:EUM:DAT:METOP:ASCSZF1B",
            description="ASCAT Level 1 Sigma0 Full Resolution - Metop - Global"
        )

    ASCAT_LEVEL_1_SIGMA0_RESAMPLED_AT_25_KM_SWATH_GRID_METOP_GLOBAL_EUMDAC = DataCollectionDefinition(
            api_id="EUMDAC",
            collections="EUMDAC_ASCAT_LEVEL_1_SIGMA0_RESAMPLED_AT_25_KM_SWATH_GRID_METOP_GLOBAL_EUMDAC",
            provider="EUMDAC", 
            shortname="EO:EUM:DAT:METOP:ASCSZO1B",
            description="ASCAT Level 1 Sigma0 resampled at 25 km Swath Grid - Metop - Global"
        )

    ASCAT_LEVEL_1_SIGMA0_RESAMPLED_AT_125_KM_SWATH_GRID_METOP_GLOBAL_EUMDAC = DataCollectionDefinition(
            api_id="EUMDAC",
            collections="EUMDAC_ASCAT_LEVEL_1_SIGMA0_RESAMPLED_AT_125_KM_SWATH_GRID_METOP_GLOBAL_EUMDAC",
            provider="EUMDAC", 
            shortname="EO:EUM:DAT:METOP:ASCSZR1B",
            description="ASCAT Level 1 Sigma0 resampled at 12.5 km Swath Grid - Metop - Global"
        )

    AVHRR_LEVEL_1B_METOP_GLOBAL_EUMDAC = DataCollectionDefinition(
            api_id="EUMDAC",
            collections="EUMDAC_AVHRR_LEVEL_1B_METOP_GLOBAL_EUMDAC",
            provider="EUMDAC", 
            shortname="EO:EUM:DAT:METOP:AVHRRL1",
            description="AVHRR Level 1B - Metop - Global"
        )

    GOME_2_LEVEL_1B_METOP_GLOBAL_EUMDAC = DataCollectionDefinition(
            api_id="EUMDAC",
            collections="EUMDAC_GOME_2_LEVEL_1B_METOP_GLOBAL_EUMDAC",
            provider="EUMDAC", 
            shortname="EO:EUM:DAT:METOP:GOMEL1",
            description="GOME-2 Level 1B - Metop - Global"
        )

    IASI_LEVEL_1C_ALL_SPECTRAL_SAMPLES_METOP_GLOBAL_EUMDAC = DataCollectionDefinition(
            api_id="EUMDAC",
            collections="EUMDAC_IASI_LEVEL_1C_ALL_SPECTRAL_SAMPLES_METOP_GLOBAL_EUMDAC",
            provider="EUMDAC", 
            shortname="EO:EUM:DAT:METOP:IASIL1C-ALL",
            description="IASI Level 1C - All Spectral Samples - Metop - Global"
        )

    IASI_COMBINED_SOUNDING_PRODUCTS_METOP_EUMDAC = DataCollectionDefinition(
            api_id="EUMDAC",
            collections="EUMDAC_IASI_COMBINED_SOUNDING_PRODUCTS_METOP_EUMDAC",
            provider="EUMDAC", 
            shortname="EO:EUM:DAT:METOP:IASSND02",
            description="IASI Combined Sounding Products - Metop"
        )

    MHS_LEVEL_1B_METOP_GLOBAL_EUMDAC = DataCollectionDefinition(
            api_id="EUMDAC",
            collections="EUMDAC_MHS_LEVEL_1B_METOP_GLOBAL_EUMDAC",
            provider="EUMDAC", 
            shortname="EO:EUM:DAT:METOP:MHSL1",
            description="MHS Level 1B - Metop - Global"
        )

    ASCAT_WINDS_AND_SOIL_MOISTURE_AT_25_KM_SWATH_GRID_METOP_EUMDAC = DataCollectionDefinition(
            api_id="EUMDAC",
            collections="EUMDAC_ASCAT_WINDS_AND_SOIL_MOISTURE_AT_25_KM_SWATH_GRID_METOP_EUMDAC",
            provider="EUMDAC", 
            shortname="EO:EUM:DAT:METOP:OAS025",
            description="ASCAT Winds and Soil Moisture at 25 km Swath Grid - Metop"
        )

    ASCAT_COASTAL_WINDS_AT_125_KM_SWATH_GRID_METOP_EUMDAC = DataCollectionDefinition(
            api_id="EUMDAC",
            collections="EUMDAC_ASCAT_COASTAL_WINDS_AT_125_KM_SWATH_GRID_METOP_EUMDAC",
            provider="EUMDAC", 
            shortname="EO:EUM:DAT:METOP:OSI-104",
            description="ASCAT Coastal Winds at 12.5 km Swath Grid - Metop"
        )

    ASCAT_L2_25_KM_WINDS_DATA_RECORD_RELEASE_1_METOP_EUMDAC = DataCollectionDefinition(
            api_id="EUMDAC",
            collections="EUMDAC_ASCAT_L2_25_KM_WINDS_DATA_RECORD_RELEASE_1_METOP_EUMDAC",
            provider="EUMDAC", 
            shortname="EO:EUM:DAT:METOP:OSI-150-A",
            description="ASCAT L2 25 km Winds Data Record Release 1 - Metop"
        )

    ASCAT_L2_125_KM_WINDS_DATA_RECORD_RELEASE_1_METOP_EUMDAC = DataCollectionDefinition(
            api_id="EUMDAC",
            collections="EUMDAC_ASCAT_L2_125_KM_WINDS_DATA_RECORD_RELEASE_1_METOP_EUMDAC",
            provider="EUMDAC", 
            shortname="EO:EUM:DAT:METOP:OSI-150-B",
            description="ASCAT L2 12.5 km Winds Data Record Release 1 - Metop"
        )

    ASCAT_SOIL_MOISTURE_AT_125_KM_SWATH_GRID_IN_NRT_METOP_EUMDAC = DataCollectionDefinition(
            api_id="EUMDAC",
            collections="EUMDAC_ASCAT_SOIL_MOISTURE_AT_125_KM_SWATH_GRID_IN_NRT_METOP_EUMDAC",
            provider="EUMDAC", 
            shortname="EO:EUM:DAT:METOP:SOMO12",
            description="ASCAT Soil Moisture at 12.5 km Swath Grid in NRT - Metop"
        )

    ASCAT_SOIL_MOISTURE_AT_25_KM_SWATH_GRID_IN_NRT_METOP_EUMDAC = DataCollectionDefinition(
            api_id="EUMDAC",
            collections="EUMDAC_ASCAT_SOIL_MOISTURE_AT_25_KM_SWATH_GRID_IN_NRT_METOP_EUMDAC",
            provider="EUMDAC", 
            shortname="EO:EUM:DAT:METOP:SOMO25",
            description="ASCAT Soil Moisture at 25 km Swath Grid in NRT - Metop"
        )

    HIGH_RATE_SEVIRI_LEVEL_15_IMAGE_DATA_MSG_INDIAN_OCEAN_EUMDAC = DataCollectionDefinition(
            api_id="EUMDAC",
            collections="EUMDAC_HIGH_RATE_SEVIRI_LEVEL_15_IMAGE_DATA_MSG_INDIAN_OCEAN_EUMDAC",
            provider="EUMDAC", 
            shortname="EO:EUM:DAT:MSG:HRSEVIRI-IODC",
            description="High Rate SEVIRI Level 1.5 Image Data - MSG - Indian Ocean"
        )

    HIGH_RATE_SEVIRI_LEVEL_15_IMAGE_DATA_MSG_0_DEGREE_EUMDAC = DataCollectionDefinition(
            api_id="EUMDAC",
            collections="EUMDAC_HIGH_RATE_SEVIRI_LEVEL_15_IMAGE_DATA_MSG_0_DEGREE_EUMDAC",
            provider="EUMDAC", 
            shortname="EO:EUM:DAT:MSG:HRSEVIRI",
            description="High Rate SEVIRI Level 1.5 Image Data - MSG - 0 degree"
        )

    RAPID_SCAN_HIGH_RATE_SEVIRI_LEVEL_15_IMAGE_DATA_MSG_EUMDAC = DataCollectionDefinition(
            api_id="EUMDAC",
            collections="EUMDAC_RAPID_SCAN_HIGH_RATE_SEVIRI_LEVEL_15_IMAGE_DATA_MSG_EUMDAC",
            provider="EUMDAC", 
            shortname="EO:EUM:DAT:MSG:MSG15-RSS",
            description="Rapid Scan High Rate SEVIRI Level 1.5 Image Data - MSG"
        )

    RAPID_SCAN_CLOUD_MASK_MSG_EUMDAC = DataCollectionDefinition(
            api_id="EUMDAC",
            collections="EUMDAC_RAPID_SCAN_CLOUD_MASK_MSG_EUMDAC",
            provider="EUMDAC", 
            shortname="EO:EUM:DAT:MSG:RSS-CLM",
            description="Rapid Scan Cloud Mask - MSG"
        )

    HIRS_LEVEL_1B_METOP_GLOBAL_EUMDAC = DataCollectionDefinition(
            api_id="EUMDAC",
            collections="EUMDAC_HIRS_LEVEL_1B_METOP_GLOBAL_EUMDAC",
            provider="EUMDAC", 
            shortname="EO:EUM:DAT:MULT:HIRSL1",
            description="HIRS Level 1B - Metop - Global"
        )

    RINEX_AUXILIARY_DATA_SENTINEL_6_EUMDAC = DataCollectionDefinition(
            api_id="EUMDAC",
            collections="EUMDAC_RINEX_AUXILIARY_DATA_SENTINEL_6_EUMDAC",
            provider="EUMDAC", 
            shortname="EO:EUM:DAT:0274",
            description="RINEX Auxiliary Data - Sentinel-6"
        )

    IASI_LEVEL_1_PRINCIPAL_COMPONENT_SCORES_METOP_GLOBAL_EUMDAC = DataCollectionDefinition(
            api_id="EUMDAC",
            collections="EUMDAC_IASI_LEVEL_1_PRINCIPAL_COMPONENT_SCORES_METOP_GLOBAL_EUMDAC",
            provider="EUMDAC", 
            shortname="EO:EUM:DAT:METOP:IASPCS01",
            description="IASI Level 1 Principal Component Scores - Metop - Global"
        )

    CLOUD_TOP_HEIGHT_MSG_INDIAN_OCEAN_EUMDAC = DataCollectionDefinition(
            api_id="EUMDAC",
            collections="EUMDAC_CLOUD_TOP_HEIGHT_MSG_INDIAN_OCEAN_EUMDAC",
            provider="EUMDAC", 
            shortname="EO:EUM:DAT:MSG:CTH-IODC",
            description="Cloud Top Height - MSG - Indian Ocean"
        )

    CLOUD_TOP_HEIGHT_MSG_0_DEGREE_EUMDAC = DataCollectionDefinition(
            api_id="EUMDAC",
            collections="EUMDAC_CLOUD_TOP_HEIGHT_MSG_0_DEGREE_EUMDAC",
            provider="EUMDAC", 
            shortname="EO:EUM:DAT:MSG:CTH",
            description="Cloud Top Height - MSG - 0 degree"
        )

    FCI_LEVEL_1C_NORMAL_RESOLUTION_IMAGE_DATA_MTG_0_DEGREE_EUMDAC = DataCollectionDefinition(
            api_id="EUMDAC",
            collections="EUMDAC_FCI_LEVEL_1C_NORMAL_RESOLUTION_IMAGE_DATA_MTG_0_DEGREE_EUMDAC",
            provider="EUMDAC", 
            shortname="EO:EUM:DAT:0662",
            description="FCI Level 1c Normal Resolution Image Data - MTG - 0 degree"
        )

    FCI_LEVEL_1C_HIGH_RESOLUTION_IMAGE_DATA_MTG_0_DEGREE_EUMDAC = DataCollectionDefinition(
            api_id="EUMDAC",
            collections="EUMDAC_FCI_LEVEL_1C_HIGH_RESOLUTION_IMAGE_DATA_MTG_0_DEGREE_EUMDAC",
            provider="EUMDAC", 
            shortname="EO:EUM:DAT:0665",
            description="FCI Level 1c High Resolution Image Data - MTG - 0 degree"
        )

