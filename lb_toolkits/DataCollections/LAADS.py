# -*- coding:utf-8 -*-

from lb_toolkits.DataCollections.DataCollectionDefinition import DataCollectionDefinition 

class DataCollectionLAADS : 
    XAERDT_L2_ABI_G16_V1_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_XAERDT_L2_ABI_G16_1",
            provider="LAADS", 
            shortname="XAERDT_L2_ABI_G16",
            version="1",
            description="ABI/GOES-16 Dark Target Aerosol 10-Min L2 Full Disk 10 km version: 1"
        )

    XAERDT_L2_ABI_G17_V1_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_XAERDT_L2_ABI_G17_1",
            provider="LAADS", 
            shortname="XAERDT_L2_ABI_G17",
            version="1",
            description="ABI/GOES-17 Dark Target Aerosol 10-Min L2 Full Disk 10 km version: 1"
        )

    XAERDT_L2_AHI_H08_V1_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_XAERDT_L2_AHI_H08_1",
            provider="LAADS", 
            shortname="XAERDT_L2_AHI_H08",
            version="1",
            description="AHI/Himawari-08 Dark Target Aerosol 10-Min L2 Full Disk 10 km version: 1"
        )

    XAERDT_L2_AHI_H09_V1_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_XAERDT_L2_AHI_H09_1",
            provider="LAADS", 
            shortname="XAERDT_L2_AHI_H09",
            version="1",
            description="AHI/Himawari-09 Dark Target Aerosol 10-Min L2 Full Disk 10 km version: 1"
        )

    EMASL1B_V1_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_eMASL1B_1",
            provider="LAADS", 
            shortname="eMASL1B",
            version="1",
            description="Enhanced MODIS Airborne Simulator (eMAS) Calibrated, Geolocated Radiances L1B 50m Data version: 1"
        )

    EMASL2AER_V1_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_eMASL2AER_1",
            provider="LAADS", 
            shortname="eMASL2AER",
            version="1",
            description="Enhanced MODIS Airborne Simulator (eMAS) L2 Aerosol Data version: 1"
        )

    EMASL2CLD_V1_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_eMASL2CLD_1",
            provider="LAADS", 
            shortname="eMASL2CLD",
            version="1",
            description="Enhanced MODIS Airborne Simulator (eMAS) L2 Cloud Data version: 1"
        )

    EN1_MDSI_MER_FRS_1P_V4_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_EN1_MDSI_MER_FRS_1P_4",
            provider="LAADS", 
            shortname="EN1_MDSI_MER_FRS_1P",
            version="4",
            description="Full Resolution Full Swath Geolocated and Calibrated TOA Radiance version: 4"
        )

    EN1_MDSI_MER_FRS_2P_V4_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_EN1_MDSI_MER_FRS_2P_4",
            provider="LAADS", 
            shortname="EN1_MDSI_MER_FRS_2P",
            version="4",
            description="Full Resolution Full Swath Geophysical Product for Ocean, Land and Atmosphere version: 4"
        )

    M1_AVH13C1_V6_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_M1_AVH13C1_6",
            provider="LAADS", 
            shortname="M1_AVH13C1",
            version="6",
            description="METOP-B AVHRR Atmospherically Corrected Normalized Difference Vegetation Index Daily L3 Global 0.05 Deg. CMG version: 6"
        )

    M1_AVH09C1_V6_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_M1_AVH09C1_6",
            provider="LAADS", 
            shortname="M1_AVH09C1",
            version="6",
            description="METOP-B AVHRR Atmospherically Corrected Surface Reflectance Daily L3 Global 0.05 Deg CMG version: 6"
        )

    M1_AVH02C1_V6_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_M1_AVH02C1_6",
            provider="LAADS", 
            shortname="M1_AVH02C1",
            version="6",
            description="METOP-B AVHRR Top-of-Atmosphere Reflectance Daily L3 Global 0.05 Deg. CMG version: 6"
        )

    MCD06COSP_D3_MODIS_V62_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_MCD06COSP_D3_MODIS_6.2",
            provider="LAADS", 
            shortname="MCD06COSP_D3_MODIS",
            version="6.2",
            description="MODIS (Aqua/Terra) Cloud Properties Level 3 daily, 1x1 degree grid version: 6.2"
        )

    MCD06COSP_M3_MODIS_V62_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_MCD06COSP_M3_MODIS_6.2",
            provider="LAADS", 
            shortname="MCD06COSP_M3_MODIS",
            version="6.2",
            description="MODIS (Aqua/Terra) Cloud Properties Level 3 monthly, 1x1 degree grid version: 6.2"
        )

    MASL1B_V1_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_MASL1B_1",
            provider="LAADS", 
            shortname="MASL1B",
            version="1",
            description="MODIS Airborne Simulator (MAS) Calibrated, Geolocated Radiances L1B 50m Data version: 1"
        )

    MASL2CLD_V1_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_MASL2CLD_1",
            provider="LAADS", 
            shortname="MASL2CLD",
            version="1",
            description="MODIS Airborne Simulator (MAS) L2 Cloud Data version: 1"
        )

    MYDCSR_B_V61_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_MYDCSR_B_6.1",
            provider="LAADS", 
            shortname="MYDCSR_B",
            version="6.1",
            description="MODIS/Aqua 8-Day Clear Sky Radiance Bias Daily L3 Global 1Deg Zonal Bands version: 6.1"
        )

    MYD04_L2_V61_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_MYD04_L2_6.1",
            provider="LAADS", 
            shortname="MYD04_L2",
            version="6.1",
            description="MODIS/Aqua Aerosol 5-Min L2 Swath 10km version: 6.1"
        )

    MYD04_3K_V61_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_MYD04_3K_6.1",
            provider="LAADS", 
            shortname="MYD04_3K",
            version="6.1",
            description="MODIS/Aqua Aerosol 5-Min L2 Swath 3km version: 6.1"
        )

    MYD08_E3_V61_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_MYD08_E3_6.1",
            provider="LAADS", 
            shortname="MYD08_E3",
            version="6.1",
            description="MODIS/Aqua Aerosol Cloud Water Vapor Ozone 8-Day L3 Global 1Deg CMG version: 6.1"
        )

    MYD08_D3_V61_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_MYD08_D3_6.1",
            provider="LAADS", 
            shortname="MYD08_D3",
            version="6.1",
            description="MODIS/Aqua Aerosol Cloud Water Vapor Ozone Daily L3 Global 1Deg CMG version: 6.1"
        )

    MYD08_M3_V61_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_MYD08_M3_6.1",
            provider="LAADS", 
            shortname="MYD08_M3",
            version="6.1",
            description="MODIS/Aqua Aerosol Cloud Water Vapor Ozone Monthly L3 Global 1Deg CMG version: 6.1"
        )

    MYDATML2_V61_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_MYDATML2_6.1",
            provider="LAADS", 
            shortname="MYDATML2",
            version="6.1",
            description="MODIS/Aqua Aerosol, Cloud and Water Vapor Subset 5-Min L2 Swath 5km and 10km version: 6.1"
        )

    MYDARNSS_V61_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_MYDARNSS_6.1",
            provider="LAADS", 
            shortname="MYDARNSS",
            version="6.1",
            description="MODIS/Aqua Atmosphere Aeronet Subsetting Product version: 6.1"
        )

    MYDBMSS_V61_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_MYDBMSS_6.1",
            provider="LAADS", 
            shortname="MYDBMSS",
            version="6.1",
            description="MODIS/Aqua Atmosphere BELMANIP Subsetting Product version: 6.1"
        )

    MYDFNSS_V61_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_MYDFNSS_6.1",
            provider="LAADS", 
            shortname="MYDFNSS",
            version="6.1",
            description="MODIS/Aqua Atmosphere FluxNet Subsetting Product version: 6.1"
        )

    MYD09_V61_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_MYD09_6.1",
            provider="LAADS", 
            shortname="MYD09",
            version="6.1",
            description="MODIS/Aqua Atmospherically Corrected Surface Reflectance 5-Min L2 Swath 250m, 500m, and 1km version: 6.1"
        )

    MYD021KM_V61_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_MYD021KM_6.1",
            provider="LAADS", 
            shortname="MYD021KM",
            version="6.1",
            description="MODIS/Aqua Calibrated Radiances 5-Min L1B Swath 1km version: 6.1"
        )

    MYD02QKM_V61_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_MYD02QKM_6.1",
            provider="LAADS", 
            shortname="MYD02QKM",
            version="6.1",
            description="MODIS/Aqua Calibrated Radiances 5-Min L1B Swath 250m version: 6.1"
        )

    MYD02HKM_V61_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_MYD02HKM_6.1",
            provider="LAADS", 
            shortname="MYD02HKM",
            version="6.1",
            description="MODIS/Aqua Calibrated Radiances 5-Min L1B Swath 500m version: 6.1"
        )

    MYDCSR_8_V61_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_MYDCSR_8_6.1",
            provider="LAADS", 
            shortname="MYDCSR_8",
            version="6.1",
            description="MODIS/Aqua Clear Sky Radiance 8-Day Composite Daily L3 Global 25km Equal Area version: 6.1"
        )

    CLDMSK_L2_MODIS_AQUA_V1_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_CLDMSK_L2_MODIS_Aqua_1",
            provider="LAADS", 
            shortname="CLDMSK_L2_MODIS_Aqua",
            version="1",
            description="MODIS/Aqua Cloud Mask 5-Min Swath 1000 m version: 1"
        )

    MYD35_L2_V61_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_MYD35_L2_6.1",
            provider="LAADS", 
            shortname="MYD35_L2",
            version="6.1",
            description="MODIS/Aqua Cloud Mask and Spectral Test Results 5-Min L2 Swath 250m and 1km version: 6.1"
        )

    CLDPROP_L2_MODIS_AQUA_V11_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_CLDPROP_L2_MODIS_Aqua_1.1",
            provider="LAADS", 
            shortname="CLDPROP_L2_MODIS_Aqua",
            version="1.1",
            description="MODIS/Aqua Cloud Properties 5-min L2 Swath 1km version: 1.1"
        )

    CLDPROPCOSP_D3_MODIS_AQUA_V11_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_CLDPROPCOSP_D3_MODIS_Aqua_1.1",
            provider="LAADS", 
            shortname="CLDPROPCOSP_D3_MODIS_Aqua",
            version="1.1",
            description="MODIS/Aqua Cloud Properties COSP Level 3 daily, 1x1 deg. grid version: 1.1"
        )

    CLDPROPCOSP_M3_MODIS_AQUA_V11_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_CLDPROPCOSP_M3_MODIS_Aqua_1.1",
            provider="LAADS", 
            shortname="CLDPROPCOSP_M3_MODIS_Aqua",
            version="1.1",
            description="MODIS/Aqua Cloud Properties COSP Level 3 monthly, 1x1 deg. grid version: 1.1"
        )

    CLDPROP_D3_MODIS_AQUA_V11_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_CLDPROP_D3_MODIS_Aqua_1.1",
            provider="LAADS", 
            shortname="CLDPROP_D3_MODIS_Aqua",
            version="1.1",
            description="MODIS/Aqua Cloud Properties Level 3 daily, 1x1 degree grid version: 1.1"
        )

    CLDPROP_M3_MODIS_AQUA_V11_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_CLDPROP_M3_MODIS_Aqua_1.1",
            provider="LAADS", 
            shortname="CLDPROP_M3_MODIS_Aqua",
            version="1.1",
            description="MODIS/Aqua Cloud Properties Level 3 monthly, 1x1 degree grid version: 1.1"
        )

    MYD06_L2_V61_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_MYD06_L2_6.1",
            provider="LAADS", 
            shortname="MYD06_L2",
            version="6.1",
            description="MODIS/Aqua Clouds 5-Min L2 Swath 1km and 5km version: 6.1"
        )

    XAERDT_L2_MODIS_AQUA_V1_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_XAERDT_L2_MODIS_Aqua_1",
            provider="LAADS", 
            shortname="XAERDT_L2_MODIS_Aqua",
            version="1",
            description="MODIS/Aqua Dark Target Aerosol 5-Min L2 Swath 10 km version: 1"
        )

    MYD03_V61_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_MYD03_6.1",
            provider="LAADS", 
            shortname="MYD03",
            version="6.1",
            description="MODIS/Aqua Geolocation Fields 5-Min L1A Swath 1km version: 6.1"
        )

    MYD02SSH_V61_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_MYD02SSH_6.1",
            provider="LAADS", 
            shortname="MYD02SSH",
            version="6.1",
            description="MODIS/Aqua Level 1B Subsampled Calibrated Radiance 5Km version: 6.1"
        )

    MYD01_V61_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_MYD01_6.1",
            provider="LAADS", 
            shortname="MYD01",
            version="6.1",
            description="MODIS/Aqua Raw Radiances in Counts 5-Min L1A Swath version: 6.1"
        )

    MYD07_L2_V61_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_MYD07_L2_6.1",
            provider="LAADS", 
            shortname="MYD07_L2",
            version="6.1",
            description="MODIS/Aqua Temperature and Water Vapor Profiles 5-Min L2 Swath 5km version: 6.1"
        )

    MYD05_L2_V61_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_MYD05_L2_6.1",
            provider="LAADS", 
            shortname="MYD05_L2",
            version="6.1",
            description="MODIS/Aqua Total Precipitable Water Vapor 5-Min L2 Swath 1km and 5km version: 6.1"
        )

    MODCSR_B_V61_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_MODCSR_B_6.1",
            provider="LAADS", 
            shortname="MODCSR_B",
            version="6.1",
            description="MODIS/Terra 8-Day Clear Sky Radiance Bias Daily L3 Global 1Deg Zonal Bands version: 6.1"
        )

    MOD04_L2_V61_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_MOD04_L2_6.1",
            provider="LAADS", 
            shortname="MOD04_L2",
            version="6.1",
            description="MODIS/Terra Aerosol 5-Min L2 Swath 10km version: 6.1"
        )

    MOD04_3K_V61_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_MOD04_3K_6.1",
            provider="LAADS", 
            shortname="MOD04_3K",
            version="6.1",
            description="MODIS/Terra Aerosol 5-Min L2 Swath 3km version: 6.1"
        )

    MOD08_E3_V61_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_MOD08_E3_6.1",
            provider="LAADS", 
            shortname="MOD08_E3",
            version="6.1",
            description="MODIS/Terra Aerosol Cloud Water Vapor Ozone 8-Day L3 Global 1Deg CMG version: 6.1"
        )

    MOD08_D3_V61_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_MOD08_D3_6.1",
            provider="LAADS", 
            shortname="MOD08_D3",
            version="6.1",
            description="MODIS/Terra Aerosol Cloud Water Vapor Ozone Daily L3 Global 1Deg CMG version: 6.1"
        )

    MOD08_M3_V61_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_MOD08_M3_6.1",
            provider="LAADS", 
            shortname="MOD08_M3",
            version="6.1",
            description="MODIS/Terra Aerosol Cloud Water Vapor Ozone Monthly L3 Global 1Deg CMG version: 6.1"
        )

    MODATML2_V61_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_MODATML2_6.1",
            provider="LAADS", 
            shortname="MODATML2",
            version="6.1",
            description="MODIS/Terra Aerosol, Cloud and Water Vapor Subset 5-Min L2 Swath 5km and 10km version: 6.1"
        )

    MODARNSS_V61_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_MODARNSS_6.1",
            provider="LAADS", 
            shortname="MODARNSS",
            version="6.1",
            description="MODIS/Terra Atmosphere Aeronet Subsetting Product version: 6.1"
        )

    MODBMSS_V61_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_MODBMSS_6.1",
            provider="LAADS", 
            shortname="MODBMSS",
            version="6.1",
            description="MODIS/Terra Atmosphere BELMANIP Subsetting Product version: 6.1"
        )

    MODFNSS_V61_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_MODFNSS_6.1",
            provider="LAADS", 
            shortname="MODFNSS",
            version="6.1",
            description="MODIS/Terra Atmosphere FluxNet Subsetting Product version: 6.1"
        )

    MOD09_V61_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_MOD09_6.1",
            provider="LAADS", 
            shortname="MOD09",
            version="6.1",
            description="MODIS/Terra Atmospherically Corrected Surface Reflectance 5-Min L2 Swath 250m, 500m, 1km version: 6.1"
        )

    MOD021KM_V61_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_MOD021KM_6.1",
            provider="LAADS", 
            shortname="MOD021KM",
            version="6.1",
            description="MODIS/Terra Calibrated Radiances 5-Min L1B Swath 1km version: 6.1"
        )

    MOD02QKM_V61_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_MOD02QKM_6.1",
            provider="LAADS", 
            shortname="MOD02QKM",
            version="6.1",
            description="MODIS/Terra Calibrated Radiances 5-Min L1B Swath 250m version: 6.1"
        )

    MOD02HKM_V61_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_MOD02HKM_6.1",
            provider="LAADS", 
            shortname="MOD02HKM",
            version="6.1",
            description="MODIS/Terra Calibrated Radiances 5-Min L1B Swath 500m version: 6.1"
        )

    MODCSR_8_V61_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_MODCSR_8_6.1",
            provider="LAADS", 
            shortname="MODCSR_8",
            version="6.1",
            description="MODIS/Terra Clear Sky Radiance 8-Day Composite Daily L3 Global 25km Equal Area version: 6.1"
        )

    MOD35_L2_V61_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_MOD35_L2_6.1",
            provider="LAADS", 
            shortname="MOD35_L2",
            version="6.1",
            description="MODIS/Terra Cloud Mask and Spectral Test Results 5-Min L2 Swath 250m and 1km version: 6.1"
        )

    MOD06_L2_V61_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_MOD06_L2_6.1",
            provider="LAADS", 
            shortname="MOD06_L2",
            version="6.1",
            description="MODIS/Terra Clouds 5-Min L2 Swath 1km and 5km version: 6.1"
        )

    XAERDT_L2_MODIS_TERRA_V1_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_XAERDT_L2_MODIS_Terra_1",
            provider="LAADS", 
            shortname="XAERDT_L2_MODIS_Terra",
            version="1",
            description="MODIS/Terra Dark Target Aerosol 5-Min L2 Swath 10 km version: 1"
        )

    MOD09Q1P_EVI_V6_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_MOD09Q1P_EVI_6",
            provider="LAADS", 
            shortname="MOD09Q1P_EVI",
            version="6",
            description="MODIS/Terra EVI Phenology annual L4 250m SIN Grid version: 6"
        )

    MOD09A1P_EVI_V6_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_MOD09A1P_EVI_6",
            provider="LAADS", 
            shortname="MOD09A1P_EVI",
            version="6",
            description="MODIS/Terra EVI Phenology annual L4 500m SIN Grid version: 6"
        )

    MOD09Q1G_EVI_V6_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_MOD09Q1G_EVI_6",
            provider="LAADS", 
            shortname="MOD09Q1G_EVI",
            version="6",
            description="MODIS/Terra Gap-Filled, Smoothed EVI 8-Day L4 250m SIN Grid version: 6"
        )

    MOD09A1G_EVI_V6_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_MOD09A1G_EVI_6",
            provider="LAADS", 
            shortname="MOD09A1G_EVI",
            version="6",
            description="MODIS/Terra Gap-Filled, Smoothed EVI 8-Day L4 500m SIN Grid version: 6"
        )

    MOD15A2GFS_V6_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_MOD15A2GFS_6",
            provider="LAADS", 
            shortname="MOD15A2GFS",
            version="6",
            description="MODIS/Terra Gap-Filled, Smoothed LAI-FPAR 8-Day L4 Global 1km SIN Grid version: 6"
        )

    MOD09Q1G_NDVI_V6_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_MOD09Q1G_NDVI_6",
            provider="LAADS", 
            shortname="MOD09Q1G_NDVI",
            version="6",
            description="MODIS/Terra Gap-Filled, Smoothed NDVI 8-Day L4 250m SIN Grid version: 6"
        )

    MOD09A1G_NDVI_V6_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_MOD09A1G_NDVI_6",
            provider="LAADS", 
            shortname="MOD09A1G_NDVI",
            version="6",
            description="MODIS/Terra Gap-Filled, Smoothed NDVI 8-Day L4 500m SIN Grid version: 6"
        )

    MOD03_V61_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_MOD03_6.1",
            provider="LAADS", 
            shortname="MOD03",
            version="6.1",
            description="MODIS/Terra Geolocation Fields 5-Min L1A Swath 1km version: 6.1"
        )

    MOD15A2PHN_V6_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_MOD15A2PHN_6",
            provider="LAADS", 
            shortname="MOD15A2PHN",
            version="6",
            description="MODIS/Terra LAI-FPAR Phenology annual L4 Global 1km SIN Grid version: 6"
        )

    MOD02SSH_V61_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_MOD02SSH_6.1",
            provider="LAADS", 
            shortname="MOD02SSH",
            version="6.1",
            description="MODIS/Terra Level 1B Subsampled Calibrated Radiance 5Km version: 6.1"
        )

    MOD09Q1P_NDVI_V6_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_MOD09Q1P_NDVI_6",
            provider="LAADS", 
            shortname="MOD09Q1P_NDVI",
            version="6",
            description="MODIS/Terra NDVI Phenology annual L4 250m SIN Grid version: 6"
        )

    MOD09A1P_NDVI_V6_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_MOD09A1P_NDVI_6",
            provider="LAADS", 
            shortname="MOD09A1P_NDVI",
            version="6",
            description="MODIS/Terra NDVI Phenology annual L4 500m SIN Grid version: 6"
        )

    MOD01_V61_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_MOD01_6.1",
            provider="LAADS", 
            shortname="MOD01",
            version="6.1",
            description="MODIS/Terra Raw Radiances in Counts 5-Min L1A Swath version: 6.1"
        )

    MOD07_L2_V61_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_MOD07_L2_6.1",
            provider="LAADS", 
            shortname="MOD07_L2",
            version="6.1",
            description="MODIS/Terra Temperature and Water Vapor Profiles 5-Min L2 Swath 5km version: 6.1"
        )

    MOD05_L2_V61_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_MOD05_L2_6.1",
            provider="LAADS", 
            shortname="MOD05_L2",
            version="6.1",
            description="MODIS/Terra Total Precipitable Water Vapor 5-Min L2 Swath 1km and 5km version: 6.1"
        )

    N07_AVH13C1_V6_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_N07_AVH13C1_6",
            provider="LAADS", 
            shortname="N07_AVH13C1",
            version="6",
            description="NOAA-07 AVHRR Atmospherically Corrected Normalized Difference Vegetation Index Daily L3 Global 0.05 Deg. CMG version: 6"
        )

    N07_AVH09C1_V6_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_N07_AVH09C1_6",
            provider="LAADS", 
            shortname="N07_AVH09C1",
            version="6",
            description="NOAA-07 AVHRR Atmospherically Corrected Surface Reflectance Daily L3 Global 0.05 Deg. CMG version: 6"
        )

    N07_AVH02C1_V6_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_N07_AVH02C1_6",
            provider="LAADS", 
            shortname="N07_AVH02C1",
            version="6",
            description="NOAA-07 AVHRR Top-of-Atmosphere Reflectance Daily L3 Global 0.05 Deg. CMG version: 6"
        )

    N09_AVH13C1_V6_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_N09_AVH13C1_6",
            provider="LAADS", 
            shortname="N09_AVH13C1",
            version="6",
            description="NOAA-09 AVHRR Atmospherically Corrected Normalized Difference Vegetation Index Daily L3 Global 0.05 Deg. CMG version: 6"
        )

    N09_AVH09C1_V6_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_N09_AVH09C1_6",
            provider="LAADS", 
            shortname="N09_AVH09C1",
            version="6",
            description="NOAA-09 AVHRR Atmospherically Corrected Surface Reflectance Daily L3 Global 0.05 Deg. CMG version: 6"
        )

    N09_AVH02C1_V6_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_N09_AVH02C1_6",
            provider="LAADS", 
            shortname="N09_AVH02C1",
            version="6",
            description="NOAA-09 AVHRR Top-of-Atmosphere Reflectance Daily L3 Global 0.05 Deg. CMG version: 6"
        )

    N11_AVH13C1_V6_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_N11_AVH13C1_6",
            provider="LAADS", 
            shortname="N11_AVH13C1",
            version="6",
            description="NOAA-11 AVHRR Atmospherically Corrected Normalized Difference Vegetation Index Daily L3 Global 0.05 Deg. CMG version: 6"
        )

    N11_AVH09C1_V6_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_N11_AVH09C1_6",
            provider="LAADS", 
            shortname="N11_AVH09C1",
            version="6",
            description="NOAA-11 AVHRR Atmospherically Corrected Surface Reflectance Daily L3 Global 0.05Deg CMG version: 6"
        )

    N11_AVH02C1_V6_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_N11_AVH02C1_6",
            provider="LAADS", 
            shortname="N11_AVH02C1",
            version="6",
            description="NOAA-11 AVHRR Top-of-Atmosphere Reflectance Daily L3 Global 0.05 Deg. CMG version: 6"
        )

    N14_AVH13C1_V6_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_N14_AVH13C1_6",
            provider="LAADS", 
            shortname="N14_AVH13C1",
            version="6",
            description="NOAA-14 AVHRR Atmospherically Corrected Normalized Difference Vegetation Index Daily L3 Global 0.05 Deg. CMG version: 6"
        )

    N14_AVH09C1_V6_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_N14_AVH09C1_6",
            provider="LAADS", 
            shortname="N14_AVH09C1",
            version="6",
            description="NOAA-14 AVHRR Atmospherically Corrected Surface Reflectance Daily L3 Global 0.05 Deg. CMG version: 6"
        )

    N14_AVH02C1_V6_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_N14_AVH02C1_6",
            provider="LAADS", 
            shortname="N14_AVH02C1",
            version="6",
            description="NOAA-14 AVHRR Top-of-Atmosphere Reflectance Daily L3 Global 0.05 Deg. CMG version: 6"
        )

    N16_AVH13C1_V6_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_N16_AVH13C1_6",
            provider="LAADS", 
            shortname="N16_AVH13C1",
            version="6",
            description="NOAA-16 AVHRR Atmospherically Corrected Normalized Difference Vegetation Index Daily L3 Global 0.05 Deg. CMG version: 6"
        )

    N16_AVH09C1_V6_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_N16_AVH09C1_6",
            provider="LAADS", 
            shortname="N16_AVH09C1",
            version="6",
            description="NOAA-16 AVHRR Atmospherically Corrected Surface Reflectance Daily L3 Global 0.05 Deg. CMG version: 6"
        )

    N16_AVH02C1_V6_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_N16_AVH02C1_6",
            provider="LAADS", 
            shortname="N16_AVH02C1",
            version="6",
            description="NOAA-16 AVHRR Top-of-Atmosphere Reflectance Daily L3 Global 0.05Deg CMG version: 6"
        )

    N18_AVH13C1_V6_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_N18_AVH13C1_6",
            provider="LAADS", 
            shortname="N18_AVH13C1",
            version="6",
            description="NOAA-18 AVHRR Atmospherically Corrected Normalized Difference Vegetation Index Daily L3 Global 0.05 Deg. CMG version: 6"
        )

    N18_AVH09C1_V6_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_N18_AVH09C1_6",
            provider="LAADS", 
            shortname="N18_AVH09C1",
            version="6",
            description="NOAA-18 AVHRR Atmospherically Corrected Surface Reflectance Daily L3 Global 0.05 Deg. CMG version: 6"
        )

    N18_AVH02C1_V6_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_N18_AVH02C1_6",
            provider="LAADS", 
            shortname="N18_AVH02C1",
            version="6",
            description="NOAA-18 AVHRR Top-of-Atmosphere Reflectance Daily L3 Global 0.05 Deg. CMG version: 6"
        )

    N19_AVH09C1_V6_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_N19_AVH09C1_6",
            provider="LAADS", 
            shortname="N19_AVH09C1",
            version="6",
            description="NOAA-19 AVHRR Atmospherically Corrected Surface Reflectance Daily L3 Global 0.05 Deg. CMG version: 6"
        )

    N19_AVH02C1_V6_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_N19_AVH02C1_6",
            provider="LAADS", 
            shortname="N19_AVH02C1",
            version="6",
            description="NOAA-19 AVHRR Top-of-Atmosphere Reflectance Daily L3 Global 0.05 Deg. CMG version: 6"
        )

    N19_AVH13C1_V6_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_N19_AVH13C1_6",
            provider="LAADS", 
            shortname="N19_AVH13C1",
            version="6",
            description="NOAA19 AVHRR Atmospherically Corrected Normalized Difference Vegetation Index Daily L3 Global 0.05 Deg. CMG version: 6"
        )

    FSNRAD_L2_VIIRS_CRIS_NOAA20_V2_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_FSNRAD_L2_VIIRS_CRIS_NOAA20_2",
            provider="LAADS", 
            shortname="FSNRAD_L2_VIIRS_CRIS_NOAA20",
            version="2",
            description="NOAA20 VIIRS+CrIS Fusion 6-Min L2 Swath 750 m version: 2"
        )

    S3A_SY_2_SYN_V1_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_S3A_SY_2_SYN_1",
            provider="LAADS", 
            shortname="S3A_SY_2_SYN",
            version="1",
            description="OLCI+SLSTR/Sentinel-3A L2 Surface Reflectance and Aerosol parameters over Land version: 1"
        )

    S3B_SY_2_SYN_V1_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_S3B_SY_2_SYN_1",
            provider="LAADS", 
            shortname="S3B_SY_2_SYN",
            version="1",
            description="OLCI+SLSTR/Sentinel-3B L2 Surface Reflectance and Aerosol parameters over Land version: 1"
        )

    S3A_OL_1_EFR_V1_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_S3A_OL_1_EFR_1",
            provider="LAADS", 
            shortname="S3A_OL_1_EFR",
            version="1",
            description="OLCI/Sentinel-3A L1 Full Resolution Top of Atmosphere Reflectance version: 1"
        )

    S3A_OL_1_ERR_V1_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_S3A_OL_1_ERR_1",
            provider="LAADS", 
            shortname="S3A_OL_1_ERR",
            version="1",
            description="OLCI/Sentinel-3A L1 Reduced Resolution Top of Atmosphere Reflectance version: 1"
        )

    S3B_OL_1_EFR_V1_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_S3B_OL_1_EFR_1",
            provider="LAADS", 
            shortname="S3B_OL_1_EFR",
            version="1",
            description="OLCI/Sentinel-3B L1 Full Resolution Top of Atmosphere Reflectance version: 1"
        )

    S3B_OL_1_ERR_V1_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_S3B_OL_1_ERR_1",
            provider="LAADS", 
            shortname="S3B_OL_1_ERR",
            version="1",
            description="OLCI/Sentinel-3B L1 Reduced Resolution Top of Atmosphere Reflectance version: 1"
        )

    EN1_MDSI_MER_RR__1P_V4_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_EN1_MDSI_MER_RR__1P_4",
            provider="LAADS", 
            shortname="EN1_MDSI_MER_RR__1P",
            version="4",
            description="Reduced Resolution Geolocated and Calibrated TOA Radiance version: 4"
        )

    EN1_MDSI_MER_RR__2P_V4_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_EN1_MDSI_MER_RR__2P_4",
            provider="LAADS", 
            shortname="EN1_MDSI_MER_RR__2P",
            version="4",
            description="Reduced Resolution Geophysical Product for Ocean, Land and Atmosphere version: 4"
        )

    S3A_SL_1_RBT_V1_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_S3A_SL_1_RBT_1",
            provider="LAADS", 
            shortname="S3A_SL_1_RBT",
            version="1",
            description="SLSTR/Sentinel-3A L1 Full Resolution Top of Atmosphere Radiances and Brightness Temperature version: 1"
        )

    S3B_SL_1_RBT_V1_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_S3B_SL_1_RBT_1",
            provider="LAADS", 
            shortname="S3B_SL_1_RBT",
            version="1",
            description="SLSTR/Sentinel-3B L1 Full Resolution Top of Atmosphere Radiances and Brightness Temperature version: 1"
        )

    FSNRAD_L2_VIIRS_CRIS_SNPP_V2_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_FSNRAD_L2_VIIRS_CRIS_SNPP_2",
            provider="LAADS", 
            shortname="FSNRAD_L2_VIIRS_CRIS_SNPP",
            version="2",
            description="SNPP VIIRS+CrIS Fusion 6-Min L2 Swath 750 m version: 2"
        )

    VJ109_V2_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_VJ109_2",
            provider="LAADS", 
            shortname="VJ109",
            version="2",
            description="VIIRS/JPSS1 Atmospherically Corrected Surface Reflectance 6-Min L2 Swath 375m, 750m version: 2"
        )

    VJ102DNB_V21_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_VJ102DNB_2.1",
            provider="LAADS", 
            shortname="VJ102DNB",
            version="2.1",
            description="VIIRS/JPSS1 Day/Night Band 6-Min L1B Swath 750 m version: 2.1"
        )

    VJ103DNB_V21_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_VJ103DNB_2.1",
            provider="LAADS", 
            shortname="VJ103DNB",
            version="2.1",
            description="VIIRS/JPSS1 Day/Night Band Resolution Terrain Corrected Geolocation L1 6-Min Swath 750 m version: 2.1"
        )

    VJ102IMG_V21_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_VJ102IMG_2.1",
            provider="LAADS", 
            shortname="VJ102IMG",
            version="2.1",
            description="VIIRS/JPSS1 Imagery Resolution 6-Min L1B Swath 375 m version: 2.1"
        )

    VJ103IMG_V21_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_VJ103IMG_2.1",
            provider="LAADS", 
            shortname="VJ103IMG",
            version="2.1",
            description="VIIRS/JPSS1 Imagery Resolution Terrain Corrected Geolocation L1 6-Min Swath 375 m version: 2.1"
        )

    VJ102MOD_V21_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_VJ102MOD_2.1",
            provider="LAADS", 
            shortname="VJ102MOD",
            version="2.1",
            description="VIIRS/JPSS1 Moderate Resolution 6-Min L1B Swath 750 m version: 2.1"
        )

    VJ103MOD_V21_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_VJ103MOD_2.1",
            provider="LAADS", 
            shortname="VJ103MOD",
            version="2.1",
            description="VIIRS/JPSS1 Moderate Resolution Terrain Corrected Geolocation L1 6-Min Swath 750m version: 2.1"
        )

    VJ202DNB_V2_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_VJ202DNB_2",
            provider="LAADS", 
            shortname="VJ202DNB",
            version="2",
            description="VIIRS/JPSS2 Day/Night Band 6-Min L1B Swath 750 m version: 2"
        )

    VJ202IMG_V2_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_VJ202IMG_2",
            provider="LAADS", 
            shortname="VJ202IMG",
            version="2",
            description="VIIRS/JPSS2 Imagery Resolution 6-Min L1B Swath 375 m version: 2"
        )

    VJ203IMG_V2_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_VJ203IMG_2",
            provider="LAADS", 
            shortname="VJ203IMG",
            version="2",
            description="VIIRS/JPSS2 Imagery Resolution Terrain Corrected Geolocation 6-Min L1 Swath 375 m version: 2"
        )

    VJ202MOD_V2_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_VJ202MOD_2",
            provider="LAADS", 
            shortname="VJ202MOD",
            version="2",
            description="VIIRS/JPSS2 Moderate Resolution 6 Min L1B Swath 750 m version: 2"
        )

    VJ203MOD_V2_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_VJ203MOD_2",
            provider="LAADS", 
            shortname="VJ203MOD",
            version="2",
            description="VIIRS/JPSS2 Moderate Resolution Terrain Corrected Geolocation 6-Min L1 Swath 750 m version: 2"
        )

    VJ203DNB_V2_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_VJ203DNB_2",
            provider="LAADS", 
            shortname="VJ203DNB",
            version="2",
            description="VIIRS/JPSS2Day/Night Band Resolution Terrain Corrected Geolocation 6-Min L1 Swath 750 m version: 2"
        )

    CLDMSK_L2_VIIRS_NOAA20_V1_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_CLDMSK_L2_VIIRS_NOAA20_1",
            provider="LAADS", 
            shortname="CLDMSK_L2_VIIRS_NOAA20",
            version="1",
            description="VIIRS/NOAA20 Cloud Mask and Spectral Test Results 6-Min L2 Swath 750m version: 1"
        )

    CLDPROP_L2_VIIRS_NOAA20_V11_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_CLDPROP_L2_VIIRS_NOAA20_1.1",
            provider="LAADS", 
            shortname="CLDPROP_L2_VIIRS_NOAA20",
            version="1.1",
            description="VIIRS/NOAA20 Cloud Properties 6-min L2 Swath 750m version: 1.1"
        )

    CLDPROPCOSP_D3_VIIRS_NOAA20_V11_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_CLDPROPCOSP_D3_VIIRS_NOAA20_1.1",
            provider="LAADS", 
            shortname="CLDPROPCOSP_D3_VIIRS_NOAA20",
            version="1.1",
            description="VIIRS/NOAA20 Cloud Properties COSP Level 3 daily, 1x1 deg. grid version: 1.1"
        )

    CLDPROPCOSP_M3_VIIRS_NOAA20_V11_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_CLDPROPCOSP_M3_VIIRS_NOAA20_1.1",
            provider="LAADS", 
            shortname="CLDPROPCOSP_M3_VIIRS_NOAA20",
            version="1.1",
            description="VIIRS/NOAA20 Cloud Properties COSP Level 3 monthly, 1x1 deg. grid version: 1.1"
        )

    CLDPROP_M3_VIIRS_NOAA20_V11_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_CLDPROP_M3_VIIRS_NOAA20_1.1",
            provider="LAADS", 
            shortname="CLDPROP_M3_VIIRS_NOAA20",
            version="1.1",
            description="VIIRS/NOAA20 Cloud Properties Level 3 monthly, 1x1 degree grid version: 1.1"
        )

    AERDT_L2_VIIRS_NOAA20_V2_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_AERDT_L2_VIIRS_NOAA20_2",
            provider="LAADS", 
            shortname="AERDT_L2_VIIRS_NOAA20",
            version="2",
            description="VIIRS/NOAA20 Dark Target Aerosol 6-Min L2 Swath 6 km version: 2"
        )

    XAERDT_L2_VIIRS_NOAA20_V1_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_XAERDT_L2_VIIRS_NOAA20_1",
            provider="LAADS", 
            shortname="XAERDT_L2_VIIRS_NOAA20",
            version="1",
            description="VIIRS/NOAA20 Dark Target Aerosol L2 6-Min Swath 6 km version: 1"
        )

    AERDB_L2_VIIRS_NOAA20_V2_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_AERDB_L2_VIIRS_NOAA20_2",
            provider="LAADS", 
            shortname="AERDB_L2_VIIRS_NOAA20",
            version="2",
            description="VIIRS/NOAA20 Deep Blue Aerosol L2 6-Min Swath 6 km version: 2"
        )

    AERDB_D3_VIIRS_NOAA20_V2_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_AERDB_D3_VIIRS_NOAA20_2",
            provider="LAADS", 
            shortname="AERDB_D3_VIIRS_NOAA20",
            version="2",
            description="VIIRS/NOAA20 Deep Blue Level 3 daily aerosol data, 1 degree x 1 degree grid version: 2"
        )

    AERDB_M3_VIIRS_NOAA20_V2_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_AERDB_M3_VIIRS_NOAA20_2",
            provider="LAADS", 
            shortname="AERDB_M3_VIIRS_NOAA20",
            version="2",
            description="VIIRS/NOAA20 Deep Blue Level 3 monthly aerosol data, 1x1 degree grid version: 2"
        )

    CLDMSK_L2_VIIRS_NOAA21_V1_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_CLDMSK_L2_VIIRS_NOAA21_1",
            provider="LAADS", 
            shortname="CLDMSK_L2_VIIRS_NOAA21",
            version="1",
            description="VIIRS/NOAA21 Cloud Mask and Spectral Test Results 6-Min L2 Swath 750m version: 1"
        )

    VNP09_V2_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_VNP09_2",
            provider="LAADS", 
            shortname="VNP09",
            version="2",
            description="VIIRS/NPP Atmospherically Corrected Surface Reflectance 6-Min L2 Swath 375m, 750m - V2 version: 2"
        )

    VNP46A1_V2_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_VNP46A1_2",
            provider="LAADS", 
            shortname="VNP46A1",
            version="2",
            description="VIIRS/NPP Daily Gridded Day Night Band 500 m Linear Lat Lon Grid Night version: 2"
        )

    VNP46A1_V1_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_VNP46A1_1",
            provider="LAADS", 
            shortname="VNP46A1",
            version="1",
            description="VIIRS/NPP Daily Gridded Day Night Band 500m Linear Lat Lon Grid Night version: 1"
        )

    VNP02DNB_V2_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_VNP02DNB_2",
            provider="LAADS", 
            shortname="VNP02DNB",
            version="2",
            description="VIIRS/NPP Day/Night Band 6-Min L1B Swath 750 m version: 2"
        )

    VNP03DNB_V2_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_VNP03DNB_2",
            provider="LAADS", 
            shortname="VNP03DNB",
            version="2",
            description="VIIRS/NPP Day/Night Band Terrain Corrected Geolocation L1 6-Min Swath 750 m version: 2"
        )

    VNP46A2_V1_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_VNP46A2_1",
            provider="LAADS", 
            shortname="VNP46A2",
            version="1",
            description="VIIRS/NPP Gap-Filled Lunar BRDF-Adjusted Nighttime Lights Daily L3 Global 500m Linear Lat Lon Grid version: 1"
        )

    VNP02IMG_V2_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_VNP02IMG_2",
            provider="LAADS", 
            shortname="VNP02IMG",
            version="2",
            description="VIIRS/NPP Imagery Resolution 6-Min L1B Swath 375 m version: 2"
        )

    VNP03IMG_V2_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_VNP03IMG_2",
            provider="LAADS", 
            shortname="VNP03IMG",
            version="2",
            description="VIIRS/NPP Imagery Resolution Terrain Corrected Geolocation 6-Min L1 Swath 375 m version: 2"
        )

    VNP46A3_V1_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_VNP46A3_1",
            provider="LAADS", 
            shortname="VNP46A3",
            version="1",
            description="VIIRS/NPP Lunar BRDF-Adjusted Nighttime Lights Monthly L3 Global 15 arc-second Linear Lat Lon Grid version: 1"
        )

    VNP46A4_V1_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_VNP46A4_1",
            provider="LAADS", 
            shortname="VNP46A4",
            version="1",
            description="VIIRS/NPP Lunar BRDF-Adjusted Nighttime Lights Yearly L3 Global 15 arc-second Linear Lat Lon Grid version: 1"
        )

    VNP03MOD_V2_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_VNP03MOD_2",
            provider="LAADS", 
            shortname="VNP03MOD",
            version="2",
            description="VIIRS/NPP Moderate Resolution Terrain-Corrected Geolocation L1 6-Min Swath 750 m version: 2"
        )

    CLDCR_L2_VIIRS_SNPP_V1_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_CLDCR_L2_VIIRS_SNPP_1",
            provider="LAADS", 
            shortname="CLDCR_L2_VIIRS_SNPP",
            version="1",
            description="VIIRS/SNPP Cirrus Reflectance 6-min L2 Swath 750m version: 1"
        )

    CLDPROP_L2_VIIRS_SNPP_V11_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_CLDPROP_L2_VIIRS_SNPP_1.1",
            provider="LAADS", 
            shortname="CLDPROP_L2_VIIRS_SNPP",
            version="1.1",
            description="VIIRS/SNPP Cloud Properties 6-min L2 Swath 750m version: 1.1"
        )

    CLDPROPCOSP_D3_VIIRS_SNPP_V11_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_CLDPROPCOSP_D3_VIIRS_SNPP_1.1",
            provider="LAADS", 
            shortname="CLDPROPCOSP_D3_VIIRS_SNPP",
            version="1.1",
            description="VIIRS/SNPP Cloud Properties COSP Level 3 daily, 1x1 deg. grid version: 1.1"
        )

    CLDPROPCOSP_M3_VIIRS_SNPP_V11_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_CLDPROPCOSP_M3_VIIRS_SNPP_1.1",
            provider="LAADS", 
            shortname="CLDPROPCOSP_M3_VIIRS_SNPP",
            version="1.1",
            description="VIIRS/SNPP Cloud Properties COSP Level 3 monthly, 1x1 deg. grid version: 1.1"
        )

    CLDPROP_D3_VIIRS_SNPP_V11_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_CLDPROP_D3_VIIRS_SNPP_1.1",
            provider="LAADS", 
            shortname="CLDPROP_D3_VIIRS_SNPP",
            version="1.1",
            description="VIIRS/SNPP Cloud Properties Level 3 daily, 1x1 degree grid version: 1.1"
        )

    CLDPROP_M3_VIIRS_SNPP_V11_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_CLDPROP_M3_VIIRS_SNPP_1.1",
            provider="LAADS", 
            shortname="CLDPROP_M3_VIIRS_SNPP",
            version="1.1",
            description="VIIRS/SNPP Cloud Properties Level 3 monthly, 1x1 degree grid version: 1.1"
        )

    CLDPROP_D3_VIIRS_NOAA20_V11_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_CLDPROP_D3_VIIRS_NOAA20_1.1",
            provider="LAADS", 
            shortname="CLDPROP_D3_VIIRS_NOAA20",
            version="1.1",
            description="VIIRS/SNPP Cloud Properties Level-3 daily 1x1 degree grid version: 1.1"
        )

    AERDT_L2_VIIRS_SNPP_V2_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_AERDT_L2_VIIRS_SNPP_2",
            provider="LAADS", 
            shortname="AERDT_L2_VIIRS_SNPP",
            version="2",
            description="VIIRS/SNPP Dark Target Aerosol L2 6-Min Swath 6 km V2 version: 2"
        )

    XAERDT_L2_VIIRS_SNPP_V1_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_XAERDT_L2_VIIRS_SNPP_1",
            provider="LAADS", 
            shortname="XAERDT_L2_VIIRS_SNPP",
            version="1",
            description="VIIRS/SNPP Dark Target Aerosol L2 6-Min Swath 6km version: 1"
        )

    AERDB_L2_VIIRS_SNPP_V2_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_AERDB_L2_VIIRS_SNPP_2",
            provider="LAADS", 
            shortname="AERDB_L2_VIIRS_SNPP",
            version="2",
            description="VIIRS/SNPP Deep Blue Aerosol L2 6 Min Swath 6km version: 2"
        )

    AERDB_L2_VIIRS_SNPP_V11_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_AERDB_L2_VIIRS_SNPP_1.1",
            provider="LAADS", 
            shortname="AERDB_L2_VIIRS_SNPP",
            version="1.1",
            description="VIIRS/SNPP Deep Blue Aerosol L2 6-Min Swath 6km version: 1.1"
        )

    AERDB_D3_VIIRS_SNPP_V2_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_AERDB_D3_VIIRS_SNPP_2",
            provider="LAADS", 
            shortname="AERDB_D3_VIIRS_SNPP",
            version="2",
            description="VIIRS/SNPP Deep Blue Level 3 daily aerosol data, 1 degree x 1 degree grid version: 2"
        )

    AERDB_D3_VIIRS_SNPP_V11_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_AERDB_D3_VIIRS_SNPP_1.1",
            provider="LAADS", 
            shortname="AERDB_D3_VIIRS_SNPP",
            version="1.1",
            description="VIIRS/SNPP Deep Blue Level 3 daily aerosol data, 1 degree x1 degree grid version: 1.1"
        )

    AERDB_M3_VIIRS_SNPP_V2_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_AERDB_M3_VIIRS_SNPP_2",
            provider="LAADS", 
            shortname="AERDB_M3_VIIRS_SNPP",
            version="2",
            description="VIIRS/SNPP Deep Blue Level 3 monthly aerosol data 1x1 degree grid version: 2"
        )

    AERDB_M3_VIIRS_SNPP_V11_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_AERDB_M3_VIIRS_SNPP_1.1",
            provider="LAADS", 
            shortname="AERDB_M3_VIIRS_SNPP",
            version="1.1",
            description="VIIRS/SNPP Deep Blue Level 3 monthly aerosol data, 1 degree x1 degree grid version: 1.1"
        )

    WATVP_L2_VIIRS_SNPP_V1_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_WATVP_L2_VIIRS_SNPP_1",
            provider="LAADS", 
            shortname="WATVP_L2_VIIRS_SNPP",
            version="1",
            description="VIIRS/SNPP Level-2 Water Vapor Products 6-min Swath 750m version: 1"
        )

    WATVP_D3_VIIRS_SNPP_V1_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_WATVP_D3_VIIRS_SNPP_1",
            provider="LAADS", 
            shortname="WATVP_D3_VIIRS_SNPP",
            version="1",
            description="VIIRS/SNPP Water Vapor Level-3 daily 0.5 x 0.5 degree grid version: 1"
        )

    WATVP_M3_VIIRS_SNPP_V1_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_WATVP_M3_VIIRS_SNPP_1",
            provider="LAADS", 
            shortname="WATVP_M3_VIIRS_SNPP",
            version="1",
            description="VIIRS/SNPP Water Vapor Level-3 monthly 0.5 x 0.5 degree grid version: 1"
        )

    CLDMSK_L2_VIIRS_SNPP_V1_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_CLDMSK_L2_VIIRS_SNPP_1",
            provider="LAADS", 
            shortname="CLDMSK_L2_VIIRS_SNPP",
            version="1",
            description="VIIRS/Suomi-NPP Cloud Mask 6-Min Swath 750 m version: 1"
        )

    VNP02MOD_V2_LAADS = DataCollectionDefinition(
            api_id="CMR",
            collections="LAADS_VNP02MOD_2",
            provider="LAADS", 
            shortname="VNP02MOD",
            version="2",
            description="VNP02MOD | VIIRS/NPP Moderate Resolution 6-Min L1B Swath 750 m version: 2"
        )

