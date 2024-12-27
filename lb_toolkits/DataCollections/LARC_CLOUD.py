# -*- coding:utf-8 -*-

from lb_toolkits.DataCollections.DataCollectionDefinition import DataCollectionDefinition 

class DataCollectionLARC_CLOUD : 
    PREFIRE_SAT1_0_PAYLOAD_TLM_VR01_LARC_CLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="LARC_CLOUD_PREFIRE_SAT1_0-PAYLOAD-TLM_R01",
            provider="LARC_CLOUD", 
            shortname="PREFIRE_SAT1_0-PAYLOAD-TLM",
            version="R01",
            description="Polar Radiant Energy in the Far InfraRed Experiment (PREFIRE) Satellite 1 Raw Curated Payload R01 version: R01"
        )

    PREFIRE_SAT1_0_PAYLOAD_VR01_LARC_CLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="LARC_CLOUD_PREFIRE_SAT1_0-PAYLOAD_R01",
            provider="LARC_CLOUD", 
            shortname="PREFIRE_SAT1_0-PAYLOAD",
            version="R01",
            description="Polar Radiant Energy in the Far InfraRed Experiment (PREFIRE) Satellite 1 Raw Payload R01 version: R01"
        )

    PREFIRE_SAT1_0_BUS_TLM_VR01_LARC_CLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="LARC_CLOUD_PREFIRE_SAT1_0-BUS-TLM_R01",
            provider="LARC_CLOUD", 
            shortname="PREFIRE_SAT1_0-BUS-TLM",
            version="R01",
            description="Polar Radiant Energy in the Far InfraRed Experiment (PREFIRE) Satellite 1 telemetry R01 version: R01"
        )

    PREFIRE_SAT2_0_PAYLOAD_TLM_VR01_LARC_CLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="LARC_CLOUD_PREFIRE_SAT2_0-PAYLOAD-TLM_R01",
            provider="LARC_CLOUD", 
            shortname="PREFIRE_SAT2_0-PAYLOAD-TLM",
            version="R01",
            description="Polar Radiant Energy in the Far InfraRed Experiment (PREFIRE) Satellite 2 Raw Curated Radiance R01 version: R01"
        )

    PREFIRE_SAT2_0_PAYLOAD_VR01_LARC_CLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="LARC_CLOUD_PREFIRE_SAT2_0-PAYLOAD_R01",
            provider="LARC_CLOUD", 
            shortname="PREFIRE_SAT2_0-PAYLOAD",
            version="R01",
            description="Polar Radiant Energy in the Far InfraRed Experiment (PREFIRE) Satellite 2 Raw Payload R01 version: R01"
        )

    PREFIRE_SAT2_0_BUS_TLM_VR01_LARC_CLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="LARC_CLOUD_PREFIRE_SAT2_0-BUS-TLM_R01",
            provider="LARC_CLOUD", 
            shortname="PREFIRE_SAT2_0-BUS-TLM",
            version="R01",
            description="Polar Radiant Energy in the Far InfraRed Experiment (PREFIRE) Satellite 2 telemetry R01 version: R01"
        )

    STAQS_SONDES_DATA_V1_LARC_CLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="LARC_CLOUD_STAQS_Sondes_Data_1",
            provider="LARC_CLOUD", 
            shortname="STAQS_Sondes_Data",
            version="1",
            description="STAQS Balloonsondes and Ozonesondes Data version: 1"
        )

    STAQS_CHIWAUKEE_PRAIRIE_DATA_V1_LARC_CLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="LARC_CLOUD_STAQS_Chiwaukee-Prairie_Data_1",
            provider="LARC_CLOUD", 
            shortname="STAQS_Chiwaukee-Prairie_Data",
            version="1",
            description="STAQS Chiwaukee Prairie Data version: 1"
        )

    STAQS_DRONE_DATA_V1_LARC_CLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="LARC_CLOUD_STAQS_Drone_Data_1",
            provider="LARC_CLOUD", 
            shortname="STAQS_Drone_Data",
            version="1",
            description="STAQS Drone Data version: 1"
        )

    STAQS_GROUND_DATA_V1_LARC_CLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="LARC_CLOUD_STAQS_Ground_Data_1",
            provider="LARC_CLOUD", 
            shortname="STAQS_Ground_Data",
            version="1",
            description="STAQS Ground Data version: 1"
        )

    STAQS_INSTEP_DATA_V1_LARC_CLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="LARC_CLOUD_STAQS_INSTEP_Data_1",
            provider="LARC_CLOUD", 
            shortname="STAQS_INSTEP_Data",
            version="1",
            description="STAQS INSTEP Data version: 1"
        )

    STAQS_AIRCRAFTREMOTESENSING_JSC_GV_GCAS_DATA_V1_LARC_CLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="LARC_CLOUD_STAQS_AircraftRemoteSensing_JSC-GV_GCAS_Data_1",
            provider="LARC_CLOUD", 
            shortname="STAQS_AircraftRemoteSensing_JSC-GV_GCAS_Data",
            version="1",
            description="STAQS JSC GV GEOstationary Coastal and Air Pollution Events (GEO-CAPE) Airborne Simulator Data version: 1"
        )

    STAQS_AIRCRAFTREMOTESENSING_JSC_GV_HSRL2_DATA_V1_LARC_CLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="LARC_CLOUD_STAQS_AircraftRemoteSensing_JSC-GV_HSRL2_Data_1",
            provider="LARC_CLOUD", 
            shortname="STAQS_AircraftRemoteSensing_JSC-GV_HSRL2_Data",
            version="1",
            description="STAQS JSC GV High Spectral Resolution Lidar-2 Data version: 1"
        )

    STAQS_AIRCRAFTREMOTESENSING_NASA_G3_GCAS_DATA_V1_LARC_CLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="LARC_CLOUD_STAQS_AircraftRemoteSensing_NASA-G3_GCAS_Data_1",
            provider="LARC_CLOUD", 
            shortname="STAQS_AircraftRemoteSensing_NASA-G3_GCAS_Data",
            version="1",
            description="STAQS NASA G-III GEOstationary Coastal and Air Pollution Events (GEO-CAPE) Airborne Simulator Data version: 1"
        )

    STAQS_AIRCRAFTREMOTESENSING_NASA_G3_HALO_DATA_V1_LARC_CLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="LARC_CLOUD_STAQS_AircraftRemoteSensing_NASA-G3_HALO_Data_1",
            provider="LARC_CLOUD", 
            shortname="STAQS_AircraftRemoteSensing_NASA-G3_HALO_Data",
            version="1",
            description="STAQS NASA G-III High Altitude Lidar Observatory (HALO) Data version: 1"
        )

    STAQS_SEAREY_DATA_V1_LARC_CLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="LARC_CLOUD_STAQS_SeaRey_Data_1",
            provider="LARC_CLOUD", 
            shortname="STAQS_SeaRey_Data",
            version="1",
            description="STAQS SeaRey Data version: 1"
        )

    TEMPO_NO2_L2_VV03_LARC_CLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="LARC_CLOUD_TEMPO_NO2_L2_V03",
            provider="LARC_CLOUD", 
            shortname="TEMPO_NO2_L2",
            version="V03",
            description="TEMPO NO2 tropospheric and stratospheric columns V03 (BETA) version: V03"
        )

    TEMPO_CLDO4_L2_VV03_LARC_CLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="LARC_CLOUD_TEMPO_CLDO4_L2_V03",
            provider="LARC_CLOUD", 
            shortname="TEMPO_CLDO4_L2",
            version="V03",
            description="TEMPO cloud pressure and fraction (O2-O2 dimer) V03 (BETA) version: V03"
        )

    TEMPO_DRK_L1_VV02_LARC_CLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="LARC_CLOUD_TEMPO_DRK_L1_V02",
            provider="LARC_CLOUD", 
            shortname="TEMPO_DRK_L1",
            version="V02",
            description="TEMPO dark exposure V02 (BETA) version: V02"
        )

    TEMPO_DRK_L1_VV03_LARC_CLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="LARC_CLOUD_TEMPO_DRK_L1_V03",
            provider="LARC_CLOUD", 
            shortname="TEMPO_DRK_L1",
            version="V03",
            description="TEMPO dark exposure V03 (BETA) version: V03"
        )

    TEMPO_HCHO_L2_VV03_LARC_CLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="LARC_CLOUD_TEMPO_HCHO_L2_V03",
            provider="LARC_CLOUD", 
            shortname="TEMPO_HCHO_L2",
            version="V03",
            description="TEMPO formaldehyde total column V03 (BETA) version: V03"
        )

    TEMPO_RAD_L1_VV02_LARC_CLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="LARC_CLOUD_TEMPO_RAD_L1_V02",
            provider="LARC_CLOUD", 
            shortname="TEMPO_RAD_L1",
            version="V02",
            description="TEMPO geolocated Earth radiances V02 (BETA) version: V02"
        )

    TEMPO_RAD_L1_VV03_LARC_CLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="LARC_CLOUD_TEMPO_RAD_L1_V03",
            provider="LARC_CLOUD", 
            shortname="TEMPO_RAD_L1",
            version="V03",
            description="TEMPO geolocated Earth radiances V03 (BETA) version: V03"
        )

    TEMPO_RADT_L1_VV03_LARC_CLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="LARC_CLOUD_TEMPO_RADT_L1_V03",
            provider="LARC_CLOUD", 
            shortname="TEMPO_RADT_L1",
            version="V03",
            description="TEMPO geolocated Earth radiances twilight V03 (BETA) version: V03"
        )

    TEMPO_NO2_L3_VV03_LARC_CLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="LARC_CLOUD_TEMPO_NO2_L3_V03",
            provider="LARC_CLOUD", 
            shortname="TEMPO_NO2_L3",
            version="V03",
            description="TEMPO gridded NO2 tropospheric and stratospheric columns V03 (BETA) version: V03"
        )

    TEMPO_CLDO4_L3_VV03_LARC_CLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="LARC_CLOUD_TEMPO_CLDO4_L3_V03",
            provider="LARC_CLOUD", 
            shortname="TEMPO_CLDO4_L3",
            version="V03",
            description="TEMPO gridded cloud fraction and pressure (O2-O2 dimer) V03 (BETA) version: V03"
        )

    TEMPO_HCHO_L3_VV03_LARC_CLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="LARC_CLOUD_TEMPO_HCHO_L3_V03",
            provider="LARC_CLOUD", 
            shortname="TEMPO_HCHO_L3",
            version="V03",
            description="TEMPO gridded formaldehyde total column V03 (BETA) version: V03"
        )

    TEMPO_O3TOT_L3_VV03_LARC_CLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="LARC_CLOUD_TEMPO_O3TOT_L3_V03",
            provider="LARC_CLOUD", 
            shortname="TEMPO_O3TOT_L3",
            version="V03",
            description="TEMPO gridded ozone total column V03 (BETA) version: V03"
        )

    TEMPO_O3TOT_L2_VV03_LARC_CLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="LARC_CLOUD_TEMPO_O3TOT_L2_V03",
            provider="LARC_CLOUD", 
            shortname="TEMPO_O3TOT_L2",
            version="V03",
            description="TEMPO ozone total column V03 (BETA) version: V03"
        )

    TEMPO_IRRR_L1_VV02_LARC_CLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="LARC_CLOUD_TEMPO_IRRR_L1_V02",
            provider="LARC_CLOUD", 
            shortname="TEMPO_IRRR_L1",
            version="V02",
            description="TEMPO solar irradiance (reference diffuser) V02 (BETA) version: V02"
        )

    TEMPO_IRRR_L1_VV03_LARC_CLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="LARC_CLOUD_TEMPO_IRRR_L1_V03",
            provider="LARC_CLOUD", 
            shortname="TEMPO_IRRR_L1",
            version="V03",
            description="TEMPO solar irradiance (reference diffuser) V03 (BETA) version: V03"
        )

    TEMPO_IRR_L1_VV02_LARC_CLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="LARC_CLOUD_TEMPO_IRR_L1_V02",
            provider="LARC_CLOUD", 
            shortname="TEMPO_IRR_L1",
            version="V02",
            description="TEMPO solar irradiance V02 (BETA) version: V02"
        )

    TEMPO_IRR_L1_VV03_LARC_CLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="LARC_CLOUD_TEMPO_IRR_L1_V03",
            provider="LARC_CLOUD", 
            shortname="TEMPO_IRR_L1",
            version="V03",
            description="TEMPO solar irradiance V03 (BETA) version: V03"
        )

    TRACE_A_SONDES_DATA_V1_LARC_CLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="LARC_CLOUD_TRACE-A_Sondes_Data_1",
            provider="LARC_CLOUD", 
            shortname="TRACE-A_Sondes_Data",
            version="1",
            description="TRACE-A Balloonsondes and Ozonesondes Data version: 1"
        )

    TRACE_A_BRAZIL_DATA_V1_LARC_CLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="LARC_CLOUD_TRACE-A_Brazil_Data_1",
            provider="LARC_CLOUD", 
            shortname="TRACE-A_Brazil_Data",
            version="1",
            description="TRACE-A Brazil Data version: 1"
        )

    TRACE_A_TRACEGAS_AIRCRAFTINSITU_DC8_DATA_V1_LARC_CLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="LARC_CLOUD_TRACE-A_TraceGas_AircraftInSitu_DC8_Data_1",
            provider="LARC_CLOUD", 
            shortname="TRACE-A_TraceGas_AircraftInSitu_DC8_Data",
            version="1",
            description="TRACE-A DC-8 In-Situ Trace Gas Data version: 1"
        )

    TRACE_A_AIRCRAFTREMOTESENSING_DC8_DIAL_DATA_V1_LARC_CLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="LARC_CLOUD_TRACE-A_AircraftRemoteSensing_DC8_DIAL_Data_1",
            provider="LARC_CLOUD", 
            shortname="TRACE-A_AircraftRemoteSensing_DC8_DIAL_Data",
            version="1",
            description="TRACE-A DC-8 Remotely Sensed Differential Absorption Lidar (DIAL) Data version: 1"
        )

    TRACE_A_METNAV_AIRCRAFTINSITU_DC8_DATA_V1_LARC_CLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="LARC_CLOUD_TRACE-A_MetNav_AircraftInSitu_DC8_Data_1",
            provider="LARC_CLOUD", 
            shortname="TRACE-A_MetNav_AircraftInSitu_DC8_Data",
            version="1",
            description="TRACE-A In Situ DC-8 Meteorology and Navigation Data version: 1"
        )

    TRACE_A_TRAJECTORY_DATA_V1_LARC_CLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="LARC_CLOUD_TRACE-A_Trajectory_Data_1",
            provider="LARC_CLOUD", 
            shortname="TRACE-A_Trajectory_Data",
            version="1",
            description="TRACE-A Kinematic Trajectory Data version: 1"
        )

    TRACE_A_MERGE_DATA_V1_LARC_CLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="LARC_CLOUD_TRACE-A_Merge_Data_1",
            provider="LARC_CLOUD", 
            shortname="TRACE-A_Merge_Data",
            version="1",
            description="TRACE-A Merge Data version: 1"
        )

    TRACE_A_SATELLITE_DATA_V1_LARC_CLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="LARC_CLOUD_TRACE-A_Satellite_Data_1",
            provider="LARC_CLOUD", 
            shortname="TRACE-A_Satellite_Data",
            version="1",
            description="TRACE-A Supplementary Satellite Data version: 1"
        )

    TRACE_P_SONDES_DATA_V1_LARC_CLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="LARC_CLOUD_TRACE-P_Sondes_Data_1",
            provider="LARC_CLOUD", 
            shortname="TRACE-P_Sondes_Data",
            version="1",
            description="TRACE-P Balloonsondes and Ozonesondes Data version: 1"
        )

    TRACE_P_CLOUD_AIRCRAFTINSITU_DC8_DATA_V1_LARC_CLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="LARC_CLOUD_TRACE-P_Cloud_AircraftInSitu_DC8_Data_1",
            provider="LARC_CLOUD", 
            shortname="TRACE-P_Cloud_AircraftInSitu_DC8_Data",
            version="1",
            description="TRACE-P DC-8 Aircraft In-situ Cloud Data version: 1"
        )

    TRACE_P_AEROSOL_AIRCRAFTINSITU_DC8_DATA_V1_LARC_CLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="LARC_CLOUD_TRACE-P_Aerosol_AircraftInSitu_DC8_Data_1",
            provider="LARC_CLOUD", 
            shortname="TRACE-P_Aerosol_AircraftInSitu_DC8_Data",
            version="1",
            description="TRACE-P DC-8 In-Situ Aerosol Data version: 1"
        )

    TRACE_P_TRACEGAS_AIRCRAFTINSITU_DC8_DATA_V1_LARC_CLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="LARC_CLOUD_TRACE-P_TraceGas_AircraftInSitu_DC8_Data_1",
            provider="LARC_CLOUD", 
            shortname="TRACE-P_TraceGas_AircraftInSitu_DC8_Data",
            version="1",
            description="TRACE-P DC-8 In-Situ Trace Gas Data version: 1"
        )

    TRACE_P_JVALUE_AIRCRAFTINSITU_DC8_DATA_V1_LARC_CLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="LARC_CLOUD_TRACE-P_jValue_AircraftInSitu_DC8_Data_1",
            provider="LARC_CLOUD", 
            shortname="TRACE-P_jValue_AircraftInSitu_DC8_Data",
            version="1",
            description="TRACE-P DC-8 Photolysis Frequencies (J-Values) version: 1"
        )

    TRACE_P_AIRCRAFTREMOTESENSING_DC8_DIAL_DATA_V1_LARC_CLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="LARC_CLOUD_TRACE-P_AircraftRemoteSensing_DC8_DIAL_Data_1",
            provider="LARC_CLOUD", 
            shortname="TRACE-P_AircraftRemoteSensing_DC8_DIAL_Data",
            version="1",
            description="TRACE-P DC-8 Remotely Sensed Differential Absorption Lidar (DIAL) Data version: 1"
        )

    TRACE_P_TRAJECTORY_DC8_DATA_V1_LARC_CLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="LARC_CLOUD_TRACE-P_Trajectory_DC8_Data_1",
            provider="LARC_CLOUD", 
            shortname="TRACE-P_Trajectory_DC8_Data",
            version="1",
            description="TRACE-P DC-8 Trajectory Data version: 1"
        )

    TRACE_P_GROUND_DATA_V1_LARC_CLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="LARC_CLOUD_TRACE-P_Ground_Data_1",
            provider="LARC_CLOUD", 
            shortname="TRACE-P_Ground_Data",
            version="1",
            description="TRACE-P Ground Data version: 1"
        )

    TRACE_P_METNAV_AIRCRAFTINSITU_DC8_DATA_V1_LARC_CLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="LARC_CLOUD_TRACE-P_MetNav_AircraftInSitu_DC8_Data_1",
            provider="LARC_CLOUD", 
            shortname="TRACE-P_MetNav_AircraftInSitu_DC8_Data",
            version="1",
            description="TRACE-P In Situ DC-8 Meteorology and Navigation Data version: 1"
        )

    TRACE_P_METNAV_AIRCRAFT_INSITU_P3B_DATA_V1_LARC_CLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="LARC_CLOUD_TRACE-P_MetNav_Aircraft_InSitu_P3B_Data_1",
            provider="LARC_CLOUD", 
            shortname="TRACE-P_MetNav_Aircraft_InSitu_P3B_Data",
            version="1",
            description="TRACE-P In Situ P-3B Meteorology and Navigation Data version: 1"
        )

    TRACE_P_MERGE_DATA_V1_LARC_CLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="LARC_CLOUD_TRACE-P_Merge_Data_1",
            provider="LARC_CLOUD", 
            shortname="TRACE-P_Merge_Data",
            version="1",
            description="TRACE-P Merge Data version: 1"
        )

    TRACE_P_MODEL_DATA_V1_LARC_CLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="LARC_CLOUD_TRACE-P_Model_Data_1",
            provider="LARC_CLOUD", 
            shortname="TRACE-P_Model_Data",
            version="1",
            description="TRACE-P Model Data version: 1"
        )

    TRACE_P_AEROSOL_AIRCRAFTINSITU_P3B_DATA_V1_LARC_CLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="LARC_CLOUD_TRACE-P_Aerosol_AircraftInSitu_P3B_Data_1",
            provider="LARC_CLOUD", 
            shortname="TRACE-P_Aerosol_AircraftInSitu_P3B_Data",
            version="1",
            description="TRACE-P P-3B In-Situ Aerosol Data version: 1"
        )

    TRACE_P_TRACEGAS_INSITU_P3B_DATA_V1_LARC_CLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="LARC_CLOUD_TRACE-P_TraceGas_InSitu_P3B_Data_1",
            provider="LARC_CLOUD", 
            shortname="TRACE-P_TraceGas_InSitu_P3B_Data",
            version="1",
            description="TRACE-P P-3B In-Situ Trace Gas Data version: 1"
        )

    TRACE_P_JVALUE_AIRCRAFTINSITU_P3B_DATA_V1_LARC_CLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="LARC_CLOUD_TRACE-P_jValue_AircraftInSitu_P3B_Data_1",
            provider="LARC_CLOUD", 
            shortname="TRACE-P_jValue_AircraftInSitu_P3B_Data",
            version="1",
            description="TRACE-P P-3B Photolysis Frequencies (J-Values) version: 1"
        )

    TRACE_P_TRAJECTORY_P3B_DATA_V1_LARC_CLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="LARC_CLOUD_TRACE-P_Trajectory_P3B_Data_1",
            provider="LARC_CLOUD", 
            shortname="TRACE-P_Trajectory_P3B_Data",
            version="1",
            description="TRACE-P P-3B Trajectory Data version: 1"
        )

    TRACE_P_SATELLITE_DATA_V1_LARC_CLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="LARC_CLOUD_TRACE-P_Satellite_Data_1",
            provider="LARC_CLOUD", 
            shortname="TRACE-P_Satellite_Data",
            version="1",
            description="TRACE-P Supplementary Satellite Data version: 1"
        )

