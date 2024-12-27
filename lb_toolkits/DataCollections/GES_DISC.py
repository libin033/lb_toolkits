# -*- coding:utf-8 -*-

from lb_toolkits.DataCollections.DataCollectionDefinition import DataCollectionDefinition 

class DataCollectionGES_DISC : 
    ACOS_L2S_V73_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ACOS_L2S_7.3",
            provider="GES_DISC", 
            shortname="ACOS_L2S",
            version="7.3",
            description="ACOS GOSAT/TANSO-FTS Level 2 Full Physics Standard Product V7.3 (ACOS_L2S) at GES DISC version: 7.3"
        )

    ACOS_L2S_V9R_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ACOS_L2S_9r",
            provider="GES_DISC", 
            shortname="ACOS_L2S",
            version="9r",
            description="ACOS GOSAT/TANSO-FTS Level 2 Full Physics Standard Product V9r (ACOS_L2S) at GES DISC version: 9r"
        )

    ACOS_L2_LITE_FP_V73_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ACOS_L2_Lite_FP_7.3",
            provider="GES_DISC", 
            shortname="ACOS_L2_Lite_FP",
            version="7.3",
            description="ACOS GOSAT/TANSO-FTS Level 2 bias-corrected XCO2 and other select fields from the full-physics retrieval aggregated as daily files V7.3 (ACOS_L2_Lite_FP) at GES DISC version: 7.3"
        )

    ACOS_L2_LITE_FP_V9R_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ACOS_L2_Lite_FP_9r",
            provider="GES_DISC", 
            shortname="ACOS_L2_Lite_FP",
            version="9r",
            description="ACOS GOSAT/TANSO-FTS Level 2 bias-corrected XCO2 and other select fields from the full-physics retrieval aggregated as daily files V9r (ACOS_L2_Lite_FP) at GES DISC version: 9r"
        )

    AIRSM_CPR_MAT_V32_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRSM_CPR_MAT_3.2",
            provider="GES_DISC", 
            shortname="AIRSM_CPR_MAT",
            version="3.2",
            description="AIRS-AMSU variables-CloudSat cloud mask, radar reflectivities, and cloud classification matchups V3.2 (AIRSM_CPR_MAT) at GES DISC version: 3.2"
        )

    AIRS_CPR_IND_V40_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRS_CPR_IND_4.0",
            provider="GES_DISC", 
            shortname="AIRS_CPR_IND",
            version="4.0",
            description="AIRS-CloudSat cloud mask and radar reflectivities collocation indexes V4.0 (AIRS_CPR_IND) at GES_DISC version: 4.0"
        )

    AIRS_CPR_MAT_V32_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRS_CPR_MAT_3.2",
            provider="GES_DISC", 
            shortname="AIRS_CPR_MAT",
            version="3.2",
            description="AIRS-CloudSat cloud mask, radar reflectivities, and cloud classification matchups V3.2 (AIRS_CPR_MAT) at GES DISC version: 3.2"
        )

    AIRXAMAP_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRXAMAP_005",
            provider="GES_DISC", 
            shortname="AIRXAMAP",
            version="005",
            description="AIRS/Aqua Granule map product V005 (AIRXAMAP) at GES DISC version: 005"
        )

    AIRABRAD_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRABRAD_005",
            provider="GES_DISC", 
            shortname="AIRABRAD",
            version="005",
            description="AIRS/Aqua L1B AMSU (A1/A2) geolocated and calibrated brightness temperatures V005 (AIRABRAD) at GES DISC version: 005"
        )

    AIRXBCAL_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRXBCAL_005",
            provider="GES_DISC", 
            shortname="AIRXBCAL",
            version="005",
            description="AIRS/Aqua L1B Calibration subset V005 (AIRXBCAL) at GES DISC version: 005"
        )

    AIRHBRAD_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRHBRAD_005",
            provider="GES_DISC", 
            shortname="AIRHBRAD",
            version="005",
            description="AIRS/Aqua L1B HSB geolocated and calibrated brightness temperatures V005 (AIRHBRAD) at GES DISC version: 005"
        )

    AIRIBRAD_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRIBRAD_005",
            provider="GES_DISC", 
            shortname="AIRIBRAD",
            version="005",
            description="AIRS/Aqua L1B Infrared (IR) geolocated and calibrated radiances V005 (AIRIBRAD) at GES DISC version: 005"
        )

    AIRIBQAP_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRIBQAP_005",
            provider="GES_DISC", 
            shortname="AIRIBQAP",
            version="005",
            description="AIRS/Aqua L1B Infrared (IR) quality assurance subset V005 (AIRIBQAP) at GES DISC version: 005"
        )

    AIRABRAD_NRT_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRABRAD_NRT_005",
            provider="GES_DISC", 
            shortname="AIRABRAD_NRT",
            version="005",
            description="AIRS/Aqua L1B Near Real Time (NRT) AMSU (A1/A2) geolocated and calibrated brightness temperatures V005 (AIRABRAD_NRT) at GES DISC version: 005"
        )

    AIRIBRAD_NRT_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRIBRAD_NRT_005",
            provider="GES_DISC", 
            shortname="AIRIBRAD_NRT",
            version="005",
            description="AIRS/Aqua L1B Near Real Time (NRT) Infrared (IR) geolocated and calibrated radiances V005 (AIRIBRAD_NRT) at GES DISC version: 005"
        )

    AIRIBRAD_NRT_BUFR_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRIBRAD_NRT_BUFR_005",
            provider="GES_DISC", 
            shortname="AIRIBRAD_NRT_BUFR",
            version="005",
            description="AIRS/Aqua L1B Near Real Time (NRT) Infrared (IR) geolocated and calibrated radiances in BUFR format V005 (AIRIBRAD_NRT_BUFR) at GES DISC version: 005"
        )

    AIRIBQAP_NRT_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRIBQAP_NRT_005",
            provider="GES_DISC", 
            shortname="AIRIBQAP_NRT",
            version="005",
            description="AIRS/Aqua L1B Near Real Time (NRT) Infrared (IR) quality assurance subset V005 (AIRIBQAP_NRT) at GES DISC version: 005"
        )

    AIRVBRAD_NRT_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRVBRAD_NRT_005",
            provider="GES_DISC", 
            shortname="AIRVBRAD_NRT",
            version="005",
            description="AIRS/Aqua L1B Near Real Time (NRT) Visible/Near Infrared (VIS/NIR) geolocated and calibrated radiances V005 (AIRVBRAD_NRT) at GES DISC version: 005"
        )

    AIRVBQAP_NRT_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRVBQAP_NRT_005",
            provider="GES_DISC", 
            shortname="AIRVBQAP_NRT",
            version="005",
            description="AIRS/Aqua L1B Near Real Time (NRT) Visible/Near Infrared (VIS/NIR) quality assurance subset V005 (AIRVBQAP_NRT) at GES DISC version: 005"
        )

    AIRVBRAD_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRVBRAD_005",
            provider="GES_DISC", 
            shortname="AIRVBRAD",
            version="005",
            description="AIRS/Aqua L1B Visible/Near Infrared (VIS/NIR) geolocated and calibrated radiances V005 (AIRVBRAD) at GES DISC version: 005"
        )

    AIRVBQAP_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRVBQAP_005",
            provider="GES_DISC", 
            shortname="AIRVBQAP",
            version="005",
            description="AIRS/Aqua L1B Visible/Near Infrared (VIS/NIR) quality assurance subset V005 (AIRVBQAP) at GES DISC version: 005"
        )

    AIRICRAD_V67_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRICRAD_6.7",
            provider="GES_DISC", 
            shortname="AIRICRAD",
            version="6.7",
            description="AIRS/Aqua L1C Infrared (IR) resampled and corrected radiances V6.7 (AIRICRAD) at GES DISC version: 6.7"
        )

    AIRICRAD_NRT_V67_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRICRAD_NRT_6.7",
            provider="GES_DISC", 
            shortname="AIRICRAD_NRT",
            version="6.7",
            description="AIRS/Aqua L1C Near Real Time (NRT) Infrared (IR) resampled and corrected radiances V6.7 (AIRICRAD_NRT) at GES DISC version: 6.7"
        )

    AIRX2STC_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRX2STC_005",
            provider="GES_DISC", 
            shortname="AIRX2STC",
            version="005",
            description="AIRS/Aqua L2 CO2 in the free troposphere (AIRS+AMSU) V005 (AIRX2STC) at GES DISC version: 005"
        )

    AIRS2STC_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRS2STC_005",
            provider="GES_DISC", 
            shortname="AIRS2STC",
            version="005",
            description="AIRS/Aqua L2 CO2 in the free troposphere (AIRS-only) V005 (AIRS2STC) at GES DISC version: 005"
        )

    AIRX2SPC_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRX2SPC_005",
            provider="GES_DISC", 
            shortname="AIRX2SPC",
            version="005",
            description="AIRS/Aqua L2 CO2 support retrieval (AIRS+AMSU) V005 (AIRX2SPC) at GES DISC version: 005"
        )

    AIRS2SPC_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRS2SPC_005",
            provider="GES_DISC", 
            shortname="AIRS2SPC",
            version="005",
            description="AIRS/Aqua L2 CO2 support retrieval (AIRS-only) V005 (AIRS2SPC) at GES DISC version: 005"
        )

    AIRI2CCF_V006_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRI2CCF_006",
            provider="GES_DISC", 
            shortname="AIRI2CCF",
            version="006",
            description="AIRS/Aqua L2 Cloud-Cleared Infrared Radiances (AIRS+AMSU) V006 (AIRI2CCF) at GES DISC version: 006"
        )

    AIRH2CCF_V006_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRH2CCF_006",
            provider="GES_DISC", 
            shortname="AIRH2CCF",
            version="006",
            description="AIRS/Aqua L2 Cloud-Cleared Infrared Radiances (AIRS+AMSU+HSB) V006 (AIRH2CCF) at GES DISC version: 006"
        )

    AIRS2CCF_V006_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRS2CCF_006",
            provider="GES_DISC", 
            shortname="AIRS2CCF",
            version="006",
            description="AIRS/Aqua L2 Cloud-Cleared Infrared Radiances (AIRS-only) V006 (AIRS2CCF) at GES DISC version: 006"
        )

    AIRS2CCF_NRT_V006_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRS2CCF_NRT_006",
            provider="GES_DISC", 
            shortname="AIRS2CCF_NRT",
            version="006",
            description="AIRS/Aqua L2 Near Real Time (NRT) Cloud-Cleared Infrared Radiances (AIRS-only) V006 (AIRS2CCF_NRT) at GES DISC version: 006"
        )

    AIRS2RET_NRT_V006_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRS2RET_NRT_006",
            provider="GES_DISC", 
            shortname="AIRS2RET_NRT",
            version="006",
            description="AIRS/Aqua L2 Near Real Time (NRT) Standard Physical Retrieval (AIRS-only) V006 (AIRS2RET_NRT) at GES DISC version: 006"
        )

    AIRS2SUP_NRT_V006_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRS2SUP_NRT_006",
            provider="GES_DISC", 
            shortname="AIRS2SUP_NRT",
            version="006",
            description="AIRS/Aqua L2 Near Real Time (NRT) Support Retrieval (AIRS-only) V006 (AIRS2SUP_NRT) at GES DISC version: 006"
        )

    AIRX2RET_V006_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRX2RET_006",
            provider="GES_DISC", 
            shortname="AIRX2RET",
            version="006",
            description="AIRS/Aqua L2 Standard Physical Retrieval (AIRS+AMSU) V006 (AIRX2RET) at GES DISC version: 006"
        )

    AIRH2RET_V006_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRH2RET_006",
            provider="GES_DISC", 
            shortname="AIRH2RET",
            version="006",
            description="AIRS/Aqua L2 Standard Physical Retrieval (AIRS+AMSU+HSB) V006 (AIRH2RET) at GES DISC version: 006"
        )

    AIRS2RET_V006_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRS2RET_006",
            provider="GES_DISC", 
            shortname="AIRS2RET",
            version="006",
            description="AIRS/Aqua L2 Standard Physical Retrieval (AIRS-only) V006 (AIRS2RET) at GES DISC version: 006"
        )

    AIRX2SUP_V006_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRX2SUP_006",
            provider="GES_DISC", 
            shortname="AIRX2SUP",
            version="006",
            description="AIRS/Aqua L2 Support Retrieval (AIRS+AMSU) V006 (AIRX2SUP) at GES DISC version: 006"
        )

    AIRH2SUP_V006_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRH2SUP_006",
            provider="GES_DISC", 
            shortname="AIRH2SUP",
            version="006",
            description="AIRS/Aqua L2 Support Retrieval (AIRS+AMSU+HSB) V006 (AIRH2SUP) at GES DISC version: 006"
        )

    AIRS2SUP_V006_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRS2SUP_006",
            provider="GES_DISC", 
            shortname="AIRS2SUP",
            version="006",
            description="AIRS/Aqua L2 Support Retrieval (AIRS-only) V006 (AIRS2SUP) at GES DISC version: 006"
        )

    AIRG2SSD_IRONLY_V006_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRG2SSD_IRonly_006",
            provider="GES_DISC", 
            shortname="AIRG2SSD_IRonly",
            version="006",
            description="AIRS/Aqua L2G Precipitation Estimate (AIRS-only) V006 (AIRG2SSD_IRonly) at GES DISC version: 006"
        )

    AIRG2SSD_IRONLY_V70_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRG2SSD_IRonly_7.0",
            provider="GES_DISC", 
            shortname="AIRG2SSD_IRonly",
            version="7.0",
            description="AIRS/Aqua L2G Precipitation Estimate (AIRS-only) V7.0 at GES DISC version: 7.0"
        )

    AIRG2SSD_V006_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRG2SSD_006",
            provider="GES_DISC", 
            shortname="AIRG2SSD",
            version="006",
            description="AIRS/Aqua L2G Precipitation Estimate V006 (AIRG2SSD) at GES DISC version: 006"
        )

    AIRX3QP5_V006_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRX3QP5_006",
            provider="GES_DISC", 
            shortname="AIRX3QP5",
            version="006",
            description="AIRS/Aqua L3 5-day Quantization in Physical Units (AIRS+AMSU) 5 degrees x 5 degrees V006 (AIRX3QP5) at GES DISC version: 006"
        )

    AIRH3QP5_V006_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRH3QP5_006",
            provider="GES_DISC", 
            shortname="AIRH3QP5",
            version="006",
            description="AIRS/Aqua L3 5-day Quantization in Physical Units (AIRS+AMSU+HSB) 5 degrees x 5 degrees V006 (AIRH3QP5) at GES DISC version: 006"
        )

    AIRS3QP5_V006_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRS3QP5_006",
            provider="GES_DISC", 
            shortname="AIRS3QP5",
            version="006",
            description="AIRS/Aqua L3 5-day Quantization in Physical Units (AIRS-only) 5 degrees x 5 degrees V006 (AIRS3QP5) at GES DISC version: 006"
        )

    AIRX3C28_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRX3C28_005",
            provider="GES_DISC", 
            shortname="AIRX3C28",
            version="005",
            description="AIRS/Aqua L3 8-day CO2 in the free troposphere (AIRS+AMSU) 2.5 degrees x 2 degrees V005 (AIRX3C28) at GES DISC version: 005"
        )

    AIRS3C28_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRS3C28_005",
            provider="GES_DISC", 
            shortname="AIRS3C28",
            version="005",
            description="AIRS/Aqua L3 8-day CO2 in the free troposphere (AIRS-only) 2.5 degrees x 2 degrees V005 (AIRS3C28) at GES DISC version: 005"
        )

    AIRX3ST8_V006_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRX3ST8_006",
            provider="GES_DISC", 
            shortname="AIRX3ST8",
            version="006",
            description="AIRS/Aqua L3 8-day Standard Physical Retrieval (AIRS+AMSU) 1 degree x 1 degree V006 (AIRX3ST8) at GES DISC version: 006"
        )

    AIRH3ST8_V006_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRH3ST8_006",
            provider="GES_DISC", 
            shortname="AIRH3ST8",
            version="006",
            description="AIRS/Aqua L3 8-day Standard Physical Retrieval (AIRS+AMSU+HSB) 1 degree x 1 degree V006 (AIRH3ST8) at GES DISC version: 006"
        )

    AIRS3ST8_V006_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRS3ST8_006",
            provider="GES_DISC", 
            shortname="AIRS3ST8",
            version="006",
            description="AIRS/Aqua L3 8-day Standard Physical Retrieval (AIRS-only) 1 degree X 1 degree V006 (AIRS3ST8) at GES DISC version: 006"
        )

    AIRX3SP8_V006_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRX3SP8_006",
            provider="GES_DISC", 
            shortname="AIRX3SP8",
            version="006",
            description="AIRS/Aqua L3 8-day Support Multiday Product (AIRS+AMSU) 1 degree x 1 degree V006 (AIRX3SP8) at GES DISC version: 006"
        )

    AIRH3SP8_V006_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRH3SP8_006",
            provider="GES_DISC", 
            shortname="AIRH3SP8",
            version="006",
            description="AIRS/Aqua L3 8-day Support Multiday Product (AIRS+AMSU+HSB) 1 degree x 1 degree V006 (AIRH3SP8) at GES DISC version: 006"
        )

    AIRS3SP8_V006_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRS3SP8_006",
            provider="GES_DISC", 
            shortname="AIRS3SP8",
            version="006",
            description="AIRS/Aqua L3 8-day Support Product (AIRS-only) 1 degree X 1 degree V006 (AIRS3SP8) at GES DISC version: 006"
        )

    AIRX3STD_V006_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRX3STD_006",
            provider="GES_DISC", 
            shortname="AIRX3STD",
            version="006",
            description="AIRS/Aqua L3 Daily Standard Physical Retrieval (AIRS+AMSU) 1 degree x 1 degree V006 (AIRX3STD) at GES DISC version: 006"
        )

    AIRH3STD_V006_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRH3STD_006",
            provider="GES_DISC", 
            shortname="AIRH3STD",
            version="006",
            description="AIRS/Aqua L3 Daily Standard Physical Retrieval (AIRS+AMSU+HSB) 1 degree x 1 degree V006 (AIRH3STD) at GES DISC version: 006"
        )

    AIRS3STD_V006_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRS3STD_006",
            provider="GES_DISC", 
            shortname="AIRS3STD",
            version="006",
            description="AIRS/Aqua L3 Daily Standard Physical Retrieval (AIRS-only) 1 degree x 1 degree V006 (AIRS3STD) at GES DISC version: 006"
        )

    AIRH3SPD_V006_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRH3SPD_006",
            provider="GES_DISC", 
            shortname="AIRH3SPD",
            version="006",
            description="AIRS/Aqua L3 Daily Support Daily Product (AIRS+AMSU+HSB) 1 degree x 1 degree V006 (AIRH3SPD) at GES DISC version: 006"
        )

    AIRX3SPD_V006_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRX3SPD_006",
            provider="GES_DISC", 
            shortname="AIRX3SPD",
            version="006",
            description="AIRS/Aqua L3 Daily Support Product (AIRS+AMSU) 1 degree x 1 degree V006 (AIRX3SPD) at GES DISC version: 006"
        )

    AIRS3SPD_V006_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRS3SPD_006",
            provider="GES_DISC", 
            shortname="AIRS3SPD",
            version="006",
            description="AIRS/Aqua L3 Daily Support Product (AIRS-only) 1 degree x 1 degree V006 (AIRS3SPD) at GES DISC version: 006"
        )

    AIRX3C2M_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRX3C2M_005",
            provider="GES_DISC", 
            shortname="AIRX3C2M",
            version="005",
            description="AIRS/Aqua L3 Monthly CO2 in the free troposphere (AIRS+AMSU) 2.5 degrees x 2 degrees V005 (AIRX3C2M) at GES DISC version: 005"
        )

    AIRS3C2M_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRS3C2M_005",
            provider="GES_DISC", 
            shortname="AIRS3C2M",
            version="005",
            description="AIRS/Aqua L3 Monthly CO2 in the free troposphere (AIRS-only) 2.5 degrees x 2 degrees V005 (AIRS3C2M) at GES DISC version: 005"
        )

    AIRX3QPM_V006_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRX3QPM_006",
            provider="GES_DISC", 
            shortname="AIRX3QPM",
            version="006",
            description="AIRS/Aqua L3 Monthly Quantization in Physical Units (AIRS+AMSU) 5 degrees x 5 degrees V006 (AIRX3QPM) at GES DISC version: 006"
        )

    AIRH3QPM_V006_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRH3QPM_006",
            provider="GES_DISC", 
            shortname="AIRH3QPM",
            version="006",
            description="AIRS/Aqua L3 Monthly Quantization in Physical Units (AIRS+AMSU+HSB) 5 degrees x 5 degrees V006 (AIRH3QPM) at GES DISC version: 006"
        )

    AIRS3QPM_V006_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRS3QPM_006",
            provider="GES_DISC", 
            shortname="AIRS3QPM",
            version="006",
            description="AIRS/Aqua L3 Monthly Quantization in Physical Units (AIRS-only) 5 degrees x 5 degrees V006 (AIRS3QPM) at GES DISC version: 006"
        )

    AIRX3STM_V006_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRX3STM_006",
            provider="GES_DISC", 
            shortname="AIRX3STM",
            version="006",
            description="AIRS/Aqua L3 Monthly Standard Physical Retrieval (AIRS+AMSU) 1 degree x 1 degree V006 (AIRX3STM) at GES DISC version: 006"
        )

    AIRH3STM_V006_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRH3STM_006",
            provider="GES_DISC", 
            shortname="AIRH3STM",
            version="006",
            description="AIRS/Aqua L3 Monthly Standard Physical Retrieval (AIRS+AMSU+HSB) 1 degree x 1 degree V006 (AIRH3STM) at GES DISC version: 006"
        )

    AIRS3STM_V006_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRS3STM_006",
            provider="GES_DISC", 
            shortname="AIRS3STM",
            version="006",
            description="AIRS/Aqua L3 Monthly Standard Physical Retrieval (AIRS-only) 1 degree x 1 degree V006 (AIRS3STM) at GES DISC version: 006"
        )

    AIRX3SPM_V006_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRX3SPM_006",
            provider="GES_DISC", 
            shortname="AIRX3SPM",
            version="006",
            description="AIRS/Aqua L3 Monthly Support Product (AIRS+AMSU) 1 degree x 1 degree V006 (AIRX3SPM) at GES DISC version: 006"
        )

    AIRH3SPM_V006_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRH3SPM_006",
            provider="GES_DISC", 
            shortname="AIRH3SPM",
            version="006",
            description="AIRS/Aqua L3 Monthly Support Product (AIRS+AMSU+HSB) 1 degree x 1 degree V006 (AIRH3SPM) at GES DISC version: 006"
        )

    AIRS3SPM_V006_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRS3SPM_006",
            provider="GES_DISC", 
            shortname="AIRS3SPM",
            version="006",
            description="AIRS/Aqua L3 Monthly Support Product (AIRS-only) 1 degree x 1 degree V006 (AIRS3SPM) at GES DISC version: 006"
        )

    AIRX3C2D_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRX3C2D_005",
            provider="GES_DISC", 
            shortname="AIRX3C2D",
            version="005",
            description="AIRS/Aqua L3 daily CO2 in the free troposphere (AIRS+AMSU) 2.5 degrees x 2 degrees V005 (AIRX3C2D) at GES DISC version: 005"
        )

    AIRS3C2D_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRS3C2D_005",
            provider="GES_DISC", 
            shortname="AIRS3C2D",
            version="005",
            description="AIRS/Aqua L3 daily CO2 in the free troposphere (AIRS-only) 2.5 degrees x 2 degrees V005 (AIRS3C2D) at GES DISC version: 005"
        )

    AMSRERR_CPR_V002_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AMSRERR_CPR_002",
            provider="GES_DISC", 
            shortname="AMSRERR_CPR",
            version="002",
            description="AMSR-E L2 Rainfall Subset, collocated with CloudSat track V002 (AMSERR_CPR) at GES DISC version: 002"
        )

    AMSRE_AVRMO_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AMSRE_AVRMO_005",
            provider="GES_DISC", 
            shortname="AMSRE_AVRMO",
            version="005",
            description="AMSR-E/Aqua level 3 global monthly Surface Soil Moisture Averages V005 (AMSRE_AVRMO) at GES DISC version: 005"
        )

    AMSRE_STDMO_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AMSRE_STDMO_005",
            provider="GES_DISC", 
            shortname="AMSRE_STDMO",
            version="005",
            description="AMSR-E/Aqua level 3 global monthly Surface Soil Moisture Standard Deviation V005 (AMSRE_STDMO) at GES DISC version: 005"
        )

    LPRM_AMSRE_SOILM2_V002_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_LPRM_AMSRE_SOILM2_002",
            provider="GES_DISC", 
            shortname="LPRM_AMSRE_SOILM2",
            version="002",
            description="AMSR-E/Aqua surface soil moisture (LPRM) L2B V002 (LPRM_AMSRE_SOILM2) at GES DISC version: 002"
        )

    LPRM_AMSRE_A_SOILM3_V002_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_LPRM_AMSRE_A_SOILM3_002",
            provider="GES_DISC", 
            shortname="LPRM_AMSRE_A_SOILM3",
            version="002",
            description="AMSR-E/Aqua surface soil moisture (LPRM) L3 1 day 25 km x 25 km ascending V002 (LPRM_AMSRE_A_SOILM3) at GES DISC version: 002"
        )

    LPRM_AMSRE_D_SOILM3_V002_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_LPRM_AMSRE_D_SOILM3_002",
            provider="GES_DISC", 
            shortname="LPRM_AMSRE_D_SOILM3",
            version="002",
            description="AMSR-E/Aqua surface soil moisture (LPRM) L3 1 day 25 km x 25 km descending V002 (LPRM_AMSRE_D_SOILM3) at GES DISC version: 002"
        )

    WC_LSMEM_SOILM_025_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_WC_LSMEM_SOILM_025_001",
            provider="GES_DISC", 
            shortname="WC_LSMEM_SOILM_025",
            version="001",
            description="AMSR-E/Aqua surface soil moisture (LSMEM) L3 1 day 0.25 degree x 0.25 degree V001 (WC_LSMEM_SOILM_025) at GES DISC version: 001"
        )

    AMDBLWV_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AMDBLWV_1",
            provider="GES_DISC", 
            shortname="AMDBLWV",
            version="1",
            description="AMSR-MODIS Boundary Layer Water Vapor L3 Daily 1 degree x 1 degree V1 (AMDBLWV) at GES DISC version: 1"
        )

    AMDBLWV_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AMDBLWV_2",
            provider="GES_DISC", 
            shortname="AMDBLWV",
            version="2",
            description="AMSR-MODIS Boundary Layer Water Vapor L3 Daily 1 degree x 1 degree V2 (AMDBLWV) at GES DISC version: 2"
        )

    AMMBLWV_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AMMBLWV_1",
            provider="GES_DISC", 
            shortname="AMMBLWV",
            version="1",
            description="AMSR-MODIS Boundary Layer Water Vapor L3 Monthly 1 degree x 1 degree V1 (AMMBLWV) at GES DISC version: 1"
        )

    AMMBLWV_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AMMBLWV_2",
            provider="GES_DISC", 
            shortname="AMMBLWV",
            version="2",
            description="AMSR-MODIS Boundary Layer Water Vapor L3 Monthly 1 degree x 1 degree V2 (AMMBLWV) at GES DISC version: 2"
        )

    LPRM_AMSR2_DS_SOILM2_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_LPRM_AMSR2_DS_SOILM2_001",
            provider="GES_DISC", 
            shortname="LPRM_AMSR2_DS_SOILM2",
            version="001",
            description="AMSR2/GCOM-W1 downscaled surface soil moisture (LPRM) L2B V001 (LPRM_AMSR2_DS_SOILM2) at GES DISC version: 001"
        )

    LPRM_AMSR2_SOILM2_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_LPRM_AMSR2_SOILM2_001",
            provider="GES_DISC", 
            shortname="LPRM_AMSR2_SOILM2",
            version="001",
            description="AMSR2/GCOM-W1 surface soil moisture (LPRM) L2B V001 (LPRM_AMSR2_SOILM2) at GES DISC version: 001"
        )

    LPRM_AMSR2_DS_A_SOILM3_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_LPRM_AMSR2_DS_A_SOILM3_001",
            provider="GES_DISC", 
            shortname="LPRM_AMSR2_DS_A_SOILM3",
            version="001",
            description="AMSR2/GCOM-W1 surface soil moisture (LPRM) L3 1 day 10 km x 10 km ascending V001 (LPRM_AMSR2_DS_A_SOILM3) at GES DISC version: 001"
        )

    LPRM_AMSR2_DS_D_SOILM3_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_LPRM_AMSR2_DS_D_SOILM3_001",
            provider="GES_DISC", 
            shortname="LPRM_AMSR2_DS_D_SOILM3",
            version="001",
            description="AMSR2/GCOM-W1 surface soil moisture (LPRM) L3 1 day 10 km x 10 km descending V001 (LPRM_AMSR2_DS_D_SOILM3) at GES DISC version: 001"
        )

    LPRM_AMSR2_A_SOILM3_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_LPRM_AMSR2_A_SOILM3_001",
            provider="GES_DISC", 
            shortname="LPRM_AMSR2_A_SOILM3",
            version="001",
            description="AMSR2/GCOM-W1 surface soil moisture (LPRM) L3 1 day 25 km x 25 km ascending V001 (LPRM_AMSR2_A_SOILM3) at GES DISC version: 001"
        )

    LPRM_AMSR2_D_SOILM3_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_LPRM_AMSR2_D_SOILM3_001",
            provider="GES_DISC", 
            shortname="LPRM_AMSR2_D_SOILM3",
            version="001",
            description="AMSR2/GCOM-W1 surface soil moisture (LPRM) L3 1 day 25 km x 25 km descending V001 (LPRM_AMSR2_D_SOILM3) at GES DISC version: 001"
        )

    ATMOSL1_V3_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ATMOSL1_3",
            provider="GES_DISC", 
            shortname="ATMOSL1",
            version="3",
            description="ATMOS L1 Spectra and Runlogs V3 (ATMOSL1) at GES DISC version: 3"
        )

    ATMOSL2AF_V3_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ATMOSL2AF_3",
            provider="GES_DISC", 
            shortname="ATMOSL2AF",
            version="3",
            description="ATMOS L2 Trace Gases on Altitude Grid, Fixed Field Format V3 (ATMOSL2AF) at GES DISC version: 3"
        )

    ATMOSL2AT_V3_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ATMOSL2AT_3",
            provider="GES_DISC", 
            shortname="ATMOSL2AT",
            version="3",
            description="ATMOS L2 Trace Gases on Altitude Grid, Tab Delimited Format V3 (ATMOSL2AT) at GES DISC version: 3"
        )

    ATMOSL2TF_V3_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ATMOSL2TF_3",
            provider="GES_DISC", 
            shortname="ATMOSL2TF",
            version="3",
            description="ATMOS L2 Trace Gases on Potential Temperature Grid, Fixed Field Format V3 (ATMOSL2TF) at GES DISC version: 3"
        )

    ATMOSL2TT_V3_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ATMOSL2TT_3",
            provider="GES_DISC", 
            shortname="ATMOSL2TT",
            version="3",
            description="ATMOS L2 Trace Gases on Potential Temperature Grid, Tab Delimited Format V3 (ATMOSL2TT) at GES DISC version: 3"
        )

    ATMOSL2PF_V3_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ATMOSL2PF_3",
            provider="GES_DISC", 
            shortname="ATMOSL2PF",
            version="3",
            description="ATMOS L2 Trace Gases on Pressure Grid, Fixed Field Format V3 (ATMOSL2PF) at GES DISC version: 3"
        )

    ATMOSL2PT_V3_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ATMOSL2PT_3",
            provider="GES_DISC", 
            shortname="ATMOSL2PT",
            version="3",
            description="ATMOS L2 Trace Gases on Pressure Grid, Tab Delimited Format V3 (ATMOSL2PT) at GES DISC version: 3"
        )

    ALAN_VIIRS_CONUS_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ALAN_VIIRS_CONUS_1",
            provider="GES_DISC", 
            shortname="ALAN_VIIRS_CONUS",
            version="1",
            description="Annual Summary of Artificial Light At Night from VIIRS/S-NPP at CONUS County and Census Tract V1 (ALAN_VIIRS_CONUS) at GES DISC version: 1"
        )

    SNDRAQIL2JSFRET_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDRAQIL2JSFRET_2",
            provider="GES_DISC", 
            shortname="SNDRAQIL2JSFRET",
            version="2",
            description="Aqua AIRS Level 2 JoSFRA Retrieval Standard: Atmosphere cloud and surface geophysical state per footprint V2 at GES DISC version: 2"
        )

    AIRSIL3MSOLR_V61_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRSIL3MSOLR_6.1",
            provider="GES_DISC", 
            shortname="AIRSIL3MSOLR",
            version="6.1",
            description="Aqua AIRS Level 3 Spectral Outgoing Longwave Radiation (OLR) Monthly version: 6.1"
        )

    AIRS_MLS_IND_V10_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRS_MLS_IND_1.0",
            provider="GES_DISC", 
            shortname="AIRS_MLS_IND",
            version="1.0",
            description="Aqua AIRS-MLS Matchup Indexes V1.0 (AIRS_MLS_IND) at GES_DISC version: 1.0"
        )

    AQUA_AIRS_MODIS1KM_IND_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_Aqua_AIRS_MODIS1km_IND_1",
            provider="GES_DISC", 
            shortname="Aqua_AIRS_MODIS1km_IND",
            version="1",
            description="Aqua AIRS-MODIS 1-km Matchup Indexes V1 (Aqua_AIRS_MODIS1km_IND) at GES_DISC version: 1"
        )

    AIRS_MDS_IND_V10_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRS_MDS_IND_1.0",
            provider="GES_DISC", 
            shortname="AIRS_MDS_IND",
            version="1.0",
            description="Aqua AIRS-MODIS Matchup Indexes V1.0 (AIRS_MDS_IND) at GES_DISC version: 1.0"
        )

    AIRX2RET_V70_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRX2RET_7.0",
            provider="GES_DISC", 
            shortname="AIRX2RET",
            version="7.0",
            description="Aqua/AIRS L2 Standard Physical Retrieval (AIRS+AMSU) V7.0 at GES DISC version: 7.0"
        )

    AIRX2SUP_V70_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRX2SUP_7.0",
            provider="GES_DISC", 
            shortname="AIRX2SUP",
            version="7.0",
            description="Aqua/AIRS L2 Support Retrieval (AIRS+AMSU) V7.0 at GES DISC version: 7.0"
        )

    AIRI2CCF_V70_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRI2CCF_7.0",
            provider="GES_DISC", 
            shortname="AIRI2CCF",
            version="7.0",
            description="Aqua/AIRS L2 Cloud-Cleared Infrared Radiances (AIRS+AMSU) V7.0 at GES DISC version: 7.0"
        )

    AIRH2CCF_V70_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRH2CCF_7.0",
            provider="GES_DISC", 
            shortname="AIRH2CCF",
            version="7.0",
            description="Aqua/AIRS L2 Cloud-Cleared Infrared Radiances (AIRS+AMSU+HSB) V7.0 at GES DISC version: 7.0"
        )

    AIRS2CCF_V70_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRS2CCF_7.0",
            provider="GES_DISC", 
            shortname="AIRS2CCF",
            version="7.0",
            description="Aqua/AIRS L2 Cloud-Cleared Infrared Radiances (AIRS-only) V7.0 at GES DISC version: 7.0"
        )

    AIRS2CCF_NRT_V70_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRS2CCF_NRT_7.0",
            provider="GES_DISC", 
            shortname="AIRS2CCF_NRT",
            version="7.0",
            description="Aqua/AIRS L2 Near Real Time (NRT) Cloud-Cleared Infrared Radiances (AIRS-only) V7.0 at GES DISC version: 7.0"
        )

    AIRS2RET_NRT_V70_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRS2RET_NRT_7.0",
            provider="GES_DISC", 
            shortname="AIRS2RET_NRT",
            version="7.0",
            description="Aqua/AIRS L2 Near Real Time (NRT) Standard Physical Retrieval (AIRS-only) V7.0 at GES DISC version: 7.0"
        )

    AIRS2SUP_NRT_V70_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRS2SUP_NRT_7.0",
            provider="GES_DISC", 
            shortname="AIRS2SUP_NRT",
            version="7.0",
            description="Aqua/AIRS L2 Near Real Time (NRT) Support Retrieval (AIRS-only) V7.0 at GES DISC version: 7.0"
        )

    AIRH2RET_V70_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRH2RET_7.0",
            provider="GES_DISC", 
            shortname="AIRH2RET",
            version="7.0",
            description="Aqua/AIRS L2 Standard Physical Retrieval (AIRS+AMSU+HSB) V7.0 at GES DISC version: 7.0"
        )

    AIRS2RET_V70_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRS2RET_7.0",
            provider="GES_DISC", 
            shortname="AIRS2RET",
            version="7.0",
            description="Aqua/AIRS L2 Standard Physical Retrieval (AIRS-only) V7.0 at GES DISC version: 7.0"
        )

    AIRH2SUP_V70_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRH2SUP_7.0",
            provider="GES_DISC", 
            shortname="AIRH2SUP",
            version="7.0",
            description="Aqua/AIRS L2 Support Retrieval (AIRS+AMSU+HSB) V7.0 at GES DISC version: 7.0"
        )

    AIRS2SUP_V70_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRS2SUP_7.0",
            provider="GES_DISC", 
            shortname="AIRS2SUP",
            version="7.0",
            description="Aqua/AIRS L2 Support Retrieval (AIRS-only) V7.0 at GES DISC version: 7.0"
        )

    AIRX3STD_V70_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRX3STD_7.0",
            provider="GES_DISC", 
            shortname="AIRX3STD",
            version="7.0",
            description="Aqua/AIRS L3 Daily Standard Physical Retrieval (AIRS+AMSU) 1 degree x 1 degree V7.0 at GES DISC version: 7.0"
        )

    AIRH3STD_V70_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRH3STD_7.0",
            provider="GES_DISC", 
            shortname="AIRH3STD",
            version="7.0",
            description="Aqua/AIRS L3 Daily Standard Physical Retrieval (AIRS+AMSU+HSB) 1 degree x 1 degree V7.0 at GES DISC version: 7.0"
        )

    AIRS3STD_V70_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRS3STD_7.0",
            provider="GES_DISC", 
            shortname="AIRS3STD",
            version="7.0",
            description="Aqua/AIRS L3 Daily Standard Physical Retrieval (AIRS-only) 1 degree x 1 degree V7.0 at GES DISC version: 7.0"
        )

    AIRH3SPD_V70_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRH3SPD_7.0",
            provider="GES_DISC", 
            shortname="AIRH3SPD",
            version="7.0",
            description="Aqua/AIRS L3 Daily Support Daily Product (AIRS+AMSU+HSB) 1 degree x 1 degree V7.0 at GES DISC version: 7.0"
        )

    AIRX3SPD_V70_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRX3SPD_7.0",
            provider="GES_DISC", 
            shortname="AIRX3SPD",
            version="7.0",
            description="Aqua/AIRS L3 Daily Support Product (AIRS+AMSU) 1 degree x 1 degree V7.0 at GES DISC version: 7.0"
        )

    AIRS3SPD_V70_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRS3SPD_7.0",
            provider="GES_DISC", 
            shortname="AIRS3SPD",
            version="7.0",
            description="Aqua/AIRS L3 Daily Support Product (AIRS-only) 1 degree x 1 degree V7.0 at GES DISC version: 7.0"
        )

    AIRX3STM_V70_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRX3STM_7.0",
            provider="GES_DISC", 
            shortname="AIRX3STM",
            version="7.0",
            description="Aqua/AIRS L3 Monthly Standard Physical Retrieval (AIRS+AMSU) 1 degree x 1 degree V7.0 at GES DISC version: 7.0"
        )

    AIRH3STM_V70_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRH3STM_7.0",
            provider="GES_DISC", 
            shortname="AIRH3STM",
            version="7.0",
            description="Aqua/AIRS L3 Monthly Standard Physical Retrieval (AIRS+AMSU+HSB) 1 degree x 1 degree V7.0 at GES DISC version: 7.0"
        )

    AIRS3STM_V70_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRS3STM_7.0",
            provider="GES_DISC", 
            shortname="AIRS3STM",
            version="7.0",
            description="Aqua/AIRS L3 Monthly Standard Physical Retrieval (AIRS-only) 1 degree x 1 degree V7.0 at GES DISC version: 7.0"
        )

    AIRH3SPM_V70_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRH3SPM_7.0",
            provider="GES_DISC", 
            shortname="AIRH3SPM",
            version="7.0",
            description="Aqua/AIRS L3 Monthly Support Monthly Product (AIRS+AMSU+HSB) 1 degree x 1 degree V7.0 at GES DISC version: 7.0"
        )

    AIRX3SPM_V70_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRX3SPM_7.0",
            provider="GES_DISC", 
            shortname="AIRX3SPM",
            version="7.0",
            description="Aqua/AIRS L3 Monthly Support Product (AIRS+AMSU) 1 degree x 1 degree V7.0 at GES DISC version: 7.0"
        )

    AIRS3SPM_V70_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRS3SPM_7.0",
            provider="GES_DISC", 
            shortname="AIRS3SPM",
            version="7.0",
            description="Aqua/AIRS L3 Monthly Support Product (AIRS-only) 1 degree x 1 degree V7.0 at GES DISC version: 7.0"
        )

    RAIN_ARKIN_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_RAIN_ARKIN_1",
            provider="GES_DISC", 
            shortname="RAIN_ARKIN",
            version="1",
            description="Arkin and Janowiak GPI: IR -Based Monthly Rainfall for the GPCP 2.5 x 2.5 degree V1 (RAIN_ARKIN) at GES DISC version: 1"
        )

    AIRSAC3MNH3_V3_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_AIRSAC3MNH3_3",
            provider="GES_DISC", 
            shortname="AIRSAC3MNH3",
            version="3",
            description="Atmospheric Composition Ammonia Volume Mixing Ratio L3 (AIRSAC3MNH3 V3) from AIRS/AMSU on NASA Aqua at GES DISC version: 3"
        )

    BUVN4L1DCM_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_BUVN4L1DCM_001",
            provider="GES_DISC", 
            shortname="BUVN4L1DCM",
            version="001",
            description="BUV/Nimbus-4 Dark Current Study Master Data V001 (BUVN4L1DCM) at GES DISC version: 001"
        )

    BUVN4L1DCW_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_BUVN4L1DCW_001",
            provider="GES_DISC", 
            shortname="BUVN4L1DCW",
            version="001",
            description="BUV/Nimbus-4 Dark Current Study Working Data V001 (BUVN4L1DCW) at GES DISC version: 001"
        )

    BUVN4L1RUT_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_BUVN4L1RUT_001",
            provider="GES_DISC", 
            shortname="BUVN4L1RUT",
            version="001",
            description="BUV/Nimbus-4 Level 1 Radiance Data V001 (BUVN4L1RUT) at GES DISC version: 001"
        )

    BUVN4L1PDB_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_BUVN4L1PDB_001",
            provider="GES_DISC", 
            shortname="BUVN4L1PDB",
            version="001",
            description="BUV/Nimbus-4 Level 1 Radiance and Housekeeping Data in Telemetry Units V001 (BUVN4L1PDB) at GES DISC version: 001"
        )

    BUVN4L2CPOZ_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_BUVN4L2CPOZ_005",
            provider="GES_DISC", 
            shortname="BUVN4L2CPOZ",
            version="005",
            description="BUV/Nimbus-4 Level 2 Compressed Ozone Profile Data V005 (BUVN4L2CPOZ) at GES DISC version: 005"
        )

    BUVN4L2HDBUV_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_BUVN4L2HDBUV_005",
            provider="GES_DISC", 
            shortname="BUVN4L2HDBUV",
            version="005",
            description="BUV/Nimbus-4 Level 2 High-Density Ozone Data V005 (BUVN4L2HDBUV) at GES DISC version: 005"
        )

    BUVN4L3ZMT_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_BUVN4L3ZMT_005",
            provider="GES_DISC", 
            shortname="BUVN4L3ZMT",
            version="005",
            description="BUV/Nimbus-4 Level 3 Ozone Zonal Means V005 (BUVN4L3ZMT) at GES DISC version: 005"
        )

    BUVN04L2_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_BUVN04L2_1",
            provider="GES_DISC", 
            shortname="BUVN04L2",
            version="1",
            description="BUV/Nimbus-4 Ozone (O3) Nadir Profile and Total Column 1 Day L2 V1 (BUVN04L2) at GES DISC version: 1"
        )

    BUVN04L3ZM_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_BUVN04L3zm_1",
            provider="GES_DISC", 
            shortname="BUVN04L3zm",
            version="1",
            description="BUV/Nimbus-4 Ozone (O3) Profile and Total Column Ozone 1 Month Zonal Mean L3 Global 5.0 degree Latitude Zones V1 (BUVN04L3zm) at GES DISC version: 1"
        )

    CAR_ARCTAS_L1C_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_CAR_ARCTAS_L1C_1",
            provider="GES_DISC", 
            shortname="CAR_ARCTAS_L1C",
            version="1",
            description="CAR ARCTAS Arctic Research of the Composition of the Troposphere from Aircraft and Satellites L1 V1 (CAR_ARCTAS_L1C) at GES DISC version: 1"
        )

    CAR_ARCTAS_BRDF_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_CAR_ARCTAS_BRDF_2",
            provider="GES_DISC", 
            shortname="CAR_ARCTAS_BRDF",
            version="2",
            description="CAR ARCTAS BRDF Measurements V2 (CAR_ARCTAS_BRDF) at GES DISC version: 2"
        )

    CAR_ARMCAS_BRDF_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_CAR_ARMCAS_BRDF_2",
            provider="GES_DISC", 
            shortname="CAR_ARMCAS_BRDF",
            version="2",
            description="CAR ARMCAS Arctic Cloud BRDF Measurements V2 (CAR_ARMCAS_BRDF) at GES DISC version: 2"
        )

    CAR_ARMCAS_L1C_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_CAR_ARMCAS_L1C_1",
            provider="GES_DISC", 
            shortname="CAR_ARMCAS_L1C",
            version="1",
            description="CAR ARMCAS Arctic Cloud Radiation Measurements L1 V1 (CAR_ARMCAS_L1C) at GES DISC version: 1"
        )

    CAR_CLAMS_BRDF_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_CAR_CLAMS_BRDF_2",
            provider="GES_DISC", 
            shortname="CAR_CLAMS_BRDF",
            version="2",
            description="CAR CLAMS BRDF Measurements V2 (CAR_CLAMS_BRDF) at GES DISC version: 2"
        )

    CAR_CLASIC_BRDF_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_CAR_CLASIC_BRDF_2",
            provider="GES_DISC", 
            shortname="CAR_CLASIC_BRDF",
            version="2",
            description="CAR CLASIC BRDF Measurements V2 (CAR_CLASIC_BRDF) at GES DISC version: 2"
        )

    CAR_CLASIC_L1C_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_CAR_CLASIC_L1C_1",
            provider="GES_DISC", 
            shortname="CAR_CLASIC_L1C",
            version="1",
            description="CAR CLASIC Cloud and Land Surface Measurements L1 V1 (CAR_CLASIC_L1C) at GES DISC version: 1"
        )

    CAR_CLAMS_L1C_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_CAR_CLAMS_L1C_1",
            provider="GES_DISC", 
            shortname="CAR_CLAMS_L1C",
            version="1",
            description="CAR Clams Chesapeake Lighthouse Aircraft Ocean Measurements L1 V1 (CAR_CLAMS_L1C) at GES DISC version: 1"
        )

    CAR_DISCOVERAQ_L1C_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_CAR_DISCOVERAQ_L1C_1",
            provider="GES_DISC", 
            shortname="CAR_DISCOVERAQ_L1C",
            version="1",
            description="CAR Discover AQ Air Quality L1 V1 (CAR_DISCOVERAQ_L1C) at GES DISC version: 1"
        )

    CAR_DISCOVERAQ_BRDF_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_CAR_DISCOVERAQ_BRDF_2",
            provider="GES_DISC", 
            shortname="CAR_DISCOVERAQ_BRDF",
            version="2",
            description="CAR Discover AQ BRDF Measurements V2 (CAR_DISCOVERAQ_BRDF_2) version: 2"
        )

    CAR_ECO3D_BRDF_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_CAR_ECO3D_BRDF_2",
            provider="GES_DISC", 
            shortname="CAR_ECO3D_BRDF",
            version="2",
            description="CAR ECO3D BRDF Measurements V2 (CAR_ECO3D_BRDF) at GES DISC version: 2"
        )

    CAR_ECO3D_L1C_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_CAR_ECO3D_L1C_1",
            provider="GES_DISC", 
            shortname="CAR_ECO3D_L1C",
            version="1",
            description="CAR Eco-3D Vegetation Response to Changing Forcing Factors L1 V1 (CAR_ECO3D_L1C) at GES DISC version: 1"
        )

    CAR_FIREACE_BRDF_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_CAR_FIREACE_BRDF_2",
            provider="GES_DISC", 
            shortname="CAR_FIREACE_BRDF",
            version="2",
            description="CAR FIREACE Arctic Ice and Cloud Radiation BRDF V2 (CAR_FIREACE_BRDF) at GES DISC version: 2"
        )

    CAR_FIREACE_L1C_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_CAR_FIREACE_L1C_1",
            provider="GES_DISC", 
            shortname="CAR_FIREACE_L1C",
            version="1",
            description="CAR FIREACE Arctic Ice and Cloud Radiation L1 V1 (CAR_FIREACE_L1C) at GES DISC version: 1"
        )

    CAR_INTEXB_L1C_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_CAR_INTEXB_L1C_1",
            provider="GES_DISC", 
            shortname="CAR_INTEXB_L1C",
            version="1",
            description="CAR INTEX-B Long-range Pollution Transportation L1 V1 (CAR_INTEXB_L1C) at GES DISC version: 1"
        )

    CAR_INTEXB_BRDF_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_CAR_INTEXB_BRDF_2",
            provider="GES_DISC", 
            shortname="CAR_INTEXB_BRDF",
            version="2",
            description="CAR INTEXB BRDF Measurements L1 V2 (CAR_INTEXB_BRDF) at GES DISC version: 2"
        )

    CAR_KUWAITOILFIRE_BRDF_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_CAR_KUWAITOILFIRE_BRDF_2",
            provider="GES_DISC", 
            shortname="CAR_KUWAITOILFIRE_BRDF",
            version="2",
            description="CAR Kuwait Oil Fire BRDF V2 (CAR_KUWAITOILFIRE_BRDF) at GES DISC version: 2"
        )

    CAR_KUWAITOILFIRE_L1C_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_CAR_KUWAITOILFIRE_L1C_1",
            provider="GES_DISC", 
            shortname="CAR_KUWAITOILFIRE_L1C",
            version="1",
            description="CAR Kuwait Oil Fire Spectral Reflectance L1 V1 (CAR_KUWAITOILFIRE_L1C) at GES DISC version: 1"
        )

    CAR_LEADEX_BRDF_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_CAR_LEADEX_BRDF_2",
            provider="GES_DISC", 
            shortname="CAR_LEADEX_BRDF",
            version="2",
            description="CAR LEADEX Arctic Sea Ice and Tundra BRDF Measurements L1 V2 (CAR_LEADEX_BRDF) at GES DISC version: 2"
        )

    CAR_LEADEX_L1C_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_CAR_LEADEX_L1C_1",
            provider="GES_DISC", 
            shortname="CAR_LEADEX_L1C",
            version="1",
            description="CAR LEADEX Arctic Sea Ice and Tundra Radiation Measurements L1 V1 (CAR_LEADEX_L1C) at GES DISC version: 1"
        )

    CAR_SCARA_BRDF_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_CAR_SCARA_BRDF_2",
            provider="GES_DISC", 
            shortname="CAR_SCARA_BRDF",
            version="2",
            description="CAR SCAR-A Sulfates, Clouds, and Radiation-Atlantic BRDF Measurements BRDF V2 (CAR_SCARA_BRDF) at GES DISC version: 2"
        )

    CAR_SCARA_L1C_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_CAR_SCARA_L1C_1",
            provider="GES_DISC", 
            shortname="CAR_SCARA_L1C",
            version="1",
            description="CAR SCAR-A Sulfates, Clouds, and Radiation-Atlantic L1 V1 (CAR_SCARA_L1C) at GES DISC version: 1"
        )

    CAR_SCARB_BRDF_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_CAR_SCARB_BRDF_2",
            provider="GES_DISC", 
            shortname="CAR_SCARB_BRDF",
            version="2",
            description="CAR SCAR-B BRDF Measurements L1 V2 (CAR_SCARB_BRDF) at GES DISC version: 2"
        )

    CAR_SCARB_L1C_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_CAR_SCARB_L1C_1",
            provider="GES_DISC", 
            shortname="CAR_SCARB_L1C",
            version="1",
            description="CAR SCAR-B Smoke, Clouds, and Radiation-Brazil L1 V1 (CAR_SCARB_L1C) at GES DISC version: 1"
        )

    CAR_SKUKUZA_BRDF_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_CAR_SKUKUZA_BRDF_2",
            provider="GES_DISC", 
            shortname="CAR_SKUKUZA_BRDF",
            version="2",
            description="CAR SKUKUZA BRDF Measurements L1 V2 (CAR_SKUKUZA_BRDF) at GES DISC version: 2"
        )

    CAR_SAFARI_BRDF_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_CAR_SAFARI_BRDF_2",
            provider="GES_DISC", 
            shortname="CAR_SAFARI_BRDF",
            version="2",
            description="CAR Safari BRDF Measurements L1 V2 (CAR_SAFARI_BRDF) at GES DISC version: 2"
        )

    CAR_SAFARI_L1C_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_CAR_SAFARI_L1C_1",
            provider="GES_DISC", 
            shortname="CAR_SAFARI_L1C",
            version="1",
            description="CAR Safari South African Biogeophysics and Biogeochemistry L1 V1 (CAR_SAFARI_L1C) at GES DISC version: 1"
        )

    CAR_SKUKUZA_L1C_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_CAR_SKUKUZA_L1C_1",
            provider="GES_DISC", 
            shortname="CAR_SKUKUZA_L1C",
            version="1",
            description="CAR Skukuza South African Ecosystems L1 V1 (CAR_SKUKUZA_L1C) at GES DISC version: 1"
        )

    CAR_SNOWEX17_BRDF_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_CAR_SNOWEX17_BRDF_2",
            provider="GES_DISC", 
            shortname="CAR_SNOWEX17_BRDF",
            version="2",
            description="CAR SnowEx17 BRDF Measurements L1 V2 (CAR_SNOWEX17_BRDF) at GES DISC version: 2"
        )

    CAR_SNOWEX17_L1C_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_CAR_SNOWEX17_L1C_1",
            provider="GES_DISC", 
            shortname="CAR_SNOWEX17_L1C",
            version="1",
            description="CAR SnowEx17 Snow Mass and Energy Measurements L1 V1 (CAR_SNOWEX17_L1C) at GES DISC version: 1"
        )

    CAR_TARFOX_BRDF_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_CAR_TARFOX_BRDF_2",
            provider="GES_DISC", 
            shortname="CAR_TARFOX_BRDF",
            version="2",
            description="CAR TARFOX Tropospheric Aerosol Experiment BRDF V2 (CAR_TARFOX_BRDF) at GES DISC version: 2"
        )

    CAR_TARFOX_L1C_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_CAR_TARFOX_L1C_1",
            provider="GES_DISC", 
            shortname="CAR_TARFOX_L1C",
            version="1",
            description="CAR TARFOX Tropospheric Aerosol Radiative Forcing Observational Experiment L1 V1 (CAR_TARFOX_L1C) at GES DISC version: 1"
        )

    CMS_CH4_FLX_NA_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_CMS_CH4_FLX_NA_1",
            provider="GES_DISC", 
            shortname="CMS_CH4_FLX_NA",
            version="1",
            description="CMS (Carbon Monitoring System) Methane (CH4) Flux for North America 0.5 degree x 0.667 degree V1 (CMS_CH4_FLX_NA) at GES DISC version: 1"
        )

    CMS_GO_CH4_SEC_TDYC_NA_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_CMS_GO_CH4_SEC_TDYC_NA_1",
            provider="GES_DISC", 
            shortname="CMS_GO_CH4_SEC_TDYC_NA",
            version="1",
            description="CMS GOSAT and ObsPack L4 Top-down yearly methane emissions for individual sectors at 0.5x0.625 degrees for North America V1 (CMS_GO_CH4_SEC_TDYC_NA) version: 1"
        )

    CMSFLUXFOSSILFUELPRIOR_V3_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_CMSFluxFossilFuelPrior_3",
            provider="GES_DISC", 
            shortname="CMSFluxFossilFuelPrior",
            version="3",
            description="Carbon Monitoring System Carbon Flux FossilFuel Prior L4 V3 (CMSFluxFossilFuelPrior) version: 3"
        )

    CMSFLUXLANDPRIOR_V3_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_CMSFluxLandPrior_3",
            provider="GES_DISC", 
            shortname="CMSFluxLandPrior",
            version="3",
            description="Carbon Monitoring System Carbon Flux Land Prior L4 V3 (CMSFluxLandPrior) version: 3"
        )

    CMSFLUXNBE_V3_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_CMSFluxNBE_3",
            provider="GES_DISC", 
            shortname="CMSFluxNBE",
            version="3",
            description="Carbon Monitoring System Carbon Flux NBE L4 V3 (CMSFluxNBE) version: 3"
        )

    CMSFLUXOCEAN_V3_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_CMSFluxOcean_3",
            provider="GES_DISC", 
            shortname="CMSFluxOcean",
            version="3",
            description="Carbon Monitoring System Carbon Flux Ocean L4 V3 (CMSFluxOcean) version: 3"
        )

    CMSFLUXOCEANPRIOR_V3_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_CMSFluxOceanPrior_3",
            provider="GES_DISC", 
            shortname="CMSFluxOceanPrior",
            version="3",
            description="Carbon Monitoring System Carbon Flux Ocean Prior L4 V3 (CMSFluxOceanPrior) version: 3"
        )

    CMSFLUXTOTAL_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_CMSFluxTotal_2",
            provider="GES_DISC", 
            shortname="CMSFluxTotal",
            version="2",
            description="Carbon Monitoring System Carbon Flux Total L4 V2 (CMSFluxTotal) at GES DISC version: 2"
        )

    CMSFLUXTOTAL_V3_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_CMSFluxTotal_3",
            provider="GES_DISC", 
            shortname="CMSFluxTotal",
            version="3",
            description="Carbon Monitoring System Carbon Flux Total L4 V3 (CMSFluxTotal) version: 3"
        )

    CMSFLUXTOTALPRIOR_V3_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_CMSFluxTotalPrior_3",
            provider="GES_DISC", 
            shortname="CMSFluxTotalPrior",
            version="3",
            description="Carbon Monitoring System Carbon Flux Total Prior L4 V3 (CMSFluxTotalPrior) version: 3"
        )

    CMSFLUXFIRE_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_CMSFluxFire_1",
            provider="GES_DISC", 
            shortname="CMSFluxFire",
            version="1",
            description="Carbon Monitoring System Carbon Flux for Fire L4 V1 (CMSFluxFire) at GES DISC version: 1"
        )

    CMSFLUXFIRE_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_CMSFluxFire_2",
            provider="GES_DISC", 
            shortname="CMSFluxFire",
            version="2",
            description="Carbon Monitoring System Carbon Flux for Fire L4 V2 (CMSFluxFire) at GES DISC version: 2"
        )

    CMSFLUXFOSSILFUELPRIOR_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_CMSFluxFossilFuelPrior_2",
            provider="GES_DISC", 
            shortname="CMSFluxFossilFuelPrior",
            version="2",
            description="Carbon Monitoring System Carbon Flux for Fossil Fuel Prior L4 V2 (CMSFluxFossilFuelPrior) at GES DISC version: 2"
        )

    CMSFLUXOCEANPRIOR_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_CMSFluxOceanPrior_2",
            provider="GES_DISC", 
            shortname="CMSFluxOceanPrior",
            version="2",
            description="Carbon Monitoring System Carbon Flux for Ocean Prior L4 V2 (CMSFluxOceanPrior) at GES DISC version: 2"
        )

    CMSFLUXNBE_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_CMSFluxNBE_2",
            provider="GES_DISC", 
            shortname="CMSFluxNBE",
            version="2",
            description="Carbon Monitoring System Carbon Flux from the Net Biome Exchange L4 V2 (CMSFluxNBE) at GES DISC version: 2"
        )

    CMSFLUXNBEPRIOR_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_CMSFluxNBEPrior_2",
            provider="GES_DISC", 
            shortname="CMSFluxNBEPrior",
            version="2",
            description="Carbon Monitoring System Carbon Flux from the Net Biome Exchange Prior L4 V2 (CMSFluxNBEPrior) at GES DISC version: 2"
        )

    CMSFLUXFOSSILFUEL_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_CMSFluxFossilfuel_1",
            provider="GES_DISC", 
            shortname="CMSFluxFossilfuel",
            version="1",
            description="Carbon Monitoring System Flux for Fossil Fuel L4 V1 (CMSFluxFossilfuel) at GES DISC version: 1"
        )

    CMSFLUXOCEAN_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_CMSFluxOcean_1",
            provider="GES_DISC", 
            shortname="CMSFluxOcean",
            version="1",
            description="Carbon Monitoring System Flux for Ocean Carbon L4 V1 (CMSFluxOcean) at GES DISC version: 1"
        )

    CMSFLUXFIREPOST_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_CMSFluxFirepost_1",
            provider="GES_DISC", 
            shortname="CMSFluxFirepost",
            version="1",
            description="Carbon Monitoring System Flux for Posterior Fire Carbon L4 V1 (CMSFluxFirepost) at GES DISC version: 1"
        )

    CMSFLUXTOTALPOST_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_CMSFluxTotalpost_1",
            provider="GES_DISC", 
            shortname="CMSFluxTotalpost",
            version="1",
            description="Carbon Monitoring System Flux for Posterior Total Carbon L4 V1 (CMSFluxTotalpost) at GES DISC version: 1"
        )

    CMSFLUXTOTALPRIOR_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_CMSFluxTotalprior_1",
            provider="GES_DISC", 
            shortname="CMSFluxTotalprior",
            version="1",
            description="Carbon Monitoring System Flux for Prior Total Carbon L4 V1 (CMSFluxTotalprior) at GES DISC version: 1"
        )

    CMSFLUXMISC_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_CMSFluxMISC_1",
            provider="GES_DISC", 
            shortname="CMSFluxMISC",
            version="1",
            description="Carbon Monitoring System Flux for Shipping, Aviation, and Chemical Sources L4 V1 (CMSFluxMISC) at GES DISC version: 1"
        )

    CMSFLUXNEE_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_CMSFluxNEE_1",
            provider="GES_DISC", 
            shortname="CMSFluxNEE",
            version="1",
            description="Carbon Monitoring System Flux from the Net Ecosystem Exchange L4 V1 (CMSFluxNEE) at GES DISC version: 1"
        )

    CMSLAKEHURONPPM_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_CMSLakeHuronPPM_1",
            provider="GES_DISC", 
            shortname="CMSLakeHuronPPM",
            version="1",
            description="Carbon Monitoring System Lake Huron Primary Production Monthly V1 (CMSLakeHuronPPM) at GES DISC version: 1"
        )

    CMSLAKEHURONPPY_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_CMSLakeHuronPPY_1",
            provider="GES_DISC", 
            shortname="CMSLakeHuronPPY",
            version="1",
            description="Carbon Monitoring System Lake Huron Primary Production Yearly V1 (CMSLakeHuronPPY) at GES DISC version: 1"
        )

    CMSLAKEMICHIGANPPM_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_CMSLakeMichiganPPM_1",
            provider="GES_DISC", 
            shortname="CMSLakeMichiganPPM",
            version="1",
            description="Carbon Monitoring System Lake Michigan Primary Production Monthly V1 (CMSLakeMichiganPPM) at GES DISC version: 1"
        )

    CMSLAKEMICHIGANPPY_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_CMSLakeMichiganPPY_1",
            provider="GES_DISC", 
            shortname="CMSLakeMichiganPPY",
            version="1",
            description="Carbon Monitoring System Lake Michigan Primary Production Yearly V1 (CMSLakeMichiganPPY) at GES DISC version: 1"
        )

    CMSLAKESUPERIORPPM_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_CMSLakeSuperiorPPM_1",
            provider="GES_DISC", 
            shortname="CMSLakeSuperiorPPM",
            version="1",
            description="Carbon Monitoring System Lake Superior Primary Production Monthly V1 (CMSLakeSuperiorPPM) at GES DISC version: 1"
        )

    CMSLAKESUPERIORPPY_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_CMSLakeSuperiorPPY_1",
            provider="GES_DISC", 
            shortname="CMSLakeSuperiorPPY",
            version="1",
            description="Carbon Monitoring System Lake Superior Primary Production Yearly V1 (CMSLakeSuperiorPPY) at GES DISC version: 1"
        )

    CMS_CTL_NA_GOSAT_FOOTPRINTS_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_CMS_CTL_NA_GOSAT_FOOTPRINTS_1",
            provider="GES_DISC", 
            shortname="CMS_CTL_NA_GOSAT_FOOTPRINTS",
            version="1",
            description="CarbonTracker-Lagrange North America GOSAT Vertical Profile of Footprints V1 (CMS_CTL_NA_GOSAT_FOOTPRINTS) version: 1"
        )

    CMS_CTL_NA_OCO2_FOOTPRINTS_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_CMS_CTL_NA_OCO2_FOOTPRINTS_1",
            provider="GES_DISC", 
            shortname="CMS_CTL_NA_OCO2_FOOTPRINTS",
            version="1",
            description="CarbonTracker-Lagrange North America OCO-2 Vertical Profile of Footprints V1 (CMS_CTL_NA_OCO2_FOOTPRINTS) version: 1"
        )

    CMS_CTL_NA_TCCON_FOOTPRINTS_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_CMS_CTL_NA_TCCON_FOOTPRINTS_1",
            provider="GES_DISC", 
            shortname="CMS_CTL_NA_TCCON_FOOTPRINTS",
            version="1",
            description="CarbonTracker-Lagrange North America TCCON Vertical Profile of Footprints V1 (CMS_CTL_NA_TCCON_FOOTPRINTS) version: 1"
        )

    CMS_CTL_SA_OCO2_FOOTPRINTS_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_CMS_CTL_SA_OCO2_FOOTPRINTS_1",
            provider="GES_DISC", 
            shortname="CMS_CTL_SA_OCO2_FOOTPRINTS",
            version="1",
            description="CarbonTracker-Lagrange South America OCO-2 Vertical Profile of Footprints V1 (CMS_CTL_SA_OCO2_FOOTPRINTS) version: 1"
        )

    RAIN_CHANG_V23_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_RAIN_CHANG_2.3",
            provider="GES_DISC", 
            shortname="RAIN_CHANG",
            version="2.3",
            description="Chang SSM/I Derived Monthly Rain Indices 5 x 5 degree V2.3 (RAIN_CHANG) at GES DISC version: 2.3"
        )

    SNDRSNIL2ESPNH3_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDRSNIL2ESPNH3_1",
            provider="GES_DISC", 
            shortname="SNDRSNIL2ESPNH3",
            version="1",
            description="Cross-track Infrared Sounder (CrIS) Level 2 Earth System Science Profiling Algorithm Ammonia Retrieval Algorithm (ESSPA-NH3) V1 (SNDRSNIL2ESPNH3) version: 1"
        )

    ESMRN5IM_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ESMRN5IM_001",
            provider="GES_DISC", 
            shortname="ESMRN5IM",
            version="001",
            description="ESMR/Nimbus-5 Images of Brightness Temperature on 70 mm Film V001 (ESMRN5IM) at GES DISC version: 001"
        )

    ESMRN5L1_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ESMRN5L1_001",
            provider="GES_DISC", 
            shortname="ESMRN5L1",
            version="001",
            description="ESMR/Nimbus-5 Level 1 Calibrated Brightness Temperature V001 (ESMRN5L1) at GES DISC version: 001"
        )

    ESMRN6IM_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ESMRN6IM_001",
            provider="GES_DISC", 
            shortname="ESMRN6IM",
            version="001",
            description="ESMR/Nimbus-6 Images of Brightness Temperature on 70 mm Film V001 (ESMRN6IM) at GES DISC version: 001"
        )

    EOLE1_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_EOLE1_001",
            provider="GES_DISC", 
            shortname="EOLE1",
            version="001",
            description="Eole 1 Raw Temperature, Pressure and Location Data Near 200 mbar (EOLE1) at GES DISC version: 001"
        )

    EXP7L1TRTWHT_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_EXP7L1TRTWHT_001",
            provider="GES_DISC", 
            shortname="EXP7L1TRTWHT",
            version="001",
            description="Explorer-7 Thermal Radiation Experiment Selected White Sensor Temperature (Nighttime) Values V001 (EXP7L1TRTWHT) at GES DISC version: 001"
        )

    EXP7L1TRTALL_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_EXP7L1TRTALL_001",
            provider="GES_DISC", 
            shortname="EXP7L1TRTALL",
            version="001",
            description="Explorer-7 Thermal Radiation Experiment Temperature Values from All Sensors V001 (EXP7L1TRTALL) at GES DISC version: 001"
        )

    FLDAS_NOAH01_CP_GL_M_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_FLDAS_NOAH01_CP_GL_M_001",
            provider="GES_DISC", 
            shortname="FLDAS_NOAH01_CP_GL_M",
            version="001",
            description="FLDAS Noah Land Surface Model L4 Global Monthly 0.1 x 0.1 degree (GDAS and CHIRPS-PRELIM) V001 (FLDAS_NOAH01_CP_GL_M) at GES DISC version: 001"
        )

    FLDAS_NOAH01_C_GL_M_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_FLDAS_NOAH01_C_GL_M_001",
            provider="GES_DISC", 
            shortname="FLDAS_NOAH01_C_GL_M",
            version="001",
            description="FLDAS Noah Land Surface Model L4 Global Monthly 0.1 x 0.1 degree (MERRA-2 and CHIRPS) V001 (FLDAS_NOAH01_C_GL_M) at GES DISC version: 001"
        )

    FLDAS_NOAH01_C_GL_MA_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_FLDAS_NOAH01_C_GL_MA_001",
            provider="GES_DISC", 
            shortname="FLDAS_NOAH01_C_GL_MA",
            version="001",
            description="FLDAS Noah Land Surface Model L4 Global Monthly Anomaly 0.1 x 0.1 degree (MERRA-2 and CHIRPS) V001 (FLDAS_NOAH01_C_GL_MA) at GES DISC version: 001"
        )

    FLDAS_NOAH01_C_GL_MC_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_FLDAS_NOAH01_C_GL_MC_001",
            provider="GES_DISC", 
            shortname="FLDAS_NOAH01_C_GL_MC",
            version="001",
            description="FLDAS Noah Land Surface Model L4 Global Monthly Climatology 0.1 x 0.1 degree (MERRA-2 and CHIRPS) V001 (FLDAS_NOAH01_C_GL_MC) at GES DISC version: 001"
        )

    FLDAS_NOAHMP001_G_CA_D_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_FLDAS_NOAHMP001_G_CA_D_001",
            provider="GES_DISC", 
            shortname="FLDAS_NOAHMP001_G_CA_D",
            version="001",
            description="FLDAS2 Noah-MP GDAS Land Surface Model L4 Central Asia Daily 0.01 degree x 0.01 degree V001 (FLDAS_NOAHMP001_G_CA_D) version: 001"
        )

    BCFLEXPART_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_BCFLEXPART_1",
            provider="GES_DISC", 
            shortname="BCFLEXPART",
            version="1",
            description="FLEXPART black carbon aerosol L4 global daily 1 x 1 degrees V1 (BCFLEXPART) version: 1"
        )

    DUSTFLEXPART_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_DUSTFLEXPART_1",
            provider="GES_DISC", 
            shortname="DUSTFLEXPART",
            version="1",
            description="FLEXPART dust aerosol L4 global daily 1 x 1 degrees V1 (DUSTFLEXPART) version: 1"
        )

    OCFLEXPART_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCFLEXPART_1",
            provider="GES_DISC", 
            shortname="OCFLEXPART",
            version="1",
            description="FLEXPART organic carbon aerosol L4 global daily 1 x 1 degrees V1 (OCFLEXPART) version: 1"
        )

    GEOS2OBSINPUTINTL_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GEOS2OBSINPUTINTL_001",
            provider="GES_DISC", 
            shortname="GEOS2OBSINPUTINTL",
            version="001",
            description="GEOS-2 International Optical Beacon Data Input V001 (GEOS2OBSINPUTINTL) at GES DISC version: 001"
        )

    GEOS3STST_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GEOS3STST_001",
            provider="GES_DISC", 
            shortname="GEOS3STST",
            version="001",
            description="GEOS-3 Satellite-to-Satellite Tracking Data V001 (GEOS3STST) at GES DISC version: 001"
        )

    OMUFPMET_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMUFPMET_004",
            provider="GES_DISC", 
            shortname="OMUFPMET",
            version="004",
            description="GEOS-5 FP-IT 3D Time-Averaged Model-Layer Assimilated Data Geo-Colocated to OMI/Aura UV2 1-Orbit L2 Swath 13x24km V4 (OMUFPMET) at GES DISC version: 004"
        )

    OMVFPMET_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMVFPMET_004",
            provider="GES_DISC", 
            shortname="OMVFPMET",
            version="004",
            description="GEOS-5 FP-IT 3D Time-Averaged Model-Layer Assimilated Data Geo-Colocated to OMI/Aura VIS 1-Orbit L2 Swath 13x24km V4 (OMVFPMET) at GES DISC version: 004"
        )

    OMUFPSLV_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMUFPSLV_004",
            provider="GES_DISC", 
            shortname="OMUFPSLV",
            version="004",
            description="GEOS-5 FP-IT 3D Time-Averaged Single-Level Diagnostics Geo-Colocated to OMI/Aura UV2 1-Orbit L2 Swath 13x24km V4 (OMUFPSLV) at GES DISC version: 004"
        )

    OMVFPSLV_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMVFPSLV_004",
            provider="GES_DISC", 
            shortname="OMVFPSLV",
            version="004",
            description="GEOS-5 FP-IT 3D Time-Averaged Single-Level Diagnostics Geo-Colocated to OMI/Aura VIS 1-Orbit L2 Swath 13x24km V4 (OMVFPSLV) at GES DISC version: 004"
        )

    OMUFPITMET_V003_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMUFPITMET_003",
            provider="GES_DISC", 
            shortname="OMUFPITMET",
            version="003",
            description="GEOS-5 FP-IT Assimilation Geo-colocated to OMI/Aura UV-2 1-Orbit L2 Support Swath 13x24km V3 (OMUFPITMET) at GES DISC version: 003"
        )

    OMVFPITMET_V003_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMVFPITMET_003",
            provider="GES_DISC", 
            shortname="OMVFPITMET",
            version="003",
            description="GEOS-5 FP-IT Assimilation Geo-colocated to OMI/Aura VIS 1-Orbit L2 Support Swath 13x24km V3 (OMVFPITMET) at GES DISC version: 003"
        )

    GEOS_CASAGFED_3H_NEE_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GEOS_CASAGFED_3H_NEE_2",
            provider="GES_DISC", 
            shortname="GEOS_CASAGFED_3H_NEE",
            version="2",
            description="GEOS-Carb CASA-GFED 3-hourly Ecosystem Exchange Fluxes 0.5 degree x 0.625 degree V2 (GEOS_CASAGFED_3H_NEE) at GES DISC version: 2"
        )

    GEOS_CASAGFED_3H_NEE_V3_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GEOS_CASAGFED_3H_NEE_3",
            provider="GES_DISC", 
            shortname="GEOS_CASAGFED_3H_NEE",
            version="3",
            description="GEOS-Carb CASA-GFED 3-hourly Ecosystem Exchange Fluxes 0.5 degree x 0.625 degree V3 (GEOS_CASAGFED_3H_NEE) at GES DISC version: 3"
        )

    GEOS_CASAGFED_D_FIRE_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GEOS_CASAGFED_D_FIRE_2",
            provider="GES_DISC", 
            shortname="GEOS_CASAGFED_D_FIRE",
            version="2",
            description="GEOS-Carb CASA-GFED Daily Fire and Fuel Emissions 0.5 degree x 0.5 degree V2 (GEOS_CASAGFED_D_FIRE) at GES DISC version: 2"
        )

    GEOS_CASAGFED_D_FIRE_V3_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GEOS_CASAGFED_D_FIRE_3",
            provider="GES_DISC", 
            shortname="GEOS_CASAGFED_D_FIRE",
            version="3",
            description="GEOS-Carb CASA-GFED Daily Fire and Fuel Emissions 0.5 degree x 0.5 degree V3 (GEOS_CASAGFED_D_FIRE) at GES DISC version: 3"
        )

    GEOS_CASAGFED_M_FLUX_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GEOS_CASAGFED_M_FLUX_2",
            provider="GES_DISC", 
            shortname="GEOS_CASAGFED_M_FLUX",
            version="2",
            description="GEOS-Carb CASA-GFED Monthly Fire Fuel NPP Rh NEE Fluxes 0.5 degree x 0.5 degree V2 (GEOS_CASAGFED_M_FLUX) at GES DISC version: 2"
        )

    GEOS_CASAGFED_M_FLUX_V3_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GEOS_CASAGFED_M_FLUX_3",
            provider="GES_DISC", 
            shortname="GEOS_CASAGFED_M_FLUX",
            version="3",
            description="GEOS-Carb CASA-GFED Monthly Fire Fuel NPP Rh NEE Fluxes 0.5 degree x 0.5 degree V3 (GEOS_CASAGFED_M_FLUX) at GES DISC version: 3"
        )

    GLDAS_CLM10SUBP_3H_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GLDAS_CLM10SUBP_3H_001",
            provider="GES_DISC", 
            shortname="GLDAS_CLM10SUBP_3H",
            version="001",
            description="GLDAS CLM Land Surface Model L4 3 hourly 1.0 x 1.0 degree Subsetted V001 (GLDAS_CLM10SUBP_3H) at GES DISC version: 001"
        )

    GLDAS_CLSM10_3H_EP_V21_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GLDAS_CLSM10_3H_EP_2.1",
            provider="GES_DISC", 
            shortname="GLDAS_CLSM10_3H_EP",
            version="2.1",
            description="GLDAS Catchment Land Surface Model L4 3 hourly 1.0 x 1.0 degree Early Product V2.1 (GLDAS_CLSM10_3H_EP) at GES DISC version: 2.1"
        )

    GLDAS_CLSM10_3H_V20_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GLDAS_CLSM10_3H_2.0",
            provider="GES_DISC", 
            shortname="GLDAS_CLSM10_3H",
            version="2.0",
            description="GLDAS Catchment Land Surface Model L4 3 hourly 1.0 x 1.0 degree V2.0 (GLDAS_CLSM10_3H) at GES DISC version: 2.0"
        )

    GLDAS_CLSM10_3H_V21_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GLDAS_CLSM10_3H_2.1",
            provider="GES_DISC", 
            shortname="GLDAS_CLSM10_3H",
            version="2.1",
            description="GLDAS Catchment Land Surface Model L4 3 hourly 1.0 x 1.0 degree V2.1 (GLDAS_CLSM10_3H) at GES DISC version: 2.1"
        )

    GLDAS_CLSM025_DA1_D_V22_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GLDAS_CLSM025_DA1_D_2.2",
            provider="GES_DISC", 
            shortname="GLDAS_CLSM025_DA1_D",
            version="2.2",
            description="GLDAS Catchment Land Surface Model L4 daily 0.25 x 0.25 degree GRACE-DA1 V2.2 (GLDAS_CLSM025_DA1_D) at GES DISC version: 2.2"
        )

    GLDAS_CLSM025_DA1_D_EP_V22_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GLDAS_CLSM025_DA1_D_EP_2.2",
            provider="GES_DISC", 
            shortname="GLDAS_CLSM025_DA1_D_EP",
            version="2.2",
            description="GLDAS Catchment Land Surface Model L4 daily 0.25 x 0.25 degree GRACE-DA1 V2.2 (GLDAS_CLSM025_DA1_D_EP) at GES DISC version: 2.2"
        )

    GLDAS_CLSM025_D_V20_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GLDAS_CLSM025_D_2.0",
            provider="GES_DISC", 
            shortname="GLDAS_CLSM025_D",
            version="2.0",
            description="GLDAS Catchment Land Surface Model L4 daily 0.25 x 0.25 degree V2.0 (GLDAS_CLSM025_D) at GES DISC version: 2.0"
        )

    GLDAS_CLSM10_M_EP_V21_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GLDAS_CLSM10_M_EP_2.1",
            provider="GES_DISC", 
            shortname="GLDAS_CLSM10_M_EP",
            version="2.1",
            description="GLDAS Catchment Land Surface Model L4 monthly 1.0 x 1.0 degree Early Product V2.1 (GLDAS_CLSM10_M_EP) at GES DISC version: 2.1"
        )

    GLDAS_CLSM10_M_V20_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GLDAS_CLSM10_M_2.0",
            provider="GES_DISC", 
            shortname="GLDAS_CLSM10_M",
            version="2.0",
            description="GLDAS Catchment Land Surface Model L4 monthly 1.0 x 1.0 degree V2.0 (GLDAS_CLSM10_M) at GES DISC version: 2.0"
        )

    GLDAS_CLSM10_M_V21_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GLDAS_CLSM10_M_2.1",
            provider="GES_DISC", 
            shortname="GLDAS_CLSM10_M",
            version="2.1",
            description="GLDAS Catchment Land Surface Model L4 monthly 1.0 x 1.0 degree V2.1 (GLDAS_CLSM10_M) at GES DISC version: 2.1"
        )

    GLDAS_NOAH025_3H_EP_V21_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GLDAS_NOAH025_3H_EP_2.1",
            provider="GES_DISC", 
            shortname="GLDAS_NOAH025_3H_EP",
            version="2.1",
            description="GLDAS Noah Land Surface Model L4 3 hourly 0.25 x 0.25 degree Early Product V2.1 (GLDAS_NOAH025_3H_EP) at GES DISC version: 2.1"
        )

    GLDAS_NOAH025_3H_V20_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GLDAS_NOAH025_3H_2.0",
            provider="GES_DISC", 
            shortname="GLDAS_NOAH025_3H",
            version="2.0",
            description="GLDAS Noah Land Surface Model L4 3 hourly 0.25 x 0.25 degree V2.0 (GLDAS_NOAH025_3H) at GES DISC version: 2.0"
        )

    GLDAS_NOAH025_3H_V21_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GLDAS_NOAH025_3H_2.1",
            provider="GES_DISC", 
            shortname="GLDAS_NOAH025_3H",
            version="2.1",
            description="GLDAS Noah Land Surface Model L4 3 hourly 0.25 x 0.25 degree V2.1 (GLDAS_NOAH025_3H) at GES DISC version: 2.1"
        )

    GLDAS_NOAH10_3H_EP_V21_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GLDAS_NOAH10_3H_EP_2.1",
            provider="GES_DISC", 
            shortname="GLDAS_NOAH10_3H_EP",
            version="2.1",
            description="GLDAS Noah Land Surface Model L4 3 hourly 1.0 x 1.0 degree Early Product V2.1 (GLDAS_NOAH10_3H_EP) at GES DISC version: 2.1"
        )

    GLDAS_NOAH10_3H_V20_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GLDAS_NOAH10_3H_2.0",
            provider="GES_DISC", 
            shortname="GLDAS_NOAH10_3H",
            version="2.0",
            description="GLDAS Noah Land Surface Model L4 3 hourly 1.0 x 1.0 degree V2.0 (GLDAS_NOAH10_3H) at GES DISC version: 2.0"
        )

    GLDAS_NOAH10_3H_V21_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GLDAS_NOAH10_3H_2.1",
            provider="GES_DISC", 
            shortname="GLDAS_NOAH10_3H",
            version="2.1",
            description="GLDAS Noah Land Surface Model L4 3 hourly 1.0 x 1.0 degree V2.1 (GLDAS_NOAH10_3H) at GES DISC version: 2.1"
        )

    GLDAS_NOAH025_M_EP_V21_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GLDAS_NOAH025_M_EP_2.1",
            provider="GES_DISC", 
            shortname="GLDAS_NOAH025_M_EP",
            version="2.1",
            description="GLDAS Noah Land Surface Model L4 monthly 0.25 x 0.25 degree Early Product V2.1 (GLDAS_NOAH025_M_EP) at GES DISC version: 2.1"
        )

    GLDAS_NOAH025_M_V20_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GLDAS_NOAH025_M_2.0",
            provider="GES_DISC", 
            shortname="GLDAS_NOAH025_M",
            version="2.0",
            description="GLDAS Noah Land Surface Model L4 monthly 0.25 x 0.25 degree V2.0 (GLDAS_NOAH025_M) at GES DISC version: 2.0"
        )

    GLDAS_NOAH025_M_V21_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GLDAS_NOAH025_M_2.1",
            provider="GES_DISC", 
            shortname="GLDAS_NOAH025_M",
            version="2.1",
            description="GLDAS Noah Land Surface Model L4 monthly 0.25 x 0.25 degree V2.1 (GLDAS_NOAH025_M) at GES DISC version: 2.1"
        )

    GLDAS_NOAH10_M_EP_V21_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GLDAS_NOAH10_M_EP_2.1",
            provider="GES_DISC", 
            shortname="GLDAS_NOAH10_M_EP",
            version="2.1",
            description="GLDAS Noah Land Surface Model L4 monthly 1.0 x 1.0 degree Early Product V2.1 (GLDAS_NOAH10_M_EP) at GES DISC version: 2.1"
        )

    GLDAS_NOAH10_M_V20_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GLDAS_NOAH10_M_2.0",
            provider="GES_DISC", 
            shortname="GLDAS_NOAH10_M",
            version="2.0",
            description="GLDAS Noah Land Surface Model L4 monthly 1.0 x 1.0 degree V2.0 (GLDAS_NOAH10_M) at GES DISC version: 2.0"
        )

    GLDAS_NOAH10_M_V21_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GLDAS_NOAH10_M_2.1",
            provider="GES_DISC", 
            shortname="GLDAS_NOAH10_M",
            version="2.1",
            description="GLDAS Noah Land Surface Model L4 monthly 1.0 x 1.0 degree V2.1 (GLDAS_NOAH10_M) at GES DISC version: 2.1"
        )

    GLDAS_VIC10_3H_EP_V21_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GLDAS_VIC10_3H_EP_2.1",
            provider="GES_DISC", 
            shortname="GLDAS_VIC10_3H_EP",
            version="2.1",
            description="GLDAS VIC Land Surface Model L4 3 hourly 1.0 x 1.0 degree Early Product V2.1 (GLDAS_VIC10_3H_EP) at GES DISC version: 2.1"
        )

    GLDAS_VIC10_3H_V20_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GLDAS_VIC10_3H_2.0",
            provider="GES_DISC", 
            shortname="GLDAS_VIC10_3H",
            version="2.0",
            description="GLDAS VIC Land Surface Model L4 3 hourly 1.0 x 1.0 degree V2.0 (GLDAS_VIC10_3H) at GES DISC version: 2.0"
        )

    GLDAS_VIC10_3H_V21_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GLDAS_VIC10_3H_2.1",
            provider="GES_DISC", 
            shortname="GLDAS_VIC10_3H",
            version="2.1",
            description="GLDAS VIC Land Surface Model L4 3 hourly 1.0 x 1.0 degree V2.1 (GLDAS_VIC10_3H) at GES DISC version: 2.1"
        )

    GLDAS_VIC10_M_EP_V21_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GLDAS_VIC10_M_EP_2.1",
            provider="GES_DISC", 
            shortname="GLDAS_VIC10_M_EP",
            version="2.1",
            description="GLDAS VIC Land Surface Model L4 monthly 1.0 x 1.0 degree Early Product V2.1 (GLDAS_VIC10_M_EP) at GES DISC version: 2.1"
        )

    GLDAS_VIC10_M_V20_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GLDAS_VIC10_M_2.0",
            provider="GES_DISC", 
            shortname="GLDAS_VIC10_M",
            version="2.0",
            description="GLDAS VIC Land Surface Model L4 monthly 1.0 x 1.0 degree V2.0 (GLDAS_VIC10_M) at GES DISC version: 2.0"
        )

    GLDAS_VIC10_M_V21_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GLDAS_VIC10_M_2.1",
            provider="GES_DISC", 
            shortname="GLDAS_VIC10_M",
            version="2.1",
            description="GLDAS VIC Land Surface Model L4 monthly 1.0 x 1.0 degree V2.1 (GLDAS_VIC10_M) at GES DISC version: 2.1"
        )

    GOME_MINDS_NO2_V11_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GOME_MINDS_NO2_1.1",
            provider="GES_DISC", 
            shortname="GOME_MINDS_NO2",
            version="1.1",
            description="GOME/ERS-2 NO2 Tropospheric, Stratospheric and Total Columns MINDS 1-Orbit L2 Swath 40 km x 320 km V1.1 (GOME_MINDS_NO2) at GES DISC version: 1.1"
        )

    GOZMMLPHCL_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GozMmlpHCl_1",
            provider="GES_DISC", 
            shortname="GozMmlpHCl",
            version="1",
            description="GOZCARDS Merged Hydrogen Chloride 1 month L3 10 degree Zonal Means on a Vertical Pressure Grid V1 (GozMmlpHCl) at GES DISC version: 1"
        )

    GOZMMLPHNO3_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GozMmlpHNO3_1",
            provider="GES_DISC", 
            shortname="GozMmlpHNO3",
            version="1",
            description="GOZCARDS Merged Nitric Acid 1 month L3 10 degree Zonal Means on a Vertical Pressure Grid V1 (GozMmlpHNO3) at GES DISC version: 1"
        )

    GOZMMLPN2O_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GozMmlpN2O_1",
            provider="GES_DISC", 
            shortname="GozMmlpN2O",
            version="1",
            description="GOZCARDS Merged Nitrous Oxide 1 month L3 10 degree Zonal Means on a Vertical Pressure Grid V1 (GozMmlpN2O) at GES DISC version: 1"
        )

    GOZMMLPO3_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GozMmlpO3_1",
            provider="GES_DISC", 
            shortname="GozMmlpO3",
            version="1",
            description="GOZCARDS Merged Ozone 1 month L3 10 degree Zonal Means on a Vertical Pressure Grid V1 (GozMmlpO3) at GES DISC version: 1"
        )

    GOZMMLPH2O_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GozMmlpH2O_1",
            provider="GES_DISC", 
            shortname="GozMmlpH2O",
            version="1",
            description="GOZCARDS Merged Water Vapor 1 month L3 10 degree Zonal Means on a Vertical Pressure Grid V1 (GozMmlpH2O) at GES DISC version: 1"
        )

    GOZSMLPHCL_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GozSmlpHCl_1",
            provider="GES_DISC", 
            shortname="GozSmlpHCl",
            version="1",
            description="GOZCARDS Source Hydrogen Chloride 1 month L3 10 degree Zonal Means on a Vertical Pressure Grid V1 (GozSmlpHCl) at GES DISC version: 1"
        )

    GOZSMLPHNO3_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GozSmlpHNO3_1",
            provider="GES_DISC", 
            shortname="GozSmlpHNO3",
            version="1",
            description="GOZCARDS Source Nitric Acid 1 month L3 10 degree Zonal Means on a Vertical Pressure Grid V1 (GozSmlpHNO3) at GES DISC version: 1"
        )

    GOZSMLPN2O_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GozSmlpN2O_1",
            provider="GES_DISC", 
            shortname="GozSmlpN2O",
            version="1",
            description="GOZCARDS Source Nitrous Oxide 1 month L3 10 degree Zonal Means on a Vertical Pressure Grid V1 (GozSmlpN2O) at GES DISC version: 1"
        )

    GOZSMLPO3_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GozSmlpO3_1",
            provider="GES_DISC", 
            shortname="GozSmlpO3",
            version="1",
            description="GOZCARDS Source Ozone 1 month L3 10 degree Zonal Means on a Vertical Pressure Grid V1 (GozSmlpO3) at GES DISC version: 1"
        )

    GOZSMLPT_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GozSmlpT_1",
            provider="GES_DISC", 
            shortname="GozSmlpT",
            version="1",
            description="GOZCARDS Source Temperature 1 month L4 10 degree Zonal Averages on a Vertical Pressure Grid V1 (GozSmlpT) at GES DISC version: 1"
        )

    GOZSMLPH2O_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GozSmlpH2O_1",
            provider="GES_DISC", 
            shortname="GozSmlpH2O",
            version="1",
            description="GOZCARDS Source Water Vapor 1 month L3 10 degree Zonal Means on a Vertical Pressure Grid V1 (GozSmlpH2O) at GES DISC version: 1"
        )

    GPCPDAY_V31_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPCPDAY_3.1",
            provider="GES_DISC", 
            shortname="GPCPDAY",
            version="3.1",
            description="GPCP Precipitation Level 3 Daily 0.5-Degree V3.1 (GPCPDAY) at GES DISC version: 3.1"
        )

    GPCPDAY_V32_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPCPDAY_3.2",
            provider="GES_DISC", 
            shortname="GPCPDAY",
            version="3.2",
            description="GPCP Precipitation Level 3 Daily 0.5-Degree V3.2 (GPCPDAY) at GES DISC version: 3.2"
        )

    GPCPMON_V31_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPCPMON_3.1",
            provider="GES_DISC", 
            shortname="GPCPMON",
            version="3.1",
            description="GPCP Precipitation Level 3 Monthly 0.5-Degree V3.1 (GPCPMON) at GES DISC version: 3.1"
        )

    GPCPMON_V32_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPCPMON_3.2",
            provider="GES_DISC", 
            shortname="GPCPMON",
            version="3.2",
            description="GPCP Precipitation Level 3 Monthly 0.5-Degree V3.2 (GPCPMON) at GES DISC version: 3.2"
        )

    GPM_2AGPROFGCOMW1AMSR2_CLIM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_2AGPROFGCOMW1AMSR2_CLIM_07",
            provider="GES_DISC", 
            shortname="GPM_2AGPROFGCOMW1AMSR2_CLIM",
            version="07",
            description="GPM AMSR-2 on GCOM-W1 (GPROF) Climate-based Radiometer Precipitation Profiling L2A 1.5 hours 10 km V07 (GPM_2AGPROFGCOMW1AMSR2_CLIM) at GES DISC version: 07"
        )

    GPM_3GPROFGCOMW1AMSR2_DAY_CLIM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3GPROFGCOMW1AMSR2_DAY_CLIM_07",
            provider="GES_DISC", 
            shortname="GPM_3GPROFGCOMW1AMSR2_DAY_CLIM",
            version="07",
            description="GPM AMSR-2 on GCOM-W1 (GPROF) Climate-based Radiometer Precipitation Profiling L3 1 day 0.25 degree x 0.25 degree V07 (GPM_3GPROFGCOMW1AMSR2_DAY_CLIM) at GES DISC version: 07"
        )

    GPM_3GPROFGCOMW1AMSR2_CLIM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3GPROFGCOMW1AMSR2_CLIM_07",
            provider="GES_DISC", 
            shortname="GPM_3GPROFGCOMW1AMSR2_CLIM",
            version="07",
            description="GPM AMSR-2 on GCOM-W1 (GPROF) Climate-based Radiometer Precipitation Profiling L3 1 month 0.25 degree x 0.25 degree V07 (GPM_3GPROFGCOMW1AMSR2_CLIM) at GES DISC version: 07"
        )

    GPM_2AGPROFGCOMW1AMSR2_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_2AGPROFGCOMW1AMSR2_07",
            provider="GES_DISC", 
            shortname="GPM_2AGPROFGCOMW1AMSR2",
            version="07",
            description="GPM AMSR-2 on GCOM-W1 (GPROF) Radiometer Precipitation Profiling L2A 1.5 hours 10 km V07 (GPM_2AGPROFGCOMW1AMSR2) at GES DISC version: 07"
        )

    GPM_3GPROFGCOMW1AMSR2_DAY_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3GPROFGCOMW1AMSR2_DAY_07",
            provider="GES_DISC", 
            shortname="GPM_3GPROFGCOMW1AMSR2_DAY",
            version="07",
            description="GPM AMSR-2 on GCOM-W1 (GPROF) Radiometer Precipitation Profiling L3 1 day 0.25 degree x 0.25 degree V07 (GPM_3GPROFGCOMW1AMSR2_DAY) at GES DISC version: 07"
        )

    GPM_3GPROFGCOMW1AMSR2_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3GPROFGCOMW1AMSR2_07",
            provider="GES_DISC", 
            shortname="GPM_3GPROFGCOMW1AMSR2",
            version="07",
            description="GPM AMSR-2 on GCOM-W1 (GPROF) Radiometer Precipitation Profiling L3 1 month 0.25 degree x 0.25 degree V07 (GPM_3GPROFGCOMW1AMSR2) at GES DISC version: 07"
        )

    GPM_1CGCOMW1AMSR2_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_1CGCOMW1AMSR2_07",
            provider="GES_DISC", 
            shortname="GPM_1CGCOMW1AMSR2",
            version="07",
            description="GPM AMSR-2 on GCOM-W1 Common Calibrated Brightness Temperature L1C 1.5 hours 10 km V07 (GPM_1CGCOMW1AMSR2) at GES DISC version: 07"
        )

    GPM_1CAQUAAMSRE_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_1CAQUAAMSRE_07",
            provider="GES_DISC", 
            shortname="GPM_1CAQUAAMSRE",
            version="07",
            description="GPM AMSR-E on AQUA Common Calibrated Brightness Temperatures L1C 1.5 hours 10.5 km V07 (GPM_1CAQUAAMSRE) at GES DISC version: 07"
        )

    GPM_2AGPROFAQUAAMSRE_CLIM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_2AGPROFAQUAAMSRE_CLIM_07",
            provider="GES_DISC", 
            shortname="GPM_2AGPROFAQUAAMSRE_CLIM",
            version="07",
            description="GPM AMSR-E on Aqua (GPROF) Climate-based Radiometer Precipitation Profiling L2 1.5 hours 5 km V07 (GPM_2AGPROFAQUAAMSRE_CLIM) at GES DISC version: 07"
        )

    GPM_3GPROFAQUAAMSRE_DAY_CLIM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3GPROFAQUAAMSRE_DAY_CLIM_07",
            provider="GES_DISC", 
            shortname="GPM_3GPROFAQUAAMSRE_DAY_CLIM",
            version="07",
            description="GPM AMSR-E on Aqua (GPROF) Climate-based Radiometer Precipitation Profiling L3 1 day 0.25 degree x 0.25 degree V07 (GPM_3GPROFAQUAAMSRE_DAY_CLIM) at GES DISC version: 07"
        )

    GPM_3GPROFAQUAAMSRE_CLIM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3GPROFAQUAAMSRE_CLIM_07",
            provider="GES_DISC", 
            shortname="GPM_3GPROFAQUAAMSRE_CLIM",
            version="07",
            description="GPM AMSR-E on Aqua (GPROF) Climate-based Radiometer Precipitation Profiling L3 1 month 0.25 degree x 0.25 degree V07 (GPM_3GPROFAQUAAMSRE_CLIM) at GES DISC version: 07"
        )

    GPM_1CNOAA15AMSUB_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_1CNOAA15AMSUB_07",
            provider="GES_DISC", 
            shortname="GPM_1CNOAA15AMSUB",
            version="07",
            description="GPM AMSU-B on NOAA 15 Common Calibrated Brightness Temperatures L1C 1.5 hours 16 km V07 (GPM_1CNOAA15AMSUB) at GES DISC version: 07"
        )

    GPM_1CNOAA16AMSUB_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_1CNOAA16AMSUB_07",
            provider="GES_DISC", 
            shortname="GPM_1CNOAA16AMSUB",
            version="07",
            description="GPM AMSU-B on NOAA 16 Common Calibrated Brightness Temperatures L1C 1.5 hours 16 km V07 (GPM_1CNOAA16AMSUB) at GES DISC version: 07"
        )

    GPM_1CNOAA17AMSUB_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_1CNOAA17AMSUB_07",
            provider="GES_DISC", 
            shortname="GPM_1CNOAA17AMSUB",
            version="07",
            description="GPM AMSU-B on NOAA 17 Common Calibrated Brightness Temperatures L1C 1.5 hours 16 km V07 (GPM_1CNOAA17AMSUB) at GES DISC version: 07"
        )

    GPM_2AGPROFNOAA15AMSUB_CLIM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_2AGPROFNOAA15AMSUB_CLIM_07",
            provider="GES_DISC", 
            shortname="GPM_2AGPROFNOAA15AMSUB_CLIM",
            version="07",
            description="GPM AMSU-B on NOAA15 (GPROF) Climate-based Radiometer Precipitation Profiling L2 1.5 hours 16 km V07 (GPM_2AGPROFNOAA15AMSUB) at GES DISC version: 07"
        )

    GPM_2AGPROFNOAA16AMSUB_CLIM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_2AGPROFNOAA16AMSUB_CLIM_07",
            provider="GES_DISC", 
            shortname="GPM_2AGPROFNOAA16AMSUB_CLIM",
            version="07",
            description="GPM AMSU-B on NOAA16 (GPROF) Climate-based Radiometer Precipitation Profiling L2 1.5 hours 16 km V07 (GPM_2AGPROFNOAA16AMSUB) at GES DISC version: 07"
        )

    GPM_2AGPROFNOAA17AMSUB_CLIM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_2AGPROFNOAA17AMSUB_CLIM_07",
            provider="GES_DISC", 
            shortname="GPM_2AGPROFNOAA17AMSUB_CLIM",
            version="07",
            description="GPM AMSU-B on NOAA17 (GPROF) Climate-based Radiometer Precipitation Profiling L2 1.5 hours 16 km V07 (GPM_2AGPROFNOAA17AMSUB) at GES DISC version: 07"
        )

    GPM_3GPROFNOAA15AMSUB_DAY_CLIM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3GPROFNOAA15AMSUB_DAY_CLIM_07",
            provider="GES_DISC", 
            shortname="GPM_3GPROFNOAA15AMSUB_DAY_CLIM",
            version="07",
            description="GPM AMSUB on NOAA15 (GPROF) Climate-based Radiometer Precipitation Profiling L3 1 day 0.25 degree x 0.25 degree V07 (GPM_3GPROFNOAA15AMSUB_DAY_CLIM) at GES DISC version: 07"
        )

    GPM_3GPROFNOAA15AMSUB_CLIM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3GPROFNOAA15AMSUB_CLIM_07",
            provider="GES_DISC", 
            shortname="GPM_3GPROFNOAA15AMSUB_CLIM",
            version="07",
            description="GPM AMSUB on NOAA15 (GPROF) Climate-based Radiometer Precipitation Profiling L3 1 month 0.25 degree x 0.25 degree V07 (GPM_3GPROFNOAA15AMSUB_CLIM) at GES DISC version: 07"
        )

    GPM_3GPROFNOAA16AMSUB_DAY_CLIM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3GPROFNOAA16AMSUB_DAY_CLIM_07",
            provider="GES_DISC", 
            shortname="GPM_3GPROFNOAA16AMSUB_DAY_CLIM",
            version="07",
            description="GPM AMSUB on NOAA16 (GPROF) Climate-based Radiometer Precipitation Profiling L3 1 day 0.25 degree x 0.25 degree V07 (GPM_3GPROFNOAA16AMSUB_DAY_CLIM) at GES DISC version: 07"
        )

    GPM_3GPROFNOAA16AMSUB_CLIM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3GPROFNOAA16AMSUB_CLIM_07",
            provider="GES_DISC", 
            shortname="GPM_3GPROFNOAA16AMSUB_CLIM",
            version="07",
            description="GPM AMSUB on NOAA16 (GPROF) Climate-based Radiometer Precipitation Profiling L3 1 month 0.25 degree x 0.25 degree V07 (GPM_3GPROFNOAA16AMSUB_CLIM) at GES DISC version: 07"
        )

    GPM_3GPROFNOAA17AMSUB_DAY_CLIM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3GPROFNOAA17AMSUB_DAY_CLIM_07",
            provider="GES_DISC", 
            shortname="GPM_3GPROFNOAA17AMSUB_DAY_CLIM",
            version="07",
            description="GPM AMSUB on NOAA17 (GPROF) Climate-based Radiometer Precipitation Profiling L3 1 day 0.25 degree x 0.25 degree V07 (GPM_3GPROFNOAA17AMSUB_DAY_CLIM) at GES DISC version: 07"
        )

    GPM_3GPROFNOAA17AMSUB_CLIM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3GPROFNOAA17AMSUB_CLIM_07",
            provider="GES_DISC", 
            shortname="GPM_3GPROFNOAA17AMSUB_CLIM",
            version="07",
            description="GPM AMSUB on NOAA17 (GPROF) Climate-based Radiometer Precipitation Profiling L3 1 month 0.25 degree x 0.25 degree V07 (GPM_3GPROFNOAA17AMSUB_CLIM) at GES DISC version: 07"
        )

    GPM_2AGPROFNOAA20ATMS_CLIM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_2AGPROFNOAA20ATMS_CLIM_07",
            provider="GES_DISC", 
            shortname="GPM_2AGPROFNOAA20ATMS_CLIM",
            version="07",
            description="GPM ATMS on NOAA-20 (GPROF) Climate-based Radiometer Precipitation Profiling L2A 1.5 hours 17 km V07 (GPM_2AGPROFNOAA20ATMS_CLIM) at GES DISC version: 07"
        )

    GPM_3GPROFNOAA20ATMS_DAY_CLIM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3GPROFNOAA20ATMS_DAY_CLIM_07",
            provider="GES_DISC", 
            shortname="GPM_3GPROFNOAA20ATMS_DAY_CLIM",
            version="07",
            description="GPM ATMS on NOAA-20 (GPROF) Climate-based Radiometer Precipitation Profiling L3 1 day 0.25 degree x 0.25 degree V07 (GPM_3GPROFNOAA20ATMS_DAY_CLIM) at GES DISC version: 07"
        )

    GPM_3GPROFNOAA20ATMS_CLIM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3GPROFNOAA20ATMS_CLIM_07",
            provider="GES_DISC", 
            shortname="GPM_3GPROFNOAA20ATMS_CLIM",
            version="07",
            description="GPM ATMS on NOAA-20 (GPROF) Climate-based Radiometer Precipitation Profiling L3 1 month 0.25 degree x 0.25 degree V07 (GPM_3GPROFNOAA20ATMS_CLIM) at GES DISC version: 07"
        )

    GPM_2AGPROFNOAA20ATMS_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_2AGPROFNOAA20ATMS_07",
            provider="GES_DISC", 
            shortname="GPM_2AGPROFNOAA20ATMS",
            version="07",
            description="GPM ATMS on NOAA-20 (GPROF) Radiometer Precipitation Profiling L2A 1.5 hours 17 km V07 (GPM_2AGPROFNOAA20ATMS) at GES DISC version: 07"
        )

    GPM_3GPROFNOAA20ATMS_DAY_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3GPROFNOAA20ATMS_DAY_07",
            provider="GES_DISC", 
            shortname="GPM_3GPROFNOAA20ATMS_DAY",
            version="07",
            description="GPM ATMS on NOAA-20 (GPROF) Radiometer Precipitation Profiling L3 1 day 0.25 degree x 0.25 degree V07 (GPM_3GPROFNOAA20ATMS_DAY) at GES DISC version: 07"
        )

    GPM_3GPROFNOAA20ATMS_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3GPROFNOAA20ATMS_07",
            provider="GES_DISC", 
            shortname="GPM_3GPROFNOAA20ATMS",
            version="07",
            description="GPM ATMS on NOAA-20 (GPROF) Radiometer Precipitation Profiling L3 1 month 0.25 degree x 0.25 degree V07 (GPM_3GPROFNOAA20ATMS) at GES DISC version: 07"
        )

    GPM_1CNOAA20ATMS_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_1CNOAA20ATMS_07",
            provider="GES_DISC", 
            shortname="GPM_1CNOAA20ATMS",
            version="07",
            description="GPM ATMS on NOAA-20 Common Calibrated Brightness Temperatures L1C 1.5 hours 17 km V07 (GPM_1CNOAA20ATMS) at GES DISC version: 07"
        )

    GPM_2AGPROFNOAA21ATMS_CLIM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_2AGPROFNOAA21ATMS_CLIM_07",
            provider="GES_DISC", 
            shortname="GPM_2AGPROFNOAA21ATMS_CLIM",
            version="07",
            description="GPM ATMS on NOAA-21 (GPROF) Climate-based Radiometer Precipitation Profiling L2A 1.5 hours 17 km V07 (GPM_2AGPROFNOAA21ATMS_CLIM) at GES DISC version: 07"
        )

    GPM_3GPROFNOAA21ATMS_DAY_CLIM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3GPROFNOAA21ATMS_DAY_CLIM_07",
            provider="GES_DISC", 
            shortname="GPM_3GPROFNOAA21ATMS_DAY_CLIM",
            version="07",
            description="GPM ATMS on NOAA-21 (GPROF) Climate-based Radiometer Precipitation Profiling L3 1 day 0.25 degree x 0.25 degree V07 (GPM_3GPROFNOAA21ATMS_DAY_CLIM) at GES DISC version: 07"
        )

    GPM_3GPROFNOAA21ATMS_CLIM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3GPROFNOAA21ATMS_CLIM_07",
            provider="GES_DISC", 
            shortname="GPM_3GPROFNOAA21ATMS_CLIM",
            version="07",
            description="GPM ATMS on NOAA-21 (GPROF) Climate-based Radiometer Precipitation Profiling L3 1 month 0.25 degree x 0.25 degree V07 (GPM_3GPROFNOAA21ATMS_CLIM) at GES DISC version: 07"
        )

    GPM_2AGPROFNOAA21ATMS_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_2AGPROFNOAA21ATMS_07",
            provider="GES_DISC", 
            shortname="GPM_2AGPROFNOAA21ATMS",
            version="07",
            description="GPM ATMS on NOAA-21 (GPROF) Radiometer Precipitation Profiling L2A 1.5 hours 17 km V07 (GPM_2AGPROFNOAA21ATMS) at GES DISC version: 07"
        )

    GPM_3GPROFNOAA21ATMS_DAY_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3GPROFNOAA21ATMS_DAY_07",
            provider="GES_DISC", 
            shortname="GPM_3GPROFNOAA21ATMS_DAY",
            version="07",
            description="GPM ATMS on NOAA-21 (GPROF) Radiometer Precipitation Profiling L3 1 day 0.25 degree x 0.25 degree V07 (GPM_3GPROFNOAA21ATMS_DAY) at GES DISC version: 07"
        )

    GPM_3GPROFNOAA21ATMS_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3GPROFNOAA21ATMS_07",
            provider="GES_DISC", 
            shortname="GPM_3GPROFNOAA21ATMS",
            version="07",
            description="GPM ATMS on NOAA-21 (GPROF) Radiometer Precipitation Profiling L3 1 month 0.25 degree x 0.25 degree V07 (GPM_3GPROFNOAA21ATMS) at GES DISC version: 07"
        )

    GPM_1CNOAA21ATMS_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_1CNOAA21ATMS_07",
            provider="GES_DISC", 
            shortname="GPM_1CNOAA21ATMS",
            version="07",
            description="GPM ATMS on NOAA-21 Common Calibrated Brightness Temperatures L1C 1.5 hours 17 km V07 (GPM_1CNOAA21ATMS) at GES DISC version: 07"
        )

    GPM_2AGPROFNPPATMS_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_2AGPROFNPPATMS_07",
            provider="GES_DISC", 
            shortname="GPM_2AGPROFNPPATMS",
            version="07",
            description="GPM ATMS on SUOMI-NPP (GPROF) Radiometer Precipitation Profiling L2 1.5 hours 16 km V07 (GPM_2AGPROFNPPATMS) at GES DISC version: 07"
        )

    GPM_2AGPROFNPPATMS_CLIM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_2AGPROFNPPATMS_CLIM_07",
            provider="GES_DISC", 
            shortname="GPM_2AGPROFNPPATMS_CLIM",
            version="07",
            description="GPM ATMS on SUOMI-NPP (GPROF) Radiometer Precipitation Profiling L2 1.5 hours 16 km V07 (GPM_2AGPROFNPPATMS_CLIM) at GES DISC version: 07"
        )

    GPM_3GPROFNPPATMS_DAY_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3GPROFNPPATMS_DAY_07",
            provider="GES_DISC", 
            shortname="GPM_3GPROFNPPATMS_DAY",
            version="07",
            description="GPM ATMS on SUOMI-NPP (GPROF) Radiometer Precipitation Profiling L3 1 day 0.25 degree x 0.25 degree V07 (GPM_3GPROFNPPATMS_DAY) at GES DISC version: 07"
        )

    GPM_3GPROFNPPATMS_DAY_CLIM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3GPROFNPPATMS_DAY_CLIM_07",
            provider="GES_DISC", 
            shortname="GPM_3GPROFNPPATMS_DAY_CLIM",
            version="07",
            description="GPM ATMS on SUOMI-NPP (GPROF) Radiometer Precipitation Profiling L3 1 day 0.25 degree x 0.25 degree V07 (GPM_3GPROFNPPATMS_DAY_CLIM) at GES DISC version: 07"
        )

    GPM_3GPROFNPPATMS_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3GPROFNPPATMS_07",
            provider="GES_DISC", 
            shortname="GPM_3GPROFNPPATMS",
            version="07",
            description="GPM ATMS on SUOMI-NPP (GPROF) Radiometer Precipitation Profiling L3 1 month 0.25 degree x 0.25 degree V07 (GPM_3GPROFNPPATMS) at GES DISC version: 07"
        )

    GPM_3GPROFNPPATMS_CLIM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3GPROFNPPATMS_CLIM_07",
            provider="GES_DISC", 
            shortname="GPM_3GPROFNPPATMS_CLIM",
            version="07",
            description="GPM ATMS on SUOMI-NPP (GPROF) Radiometer Precipitation Profiling L3 1 month 0.25 degree x 0.25 degree V07 (GPM_3GPROFNPPATMS_CLIM) at GES DISC version: 07"
        )

    GPM_1CNPPATMS_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_1CNPPATMS_07",
            provider="GES_DISC", 
            shortname="GPM_1CNPPATMS",
            version="07",
            description="GPM ATMS on SUOMI-NPP Common Calibrated Brightness Temperature L1C 1.5 hours 16 km V07 (GPM_1CNPPATMS) at GES DISC version: 07"
        )

    GPM_3GCSH_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3GCSH_07",
            provider="GES_DISC", 
            shortname="GPM_3GCSH",
            version="07",
            description="GPM DPR (Gridded Convective Stratiform Heating) L3 1.5 hours 0.5 degree x 0.5 degree V07 (GPM_3GCSH) at GES DISC version: 07"
        )

    GPM_3GSLH_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3GSLH_07",
            provider="GES_DISC", 
            shortname="GPM_3GSLH",
            version="07",
            description="GPM DPR Gridded Orbital Spectral Latent Heating Profiles L3 1.5 hours 0.5 degree x 0.5 degree V07 (GPM_3GSLH) at GES DISC version: 07"
        )

    GPM_2AKAENV_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_2AKaENV_07",
            provider="GES_DISC", 
            shortname="GPM_2AKaENV",
            version="07",
            description="GPM DPR Ka Environment L2A 1.5 hours 5 km V07 (GPM_2AKaENV) at GES DISC version: 07"
        )

    GPM_2AKA_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_2AKa_07",
            provider="GES_DISC", 
            shortname="GPM_2AKa",
            version="07",
            description="GPM DPR Ka Precipitation Profile 2A 1.5 hours 5 km V07 (GPM_2AKa) at GES DISC version: 07"
        )

    GPM_PRL1KA_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_PRL1KA_07",
            provider="GES_DISC", 
            shortname="GPM_PRL1KA",
            version="07",
            description="GPM DPR Ka-band Received Power L1B 1.5 hours 5 km V07 (GPM_PRL1KA) at GES DISC version: 07"
        )

    GPM_2AKUENV_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_2AKuENV_07",
            provider="GES_DISC", 
            shortname="GPM_2AKuENV",
            version="07",
            description="GPM DPR Ku Environment L2A 1.5 hours 5 km V07 (GPM_2AKuENV) at GES DISC version: 07"
        )

    GPM_2AKU_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_2AKu_07",
            provider="GES_DISC", 
            shortname="GPM_2AKu",
            version="07",
            description="GPM DPR Ku Precipitation Profile 2A 1.5 hours 5 km V07 (GPM_2AKu) at GES DISC version: 07"
        )

    GPM_PRL1KU_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_PRL1KU_07",
            provider="GES_DISC", 
            shortname="GPM_PRL1KU",
            version="07",
            description="GPM DPR Ku-band Received Power L1B 1.5 hours 5 km V07 (GPM_PRL1KU) at GES DISC version: 07"
        )

    GPM_2ADPRENV_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_2ADPRENV_07",
            provider="GES_DISC", 
            shortname="GPM_2ADPRENV",
            version="07",
            description="GPM DPR L2A Environment 1.5 hours 5 km V07 (GPM_2ADPRENV) at GES DISC version: 07"
        )

    GPM_3DPRD_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3DPRD_07",
            provider="GES_DISC", 
            shortname="GPM_3DPRD",
            version="07",
            description="GPM DPR Precipitation Profile 1 Day 0.25 degree x 0.25 degree V07 (GPM_3DPRD) at GES DISC version: 07"
        )

    GPM_3DPR_ASC_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3DPR_ASC_07",
            provider="GES_DISC", 
            shortname="GPM_3DPR_ASC",
            version="07",
            description="GPM DPR Precipitation Profile 1 Day Ascending 0.25 degree x 0.25 degree V07 (GPM_3DPR_ASC) at GES DISC version: 07"
        )

    GPM_3DPR_DES_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3DPR_DES_07",
            provider="GES_DISC", 
            shortname="GPM_3DPR_DES",
            version="07",
            description="GPM DPR Precipitation Profile 1 Day Descending 0.25 degree x 0.25 degree V07 (GPM_3DPR_DES) at GES DISC version: 07"
        )

    GPM_3DPR_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3DPR_07",
            provider="GES_DISC", 
            shortname="GPM_3DPR",
            version="07",
            description="GPM DPR Precipitation Profile 1 month 0.25 degree x 0.25 degree V07 (GPM_3DPR) at GES DISC version: 07"
        )

    GPM_2ADPR_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_2ADPR_07",
            provider="GES_DISC", 
            shortname="GPM_2ADPR",
            version="07",
            description="GPM DPR Precipitation Profile L2A 1.5 hours 5 km V07 (GPM_2ADPR) at GES DISC version: 07"
        )

    GPM_2HSLH_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_2HSLH_07",
            provider="GES_DISC", 
            shortname="GPM_2HSLH",
            version="07",
            description="GPM DPR Spectral Latent Heating Profiles L2 1.5 hours 5 km V07 (GPM_2HSLH) at GES DISC version: 07"
        )

    GPM_3HSLH_DAY_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3HSLH_DAY_07",
            provider="GES_DISC", 
            shortname="GPM_3HSLH_DAY",
            version="07",
            description="GPM DPR Spectral Latent Heating Profiles L3 1 day 0.5 degree x 0.5 degree V07 (GPM_3HSLH_DAY) at GES DISC version: 07"
        )

    GPM_3HSLH_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3HSLH_07",
            provider="GES_DISC", 
            shortname="GPM_3HSLH",
            version="07",
            description="GPM DPR Spectral Latent Heating Profiles L3 1 month 0.5 degree x 0.5 degree V07 (GPM_3HSLH) at GES DISC version: 07"
        )

    GPM_3CMB_DAY_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3CMB_DAY_07",
            provider="GES_DISC", 
            shortname="GPM_3CMB_DAY",
            version="07",
            description="GPM DPR and GMI (Combined Precipitation) L3 1 day 0.25 degree x 0.25 degree V07 (GPM_3CMB_DAY) at GES DISC version: 07"
        )

    GPM_3CMB_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3CMB_07",
            provider="GES_DISC", 
            shortname="GPM_3CMB",
            version="07",
            description="GPM DPR and GMI (Combined Precipitation) L3 1 month 0.25 degree x 0.25 degree V07 (GPM_3CMB) at GES DISC version: 07"
        )

    GPM_3HCSH_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3HCSH_07",
            provider="GES_DISC", 
            shortname="GPM_3HCSH",
            version="07",
            description="GPM DPR and GMI Combined Convective Stratiform Heating L3 1 month 0.5 degree x 0.5 degree V07 (GPM_3HCSH) at GES DISC version: 07"
        )

    GPM_2BCMB_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_2BCMB_07",
            provider="GES_DISC", 
            shortname="GPM_2BCMB",
            version="07",
            description="GPM DPR and GMI Combined Precipitation L2B 1.5 hours 5 km V07 (GPM_2BCMB) at GES DISC version: 07"
        )

    GPM_2HCSH_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_2HCSH_07",
            provider="GES_DISC", 
            shortname="GPM_2HCSH",
            version="07",
            description="GPM DPR and GMI Combined Stratiform Heating L2 1.5 hours 5 km V07 (GPM_2HCSH) at GES DISC version: 07"
        )

    GPM_2AGPROFGPMGMI_CLIM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_2AGPROFGPMGMI_CLIM_07",
            provider="GES_DISC", 
            shortname="GPM_2AGPROFGPMGMI_CLIM",
            version="07",
            description="GPM GMI (GPROF) Climate-based Radiometer Precipitation Profiling L2A 1.5 hours 4 km x 4 km V07 (GPM_2AGPROFGPMGMI_CLIM) at GES DISC version: 07"
        )

    GPM_3GPROFGPMGMI_DAY_CLIM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3GPROFGPMGMI_DAY_CLIM_07",
            provider="GES_DISC", 
            shortname="GPM_3GPROFGPMGMI_DAY_CLIM",
            version="07",
            description="GPM GMI (GPROF) Climate-based Radiometer Precipitation Profiling L3 1 day 0.25 degree x 0.25 degree V07 (GPM_3GPROFGPMGMI_DAY_CLIM) at GES DISC version: 07"
        )

    GPM_3GPROFGPMGMI_CLIM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3GPROFGPMGMI_CLIM_07",
            provider="GES_DISC", 
            shortname="GPM_3GPROFGPMGMI_CLIM",
            version="07",
            description="GPM GMI (GPROF) Climate-based Radiometer Precipitation Profiling L3 1 month 0.25 degree x 0.25 degree V07 (GPM_3GPROFGPMGMI_CLIM) at GES DISC version: 07"
        )

    GPM_2AGPROFGPMGMI_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_2AGPROFGPMGMI_07",
            provider="GES_DISC", 
            shortname="GPM_2AGPROFGPMGMI",
            version="07",
            description="GPM GMI (GPROF) Radiometer Precipitation Profiling L2A 1.5 hours 13 km V07 (GPM_2AGPROFGPMGMI) at GES DISC version: 07"
        )

    GPM_3GPROFGPMGMI_DAY_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3GPROFGPMGMI_DAY_07",
            provider="GES_DISC", 
            shortname="GPM_3GPROFGPMGMI_DAY",
            version="07",
            description="GPM GMI (GPROF) Radiometer Precipitation Profiling L3 1 day 0.25 degree x 0.25 degree V07 (GPM_3GPROFGPMGMI_DAY) at GES DISC version: 07"
        )

    GPM_3GPROFGPMGMI_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3GPROFGPMGMI_07",
            provider="GES_DISC", 
            shortname="GPM_3GPROFGPMGMI",
            version="07",
            description="GPM GMI (GPROF) Radiometer Precipitation Profiling L3 1 month 0.25 degree x 0.25 degree V07 (GPM_3GPROFGPMGMI) at GES DISC version: 07"
        )

    GPM_BASEGPMGMI_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_BASEGPMGMI_07",
            provider="GES_DISC", 
            shortname="GPM_BASEGPMGMI",
            version="07",
            description="GPM GMI Antenna Temperatures L1BASE 1.5 hours 13 km V07 (GPM_BASEGPMGMI) at GES DISC version: 07"
        )

    GPM_1BGMI_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_1BGMI_07",
            provider="GES_DISC", 
            shortname="GPM_1BGMI",
            version="07",
            description="GPM GMI Brightness Temperatures L1B 1.5 hours 13 km V07 (GPM_1BGMI) at GES DISC version: 07"
        )

    GPM_1CGPMGMI_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_1CGPMGMI_07",
            provider="GES_DISC", 
            shortname="GPM_1CGPMGMI",
            version="07",
            description="GPM GMI Common Calibrated Brightness Temperatures Collocated L1C 1.5 hours 13 km V07 (GPM_1CGPMGMI) at GES DISC version: 07"
        )

    GPM_BASEGPMGMI_RSS_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_BASEGPMGMI_RSS_07",
            provider="GES_DISC", 
            shortname="GPM_BASEGPMGMI_RSS",
            version="07",
            description="GPM GMI RSS Common Calibrated Brightness Temperatures L1BASE 1.5 hours 13 km V07 (GPM_BASEGPMGMI_RSS) at GES DISC version: 07"
        )

    GPM_BASEGPMGMI_XCAL_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_BASEGPMGMI_XCAL_07",
            provider="GES_DISC", 
            shortname="GPM_BASEGPMGMI_XCAL",
            version="07",
            description="GPM GMI XCAL Common Calibrated Brightness Temperatures L1BASE 1.5 hours 13 km V07 (GPM_BASEGPMGMI_XCAL) at GES DISC version: 07"
        )

    GPM_1AGMI_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_1AGMI_07",
            provider="GES_DISC", 
            shortname="GPM_1AGMI",
            version="07",
            description="GPM GMI unpacked data L1A 1.5 hours 13 km V07 (GPM_1AGMI) at GES DISC version: 07"
        )

    GPM_1CGPMGMI_R_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_1CGPMGMI_R_07",
            provider="GES_DISC", 
            shortname="GPM_1CGPMGMI_R",
            version="07",
            description="GPM GMI_R Common Calibrated Brightness Temperatures Collocated L1C 1.5 hours 13 km V07 (GPM_1CGPMGMI_R) at GES DISC version: 07"
        )

    GPM_3IMERGDE_V06_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3IMERGDE_06",
            provider="GES_DISC", 
            shortname="GPM_3IMERGDE",
            version="06",
            description="GPM IMERG Early Precipitation L3 1 day 0.1 degree x 0.1 degree V06 (GPM_3IMERGDE) at GES DISC version: 06"
        )

    GPM_3IMERGDE_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3IMERGDE_07",
            provider="GES_DISC", 
            shortname="GPM_3IMERGDE",
            version="07",
            description="GPM IMERG Early Precipitation L3 1 day 0.1 degree x 0.1 degree V07 (GPM_3IMERGDE) at GES DISC version: 07"
        )

    GPM_3IMERGHHE_V06_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3IMERGHHE_06",
            provider="GES_DISC", 
            shortname="GPM_3IMERGHHE",
            version="06",
            description="GPM IMERG Early Precipitation L3 Half Hourly 0.1 degree x 0.1 degree V06 (GPM_3IMERGHHE) at GES DISC version: 06"
        )

    GPM_3IMERGHHE_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3IMERGHHE_07",
            provider="GES_DISC", 
            shortname="GPM_3IMERGHHE",
            version="07",
            description="GPM IMERG Early Precipitation L3 Half Hourly 0.1 degree x 0.1 degree V07 (GPM_3IMERGHHE) at GES DISC version: 07"
        )

    GPM_3IMERGDF_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3IMERGDF_07",
            provider="GES_DISC", 
            shortname="GPM_3IMERGDF",
            version="07",
            description="GPM IMERG Final Precipitation L3 1 day 0.1 degree x 0.1 degree V07 (GPM_3IMERGDF) at GES DISC version: 07"
        )

    GPM_3IMERGM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3IMERGM_07",
            provider="GES_DISC", 
            shortname="GPM_3IMERGM",
            version="07",
            description="GPM IMERG Final Precipitation L3 1 month 0.1 degree x 0.1 degree V07 (GPM_3IMERGM) at GES DISC version: 07"
        )

    GPM_3IMERGHH_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3IMERGHH_07",
            provider="GES_DISC", 
            shortname="GPM_3IMERGHH",
            version="07",
            description="GPM IMERG Final Precipitation L3 Half Hourly 0.1 degree x 0.1 degree V07 (GPM_3IMERGHH) at GES DISC version: 07"
        )

    GPM_3IMERGDL_V06_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3IMERGDL_06",
            provider="GES_DISC", 
            shortname="GPM_3IMERGDL",
            version="06",
            description="GPM IMERG Late Precipitation L3 1 day 0.1 degree x 0.1 degree V06 (GPM_3IMERGDL) at GES DISC version: 06"
        )

    GPM_3IMERGDL_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3IMERGDL_07",
            provider="GES_DISC", 
            shortname="GPM_3IMERGDL",
            version="07",
            description="GPM IMERG Late Precipitation L3 1 day 0.1 degree x 0.1 degree V07 (GPM_3IMERGDL) at GES DISC version: 07"
        )

    GPM_3IMERGHHL_V06_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3IMERGHHL_06",
            provider="GES_DISC", 
            shortname="GPM_3IMERGHHL",
            version="06",
            description="GPM IMERG Late Precipitation L3 Half Hourly 0.1 degree x 0.1 degree V06 (GPM_3IMERGHHL) at GES DISC version: 06"
        )

    GPM_3IMERGHHL_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3IMERGHHL_07",
            provider="GES_DISC", 
            shortname="GPM_3IMERGHHL",
            version="07",
            description="GPM IMERG Late Precipitation L3 Half Hourly 0.1 degree x 0.1 degree V07 (GPM_3IMERGHHL) at GES DISC version: 07"
        )

    GPM_2AGPROFMETOPAMHS_CLIM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_2AGPROFMETOPAMHS_CLIM_07",
            provider="GES_DISC", 
            shortname="GPM_2AGPROFMETOPAMHS_CLIM",
            version="07",
            description="GPM MHS on METOP-A (GPROF) Radiometer Precipitation Profiling L2A 1.5 hours 17 km V07 (GPM_2AGPROFMETOPAMHS_CLIM) at GES DISC version: 07"
        )

    GPM_3GPROFMETOPAMHS_DAY_CLIM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3GPROFMETOPAMHS_DAY_CLIM_07",
            provider="GES_DISC", 
            shortname="GPM_3GPROFMETOPAMHS_DAY_CLIM",
            version="07",
            description="GPM MHS on METOP-A (GPROF) Radiometer Precipitation Profiling L3 1 day 0.25 degree x 0.25 degree V07 (GPM_3GPROFMETOPAMHS_DAY_CLIM) at GES DISC version: 07"
        )

    GPM_3GPROFMETOPAMHS_CLIM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3GPROFMETOPAMHS_CLIM_07",
            provider="GES_DISC", 
            shortname="GPM_3GPROFMETOPAMHS_CLIM",
            version="07",
            description="GPM MHS on METOP-A (GPROF) Radiometer Precipitation Profiling L3 1 month 0.25 degree x 0.25 degree V07 (GPM_3GPROFMETOPAMHS_CLIM) at GES DISC version: 07"
        )

    GPM_1CMETOPAMHS_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_1CMETOPAMHS_07",
            provider="GES_DISC", 
            shortname="GPM_1CMETOPAMHS",
            version="07",
            description="GPM MHS on METOP-A Common Calibrated Brightness Temperature L1C 1.5 hours 17 km V07 (GPM_1CMETOPAMHS) at GES DISC version: 07"
        )

    GPM_2AGPROFMETOPBMHS_CLIM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_2AGPROFMETOPBMHS_CLIM_07",
            provider="GES_DISC", 
            shortname="GPM_2AGPROFMETOPBMHS_CLIM",
            version="07",
            description="GPM MHS on METOP-B (GPROF) Climate-based Radiometer Precipitation Profiling L2A 1.5 hours 17 km V07 (GPM_2AGPROFMETOPBMHS_CLIM) at GES DISC version: 07"
        )

    GPM_3GPROFMETOPBMHS_DAY_CLIM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3GPROFMETOPBMHS_DAY_CLIM_07",
            provider="GES_DISC", 
            shortname="GPM_3GPROFMETOPBMHS_DAY_CLIM",
            version="07",
            description="GPM MHS on METOP-B (GPROF) Climate-based Radiometer Precipitation Profiling L3 1 day 0.25 degree x 0.25 degree V07 (GPM_3GPROFMETOPBMHS_DAY_CLIM) at GES DISC version: 07"
        )

    GPM_3GPROFMETOPBMHS_CLIM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3GPROFMETOPBMHS_CLIM_07",
            provider="GES_DISC", 
            shortname="GPM_3GPROFMETOPBMHS_CLIM",
            version="07",
            description="GPM MHS on METOP-B (GPROF) Climate-based Radiometer Precipitation Profiling L3 1 month 0.25 degree x 0.25 degree V07 (GPM_3GPROFMETOPBMHS_CLIM) at GES DISC version: 07"
        )

    GPM_2AGPROFMETOPBMHS_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_2AGPROFMETOPBMHS_07",
            provider="GES_DISC", 
            shortname="GPM_2AGPROFMETOPBMHS",
            version="07",
            description="GPM MHS on METOP-B (GPROF) Radiometer Precipitation Profiling L2A 1.5 hours 17 km V07 (GPM_2AGPROFMETOPBMHS) at GES DISC version: 07"
        )

    GPM_3GPROFMETOPBMHS_DAY_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3GPROFMETOPBMHS_DAY_07",
            provider="GES_DISC", 
            shortname="GPM_3GPROFMETOPBMHS_DAY",
            version="07",
            description="GPM MHS on METOP-B (GPROF) Radiometer Precipitation Profiling L3 1 day 0.25 degree x 0.25 degree V07 (GPM_3GPROFMETOPBMHS_DAY) at GES DISC version: 07"
        )

    GPM_3GPROFMETOPBMHS_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3GPROFMETOPBMHS_07",
            provider="GES_DISC", 
            shortname="GPM_3GPROFMETOPBMHS",
            version="07",
            description="GPM MHS on METOP-B (GPROF) Radiometer Precipitation Profiling L3 1 month 0.25 degree x 0.25 degree V07 (GPM_3GPROFMETOPBMHS) at GES DISC version: 07"
        )

    GPM_1CMETOPBMHS_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_1CMETOPBMHS_07",
            provider="GES_DISC", 
            shortname="GPM_1CMETOPBMHS",
            version="07",
            description="GPM MHS on METOP-B Common Calibrated Brightness Temperature L1C 1.5 hours 17 km V07 (GPM_1CMETOPBMHS) at GES DISC version: 07"
        )

    GPM_2AGPROFMETOPCMHS_CLIM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_2AGPROFMETOPCMHS_CLIM_07",
            provider="GES_DISC", 
            shortname="GPM_2AGPROFMETOPCMHS_CLIM",
            version="07",
            description="GPM MHS on METOP-C (GPROF) Climate-based Radiometer Precipitation Profiling L2A 1.5 hours 17 km V07 (GPM_2AGPROFMETOPCMHS_CLIM) at GES DISC version: 07"
        )

    GPM_3GPROFMETOPCMHS_DAY_CLIM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3GPROFMETOPCMHS_DAY_CLIM_07",
            provider="GES_DISC", 
            shortname="GPM_3GPROFMETOPCMHS_DAY_CLIM",
            version="07",
            description="GPM MHS on METOP-C (GPROF) Climate-based Radiometer Precipitation Profiling L3 1 day 0.25 degree x 0.25 degree V07 (GPM_3GPROFMETOPCMHS_DAY_CLIM) at GES DISC version: 07"
        )

    GPM_3GPROFMETOPCMHS_CLIM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3GPROFMETOPCMHS_CLIM_07",
            provider="GES_DISC", 
            shortname="GPM_3GPROFMETOPCMHS_CLIM",
            version="07",
            description="GPM MHS on METOP-C (GPROF) Climate-based Radiometer Precipitation Profiling L3 1 month 0.25 degree x 0.25 degree V07 (GPM_3GPROFMETOPCMHS_CLIM) at GES DISC version: 07"
        )

    GPM_2AGPROFMETOPCMHS_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_2AGPROFMETOPCMHS_07",
            provider="GES_DISC", 
            shortname="GPM_2AGPROFMETOPCMHS",
            version="07",
            description="GPM MHS on METOP-C (GPROF) Radiometer Precipitation Profiling L2A 1.5 hours 17 km V07 (GPM_2AGPROFMETOPCMHS) at GES DISC version: 07"
        )

    GPM_3GPROFMETOPCMHS_DAY_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3GPROFMETOPCMHS_DAY_07",
            provider="GES_DISC", 
            shortname="GPM_3GPROFMETOPCMHS_DAY",
            version="07",
            description="GPM MHS on METOP-C (GPROF) Radiometer Precipitation Profiling L3 1 day 0.25 degree x 0.25 degree V07 (GPM_3GPROFMETOPCMHS_DAY) at GES DISC version: 07"
        )

    GPM_3GPROFMETOPCMHS_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3GPROFMETOPCMHS_07",
            provider="GES_DISC", 
            shortname="GPM_3GPROFMETOPCMHS",
            version="07",
            description="GPM MHS on METOP-C (GPROF) Radiometer Precipitation Profiling L3 1 month 0.25 degree x 0.25 degree V07 (GPM_3GPROFMETOPCMHS) at GES DISC version: 07"
        )

    GPM_1CMETOPCMHS_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_1CMETOPCMHS_07",
            provider="GES_DISC", 
            shortname="GPM_1CMETOPCMHS",
            version="07",
            description="GPM MHS on METOP-C Common Calibrated Brightness Temperature L1C 1.5 hours 17 km V07 (GPM_1CMETOPCMHS) at GES DISC version: 07"
        )

    GPM_2AGPROFNOAA18MHS_CLIM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_2AGPROFNOAA18MHS_CLIM_07",
            provider="GES_DISC", 
            shortname="GPM_2AGPROFNOAA18MHS_CLIM",
            version="07",
            description="GPM MHS on NOAA-18 (GPROF) Radiometer Precipitation Profiling L2A 1.5 hours 17 km V07 (GPM_2AGPROFNOAA18MHS_CLIM) at GES DISC version: 07"
        )

    GPM_1CNOAA18MHS_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_1CNOAA18MHS_07",
            provider="GES_DISC", 
            shortname="GPM_1CNOAA18MHS",
            version="07",
            description="GPM MHS on NOAA-18 Common Calibrated Brightness Temperature L1C 1.5 hours 17 km V07 (GPM_1CNOAA18MHS) at GES DISC version: 07"
        )

    GPM_2AGPROFNOAA19MHS_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_2AGPROFNOAA19MHS_07",
            provider="GES_DISC", 
            shortname="GPM_2AGPROFNOAA19MHS",
            version="07",
            description="GPM MHS on NOAA-19 (GPROF) Radiometer Precipitation Profiling L2A 1.5 hours 17 km V07 (GPM_2AGPROFNOAA19MHS) at GES DISC version: 07"
        )

    GPM_2AGPROFNOAA19MHS_CLIM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_2AGPROFNOAA19MHS_CLIM_07",
            provider="GES_DISC", 
            shortname="GPM_2AGPROFNOAA19MHS_CLIM",
            version="07",
            description="GPM MHS on NOAA-19 (GPROF) Radiometer Precipitation Profiling L2A 1.5 hours 17 km V07 (GPM_2AGPROFNOAA19MHS_CLIM) at GES DISC version: 07"
        )

    GPM_1CNOAA19MHS_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_1CNOAA19MHS_07",
            provider="GES_DISC", 
            shortname="GPM_1CNOAA19MHS",
            version="07",
            description="GPM MHS on NOAA-19 Common Calibrated Brightness Temperatures L1C 1.5 hours 17 km V07 (GPM_1CNOAA19MHS) at GES DISC version: 07"
        )

    GPM_3GPROFNOAA18MHS_DAY_CLIM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3GPROFNOAA18MHS_DAY_CLIM_07",
            provider="GES_DISC", 
            shortname="GPM_3GPROFNOAA18MHS_DAY_CLIM",
            version="07",
            description="GPM MHS on NOAA18 (GPROF) Radiometer Precipitation Profiling L3 1 day 0.25 degree x 0.25 degree V07 (GPM_3GPROFNOAA18MHS_DAY_CLIM) at GES DISC version: 07"
        )

    GPM_3GPROFNOAA18MHS_CLIM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3GPROFNOAA18MHS_CLIM_07",
            provider="GES_DISC", 
            shortname="GPM_3GPROFNOAA18MHS_CLIM",
            version="07",
            description="GPM MHS on NOAA18 (GPROF) Radiometer Precipitation Profiling L3 1 month 0.25 degree x 0.25 degree V07 (GPM_3GPROFNOAA18MHS_CLIM) at GES DISC version: 07"
        )

    GPM_3GPROFNOAA19MHS_DAY_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3GPROFNOAA19MHS_DAY_07",
            provider="GES_DISC", 
            shortname="GPM_3GPROFNOAA19MHS_DAY",
            version="07",
            description="GPM MHS on NOAA19 (GPROF) Radiometer Precipitation Profiling L3 1 day 0.25 degree x 0.25 degree V07 (GPM_3GPROFNOAA19MHS_DAY) at GES DISC version: 07"
        )

    GPM_3GPROFNOAA19MHS_DAY_CLIM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3GPROFNOAA19MHS_DAY_CLIM_07",
            provider="GES_DISC", 
            shortname="GPM_3GPROFNOAA19MHS_DAY_CLIM",
            version="07",
            description="GPM MHS on NOAA19 (GPROF) Radiometer Precipitation Profiling L3 1 day 0.25 degree x 0.25 degree V07 (GPM_3GPROFNOAA19MHS_DAY_CLIM) at GES DISC version: 07"
        )

    GPM_3GPROFNOAA19MHS_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3GPROFNOAA19MHS_07",
            provider="GES_DISC", 
            shortname="GPM_3GPROFNOAA19MHS",
            version="07",
            description="GPM MHS on NOAA19 (GPROF) Radiometer Precipitation Profiling L3 1 month 0.25 degree x 0.25 degree V07 (GPM_3GPROFNOAA19MHS) at GES DISC version: 07"
        )

    GPM_3GPROFNOAA19MHS_CLIM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3GPROFNOAA19MHS_CLIM_07",
            provider="GES_DISC", 
            shortname="GPM_3GPROFNOAA19MHS_CLIM",
            version="07",
            description="GPM MHS on NOAA19 (GPROF) Radiometer Precipitation Profiling L3 1 month 0.25 degree x 0.25 degree V07 (GPM_3GPROFNOAA19MHS_CLIM) at GES DISC version: 07"
        )

    GPM_3CMB_TRMM_DAY_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3CMB_TRMM_DAY_07",
            provider="GES_DISC", 
            shortname="GPM_3CMB_TRMM_DAY",
            version="07",
            description="GPM PR and TMI on TRMM (Combined Precipitation) L3 1 day 0.25x0.25 degree V07 (GPM_3CMB_TRMM_DAY) at GES DISC version: 07"
        )

    GPM_3CMB_TRMM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3CMB_TRMM_07",
            provider="GES_DISC", 
            shortname="GPM_3CMB_TRMM",
            version="07",
            description="GPM PR and TMI on TRMM (Combined Precipitation) L3 1 month 0.25x0.25 degree V07 (GPM_3CMB_TRMM) at GES DISC version: 07"
        )

    GPM_2HCSH_TRMM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_2HCSH_TRMM_07",
            provider="GES_DISC", 
            shortname="GPM_2HCSH_TRMM",
            version="07",
            description="GPM PR and TMI on TRMM Combined Convective-Stratiform Latent Heating Profiles L2 1.5 hours 5 km V07 (GPM_2HCSH_TRMM) at GES DISC version: 07"
        )

    GPM_3HCSH_TRMM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3HCSH_TRMM_07",
            provider="GES_DISC", 
            shortname="GPM_3HCSH_TRMM",
            version="07",
            description="GPM PR and TMI on TRMM Combined Convective-Stratiform Latent Heating Profiles L3 1 month 0.25x0.25 degree V07 (GPM_3HCSH_TRMM) at GES DISC version: 07"
        )

    GPM_3GCSH_TRMM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3GCSH_TRMM_07",
            provider="GES_DISC", 
            shortname="GPM_3GCSH_TRMM",
            version="07",
            description="GPM PR and TMI on TRMM Combined Gridded Orbital Convective-Stratiform Latent Heating Profiles L3 1.5 hours 0.25x0.25 degree V07 (GPM_3GCSH_TRMM) at GES DISC version: 07"
        )

    GPM_2BCMB_TRMM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_2BCMB_TRMM_07",
            provider="GES_DISC", 
            shortname="GPM_2BCMB_TRMM",
            version="07",
            description="GPM PR and TMI on TRMM Combined Precipitation L2B 1.5 hours 5 km V07 (GPM_2BCMB_TRMM) at GES DISC version: 07"
        )

    GPM_1BPR_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_1BPR_07",
            provider="GES_DISC", 
            shortname="GPM_1BPR",
            version="07",
            description="GPM PR on TRMM Echo Power L1B 1.5 hours 5 km V07 (GPM_1BPR) at GES DISC version: 07"
        )

    GPM_3GSLH_TRMM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3GSLH_TRMM_07",
            provider="GES_DISC", 
            shortname="GPM_3GSLH_TRMM",
            version="07",
            description="GPM PR on TRMM Gridded Orbital Spectral Latent Heating Profiles L3 1.5 hours 0.5x0.5 degree V07 (GPM_3GSLH_TRMM) at GES DISC version: 07"
        )

    GPM_3PRD_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3PRD_07",
            provider="GES_DISC", 
            shortname="GPM_3PRD",
            version="07",
            description="GPM PR on TRMM Precipitation Statistics, at Surface and Fixed Heights 1 day 0.25x0.25 degree V07 (GPM_3PRD) at GES DISC version: 07"
        )

    GPM_2APR_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_2APR_07",
            provider="GES_DISC", 
            shortname="GPM_2APR",
            version="07",
            description="GPM PR on TRMM Reflectivity, Precipitation Characteristics and Rate, at Surface and Profile L2 1.5 hours V07 (GPM_2APR) at GES DISC version: 07"
        )

    GPM_3PR_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3PR_07",
            provider="GES_DISC", 
            shortname="GPM_3PR",
            version="07",
            description="GPM PR on TRMM Reflectivity, Precipitation Statistics, Histograms, at Surface and Fixed Heights, 1 month 5x5 and 0.25x0.25 degree V07 (GPM_3PR) at GES DISC version: 07"
        )

    GPM_3PR_ASC_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3PR_ASC_07",
            provider="GES_DISC", 
            shortname="GPM_3PR_ASC",
            version="07",
            description="GPM PR on TRMM Reflectivity, Precipitation Statistics, Histograms, at Surface and Fixed Heights, Ascending, 1 day 5x5 and 0.25x0.25 degree V07 (GPM_3PR_ASC) at GES DISC version: 07"
        )

    GPM_3PR_DES_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3PR_DES_07",
            provider="GES_DISC", 
            shortname="GPM_3PR_DES",
            version="07",
            description="GPM PR on TRMM Reflectivity, Precipitation Statistics, Histograms, at Surface and Fixed Heights, Descending, 1 day 5x5 and 0.25x0.25 degree V07 (GPM_3PR_DES) at GES DISC version: 07"
        )

    GPM_3HSLH_TRMM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3HSLH_TRMM_07",
            provider="GES_DISC", 
            shortname="GPM_3HSLH_TRMM",
            version="07",
            description="GPM PR on TRMM Spectral Latent Heating L3 1 month 0.5 degree x 0.5 degree V07 (GPM_3HSLH_TRMM) at GES DISC version: 07"
        )

    GPM_2HSLH_TRMM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_2HSLH_TRMM_07",
            provider="GES_DISC", 
            shortname="GPM_2HSLH_TRMM",
            version="07",
            description="GPM PR on TRMM Spectral Latent Heating Profiles L2 1.5 hours 5 km V07 (GPM_2HSLH_TRMM) at GES DISC version: 07"
        )

    GPM_3HSLH_TRMM_DAY_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3HSLH_TRMM_DAY_07",
            provider="GES_DISC", 
            shortname="GPM_3HSLH_TRMM_DAY",
            version="07",
            description="GPM PR on TRMM Spectral Latent Heating Profiles L3 1 Day 0.5x0.5 degree V07 (GPM_3HSLH_TRMM_DAY) at GES DISC version: 07"
        )

    GPM_2APRPSMT1SAPHIR_CLIM_V06_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_2APRPSMT1SAPHIR_CLIM_06",
            provider="GES_DISC", 
            shortname="GPM_2APRPSMT1SAPHIR_CLIM",
            version="06",
            description="GPM SAPHIR on MT1 (PRPS) Climate-based Radiometer Precipitation Profiling L2 1.5 hours 10 km V06 (GPM_2APRPSMT1SAPHIR_CLIM) at GES DISC version: 06"
        )

    GPM_3PRPSMT1SAPHIR_DAY_CLIM_V06_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3PRPSMT1SAPHIR_DAY_CLIM_06",
            provider="GES_DISC", 
            shortname="GPM_3PRPSMT1SAPHIR_DAY_CLIM",
            version="06",
            description="GPM SAPHIR on MT1 (PRPS) Climate-based Radiometer Precipitation Profiling L3 1 day 0.25 x 0.25 degree V06 (GPM_3PRPSMT1SAPHIR_DAY_CLIM) at GES DISC version: 06"
        )

    GPM_3PRPSMT1SAPHIR_CLIM_V06_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3PRPSMT1SAPHIR_CLIM_06",
            provider="GES_DISC", 
            shortname="GPM_3PRPSMT1SAPHIR_CLIM",
            version="06",
            description="GPM SAPHIR on MT1 (PRPS) Climate-based Radiometer Precipitation Profiling L3 1 month 0.25 x 0.25 degree V06 (GPM_3PRPSMT1SAPHIR_CLIM) at GES DISC version: 06"
        )

    GPM_2APRPSMT1SAPHIR_V06_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_2APRPSMT1SAPHIR_06",
            provider="GES_DISC", 
            shortname="GPM_2APRPSMT1SAPHIR",
            version="06",
            description="GPM SAPHIR on MT1 (PRPS) Radiometer Precipitation Profiling L2 1.5 hours 10 km V06 (GPM_2APRPSMT1SAPHIR) at GES DISC version: 06"
        )

    GPM_3PRPSMT1SAPHIR_DAY_V06_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3PRPSMT1SAPHIR_DAY_06",
            provider="GES_DISC", 
            shortname="GPM_3PRPSMT1SAPHIR_DAY",
            version="06",
            description="GPM SAPHIR on MT1 (PRPS) Radiometer Precipitation Profiling L3 1 day 0.25 x 0.25 degree V06 (GPM_3PRPSMT1SAPHIR_DAY) at GES DISC version: 06"
        )

    GPM_3PRPSMT1SAPHIR_V06_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3PRPSMT1SAPHIR_06",
            provider="GES_DISC", 
            shortname="GPM_3PRPSMT1SAPHIR",
            version="06",
            description="GPM SAPHIR on MT1 (PRPS) Radiometer Precipitation Profiling L3 1 month 0.25 x 0.25 degree V06 (GPM_3PRPSMT1SAPHIR) at GES DISC version: 06"
        )

    GPM_1CMT1SAPHIR_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_1CMT1SAPHIR_07",
            provider="GES_DISC", 
            shortname="GPM_1CMT1SAPHIR",
            version="07",
            description="GPM SAPHIR on MT1 Common Calibrated Brightness Temperature L1C 1.5 hours 10 km V07 (GPM_1CMT1SAPHIR) at GES DISC version: 07"
        )

    GPM_2AGPROFF08SSMI_CLIM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_2AGPROFF08SSMI_CLIM_07",
            provider="GES_DISC", 
            shortname="GPM_2AGPROFF08SSMI_CLIM",
            version="07",
            description="GPM SSM/I on F08 (GPROF) Climate-based Radiometer Precipitation Profiling L2 1.5 hours 12 km V07 (GPM_2AGPROFF08SSMI_CLIM) at GES DISC version: 07"
        )

    GPM_2AGPROFF10SSMI_CLIM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_2AGPROFF10SSMI_CLIM_07",
            provider="GES_DISC", 
            shortname="GPM_2AGPROFF10SSMI_CLIM",
            version="07",
            description="GPM SSM/I on F10 (GPROF) Climate-based Radiometer Precipitation Profiling L2 1.5 hours 12 km V07 (GPM_2AGPROFF10SSMI_CLIM) at GES DISC version: 07"
        )

    GPM_2AGPROFF11SSMI_CLIM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_2AGPROFF11SSMI_CLIM_07",
            provider="GES_DISC", 
            shortname="GPM_2AGPROFF11SSMI_CLIM",
            version="07",
            description="GPM SSM/I on F11 (GPROF) Climate-based Radiometer Precipitation Profiling L2 1.5 hours 13 km V07 (GPM_2AGPROFF11SSMI_CLIM) at GES DISC version: 07"
        )

    GPM_2AGPROFF13SSMI_CLIM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_2AGPROFF13SSMI_CLIM_07",
            provider="GES_DISC", 
            shortname="GPM_2AGPROFF13SSMI_CLIM",
            version="07",
            description="GPM SSM/I on F13 (GPROF) Climate-based Radiometer Precipitation Profiling L2 1.5 hours 12 km V07 (GPM_2AGPROFF13SSMI_CLIM) at GES DISC version: 07"
        )

    GPM_2AGPROFF14SSMI_CLIM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_2AGPROFF14SSMI_CLIM_07",
            provider="GES_DISC", 
            shortname="GPM_2AGPROFF14SSMI_CLIM",
            version="07",
            description="GPM SSM/I on F14 (GPROF) Climate-based Radiometer Precipitation Profiling L2 1.5 hours 12 km V07 (GPM_2AGPROFF14SSMI_CLIM) at GES DISC version: 07"
        )

    GPM_2AGPROFF15SSMI_CLIM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_2AGPROFF15SSMI_CLIM_07",
            provider="GES_DISC", 
            shortname="GPM_2AGPROFF15SSMI_CLIM",
            version="07",
            description="GPM SSM/I on F15 (GPROF) Climate-based Radiometer Precipitation Profiling L2 1.5 hours 12 km V07 (GPM_2AGPROFF15SSMI_CLIM) at GES DISC version: 07"
        )

    GPM_3GPROFF08SSMI_DAY_CLIM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3GPROFF08SSMI_DAY_CLIM_07",
            provider="GES_DISC", 
            shortname="GPM_3GPROFF08SSMI_DAY_CLIM",
            version="07",
            description="GPM SSMI on F08 (GPROF) Climate-based Radiometer Precipitation Profiling L3 1 day 0.25 degree x 0.25 degree V07 (GPM_3GPROFF08SSMI_DAY_CLIM) at GES DISC version: 07"
        )

    GPM_3GPROFF08SSMI_CLIM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3GPROFF08SSMI_CLIM_07",
            provider="GES_DISC", 
            shortname="GPM_3GPROFF08SSMI_CLIM",
            version="07",
            description="GPM SSMI on F08 (GPROF) Climate-based Radiometer Precipitation Profiling L3 1 month 0.25 degree x 0.25 degree V07 (GPM_3GPROFF08SSMI_CLIM) at GES DISC version: 07"
        )

    GPM_1CF08SSMI_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_1CF08SSMI_07",
            provider="GES_DISC", 
            shortname="GPM_1CF08SSMI",
            version="07",
            description="GPM SSMI on F08 Common Calibrated Brightness Temperatures L1C 1.5 hours 13 km V07 (GPM_1CF08SSMI) at GES DISC version: 07"
        )

    GPM_3GPROFF10SSMI_DAY_CLIM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3GPROFF10SSMI_DAY_CLIM_07",
            provider="GES_DISC", 
            shortname="GPM_3GPROFF10SSMI_DAY_CLIM",
            version="07",
            description="GPM SSMI on F10 (GPROF) Climate-based Radiometer Precipitation Profiling L3 1 day 0.25 degree x 0.25 degree V07 (GPM_3GPROFF10SSMI_DAY_CLIM) at GES DISC version: 07"
        )

    GPM_3GPROFF10SSMI_CLIM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3GPROFF10SSMI_CLIM_07",
            provider="GES_DISC", 
            shortname="GPM_3GPROFF10SSMI_CLIM",
            version="07",
            description="GPM SSMI on F10 (GPROF) Climate-based Radiometer Precipitation Profiling L3 1 month 0.25 degree x 0.25 degree V07 (GPM_3GPROFF10SSMI_CLIM) at GES DISC version: 07"
        )

    GPM_1CF10SSMI_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_1CF10SSMI_07",
            provider="GES_DISC", 
            shortname="GPM_1CF10SSMI",
            version="07",
            description="GPM SSMI on F10 Common Calibrated Brightness Temperatures L1C 1.5 hours 13 km V07 (GPM_1CF10SSMI) at GES DISC version: 07"
        )

    GPM_3GPROFF11SSMI_DAY_CLIM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3GPROFF11SSMI_DAY_CLIM_07",
            provider="GES_DISC", 
            shortname="GPM_3GPROFF11SSMI_DAY_CLIM",
            version="07",
            description="GPM SSMI on F11 (GPROF) Climate-based Radiometer Precipitation Profiling L3 1 day 0.25 degree x 0.25 degree V07 (GPM_3GPROFF11SSMI_DAY_CLIM) at GES DISC version: 07"
        )

    GPM_3GPROFF11SSMI_CLIM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3GPROFF11SSMI_CLIM_07",
            provider="GES_DISC", 
            shortname="GPM_3GPROFF11SSMI_CLIM",
            version="07",
            description="GPM SSMI on F11 (GPROF) Climate-based Radiometer Precipitation Profiling L3 1 month 0.25 degree x 0.25 degree V07 (GPM_3GPROFF11SSMI_CLIM) at GES DISC version: 07"
        )

    GPM_1CF11SSMI_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_1CF11SSMI_07",
            provider="GES_DISC", 
            shortname="GPM_1CF11SSMI",
            version="07",
            description="GPM SSMI on F11 Common Calibrated Brightness Temperatures L1C 1.5 hours 13 km V07 (GPM_1CF11SSMI) at GES DISC version: 07"
        )

    GPM_3GPROFF13SSMI_DAY_CLIM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3GPROFF13SSMI_DAY_CLIM_07",
            provider="GES_DISC", 
            shortname="GPM_3GPROFF13SSMI_DAY_CLIM",
            version="07",
            description="GPM SSMI on F13 (GPROF) Climate-based Radiometer Precipitation Profiling L3 1 day 0.25 degree x 0.25 degree V07 (GPM_3GPROFF13SSMI_DAY_CLIM) at GES DISC version: 07"
        )

    GPM_3GPROFF13SSMI_CLIM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3GPROFF13SSMI_CLIM_07",
            provider="GES_DISC", 
            shortname="GPM_3GPROFF13SSMI_CLIM",
            version="07",
            description="GPM SSMI on F13 (GPROF) Climate-based Radiometer Precipitation Profiling L3 1 month 0.25 degree x 0.25 degree V07 (GPM_3GPROFF13SSMI_CLIM) at GES DISC version: 07"
        )

    GPM_1CF13SSMI_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_1CF13SSMI_07",
            provider="GES_DISC", 
            shortname="GPM_1CF13SSMI",
            version="07",
            description="GPM SSMI on F13 Common Calibrated Brightness Temperatures L1C 1.5 hours 13 km V07 (GPM_1CF13SSMI) at GES DISC version: 07"
        )

    GPM_3GPROFF14SSMI_DAY_CLIM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3GPROFF14SSMI_DAY_CLIM_07",
            provider="GES_DISC", 
            shortname="GPM_3GPROFF14SSMI_DAY_CLIM",
            version="07",
            description="GPM SSMI on F14 (GPROF) Climate-based Radiometer Precipitation Profiling L3 1 day 0.25 degree x 0.25 degree V07 (GPM_3GPROFF14SSMI_DAY_CLIM) at GES DISC version: 07"
        )

    GPM_3GPROFF14SSMI_CLIM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3GPROFF14SSMI_CLIM_07",
            provider="GES_DISC", 
            shortname="GPM_3GPROFF14SSMI_CLIM",
            version="07",
            description="GPM SSMI on F14 (GPROF) Climate-based Radiometer Precipitation Profiling L3 1 month 0.25 degree x 0.25 degree V07 (GPM_3GPROFF14SSMI_CLIM) at GES DISC version: 07"
        )

    GPM_1CF14SSMI_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_1CF14SSMI_07",
            provider="GES_DISC", 
            shortname="GPM_1CF14SSMI",
            version="07",
            description="GPM SSMI on F14 Common Calibrated Brightness Temperatures L1C 1.5 hours 13 km V07 (GPM_1CF14SSMI) at GES DISC version: 07"
        )

    GPM_3GPROFF15SSMI_DAY_CLIM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3GPROFF15SSMI_DAY_CLIM_07",
            provider="GES_DISC", 
            shortname="GPM_3GPROFF15SSMI_DAY_CLIM",
            version="07",
            description="GPM SSMI on F15 (GPROF) Climate-based Radiometer Precipitation Profiling L3 1 day 0.25 degree x 0.25 degree V07 (GPM_3GPROFF15SSMI_DAY_CLIM) at GES DISC version: 07"
        )

    GPM_3GPROFF15SSMI_CLIM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3GPROFF15SSMI_CLIM_07",
            provider="GES_DISC", 
            shortname="GPM_3GPROFF15SSMI_CLIM",
            version="07",
            description="GPM SSMI on F15 (GPROF) Climate-based Radiometer Precipitation Profiling L3 1 month 0.25 degree x 0.25 degree V07 (GPM_3GPROFF15SSMI_CLIM) at GES DISC version: 07"
        )

    GPM_1CF15SSMI_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_1CF15SSMI_07",
            provider="GES_DISC", 
            shortname="GPM_1CF15SSMI",
            version="07",
            description="GPM SSMI on F15 Common Calibrated Brightness Temperatures L1C 1.5 hours 13 km V07 (GPM_1CF15SSMI) at GES DISC version: 07"
        )

    GPM_2AGPROFF16SSMIS_CLIM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_2AGPROFF16SSMIS_CLIM_07",
            provider="GES_DISC", 
            shortname="GPM_2AGPROFF16SSMIS_CLIM",
            version="07",
            description="GPM SSMIS on F16 (GPROF) Climate-based Radiometer Precipitation Profiling 1.5 hours 12 km V07 (GPM_2AGPROFF16SSMIS_CLIM) at GES DISC version: 07"
        )

    GPM_3GPROFF16SSMIS_DAY_CLIM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3GPROFF16SSMIS_DAY_CLIM_07",
            provider="GES_DISC", 
            shortname="GPM_3GPROFF16SSMIS_DAY_CLIM",
            version="07",
            description="GPM SSMIS on F16 (GPROF) Climate-based Radiometer Precipitation Profiling L3 1 day 0.25 degree x 0.25 degree V07 (GPM_3GPROFF16SSMIS_DAY_CLIM) at GES DISC version: 07"
        )

    GPM_3GPROFF16SSMIS_CLIM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3GPROFF16SSMIS_CLIM_07",
            provider="GES_DISC", 
            shortname="GPM_3GPROFF16SSMIS_CLIM",
            version="07",
            description="GPM SSMIS on F16 (GPROF) Climate-based Radiometer Precipitation Profiling L3 1 month 0.25 degree x 0.25 degree V07 (GPM_3GPROFF16SSMIS_CLIM) at GES DISC version: 07"
        )

    GPM_2AGPROFF16SSMIS_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_2AGPROFF16SSMIS_07",
            provider="GES_DISC", 
            shortname="GPM_2AGPROFF16SSMIS",
            version="07",
            description="GPM SSMIS on F16 (GPROF) Radiometer Precipitation Profiling L2 1.5 hours 12 km V07 (GPM_2AGPROFF16SSMIS) at GES DISC version: 07"
        )

    GPM_3GPROFF16SSMIS_DAY_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3GPROFF16SSMIS_DAY_07",
            provider="GES_DISC", 
            shortname="GPM_3GPROFF16SSMIS_DAY",
            version="07",
            description="GPM SSMIS on F16 (GPROF) Radiometer Precipitation Profiling L3 1 day 0.25 degree x 0.25 degree V07 (GPM_3GPROFF16SSMIS_DAY) at GES DISC version: 07"
        )

    GPM_3GPROFF16SSMIS_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3GPROFF16SSMIS_07",
            provider="GES_DISC", 
            shortname="GPM_3GPROFF16SSMIS",
            version="07",
            description="GPM SSMIS on F16 (GPROF) Radiometer Precipitation Profiling L3 1 month 0.25 degree x 0.25 degree V07 (GPM_3GPROFF16SSMIS) at GES DISC version: 07"
        )

    GPM_1CF16SSMIS_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_1CF16SSMIS_07",
            provider="GES_DISC", 
            shortname="GPM_1CF16SSMIS",
            version="07",
            description="GPM SSMIS on F16 Common Calibrated Brightness Temperatures L1C 1.5 hours 12 km V07 (GPM_1CF16SSMIS) at GES DISC version: 07"
        )

    GPM_2AGPROFF17SSMIS_CLIM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_2AGPROFF17SSMIS_CLIM_07",
            provider="GES_DISC", 
            shortname="GPM_2AGPROFF17SSMIS_CLIM",
            version="07",
            description="GPM SSMIS on F17 (GPROF) Climate-based Radiometer Precipitation Profiling 1.5 hours 12 km V07 (GPM_2AGPROFF17SSMIS_CLIM) at GES DISC version: 07"
        )

    GPM_3GPROFF17SSMIS_DAY_CLIM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3GPROFF17SSMIS_DAY_CLIM_07",
            provider="GES_DISC", 
            shortname="GPM_3GPROFF17SSMIS_DAY_CLIM",
            version="07",
            description="GPM SSMIS on F17 (GPROF) Climate-based Radiometer Precipitation Profiling L3 1 day 0.25 degree x 0.25 degree V07 (GPM_3GPROFF17SSMIS_DAY_CLIM) at GES DISC version: 07"
        )

    GPM_3GPROFF17SSMIS_CLIM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3GPROFF17SSMIS_CLIM_07",
            provider="GES_DISC", 
            shortname="GPM_3GPROFF17SSMIS_CLIM",
            version="07",
            description="GPM SSMIS on F17 (GPROF) Climate-based Radiometer Precipitation Profiling L3 1 month 0.25 degree x 0.25 degree V07 (GPM_3GPROFF17SSMIS_CLIM) at GES DISC version: 07"
        )

    GPM_2AGPROFF17SSMIS_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_2AGPROFF17SSMIS_07",
            provider="GES_DISC", 
            shortname="GPM_2AGPROFF17SSMIS",
            version="07",
            description="GPM SSMIS on F17 (GPROF) Radiometer Precipitation Profiling L2 1.5 hours 12 km V07 (GPM_2AGPROFF17SSMIS) at GES DISC version: 07"
        )

    GPM_3GPROFF17SSMIS_DAY_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3GPROFF17SSMIS_DAY_07",
            provider="GES_DISC", 
            shortname="GPM_3GPROFF17SSMIS_DAY",
            version="07",
            description="GPM SSMIS on F17 (GPROF) Radiometer Precipitation Profiling L3 1 day 0.25 degree x 0.25 degree V07 (GPM_3GPROFF17SSMIS_DAY) at GES DISC version: 07"
        )

    GPM_3GPROFF17SSMIS_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3GPROFF17SSMIS_07",
            provider="GES_DISC", 
            shortname="GPM_3GPROFF17SSMIS",
            version="07",
            description="GPM SSMIS on F17 (GPROF) Radiometer Precipitation Profiling L3 1 month 0.25 degree x 0.25 degree V07 (GPM_3GPROFF17SSMIS) at GES DISC version: 07"
        )

    GPM_1CF17SSMIS_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_1CF17SSMIS_07",
            provider="GES_DISC", 
            shortname="GPM_1CF17SSMIS",
            version="07",
            description="GPM SSMIS on F17 Common Calibrated Brightness Temperatures L1C 1.5 hours 12 km V07 (GPM_1CF17SSMIS) at GES DISC version: 07"
        )

    GPM_2AGPROFF18SSMIS_CLIM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_2AGPROFF18SSMIS_CLIM_07",
            provider="GES_DISC", 
            shortname="GPM_2AGPROFF18SSMIS_CLIM",
            version="07",
            description="GPM SSMIS on F18 (GPROF) Climate-based Radiometer Precipitation Profiling 1.5 hours 12 km V07 (GPM_2AGPROFF18SSMIS_CLIM) at GES DISC version: 07"
        )

    GPM_3GPROFF18SSMIS_DAY_CLIM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3GPROFF18SSMIS_DAY_CLIM_07",
            provider="GES_DISC", 
            shortname="GPM_3GPROFF18SSMIS_DAY_CLIM",
            version="07",
            description="GPM SSMIS on F18 (GPROF) Climate-based Radiometer Precipitation Profiling L3 1 day 0.25 degree x 0.25 degree V07 (GPM_3GPROFF18SSMIS_DAY_CLIM) at GES DISC version: 07"
        )

    GPM_3GPROFF18SSMIS_CLIM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3GPROFF18SSMIS_CLIM_07",
            provider="GES_DISC", 
            shortname="GPM_3GPROFF18SSMIS_CLIM",
            version="07",
            description="GPM SSMIS on F18 (GPROF) Climate-based Radiometer Precipitation Profiling L3 1 month 0.25 degree x 0.25 degree V07 (GPM_3GPROFF18SSMIS_CLIM) at GES DISC version: 07"
        )

    GPM_2AGPROFF18SSMIS_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_2AGPROFF18SSMIS_07",
            provider="GES_DISC", 
            shortname="GPM_2AGPROFF18SSMIS",
            version="07",
            description="GPM SSMIS on F18 (GPROF) Radiometer Precipitation Profiling L2 1.5 hours 12 km V07 (GPM_2AGPROFF18SSMIS) at GES DISC version: 07"
        )

    GPM_3GPROFF18SSMIS_DAY_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3GPROFF18SSMIS_DAY_07",
            provider="GES_DISC", 
            shortname="GPM_3GPROFF18SSMIS_DAY",
            version="07",
            description="GPM SSMIS on F18 (GPROF) Radiometer Precipitation Profiling L3 1 day 0.25 degree x 0.25 degree V07 (GPM_3GPROFF18SSMIS_DAY) at GES DISC version: 07"
        )

    GPM_3GPROFF18SSMIS_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3GPROFF18SSMIS_07",
            provider="GES_DISC", 
            shortname="GPM_3GPROFF18SSMIS",
            version="07",
            description="GPM SSMIS on F18 (GPROF) Radiometer Precipitation Profiling L3 1 month 0.25 degree x 0.25 degree V07 (GPM_3GPROFF18SSMIS) at GES DISC version: 07"
        )

    GPM_1CF18SSMIS_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_1CF18SSMIS_07",
            provider="GES_DISC", 
            shortname="GPM_1CF18SSMIS",
            version="07",
            description="GPM SSMIS on F18 Common Calibrated Brightness Temperatures L1C 1.5 hours 12 km V07 (GPM_1CF18SSMIS) at GES DISC version: 07"
        )

    GPM_2AGPROFF19SSMIS_CLIM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_2AGPROFF19SSMIS_CLIM_07",
            provider="GES_DISC", 
            shortname="GPM_2AGPROFF19SSMIS_CLIM",
            version="07",
            description="GPM SSMIS on F19 (GPROF) Climate-based Radiometer Precipitation Profiling 1.5 hours 12 km V07 (GPM_2AGPROFF19SSMIS_CLIM) at GES DISC version: 07"
        )

    GPM_3GPROFF19SSMIS_DAY_CLIM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3GPROFF19SSMIS_DAY_CLIM_07",
            provider="GES_DISC", 
            shortname="GPM_3GPROFF19SSMIS_DAY_CLIM",
            version="07",
            description="GPM SSMIS on F19 (GPROF) Climate-based Radiometer Precipitation Profiling L3 1 day 0.25 degree x 0.25 degree V07 (GPM_3GPROFF19SSMIS_DAY_CLIM) at GES DISC version: 07"
        )

    GPM_3GPROFF19SSMIS_CLIM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3GPROFF19SSMIS_CLIM_07",
            provider="GES_DISC", 
            shortname="GPM_3GPROFF19SSMIS_CLIM",
            version="07",
            description="GPM SSMIS on F19 (GPROF) Climate-based Radiometer Precipitation Profiling L3 1 month 0.25 degree x 0.25 degree V07 (GPM_3GPROFF19SSMIS_CLIM) at GES DISC version: 07"
        )

    GPM_1CF19SSMIS_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_1CF19SSMIS_07",
            provider="GES_DISC", 
            shortname="GPM_1CF19SSMIS",
            version="07",
            description="GPM SSMIS on F19 Common Calibrated Brightness Temperatures L1C 1.5 hours 12 km V07 (GPM_1CF19SSMIS) at GES DISC version: 07"
        )

    GPM_2AGPROFTRMMTMI_CLIM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_2AGPROFTRMMTMI_CLIM_07",
            provider="GES_DISC", 
            shortname="GPM_2AGPROFTRMMTMI_CLIM",
            version="07",
            description="GPM TMI on TRMM (GPROF) Climate-based Radiometer Precipitation Profiling L2A 1.5 hours 13 km V07 (GPM_2AGPROFTRMMTMI_CLIM) at GES DISC version: 07"
        )

    GPM_3GPROFTRMMTMI_DAY_CLIM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3GPROFTRMMTMI_DAY_CLIM_07",
            provider="GES_DISC", 
            shortname="GPM_3GPROFTRMMTMI_DAY_CLIM",
            version="07",
            description="GPM TMI on TRMM (GPROF) Climate-based Radiometer Precipitation Profiling L3 1 day 0.25 degree x 0.25 degree V07 (GPM_3GPROFTRMMTMI_DAY_CLIM) at GES DISC version: 07"
        )

    GPM_3GPROFTRMMTMI_CLIM_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_3GPROFTRMMTMI_CLIM_07",
            provider="GES_DISC", 
            shortname="GPM_3GPROFTRMMTMI_CLIM",
            version="07",
            description="GPM TMI on TRMM (GPROF) Climate-based Radiometer Precipitation Profiling L3 1 month 0.25 degree x 0.25 degree V07 (GPM_3GPROFTRMMTMI_CLIM) at GES DISC version: 07"
        )

    GPM_BASETRMMTMI_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_BASETRMMTMI_07",
            provider="GES_DISC", 
            shortname="GPM_BASETRMMTMI",
            version="07",
            description="GPM TMI on TRMM Antenna Temperatures L1BASE 1.5 hours 13 km V07 (GPM_BASETRMMTMI) at GES DISC version: 07"
        )

    GPM_1BTMI_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_1BTMI_07",
            provider="GES_DISC", 
            shortname="GPM_1BTMI",
            version="07",
            description="GPM TMI on TRMM Brightness Temperatures L1B 1.5 hours 13 km V07 (GPM_1BTMI) at GES DISC version: 07"
        )

    GPM_1CTRMMTMI_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_1CTRMMTMI_07",
            provider="GES_DISC", 
            shortname="GPM_1CTRMMTMI",
            version="07",
            description="GPM TMI on TRMM Common Calibrated Brightness Temperatures L1C 1.5 hours 13 km V07 (GPM_1CTRMMTMI) at GES DISC version: 07"
        )

    GPM_1ATMI_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_1ATMI_07",
            provider="GES_DISC", 
            shortname="GPM_1ATMI",
            version="07",
            description="GPM TMI on TRMM unpacked data L1A 1.5 hours 13 km V07 (GPM_1ATMI) at GES DISC version: 07"
        )

    GPM_1BVIRS_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_1BVIRS_07",
            provider="GES_DISC", 
            shortname="GPM_1BVIRS",
            version="07",
            description="GPM VIRS on TRMM Radiance L1B 1.5 hours 2 km V07 (GPM_1BVIRS) at GES DISC version: 07"
        )

    GPM_1AVIRS_V07_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_1AVIRS_07",
            provider="GES_DISC", 
            shortname="GPM_1AVIRS",
            version="07",
            description="GPM VIRS on TRMM unpacked data L1A 1.5 hours 2 km V07 (GPM_1AVIRS) at GES DISC version: 07"
        )

    GPSROZPBLA_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPSROZPBLA_1",
            provider="GES_DISC", 
            shortname="GPSROZPBLA",
            version="1",
            description="GPS Radio Occultation Boundary Layer Depth Annual L3 V1 (GPSROZPBLA) at GES DISC version: 1"
        )

    GPSROZPBLA_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPSROZPBLA_2",
            provider="GES_DISC", 
            shortname="GPSROZPBLA",
            version="2",
            description="GPS Radio Occultation Boundary Layer Depth Annual L3 V2 (GPSROZPBLA) at GES DISC version: 2"
        )

    GPSROZPBLS_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPSROZPBLS_1",
            provider="GES_DISC", 
            shortname="GPSROZPBLS",
            version="1",
            description="GPS Radio Occultation Boundary Layer Depth Seasonal L3 V1 (GPSROZPBLS) at GES DISC version: 1"
        )

    GPSROZPBLS_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPSROZPBLS_2",
            provider="GES_DISC", 
            shortname="GPSROZPBLS",
            version="2",
            description="GPS Radio Occultation Boundary Layer Depth Seasonal L3 V2 (GPSROZPBLS) at GES DISC version: 2"
        )

    GVHRRATS6IMIR_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GVHRRATS6IMIR_001",
            provider="GES_DISC", 
            shortname="GVHRRATS6IMIR",
            version="001",
            description="GVHRR/ATS-6 Black and White Infrared Images on Film V001 (GVHRRATS6IMIR) at GES DISC version: 001"
        )

    GVHRRATS6IMVIS_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GVHRRATS6IMVIS_001",
            provider="GES_DISC", 
            shortname="GVHRRATS6IMVIS",
            version="001",
            description="GVHRR/ATS-6 Black and White Visible Images on Film V001 (GVHRRATS6IMVIS) at GES DISC version: 001"
        )

    GFEI_CH4_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GFEI_CH4_1",
            provider="GES_DISC", 
            shortname="GFEI_CH4",
            version="1",
            description="Global Inventory of Methane Emissions from Fuel Exploitation V1 (GFEI_CH4) version: 1"
        )

    GLOBAL_LANDSLIDE_NOWCAST_V11_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_Global_Landslide_Nowcast_1.1",
            provider="GES_DISC", 
            shortname="Global_Landslide_Nowcast",
            version="1.1",
            description="Global Landslide Nowcast from LHASA L4 1 day 1 km x 1 km version 1.1 (Global_Landslide_Nowcast) at GES DISC version: 1.1"
        )

    GLOBAL_LANDSLIDE_NOWCAST_V200_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_Global_Landslide_Nowcast_2.0.0",
            provider="GES_DISC", 
            shortname="Global_Landslide_Nowcast",
            version="2.0.0",
            description="Global Landslide Nowcast from LHASA L4 1 day 1 km x 1 km version 2.0.0 (Global_Landslide_Nowcast) at GES DISC version: 2.0.0"
        )

    CMSGCH4F_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_CMSGCH4F_1",
            provider="GES_DISC", 
            shortname="CMSGCH4F",
            version="1",
            description="Global methane fluxes optimized with GOSAT data for 2010-2018 V1 (CMSGCH4F) version: 1"
        )

    GSSTFMC_V3_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GSSTFMC_3",
            provider="GES_DISC", 
            shortname="GSSTFMC",
            version="3",
            description="Goddard Satellite-Based Surface Turbulent Fluxes Climatology, 0.25 x 0.25 deg, Monthly Grid V3 (GSSTFMC) at GES DISC version: 3"
        )

    GSSTFSC_V3_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GSSTFSC_3",
            provider="GES_DISC", 
            shortname="GSSTFSC",
            version="3",
            description="Goddard Satellite-Based Surface Turbulent Fluxes Climatology, 0.25 x 0.25 deg, Seasonal Grid V3 (GSSTFSC) at GES DISC version: 3"
        )

    GSSTFYC_V3_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GSSTFYC_3",
            provider="GES_DISC", 
            shortname="GSSTFYC",
            version="3",
            description="Goddard Satellite-Based Surface Turbulent Fluxes Climatology, 0.25 x 0.25 deg, Yearly Grid V3 (GSSTFYC) at GES DISC version: 3"
        )

    GSSTF_F08_V3_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GSSTF_F08_3",
            provider="GES_DISC", 
            shortname="GSSTF_F08",
            version="3",
            description="Goddard Satellite-Based Surface Turbulent Fluxes, 0.25 x 0.25 deg, Daily Grid F08 V3 (GSSTF_F08) at GES DISC version: 3"
        )

    GSSTF_F10_V3_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GSSTF_F10_3",
            provider="GES_DISC", 
            shortname="GSSTF_F10",
            version="3",
            description="Goddard Satellite-Based Surface Turbulent Fluxes, 0.25 x 0.25 deg, Daily Grid F10 V3 (GSSTF_F10) at GES DISC version: 3"
        )

    GSSTF_F11_V3_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GSSTF_F11_3",
            provider="GES_DISC", 
            shortname="GSSTF_F11",
            version="3",
            description="Goddard Satellite-Based Surface Turbulent Fluxes, 0.25 x 0.25 deg, Daily Grid F11 V3 (GSSTF_F11) at GES DISC version: 3"
        )

    GSSTF_F13_V3_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GSSTF_F13_3",
            provider="GES_DISC", 
            shortname="GSSTF_F13",
            version="3",
            description="Goddard Satellite-Based Surface Turbulent Fluxes, 0.25 x 0.25 deg, Daily Grid F13 V3 (GSSTF_F13) at GES DISC version: 3"
        )

    GSSTF_F14_V3_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GSSTF_F14_3",
            provider="GES_DISC", 
            shortname="GSSTF_F14",
            version="3",
            description="Goddard Satellite-Based Surface Turbulent Fluxes, 0.25 x 0.25 deg, Daily Grid F14 V3 (GSSTF_F14) at GES DISC version: 3"
        )

    GSSTF_F15_V3_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GSSTF_F15_3",
            provider="GES_DISC", 
            shortname="GSSTF_F15",
            version="3",
            description="Goddard Satellite-Based Surface Turbulent Fluxes, 0.25 x 0.25 deg, Daily Grid F15 V3 (GSSTF_F15) at GES DISC version: 3"
        )

    GSSTF_V3_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GSSTF_3",
            provider="GES_DISC", 
            shortname="GSSTF",
            version="3",
            description="Goddard Satellite-Based Surface Turbulent Fluxes, 0.25 x 0.25 deg, Daily Grid V3 (GSSTF) at GES DISC version: 3"
        )

    GSSTFM_V3_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GSSTFM_3",
            provider="GES_DISC", 
            shortname="GSSTFM",
            version="3",
            description="Goddard Satellite-Based Surface Turbulent Fluxes, 0.25 x 0.25 deg, Monthly Grid V3 (GSSTFM) at GES DISC version: 3"
        )

    GSSTF_F08_V2C_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GSSTF_F08_2c",
            provider="GES_DISC", 
            shortname="GSSTF_F08",
            version="2c",
            description="Goddard Satellite-Based Surface Turbulent Fluxes, 1x1 deg Daily Grid, Satellite F08 V2c (GSSTF_F08) at GES DISC version: 2c"
        )

    GSSTF_F10_V2C_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GSSTF_F10_2c",
            provider="GES_DISC", 
            shortname="GSSTF_F10",
            version="2c",
            description="Goddard Satellite-Based Surface Turbulent Fluxes, 1x1 deg Daily Grid, Satellite F10 V2c (GSSTF_F10) at GES DISC version: 2c"
        )

    GSSTF_F11_V2C_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GSSTF_F11_2c",
            provider="GES_DISC", 
            shortname="GSSTF_F11",
            version="2c",
            description="Goddard Satellite-Based Surface Turbulent Fluxes, 1x1 deg Daily Grid, Satellite F11 V2c (GSSTF_F11) at GES DISC version: 2c"
        )

    GSSTF_F13_V2C_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GSSTF_F13_2c",
            provider="GES_DISC", 
            shortname="GSSTF_F13",
            version="2c",
            description="Goddard Satellite-Based Surface Turbulent Fluxes, 1x1 deg Daily Grid, Satellite F13 V2c (GSSTF_F13) at GES DISC version: 2c"
        )

    GSSTF_F14_V2C_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GSSTF_F14_2c",
            provider="GES_DISC", 
            shortname="GSSTF_F14",
            version="2c",
            description="Goddard Satellite-Based Surface Turbulent Fluxes, 1x1 deg Daily Grid, Satellite F14 V2c (GSSTF_F14) at GES DISC version: 2c"
        )

    GSSTF_F15_V2C_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GSSTF_F15_2c",
            provider="GES_DISC", 
            shortname="GSSTF_F15",
            version="2c",
            description="Goddard Satellite-Based Surface Turbulent Fluxes, 1x1 deg Daily Grid, Satellite F15 V2c (GSSTF_F15) at GES DISC version: 2c"
        )

    GSSTF_V2C_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GSSTF_2c",
            provider="GES_DISC", 
            shortname="GSSTF",
            version="2c",
            description="Goddard Satellite-Based Surface Turbulent Fluxes, 1x1 deg Daily Grid, Set1 V2c (GSSTF) at GES DISC version: 2c"
        )

    GSSTFMC_V2C_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GSSTFMC_2c",
            provider="GES_DISC", 
            shortname="GSSTFMC",
            version="2c",
            description="Goddard Satellite-Based Surface Turbulent Fluxes, 1x1 deg Monthly Climatology, Set1 and NCEP V2c (GSSTFMC) at GES DISC version: 2c"
        )

    GSSTFM_V2C_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GSSTFM_2c",
            provider="GES_DISC", 
            shortname="GSSTFM",
            version="2c",
            description="Goddard Satellite-Based Surface Turbulent Fluxes, 1x1 deg Monthly Grid, Set1 and Interpolated Data V2c (GSSTFM) at GES DISC version: 2c"
        )

    GSSTFSC_V2C_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GSSTFSC_2c",
            provider="GES_DISC", 
            shortname="GSSTFSC",
            version="2c",
            description="Goddard Satellite-Based Surface Turbulent Fluxes, 1x1 deg Seasonal Climatology, Set1 and NCEP V2c (GSSTFSC) at GES DISC version: 2c"
        )

    GSSTFYC_V2C_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GSSTFYC_2c",
            provider="GES_DISC", 
            shortname="GSSTFYC",
            version="2c",
            description="Goddard Satellite-Based Surface Turbulent Fluxes, 1x1 deg Yearly Climatology, Set1 and NCEP V2c (GSSTFYC) at GES DISC version: 2c"
        )

    GRACEDADM_CLSM0125US_7D_V40_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GRACEDADM_CLSM0125US_7D_4.0",
            provider="GES_DISC", 
            shortname="GRACEDADM_CLSM0125US_7D",
            version="4.0",
            description="Groundwater and Soil Moisture Conditions from GRACE and GRACE-FO Data Assimilation L4 7-days 0.125 x 0.125 degree U.S. V4.0 (GRACEDADM_CLSM0125US_7D) at GES DISC version: 4.0"
        )

    GRACEDADM_CLSM025GL_7D_V30_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GRACEDADM_CLSM025GL_7D_3.0",
            provider="GES_DISC", 
            shortname="GRACEDADM_CLSM025GL_7D",
            version="3.0",
            description="Groundwater and Soil Moisture Conditions from GRACE and GRACE-FO Data Assimilation L4 7-days 0.25 x 0.25 degree Global V3.0 (GRACEDADM_CLSM025GL_7D) at GES DISC version: 3.0"
        )

    HAQ_TROPOMI_NO2_CONUS_A_L3_V24_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_HAQ_TROPOMI_NO2_CONUS_A_L3_2.4",
            provider="GES_DISC", 
            shortname="HAQ_TROPOMI_NO2_CONUS_A_L3",
            version="2.4",
            description="HAQAST Sentinel-5P TROPOMI Nitrogen Dioxide (NO2) CONUS Annual Level 3 0.01 x 0.01 Degree Gridded Data V2.4 (HAQ_TROPOMI_NO2_CONUS_A_L3) at GES DISC version: 2.4"
        )

    HAQ_TROPOMI_NO2_CONUS_M_L3_V24_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_HAQ_TROPOMI_NO2_CONUS_M_L3_2.4",
            provider="GES_DISC", 
            shortname="HAQ_TROPOMI_NO2_CONUS_M_L3",
            version="2.4",
            description="HAQAST Sentinel-5P TROPOMI Nitrogen Dioxide (NO2) CONUS Monthly Level 3 0.01 x 0.01 Degree Gridded Data V2.4 (HAQ_TROPOMI_NO2_CONUS_M_L3) at GES DISC version: 2.4"
        )

    HAQ_TROPOMI_NO2_CONUS_S_L3_V24_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_HAQ_TROPOMI_NO2_CONUS_S_L3_2.4",
            provider="GES_DISC", 
            shortname="HAQ_TROPOMI_NO2_CONUS_S_L3",
            version="2.4",
            description="HAQAST Sentinel-5P TROPOMI Nitrogen Dioxide (NO2) CONUS Seasonal Level 3 0.01 x 0.01 Degree Gridded Data V2.4 (HAQ_TROPOMI_NO2_CONUS_S_L3) at GES DISC version: 2.4"
        )

    HAQ_TROPOMI_NO2_GLOBAL_A_L3_V24_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_HAQ_TROPOMI_NO2_GLOBAL_A_L3_2.4",
            provider="GES_DISC", 
            shortname="HAQ_TROPOMI_NO2_GLOBAL_A_L3",
            version="2.4",
            description="HAQAST Sentinel-5P TROPOMI Nitrogen Dioxide (NO2) GLOBAL Annual Level 3 0.1 x 0.1 Degree Gridded Data Version 2.4 (HAQ_TROPOMI_NO2_GLOBAL_A_L3) at GES DISC version: 2.4"
        )

    HAQ_TROPOMI_NO2_GLOBAL_M_L3_V24_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_HAQ_TROPOMI_NO2_GLOBAL_M_L3_2.4",
            provider="GES_DISC", 
            shortname="HAQ_TROPOMI_NO2_GLOBAL_M_L3",
            version="2.4",
            description="HAQAST Sentinel-5P TROPOMI Nitrogen Dioxide (NO2) GLOBAL Monthly Level 3 0.1 x 0.1 Degree Gridded Data Version 2.4 (HAQ_TROPOMI_NO2_GLOBAL_M_L3) at GES DISC version: 2.4"
        )

    HAQES_NA_PM25_BC_CENSUS_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_HAQES_NA_PM25_BC_CENSUS_1",
            provider="GES_DISC", 
            shortname="HAQES_NA_PM25_BC_CENSUS",
            version="1",
            description="HAQES 3-Hourly Ensemble mean surface PM2.5 Black Carbon concentration at census level, North America V1 (HAQES_NA_PM25_BC_CENSUS) at GES DISC version: 1"
        )

    HAQES_NA_PM25_BC_COUNTY_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_HAQES_NA_PM25_BC_COUNTY_1",
            provider="GES_DISC", 
            shortname="HAQES_NA_PM25_BC_COUNTY",
            version="1",
            description="HAQES 3-Hourly Ensemble mean surface PM2.5 Black Carbon concentration at county level, North America V1 (HAQES_NA_PM25_BC_COUNTY) at GES DISC version: 1"
        )

    HAQES_NA_PM25_BC_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_HAQES_NA_PM25_BC_1",
            provider="GES_DISC", 
            shortname="HAQES_NA_PM25_BC",
            version="1",
            description="HAQES 3-Hourly Ensemble mean surface PM2.5 Black Carbon concentration, North America V1 (HAQES_NA_PM25_BC) at GES DISC version: 1"
        )

    HAQES_NA_PM25_OC_CENSUS_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_HAQES_NA_PM25_OC_CENSUS_1",
            provider="GES_DISC", 
            shortname="HAQES_NA_PM25_OC_CENSUS",
            version="1",
            description="HAQES 3-Hourly Ensemble mean surface PM2.5 Organic Carbon concentration at census level, North America V1 (HAQES_NA_PM25_OC_CENSUS) at GES DISC version: 1"
        )

    HAQES_NA_PM25_OC_COUNTY_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_HAQES_NA_PM25_OC_COUNTY_1",
            provider="GES_DISC", 
            shortname="HAQES_NA_PM25_OC_COUNTY",
            version="1",
            description="HAQES 3-Hourly Ensemble mean surface PM2.5 Organic Carbon concentration at county level, North America V1 (HAQES_NA_PM25_OC_COUNTY) at GES DISC version: 1"
        )

    HAQES_NA_PM25_OC_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_HAQES_NA_PM25_OC_1",
            provider="GES_DISC", 
            shortname="HAQES_NA_PM25_OC",
            version="1",
            description="HAQES 3-Hourly Ensemble mean surface PM2.5 Organic Carbon concentration, North America V1 (HAQES_NA_PM25_OC) at GES DISC version: 1"
        )

    HAQES_NA_PM25_TOT_CENSUS_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_HAQES_NA_PM25_TOT_CENSUS_1",
            provider="GES_DISC", 
            shortname="HAQES_NA_PM25_TOT_CENSUS",
            version="1",
            description="HAQES 3-Hourly Ensemble mean surface total PM2.5 concentration at census level, North America V1 (HAQES_NA_PM25_TOT_CENSUS) at GES DISC version: 1"
        )

    HAQES_NA_PM25_TOT_COUNTY_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_HAQES_NA_PM25_TOT_COUNTY_1",
            provider="GES_DISC", 
            shortname="HAQES_NA_PM25_TOT_COUNTY",
            version="1",
            description="HAQES 3-Hourly Ensemble mean surface total PM2.5 concentration at county level, North America V1 (HAQES_NA_PM25_TOT_COUNTY) at GES DISC version: 1"
        )

    HAQES_NA_PM25_TOT_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_HAQES_NA_PM25_TOT_1",
            provider="GES_DISC", 
            shortname="HAQES_NA_PM25_TOT",
            version="1",
            description="HAQES 3-Hourly Ensemble mean surface total PM2.5 concentration, North America V1 (HAQES_NA_PM25_TOT) at GES DISC version: 1"
        )

    HIRMLS3IWC_V002_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_HIRMLS3IWC_002",
            provider="GES_DISC", 
            shortname="HIRMLS3IWC",
            version="002",
            description="HIRDLS-MLS/Aura Level 3 Monthly 10 x 20 deg Ice Water Content V002 (HIRMLS3IWC) at GES DISC version: 002"
        )

    HIRDLS2_V007_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_HIRDLS2_007",
            provider="GES_DISC", 
            shortname="HIRDLS2",
            version="007",
            description="HIRDLS/Aura Level 2 Daily Geophysical Parameters V007 (HIRDLS2) at GES DISC version: 007"
        )

    H3ZFCCLONO2_V007_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_H3ZFCCLONO2_007",
            provider="GES_DISC", 
            shortname="H3ZFCCLONO2",
            version="007",
            description="HIRDLS/Aura Level 3 Chlorine Nitrate (ClONO2) 1deg Lat Zonal Fourier Coefficients V007 (H3ZFCCLONO2) at GES DISC version: 007"
        )

    H3ZFCCFC11_V007_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_H3ZFCCFC11_007",
            provider="GES_DISC", 
            shortname="H3ZFCCFC11",
            version="007",
            description="HIRDLS/Aura Level 3 Chlorofluorocarbon-11 (CFC-11) 1deg Lat Zonal Fourier Coefficients V007 (H3ZFCCFC11) at GES DISC version: 007"
        )

    H3ZFCCFC12_V007_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_H3ZFCCFC12_007",
            provider="GES_DISC", 
            shortname="H3ZFCCFC12",
            version="007",
            description="HIRDLS/Aura Level 3 Chlorofluorocarbon-12 (CFC-12) 1deg Lat Zonal Fourier Coefficients V007 (H3ZFCCFC11) at GES DISC version: 007"
        )

    HIR3SCOL_V007_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_HIR3SCOL_007",
            provider="GES_DISC", 
            shortname="HIR3SCOL",
            version="007",
            description="HIRDLS/Aura Level 3 Daily Gridded 1 x 1 deg Stratospheric Columns of NO2 V007 (HIR3SCOL) at GES DISC version: 007"
        )

    H3ZFCN2O5_V007_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_H3ZFCN2O5_007",
            provider="GES_DISC", 
            shortname="H3ZFCN2O5",
            version="007",
            description="HIRDLS/Aura Level 3 Dinitrogen Pentoxide (N2O5) 1deg Lat Zonal Fourier Coefficients V007 (H3ZFCN2O5) at GES DISC version: 007"
        )

    H3ZFC12MEXT_V007_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_H3ZFC12MEXT_007",
            provider="GES_DISC", 
            shortname="H3ZFC12MEXT",
            version="007",
            description="HIRDLS/Aura Level 3 Extinction at 12.1 Microns 1deg Lat Zonal Fourier Coefficients V007 (H3ZFC12MEXT) at GES DISC version: 007"
        )

    H3ZFC8MEXT_V007_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_H3ZFC8MEXT_007",
            provider="GES_DISC", 
            shortname="H3ZFC8MEXT",
            version="007",
            description="HIRDLS/Aura Level 3 Extinction at 8.3 Microns 1deg Lat Zonal Fourier Coefficients V007 (H3ZFC8MEXT) at GES DISC version: 007"
        )

    H3ZFCGPH_V007_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_H3ZFCGPH_007",
            provider="GES_DISC", 
            shortname="H3ZFCGPH",
            version="007",
            description="HIRDLS/Aura Level 3 Geopotential Height 1deg Lat Zonal Fourier Coefficients V007 (H3ZFCGPH) at GES DISC version: 007"
        )

    H3ZFCHNO3_V007_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_H3ZFCHNO3_007",
            provider="GES_DISC", 
            shortname="H3ZFCHNO3",
            version="007",
            description="HIRDLS/Aura Level 3 Nitric Acid (HNO3) 1deg Lat Zonal Fourier Coefficients V007 (H3ZFCHNO3) at GES DISC version: 007"
        )

    H3ZFCNO2_V007_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_H3ZFCNO2_007",
            provider="GES_DISC", 
            shortname="H3ZFCNO2",
            version="007",
            description="HIRDLS/Aura Level 3 Nitrogen Dioxide (NO2) 1deg Lat Zonal Fourier Coefficients V007 (H3ZFCNO2) at GES DISC version: 007"
        )

    H3ZFCN2O_V007_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_H3ZFCN2O_007",
            provider="GES_DISC", 
            shortname="H3ZFCN2O",
            version="007",
            description="HIRDLS/Aura Level 3 Nitrous Oxide (N2O) 1deg Lat Zonal Fourier Coefficients V007 (H3ZFCN2O) at GES DISC version: 007"
        )

    H3ZFCO3_V007_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_H3ZFCO3_007",
            provider="GES_DISC", 
            shortname="H3ZFCO3",
            version="007",
            description="HIRDLS/Aura Level 3 Ozone (O3) 1deg Lat Zonal Fourier Coefficients V007 (H3ZFCO3) at GES DISC version: 007"
        )

    H3ZFCT_V007_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_H3ZFCT_007",
            provider="GES_DISC", 
            shortname="H3ZFCT",
            version="007",
            description="HIRDLS/Aura Level 3 Temperature 1deg Lat Zonal Fourier Coefficients V007 (H3ZFCT) at GES DISC version: 007"
        )

    H3ZFCH2O_V007_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_H3ZFCH2O_007",
            provider="GES_DISC", 
            shortname="H3ZFCH2O",
            version="007",
            description="HIRDLS/Aura Level 3 Water Vapor (H2O) 1deg Lat Zonal Fourier Coefficients V007 (H3ZFCH2O) at GES DISC version: 007"
        )

    HIRSN6IM_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_HIRSN6IM_001",
            provider="GES_DISC", 
            shortname="HIRSN6IM",
            version="001",
            description="HIRS/Nimbus-6 Images of Brightness Temperature on 70 mm Film V001 (HIRSN6IM) at GES DISC version: 001"
        )

    HIRSN6L1GARP_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_HIRSN6L1GARP_001",
            provider="GES_DISC", 
            shortname="HIRSN6L1GARP",
            version="001",
            description="HIRS/Nimbus-6 Level 1 Calibrated Radiances for the Global Atmospheric Research Program (GARP) V001 (HIRSN6L1GARP) at GES DISC version: 001"
        )

    HRIRN1IM_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_HRIRN1IM_001",
            provider="GES_DISC", 
            shortname="HRIRN1IM",
            version="001",
            description="HRIR/Nimbus-1 Images of Nighttime Brightness Temperature on 70 mm Film V001 (HRIRN1IM) at GES DISC version: 001"
        )

    HRIRN1L1_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_HRIRN1L1_001",
            provider="GES_DISC", 
            shortname="HRIRN1L1",
            version="001",
            description="HRIR/Nimbus-1 Level 1 Meteorological Radiation Data V001 (HRIRN1L1) at GES DISC version: 001"
        )

    HRIRN2IM_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_HRIRN2IM_001",
            provider="GES_DISC", 
            shortname="HRIRN2IM",
            version="001",
            description="HRIR/Nimbus-2 Images of Nighttime Brightness Temperature on 70 mm Film V001 (HRIRN2IM) at GES DISC version: 001"
        )

    HRIRN2L1_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_HRIRN2L1_001",
            provider="GES_DISC", 
            shortname="HRIRN2L1",
            version="001",
            description="HRIR/Nimbus-2 Level 1 Meteorological Radiation Data V001 (HRIRN2L1) at GES DISC version: 001"
        )

    HRIRN3IM_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_HRIRN3IM_001",
            provider="GES_DISC", 
            shortname="HRIRN3IM",
            version="001",
            description="HRIR/Nimbus-3 Images of Daytime and Nighttime Brightness Temperature on 70 mm Film V001 (HRIRN3IM) at GES DISC version: 001"
        )

    HRIRN3L1_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_HRIRN3L1_001",
            provider="GES_DISC", 
            shortname="HRIRN3L1",
            version="001",
            description="HRIR/Nimbus-3 Level 1 Meteorological Radiation Data V001 (HRIRN3L1) at GES DISC version: 001"
        )

    HRAC_PRECIP_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_HRAC_Precip_1",
            provider="GES_DISC", 
            shortname="HRAC_Precip",
            version="1",
            description="High Resolution Altitude Corrected Precipitation based on TMPA and other sources L4 Monthly 1 km x 1 km V1 (HRAC_Precip) at GES DISC version: 1"
        )

    CMS_HR_MNA_CH4_FLUX_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_CMS_HR_MNA_CH4_FLUX_1",
            provider="GES_DISC", 
            shortname="CMS_HR_MNA_CH4_FLUX",
            version="1",
            description="High-resolution mean North American methane fluxes for 2010-2015 optimized with GOSAT satellite data V1 (CMS_HR_MNA_CH4_FLUX) version: 1"
        )

    GLOBAL_LANDSLIDE_EXPOSURE_MAPS_V10_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_Global_Landslide_Exposure_Maps_1.0",
            provider="GES_DISC", 
            shortname="Global_Landslide_Exposure_Maps",
            version="1.0",
            description="IMERG and LHASA Global Landslide Exposure Maps 1.0 version: 1.0"
        )

    IRISN4RAD_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_IRISN4RAD_001",
            provider="GES_DISC", 
            shortname="IRISN4RAD",
            version="001",
            description="IRIS/Nimbus-4 Level 1 Radiance Data V001 (IRISN4RAD) at GES DISC version: 001"
        )

    ITPRN5L1_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ITPRN5L1_001",
            provider="GES_DISC", 
            shortname="ITPRN5L1",
            version="001",
            description="ITPR/Nimbus-5 Level 1 Calibrated Radiances V001 (ITPRN5L1) at GES DISC version: 001"
        )

    SNDRJ1ATMSL1B_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDRJ1ATMSL1B_2",
            provider="GES_DISC", 
            shortname="SNDRJ1ATMSL1B",
            version="2",
            description="JPSS-1 ATMS Level 1B Brightness Temperature V2 (SNDRJ1ATMSL1B) at GES DISC version: 2"
        )

    SNDRJ1ATMSL1B_V3_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDRJ1ATMSL1B_3",
            provider="GES_DISC", 
            shortname="SNDRJ1ATMSL1B",
            version="3",
            description="JPSS-1 ATMS Level 1B Brightness Temperature V3 (SNDRJ1ATMSL1B) at GES DISC version: 3"
        )

    SNDRJ1CRISL1BIMG_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDRJ1CrISL1BIMG_2",
            provider="GES_DISC", 
            shortname="SNDRJ1CrISL1BIMG",
            version="2",
            description="JPSS-1 CrIS IMG: Collocated VIIRS level 1 / cloud mask statistical summary V2 (SNDRJ1CrISL1BIMG) at GES DISC version: 2"
        )

    SNDRJ1CRISL1BIMGC_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDRJ1CrISL1BIMGC_2",
            provider="GES_DISC", 
            shortname="SNDRJ1CrISL1BIMGC",
            version="2",
            description="JPSS-1 CrIS IMG_COL: Array indices for collocated VIIRS observations V2 (SNDRJ1CrISL1BIMGC) at GES DISC version: 2"
        )

    SNDRJ1CRISL1B_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDRJ1CrISL1B_2",
            provider="GES_DISC", 
            shortname="SNDRJ1CrISL1B",
            version="2",
            description="JPSS-1 CrIS Level 1B Full Spectral Resolution V2 (SNDRJ1CrISL1B) at GES DISC version: 2"
        )

    SNDRJ1CRISL1B_V3_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDRJ1CrISL1B_3",
            provider="GES_DISC", 
            shortname="SNDRJ1CrISL1B",
            version="3",
            description="JPSS-1 CrIS Level 1B Full Spectral Resolution V3 (SNDRJ1CrISL1B) at GES DISC version: 3"
        )

    SNDRJ1CRISL1BPCARED_V30_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDRJ1CrISL1BPCARED_3.0",
            provider="GES_DISC", 
            shortname="SNDRJ1CrISL1BPCARED",
            version="3.0",
            description="JPSS-1 CrIS Level 1B Principal Component Analysis / Rapid Event Detection V3.0 (SNDRJ1CrISL1BPCARED) at GES DISC version: 3.0"
        )

    SNDRJ2CRISL1BIMG_V30_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDRJ2CrISL1BIMG_3.0",
            provider="GES_DISC", 
            shortname="SNDRJ2CrISL1BIMG",
            version="3.0",
            description="JPSS-2 CrIS IMG: Collocated VIIRS level 1 / cloud mask statistical summary V3.0 (SNDRJ2CrISL1BIMG) at GES DISC version: 3.0"
        )

    SNDRJ2CRISL1BIMGC_V30_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDRJ2CrISL1BIMGC_3.0",
            provider="GES_DISC", 
            shortname="SNDRJ2CrISL1BIMGC",
            version="3.0",
            description="JPSS-2 CrIS IMG_COL: Array indices for collocated VIIRS observations V3.0 (SNDRJ2CrISL1BIMGC) at GES DISC version: 3.0"
        )

    SNDRJ2CRISL1B_V3_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDRJ2CrISL1B_3",
            provider="GES_DISC", 
            shortname="SNDRJ2CrISL1B",
            version="3",
            description="JPSS-2 CrIS Level 1B Beta Full Spectral Resolution V3 (SNDRJ2CrISL1B) at GES DISC version: 3"
        )

    J1_CRIS_VIIRS750M_IND_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_J1_CrIS_VIIRS750m_IND_1",
            provider="GES_DISC", 
            shortname="J1_CrIS_VIIRS750m_IND",
            version="1",
            description="JPSS1 CrIS-VIIRS 750-m Matchup Indexes V1 (J1_CrIS_VIIRS750m_IND) at GES_DISC version: 1"
        )

    RAIN_JAEGER_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_RAIN_JAEGER_1",
            provider="GES_DISC", 
            shortname="RAIN_JAEGER",
            version="1",
            description="Jaeger Monthly Mean Global Precipitation Climatology 2.5 x 5.0 degree V1 (RAIN_JEAGER) at GES DISC version: 1"
        )

    LANDMET_ANC_ST_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_LANDMET_ANC_ST_1",
            provider="GES_DISC", 
            shortname="LANDMET_ANC_ST",
            version="1",
            description="LANDMET Ancillary ISCCP Surface Type Data L3 V1 (LANDMET_ANC_ST) at GES DISC version: 1"
        )

    LANDMET_ANC_TESA_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_LANDMET_ANC_TESA_1",
            provider="GES_DISC", 
            shortname="LANDMET_ANC_TESA",
            version="1",
            description="LANDMET Ancillary Monthly Mean Effective and Spectral Albedo Data L3 V1 (LANDMET_ANC_TESA) at GES DISC version: 1"
        )

    LANDMET_ANC_TEIME_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_LANDMET_ANC_TEIME_1",
            provider="GES_DISC", 
            shortname="LANDMET_ANC_TEIME",
            version="1",
            description="LANDMET Ancillary Monthly Mean Thermal Effective Infrared and Microwave Emissivity Data L3 V1 (LANDMET_ANC_TEIME) at GES DISC version: 1"
        )

    LANDMET_ANC_SM_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_LANDMET_ANC_SM_1",
            provider="GES_DISC", 
            shortname="LANDMET_ANC_SM",
            version="1",
            description="LANDMET Ancillary Soil Moisture data L3 V1 (LANDMET_ANC_SM) at GES DISC version: 1"
        )

    LIMSN7L1PROFILER_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_LIMSN7L1PROFILER_001",
            provider="GES_DISC", 
            shortname="LIMSN7L1PROFILER",
            version="001",
            description="LIMS/Nimbus-7 Level 1 Profiles of Radiance Data V001 (LIMSN7L1PROFILER) at GES DISC version: 001"
        )

    LIMSN7L1RAT_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_LIMSN7L1RAT_001",
            provider="GES_DISC", 
            shortname="LIMSN7L1RAT",
            version="001",
            description="LIMS/Nimbus-7 Level 1 Radiance Data V001 (LIMSN7L1RAT) at GES DISC version: 001"
        )

    LIMSN7L2_V006_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_LIMSN7L2_006",
            provider="GES_DISC", 
            shortname="LIMSN7L2",
            version="006",
            description="LIMS/Nimbus-7 Level 2 Vertical Profiles of O3, NO2, H2O, HNO3, Geopotential Height, and Temperature V006 (LIMSN7L2) at GES DISC version: 006"
        )

    LIMSN7L3_V006_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_LIMSN7L3_006",
            provider="GES_DISC", 
            shortname="LIMSN7L3",
            version="006",
            description="LIMS/Nimbus-7 Level 3 Daily 2 deg Latitude Zonal Fourier Coefficients of O3, NO2, H2O, HNO3, Geopotential Height, and Temperature V006 (LIMSN7L3) at GES DISC version: 006"
        )

    LRIRN6L2IPAT_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_LRIRN6L2IPAT_001",
            provider="GES_DISC", 
            shortname="LRIRN6L2IPAT",
            version="001",
            description="LRIR/Nimbus-6 Level 2 Inverted Profiles of Temperature and Ozone V001 (LRIRN6L2IPAT) at GES DISC version: 001"
        )

    LANDMET_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_LANDMET_1",
            provider="GES_DISC", 
            shortname="LANDMET",
            version="1",
            description="Land Surface Atmospheric Boundary Interaction Product L3 V1(LANDMET) at GES DISC version: 1"
        )

    GPM_IMERG_LANDSEAMASK_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_IMERG_LandSeaMask_2",
            provider="GES_DISC", 
            shortname="GPM_IMERG_LandSeaMask",
            version="2",
            description="Land/Sea static mask relevant to IMERG precipitation 0.1x0.1 degree V2 (GPM_IMERG_LandSeaMask) at GES DISC version: 2"
        )

    TRMM_TMPA_LANDSEAMASK_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRMM_TMPA_LandSeaMask_2",
            provider="GES_DISC", 
            shortname="TRMM_TMPA_LandSeaMask",
            version="2",
            description="Land/Sea static mask relevant to TMPA precipitation 0.25x0.25 degree V2 (TRMM_TMPA_LandSeaMask) at GES DISC version: 2"
        )

    RAIN_LEGATES_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_RAIN_LEGATES_1",
            provider="GES_DISC", 
            shortname="RAIN_LEGATES",
            version="1",
            description="Legates Surface and Ship Observations of Precipitation Climatology 0.5 x 0.5 degree V1 (RAIN_LEGATES) at GES DISC version: 1"
        )

    GMAO_M2SCREAM_INST3_CHEM_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GMAO_M2SCREAM_INST3_CHEM_1",
            provider="GES_DISC", 
            shortname="GMAO_M2SCREAM_INST3_CHEM",
            version="1",
            description="M2-SCREAM: 3d,3-Hourly,Instantaneous,Model-Level,Assimilation,Assimilated Constituent Fields,Replayed MERRA-2 Meteorological Fields version: 1"
        )

    GMAO_M2SCREAM_MONTH_UNCERT_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GMAO_M2SCREAM_MONTH_UNCERT_1",
            provider="GES_DISC", 
            shortname="GMAO_M2SCREAM_MONTH_UNCERT",
            version="1",
            description="M2-SCREAM: Monthly,Model-Level,Assimilated Constituent Fields uncertainties version: 1"
        )

    M2_TMAX_PM25_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2_TMAX_PM25_1",
            provider="GES_DISC", 
            shortname="M2_TMAX_PM25",
            version="1",
            description="MERRA-2 avgM_2d_pm25_admin0, 2d, Single-Level, Country-Level Surface PM2.5 Monthly Mean Products V1 (M2_TMAX_PM25) at GES DISC version: 1"
        )

    M2C0NXASM_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2C0NXASM_5.12.4",
            provider="GES_DISC", 
            shortname="M2C0NXASM",
            version="5.12.4",
            description="MERRA-2 const_2d_asm_Nx: 2d, constants 0.625 x 0.5 degree V5.12.4 (M2C0NXASM) at GES DISC version: 5.12.4"
        )

    M2C0NXCTM_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2C0NXCTM_5.12.4",
            provider="GES_DISC", 
            shortname="M2C0NXCTM",
            version="5.12.4",
            description="MERRA-2 const_2d_ctm_Nx: Constant Model Parameters for Usage by CTM 0.625 x 0.5 degree V5.12.4 (M2C0NXCTM) at GES DISC version: 5.12.4"
        )

    M2C0NXLND_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2C0NXLND_5.12.4",
            provider="GES_DISC", 
            shortname="M2C0NXLND",
            version="5.12.4",
            description="MERRA-2 const_2d_lnd_Nx: 2d, constants Land Surface Diagnostics 0.625 x 0.5 degree V5.12.4 (M2C0NXLND) at GES DISC version: 5.12.4"
        )

    M2I1NXASM_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2I1NXASM_5.12.4",
            provider="GES_DISC", 
            shortname="M2I1NXASM",
            version="5.12.4",
            description="MERRA-2 inst1_2d_asm_Nx: 2d,1-Hourly,Instantaneous,Single-Level,Assimilation,Single-Level Diagnostics 0.625 x 0.5 degree V5.12.4 (M2I1NXASM) at GES DISC version: 5.12.4"
        )

    M2I1NXINT_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2I1NXINT_5.12.4",
            provider="GES_DISC", 
            shortname="M2I1NXINT",
            version="5.12.4",
            description="MERRA-2 inst1_2d_int_Nx: 2d,1-Hourly,Instantaneous,Single-Level,Assimilation,Vertically Integrated Diagnostics 0.625 x 0.5 degree V5.12.4 (M2I1NXINT) at GES DISC version: 5.12.4"
        )

    M2I1NXLFO_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2I1NXLFO_5.12.4",
            provider="GES_DISC", 
            shortname="M2I1NXLFO",
            version="5.12.4",
            description="MERRA-2 inst1_2d_lfo_Nx: 2d,1-Hourly,Instantaneous,Single-Level,Assimilation,Land Surface Forcings 0.625 x 0.5 degree V5.12.4 (M2I1NXLFO) at GES DISC version: 5.12.4"
        )

    M2I3NXGAS_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2I3NXGAS_5.12.4",
            provider="GES_DISC", 
            shortname="M2I3NXGAS",
            version="5.12.4",
            description="MERRA-2 inst3_2d_gas_Nx: 2d,3-Hourly,Instantaneous,Single-Level,Assimilation,Aerosol Optical Depth Analysis 0.625 x 0.5 degree V5.12.4 (M2I3NXGAS) at GES DISC version: 5.12.4"
        )

    M2I3NVAER_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2I3NVAER_5.12.4",
            provider="GES_DISC", 
            shortname="M2I3NVAER",
            version="5.12.4",
            description="MERRA-2 inst3_3d_aer_Nv: 3d,3-Hourly,Instantaneous,Model-Level,Assimilation,Aerosol Mixing Ratio 0.625 x 0.5 degree V5.12.4 (M2I3NVAER) at GES DISC version: 5.12.4"
        )

    M2I3NPASM_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2I3NPASM_5.12.4",
            provider="GES_DISC", 
            shortname="M2I3NPASM",
            version="5.12.4",
            description="MERRA-2 inst3_3d_asm_Np: 3d,3-Hourly,Instantaneous,Pressure-Level,Assimilation,Assimilated Meteorological Fields 0.625 x 0.5 degree V5.12.4 (M2I3NPASM) at GES DISC version: 5.12.4"
        )

    M2I3NVASM_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2I3NVASM_5.12.4",
            provider="GES_DISC", 
            shortname="M2I3NVASM",
            version="5.12.4",
            description="MERRA-2 inst3_3d_asm_Nv: 3d,3-Hourly,Instantaneous,Model-Level,Assimilation,Assimilated Meteorological Fields 0.625 x 0.5 degree V5.12.4 (M2I3NVASM) at GES DISC version: 5.12.4"
        )

    M2I3NVCHM_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2I3NVCHM_5.12.4",
            provider="GES_DISC", 
            shortname="M2I3NVCHM",
            version="5.12.4",
            description="MERRA-2 inst3_3d_chm_Nv: 3d,3-Hourly,Instantaneous,Model-Level,Assimilation,Carbon Monoxide and Ozone Mixing Ratio 0.625 x 0.5 degree V5.12.4 (M2I3NVCHM) at GES DISC version: 5.12.4"
        )

    M2I3NVGAS_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2I3NVGAS_5.12.4",
            provider="GES_DISC", 
            shortname="M2I3NVGAS",
            version="5.12.4",
            description="MERRA-2 inst3_3d_gas_Nv: 3d,3-Hourly,Instantaneous,Model-Level,Assimilation,Aerosol Mixing Ratio Analysis Increments 0.625 x 0.5 degree V5.12.4 (M2I3NVGAS) at GES DISC version: 5.12.4"
        )

    M2I6NPANA_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2I6NPANA_5.12.4",
            provider="GES_DISC", 
            shortname="M2I6NPANA",
            version="5.12.4",
            description="MERRA-2 inst6_3d_ana_Np: 3d,6-Hourly,Instantaneous,Pressure-Level,Analysis,Analyzed Meteorological Fields 0.625 x 0.5 degree V5.12.4 (M2I6NPANA) at GES DISC version: 5.12.4"
        )

    M2I6NVANA_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2I6NVANA_5.12.4",
            provider="GES_DISC", 
            shortname="M2I6NVANA",
            version="5.12.4",
            description="MERRA-2 inst6_3d_ana_Nv: 3d,6-Hourly,Instantaneous,Model-Level,Analysis,Analyzed Meteorological Fields 0.625 x 0.5 degree V5.12.4 (M2I6NVANA) at GES DISC version: 5.12.4"
        )

    M2IMNXASM_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2IMNXASM_5.12.4",
            provider="GES_DISC", 
            shortname="M2IMNXASM",
            version="5.12.4",
            description="MERRA-2 instM_2d_asm_Nx: 2d,Monthly mean,Single-Level,Assimilation,Single-Level Diagnostics 0.625 x 0.5 degree V5.12.4 (M2IMNXASM) at GES DISC version: 5.12.4"
        )

    M2IMNXGAS_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2IMNXGAS_5.12.4",
            provider="GES_DISC", 
            shortname="M2IMNXGAS",
            version="5.12.4",
            description="MERRA-2 instM_2d_gas_Nx: 2d,Monthly mean,Instantaneous,Single-Level,Assimilation,Aerosol Optical Depth Analysis 0.625 x 0.5 degree V5.12.4 (M2IMNXGAS) at GES DISC version: 5.12.4"
        )

    M2IMNXINT_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2IMNXINT_5.12.4",
            provider="GES_DISC", 
            shortname="M2IMNXINT",
            version="5.12.4",
            description="MERRA-2 instM_2d_int_Nx: 2d,Monthly mean,Instantaneous,Single-Level,Assimilation,Vertically Integrated Diagnostics 0.625 x 0.5 degree V5.12.4 (M2IMNXINT) at GES DISC version: 5.12.4"
        )

    M2IMNXLFO_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2IMNXLFO_5.12.4",
            provider="GES_DISC", 
            shortname="M2IMNXLFO",
            version="5.12.4",
            description="MERRA-2 instM_2d_lfo_Nx: 2d,Monthly mean,Instantaneous,Single-Level,Assimilation,Land Surface Forcings 0.625 x 0.5 degree V5.12.4 (M2IMNXLFO) at GES DISC version: 5.12.4"
        )

    M2IMNPANA_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2IMNPANA_5.12.4",
            provider="GES_DISC", 
            shortname="M2IMNPANA",
            version="5.12.4",
            description="MERRA-2 instM_3d_ana_Np: 3d,Monthly mean,Instantaneous,Pressure-Level,Analysis,Analyzed Meteorological Fields 0.625 x 0.5 degree V5.12.4 (M2IMNPANA) at GES DISC version: 5.12.4"
        )

    M2IMNPASM_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2IMNPASM_5.12.4",
            provider="GES_DISC", 
            shortname="M2IMNPASM",
            version="5.12.4",
            description="MERRA-2 instM_3d_asm_Np: 3d,Monthly mean,Instantaneous,Pressure-Level,Assimilation,Assimilated Meteorological Fields 0.625 x 0.5 degree V5.12.4 (M2IMNPASM) at GES DISC version: 5.12.4"
        )

    M2IUNXASM_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2IUNXASM_5.12.4",
            provider="GES_DISC", 
            shortname="M2IUNXASM",
            version="5.12.4",
            description="MERRA-2 instU_2d_asm_Nx: 2d,diurnal,Instantaneous,Single-Level,Assimilation,Single-Level Diagnostics 0.625 x 0.5 degree V5.12.4 (M2IUNXASM) at GES DISC version: 5.12.4"
        )

    M2IUNXGAS_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2IUNXGAS_5.12.4",
            provider="GES_DISC", 
            shortname="M2IUNXGAS",
            version="5.12.4",
            description="MERRA-2 instU_2d_gas_Nx: 2d,diurnal,Instantaneous,Single-Level,Assimilation,Aerosol Optical Depth Analysis 0.625 x 0.5 degree V5.12.4 (M2IUNXGAS) at GES DISC version: 5.12.4"
        )

    M2IUNXINT_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2IUNXINT_5.12.4",
            provider="GES_DISC", 
            shortname="M2IUNXINT",
            version="5.12.4",
            description="MERRA-2 instU_2d_int_Nx: 2d,diurnal,Instantaneous,Single-Level,Assimilation,Vertically Integrated Diagnostics 0.625 x 0.5 degree V5.12.4 (M2IUNXINT) at GES DISC version: 5.12.4"
        )

    M2IUNXLFO_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2IUNXLFO_5.12.4",
            provider="GES_DISC", 
            shortname="M2IUNXLFO",
            version="5.12.4",
            description="MERRA-2 instU_2d_lfo_Nx: 2d,diurnal,Instantaneous,Single-Level,Assimilation,Land Surface Forcings 0.625 x 0.5 degree V5.12.4 (M2IUNXLFO) at GES DISC version: 5.12.4"
        )

    M2IUNPANA_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2IUNPANA_5.12.4",
            provider="GES_DISC", 
            shortname="M2IUNPANA",
            version="5.12.4",
            description="MERRA-2 instU_3d_ana_Np: 3d,diurnal,Instantaneous,Pressure-Level,Analysis,Analyzed Meteorological Fields 0.625 x 0.5 degree V5.12.4 (M2IUNPANA) at GES DISC version: 5.12.4"
        )

    M2IUNPASM_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2IUNPASM_5.12.4",
            provider="GES_DISC", 
            shortname="M2IUNPASM",
            version="5.12.4",
            description="MERRA-2 instU_3d_asm_Np: 3d,diurnal,Instantaneous,Pressure-Level,Assimilation,Assimilated Meteorological Fields 0.625 x 0.5 degree V5.12.4 (M2IUNPASM) at GES DISC version: 5.12.4"
        )

    M2SDNXSLV_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2SDNXSLV_5.12.4",
            provider="GES_DISC", 
            shortname="M2SDNXSLV",
            version="5.12.4",
            description="MERRA-2 statD_2d_slv_Nx: 2d,Daily,Aggregated Statistics,Single-Level,Assimilation,Single-Level Diagnostics 0.625 x 0.5 degree V5.12.4 (M2SDNXSLV) at GES DISC version: 5.12.4"
        )

    M2SMNXEDI_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2SMNXEDI_1",
            provider="GES_DISC", 
            shortname="M2SMNXEDI",
            version="1",
            description="MERRA-2 statM_2d_edi_Nx: 2d, Single-Level, Monthly Extremes Detection Indices V1 (M2SMNXEDI) at GES DISC version: 1"
        )

    M2SMNXEDI_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2SMNXEDI_2",
            provider="GES_DISC", 
            shortname="M2SMNXEDI",
            version="2",
            description="MERRA-2 statM_2d_edi_Nx: 2d, Single-Level, Monthly Extremes Detection Indices based on 1991-2020 V2 (M2SMNXEDI) at GES DISC version: 2"
        )

    M2SMNXPCT_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2SMNXPCT_1",
            provider="GES_DISC", 
            shortname="M2SMNXPCT",
            version="1",
            description="MERRA-2 statM_2d_pct_Nx: 2d, Single-Level, Monthly Percentiles V1 (M2SMNXPCT) at GES DISC version: 1"
        )

    M2SMNXPCT_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2SMNXPCT_2",
            provider="GES_DISC", 
            shortname="M2SMNXPCT",
            version="2",
            description="MERRA-2 statM_2d_pct_Nx: 2d, Single-Level, Monthly Percentiles based on 1991-2020 V2 (M2SMNXPCT) at GES DISC version: 2"
        )

    M2SMNXSLV_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2SMNXSLV_5.12.4",
            provider="GES_DISC", 
            shortname="M2SMNXSLV",
            version="5.12.4",
            description="MERRA-2 statM_2d_slv_Nx: 2d,Monthly,Aggregated Statistics,Single-Level,Assimilation,Single-Level Diagnostics 0.625 x 0.5 degree V5.12.4 (M2SMNXSLV) at GES DISC version: 5.12.4"
        )

    M2T1NXADG_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2T1NXADG_5.12.4",
            provider="GES_DISC", 
            shortname="M2T1NXADG",
            version="5.12.4",
            description="MERRA-2 tavg1_2d_adg_Nx: 2d,1-Hourly,Time-averaged,Single-Level,Assimilation,Aerosol Diagnostics (extended) 0.625 x 0.5 degree V5.12.4 (M2T1NXADG) at GES DISC version: 5.12.4"
        )

    M2T1NXAER_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2T1NXAER_5.12.4",
            provider="GES_DISC", 
            shortname="M2T1NXAER",
            version="5.12.4",
            description="MERRA-2 tavg1_2d_aer_Nx: 2d,1-Hourly,Time-averaged,Single-Level,Assimilation,Aerosol Diagnostics 0.625 x 0.5 degree V5.12.4 (M2T1NXAER) at GES DISC version: 5.12.4"
        )

    M2T1NXCHM_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2T1NXCHM_5.12.4",
            provider="GES_DISC", 
            shortname="M2T1NXCHM",
            version="5.12.4",
            description="MERRA-2 tavg1_2d_chm_Nx: 2d,1-Hourly,Time-Averaged,Single-Level,Assimilation,Carbon Monoxide and Ozone Diagnostics 0.625 x 0.5 degree V5.12.4 (M2T1NXCHM) at GES DISC version: 5.12.4"
        )

    M2T1NXCSP_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2T1NXCSP_5.12.4",
            provider="GES_DISC", 
            shortname="M2T1NXCSP",
            version="5.12.4",
            description="MERRA-2 tavg1_2d_csp_Nx: 2d,1-Hourly,Time-averaged,Single-Level,Assimilation,COSP Satellite Simulator 0.625 x 0.5 degree V5.12.4 (M2T1NXCSP) at GES DISC version: 5.12.4"
        )

    M2T1NXFLX_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2T1NXFLX_5.12.4",
            provider="GES_DISC", 
            shortname="M2T1NXFLX",
            version="5.12.4",
            description="MERRA-2 tavg1_2d_flx_Nx: 2d,1-Hourly,Time-Averaged,Single-Level,Assimilation,Surface Flux Diagnostics 0.625 x 0.5 degree V5.12.4 (M2T1NXFLX) at GES DISC version: 5.12.4"
        )

    M2T1NXINT_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2T1NXINT_5.12.4",
            provider="GES_DISC", 
            shortname="M2T1NXINT",
            version="5.12.4",
            description="MERRA-2 tavg1_2d_int_Nx: 2d,1-Hourly,Time-Averaged,Single-Level,Assimilation,Vertically Integrated Diagnostics 0.625 x 0.5 degree V5.12.4 (M2T1NXINT) at GES DISC version: 5.12.4"
        )

    M2T1NXLFO_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2T1NXLFO_5.12.4",
            provider="GES_DISC", 
            shortname="M2T1NXLFO",
            version="5.12.4",
            description="MERRA-2 tavg1_2d_lfo_Nx: 2d,1-Hourly,Time-Averaged,Single-Level,Assimilation,Land Surface Forcings 0.625 x 0.5 degree V5.12.4 (M2T1NXLFO) at GES DISC version: 5.12.4"
        )

    M2T1NXLND_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2T1NXLND_5.12.4",
            provider="GES_DISC", 
            shortname="M2T1NXLND",
            version="5.12.4",
            description="MERRA-2 tavg1_2d_lnd_Nx: 2d,1-Hourly,Time-Averaged,Single-Level,Assimilation,Land Surface Diagnostics 0.625 x 0.5 degree V5.12.4 (M2T1NXLND) at GES DISC version: 5.12.4"
        )

    M2T1NXOCN_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2T1NXOCN_5.12.4",
            provider="GES_DISC", 
            shortname="M2T1NXOCN",
            version="5.12.4",
            description="MERRA-2 tavg1_2d_ocn_Nx: 2d,1-Hourly,Time-Averaged,Single-Level,Assimilation,Ocean Surface Diagnostics 0.625 x 0.5 degree V5.12.4 (M2T1NXOCN) at GES DISC version: 5.12.4"
        )

    M2T1NXRAD_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2T1NXRAD_5.12.4",
            provider="GES_DISC", 
            shortname="M2T1NXRAD",
            version="5.12.4",
            description="MERRA-2 tavg1_2d_rad_Nx: 2d,1-Hourly,Time-Averaged,Single-Level,Assimilation,Radiation Diagnostics 0.625 x 0.5 degree V5.12.4 (M2T1NXRAD) at GES DISC version: 5.12.4"
        )

    M2T1NXSLV_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2T1NXSLV_5.12.4",
            provider="GES_DISC", 
            shortname="M2T1NXSLV",
            version="5.12.4",
            description="MERRA-2 tavg1_2d_slv_Nx: 2d,1-Hourly,Time-Averaged,Single-Level,Assimilation,Single-Level Diagnostics 0.625 x 0.5 degree V5.12.4 (M2T1NXSLV) at GES DISC version: 5.12.4"
        )

    M2T3NXGLC_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2T3NXGLC_5.12.4",
            provider="GES_DISC", 
            shortname="M2T3NXGLC",
            version="5.12.4",
            description="MERRA-2 tavg3_2d_glc_Nx: 2d,3-Hourly,Time-Averaged,Single-Level,Assimilation,Land Ice Surface Diagnostics 0.625 x 0.5 degree V5.12.4 (M2T3NXGLC) at GES DISC version: 5.12.4"
        )

    M2T3NVASM_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2T3NVASM_5.12.4",
            provider="GES_DISC", 
            shortname="M2T3NVASM",
            version="5.12.4",
            description="MERRA-2 tavg3_3d_asm_Nv: 3d,3-Hourly,Time-Averaged,Model-Level,Assimilation,Assimilated Meteorological Fields 0.625 x 0.5 degree V5.12.4 (M2T3NVASM) at GES DISC version: 5.12.4"
        )

    M2T3NPCLD_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2T3NPCLD_5.12.4",
            provider="GES_DISC", 
            shortname="M2T3NPCLD",
            version="5.12.4",
            description="MERRA-2 tavg3_3d_cld_Np: 3d,3-Hourly,Time-Averaged,Pressure-Level,Assimilation,Cloud Diagnostics 0.625 x 0.5 degree V5.12.4 (M2T3NPCLD) at GES DISC version: 5.12.4"
        )

    M2T3NVCLD_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2T3NVCLD_5.12.4",
            provider="GES_DISC", 
            shortname="M2T3NVCLD",
            version="5.12.4",
            description="MERRA-2 tavg3_3d_cld_Nv: 3d,3-Hourly,Time-Averaged,Model-Level,Assimilation,Cloud Diagnostics 0.625 x 0.5 degree V5.12.4 (M2T3NVCLD) at GES DISC version: 5.12.4"
        )

    M2T3NEMST_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2T3NEMST_5.12.4",
            provider="GES_DISC", 
            shortname="M2T3NEMST",
            version="5.12.4",
            description="MERRA-2 tavg3_3d_mst_Ne: 3d,3-Hourly,Time-Averaged,Model-Level Edge,Assimilation,Moist Processes Diagnostics 0.625 x 0.5 degree V5.12.4 (M2T3NEMST) at GES DISC version: 5.12.4"
        )

    M2T3NPMST_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2T3NPMST_5.12.4",
            provider="GES_DISC", 
            shortname="M2T3NPMST",
            version="5.12.4",
            description="MERRA-2 tavg3_3d_mst_Np: 3d,3-Hourly,Time-Averaged,Pressure-Level,Assimilation,Moist Processes Diagnostics 0.625 x 0.5 degree V5.12.4 (M2T3NPMST) at GES DISC version: 5.12.4"
        )

    M2T3NVMST_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2T3NVMST_5.12.4",
            provider="GES_DISC", 
            shortname="M2T3NVMST",
            version="5.12.4",
            description="MERRA-2 tavg3_3d_mst_Nv: 3d,3-Hourly,Time-Averaged,Model-Level,Assimilation,Moist Processes Diagnostics 0.625 x 0.5 degree V5.12.4 (M2T3NVMST) at GES DISC version: 5.12.4"
        )

    M2T3NENAV_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2T3NENAV_5.12.4",
            provider="GES_DISC", 
            shortname="M2T3NENAV",
            version="5.12.4",
            description="MERRA-2 tavg3_3d_nav_Ne: 3d,3-Hourly,Time-Averaged, Vertical Coordinates 0.625 x 0.5 degree V5.12.4 (M2T3NENAV) at GES DISC version: 5.12.4"
        )

    M2T3NPODT_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2T3NPODT_5.12.4",
            provider="GES_DISC", 
            shortname="M2T3NPODT",
            version="5.12.4",
            description="MERRA-2 tavg3_3d_odt_Np: 3d,3-Hourly,Time-Averaged,Pressure-Level,Assimilation,Ozone Tendencies 0.625 x 0.5 degree V5.12.4 (M2T3NPODT) at GES DISC version: 5.12.4"
        )

    M2T3NPQDT_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2T3NPQDT_5.12.4",
            provider="GES_DISC", 
            shortname="M2T3NPQDT",
            version="5.12.4",
            description="MERRA-2 tavg3_3d_qdt_Np: 3d,3-Hourly,Time-Averaged,Pressure-Level,Assimilation,Moist Tendencies 0.625 x 0.5 degree V5.12.4 (M2T3NPQDT) at GES DISC version: 5.12.4"
        )

    M2T3NPRAD_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2T3NPRAD_5.12.4",
            provider="GES_DISC", 
            shortname="M2T3NPRAD",
            version="5.12.4",
            description="MERRA-2 tavg3_3d_rad_Np: 3d,3-Hourly,Time-Averaged,Pressure-Level,Assimilation,Radiation Diagnostics 0.625 x 0.5 degree V5.12.4 (M2T3NPRAD) at GES DISC version: 5.12.4"
        )

    M2T3NVRAD_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2T3NVRAD_5.12.4",
            provider="GES_DISC", 
            shortname="M2T3NVRAD",
            version="5.12.4",
            description="MERRA-2 tavg3_3d_rad_Nv: 3d,3-Hourly,Time-Averaged,Model-Level,Assimilation,Radiation Diagnostics 0.625 x 0.5 degree V5.12.4 (M2T3NVRAD) at GES DISC version: 5.12.4"
        )

    M2T3NPTDT_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2T3NPTDT_5.12.4",
            provider="GES_DISC", 
            shortname="M2T3NPTDT",
            version="5.12.4",
            description="MERRA-2 tavg3_3d_tdt_Np: 3d,3-Hourly,Time-Averaged,Pressure-Level,Assimilation,Temperature Tendencies 0.625 x 0.5 degree V5.12.4 (M2T3NPTDT) at GES DISC version: 5.12.4"
        )

    M2T3NETRB_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2T3NETRB_5.12.4",
            provider="GES_DISC", 
            shortname="M2T3NETRB",
            version="5.12.4",
            description="MERRA-2 tavg3_3d_trb_Ne: 3d,3-Hourly,Time-Averaged,Model-Level Edge,Assimilation,Turbulence Diagnostics 0.625 x 0.5 degree V5.12.4 (M2T3NETRB) at GES DISC version: 5.12.4"
        )

    M2T3NPTRB_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2T3NPTRB_5.12.4",
            provider="GES_DISC", 
            shortname="M2T3NPTRB",
            version="5.12.4",
            description="MERRA-2 tavg3_3d_trb_Np: 3d,3-Hourly,Time-Averaged,Pressure-Level,Assimilation,Turbulence Diagnostics 0.625 x 0.5 degree V5.12.4 (M2T3NPTRB) at GES DISC version: 5.12.4"
        )

    M2T3NPUDT_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2T3NPUDT_5.12.4",
            provider="GES_DISC", 
            shortname="M2T3NPUDT",
            version="5.12.4",
            description="MERRA-2 tavg3_3d_udt_Np: 3d,3-Hourly,Time-Averaged,Pressure-Level,Assimilation,Wind Tendencies 0.625 x 0.5 degree V5.12.4 (M2T3NPUDT) at GES DISC version: 5.12.4"
        )

    M2TCNXLTM_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2TCNXLTM_1",
            provider="GES_DISC", 
            shortname="M2TCNXLTM",
            version="1",
            description="MERRA-2 tavgC_2d_ltm_Nx: 2d, Single-Level, Long Term Mean Diagnostics V1 (M2TCNXLTM) at GES DISC version: 1"
        )

    M2TCNXLTM_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2TCNXLTM_2",
            provider="GES_DISC", 
            shortname="M2TCNXLTM",
            version="2",
            description="MERRA-2 tavgC_2d_ltm_Nx: 2d, Single-Level, Long Term Mean Diagnostics based on 1991-2020 V2 (M2TCNXLTM) at GES DISC version: 2"
        )

    M2TCNPLTM_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2TCNPLTM_1",
            provider="GES_DISC", 
            shortname="M2TCNPLTM",
            version="1",
            description="MERRA-2 tavgC_3d_ltm_Np: 3d, Long Term Mean 3-Dimensional Meteorological Fields V1 (M2TCNPLTM) at GES DISC version: 1"
        )

    M2TCNPLTM_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2TCNPLTM_2",
            provider="GES_DISC", 
            shortname="M2TCNPLTM",
            version="2",
            description="MERRA-2 tavgC_3d_ltm_Np: 3d, Long Term Mean 3-Dimensional Meteorological Fields based on 1991-2020 V2 (M2TCNPLTM) at GES DISC version: 2"
        )

    M2TMNXADG_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2TMNXADG_5.12.4",
            provider="GES_DISC", 
            shortname="M2TMNXADG",
            version="5.12.4",
            description="MERRA-2 tavgM_2d_adg_Nx: 2d,Monthly mean,Time-averaged,Single-Level,Assimilation,Aerosol Diagnostics (extended) 0.625 x 0.5 degree V5.12.4 (M2TMNXADG) at GES DISC version: 5.12.4"
        )

    M2TMNXAER_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2TMNXAER_5.12.4",
            provider="GES_DISC", 
            shortname="M2TMNXAER",
            version="5.12.4",
            description="MERRA-2 tavgM_2d_aer_Nx: 2d,Monthly mean,Time-averaged,Single-Level,Assimilation,Aerosol Diagnostics 0.625 x 0.5 degree V5.12.4 (M2TMNXAER) at GES DISC version: 5.12.4"
        )

    M2TMNXCHM_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2TMNXCHM_5.12.4",
            provider="GES_DISC", 
            shortname="M2TMNXCHM",
            version="5.12.4",
            description="MERRA-2 tavgM_2d_chm_Nx: 2d,Monthly mean,Time-Averaged,Single-Level,Assimilation,Carbon Monoxide and Ozone Diagnostics 0.625 x 0.5 degree V5.12.4 (M2TMNXCHM) at GES DISC version: 5.12.4"
        )

    M2TMNXCSP_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2TMNXCSP_5.12.4",
            provider="GES_DISC", 
            shortname="M2TMNXCSP",
            version="5.12.4",
            description="MERRA-2 tavgM_2d_csp_Nx: 2d,Monthly mean,Time-averaged,Single-Level,Assimilation,COSP Satellite Simulator 0.625 x 0.5 degree V5.12.4 (M2TMNXCSP) at GES DISC version: 5.12.4"
        )

    M2TMNXFLX_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2TMNXFLX_5.12.4",
            provider="GES_DISC", 
            shortname="M2TMNXFLX",
            version="5.12.4",
            description="MERRA-2 tavgM_2d_flx_Nx: 2d,Monthly mean,Time-Averaged,Single-Level,Assimilation,Surface Flux Diagnostics 0.625 x 0.5 degree V5.12.4 (M2TMNXFLX) at GES DISC version: 5.12.4"
        )

    M2TMNXGLC_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2TMNXGLC_5.12.4",
            provider="GES_DISC", 
            shortname="M2TMNXGLC",
            version="5.12.4",
            description="MERRA-2 tavgM_2d_glc_Nx: 2d,Monthly mean,Time-Averaged,Single-Level,Assimilation,Land Ice Surface Diagnostics 0.625 x 0.5 degree V5.12.4 (M2TMNXGLC) at GES DISC version: 5.12.4"
        )

    M2TMNXINT_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2TMNXINT_5.12.4",
            provider="GES_DISC", 
            shortname="M2TMNXINT",
            version="5.12.4",
            description="MERRA-2 tavgM_2d_int_Nx: 2d,Monthly mean,Time-Averaged,Single-Level,Assimilation,Vertically Integrated Diagnostics 0.625 x 0.5 degree V5.12.4 (M2TMNXINT) at GES DISC version: 5.12.4"
        )

    M2TMNXLFO_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2TMNXLFO_5.12.4",
            provider="GES_DISC", 
            shortname="M2TMNXLFO",
            version="5.12.4",
            description="MERRA-2 tavgM_2d_lfo_Nx: 2d,Monthly mean,Time-Averaged,Single-Level,Assimilation,Land Surface Forcings 0.625 x 0.5 degree V5.12.4 (M2TMNXLFO) at GES DISC version: 5.12.4"
        )

    M2TMNXLND_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2TMNXLND_5.12.4",
            provider="GES_DISC", 
            shortname="M2TMNXLND",
            version="5.12.4",
            description="MERRA-2 tavgM_2d_lnd_Nx: 2d,Monthly mean,Time-Averaged,Single-Level,Assimilation,Land Surface Diagnostics 0.625 x 0.5 degree V5.12.4 (M2TMNXLND) at GES DISC version: 5.12.4"
        )

    M2TMNXOCN_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2TMNXOCN_5.12.4",
            provider="GES_DISC", 
            shortname="M2TMNXOCN",
            version="5.12.4",
            description="MERRA-2 tavgM_2d_ocn_Nx: 2d,Monthly mean,Time-Averaged,Single-Level,Assimilation,Ocean Surface Diagnostics 0.625 x 0.5 degree V5.12.4 (M2TMNXOCN) at GES DISC version: 5.12.4"
        )

    M2TMNXRAD_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2TMNXRAD_5.12.4",
            provider="GES_DISC", 
            shortname="M2TMNXRAD",
            version="5.12.4",
            description="MERRA-2 tavgM_2d_rad_Nx: 2d,Monthly mean,Time-Averaged,Single-Level,Assimilation,Radiation Diagnostics 0.625 x 0.5 degree V5.12.4 (M2TMNXRAD) at GES DISC version: 5.12.4"
        )

    M2TMNXSLV_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2TMNXSLV_5.12.4",
            provider="GES_DISC", 
            shortname="M2TMNXSLV",
            version="5.12.4",
            description="MERRA-2 tavgM_2d_slv_Nx: 2d,Monthly mean,Time-Averaged,Single-Level,Assimilation,Single-Level Diagnostics 0.625 x 0.5 degree V5.12.4 (M2TMNXSLV) at GES DISC version: 5.12.4"
        )

    M2TMNPCLD_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2TMNPCLD_5.12.4",
            provider="GES_DISC", 
            shortname="M2TMNPCLD",
            version="5.12.4",
            description="MERRA-2 tavgM_3d_cld_Np: 3d,Monthly mean,Time-Averaged,Pressure-Level,Assimilation,Cloud Diagnostics 0.625 x 0.5 degree V5.12.4 (M2TMNPCLD) at GES DISC version: 5.12.4"
        )

    M2TMNPMST_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2TMNPMST_5.12.4",
            provider="GES_DISC", 
            shortname="M2TMNPMST",
            version="5.12.4",
            description="MERRA-2 tavgM_3d_mst_Np: 3d,Monthly mean,Time-Averaged,Pressure-Level,Assimilation,Moist Processes Diagnostics 0.625 x 0.5 degree V5.12.4 (M2TMNPMST) at GES DISC version: 5.12.4"
        )

    M2TMNPODT_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2TMNPODT_5.12.4",
            provider="GES_DISC", 
            shortname="M2TMNPODT",
            version="5.12.4",
            description="MERRA-2 tavgM_3d_odt_Np: 3d,Monthly mean,Time-Averaged,Pressure-Level,Assimilation,Ozone Tendencies 0.625 x 0.5 degree V5.12.4 (M2TMNPODT) at GES DISC version: 5.12.4"
        )

    M2TMNPQDT_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2TMNPQDT_5.12.4",
            provider="GES_DISC", 
            shortname="M2TMNPQDT",
            version="5.12.4",
            description="MERRA-2 tavgM_3d_qdt_Np: 3d,Monthly mean,Time-Averaged,Pressure-Level,Assimilation,Moist Tendencies 0.625 x 0.5 degree V5.12.4 (M2TMNPQDT) at GES DISC version: 5.12.4"
        )

    M2TMNPRAD_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2TMNPRAD_5.12.4",
            provider="GES_DISC", 
            shortname="M2TMNPRAD",
            version="5.12.4",
            description="MERRA-2 tavgM_3d_rad_Np: 3d,Monthly mean,Time-Averaged,Pressure-Level,Assimilation,Radiation Diagnostics 0.625 x 0.5 degree V5.12.4 (M2TMNPRAD) at GES DISC version: 5.12.4"
        )

    M2TMNPTDT_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2TMNPTDT_5.12.4",
            provider="GES_DISC", 
            shortname="M2TMNPTDT",
            version="5.12.4",
            description="MERRA-2 tavgM_3d_tdt_Np: 3d,Monthly mean,Time-Averaged,Pressure-Level,Assimilation,Temperature Tendencies 0.625 x 0.5 degree V5.12.4 (M2TMNPTDT) at GES DISC version: 5.12.4"
        )

    M2TMNPTRB_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2TMNPTRB_5.12.4",
            provider="GES_DISC", 
            shortname="M2TMNPTRB",
            version="5.12.4",
            description="MERRA-2 tavgM_3d_trb_Np: 3d,Monthly mean,Time-Averaged,Pressure-Level,Assimilation,Turbulence Diagnostics 0.625 x 0.5 degree V5.12.4 (M2TMNPTRB) at GES DISC version: 5.12.4"
        )

    M2TMNPUDT_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2TMNPUDT_5.12.4",
            provider="GES_DISC", 
            shortname="M2TMNPUDT",
            version="5.12.4",
            description="MERRA-2 tavgM_3d_udt_Np: 3d,Monthly mean,Time-Averaged,Pressure-Level,Assimilation,Wind Tendencies 0.625 x 0.5 degree V5.12.4 (M2TMNPUDT) at GES DISC version: 5.12.4"
        )

    M2TUNXADG_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2TUNXADG_5.12.4",
            provider="GES_DISC", 
            shortname="M2TUNXADG",
            version="5.12.4",
            description="MERRA-2 tavgU_2d_adg_Nx: 2d,diurnal,Time-averaged,Single-Level,Assimilation,Aerosol Diagnostics (extended) 0.625 x 0.5 degree V5.12.4 (M2TUNXADG) at GES DISC version: 5.12.4"
        )

    M2TUNXAER_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2TUNXAER_5.12.4",
            provider="GES_DISC", 
            shortname="M2TUNXAER",
            version="5.12.4",
            description="MERRA-2 tavgU_2d_aer_Nx: 2d,diurnal,Time-averaged,Single-Level,Assimilation,Aerosol Diagnostics 0.625 x 0.5 degree V5.12.4 (M2TUNXAER) at GES DISC version: 5.12.4"
        )

    M2TUNXCHM_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2TUNXCHM_5.12.4",
            provider="GES_DISC", 
            shortname="M2TUNXCHM",
            version="5.12.4",
            description="MERRA-2 tavgU_2d_chm_Nx: 2d,diurnal,Time-Averaged,Single-Level,Assimilation,Carbon Monoxide and Ozone Diagnostics 0.625 x 0.5 degree V5.12.4 (M2TUNXCHM) at GES DISC version: 5.12.4"
        )

    M2TUNXCSP_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2TUNXCSP_5.12.4",
            provider="GES_DISC", 
            shortname="M2TUNXCSP",
            version="5.12.4",
            description="MERRA-2 tavgU_2d_csp_Nx: 2d,diurnal,Time-averaged,Single-Level,Assimilation,COSP Satellite Simulator 0.625 x 0.5 degree V5.12.4 (M2TUNXCSP) at GES DISC version: 5.12.4"
        )

    M2TUNXFLX_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2TUNXFLX_5.12.4",
            provider="GES_DISC", 
            shortname="M2TUNXFLX",
            version="5.12.4",
            description="MERRA-2 tavgU_2d_flx_Nx: 2d,diurnal,Time-Averaged,Single-Level,Assimilation,Surface Flux Diagnostics 0.625 x 0.5 degree V5.12.4 (M2TUNXFLX) at GES DISC version: 5.12.4"
        )

    M2TUNXGLC_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2TUNXGLC_5.12.4",
            provider="GES_DISC", 
            shortname="M2TUNXGLC",
            version="5.12.4",
            description="MERRA-2 tavgU_2d_glc_Nx: 2d,diurnal,Time-Averaged,Single-Level,Assimilation,Land Ice Surface Diagnostics 0.625 x 0.5 degree V5.12.4 (M2TUNXGLC) at GES DISC version: 5.12.4"
        )

    M2TUNXINT_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2TUNXINT_5.12.4",
            provider="GES_DISC", 
            shortname="M2TUNXINT",
            version="5.12.4",
            description="MERRA-2 tavgU_2d_int_Nx: 2d,diurnal,Time-Averaged,Single-Level,Assimilation,Vertically Integrated Diagnostics 0.625 x 0.5 degree V5.12.4 (M2TUNXINT) at GES DISC version: 5.12.4"
        )

    M2TUNXLFO_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2TUNXLFO_5.12.4",
            provider="GES_DISC", 
            shortname="M2TUNXLFO",
            version="5.12.4",
            description="MERRA-2 tavgU_2d_lfo_Nx: 2d,diurnal,Time-Averaged,Single-Level,Assimilation,Land Surface Forcings 0.625 x 0.5 degree V5.12.4 (M2TUNXLFO) at GES DISC version: 5.12.4"
        )

    M2TUNXLND_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2TUNXLND_5.12.4",
            provider="GES_DISC", 
            shortname="M2TUNXLND",
            version="5.12.4",
            description="MERRA-2 tavgU_2d_lnd_Nx: 2d,diurnal,Time-Averaged,Single-Level,Assimilation,Land Surface Diagnostics 0.625 x 0.5 degree V5.12.4 (M2TUNXLND) at GES DISC version: 5.12.4"
        )

    M2TUNXOCN_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2TUNXOCN_5.12.4",
            provider="GES_DISC", 
            shortname="M2TUNXOCN",
            version="5.12.4",
            description="MERRA-2 tavgU_2d_ocn_Nx: 2d,diurnal,Time-Averaged,Single-Level,Assimilation,Ocean Surface Diagnostics 0.625 x 0.5 degree V5.12.4 (M2TUNXOCN) at GES DISC version: 5.12.4"
        )

    M2TUNXRAD_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2TUNXRAD_5.12.4",
            provider="GES_DISC", 
            shortname="M2TUNXRAD",
            version="5.12.4",
            description="MERRA-2 tavgU_2d_rad_Nx: 2d,diurnal,Time-Averaged,Single-Level,Assimilation,Radiation Diagnostics 0.625 x 0.5 degree V5.12.4 (M2TUNXRAD) at GES DISC version: 5.12.4"
        )

    M2TUNXSLV_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2TUNXSLV_5.12.4",
            provider="GES_DISC", 
            shortname="M2TUNXSLV",
            version="5.12.4",
            description="MERRA-2 tavgU_2d_slv_Nx: 2d,diurnal,Time-Averaged,Single-Level,Assimilation,Single-Level Diagnostics 0.625 x 0.5 degree V5.12.4 (M2TUNXSLV) at GES DISC version: 5.12.4"
        )

    M2TUNPCLD_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2TUNPCLD_5.12.4",
            provider="GES_DISC", 
            shortname="M2TUNPCLD",
            version="5.12.4",
            description="MERRA-2 tavgU_3d_cld_Np: 3d,diurnal,Time-Averaged,Pressure-Level,Assimilation,Cloud Diagnostics 0.625 x 0.5 degree V5.12.4 (M2TUNPCLD) at GES DISC version: 5.12.4"
        )

    M2TUNPMST_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2TUNPMST_5.12.4",
            provider="GES_DISC", 
            shortname="M2TUNPMST",
            version="5.12.4",
            description="MERRA-2 tavgU_3d_mst_Np: 3d,diurnal,Time-Averaged,Pressure-Level,Assimilation,Moist Processes Diagnostics 0.625 x 0.5 degree V5.12.4 (M2TUNPMST) at GES DISC version: 5.12.4"
        )

    M2TUNPODT_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2TUNPODT_5.12.4",
            provider="GES_DISC", 
            shortname="M2TUNPODT",
            version="5.12.4",
            description="MERRA-2 tavgU_3d_odt_Np: 3d,diurnal,Time-Averaged,Pressure-Level,Assimilation,Ozone Tendencies 0.625 x 0.5 degree V5.12.4 (M2TUNPODT) at GES DISC version: 5.12.4"
        )

    M2TUNPQDT_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2TUNPQDT_5.12.4",
            provider="GES_DISC", 
            shortname="M2TUNPQDT",
            version="5.12.4",
            description="MERRA-2 tavgU_3d_qdt_Np: 3d,diurnal,Time-Averaged,Pressure-Level,Assimilation,Moist Tendencies 0.625 x 0.5 degree V5.12.4 (M2TUNPQDT) at GES DISC version: 5.12.4"
        )

    M2TUNPRAD_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2TUNPRAD_5.12.4",
            provider="GES_DISC", 
            shortname="M2TUNPRAD",
            version="5.12.4",
            description="MERRA-2 tavgU_3d_rad_Np: 3d,diurnal,Time-Averaged,Pressure-Level,Assimilation,Radiation Diagnostics 0.625 x 0.5 degree V5.12.4 (M2TUNPRAD) at GES DISC version: 5.12.4"
        )

    M2TUNPTDT_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2TUNPTDT_5.12.4",
            provider="GES_DISC", 
            shortname="M2TUNPTDT",
            version="5.12.4",
            description="MERRA-2 tavgU_3d_tdt_Np: 3d,diurnal,Time-Averaged,Pressure-Level,Assimilation,Temperature Tendencies 0.625 x 0.5 degree V5.12.4 (M2TUNPTDT) at GES DISC version: 5.12.4"
        )

    M2TUNPTRB_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2TUNPTRB_5.12.4",
            provider="GES_DISC", 
            shortname="M2TUNPTRB",
            version="5.12.4",
            description="MERRA-2 tavgU_3d_trb_Np: 3d,diurnal,Time-Averaged,Pressure-Level,Assimilation,Turbulence Diagnostics 0.625 x 0.5 degree V5.12.4 (M2TUNPTRB) at GES DISC version: 5.12.4"
        )

    M2TUNPUDT_V5124_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_M2TUNPUDT_5.12.4",
            provider="GES_DISC", 
            shortname="M2TUNPUDT",
            version="5.12.4",
            description="MERRA-2 tavgU_3d_udt_Np: 3d,diurnal,Time-Averaged,Pressure-Level,Assimilation,Wind Tendencies 0.625 x 0.5 degree V5.12.4 (M2TUNPUDT) at GES DISC version: 5.12.4"
        )

    MERRA2_CNN_HAQAST_PM25_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_MERRA2_CNN_HAQAST_PM25_1",
            provider="GES_DISC", 
            shortname="MERRA2_CNN_HAQAST_PM25",
            version="1",
            description="MERRA2_CNN_HAQAST bias corrected global hourly surface total PM2.5 mass concentration, V1 (MERRA2_CNN_HAQAST_PM25) at GES DISC version: 1"
        )

    ML3DZMBRO_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3DZMBRO_005",
            provider="GES_DISC", 
            shortname="ML3DZMBRO",
            version="005",
            description="MLS/Aura (pre-average radiances) Level 3 Bromine Monoxide (BrO) Daily 10deg Lat Zonal Mean V005 (ML3DZMBRO) at GES DISC version: 005"
        )

    ML3DZMHO2_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3DZMHO2_005",
            provider="GES_DISC", 
            shortname="ML3DZMHO2",
            version="005",
            description="MLS/Aura (pre-average radiances) Level 3 Hydroperoxy Radical (HO2) Daily 10deg Lat Zonal Mean V005 (ML3DZMHO2) at GES DISC version: 005"
        )

    ML1OA_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML1OA_004",
            provider="GES_DISC", 
            shortname="ML1OA",
            version="004",
            description="MLS/Aura L1 Orbit/Attitude and Tangent Point Geolocation Data V004 (ML1OA) at GES DISC version: 004"
        )

    ML1OA_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML1OA_005",
            provider="GES_DISC", 
            shortname="ML1OA",
            version="005",
            description="MLS/Aura L1 Orbit/Attitude and Tangent Point Geolocation Data V005 (ML1OA) at GES DISC version: 005"
        )

    ML1RADD_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML1RADD_004",
            provider="GES_DISC", 
            shortname="ML1RADD",
            version="004",
            description="MLS/Aura L1 Radiances from Digital Autocorrelators V004 (ML1RADD) at GES DISC version: 004"
        )

    ML1RADD_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML1RADD_005",
            provider="GES_DISC", 
            shortname="ML1RADD",
            version="005",
            description="MLS/Aura L1 Radiances from Digital Autocorrelators V005 (ML1RADD) at GES DISC version: 005"
        )

    ML1RADG_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML1RADG_004",
            provider="GES_DISC", 
            shortname="ML1RADG",
            version="004",
            description="MLS/Aura L1 Radiances from Filter Banks for GHz V004 (ML1RADG) at GES DISC version: 004"
        )

    ML1RADG_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML1RADG_005",
            provider="GES_DISC", 
            shortname="ML1RADG",
            version="005",
            description="MLS/Aura L1 Radiances from Filter Banks for GHz V005 (ML1RADG) at GES DISC version: 005"
        )

    ML1RADT_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML1RADT_004",
            provider="GES_DISC", 
            shortname="ML1RADT",
            version="004",
            description="MLS/Aura L1 Radiances from Filter Banks for THz V004 (ML1RADT) at GES DISC version: 004"
        )

    ML1RADT_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML1RADT_005",
            provider="GES_DISC", 
            shortname="ML1RADT",
            version="005",
            description="MLS/Aura L1 Radiances from Filter Banks for THz V005 (ML1RADT) at GES DISC version: 005"
        )

    ML2BRO_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML2BRO_004",
            provider="GES_DISC", 
            shortname="ML2BRO",
            version="004",
            description="MLS/Aura Level 2 Bromine Monoxide (BrO) Mixing Ratio V004 (ML2BRO) at GES DISC version: 004"
        )

    ML2BRO_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML2BRO_005",
            provider="GES_DISC", 
            shortname="ML2BRO",
            version="005",
            description="MLS/Aura Level 2 Bromine Monoxide (BrO) Mixing Ratio V005 (ML2BRO) at GES DISC version: 005"
        )

    ML2CO_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML2CO_004",
            provider="GES_DISC", 
            shortname="ML2CO",
            version="004",
            description="MLS/Aura Level 2 Carbon Monoxide (CO) Mixing Ratio V004 (ML2CO) at GES DISC version: 004"
        )

    ML2CO_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML2CO_005",
            provider="GES_DISC", 
            shortname="ML2CO",
            version="005",
            description="MLS/Aura Level 2 Carbon Monoxide (CO) Mixing Ratio V005 (ML2CO) at GES DISC version: 005"
        )

    ML2CLO_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML2CLO_004",
            provider="GES_DISC", 
            shortname="ML2CLO",
            version="004",
            description="MLS/Aura Level 2 Chlorine Monoxide (ClO) Mixing Ratio V004 (ML2CLO) at GES DISC version: 004"
        )

    ML2CLO_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML2CLO_005",
            provider="GES_DISC", 
            shortname="ML2CLO",
            version="005",
            description="MLS/Aura Level 2 Chlorine Monoxide (ClO) Mixing Ratio V005 (ML2CLO) at GES DISC version: 005"
        )

    ML2IWC_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML2IWC_004",
            provider="GES_DISC", 
            shortname="ML2IWC",
            version="004",
            description="MLS/Aura Level 2 Cloud Ice Product V004 (ML2IWC) at GES DISC version: 004"
        )

    ML2IWC_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML2IWC_005",
            provider="GES_DISC", 
            shortname="ML2IWC",
            version="005",
            description="MLS/Aura Level 2 Cloud Ice Product V005 (ML2IWC) at GES DISC version: 005"
        )

    ML2DGG_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML2DGG_004",
            provider="GES_DISC", 
            shortname="ML2DGG",
            version="004",
            description="MLS/Aura Level 2 Diagnostics, Geophysical Parameter Grid V004 (ML2DGG) at GES DISC version: 004"
        )

    ML2DGG_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML2DGG_005",
            provider="GES_DISC", 
            shortname="ML2DGG",
            version="005",
            description="MLS/Aura Level 2 Diagnostics, Geophysical Parameter Grid V005 (ML2DGG) at GES DISC version: 005"
        )

    ML2DGM_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML2DGM_004",
            provider="GES_DISC", 
            shortname="ML2DGM",
            version="004",
            description="MLS/Aura Level 2 Diagnostics, Miscellaneous Grid V004 (ML2DGM) at GES DISC version: 004"
        )

    ML2DGM_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML2DGM_005",
            provider="GES_DISC", 
            shortname="ML2DGM",
            version="005",
            description="MLS/Aura Level 2 Diagnostics, Miscellaneous Grid V005 (ML2DGM) at GES DISC version: 005"
        )

    ML2GPH_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML2GPH_004",
            provider="GES_DISC", 
            shortname="ML2GPH",
            version="004",
            description="MLS/Aura Level 2 Geopotential Height V004 (ML2GPH) at GES DISC version: 004"
        )

    ML2GPH_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML2GPH_005",
            provider="GES_DISC", 
            shortname="ML2GPH",
            version="005",
            description="MLS/Aura Level 2 Geopotential Height V005 (ML2GPH) at GES DISC version: 005"
        )

    ML2HCL_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML2HCL_004",
            provider="GES_DISC", 
            shortname="ML2HCL",
            version="004",
            description="MLS/Aura Level 2 Hydrogen Chloride (HCl) Mixing Ratio V004 (ML2HCL) at GES DISC version: 004"
        )

    ML2HCL_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML2HCL_005",
            provider="GES_DISC", 
            shortname="ML2HCL",
            version="005",
            description="MLS/Aura Level 2 Hydrogen Chloride (HCl) Mixing Ratio V005 (ML2HCL) at GES DISC version: 005"
        )

    ML2HCN_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML2HCN_004",
            provider="GES_DISC", 
            shortname="ML2HCN",
            version="004",
            description="MLS/Aura Level 2 Hydrogen Cyanide (HCN) Mixing Ratio V004 (ML2HCN) at GES DISC version: 004"
        )

    ML2HCN_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML2HCN_005",
            provider="GES_DISC", 
            shortname="ML2HCN",
            version="005",
            description="MLS/Aura Level 2 Hydrogen Cyanide (HCN) Mixing Ratio V005 (ML2HCN) at GES DISC version: 005"
        )

    ML2HO2_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML2HO2_004",
            provider="GES_DISC", 
            shortname="ML2HO2",
            version="004",
            description="MLS/Aura Level 2 Hydroperoxy (HO2) Mixing Ratio V004 (ML2HO2) at GES DISC version: 004"
        )

    ML2HO2_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML2HO2_005",
            provider="GES_DISC", 
            shortname="ML2HO2",
            version="005",
            description="MLS/Aura Level 2 Hydroperoxy (HO2) Mixing Ratio V005 (ML2HO2) at GES DISC version: 005"
        )

    ML2OH_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML2OH_004",
            provider="GES_DISC", 
            shortname="ML2OH",
            version="004",
            description="MLS/Aura Level 2 Hydroxyl (OH) Mixing Ratio V004 (ML2OH) at GES DISC version: 004"
        )

    ML2OH_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML2OH_005",
            provider="GES_DISC", 
            shortname="ML2OH",
            version="005",
            description="MLS/Aura Level 2 Hydroxyl (OH) Mixing Ratio V005 (ML2OH) at GES DISC version: 005"
        )

    ML2HOCL_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML2HOCL_004",
            provider="GES_DISC", 
            shortname="ML2HOCL",
            version="004",
            description="MLS/Aura Level 2 Hypochlorous Acid (HOCl) Mixing Ratio V004 (ML2HOCL) at GES DISC version: 004"
        )

    ML2HOCL_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML2HOCL_005",
            provider="GES_DISC", 
            shortname="ML2HOCL",
            version="005",
            description="MLS/Aura Level 2 Hypochlorous Acid (HOCl) Mixing Ratio V005 (ML2HOCL) at GES DISC version: 005"
        )

    ML2CH3OH_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML2CH3OH_004",
            provider="GES_DISC", 
            shortname="ML2CH3OH",
            version="004",
            description="MLS/Aura Level 2 Methanol (CH3OH) Mixing Ratio V004 (ML2CH3OH) at GES DISC version: 004"
        )

    ML2CH3OH_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML2CH3OH_005",
            provider="GES_DISC", 
            shortname="ML2CH3OH",
            version="005",
            description="MLS/Aura Level 2 Methanol (CH3OH) Mixing Ratio V005 (ML2CH3OH) at GES DISC version: 005"
        )

    ML2CH3CL_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML2CH3CL_004",
            provider="GES_DISC", 
            shortname="ML2CH3CL",
            version="004",
            description="MLS/Aura Level 2 Methyl Chloride (CH3CL) Mixing Ratio V004 (ML2CH3CL) at GES DISC version: 004"
        )

    ML2CH3CL_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML2CH3CL_005",
            provider="GES_DISC", 
            shortname="ML2CH3CL",
            version="005",
            description="MLS/Aura Level 2 Methyl Chloride (CH3CL) Mixing Ratio V005 (ML2CH3CL) at GES DISC version: 005"
        )

    ML2CH3CN_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML2CH3CN_004",
            provider="GES_DISC", 
            shortname="ML2CH3CN",
            version="004",
            description="MLS/Aura Level 2 Methyl Cyanide (CH3CN) Mixing Ratio V004 (ML2CH3CN) at GES DISC version: 004"
        )

    ML2CH3CN_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML2CH3CN_005",
            provider="GES_DISC", 
            shortname="ML2CH3CN",
            version="005",
            description="MLS/Aura Level 2 Methyl Cyanide (CH3CN) Mixing Ratio V005 (ML2CH3CN) at GES DISC version: 005"
        )

    ML2HNO3_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML2HNO3_004",
            provider="GES_DISC", 
            shortname="ML2HNO3",
            version="004",
            description="MLS/Aura Level 2 Nitric Acid (HNO3) Mixing Ratio V004 (ML2HNO3) at GES DISC version: 004"
        )

    ML2HNO3_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML2HNO3_005",
            provider="GES_DISC", 
            shortname="ML2HNO3",
            version="005",
            description="MLS/Aura Level 2 Nitric Acid (HNO3) Mixing Ratio V005 (ML2HNO3) at GES DISC version: 005"
        )

    ML2N2O_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML2N2O_004",
            provider="GES_DISC", 
            shortname="ML2N2O",
            version="004",
            description="MLS/Aura Level 2 Nitrous Oxide (N2O) Mixing Ratio V004 (ML2N2O) at GES DISC version: 004"
        )

    ML2N2O_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML2N2O_005",
            provider="GES_DISC", 
            shortname="ML2N2O",
            version="005",
            description="MLS/Aura Level 2 Nitrous Oxide (N2O) Mixing Ratio V005 (ML2N2O) at GES DISC version: 005"
        )

    ML2O3_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML2O3_004",
            provider="GES_DISC", 
            shortname="ML2O3",
            version="004",
            description="MLS/Aura Level 2 Ozone (O3) Mixing Ratio V004 (ML2O3) at GES DISC version: 004"
        )

    ML2O3_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML2O3_005",
            provider="GES_DISC", 
            shortname="ML2O3",
            version="005",
            description="MLS/Aura Level 2 Ozone (O3) Mixing Ratio V005 (ML2O3) at GES DISC version: 005"
        )

    ML2RHI_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML2RHI_004",
            provider="GES_DISC", 
            shortname="ML2RHI",
            version="004",
            description="MLS/Aura Level 2 Relative Humidity With Respect To Ice V004 (ML2RHI) at GES DISC version: 004"
        )

    ML2RHI_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML2RHI_005",
            provider="GES_DISC", 
            shortname="ML2RHI",
            version="005",
            description="MLS/Aura Level 2 Relative Humidity With Respect To Ice V005 (ML2RHI) at GES DISC version: 005"
        )

    ML2SO2_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML2SO2_004",
            provider="GES_DISC", 
            shortname="ML2SO2",
            version="004",
            description="MLS/Aura Level 2 Sulfur Dioxide (SO2) Mixing Ratio V004 (ML2SO2) at GES DISC version: 004"
        )

    ML2SO2_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML2SO2_005",
            provider="GES_DISC", 
            shortname="ML2SO2",
            version="005",
            description="MLS/Aura Level 2 Sulfur Dioxide (SO2) Mixing Ratio V005 (ML2SO2) at GES DISC version: 005"
        )

    ML2T_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML2T_004",
            provider="GES_DISC", 
            shortname="ML2T",
            version="004",
            description="MLS/Aura Level 2 Temperature V004 (ML2T) at GES DISC version: 004"
        )

    ML2T_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML2T_005",
            provider="GES_DISC", 
            shortname="ML2T",
            version="005",
            description="MLS/Aura Level 2 Temperature V005 (ML2T) at GES DISC version: 005"
        )

    ML2H2O_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML2H2O_004",
            provider="GES_DISC", 
            shortname="ML2H2O",
            version="004",
            description="MLS/Aura Level 2 Water Vapor (H2O) Mixing Ratio V004 (ML2H2O) at GES DISC version: 004"
        )

    ML2H2O_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML2H2O_005",
            provider="GES_DISC", 
            shortname="ML2H2O",
            version="005",
            description="MLS/Aura Level 2 Water Vapor (H2O) Mixing Ratio V005 (ML2H2O) at GES DISC version: 005"
        )

    ML3DZMBRO_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3DZMBRO_004",
            provider="GES_DISC", 
            shortname="ML3DZMBRO",
            version="004",
            description="MLS/Aura Level 3 Bromine Monoxide (BrO) Daily 10degrees Lat Zonal Mean V004 (ML3DZMBRO) at GES DISC version: 004"
        )

    ML3DBCO_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3DBCO_004",
            provider="GES_DISC", 
            shortname="ML3DBCO",
            version="004",
            description="MLS/Aura Level 3 Daily Binned Carbon Monoxide (CO) Mixing Ratio on Assorted Grids V004 (ML3DBCO) at GES DISC version: 004"
        )

    ML3DBCO_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3DBCO_005",
            provider="GES_DISC", 
            shortname="ML3DBCO",
            version="005",
            description="MLS/Aura Level 3 Daily Binned Carbon Monoxide (CO) Mixing Ratio on Assorted Grids V005 (ML3DBCO) at GES DISC version: 005"
        )

    ML3DZCO_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3DZCO_004",
            provider="GES_DISC", 
            shortname="ML3DZCO",
            version="004",
            description="MLS/Aura Level 3 Daily Binned Carbon Monoxide (CO) Mixing Ratio on Zonal and Similar Grids V004 (ML3DZCO) at GES DISC version: 004"
        )

    ML3DZCO_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3DZCO_005",
            provider="GES_DISC", 
            shortname="ML3DZCO",
            version="005",
            description="MLS/Aura Level 3 Daily Binned Carbon Monoxide (CO) Mixing Ratio on Zonal and Similar Grids V005 (ML3DZCO) at GES DISC version: 005"
        )

    ML3DBCLO_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3DBCLO_004",
            provider="GES_DISC", 
            shortname="ML3DBCLO",
            version="004",
            description="MLS/Aura Level 3 Daily Binned Chlorine Monoxide (ClO) Mixing Ratio on Assorted Grids V004 (ML3DBCLO) at GES DISC version: 004"
        )

    ML3DBCLO_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3DBCLO_005",
            provider="GES_DISC", 
            shortname="ML3DBCLO",
            version="005",
            description="MLS/Aura Level 3 Daily Binned Chlorine Monoxide (ClO) Mixing Ratio on Assorted Grids V005 (ML3DBCLO) at GES DISC version: 005"
        )

    ML3DZCLO_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3DZCLO_004",
            provider="GES_DISC", 
            shortname="ML3DZCLO",
            version="004",
            description="MLS/Aura Level 3 Daily Binned Chlorine Monoxide (ClO) Mixing Ratio on Zonal and Similar Grids V004 (ML3DZCLO) at GES DISC version: 004"
        )

    ML3DZCLO_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3DZCLO_005",
            provider="GES_DISC", 
            shortname="ML3DZCLO",
            version="005",
            description="MLS/Aura Level 3 Daily Binned Chlorine Monoxide (ClO) Mixing Ratio on Zonal and Similar Grids V005 (ML3DZCLO) at GES DISC version: 005"
        )

    ML3DBIWC_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3DBIWC_004",
            provider="GES_DISC", 
            shortname="ML3DBIWC",
            version="004",
            description="MLS/Aura Level 3 Daily Binned Cloud Ice (IWC) on Assorted Grids V004 (ML3DBIWC) at GES DISC version: 004"
        )

    ML3DBIWC_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3DBIWC_005",
            provider="GES_DISC", 
            shortname="ML3DBIWC",
            version="005",
            description="MLS/Aura Level 3 Daily Binned Cloud Ice (IWC) on Assorted Grids V005 (ML3DBIWC) at GES DISC version: 005"
        )

    ML3DZIWC_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3DZIWC_004",
            provider="GES_DISC", 
            shortname="ML3DZIWC",
            version="004",
            description="MLS/Aura Level 3 Daily Binned Cloud Ice (IWC) on Zonal and Similar Grids V004 (ML3DZIWC) at GES DISC version: 004"
        )

    ML3DZIWC_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3DZIWC_005",
            provider="GES_DISC", 
            shortname="ML3DZIWC",
            version="005",
            description="MLS/Aura Level 3 Daily Binned Cloud Ice (IWC) on Zonal and Similar Grids V005 (ML3DZIWC) at GES DISC version: 005"
        )

    ML3DBGPH_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3DBGPH_004",
            provider="GES_DISC", 
            shortname="ML3DBGPH",
            version="004",
            description="MLS/Aura Level 3 Daily Binned Geopotential Height (GPH) on Assorted Grids V004 (ML3DBGPH) at GES DISC version: 004"
        )

    ML3DBGPH_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3DBGPH_005",
            provider="GES_DISC", 
            shortname="ML3DBGPH",
            version="005",
            description="MLS/Aura Level 3 Daily Binned Geopotential Height (GPH) on Assorted Grids V005 (ML3DBGPH) at GES DISC version: 005"
        )

    ML3DZGPH_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3DZGPH_004",
            provider="GES_DISC", 
            shortname="ML3DZGPH",
            version="004",
            description="MLS/Aura Level 3 Daily Binned Geopotential Height (GPH) on Zonal and Similar Grids V004 (ML3DZGPH) at GES DISC version: 004"
        )

    ML3DZGPH_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3DZGPH_005",
            provider="GES_DISC", 
            shortname="ML3DZGPH",
            version="005",
            description="MLS/Aura Level 3 Daily Binned Geopotential Height (GPH) on Zonal and Similar Grids V005 (ML3DZGPH) at GES DISC version: 005"
        )

    ML3DBHCL_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3DBHCL_004",
            provider="GES_DISC", 
            shortname="ML3DBHCL",
            version="004",
            description="MLS/Aura Level 3 Daily Binned Hydrogen Chloride (HCl) Mixing Ratio on Assorted Grids V004 (ML3DBHCL) at GES DISC version: 004"
        )

    ML3DBHCL_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3DBHCL_005",
            provider="GES_DISC", 
            shortname="ML3DBHCL",
            version="005",
            description="MLS/Aura Level 3 Daily Binned Hydrogen Chloride (HCl) Mixing Ratio on Assorted Grids V005 (ML3DBHCL) at GES DISC version: 005"
        )

    ML3DZHCL_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3DZHCL_004",
            provider="GES_DISC", 
            shortname="ML3DZHCL",
            version="004",
            description="MLS/Aura Level 3 Daily Binned Hydrogen Chloride (HCl) Mixing Ratio on Zonal and Similar Grids V004 (ML3DZHCL) at GES DISC version: 004"
        )

    ML3DZHCL_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3DZHCL_005",
            provider="GES_DISC", 
            shortname="ML3DZHCL",
            version="005",
            description="MLS/Aura Level 3 Daily Binned Hydrogen Chloride (HCl) Mixing Ratio on Zonal and Similar Grids V005 (ML3DZHCL) at GES DISC version: 005"
        )

    ML3DBHCN_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3DBHCN_004",
            provider="GES_DISC", 
            shortname="ML3DBHCN",
            version="004",
            description="MLS/Aura Level 3 Daily Binned Hydrogen Cyanide (HCN) Mixing Ratio on Assorted Grids V004 (ML3DBHCN) at GES DISC version: 004"
        )

    ML3DBHCN_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3DBHCN_005",
            provider="GES_DISC", 
            shortname="ML3DBHCN",
            version="005",
            description="MLS/Aura Level 3 Daily Binned Hydrogen Cyanide (HCN) Mixing Ratio on Assorted Grids V005 (ML3DBHCN) at GES DISC version: 005"
        )

    ML3DZHCN_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3DZHCN_004",
            provider="GES_DISC", 
            shortname="ML3DZHCN",
            version="004",
            description="MLS/Aura Level 3 Daily Binned Hydrogen Cyanide (HCN) Mixing Ratio on Zonal and Similar Grids V004 (ML3DZHCN) at GES DISC version: 004"
        )

    ML3DZHCN_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3DZHCN_005",
            provider="GES_DISC", 
            shortname="ML3DZHCN",
            version="005",
            description="MLS/Aura Level 3 Daily Binned Hydrogen Cyanide (HCN) Mixing Ratio on Zonal and Similar Grids V005 (ML3DZHCN) at GES DISC version: 005"
        )

    ML3DBOH_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3DBOH_004",
            provider="GES_DISC", 
            shortname="ML3DBOH",
            version="004",
            description="MLS/Aura Level 3 Daily Binned Hydroxyl (OH) Mixing Ratio on Assorted Grids V004 (ML3DBOH) at GES DISC version: 004"
        )

    ML3DBOH_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3DBOH_005",
            provider="GES_DISC", 
            shortname="ML3DBOH",
            version="005",
            description="MLS/Aura Level 3 Daily Binned Hydroxyl (OH) Mixing Ratio on Assorted Grids V005 (ML3DBOH) at GES DISC version: 005"
        )

    ML3DZOH_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3DZOH_004",
            provider="GES_DISC", 
            shortname="ML3DZOH",
            version="004",
            description="MLS/Aura Level 3 Daily Binned Hydroxyl (OH) Mixing Ratio on Zonal and Similar Grids V004 (ML3DZOH) at GES DISC version: 004"
        )

    ML3DZOH_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3DZOH_005",
            provider="GES_DISC", 
            shortname="ML3DZOH",
            version="005",
            description="MLS/Aura Level 3 Daily Binned Hydroxyl (OH) Mixing Ratio on Zonal and Similar Grids V005 (ML3DZOH) at GES DISC version: 005"
        )

    ML3DBHOCL_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3DBHOCL_004",
            provider="GES_DISC", 
            shortname="ML3DBHOCL",
            version="004",
            description="MLS/Aura Level 3 Daily Binned Hypochlorous Acid (HOCl) Mixing Ratio on Assorted Grids V004 (ML3DBHOCL) at GES DISC version: 004"
        )

    ML3DBHOCL_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3DBHOCL_005",
            provider="GES_DISC", 
            shortname="ML3DBHOCL",
            version="005",
            description="MLS/Aura Level 3 Daily Binned Hypochlorous Acid (HOCl) Mixing Ratio on Assorted Grids V005 (ML3DBHOCL) at GES DISC version: 005"
        )

    ML3DZHOCL_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3DZHOCL_004",
            provider="GES_DISC", 
            shortname="ML3DZHOCL",
            version="004",
            description="MLS/Aura Level 3 Daily Binned Hypochlorous Acid (HOCl) Mixing Ratio on Zonal and Similar Grids V004 (ML3DZHOCL) at GES DISC version: 004"
        )

    ML3DZHOCL_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3DZHOCL_005",
            provider="GES_DISC", 
            shortname="ML3DZHOCL",
            version="005",
            description="MLS/Aura Level 3 Daily Binned Hypochlorous Acid (HOCl) Mixing Ratio on Zonal and Similar Grids V005 (ML3DZHOCL) at GES DISC version: 005"
        )

    ML3DBCH3CL_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3DBCH3CL_004",
            provider="GES_DISC", 
            shortname="ML3DBCH3CL",
            version="004",
            description="MLS/Aura Level 3 Daily Binned Methyl Chloride (CH3Cl) Mixing Ratio on Assorted Grids V004 (ML3DBCH3CL) at GES DISC version: 004"
        )

    ML3DBCH3CL_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3DBCH3CL_005",
            provider="GES_DISC", 
            shortname="ML3DBCH3CL",
            version="005",
            description="MLS/Aura Level 3 Daily Binned Methyl Chloride (CH3Cl) Mixing Ratio on Assorted Grids V005 (ML3DBCH3CL) at GES DISC version: 005"
        )

    ML3DZCH3CL_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3DZCH3CL_004",
            provider="GES_DISC", 
            shortname="ML3DZCH3CL",
            version="004",
            description="MLS/Aura Level 3 Daily Binned Methyl Chloride (CH3Cl) Mixing Ratio on Zonal and Similar Grids V004 (ML3DZCH3CL) at GES DISC version: 004"
        )

    ML3DZCH3CL_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3DZCH3CL_005",
            provider="GES_DISC", 
            shortname="ML3DZCH3CL",
            version="005",
            description="MLS/Aura Level 3 Daily Binned Methyl Chloride (CH3Cl) Mixing Ratio on Zonal and Similar Grids V005 (ML3DZCH3CL) at GES DISC version: 005"
        )

    ML3DBHNO3_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3DBHNO3_004",
            provider="GES_DISC", 
            shortname="ML3DBHNO3",
            version="004",
            description="MLS/Aura Level 3 Daily Binned Nitric Acid (HNO3) Mixing Ratio on Assorted Grids V004 (ML3DBHNO3) at GES DISC version: 004"
        )

    ML3DBHNO3_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3DBHNO3_005",
            provider="GES_DISC", 
            shortname="ML3DBHNO3",
            version="005",
            description="MLS/Aura Level 3 Daily Binned Nitric Acid (HNO3) Mixing Ratio on Assorted Grids V005 (ML3DBHNO3) at GES DISC version: 005"
        )

    ML3DZHNO3_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3DZHNO3_004",
            provider="GES_DISC", 
            shortname="ML3DZHNO3",
            version="004",
            description="MLS/Aura Level 3 Daily Binned Nitric Acid (HNO3) Mixing Ratio on Zonal and Similar Grids V004 (ML3DZHNO3) at GES DISC version: 004"
        )

    ML3DZHNO3_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3DZHNO3_005",
            provider="GES_DISC", 
            shortname="ML3DZHNO3",
            version="005",
            description="MLS/Aura Level 3 Daily Binned Nitric Acid (HNO3) Mixing Ratio on Zonal and Similar Grids V005 (ML3DZHNO3) at GES DISC version: 005"
        )

    ML3DBN2O_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3DBN2O_004",
            provider="GES_DISC", 
            shortname="ML3DBN2O",
            version="004",
            description="MLS/Aura Level 3 Daily Binned Nitrous Oxide (N2O) Mixing Ratio on Assorted Grids V004 (ML3DBN2O) at GES DISC version: 004"
        )

    ML3DBN2O_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3DBN2O_005",
            provider="GES_DISC", 
            shortname="ML3DBN2O",
            version="005",
            description="MLS/Aura Level 3 Daily Binned Nitrous Oxide (N2O) Mixing Ratio on Assorted Grids V005 (ML3DBN2O) at GES DISC version: 005"
        )

    ML3DZN2O_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3DZN2O_004",
            provider="GES_DISC", 
            shortname="ML3DZN2O",
            version="004",
            description="MLS/Aura Level 3 Daily Binned Nitrous Oxide (N2O) Mixing Ratio on Zonal and Similar Grids V004 (ML3DZN2O) at GES DISC version: 004"
        )

    ML3DZN2O_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3DZN2O_005",
            provider="GES_DISC", 
            shortname="ML3DZN2O",
            version="005",
            description="MLS/Aura Level 3 Daily Binned Nitrous Oxide (N2O) Mixing Ratio on Zonal and Similar Grids V005 (ML3DZN2O) at GES DISC version: 005"
        )

    ML3DBO3_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3DBO3_004",
            provider="GES_DISC", 
            shortname="ML3DBO3",
            version="004",
            description="MLS/Aura Level 3 Daily Binned Ozone (O3) Mixing Ratio on Assorted Grids V004 (ML3DBO3) at GES DISC version: 004"
        )

    ML3DBO3_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3DBO3_005",
            provider="GES_DISC", 
            shortname="ML3DBO3",
            version="005",
            description="MLS/Aura Level 3 Daily Binned Ozone (O3) Mixing Ratio on Assorted Grids V005 (ML3DBO3) at GES DISC version: 005"
        )

    ML3DZO3_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3DZO3_004",
            provider="GES_DISC", 
            shortname="ML3DZO3",
            version="004",
            description="MLS/Aura Level 3 Daily Binned Ozone (O3) Mixing Ratio on Zonal and Similar Grids V004 (ML3DZO3) at GES DISC version: 004"
        )

    ML3DZO3_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3DZO3_005",
            provider="GES_DISC", 
            shortname="ML3DZO3",
            version="005",
            description="MLS/Aura Level 3 Daily Binned Ozone (O3) Mixing Ratio on Zonal and Similar Grids V005 (ML3DZO3) at GES DISC version: 005"
        )

    ML3DBRHI_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3DBRHI_004",
            provider="GES_DISC", 
            shortname="ML3DBRHI",
            version="004",
            description="MLS/Aura Level 3 Daily Binned Relative Humidity With Respect To Ice (RHI) on Assorted Grids V004 (ML3DBRHI) at GES DISC version: 004"
        )

    ML3DBRHI_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3DBRHI_005",
            provider="GES_DISC", 
            shortname="ML3DBRHI",
            version="005",
            description="MLS/Aura Level 3 Daily Binned Relative Humidity With Respect To Ice (RHI) on Assorted Grids V005 (ML3DBRHI) at GES DISC version: 005"
        )

    ML3DZRHI_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3DZRHI_004",
            provider="GES_DISC", 
            shortname="ML3DZRHI",
            version="004",
            description="MLS/Aura Level 3 Daily Binned Relative Humidity With Respect To Ice (RHI) on Zonal and Similar Grids V004 (ML3DZRHI) at GES DISC version: 004"
        )

    ML3DZRHI_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3DZRHI_005",
            provider="GES_DISC", 
            shortname="ML3DZRHI",
            version="005",
            description="MLS/Aura Level 3 Daily Binned Relative Humidity With Respect To Ice (RHI) on Zonal and Similar Grids V005 (ML3DZRHI) at GES DISC version: 005"
        )

    ML3DBSO2_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3DBSO2_004",
            provider="GES_DISC", 
            shortname="ML3DBSO2",
            version="004",
            description="MLS/Aura Level 3 Daily Binned Sulfur Dioxide (SO2) Mixing Ratio on Assorted Grids V004 (ML3DBSO2) at GES DISC version: 004"
        )

    ML3DBSO2_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3DBSO2_005",
            provider="GES_DISC", 
            shortname="ML3DBSO2",
            version="005",
            description="MLS/Aura Level 3 Daily Binned Sulfur Dioxide (SO2) Mixing Ratio on Assorted Grids V005 (ML3DBSO2) at GES DISC version: 005"
        )

    ML3DZSO2_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3DZSO2_004",
            provider="GES_DISC", 
            shortname="ML3DZSO2",
            version="004",
            description="MLS/Aura Level 3 Daily Binned Sulfur Dioxide (SO2) Mixing Ratio on Zonal and Similar Grids V004 (ML3DZSO2) at GES DISC version: 004"
        )

    ML3DZSO2_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3DZSO2_005",
            provider="GES_DISC", 
            shortname="ML3DZSO2",
            version="005",
            description="MLS/Aura Level 3 Daily Binned Sulfur Dioxide (SO2) Mixing Ratio on Zonal and Similar Grids V005 (ML3DZSO2) at GES DISC version: 005"
        )

    ML3DBT_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3DBT_004",
            provider="GES_DISC", 
            shortname="ML3DBT",
            version="004",
            description="MLS/Aura Level 3 Daily Binned Temperature on Assorted Grids V004 (ML3DBT) at GES DISC version: 004"
        )

    ML3DBT_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3DBT_005",
            provider="GES_DISC", 
            shortname="ML3DBT",
            version="005",
            description="MLS/Aura Level 3 Daily Binned Temperature on Assorted Grids V005 (ML3DBT) at GES DISC version: 005"
        )

    ML3DZT_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3DZT_004",
            provider="GES_DISC", 
            shortname="ML3DZT",
            version="004",
            description="MLS/Aura Level 3 Daily Binned Temperature on Zonal and Similar Grids V004 (ML3DZT) at GES DISC version: 004"
        )

    ML3DZT_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3DZT_005",
            provider="GES_DISC", 
            shortname="ML3DZT",
            version="005",
            description="MLS/Aura Level 3 Daily Binned Temperature on Zonal and Similar Grids V005 (ML3DZT) at GES DISC version: 005"
        )

    ML3DBH2O_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3DBH2O_004",
            provider="GES_DISC", 
            shortname="ML3DBH2O",
            version="004",
            description="MLS/Aura Level 3 Daily Binned Water Vapor (H2O) Mixing Ratio on Assorted Grids V004 (ML3DBH2O) at GES DISC version: 004"
        )

    ML3DBH2O_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3DBH2O_005",
            provider="GES_DISC", 
            shortname="ML3DBH2O",
            version="005",
            description="MLS/Aura Level 3 Daily Binned Water Vapor (H2O) Mixing Ratio on Assorted Grids V005 (ML3DBH2O) at GES DISC version: 005"
        )

    ML3DZH2O_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3DZH2O_004",
            provider="GES_DISC", 
            shortname="ML3DZH2O",
            version="004",
            description="MLS/Aura Level 3 Daily Binned Water Vapor (H2O) Mixing Ratio on Zonal and Similar Grids V004 (ML3DZH2O) at GES DISC version: 004"
        )

    ML3DZH2O_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3DZH2O_005",
            provider="GES_DISC", 
            shortname="ML3DZH2O",
            version="005",
            description="MLS/Aura Level 3 Daily Binned Water Vapor (H2O) Mixing Ratio on Zonal and Similar Grids V005 (ML3DZH2O) at GES DISC version: 005"
        )

    ML3DZMHO2_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3DZMHO2_004",
            provider="GES_DISC", 
            shortname="ML3DZMHO2",
            version="004",
            description="MLS/Aura Level 3 Hydroperoxy (HO2) Daily 10degrees Lat Zonal Mean V004 (ML3DZMHO2) at GES DISC version: 004"
        )

    ML3MBCO_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3MBCO_004",
            provider="GES_DISC", 
            shortname="ML3MBCO",
            version="004",
            description="MLS/Aura Level 3 Monthly Binned Carbon Monoxide (CO) Mixing Ratio on Assorted Grids V004 (ML3MBCO) at GES DISC version: 004"
        )

    ML3MBCO_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3MBCO_005",
            provider="GES_DISC", 
            shortname="ML3MBCO",
            version="005",
            description="MLS/Aura Level 3 Monthly Binned Carbon Monoxide (CO) Mixing Ratio on Assorted Grids V005 (ML3MBCO) at GES DISC version: 005"
        )

    ML3MBCLO_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3MBCLO_004",
            provider="GES_DISC", 
            shortname="ML3MBCLO",
            version="004",
            description="MLS/Aura Level 3 Monthly Binned Chlorine Monoxide (ClO) Mixing Ratio on Assorted Grids V004 (ML3MBCLO) at GES DISC version: 004"
        )

    ML3MBCLO_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3MBCLO_005",
            provider="GES_DISC", 
            shortname="ML3MBCLO",
            version="005",
            description="MLS/Aura Level 3 Monthly Binned Chlorine Monoxide (ClO) Mixing Ratio on Assorted Grids V005 (ML3MBCLO) at GES DISC version: 005"
        )

    ML3MBIWC_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3MBIWC_004",
            provider="GES_DISC", 
            shortname="ML3MBIWC",
            version="004",
            description="MLS/Aura Level 3 Monthly Binned Cloud Ice (IWC) on Assorted Grids V004 (ML3MBIWC) at GES DISC version: 004"
        )

    ML3MBIWC_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3MBIWC_005",
            provider="GES_DISC", 
            shortname="ML3MBIWC",
            version="005",
            description="MLS/Aura Level 3 Monthly Binned Cloud Ice (IWC) on Assorted Grids V005 (ML3MBIWC) at GES DISC version: 005"
        )

    ML3MBGPH_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3MBGPH_004",
            provider="GES_DISC", 
            shortname="ML3MBGPH",
            version="004",
            description="MLS/Aura Level 3 Monthly Binned Geopotential Height (GPH) on Assorted Grids V004 (ML3MBGPH) at GES DISC version: 004"
        )

    ML3MBGPH_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3MBGPH_005",
            provider="GES_DISC", 
            shortname="ML3MBGPH",
            version="005",
            description="MLS/Aura Level 3 Monthly Binned Geopotential Height (GPH) on Assorted Grids V005 (ML3MBGPH) at GES DISC version: 005"
        )

    ML3MBHCL_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3MBHCL_004",
            provider="GES_DISC", 
            shortname="ML3MBHCL",
            version="004",
            description="MLS/Aura Level 3 Monthly Binned Hydrogen Chloride (HCl) Mixing Ratio on Assorted Grids V004 (ML3MBHCL) at GES DISC version: 004"
        )

    ML3MBHCL_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3MBHCL_005",
            provider="GES_DISC", 
            shortname="ML3MBHCL",
            version="005",
            description="MLS/Aura Level 3 Monthly Binned Hydrogen Chloride (HCl) Mixing Ratio on Assorted Grids V005 (ML3MBHCL) at GES DISC version: 005"
        )

    ML3MBHCN_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3MBHCN_004",
            provider="GES_DISC", 
            shortname="ML3MBHCN",
            version="004",
            description="MLS/Aura Level 3 Monthly Binned Hydrogen Cyanide (HCN) Mixing Ratio on Assorted Grids V004 (ML3MBHCN) at GES DISC version: 004"
        )

    ML3MBHCN_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3MBHCN_005",
            provider="GES_DISC", 
            shortname="ML3MBHCN",
            version="005",
            description="MLS/Aura Level 3 Monthly Binned Hydrogen Cyanide (HCN) Mixing Ratio on Assorted Grids V005 (ML3MBHCN) at GES DISC version: 005"
        )

    ML3MBOH_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3MBOH_004",
            provider="GES_DISC", 
            shortname="ML3MBOH",
            version="004",
            description="MLS/Aura Level 3 Monthly Binned Hydroxyl (OH) Mixing Ratio on Assorted Grids V004 (ML3MBOH) at GES DISC version: 004"
        )

    ML3MBOH_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3MBOH_005",
            provider="GES_DISC", 
            shortname="ML3MBOH",
            version="005",
            description="MLS/Aura Level 3 Monthly Binned Hydroxyl (OH) Mixing Ratio on Assorted Grids V005 (ML3MBOH) at GES DISC version: 005"
        )

    ML3MBHOCL_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3MBHOCL_004",
            provider="GES_DISC", 
            shortname="ML3MBHOCL",
            version="004",
            description="MLS/Aura Level 3 Monthly Binned Hypochlorous Acid (HOCl) Mixing Ratio on Assorted Grids V004 (ML3MBHOCL) at GES DISC version: 004"
        )

    ML3MBHOCL_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3MBHOCL_005",
            provider="GES_DISC", 
            shortname="ML3MBHOCL",
            version="005",
            description="MLS/Aura Level 3 Monthly Binned Hypochlorous Acid (HOCl) Mixing Ratio on Assorted Grids V005 (ML3MBHOCL) at GES DISC version: 005"
        )

    ML3MBCH3CL_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3MBCH3CL_004",
            provider="GES_DISC", 
            shortname="ML3MBCH3CL",
            version="004",
            description="MLS/Aura Level 3 Monthly Binned Methyl Chloride (CH3Cl) Mixing Ratio on Assorted Grids V004 (ML3MBCH3CL) at GES DISC version: 004"
        )

    ML3MBCH3CL_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3MBCH3CL_005",
            provider="GES_DISC", 
            shortname="ML3MBCH3CL",
            version="005",
            description="MLS/Aura Level 3 Monthly Binned Methyl Chloride (CH3Cl) Mixing Ratio on Assorted Grids V005 (ML3MBCH3CL) at GES DISC version: 005"
        )

    ML3MBHNO3_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3MBHNO3_004",
            provider="GES_DISC", 
            shortname="ML3MBHNO3",
            version="004",
            description="MLS/Aura Level 3 Monthly Binned Nitric Acid (HNO3) Mixing Ratio on Assorted Grids V004 (ML3MBHNO3) at GES DISC version: 004"
        )

    ML3MBHNO3_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3MBHNO3_005",
            provider="GES_DISC", 
            shortname="ML3MBHNO3",
            version="005",
            description="MLS/Aura Level 3 Monthly Binned Nitric Acid (HNO3) Mixing Ratio on Assorted Grids V005 (ML3MBHNO3) at GES DISC version: 005"
        )

    ML3MBN2O_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3MBN2O_004",
            provider="GES_DISC", 
            shortname="ML3MBN2O",
            version="004",
            description="MLS/Aura Level 3 Monthly Binned Nitrous Oxide (N2O) Mixing Ratio on Assorted Grids V004 (ML3MBN2O) at GES DISC version: 004"
        )

    ML3MBN2O_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3MBN2O_005",
            provider="GES_DISC", 
            shortname="ML3MBN2O",
            version="005",
            description="MLS/Aura Level 3 Monthly Binned Nitrous Oxide (N2O) Mixing Ratio on Assorted Grids V005 (ML3MBN2O) at GES DISC version: 005"
        )

    ML3MBO3_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3MBO3_004",
            provider="GES_DISC", 
            shortname="ML3MBO3",
            version="004",
            description="MLS/Aura Level 3 Monthly Binned Ozone (O3) Mixing Ratio on Assorted Grids V004 (ML3MBO3) at GES DISC version: 004"
        )

    ML3MBO3_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3MBO3_005",
            provider="GES_DISC", 
            shortname="ML3MBO3",
            version="005",
            description="MLS/Aura Level 3 Monthly Binned Ozone (O3) Mixing Ratio on Assorted Grids V005 (ML3MBO3) at GES DISC version: 005"
        )

    ML3MBRHI_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3MBRHI_004",
            provider="GES_DISC", 
            shortname="ML3MBRHI",
            version="004",
            description="MLS/Aura Level 3 Monthly Binned Relative Humidity With Respect To Ice (RHI) on Assorted Grids V004 (ML3MBRHI) at GES DISC version: 004"
        )

    ML3MBRHI_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3MBRHI_005",
            provider="GES_DISC", 
            shortname="ML3MBRHI",
            version="005",
            description="MLS/Aura Level 3 Monthly Binned Relative Humidity With Respect To Ice (RHI) on Assorted Grids V005 (ML3MBRHI) at GES DISC version: 005"
        )

    ML3MBSO2_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3MBSO2_004",
            provider="GES_DISC", 
            shortname="ML3MBSO2",
            version="004",
            description="MLS/Aura Level 3 Monthly Binned Sulfur Dioxide (SO2) Mixing Ratio on Assorted Grids V004 (ML3MBSO2) at GES DISC version: 004"
        )

    ML3MBSO2_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3MBSO2_005",
            provider="GES_DISC", 
            shortname="ML3MBSO2",
            version="005",
            description="MLS/Aura Level 3 Monthly Binned Sulfur Dioxide (SO2) Mixing Ratio on Assorted Grids V005 (ML3MBSO2) at GES DISC version: 005"
        )

    ML3MBT_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3MBT_004",
            provider="GES_DISC", 
            shortname="ML3MBT",
            version="004",
            description="MLS/Aura Level 3 Monthly Binned Temperature on Assorted Grids V004 (ML3MBT) at GES DISC version: 004"
        )

    ML3MBT_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3MBT_005",
            provider="GES_DISC", 
            shortname="ML3MBT",
            version="005",
            description="MLS/Aura Level 3 Monthly Binned Temperature on Assorted Grids V005 (ML3MBT) at GES DISC version: 005"
        )

    ML3MBH2O_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3MBH2O_004",
            provider="GES_DISC", 
            shortname="ML3MBH2O",
            version="004",
            description="MLS/Aura Level 3 Monthly Binned Water Vapor (H2O) Mixing Ratio on Assorted Grids V004 (ML3MBH2O) at GES DISC version: 004"
        )

    ML3MBH2O_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML3MBH2O_005",
            provider="GES_DISC", 
            shortname="ML3MBH2O",
            version="005",
            description="MLS/Aura Level 3 Monthly Binned Water Vapor (H2O) Mixing Ratio on Assorted Grids V005 (ML3MBH2O) at GES DISC version: 005"
        )

    ML2CO_NRT_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML2CO_NRT_005",
            provider="GES_DISC", 
            shortname="ML2CO_NRT",
            version="005",
            description="MLS/Aura Near-Real-Time L2 Carbon Monoxide (CO) Mixing Ratio V005 (ML2CO_NRT) at GES DISC version: 005"
        )

    ML2HNO3_NRT_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML2HNO3_NRT_005",
            provider="GES_DISC", 
            shortname="ML2HNO3_NRT",
            version="005",
            description="MLS/Aura Near-Real-Time L2 Nitric Acid (HNO3) Mixing Ratio V005 (ML2HNO3_NRT) at GES DISC version: 005"
        )

    ML2N2O_NRT_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML2N2O_NRT_005",
            provider="GES_DISC", 
            shortname="ML2N2O_NRT",
            version="005",
            description="MLS/Aura Near-Real-Time L2 Nitrous Oxide (N2O) Mixing Ratio V005 (ML2N2O_NRT) at GES DISC version: 005"
        )

    ML2O3_NRT_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML2O3_NRT_005",
            provider="GES_DISC", 
            shortname="ML2O3_NRT",
            version="005",
            description="MLS/Aura Near-Real-Time L2 Ozone (O3) Mixing Ratio V005 (ML2O3_NRT) at GES DISC version: 005"
        )

    ML2SO2_NRT_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML2SO2_NRT_005",
            provider="GES_DISC", 
            shortname="ML2SO2_NRT",
            version="005",
            description="MLS/Aura Near-Real-Time L2 Sulfur Dioxide (SO2) Mixing Ratio V005 (ML2SO2_NRT) at GES DISC version: 005"
        )

    ML2T_NRT_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML2T_NRT_005",
            provider="GES_DISC", 
            shortname="ML2T_NRT",
            version="005",
            description="MLS/Aura Near-Real-Time L2 Temperature V005 (ML2T_NRT) at GES DISC version: 005"
        )

    ML2H2O_NRT_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ML2H2O_NRT_005",
            provider="GES_DISC", 
            shortname="ML2H2O_NRT",
            version="005",
            description="MLS/Aura Near-Real-Time L2 Water Vapor (H2O) Mixing Ratio V005 (ML2H2O_NRT) at GES DISC version: 005"
        )

    MYD_L2_CB_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_MYD_L2_CB_001",
            provider="GES_DISC", 
            shortname="MYD_L2_CB",
            version="001",
            description="MODIS Aqua L2 chopped blocks (block size: 128 pixels x 128 pixels, daytime) V001 (MYD_L2_CB) at GES DISC version: 001"
        )

    MYD_L2_DC_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_MYD_L2_DC_001",
            provider="GES_DISC", 
            shortname="MYD_L2_DC",
            version="001",
            description="MODIS Aqua L2 deep-convective cloud classification version: 001"
        )

    MYD_L2_MPLCT_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_MYD_L2_MPLCT_001",
            provider="GES_DISC", 
            shortname="MYD_L2_MPLCT",
            version="001",
            description="MODIS Aqua L2 model predicted low cloud types of chopped blocks in which low cloud dominates (block size: 128pixels x 128pixels) V001 (MYD_L2_MPLCT) at GES DISC version: 001"
        )

    MYD_L3_OFLCT_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_MYD_L3_OFLCT_001",
            provider="GES_DISC", 
            shortname="MYD_L3_OFLCT",
            version="001",
            description="MODIS Aqua L3 occurrence frequency of low-cloud types monthly mean and annual mean 2x2 degree resolution V001 (MYD_L3_OFLCT) at GES DISC version: 001"
        )

    MOD_L2_DC_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_MOD_L2_DC_001",
            provider="GES_DISC", 
            shortname="MOD_L2_DC",
            version="001",
            description="MODIS Terra L2 deep-convective cloud classification version: 001"
        )

    MYD14CM1_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_MYD14CM1_005",
            provider="GES_DISC", 
            shortname="MYD14CM1",
            version="005",
            description="MODIS/Aqua 1 degree Gridded MODIS Active Fire Product V005 (MYD14CM1) at GES DISC version: 005"
        )

    MAC04S0_V002_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_MAC04S0_002",
            provider="GES_DISC", 
            shortname="MAC04S0",
            version="002",
            description="MODIS/Aqua Aerosol 10km 5-Min L2 Narrow Swath Subset along CloudSat V002 (MAC04S0) at GES DISC version: 002"
        )

    MAC04S1_V002_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_MAC04S1_002",
            provider="GES_DISC", 
            shortname="MAC04S1",
            version="002",
            description="MODIS/Aqua Aerosol 10km 5-Min L2 Wide Swath Subset along CloudSat V002 (MAC04S1) at GES DISC version: 002"
        )

    MAM04S0_V002_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_MAM04S0_002",
            provider="GES_DISC", 
            shortname="MAM04S0",
            version="002",
            description="MODIS/Aqua Aerosol 5-Min L2 Swath Subset 10km along MLS V002 (MAM04S0) at GES DISC version: 002"
        )

    MAC35S0_V002_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_MAC35S0_002",
            provider="GES_DISC", 
            shortname="MAC35S0",
            version="002",
            description="MODIS/Aqua CLD Mask Spect. Results 250m and 1km 5-Min L2 Narrow Swath Subset along CloudSat V002 (MAC35S0) at GES DISC version: 002"
        )

    MAC35S1_V002_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_MAC35S1_002",
            provider="GES_DISC", 
            shortname="MAC35S1",
            version="002",
            description="MODIS/Aqua CLD Mask Spect. Results 250m and 1km 5-Min L2 Wide Swath Subset along CloudSat V002 (MAC35S1) at GES DISC version: 002"
        )

    MAC021S0_V002_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_MAC021S0_002",
            provider="GES_DISC", 
            shortname="MAC021S0",
            version="002",
            description="MODIS/Aqua Calibrated Radiances 1km 5-Min 1B Narrow Swath Subset along CloudSat V002 (MAC021S0) at GES DISC version: 002"
        )

    MAC021S1_V002_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_MAC021S1_002",
            provider="GES_DISC", 
            shortname="MAC021S1",
            version="002",
            description="MODIS/Aqua Calibrated Radiances 1km 5-Min 1B Wide Swath Subset along CloudSat V002 (MAC021S1) at GES DISC version: 002"
        )

    MAC02QS0_V002_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_MAC02QS0_002",
            provider="GES_DISC", 
            shortname="MAC02QS0",
            version="002",
            description="MODIS/Aqua Calibrated Radiances 250m 5-Min L1B Narrow Swath Subset along CloudSat V002 (MAC02QS0) at GES DISC version: 002"
        )

    MAC02QS1_V002_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_MAC02QS1_002",
            provider="GES_DISC", 
            shortname="MAC02QS1",
            version="002",
            description="MODIS/Aqua Calibrated Radiances 250m 5-Min L1B Wide Swath Subset along CloudSat V002 (MAC02QS1) at GES DISC version: 002"
        )

    MAM35S0_V002_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_MAM35S0_002",
            provider="GES_DISC", 
            shortname="MAM35S0",
            version="002",
            description="MODIS/Aqua Cld Mask Spect. Test Results 5-Min L2 Swath Subset along MLS V002 (MAM35S0) at GES DISC version: 002"
        )

    MAC06S0_V002_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_MAC06S0_002",
            provider="GES_DISC", 
            shortname="MAC06S0",
            version="002",
            description="MODIS/Aqua Clouds 1km and 5km 5-Min L2 Narrow Swath Subset along CloudSat V002 (MAC06S0) at GES DISC version: 002"
        )

    MAM06S0_V002_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_MAM06S0_002",
            provider="GES_DISC", 
            shortname="MAM06S0",
            version="002",
            description="MODIS/Aqua Clouds 1km and 5km 5-Min L2 Swath Subset along MLS V002 (MAM06S0) at GES DISC version: 002"
        )

    MAC06S1_V002_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_MAC06S1_002",
            provider="GES_DISC", 
            shortname="MAC06S1",
            version="002",
            description="MODIS/Aqua Clouds 1km and 5km 5-Min L2 Wide Swath Subset along CloudSat V002 (MAC06S1) at GES DISC version: 002"
        )

    MAC03S0_V002_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_MAC03S0_002",
            provider="GES_DISC", 
            shortname="MAC03S0",
            version="002",
            description="MODIS/Aqua Geolocation Fields 1km 5-Min 1A Narrow Swath Subset along CloudSat V002 (MAC03S0) at GES DISC version: 002"
        )

    MAM03S0_V002_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_MAM03S0_002",
            provider="GES_DISC", 
            shortname="MAM03S0",
            version="002",
            description="MODIS/Aqua Geolocation Fields 1km 5-Min 1A Swath Subset along MLS V002 (MAM03S0) at GES DISC version: 002"
        )

    MAC03S1_V002_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_MAC03S1_002",
            provider="GES_DISC", 
            shortname="MAC03S1",
            version="002",
            description="MODIS/Aqua Geolocation Fields 1km 5-Min 1A Wide Swath Subset along CloudSat V002 (MAC03S1) at GES DISC version: 002"
        )

    MYDVI_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_MYDVI_005",
            provider="GES_DISC", 
            shortname="MYDVI",
            version="005",
            description="MODIS/Aqua Monthly Vegetation Indices Global 1x1 degree V005 (MYDVI) at GES DISC version: 005"
        )

    MYD11CM1D_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_MYD11CM1D_005",
            provider="GES_DISC", 
            shortname="MYD11CM1D",
            version="005",
            description="MODIS/Aqua Monthly mean Day-Time Land Surface Temperature at 1x1 degree V005 (MYD11CM1D) at GES DISC version: 005"
        )

    MYD11CM1N_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_MYD11CM1N_005",
            provider="GES_DISC", 
            shortname="MYD11CM1N",
            version="005",
            description="MODIS/Aqua Monthly mean Night-Time Land Surface Temperature at 1x1 degree V005 (MYD11CM1N) at GES DISC version: 005"
        )

    MAM07S0_V002_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_MAM07S0_002",
            provider="GES_DISC", 
            shortname="MAM07S0",
            version="002",
            description="MODIS/Aqua Temp and Water Vapor Profile 5-Min L2 Swath Subset 5km subset along MLS V002 (MAM07S0) at GES DISC version: 002"
        )

    MAC07S0_V002_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_MAC07S0_002",
            provider="GES_DISC", 
            shortname="MAC07S0",
            version="002",
            description="MODIS/Aqua Temp and Water Vapor Profiles 5km 5-Min L2 Narrow Swath Subset along CloudSat V002 (MAC07S0) at GES DISC version: 002"
        )

    MAC07S1_V002_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_MAC07S1_002",
            provider="GES_DISC", 
            shortname="MAC07S1",
            version="002",
            description="MODIS/Aqua Temp and Water Vapor Profiles 5km 5-Min L2 Wide Swath Subset along CloudSat V002 (MAC07S1) at GES DISC version: 002"
        )

    MAC05S0_V002_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_MAC05S0_002",
            provider="GES_DISC", 
            shortname="MAC05S0",
            version="002",
            description="MODIS/Aqua Total Precip Water Vapor 1km and 5km 5-Min L2 Narrow Swath Subset along CloudSat V002 (MAC05S0) at GES DISC version: 002"
        )

    MAM05S0_V002_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_MAM05S0_002",
            provider="GES_DISC", 
            shortname="MAM05S0",
            version="002",
            description="MODIS/Aqua Total Precip Water Vapor 1km and 5km 5-Min L2 Swath Subset along MLS V002 (MAM05S0) at GES DISC version: 002"
        )

    MAC05S1_V002_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_MAC05S1_002",
            provider="GES_DISC", 
            shortname="MAC05S1",
            version="002",
            description="MODIS/Aqua Total Precip Water Vapor 1km and 5km 5-Min L2 Wide Swath Subset along CloudSat V002 (MAC05S1) at GES DISC version: 002"
        )

    MOD14CM1_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_MOD14CM1_005",
            provider="GES_DISC", 
            shortname="MOD14CM1",
            version="005",
            description="MODIS/Terra 1 degree Gridded MODIS Active Fire Product V005 (MOD14CM1) at GES DISC version: 005"
        )

    MODVI_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_MODVI_005",
            provider="GES_DISC", 
            shortname="MODVI",
            version="005",
            description="MODIS/Terra Monthly Vegetation Indices Global 1x1 degree V005 (MODVI) at GES DISC version: 005"
        )

    MOD11CM1D_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_MOD11CM1D_005",
            provider="GES_DISC", 
            shortname="MOD11CM1D",
            version="005",
            description="MODIS/Terra Monthly mean Day-Time Land Surface Temperature at 1x1 degree V005 (MOD11CM1D) at GES DISC version: 005"
        )

    MOD11CM1N_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_MOD11CM1N_005",
            provider="GES_DISC", 
            shortname="MOD11CM1N",
            version="005",
            description="MODIS/Terra Monthly mean Night-Time Land Surface Temperature at 1x1 degree V005 (MOD11CM1N) at GES DISC version: 005"
        )

    MODIS_CR_EQUAL_ANGLE_3H_V10_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_MODIS_CR_Equal_Angle_3h_1.0",
            provider="GES_DISC", 
            shortname="MODIS_CR_Equal_Angle_3h",
            version="1.0",
            description="MODIS_CR_Equal_Angle_3h version: 1.0"
        )

    MODIS_CR_EQUAL_ANGLE_DAILY_V10_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_MODIS_CR_Equal_Angle_Daily_1.0",
            provider="GES_DISC", 
            shortname="MODIS_CR_Equal_Angle_Daily",
            version="1.0",
            description="MODIS_CR_Equal_Angle_Daily version: 1.0"
        )

    MODIS_CR_EQUAL_AREA_3H_V10_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_MODIS_CR_Equal_Area_3h_1.0",
            provider="GES_DISC", 
            shortname="MODIS_CR_Equal_Area_3h",
            version="1.0",
            description="MODIS_CR_Equal_Area_3h version: 1.0"
        )

    MRIRN2IM_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_MRIRN2IM_001",
            provider="GES_DISC", 
            shortname="MRIRN2IM",
            version="001",
            description="MRIR/Nimbus-2 Images of Daytime Brightness Temperature on 4 x 5 inch Film Sheets V001 (MRIRN2IM) at GES DISC version: 001"
        )

    MRIRN2L1_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_MRIRN2L1_001",
            provider="GES_DISC", 
            shortname="MRIRN2L1",
            version="001",
            description="MRIR/Nimbus-2 Level 1 Meteorological Radiation Data V001 (MRIRN2L1) at GES DISC version: 001"
        )

    MRIRN3IM_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_MRIRN3IM_001",
            provider="GES_DISC", 
            shortname="MRIRN3IM",
            version="001",
            description="MRIR/Nimbus-3 Images of Daytime Brightness Temperature on 4 x 5 inch Film Sheets V001 (MRIRN3IM) at GES DISC version: 001"
        )

    MRIRN3L1_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_MRIRN3L1_001",
            provider="GES_DISC", 
            shortname="MRIRN3L1",
            version="001",
            description="MRIR/Nimbus-3 Level 1 Meteorological Radiation Data V001 (MRIRN3L1) at GES DISC version: 001"
        )

    MSAQSO2L4_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_MSAQSO2L4_1",
            provider="GES_DISC", 
            shortname="MSAQSO2L4",
            version="1",
            description="MSAQSO2L4 version 1 is superseded by newer version, DOI: 10.5067/MEASURES/SO2/DATA406 version: 1"
        )

    MSULTT_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_MSULTT_001",
            provider="GES_DISC", 
            shortname="MSULTT",
            version="001",
            description="MSU Ch 2/3 Daily Lower Troposphere Temps with Limb93 Correction L3 1 day 2.5 degree x 2.5 degree V001 (MSULTT) at GES DISC version: 001"
        )

    MSUUTT_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_MSUUTT_001",
            provider="GES_DISC", 
            shortname="MSUUTT",
            version="001",
            description="MSU Ch 3/4 Daily Upper Troposphere Temps with Limb93 Correction V001 L3 1 day 2.5 degree x 2.5 degree (MSUUTT) at GES DISC version: 001"
        )

    MSULST_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_MSULST_001",
            provider="GES_DISC", 
            shortname="MSULST",
            version="001",
            description="MSU Ch 4 Daily Lower Stratosphere Temps with Limb93 Correction L3 1 day 2.5 degree x 2.5 degree V001 (MSULST) at GES DISC version: 001"
        )

    MSUOP_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_MSUOP_001",
            provider="GES_DISC", 
            shortname="MSUOP",
            version="001",
            description="MSU Daily Oceanic Precipitation with Limb93 Correction L3 1 day 2.5 degree x 2.5 degree V001 (MSUOP) at GES DISC version: 001"
        )

    CMS_CH4_FLX_CA_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_CMS_CH4_FLX_CA_1",
            provider="GES_DISC", 
            shortname="CMS_CH4_FLX_CA",
            version="1",
            description="Methane (CH4) Flux for Canadian Oil/Gas Systems L4 V1 (CMS_CH4_FLX_CA) at GES DISC version: 1"
        )

    CMS_CH4_FLX_MX_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_CMS_CH4_FLX_MX_1",
            provider="GES_DISC", 
            shortname="CMS_CH4_FLX_MX",
            version="1",
            description="Methane (CH4) Flux for Mexican Oil/Gas Systems L4 V1 (CMS_CH4_FLX_MX) at GES DISC version: 1"
        )

    CMS_CH4_FLX_NAD_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_CMS_CH4_FLX_NAD_1",
            provider="GES_DISC", 
            shortname="CMS_CH4_FLX_NAD",
            version="1",
            description="Methane (CH4) Flux for North America L4 Daily V1 (CMS_CH4_FLX_NAD) at GES DISC version: 1"
        )

    MICASA_FLUX_3H_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_MICASA_FLUX_3H_1",
            provider="GES_DISC", 
            shortname="MICASA_FLUX_3H",
            version="1",
            description="MiCASA 3-hourly NPP NEE Fluxes 0.1 degree x 0.1 degree version: 1"
        )

    MICASA_FLUX_D_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_MICASA_FLUX_D_1",
            provider="GES_DISC", 
            shortname="MICASA_FLUX_D",
            version="1",
            description="MiCASA Daily NPP Rh ATMC NEE FIRE FUEL Fluxes 0.1 degree x 0.1 degree version: 1"
        )

    MICASA_FLUX_M_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_MICASA_FLUX_M_1",
            provider="GES_DISC", 
            shortname="MICASA_FLUX_M",
            version="1",
            description="MiCASA Monthly NPP Rh ATMC NEE FIRE FUEL Fluxes 0.1 degree x 0.1 degree version: 1"
        )

    ACOSMONTHLYGRIDDEDXCO2_V3_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_ACOSMonthlyGriddedXCO2_3",
            provider="GES_DISC", 
            shortname="ACOSMonthlyGriddedXCO2",
            version="3",
            description="Monthly Gridded Level 4 bias-corrected XCO2 and other select fields aggregated from ACOS as Level 4 monthly files V3 (ACOSMonthlyGriddedXCO2) version: 3"
        )

    MULTIINSTRUMENTFUSEDXCO2_V4_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_MultiInstrumentFusedXCO2_4",
            provider="GES_DISC", 
            shortname="MultiInstrumentFusedXCO2",
            version="4",
            description="Multi-Instrument Fused bias-corrected XCO2 and other select fields aggregated as Level 3 daily files V4 (MultiInstrumentFusedXCO2) version: 4"
        )

    MULTIINSTRUMENTFUSEDXCO2_V3_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_MultiInstrumentFusedXCO2_3",
            provider="GES_DISC", 
            shortname="MultiInstrumentFusedXCO2",
            version="3",
            description="Multi-Instrument Fused bias-corrected XCO2 and other select fields aggregated as Level 4 daily files V3 (MultiInstrumentFusedXCO2) version: 3"
        )

    MSAQSO2L4_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_MSAQSO2L4_2",
            provider="GES_DISC", 
            shortname="MSAQSO2L4",
            version="2",
            description="Multi-Satellite Air Quality Sulfur Dioxide (SO2) Database Long-Term L4 Global V2 (MSAQSO2L4) at GES DISC version: 2"
        )

    MSLERLSTL3ZM_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_MSLERLSTL3zm_1",
            provider="GES_DISC", 
            shortname="MSLERLSTL3zm",
            version="1",
            description="Multi-Satellite Lambertian Equivalent Reflectivity (Local Satellite Time) 1 day L3 Global 5.0deg Lat Zones V1 (MSLERLSTL3zm) at GES DISC version: 1"
        )

    MSLERLSTL3D10_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_MSLERLSTL3d10_1",
            provider="GES_DISC", 
            shortname="MSLERLSTL3d10",
            version="1",
            description="Multi-Satellite Lambertian Equivalent Reflectivity (Local Satellite Time) 10-Day L3 Global 2.0x5.0deg Lat/Lon Grid V1 (MSLERLSTL3d10) at GES DISC version: 1"
        )

    MSLERNNL3ZM_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_MSLERNNL3zm_1",
            provider="GES_DISC", 
            shortname="MSLERNNL3zm",
            version="1",
            description="Multi-Satellite Lambertian Equivalent Reflectivity (Noon Normalized) 1 day L3 Global 5.0deg Lat Zones V1 (MSLERNNL3zm) at GES DISC version: 1"
        )

    MSLERNNL3D10_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_MSLERNNL3d10_1",
            provider="GES_DISC", 
            shortname="MSLERNNL3d10",
            version="1",
            description="Multi-Satellite Lambertian Equivalent Reflectivity (Noon Normalized) 10-Day L3 Global 2.0x5.0deg Lat/Lon Grid V1 (MSLERNNL3d10) at GES DISC version: 1"
        )

    MSO3L3ZM5_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_MSO3L3zm5_1",
            provider="GES_DISC", 
            shortname="MSO3L3zm5",
            version="1",
            description="Multi-Satellite Merged Ozone (O3) Profile and Total Column 1 Month Zonal Mean L3 Global 5.0 degree Latitude Zones V1 (MSO3L3zm5) at GES DISC version: 1"
        )

    MSVOLSO2L4_V4_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_MSVOLSO2L4_4",
            provider="GES_DISC", 
            shortname="MSVOLSO2L4",
            version="4",
            description="Multi-Satellite Volcanic Sulfur Dioxide L4 Long-Term Global Database V4 (MSVOLSO2L4) at GES DISC version: 4"
        )

    MACLWP_DIURNAL_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_MACLWP_diurnal_1",
            provider="GES_DISC", 
            shortname="MACLWP_diurnal",
            version="1",
            description="Multisensor Advanced Climatology Mean Liquid Water Path Diurnal Cycle L3 Monthly 1 degree x 1 degree V1 (MACLWP_diurnal) at GES DISC version: 1"
        )

    MACLWP_MEAN_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_MACLWP_mean_1",
            provider="GES_DISC", 
            shortname="MACLWP_mean",
            version="1",
            description="Multisensor Advanced Climatology Mean Liquid Water Path L3 Monthly 1 degree X 1 degree V1 (MACLWP_mean) at GES DISC version: 1"
        )

    MACTWP_MEAN_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_MACTWP_mean_1",
            provider="GES_DISC", 
            shortname="MACTWP_mean",
            version="1",
            description="Multisensor Advanced Climatology Total Liquid Water Path L3 Monthly 1 degree x 1 degree V1 (MACTWP_mean) at GES DISC version: 1"
        )

    NEWS_WEB_ACLIM_V10_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_NEWS_WEB_ACLIM_1.0",
            provider="GES_DISC", 
            shortname="NEWS_WEB_ACLIM",
            version="1.0",
            description="NASA Energy and Water cycle Study (NEWS) Annual Climatology of the 1st decade of the 21st Century V1.0 (NEWS_WEB_ACLIM) at GES DISC version: 1.0"
        )

    NEWS_WEB_MCLIM_V10_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_NEWS_WEB_MCLIM_1.0",
            provider="GES_DISC", 
            shortname="NEWS_WEB_MCLIM",
            version="1.0",
            description="NASA Energy and Water cycle Study (NEWS) Monthly Climatology of the 1st decade of the 21st Century V1.0 (NEWS_WEB_MCLIM) at GES DISC version: 1.0"
        )

    PRECIP_AMSR2_GCOMW1_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_PRECIP_AMSR2_GCOMW1_1",
            provider="GES_DISC", 
            shortname="PRECIP_AMSR2_GCOMW1",
            version="1",
            description="NASA MEASURES Precipitation Ensemble based on AMSR2 GCOMW1 NASA PPS L1C V05 TBs 1-orbit L2 Swath 10x10km V1 (PRECIP_AMSR2_GCOMW1) at GES DISC version: 1"
        )

    PRECIP_AMSRE_AQUA_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_PRECIP_AMSRE_AQUA_1",
            provider="GES_DISC", 
            shortname="PRECIP_AMSRE_AQUA",
            version="1",
            description="NASA MEASURES Precipitation Ensemble based on AMSRE AQUA NASA PPS L1C V05 Tbs 1-orbit L2 Swath 12x12km V1 (PRECIP_AMSRE_AQUA) at GES DISC version: 1"
        )

    PRECIP_GMI_GPM_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_PRECIP_GMI_GPM_1",
            provider="GES_DISC", 
            shortname="PRECIP_GMI_GPM",
            version="1",
            description="NASA MEASURES Precipitation Ensemble based on GMI GPM NASA PPS L1C V05 Tbs 1-orbit L2 Swath 10x10km V1 (PRECIP_GMI_GPM) at GES DISC version: 1"
        )

    PRECIP_SMMR_NIMBUS7_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_PRECIP_SMMR_NIMBUS7_1",
            provider="GES_DISC", 
            shortname="PRECIP_SMMR_NIMBUS7",
            version="1",
            description="NASA MEASURES Precipitation Ensemble based on SMMR Nimbus-7 NSIDC L1B Tbs 1-orbit L2 Swath 25x25km V1 (PRECIP_SMMR_NIMBUS7) at GES DISC version: 1"
        )

    PRECIP_SSMI_F08_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_PRECIP_SSMI_F08_1",
            provider="GES_DISC", 
            shortname="PRECIP_SSMI_F08",
            version="1",
            description="NASA MEASURES Precipitation Ensemble based on SSM/I DMSP F08 NASA PPS L1C V06 Tbs 1-orbit L2 Swath 12x12km V1 (PRECIP_SSMI_F08) at GES DISC version: 1"
        )

    PRECIP_SSMI_F10_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_PRECIP_SSMI_F10_1",
            provider="GES_DISC", 
            shortname="PRECIP_SSMI_F10",
            version="1",
            description="NASA MEASURES Precipitation Ensemble based on SSM/I DMSP F10 NASA PPS L1C V06 Tbs 1-orbit L2 Swath 12x12km V1 (PRECIP_SSMI_F10) at GES DISC version: 1"
        )

    PRECIP_SSMI_F11_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_PRECIP_SSMI_F11_1",
            provider="GES_DISC", 
            shortname="PRECIP_SSMI_F11",
            version="1",
            description="NASA MEASURES Precipitation Ensemble based on SSM/I DMSP F11 NASA PPS L1C V06 Tbs 1-orbit L2 Swath 12x12km V1 (PRECIP_SSMI_F11) at GES DISC version: 1"
        )

    PRECIP_SSMI_F13_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_PRECIP_SSMI_F13_1",
            provider="GES_DISC", 
            shortname="PRECIP_SSMI_F13",
            version="1",
            description="NASA MEASURES Precipitation Ensemble based on SSM/I DMSP F13 NASA PPS L1C V06 Tbs 1-orbit L2 Swath 12x12km V1 (PRECIP_SSMI_F13) at GES DISC version: 1"
        )

    PRECIP_SSMI_F14_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_PRECIP_SSMI_F14_1",
            provider="GES_DISC", 
            shortname="PRECIP_SSMI_F14",
            version="1",
            description="NASA MEASURES Precipitation Ensemble based on SSM/I DMSP F14 NASA PPS L1C V06 Tbs 1-orbit L2 Swath 12x12km V1 (PRECIP_SSMI_F14) at GES DISC version: 1"
        )

    PRECIP_SSMI_F15_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_PRECIP_SSMI_F15_1",
            provider="GES_DISC", 
            shortname="PRECIP_SSMI_F15",
            version="1",
            description="NASA MEASURES Precipitation Ensemble based on SSM/I DMSP F15 NASA PPS L1C V06 Tbs 1-orbit L2 Swath 12x12km V1 (PRECIP_SSMI_F15) at GES DISC version: 1"
        )

    PRECIP_SSMIS_F16_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_PRECIP_SSMIS_F16_1",
            provider="GES_DISC", 
            shortname="PRECIP_SSMIS_F16",
            version="1",
            description="NASA MEASURES Precipitation Ensemble based on SSMIS DMSP F16 NASA PPS L1C V05 Tbs 1-orbit L2 Swath 12x12km V1 (PRECIP_SSMIS_F16) at GES DISC version: 1"
        )

    PRECIP_SSMIS_F17_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_PRECIP_SSMIS_F17_1",
            provider="GES_DISC", 
            shortname="PRECIP_SSMIS_F17",
            version="1",
            description="NASA MEASURES Precipitation Ensemble based on SSMIS DMSP F17 NASA PPS L1C V05 Tbs 1-orbit L2 Swath 12x12km V1 (PRECIP_SSMIS_F17) at GES DISC version: 1"
        )

    PRECIP_SSMIS_F18_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_PRECIP_SSMIS_F18_1",
            provider="GES_DISC", 
            shortname="PRECIP_SSMIS_F18",
            version="1",
            description="NASA MEASURES Precipitation Ensemble based on SSMIS DMSP F18 NASA PPS L1C V05 Tbs 1-orbit L2 Swath 12x12km V1 (PRECIP_SSMIS_F18) at GES DISC version: 1"
        )

    PRECIP_SSMIS_F19_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_PRECIP_SSMIS_F19_1",
            provider="GES_DISC", 
            shortname="PRECIP_SSMIS_F19",
            version="1",
            description="NASA MEASURES Precipitation Ensemble based on SSMIS DMSP F19 NASA PPS L1C V05 Tbs 1-orbit L2 Swath 12x12km V1 (PRECIP_SSMIS_F19) at GES DISC version: 1"
        )

    PRECIP_TMI_TRMM_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_PRECIP_TMI_TRMM_1",
            provider="GES_DISC", 
            shortname="PRECIP_TMI_TRMM",
            version="1",
            description="NASA MEASURES Precipitation Ensemble based on TMI TRMM NASA PPS L1C V05 Tbs 1-orbit L2 Swath 5x5km V1 (PRECIP_TMI_TRMM) at GES DISC version: 1"
        )

    NOBM_DAY_VR2017_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_NOBM_DAY_R2017",
            provider="GES_DISC", 
            shortname="NOBM_DAY",
            version="R2017",
            description="NASA Ocean Biogeochemical Model assimilating satellite chlorophyll data global daily VR2017 (NOBM_DAY) at GES DISC version: R2017"
        )

    NOBM_MON_VR2017_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_NOBM_MON_R2017",
            provider="GES_DISC", 
            shortname="NOBM_MON",
            version="R2017",
            description="NASA Ocean Biogeochemical Model assimilating satellite chlorophyll data global monthly VR2017 (NOBM_MON) at GES DISC version: R2017"
        )

    NCALDAS_NOAH0125_D_V20_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_NCALDAS_NOAH0125_D_2.0",
            provider="GES_DISC", 
            shortname="NCALDAS_NOAH0125_D",
            version="2.0",
            description="NCA-LDAS Noah-3.3 Land Surface Model L4 Daily 0.125 x 0.125 degree V2.0 (NCALDAS_NOAH0125_D) at GES DISC version: 2.0"
        )

    NCALDAS_NOAH0125_TRENDS_V20_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_NCALDAS_NOAH0125_Trends_2.0",
            provider="GES_DISC", 
            shortname="NCALDAS_NOAH0125_Trends",
            version="2.0",
            description="NCA-LDAS Noah-3.3 Land Surface Model L4 Trends 0.125 x 0.125 degree V2.0 (NCALDAS_NOAH0125_Trends) at GES DISC version: 2.0"
        )

    GPM_MERGIR_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GPM_MERGIR_1",
            provider="GES_DISC", 
            shortname="GPM_MERGIR",
            version="1",
            description="NCEP/CPC L3 Half Hourly 4km Global (60S - 60N) Merged IR V1 (GPM_MERGIR) at GES DISC version: 1"
        )

    GSSTF_NCEP_V2C_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GSSTF_NCEP_2c",
            provider="GES_DISC", 
            shortname="GSSTF_NCEP",
            version="2c",
            description="NCEP/DOE Reanalysis II in HDF-EOS5, for GSSTF2c, 1x1 deg Daily grid V2c (GSSTF_NCEP) at GES DISC version: 2c"
        )

    GSSTFM_NCEP_V2C_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GSSTFM_NCEP_2c",
            provider="GES_DISC", 
            shortname="GSSTFM_NCEP",
            version="2c",
            description="NCEP/DOE Reanalysis II in HDF-EOS5, for GSSTF2c, 1x1 deg Monthly grid V2c (GSSTFM_NCEP) at GES DISC version: 2c"
        )

    GSSTF_NCEP_V3_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GSSTF_NCEP_3",
            provider="GES_DISC", 
            shortname="GSSTF_NCEP",
            version="3",
            description="NCEP/DOE Reanalysis II, for GSSTF, 0.25 x 0.25 deg, Daily Grid V3 (GSSTF_NCEP) at GES DISC version: 3"
        )

    GSSTFM_NCEP_V3_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_GSSTFM_NCEP_3",
            provider="GES_DISC", 
            shortname="GSSTFM_NCEP",
            version="3",
            description="NCEP/DOE Reanalysis II, for GSSTF, 0.25x0.25 deg, Monthly grid V3 (GSSTFM_NCEP) at GES DISC version: 3"
        )

    NEMSN5L2_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_NEMSN5L2_001",
            provider="GES_DISC", 
            shortname="NEMSN5L2",
            version="001",
            description="NEMS/Nimbus-5 Level 2 Output Data V001 (NEMSN5L2) at GES DISC version: 001"
        )

    NLDAS_MOS0125_H_V002_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_NLDAS_MOS0125_H_002",
            provider="GES_DISC", 
            shortname="NLDAS_MOS0125_H",
            version="002",
            description="NLDAS Mosaic Land Surface Model L4 Hourly 0.125 x 0.125 degree V002 (NLDAS_MOS0125_H) at GES DISC version: 002"
        )

    NLDAS_MOS0125_H_V20_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_NLDAS_MOS0125_H_2.0",
            provider="GES_DISC", 
            shortname="NLDAS_MOS0125_H",
            version="2.0",
            description="NLDAS Mosaic Land Surface Model L4 Hourly 0.125 x 0.125 degree V2.0 (NLDAS_MOS0125_H) at GES DISC version: 2.0"
        )

    NLDAS_MOS0125_M_V002_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_NLDAS_MOS0125_M_002",
            provider="GES_DISC", 
            shortname="NLDAS_MOS0125_M",
            version="002",
            description="NLDAS Mosaic Land Surface Model L4 Monthly 0.125 x 0.125 degree V002 (NLDAS_MOS0125_M) at GES DISC version: 002"
        )

    NLDAS_MOS0125_M_V20_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_NLDAS_MOS0125_M_2.0",
            provider="GES_DISC", 
            shortname="NLDAS_MOS0125_M",
            version="2.0",
            description="NLDAS Mosaic Land Surface Model L4 Monthly 0.125 x 0.125 degree V2.0 (NLDAS_MOS0125_M) at GES DISC version: 2.0"
        )

    NLDAS_MOS0125_MC_V002_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_NLDAS_MOS0125_MC_002",
            provider="GES_DISC", 
            shortname="NLDAS_MOS0125_MC",
            version="002",
            description="NLDAS Mosaic Land Surface Model L4 Monthly Climatology 0.125 x 0.125 degree V002 (NLDAS_MOS0125_MC) at GES DISC version: 002"
        )

    NLDAS_MOS0125_MC_V20_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_NLDAS_MOS0125_MC_2.0",
            provider="GES_DISC", 
            shortname="NLDAS_MOS0125_MC",
            version="2.0",
            description="NLDAS Mosaic Land Surface Model L4 Monthly Climatology 0.125 x 0.125 degree V2.0 (NLDAS_MOS0125_MC) at GES DISC version: 2.0"
        )

    NLDAS_NOAH0125_H_V002_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_NLDAS_NOAH0125_H_002",
            provider="GES_DISC", 
            shortname="NLDAS_NOAH0125_H",
            version="002",
            description="NLDAS Noah Land Surface Model L4 Hourly 0.125 x 0.125 degree V002 (NLDAS_NOAH0125_H) at GES DISC version: 002"
        )

    NLDAS_NOAH0125_H_V20_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_NLDAS_NOAH0125_H_2.0",
            provider="GES_DISC", 
            shortname="NLDAS_NOAH0125_H",
            version="2.0",
            description="NLDAS Noah Land Surface Model L4 Hourly 0.125 x 0.125 degree V2.0 (NLDAS_NOAH0125_H) at GES DISC version: 2.0"
        )

    NLDAS_NOAH0125_M_V002_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_NLDAS_NOAH0125_M_002",
            provider="GES_DISC", 
            shortname="NLDAS_NOAH0125_M",
            version="002",
            description="NLDAS Noah Land Surface Model L4 Monthly 0.125 x 0.125 degree V002 (NLDAS_NOAH0125_M) at GES DISC version: 002"
        )

    NLDAS_NOAH0125_M_V20_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_NLDAS_NOAH0125_M_2.0",
            provider="GES_DISC", 
            shortname="NLDAS_NOAH0125_M",
            version="2.0",
            description="NLDAS Noah Land Surface Model L4 Monthly 0.125 x 0.125 degree V2.0 (NLDAS_NOAH0125_M) at GES DISC version: 2.0"
        )

    NLDAS_NOAH0125_MC_V002_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_NLDAS_NOAH0125_MC_002",
            provider="GES_DISC", 
            shortname="NLDAS_NOAH0125_MC",
            version="002",
            description="NLDAS Noah Land Surface Model L4 Monthly Climatology 0.125 x 0.125 degree V002 (NLDAS_NOAH0125_MC) at GES DISC version: 002"
        )

    NLDAS_NOAH0125_MC_V20_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_NLDAS_NOAH0125_MC_2.0",
            provider="GES_DISC", 
            shortname="NLDAS_NOAH0125_MC",
            version="2.0",
            description="NLDAS Noah Land Surface Model L4 Monthly Climatology 0.125 x 0.125 degree V2.0 (NLDAS_NOAH0125_MC) at GES DISC version: 2.0"
        )

    NLDAS_FORA0125_H_V002_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_NLDAS_FORA0125_H_002",
            provider="GES_DISC", 
            shortname="NLDAS_FORA0125_H",
            version="002",
            description="NLDAS Primary Forcing Data L4 Hourly 0.125 x 0.125 degree V002 (NLDAS_FORA0125_H) at GES DISC version: 002"
        )

    NLDAS_FORA0125_H_V20_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_NLDAS_FORA0125_H_2.0",
            provider="GES_DISC", 
            shortname="NLDAS_FORA0125_H",
            version="2.0",
            description="NLDAS Primary Forcing Data L4 Hourly 0.125 x 0.125 degree V2.0 (NLDAS_FORA0125_H) at GES DISC version: 2.0"
        )

    NLDAS_FORA0125_M_V002_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_NLDAS_FORA0125_M_002",
            provider="GES_DISC", 
            shortname="NLDAS_FORA0125_M",
            version="002",
            description="NLDAS Primary Forcing Data L4 Monthly 0.125 x 0.125 degree V002 (NLDAS_FORA0125_M) at GES DISC version: 002"
        )

    NLDAS_FORA0125_M_V20_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_NLDAS_FORA0125_M_2.0",
            provider="GES_DISC", 
            shortname="NLDAS_FORA0125_M",
            version="2.0",
            description="NLDAS Primary Forcing Data L4 Monthly 0.125 x 0.125 degree V2.0 (NLDAS_FORA0125_M) at GES DISC version: 2.0"
        )

    NLDAS_FORA0125_MC_V002_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_NLDAS_FORA0125_MC_002",
            provider="GES_DISC", 
            shortname="NLDAS_FORA0125_MC",
            version="002",
            description="NLDAS Primary Forcing Data L4 Monthly Climatology 0.125 x 0.125 degree V002 (NLDAS_FORA0125_MC) at GES DISC version: 002"
        )

    NLDAS_FORA0125_MC_V20_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_NLDAS_FORA0125_MC_2.0",
            provider="GES_DISC", 
            shortname="NLDAS_FORA0125_MC",
            version="2.0",
            description="NLDAS Primary Forcing Data L4 Monthly Climatology 0.125 x 0.125 degree V2.0 (NLDAS_FORA0125_MC) at GES DISC version: 2.0"
        )

    NLDAS_FORB0125_H_V002_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_NLDAS_FORB0125_H_002",
            provider="GES_DISC", 
            shortname="NLDAS_FORB0125_H",
            version="002",
            description="NLDAS Secondary Forcing Data L4 Hourly 0.125 x 0.125 degree V002 (NLDAS_FORB0125_H) at GES DISC version: 002"
        )

    NLDAS_FORB0125_H_V20_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_NLDAS_FORB0125_H_2.0",
            provider="GES_DISC", 
            shortname="NLDAS_FORB0125_H",
            version="2.0",
            description="NLDAS Secondary Forcing Data L4 Hourly 0.125 x 0.125 degree V2.0 (NLDAS_FORB0125_H) at GES DISC version: 2.0"
        )

    NLDAS_FORB0125_M_V002_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_NLDAS_FORB0125_M_002",
            provider="GES_DISC", 
            shortname="NLDAS_FORB0125_M",
            version="002",
            description="NLDAS Secondary Forcing Data L4 Monthly 0.125 x 0.125 degree V002 (NLDAS_FORB0125_M) at GES DISC version: 002"
        )

    NLDAS_FORB0125_M_V20_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_NLDAS_FORB0125_M_2.0",
            provider="GES_DISC", 
            shortname="NLDAS_FORB0125_M",
            version="2.0",
            description="NLDAS Secondary Forcing Data L4 Monthly 0.125 x 0.125 degree V2.0 (NLDAS_FORB0125_M) at GES DISC version: 2.0"
        )

    NLDAS_FORB0125_MC_V002_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_NLDAS_FORB0125_MC_002",
            provider="GES_DISC", 
            shortname="NLDAS_FORB0125_MC",
            version="002",
            description="NLDAS Secondary Forcing Data L4 Monthly Climatology 0.125 x 0.125 degree V002 (NLDAS_FORB0125_MC) at GES DISC version: 002"
        )

    NLDAS_FORB0125_MC_V20_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_NLDAS_FORB0125_MC_2.0",
            provider="GES_DISC", 
            shortname="NLDAS_FORB0125_MC",
            version="2.0",
            description="NLDAS Secondary Forcing Data L4 Monthly Climatology 0.125 x 0.125 degree V2.0 (NLDAS_FORB0125_MC) at GES DISC version: 2.0"
        )

    NLDAS_VIC0125_H_V002_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_NLDAS_VIC0125_H_002",
            provider="GES_DISC", 
            shortname="NLDAS_VIC0125_H",
            version="002",
            description="NLDAS VIC Land Surface Model L4 Hourly 0.125 x 0.125 degree V002 (NLDAS_VIC0125_H) at GES DISC version: 002"
        )

    NLDAS_VIC0125_H_V20_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_NLDAS_VIC0125_H_2.0",
            provider="GES_DISC", 
            shortname="NLDAS_VIC0125_H",
            version="2.0",
            description="NLDAS VIC Land Surface Model L4 Hourly 0.125 x 0.125 degree V2.0 (NLDAS_VIC0125_H) at GES DISC version: 2.0"
        )

    NLDAS_VIC0125_M_V002_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_NLDAS_VIC0125_M_002",
            provider="GES_DISC", 
            shortname="NLDAS_VIC0125_M",
            version="002",
            description="NLDAS VIC Land Surface Model L4 Monthly 0.125 x 0.125 degree V002 (NLDAS_VIC0125_M) at GES DISC version: 002"
        )

    NLDAS_VIC0125_M_V20_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_NLDAS_VIC0125_M_2.0",
            provider="GES_DISC", 
            shortname="NLDAS_VIC0125_M",
            version="2.0",
            description="NLDAS VIC Land Surface Model L4 Monthly 0.125 x 0.125 degree V2.0 (NLDAS_VIC0125_M) at GES DISC version: 2.0"
        )

    NLDAS_VIC0125_MC_V002_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_NLDAS_VIC0125_MC_002",
            provider="GES_DISC", 
            shortname="NLDAS_VIC0125_MC",
            version="002",
            description="NLDAS VIC Land Surface Model L4 Monthly Climatology 0.125 x 0.125 degree V002 (NLDAS_VIC0125_MC) at GES DISC version: 002"
        )

    NLDAS_VIC0125_MC_V20_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_NLDAS_VIC0125_MC_2.0",
            provider="GES_DISC", 
            shortname="NLDAS_VIC0125_MC",
            version="2.0",
            description="NLDAS VIC Land Surface Model L4 Monthly Climatology 0.125 x 0.125 degree V2.0 (NLDAS_VIC0125_MC) at GES DISC version: 2.0"
        )

    SFC_NITROGEN_DIOXIDE_CONC_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SFC_NITROGEN_DIOXIDE_CONC_1",
            provider="GES_DISC", 
            shortname="SFC_NITROGEN_DIOXIDE_CONC",
            version="1",
            description="Nitrogen Dioxide Surface-Level Annual Average Concentrations V1 (SFC_NITROGEN_DIOXIDE_CONC) at GES DISC version: 1"
        )

    NHICEM_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_NHICEM_001",
            provider="GES_DISC", 
            shortname="NHICEM",
            version="001",
            description="Northern Hemisphere Ice Cover Monthly Statistics at 1 Degree Resolution V001 (NHICEM) at GES DISC version: 001"
        )

    NHSNOWM_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_NHSNOWM_001",
            provider="GES_DISC", 
            shortname="NHSNOWM",
            version="001",
            description="Northern Hemisphere Snow Cover Monthly Statistics at 1 Degree Resolution V001 (NHSNOWM) at GES DISC version: 001"
        )

    OCO2_GEOS_L3CO2_DAY_V10R_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO2_GEOS_L3CO2_DAY_10r",
            provider="GES_DISC", 
            shortname="OCO2_GEOS_L3CO2_DAY",
            version="10r",
            description="OCO-2 GEOS Level 3 daily, 0.5x0.625 assimilated CO2 V10r (OCO2_GEOS_L3CO2_DAY) at GES DISC version: 10r"
        )

    OCO2_GEOS_L3CO2_MONTH_V10R_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO2_GEOS_L3CO2_MONTH_10r",
            provider="GES_DISC", 
            shortname="OCO2_GEOS_L3CO2_MONTH",
            version="10r",
            description="OCO-2 GEOS Level 3 monthly, 0.5x0.625 assimilated CO2 V10r (OCO2_GEOS_L3CO2_MONTH) at GES DISC version: 10r"
        )

    OCO2GRIDDEDXCO2_V4_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO2GriddedXCO2_4",
            provider="GES_DISC", 
            shortname="OCO2GriddedXCO2",
            version="4",
            description="OCO-2 Gridded bias-corrected XCO2 and other select fields aggregated as Level 3 daily files V4 (OCO2GriddedXCO2) version: 4"
        )

    OCO2GRIDDEDXCO2_V3_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO2GriddedXCO2_3",
            provider="GES_DISC", 
            shortname="OCO2GriddedXCO2",
            version="3",
            description="OCO-2 Gridded bias-corrected XCO2 and other select fields aggregated as Level 4 daily files V3 (OCO2GriddedXCO2) version: 3"
        )

    OCO2GRIDDEDXCO2_SIF_V4_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO2GriddedXCO2_SIF_4",
            provider="GES_DISC", 
            shortname="OCO2GriddedXCO2_SIF",
            version="4",
            description="OCO-2 Gridded bias-corrected XCO2, SIF, and other select fields aggregated as Level 3 daily files V4 (OCO2GriddedXCO2_SIF) version: 4"
        )

    OCO2_ATT_V10_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO2_Att_10",
            provider="GES_DISC", 
            shortname="OCO2_Att",
            version="10",
            description="OCO-2 Level 0 spacecraft attitude data V10 (OCO2_Att) at GES DISC version: 10"
        )

    OCO2_ATT_V11_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO2_Att_11",
            provider="GES_DISC", 
            shortname="OCO2_Att",
            version="11",
            description="OCO-2 Level 0 spacecraft attitude data V11 (OCO2_Att) at GES DISC version: 11"
        )

    OCO2_ATT_V112_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO2_Att_11.2",
            provider="GES_DISC", 
            shortname="OCO2_Att",
            version="11.2",
            description="OCO-2 Level 0 spacecraft attitude data V11.2 (OCO2_Att) at GES DISC version: 11.2"
        )

    OCO2_ATT_V10R_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO2_Att_10r",
            provider="GES_DISC", 
            shortname="OCO2_Att",
            version="10r",
            description="OCO-2 Level 0 spacecraft attitude data, Retrospective Processing V10r (OCO2_Att) at GES DISC version: 10r"
        )

    OCO2_ATT_V11R_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO2_Att_11r",
            provider="GES_DISC", 
            shortname="OCO2_Att",
            version="11r",
            description="OCO-2 Level 0 spacecraft attitude data, Retrospective Processing V11r (OCO2_Att) at GES DISC version: 11r"
        )

    OCO2_EPH_V10_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO2_Eph_10",
            provider="GES_DISC", 
            shortname="OCO2_Eph",
            version="10",
            description="OCO-2 Level 0 spacecraft ephemerides V10 (OCO2_Eph) at GES DISC version: 10"
        )

    OCO2_EPH_V11_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO2_Eph_11",
            provider="GES_DISC", 
            shortname="OCO2_Eph",
            version="11",
            description="OCO-2 Level 0 spacecraft ephemerides V11 (OCO2_Eph) at GES DISC version: 11"
        )

    OCO2_EPH_V112_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO2_Eph_11.2",
            provider="GES_DISC", 
            shortname="OCO2_Eph",
            version="11.2",
            description="OCO-2 Level 0 spacecraft ephemerides V11.2 (OCO2_Eph) at GES DISC version: 11.2"
        )

    OCO2_EPH_V10R_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO2_Eph_10r",
            provider="GES_DISC", 
            shortname="OCO2_Eph",
            version="10r",
            description="OCO-2 Level 0 spacecraft ephemerides, Retrospective Processing V10r (OCO2_Eph) at GES DISC version: 10r"
        )

    OCO2_EPH_V11R_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO2_Eph_11r",
            provider="GES_DISC", 
            shortname="OCO2_Eph",
            version="11r",
            description="OCO-2 Level 0 spacecraft ephemerides, Retrospective Processing V11r (OCO2_Eph) at GES DISC version: 11r"
        )

    OCO2_L1AIN_PIXEL_V10_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO2_L1aIn_Pixel_10",
            provider="GES_DISC", 
            shortname="OCO2_L1aIn_Pixel",
            version="10",
            description="OCO-2 Level 1A collated, parsed, calibration data V10 (OCO2_L1aIn_Pixel) at GES DISC version: 10"
        )

    OCO2_L1AIN_PIXEL_V11_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO2_L1aIn_Pixel_11",
            provider="GES_DISC", 
            shortname="OCO2_L1aIn_Pixel",
            version="11",
            description="OCO-2 Level 1A collated, parsed, calibration data V11 (OCO2_L1aIn_Pixel) at GES DISC version: 11"
        )

    OCO2_L1AIN_PIXEL_V112_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO2_L1aIn_Pixel_11.2",
            provider="GES_DISC", 
            shortname="OCO2_L1aIn_Pixel",
            version="11.2",
            description="OCO-2 Level 1A collated, parsed, calibration data V11.2 (OCO2_L1aIn_Pixel) at GES DISC version: 11.2"
        )

    OCO2_L1AIN_PIXEL_V10R_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO2_L1aIn_Pixel_10r",
            provider="GES_DISC", 
            shortname="OCO2_L1aIn_Pixel",
            version="10r",
            description="OCO-2 Level 1A collated, parsed, calibration data, Retrospective Processing V10r (OCO2_L1aIn_Pixel) at GES DISC version: 10r"
        )

    OCO2_L1AIN_PIXEL_V11R_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO2_L1aIn_Pixel_11r",
            provider="GES_DISC", 
            shortname="OCO2_L1aIn_Pixel",
            version="11r",
            description="OCO-2 Level 1A collated, parsed, calibration data, Retrospective Processing V11r (OCO2_L1aIn_Pixel) at GES DISC version: 11r"
        )

    OCO2_L1AIN_SAMPLE_V10_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO2_L1aIn_Sample_10",
            provider="GES_DISC", 
            shortname="OCO2_L1aIn_Sample",
            version="10",
            description="OCO-2 Level 1A collated, parsed, science or calibration data V10 (OCO2_L1aIn_Sample) at GES DISC version: 10"
        )

    OCO2_L1AIN_SAMPLE_V11_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO2_L1aIn_Sample_11",
            provider="GES_DISC", 
            shortname="OCO2_L1aIn_Sample",
            version="11",
            description="OCO-2 Level 1A collated, parsed, science or calibration data V11 (OCO2_L1aIn_Sample) at GES DISC version: 11"
        )

    OCO2_L1AIN_SAMPLE_V112_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO2_L1aIn_Sample_11.2",
            provider="GES_DISC", 
            shortname="OCO2_L1aIn_Sample",
            version="11.2",
            description="OCO-2 Level 1A collated, parsed, science or calibration data V11.2 (OCO2_L1aIn_Sample) at GES DISC version: 11.2"
        )

    OCO2_L1AIN_SAMPLE_V10R_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO2_L1aIn_Sample_10r",
            provider="GES_DISC", 
            shortname="OCO2_L1aIn_Sample",
            version="10r",
            description="OCO-2 Level 1A collated, parsed, science or calibration data, Retrospective Processing V10r (OCO2_L1aIn_Sample) at GES DISC version: 10r"
        )

    OCO2_L1AIN_SAMPLE_V11R_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO2_L1aIn_Sample_11r",
            provider="GES_DISC", 
            shortname="OCO2_L1aIn_Sample",
            version="11r",
            description="OCO-2 Level 1A collated, parsed, science or calibration data, Retrospective Processing V11r (OCO2_L1aIn_Sample) at GES DISC version: 11r"
        )

    OCO2_L1B_CALIBRATION_V112R_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO2_L1B_Calibration_11.2r",
            provider="GES_DISC", 
            shortname="OCO2_L1B_Calibration",
            version="11.2r",
            description="OCO-2 Level 1B calibrated, geolocated calibration spectra Retrospective Processing V11.2r (OCO2_L1B_Calibration) at GES DISC version: 11.2r"
        )

    OCO2_L1B_CALIBRATION_V112_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO2_L1B_Calibration_11.2",
            provider="GES_DISC", 
            shortname="OCO2_L1B_Calibration",
            version="11.2",
            description="OCO-2 Level 1B calibrated, geolocated calibration spectra V11.2 (OCO2_L1B_Calibration) at GES DISC version: 11.2"
        )

    OCO2_L1B_CALIBRATION_V10R_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO2_L1B_Calibration_10r",
            provider="GES_DISC", 
            shortname="OCO2_L1B_Calibration",
            version="10r",
            description="OCO-2 Level 1B calibrated, geolocated calibration spectra, Retrospective Processing V10r (OCO2_L1B_Calibration) at GES DISC version: 10r"
        )

    OCO2_L1B_CALIBRATION_V11R_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO2_L1B_Calibration_11r",
            provider="GES_DISC", 
            shortname="OCO2_L1B_Calibration",
            version="11r",
            description="OCO-2 Level 1B calibrated, geolocated calibration spectra, Retrospective Processing V11r (OCO2_L1B_Calibration) at GES DISC version: 11r"
        )

    OCO2_L1B_SCIENCE_V112R_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO2_L1B_Science_11.2r",
            provider="GES_DISC", 
            shortname="OCO2_L1B_Science",
            version="11.2r",
            description="OCO-2 Level 1B calibrated, geolocated science spectra Retrospective Processing V11.2r (OCO2_L1B_Science) at GES DISC version: 11.2r"
        )

    OCO2_L1B_SCIENCE_V112_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO2_L1B_Science_11.2",
            provider="GES_DISC", 
            shortname="OCO2_L1B_Science",
            version="11.2",
            description="OCO-2 Level 1B calibrated, geolocated science spectra V11.2 (OCO2_L1B_Science) at GES DISC version: 11.2"
        )

    OCO2_L1B_SCIENCE_V10R_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO2_L1B_Science_10r",
            provider="GES_DISC", 
            shortname="OCO2_L1B_Science",
            version="10r",
            description="OCO-2 Level 1B calibrated, geolocated science spectra, Retrospective Processing V10r (OCO2_L1B_Science) at GES DISC version: 10r"
        )

    OCO2_L1B_SCIENCE_V11R_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO2_L1B_Science_11r",
            provider="GES_DISC", 
            shortname="OCO2_L1B_Science",
            version="11r",
            description="OCO-2 Level 1B calibrated, geolocated science spectra, Retrospective Processing V11r (OCO2_L1B_Science) at GES DISC version: 11r"
        )

    OCO2_L2_CO2PRIOR_V112R_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO2_L2_CO2Prior_11.2r",
            provider="GES_DISC", 
            shortname="OCO2_L2_CO2Prior",
            version="11.2r",
            description="OCO-2 Level 2 CO2 prior based on CO2 monthly flask record, global meteorology, and age of air Retrospective Processing V11.2r (OCO2_L2_CO2Prior) at GES DISC version: 11.2r"
        )

    OCO2_L2_CO2PRIOR_V112_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO2_L2_CO2Prior_11.2",
            provider="GES_DISC", 
            shortname="OCO2_L2_CO2Prior",
            version="11.2",
            description="OCO-2 Level 2 CO2 prior based on CO2 monthly flask record, global meteorology, and age of air V11.2 (OCO2_L2_CO2Prior) at GES DISC version: 11.2"
        )

    OCO2_L2_CO2PRIOR_V10R_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO2_L2_CO2Prior_10r",
            provider="GES_DISC", 
            shortname="OCO2_L2_CO2Prior",
            version="10r",
            description="OCO-2 Level 2 CO2 prior based on CO2 monthly flask record, global meteorology, and age of air, Retrospective Processing V10r (OCO2_L2_CO2Prior) at GES DISC version: 10r"
        )

    OCO2_L2_CO2PRIOR_V11R_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO2_L2_CO2Prior_11r",
            provider="GES_DISC", 
            shortname="OCO2_L2_CO2Prior",
            version="11r",
            description="OCO-2 Level 2 CO2 prior based on CO2 monthly flask record, global meteorology, and age of air, Retrospective Processing V11r (OCO2_L2_CO2Prior) at GES DISC version: 11r"
        )

    OCO2_L2_LITE_FP_V10R_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO2_L2_Lite_FP_10r",
            provider="GES_DISC", 
            shortname="OCO2_L2_Lite_FP",
            version="10r",
            description="OCO-2 Level 2 bias-corrected XCO2 and other select fields from the full-physics retrieval aggregated as daily files, Retrospective processing V10r (OCO2_L2_Lite_FP) at GES DISC version: 10r"
        )

    OCO2_L2_LITE_FP_V111R_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO2_L2_Lite_FP_11.1r",
            provider="GES_DISC", 
            shortname="OCO2_L2_Lite_FP",
            version="11.1r",
            description="OCO-2 Level 2 bias-corrected XCO2 and other select fields from the full-physics retrieval aggregated as daily files, Retrospective processing V11.1r (OCO2_L2_Lite_FP) at GES DISC version: 11.1r"
        )

    OCO2_L2_LITE_FP_V112R_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO2_L2_Lite_FP_11.2r",
            provider="GES_DISC", 
            shortname="OCO2_L2_Lite_FP",
            version="11.2r",
            description="OCO-2 Level 2 bias-corrected XCO2 and other select fields from the full-physics retrieval aggregated as daily files, Retrospective processing V11.2r (OCO2_L2_Lite_FP) at GES DISC version: 11.2r"
        )

    OCO2_L2_LITE_SIF_V10R_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO2_L2_Lite_SIF_10r",
            provider="GES_DISC", 
            shortname="OCO2_L2_Lite_SIF",
            version="10r",
            description="OCO-2 Level 2 bias-corrected solar-induced fluorescence and other select fields from the IMAP-DOAS algorithm aggregated as daily files, Retrospective processing V10r (OCO2_L2_Lite_SIF) at GES DISC version: 10r"
        )

    OCO2_L2_LITE_SIF_V112R_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO2_L2_Lite_SIF_11.2r",
            provider="GES_DISC", 
            shortname="OCO2_L2_Lite_SIF",
            version="11.2r",
            description="OCO-2 Level 2 bias-corrected solar-induced fluorescence and other select fields from the IMAP-DOAS algorithm aggregated as daily files, Retrospective processing V11.2r (OCO2_L2_Lite_SIF) at GES DISC version: 11.2r"
        )

    OCO2_L2_LITE_SIF_V11R_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO2_L2_Lite_SIF_11r",
            provider="GES_DISC", 
            shortname="OCO2_L2_Lite_SIF",
            version="11r",
            description="OCO-2 Level 2 bias-corrected solar-induced fluorescence and other select fields from the IMAP-DOAS algorithm aggregated as daily files, Retrospective processing V11r (OCO2_L2_Lite_SIF) at GES DISC version: 11r"
        )

    OCO2_L2_DIAGNOSTIC_V112R_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO2_L2_Diagnostic_11.2r",
            provider="GES_DISC", 
            shortname="OCO2_L2_Diagnostic",
            version="11.2r",
            description="OCO-2 Level 2 geolocated XCO2 retrieval results and algorithm diagnostic information Retrospective Processing V11.2r (OCO2_L2_Diagnostic) at GES DISC version: 11.2r"
        )

    OCO2_L2_DIAGNOSTIC_V112_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO2_L2_Diagnostic_11.2",
            provider="GES_DISC", 
            shortname="OCO2_L2_Diagnostic",
            version="11.2",
            description="OCO-2 Level 2 geolocated XCO2 retrieval results and algorithm diagnostic information V11.2 (OCO2_L2_Diagnostic) at GES DISC version: 11.2"
        )

    OCO2_L2_DIAGNOSTIC_V10R_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO2_L2_Diagnostic_10r",
            provider="GES_DISC", 
            shortname="OCO2_L2_Diagnostic",
            version="10r",
            description="OCO-2 Level 2 geolocated XCO2 retrieval results and algorithm diagnostic information, Retrospective Processing V10r (OCO2_L2_Diagnostic) at GES DISC version: 10r"
        )

    OCO2_L2_DIAGNOSTIC_V11R_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO2_L2_Diagnostic_11r",
            provider="GES_DISC", 
            shortname="OCO2_L2_Diagnostic",
            version="11r",
            description="OCO-2 Level 2 geolocated XCO2 retrieval results and algorithm diagnostic information, Retrospective Processing V11r (OCO2_L2_Diagnostic) at GES DISC version: 11r"
        )

    OCO2_L2_STANDARD_V112R_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO2_L2_Standard_11.2r",
            provider="GES_DISC", 
            shortname="OCO2_L2_Standard",
            version="11.2r",
            description="OCO-2 Level 2 geolocated XCO2 retrievals results, physical model Retrospective Processing V11.2r (OCO2_L2_Standard) at GES DISC version: 11.2r"
        )

    OCO2_L2_STANDARD_V112_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO2_L2_Standard_11.2",
            provider="GES_DISC", 
            shortname="OCO2_L2_Standard",
            version="11.2",
            description="OCO-2 Level 2 geolocated XCO2 retrievals results, physical model V11.2 (OCO2_L2_Standard) at GES DISC version: 11.2"
        )

    OCO2_L2_STANDARD_V10R_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO2_L2_Standard_10r",
            provider="GES_DISC", 
            shortname="OCO2_L2_Standard",
            version="10r",
            description="OCO-2 Level 2 geolocated XCO2 retrievals results, physical model, Retrospective Processing V10r (OCO2_L2_Standard) at GES DISC version: 10r"
        )

    OCO2_L2_STANDARD_V11R_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO2_L2_Standard_11r",
            provider="GES_DISC", 
            shortname="OCO2_L2_Standard",
            version="11r",
            description="OCO-2 Level 2 geolocated XCO2 retrievals results, physical model, Retrospective Processing V11r (OCO2_L2_Standard) at GES DISC version: 11r"
        )

    OCO2_L2_MET_V112R_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO2_L2_Met_11.2r",
            provider="GES_DISC", 
            shortname="OCO2_L2_Met",
            version="11.2r",
            description="OCO-2 Level 2 meteorological parameters interpolated from global assimilation model for each sounding Retrospective Processing V11.2r (OCO2_L2_Met) at GES DISC version: 11.2r"
        )

    OCO2_L2_MET_V112_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO2_L2_Met_11.2",
            provider="GES_DISC", 
            shortname="OCO2_L2_Met",
            version="11.2",
            description="OCO-2 Level 2 meteorological parameters interpolated from global assimilation model for each sounding V11.2 (OCO2_L2_Met) at GES DISC version: 11.2"
        )

    OCO2_L2_MET_V10R_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO2_L2_Met_10r",
            provider="GES_DISC", 
            shortname="OCO2_L2_Met",
            version="10r",
            description="OCO-2 Level 2 meteorological parameters interpolated from global assimilation model for each sounding, Retrospective Processing V10r (OCO2_L2_Met) at GES DISC version: 10r"
        )

    OCO2_L2_MET_V11R_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO2_L2_Met_11r",
            provider="GES_DISC", 
            shortname="OCO2_L2_Met",
            version="11r",
            description="OCO-2 Level 2 meteorological parameters interpolated from global assimilation model for each sounding, Retrospective Processing V11r (OCO2_L2_Met) at GES DISC version: 11r"
        )

    OCO2_L2_MET_V9R_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO2_L2_Met_9r",
            provider="GES_DISC", 
            shortname="OCO2_L2_Met",
            version="9r",
            description="OCO-2 Level 2 meteorological parameters interpolated from global assimilation model for each sounding, Retrospective Processing V9r (OCO2_L2_Met) at GES DISC version: 9r"
        )

    OCO2_L2_ABAND_V112R_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO2_L2_ABand_11.2r",
            provider="GES_DISC", 
            shortname="OCO2_L2_ABand",
            version="11.2r",
            description="OCO-2 Level 2 spatially ordered geolocated retrievals screened using the A-band Preprocessor Retrospective Processing V11.2r (OCO2_L2_ABand) at GES DISC version: 11.2r"
        )

    OCO2_L2_ABAND_V112_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO2_L2_ABand_11.2",
            provider="GES_DISC", 
            shortname="OCO2_L2_ABand",
            version="11.2",
            description="OCO-2 Level 2 spatially ordered geolocated retrievals screened using the A-band Preprocessor V11.2 (OCO2_L2_ABand) at GES DISC version: 11.2"
        )

    OCO2_L2_ABAND_V10R_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO2_L2_ABand_10r",
            provider="GES_DISC", 
            shortname="OCO2_L2_ABand",
            version="10r",
            description="OCO-2 Level 2 spatially ordered geolocated retrievals screened using the A-band Preprocessor, Retrospective Processing V10r (OCO2_L2_ABand) at GES DISC version: 10r"
        )

    OCO2_L2_ABAND_V11R_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO2_L2_ABand_11r",
            provider="GES_DISC", 
            shortname="OCO2_L2_ABand",
            version="11r",
            description="OCO-2 Level 2 spatially ordered geolocated retrievals screened using the A-band Preprocessor, Retrospective Processing V11r (OCO2_L2_ABand) at GES DISC version: 11r"
        )

    OCO2_L2_IMAPDOAS_V112R_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO2_L2_IMAPDOAS_11.2r",
            provider="GES_DISC", 
            shortname="OCO2_L2_IMAPDOAS",
            version="11.2r",
            description="OCO-2 Level 2 spatially ordered geolocated retrievals screened using the IMAP-DOAS Preprocessor (IDP) Retrospective Processing V11.2r (OCO2_L2_IMAPDOAS) at GES DISC version: 11.2r"
        )

    OCO2_L2_IMAPDOAS_V112_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO2_L2_IMAPDOAS_11.2",
            provider="GES_DISC", 
            shortname="OCO2_L2_IMAPDOAS",
            version="11.2",
            description="OCO-2 Level 2 spatially ordered geolocated retrievals screened using the IMAP-DOAS Preprocessor (IDP) V11.2 (OCO2_L2_IMAPDOAS) at GES DISC version: 11.2"
        )

    OCO2_L2_IMAPDOAS_V10R_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO2_L2_IMAPDOAS_10r",
            provider="GES_DISC", 
            shortname="OCO2_L2_IMAPDOAS",
            version="10r",
            description="OCO-2 Level 2 spatially ordered geolocated retrievals screened using the IMAP-DOAS Preprocessor (IDP), Retrospective Processing V10r (OCO2_L2_IMAPDOAS) at GES DISC version: 10r"
        )

    OCO2_L2_IMAPDOAS_V11R_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO2_L2_IMAPDOAS_11r",
            provider="GES_DISC", 
            shortname="OCO2_L2_IMAPDOAS",
            version="11r",
            description="OCO-2 Level 2 spatially ordered geolocated retrievals screened using the IMAP-DOAS Preprocessor (IDP), Retrospective Processing V11r (OCO2_L2_IMAPDOAS) at GES DISC version: 11r"
        )

    OCO3_L1AAE_V11_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO3_L1aAE_11",
            provider="GES_DISC", 
            shortname="OCO3_L1aAE",
            version="11",
            description="OCO-3 Instrument Attitude and Ephemeris Data for One Specific Solar Day, Forward Processing V11 (OCO3_L1aAE) at GES DISC version: 11"
        )

    OCO3_L1AAE_V11R_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO3_L1aAE_11r",
            provider="GES_DISC", 
            shortname="OCO3_L1aAE",
            version="11r",
            description="OCO-3 Instrument Attitude and Ephemeris Data for One Specific Solar Day, Retrospective Processing V11r (OCO3_L1aAE) at GES DISC version: 11r"
        )

    OCO3_L1AIN_PIXEL_V11_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO3_L1aIn_Pixel_11",
            provider="GES_DISC", 
            shortname="OCO3_L1aIn_Pixel",
            version="11",
            description="OCO-3 Level 1A collated, parsed, calibration data V11 (OCO3_L1aIn_Pixel) at GES DISC version: 11"
        )

    OCO3_L1AIN_SAMPLE_V11_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO3_L1aIn_Sample_11",
            provider="GES_DISC", 
            shortname="OCO3_L1aIn_Sample",
            version="11",
            description="OCO-3 Level 1A collated, parsed, science or calibration data V11 (OCO3_L1aIn_Sample) at GES DISC version: 11"
        )

    OCO3_L1AIN_SAMPLE_V11R_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO3_L1aIn_Sample_11r",
            provider="GES_DISC", 
            shortname="OCO3_L1aIn_Sample",
            version="11r",
            description="OCO-3 Level 1A collated, parsed, science or calibration data, Retrospective Processing V11r (OCO2_L1aIn_Sample) at GES DISC version: 11r"
        )

    OCO3_L1AIN_PIXEL_V11R_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO3_L1aIn_Pixel_11r",
            provider="GES_DISC", 
            shortname="OCO3_L1aIn_Pixel",
            version="11r",
            description="OCO-3 Level 1A collated, parsed, science or calibration data, Retrospective Processing V11r (OCO3_L1aIn_Pixel) at GES DISC version: 11r"
        )

    OCO3_L1B_CALIBRATION_V10_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO3_L1B_Calibration_10",
            provider="GES_DISC", 
            shortname="OCO3_L1B_Calibration",
            version="10",
            description="OCO-3 Level 1B calibrated, geolocated calibration spectra, V10 (OCO3_L1B_Calibration) at GES DISC version: 10"
        )

    OCO3_L1B_CALIBRATION_V11_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO3_L1B_Calibration_11",
            provider="GES_DISC", 
            shortname="OCO3_L1B_Calibration",
            version="11",
            description="OCO-3 Level 1B calibrated, geolocated calibration spectra, Forward Processing V11 (OCO3_L1B_Calibration) at GES DISC version: 11"
        )

    OCO3_L1B_CALIBRATION_V10R_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO3_L1B_Calibration_10r",
            provider="GES_DISC", 
            shortname="OCO3_L1B_Calibration",
            version="10r",
            description="OCO-3 Level 1B calibrated, geolocated calibration spectra, Retrospective Processing V10r (OCO3_L1B_Calibration) at GES DISC version: 10r"
        )

    OCO3_L1B_CALIBRATION_V11R_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO3_L1B_Calibration_11r",
            provider="GES_DISC", 
            shortname="OCO3_L1B_Calibration",
            version="11r",
            description="OCO-3 Level 1B calibrated, geolocated calibration spectra, Retrospective Processing V11r (OCO3_L1B_Calibration) at GES DISC version: 11r"
        )

    OCO3_L1B_SCIENCE_V10_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO3_L1B_Science_10",
            provider="GES_DISC", 
            shortname="OCO3_L1B_Science",
            version="10",
            description="OCO-3 Level 1B calibrated, geolocated science spectra, Forward Processing V10 (OCO3_L1B_Science) at GES DISC version: 10"
        )

    OCO3_L1B_SCIENCE_V11_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO3_L1B_Science_11",
            provider="GES_DISC", 
            shortname="OCO3_L1B_Science",
            version="11",
            description="OCO-3 Level 1B calibrated, geolocated science spectra, Forward Processing V11 (OCO3_L1B_Science) at GES DISC version: 11"
        )

    OCO3_L1B_SCIENCE_V10R_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO3_L1B_Science_10r",
            provider="GES_DISC", 
            shortname="OCO3_L1B_Science",
            version="10r",
            description="OCO-3 Level 1B calibrated, geolocated science spectra, Retrospective Processing V10r (OCO3_L1B_Science) at GES DISC version: 10r"
        )

    OCO3_L1B_SCIENCE_V11R_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO3_L1B_Science_11r",
            provider="GES_DISC", 
            shortname="OCO3_L1B_Science",
            version="11r",
            description="OCO-3 Level 1B calibrated, geolocated science spectra, Retrospective Processing V11r (OCO3_L1B_Science) at GES DISC version: 11r"
        )

    OCO3_L2_CO2PRIOR_V10_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO3_L2_CO2Prior_10",
            provider="GES_DISC", 
            shortname="OCO3_L2_CO2Prior",
            version="10",
            description="OCO-3 Level 2 CO2 prior based on CO2 monthly flask record, global meteorology, and age of air, Forward Processing V10 (OCO3_L2_CO2Prior) at GES DISC version: 10"
        )

    OCO3_L2_CO2PRIOR_V11_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO3_L2_CO2Prior_11",
            provider="GES_DISC", 
            shortname="OCO3_L2_CO2Prior",
            version="11",
            description="OCO-3 Level 2 CO2 prior based on CO2 monthly flask record, global meteorology, and age of air, Forward Processing V11 (OCO3_L2_CO2Prior) at GES DISC version: 11"
        )

    OCO3_L2_CO2PRIOR_V10R_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO3_L2_CO2Prior_10r",
            provider="GES_DISC", 
            shortname="OCO3_L2_CO2Prior",
            version="10r",
            description="OCO-3 Level 2 CO2 prior based on CO2 monthly flask record, global meteorology, and age of air, Retrospective Processing V10r (OCO3_L2_CO2Prior) at GES DISC version: 10r"
        )

    OCO3_L2_CO2PRIOR_V11R_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO3_L2_CO2Prior_11r",
            provider="GES_DISC", 
            shortname="OCO3_L2_CO2Prior",
            version="11r",
            description="OCO-3 Level 2 CO2 prior based on CO2 monthly flask record, global meteorology, and age of air, Retrospective Processing V11r (OCO3_L2_CO2Prior) at GES DISC version: 11r"
        )

    OCO3_L2_LITE_FP_V11R_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO3_L2_Lite_FP_11r",
            provider="GES_DISC", 
            shortname="OCO3_L2_Lite_FP",
            version="11r",
            description="OCO-3 Level 2 bias-corrected XCO2 and other select fields from the full-physics retrieval aggregated as daily files, Retrospective processing V11r (OCO3_L2_Lite_FP) at GES DISC version: 11r"
        )

    OCO3_L2_LITE_FP_V104R_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO3_L2_Lite_FP_10.4r",
            provider="GES_DISC", 
            shortname="OCO3_L2_Lite_FP",
            version="10.4r",
            description="OCO-3 Level 2 bias-corrected XCO2 and other select fields from the full-physics retrieval aggregated as daily files, Retrospective processing v10.4r (OCO3_L2_Lite_FP) at GES DISC version: 10.4r"
        )

    OCO3_L2_LITE_SIF_V10R_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO3_L2_Lite_SIF_10r",
            provider="GES_DISC", 
            shortname="OCO3_L2_Lite_SIF",
            version="10r",
            description="OCO-3 Level 2 bias-corrected solar-induced fluorescence and other select fields from the IMAP-DOAS algorithm aggregated as daily files, Retrospective processing V10r (OCO3_L2_Lite_SIF) at GES DISC version: 10r"
        )

    OCO3_L2_LITE_SIF_V11R_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO3_L2_Lite_SIF_11r",
            provider="GES_DISC", 
            shortname="OCO3_L2_Lite_SIF",
            version="11r",
            description="OCO-3 Level 2 bias-corrected solar-induced fluorescence and other select fields from the IMAP-DOAS algorithm aggregated as daily files, Retrospective processing V11r (OCO3_L2_Lite_SIF) at GES DISC version: 11r"
        )

    OCO3_L2_DIAGNOSTIC_V10_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO3_L2_Diagnostic_10",
            provider="GES_DISC", 
            shortname="OCO3_L2_Diagnostic",
            version="10",
            description="OCO-3 Level 2 geolocated XCO2 retrieval results and algorithm diagnostic information, Forward Processing V10 (OCO3_L2_Diagnostic) at GES DISC version: 10"
        )

    OCO3_L2_DIAGNOSTIC_V11_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO3_L2_Diagnostic_11",
            provider="GES_DISC", 
            shortname="OCO3_L2_Diagnostic",
            version="11",
            description="OCO-3 Level 2 geolocated XCO2 retrieval results and algorithm diagnostic information, Forward Processing V11 (OCO3_L2_Diagnostic) at GES DISC version: 11"
        )

    OCO3_L2_DIAGNOSTIC_V10R_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO3_L2_Diagnostic_10r",
            provider="GES_DISC", 
            shortname="OCO3_L2_Diagnostic",
            version="10r",
            description="OCO-3 Level 2 geolocated XCO2 retrieval results and algorithm diagnostic information, Retrospective Processing V10r (OCO3_L2_Diagnostic) at GES DISC version: 10r"
        )

    OCO3_L2_DIAGNOSTIC_V11R_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO3_L2_Diagnostic_11r",
            provider="GES_DISC", 
            shortname="OCO3_L2_Diagnostic",
            version="11r",
            description="OCO-3 Level 2 geolocated XCO2 retrieval results and algorithm diagnostic information, Retrospective Processing V11r (OCO3_L2_Diagnostic) at GES DISC version: 11r"
        )

    OCO3_L2_STANDARD_V10_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO3_L2_Standard_10",
            provider="GES_DISC", 
            shortname="OCO3_L2_Standard",
            version="10",
            description="OCO-3 Level 2 geolocated XCO2 retrievals results, physical model, Forward Processing V10 (OCO3_L2_Standard) at GES DISC version: 10"
        )

    OCO3_L2_STANDARD_V11_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO3_L2_Standard_11",
            provider="GES_DISC", 
            shortname="OCO3_L2_Standard",
            version="11",
            description="OCO-3 Level 2 geolocated XCO2 retrievals results, physical model, Forward Processing V11 (OCO3_L2_Standard) at GES DISC version: 11"
        )

    OCO3_L2_STANDARD_V10R_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO3_L2_Standard_10r",
            provider="GES_DISC", 
            shortname="OCO3_L2_Standard",
            version="10r",
            description="OCO-3 Level 2 geolocated XCO2 retrievals results, physical model, Retrospective Processing V10r (OCO3_L2_Standard) at GES DISC version: 10r"
        )

    OCO3_L2_STANDARD_V11R_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO3_L2_Standard_11r",
            provider="GES_DISC", 
            shortname="OCO3_L2_Standard",
            version="11r",
            description="OCO-3 Level 2 geolocated XCO2 retrievals results, physical model, Retrospective Processing V11r (OCO3_L2_Standard) at GES DISC version: 11r"
        )

    OCO3_L2_MET_V10_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO3_L2_Met_10",
            provider="GES_DISC", 
            shortname="OCO3_L2_Met",
            version="10",
            description="OCO-3 Level 2 meteorological parameters interpolated from global assimilation model for each sounding, Forward Processing V10 (OCO3_L2_Met) at GES DISC version: 10"
        )

    OCO3_L2_MET_V11_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO3_L2_Met_11",
            provider="GES_DISC", 
            shortname="OCO3_L2_Met",
            version="11",
            description="OCO-3 Level 2 meteorological parameters interpolated from global assimilation model for each sounding, Forward Processing V11 (OCO3_L2_Met) at GES DISC version: 11"
        )

    OCO3_L2_MET_V10R_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO3_L2_Met_10r",
            provider="GES_DISC", 
            shortname="OCO3_L2_Met",
            version="10r",
            description="OCO-3 Level 2 meteorological parameters interpolated from global assimilation model for each sounding, Retrospective Processing V10r (OCO3_L2_Met) at GES DISC version: 10r"
        )

    OCO3_L2_MET_V11R_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO3_L2_Met_11r",
            provider="GES_DISC", 
            shortname="OCO3_L2_Met",
            version="11r",
            description="OCO-3 Level 2 meteorological parameters interpolated from global assimilation model for each sounding, Retrospective Processing V11r (OCO3_L2_Met) at GES DISC version: 11r"
        )

    OCO3_L2_ABAND_V10_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO3_L2_ABand_10",
            provider="GES_DISC", 
            shortname="OCO3_L2_ABand",
            version="10",
            description="OCO-3 Level 2 spatially ordered geolocated retrievals screened using the A-band Preprocessor, Forward Processing V10 (OCO3_L2_ABand) at GES DISC version: 10"
        )

    OCO3_L2_ABAND_V11_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO3_L2_ABand_11",
            provider="GES_DISC", 
            shortname="OCO3_L2_ABand",
            version="11",
            description="OCO-3 Level 2 spatially ordered geolocated retrievals screened using the A-band Preprocessor, Forward Processing V11 (OCO3_L2_ABand) at GES DISC version: 11"
        )

    OCO3_L2_ABAND_V10R_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO3_L2_ABand_10r",
            provider="GES_DISC", 
            shortname="OCO3_L2_ABand",
            version="10r",
            description="OCO-3 Level 2 spatially ordered geolocated retrievals screened using the A-band Preprocessor, Retrospective Processing V10r (OCO3_L2_ABand) at GES DISC version: 10r"
        )

    OCO3_L2_ABAND_V11R_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO3_L2_ABand_11r",
            provider="GES_DISC", 
            shortname="OCO3_L2_ABand",
            version="11r",
            description="OCO-3 Level 2 spatially ordered geolocated retrievals screened using the A-band Preprocessor, Retrospective Processing V11r (OCO3_L2_ABand) at GES DISC version: 11r"
        )

    OCO3_L2_IMAPDOAS_V10_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO3_L2_IMAPDOAS_10",
            provider="GES_DISC", 
            shortname="OCO3_L2_IMAPDOAS",
            version="10",
            description="OCO-3 Level 2 spatially ordered geolocated retrievals screened using the IMAP-DOAS Preprocessor (IDP), Forward Processing V10 (OCO3_L2_IMAPDOAS) at GES DISC version: 10"
        )

    OCO3_L2_IMAPDOAS_V11_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO3_L2_IMAPDOAS_11",
            provider="GES_DISC", 
            shortname="OCO3_L2_IMAPDOAS",
            version="11",
            description="OCO-3 Level 2 spatially ordered geolocated retrievals screened using the IMAP-DOAS Preprocessor (IDP), Forward Processing V11 (OCO3_L2_IMAPDOAS) at GES DISC version: 11"
        )

    OCO3_L2_IMAPDOAS_V10R_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO3_L2_IMAPDOAS_10r",
            provider="GES_DISC", 
            shortname="OCO3_L2_IMAPDOAS",
            version="10r",
            description="OCO-3 Level 2 spatially ordered geolocated retrievals screened using the IMAP-DOAS Preprocessor (IDP), Retrospective Processing V10r (OCO3_L2_IMAPDOAS) at GES DISC version: 10r"
        )

    OCO3_L2_IMAPDOAS_V11R_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OCO3_L2_IMAPDOAS_11r",
            provider="GES_DISC", 
            shortname="OCO3_L2_IMAPDOAS",
            version="11r",
            description="OCO-3 Level 2 spatially ordered geolocated retrievals screened using the IMAP-DOAS Preprocessor (IDP), Retrospective Processing V11r (OCO3_L2_IMAPDOAS) at GES DISC version: 11r"
        )

    OMAEROZ_V003_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMAEROZ_003",
            provider="GES_DISC", 
            shortname="OMAEROZ",
            version="003",
            description="OMI/Aura Aerosol product Multi-wavelength Algorithm Zoomed 1-Orbit L2 Swath 13x12km V003 (OMAEROZ) at GES DISC version: 003"
        )

    OMBRO_V003_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMBRO_003",
            provider="GES_DISC", 
            shortname="OMBRO",
            version="003",
            description="OMI/Aura Bromine Monoxide (BrO) Total Column 1-orbit L2 Swath 13x24 km V003 (OMBRO) at GES DISC version: 003"
        )

    OMOCLO_V003_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMOCLO_003",
            provider="GES_DISC", 
            shortname="OMOCLO",
            version="003",
            description="OMI/Aura Chlorine Dioxide (OClO) Total Column 1-orbit L2 Swath 13x24 km V003 (OMOCLO) at GES DISC version: 003"
        )

    OMCLDO2_V003_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMCLDO2_003",
            provider="GES_DISC", 
            shortname="OMCLDO2",
            version="003",
            description="OMI/Aura Cloud Pressure and Fraction (O2-O2 Absorption) 1-Orbit L2 Swath 13x24km V003 (OMCLDO2) at GES DISC version: 003"
        )

    OMCLDO2_CPR_V003_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMCLDO2_CPR_003",
            provider="GES_DISC", 
            shortname="OMCLDO2_CPR",
            version="003",
            description="OMI/Aura Cloud Pressure and Fraction (O2-O2 Absorption) 200-km swath subset along CloudSat track V003 (OMCLDO2_CPR) at GES DISC version: 003"
        )

    OMCLDO2G_V003_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMCLDO2G_003",
            provider="GES_DISC", 
            shortname="OMCLDO2G",
            version="003",
            description="OMI/Aura Cloud Pressure and Fraction (O2-O2 Absorption) Daily L2 Global Gridded 0.25 degree x 0.25 degree V3 (OMCLDO2G) at GES DISC version: 003"
        )

    OMCLDO2Z_V003_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMCLDO2Z_003",
            provider="GES_DISC", 
            shortname="OMCLDO2Z",
            version="003",
            description="OMI/Aura Cloud Pressure and Fraction (O2-O2 Absorption) Zoomed 1-Orbit L2 Swath 13x12km V003 (OMCLDO2Z) at GES DISC version: 003"
        )

    OMCLDRR_CPR_V003_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMCLDRR_CPR_003",
            provider="GES_DISC", 
            shortname="OMCLDRR_CPR",
            version="003",
            description="OMI/Aura Cloud Pressure and Fraction (Raman Scattering) 200-km swath subset along CloudSat track V003 (OMCLDRR_CPR) at GES DISC version: 003"
        )

    OMDOAO3_V003_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMDOAO3_003",
            provider="GES_DISC", 
            shortname="OMDOAO3",
            version="003",
            description="OMI/Aura DOAS Total Column Ozone 1-Orbit L2 Swath 13x24 km V003 (OMDOAO3) at GES DISC version: 003"
        )

    OMDOAO3Z_V003_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMDOAO3Z_003",
            provider="GES_DISC", 
            shortname="OMDOAO3Z",
            version="003",
            description="OMI/Aura DOAS Total Column Ozone Zoomed 1-Orbit L2 Swath 13x12km V003 (OMDOAO3Z) at GES DISC version: 003"
        )

    OMCLDRR_V003_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMCLDRR_003",
            provider="GES_DISC", 
            shortname="OMCLDRR",
            version="003",
            description="OMI/Aura Effective Cloud Pressure and Fraction (Raman Scattering) 1-Orbit L2 Swath 13x24 km V003 (OMCLDRR) at GES DISC version: 003"
        )

    OMCLDRR_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMCLDRR_004",
            provider="GES_DISC", 
            shortname="OMCLDRR",
            version="004",
            description="OMI/Aura Effective Cloud Pressure and Fraction (Raman Scattering) 1-Orbit L2 Swath 13x24 km V004 (OMCLDRR) at GES DISC version: 004"
        )

    OMCLDRRG_V003_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMCLDRRG_003",
            provider="GES_DISC", 
            shortname="OMCLDRRG",
            version="003",
            description="OMI/Aura Effective Cloud Pressure and Fraction (Raman Scattering) Daily L2 Global Gridded 0.25 degree x 0.25 degree V3 (OMCLDRRG) at GES DISC version: 003"
        )

    OMHCHO_V003_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMHCHO_003",
            provider="GES_DISC", 
            shortname="OMHCHO",
            version="003",
            description="OMI/Aura Formaldehyde (HCHO) Total Column 1-orbit L2 Swath 13x24 km V003 (OMHCHO) at GES DISC version: 003"
        )

    OMHCHOG_V003_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMHCHOG_003",
            provider="GES_DISC", 
            shortname="OMHCHOG",
            version="003",
            description="OMI/Aura Formaldehyde (HCHO) Total Column Daily L2 Global Gridded 0.25 degree x 0.25 degree V3 (OMHCHOG) at GES DISC version: 003"
        )

    OMHCHOD_V003_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMHCHOd_003",
            provider="GES_DISC", 
            shortname="OMHCHOd",
            version="003",
            description="OMI/Aura Formaldehyde (HCHO) Total Column Daily L3 Weighted Mean Global 0.1deg Lat/Lon Grid V003 (OMHCHOd) at GES DISC version: 003"
        )

    OMGLER_V003_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMGLER_003",
            provider="GES_DISC", 
            shortname="OMGLER",
            version="003",
            description="OMI/Aura Global Geometry-Dependent Surface LER 1-Orbit L2 Swath 13x24km V3 (OMGLER) at GES DISC version: 003"
        )

    OMPIXCOR_V003_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMPIXCOR_003",
            provider="GES_DISC", 
            shortname="OMPIXCOR",
            version="003",
            description="OMI/Aura Global Ground Pixel Corners 1-Orbit L2 Swath 13x24km V003 (OMPIXCOR) at GES DISC version: 003"
        )

    OML1BIRR_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OML1BIRR_004",
            provider="GES_DISC", 
            shortname="OML1BIRR",
            version="004",
            description="OMI/Aura Level 1B Averaged Solar Irradiances V004 (OML1BIRR) at GES DISC version: 004"
        )

    OML1BIRR_V003_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OML1BIRR_003",
            provider="GES_DISC", 
            shortname="OML1BIRR",
            version="003",
            description="OMI/Aura Level 1B Solar Irradiances V003 (OML1BIRR) at GES DISC version: 003"
        )

    OML1BRUG_V003_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OML1BRUG_003",
            provider="GES_DISC", 
            shortname="OML1BRUG",
            version="003",
            description="OMI/Aura Level 1B UV Global Geolocated Earthshine Radiances 1-orbit L2 Swath 13x24 km V003 (OML1BRUG) at GES DISC version: 003"
        )

    OML1BRUG_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OML1BRUG_004",
            provider="GES_DISC", 
            shortname="OML1BRUG",
            version="004",
            description="OMI/Aura Level 1B UV Global Geolocated Earthshine Radiances V004 (OML1BRUG) at GES DISC version: 004"
        )

    OML1BRUZ_V003_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OML1BRUZ_003",
            provider="GES_DISC", 
            shortname="OML1BRUZ",
            version="003",
            description="OMI/Aura Level 1B UV Zoom-in Geolocated Earthshine Radiances 1-orbit L2 Swath 13x12 km V003 (OML1BRUZ) at GES DISC version: 003"
        )

    OML1BRUZ_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OML1BRUZ_004",
            provider="GES_DISC", 
            shortname="OML1BRUZ",
            version="004",
            description="OMI/Aura Level 1B UV Zoom-in Geolocated Earthshine Radiances V004 (OML1BRUZ) at GES DISC version: 004"
        )

    OML1BRVG_V003_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OML1BRVG_003",
            provider="GES_DISC", 
            shortname="OML1BRVG",
            version="003",
            description="OMI/Aura Level 1B VIS Global Geolocated Earth Shine Radiances 1-orbit L2 Swath 13x24 km V003 (OML1BRVG) at GES DISC version: 003"
        )

    OML1BRVG_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OML1BRVG_004",
            provider="GES_DISC", 
            shortname="OML1BRVG",
            version="004",
            description="OMI/Aura Level 1B VIS Global Geolocated Earthshine Radiances V004 (OML1BRVG) at GES DISC version: 004"
        )

    OML1BRVZ_V003_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OML1BRVZ_003",
            provider="GES_DISC", 
            shortname="OML1BRVZ",
            version="003",
            description="OMI/Aura Level 1B VIS Zoom-in Geolocated Earthshine Radiances 1-orbit L2 Swath 13x12 km V003 (OML1BRVZ) at GES DISC version: 003"
        )

    OML1BRVZ_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OML1BRVZ_004",
            provider="GES_DISC", 
            shortname="OML1BRVZ",
            version="004",
            description="OMI/Aura Level 1B VIS Zoom-in Geolocated Earthshine Radiances V004 (OML1BRVZ) at GES DISC version: 004"
        )

    OMAERUV_CPR_V003_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMAERUV_CPR_003",
            provider="GES_DISC", 
            shortname="OMAERUV_CPR",
            version="003",
            description="OMI/Aura Level 2 Near UV Aerosol Optical Depth and Single Scattering Albedo 200-m swath subset along CloudSat track V003 (OMAERUV_CPR) at GES DISC version: 003"
        )

    OMNO2_CPR_V003_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMNO2_CPR_003",
            provider="GES_DISC", 
            shortname="OMNO2_CPR",
            version="003",
            description="OMI/Aura Level 2 Nitrogen Dioxide (NO2) Trace Gas Column Data 1-Orbit subset Swath along CloudSat track 1-Orbit Swath 13x24 km version: 003"
        )

    OMTO3_CPR_V003_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMTO3_CPR_003",
            provider="GES_DISC", 
            shortname="OMTO3_CPR",
            version="003",
            description="OMI/Aura Level 2 Ozone (O3) Total Column 1-Orbit Subset and Collocated Swath along CloudSat track 200-km wide at 13x24 km2 resolution version: 003"
        )

    OMSO2_CPR_V003_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMSO2_CPR_003",
            provider="GES_DISC", 
            shortname="OMSO2_CPR",
            version="003",
            description="OMI/Aura Level 2 Sulphur Dioxide (SO2) Trace Gas Column Data 1-Orbit Subset and Collocated Swath along CloudSat V003 (OMSO2_CPR) at GES DISC version: 003"
        )

    OMAERO_V003_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMAERO_003",
            provider="GES_DISC", 
            shortname="OMAERO",
            version="003",
            description="OMI/Aura Multi-wavelength Aerosol Optical Depth and Single Scattering Albedo 1-orbit L2 Swath 13x24 km V003 (OMAERO) at GES DISC version: 003"
        )

    OMAEROG_V003_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMAEROG_003",
            provider="GES_DISC", 
            shortname="OMAEROG",
            version="003",
            description="OMI/Aura Multi-wavelength Aerosol Optical Depth and Single Scattering Albedo Daily L2 Global Gridded 0.25 degree x 0.25 degree V3 (OMAEROG) at GES DISC version: 003"
        )

    OMAEROE_V003_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMAEROe_003",
            provider="GES_DISC", 
            shortname="OMAEROe",
            version="003",
            description="OMI/Aura Multi-wavelength Aerosol Optical Depth and Single Scattering Albedo L3 1 day Best Pixel in 0.25 degree x 0.25 degree V3 (OMAEROe) at GES DISC version: 003"
        )

    OMNO2D_V003_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMNO2d_003",
            provider="GES_DISC", 
            shortname="OMNO2d",
            version="003",
            description="OMI/Aura NO2 Cloud-Screened Total and Tropospheric Column L3 Global Gridded 0.25 degree x 0.25 degree V3 (OMNO2d) at GES DISC version: 003"
        )

    OMNO2G_V003_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMNO2G_003",
            provider="GES_DISC", 
            shortname="OMNO2G",
            version="003",
            description="OMI/Aura NO2 Total and Tropospheric Column Daily L2 Global Gridded 0.25 degree x 0.25 degree V3 (OMNO2G) at GES DISC version: 003"
        )

    OMI_MINDS_NO2_V11_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMI_MINDS_NO2_1.1",
            provider="GES_DISC", 
            shortname="OMI_MINDS_NO2",
            version="1.1",
            description="OMI/Aura NO2 Tropospheric, Stratospheric & Total Columns MINDS 1-Orbit L2 Swath 13 km x 24 km V1.1 (OMI_MINDS_NO2) at GES DISC version: 1.1"
        )

    OMI_MINDS_NO2G_V11_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMI_MINDS_NO2G_1.1",
            provider="GES_DISC", 
            shortname="OMI_MINDS_NO2G",
            version="1.1",
            description="OMI/Aura NO2 Tropospheric, Stratospheric & Total Columns MINDS Daily L2 Global Gridded 0.25 degree x 0.25 degree V1.1 (OMI_MINDS_NO2G) at GES DISC version: 1.1"
        )

    OMI_MINDS_NO2D_V11_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMI_MINDS_NO2d_1.1",
            provider="GES_DISC", 
            shortname="OMI_MINDS_NO2d",
            version="1.1",
            description="OMI/Aura NO2 Tropospheric, Stratospheric & Total Columns MINDS Daily L3 Global Gridded 0.25 degree x 0.25 degree V1.1 (OMI_MINDS_NO2d) at GES DISC version: 1.1"
        )

    OMIAURAAER_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMIAuraAER_1",
            provider="GES_DISC", 
            shortname="OMIAuraAER",
            version="1",
            description="OMI/Aura Near UV Aerosol Index, Optical Depth and Single Scattering Albedo 1-Orbit L2 13x24km version: 1"
        )

    OMAERUV_V003_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMAERUV_003",
            provider="GES_DISC", 
            shortname="OMAERUV",
            version="003",
            description="OMI/Aura Near UV Aerosol Optical Depth and Single Scattering Albedo 1-orbit L2 Swath 13x24 km V003 (OMAERUV) at GES DISC version: 003"
        )

    OMAERUV_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMAERUV_004",
            provider="GES_DISC", 
            shortname="OMAERUV",
            version="004",
            description="OMI/Aura Near UV Aerosol Optical Depth and Single Scattering Albedo 1-orbit L2 Swath 13x24 km V004 (OMAERUV) at GES DISC version: 004"
        )

    OMAERUVG_V003_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMAERUVG_003",
            provider="GES_DISC", 
            shortname="OMAERUVG",
            version="003",
            description="OMI/Aura Near UV Aerosol Optical Depth and Single Scattering Albedo Daily L2 Global Gridded 0.25 degree x 0.25 degree V3 (OMAERUVG) at GES DISC version: 003"
        )

    OMAERUVD_V003_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMAERUVd_003",
            provider="GES_DISC", 
            shortname="OMAERUVd",
            version="003",
            description="OMI/Aura Near UV Aerosol Optical Depth and Single Scattering Albedo L3 1 day 1.0 degree x 1.0 degree V3 (OMAERUVd) at GES DISC version: 003"
        )

    OMNO2_V003_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMNO2_003",
            provider="GES_DISC", 
            shortname="OMNO2",
            version="003",
            description="OMI/Aura Nitrogen Dioxide (NO2) Total and Tropospheric Column 1-orbit L2 Swath 13x24 km V003 (OMNO2) at GES DISC version: 003"
        )

    OMDOAO3G_V003_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMDOAO3G_003",
            provider="GES_DISC", 
            shortname="OMDOAO3G",
            version="003",
            description="OMI/Aura Ozone (O3) DOAS Total Column Daily L2 Global Gridded 0.25 degree x 0.25 degree V3 (OMDOAO3G) at GES DISC version: 003"
        )

    OMDOAO3E_V003_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMDOAO3e_003",
            provider="GES_DISC", 
            shortname="OMDOAO3e",
            version="003",
            description="OMI/Aura Ozone (O3) DOAS Total Column Daily L3 1 day 0.25 degree x 0.25 degree V3 (OMDOAO3e) at GES DISC version: 003"
        )

    OMO3PR_V003_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMO3PR_003",
            provider="GES_DISC", 
            shortname="OMO3PR",
            version="003",
            description="OMI/Aura Ozone (O3) Profile 1-Orbit L2 Swath 13x48km V003 (OMO3PR) at GES DISC version: 003"
        )

    OMTO3G_V003_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMTO3G_003",
            provider="GES_DISC", 
            shortname="OMTO3G",
            version="003",
            description="OMI/Aura Ozone (O3) Total Column Daily L2 Global Gridded 0.25 degree x 0.25 degree V3 (OMTO3G) at GES DISC version: 003"
        )

    OMTO3_V003_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMTO3_003",
            provider="GES_DISC", 
            shortname="OMTO3",
            version="003",
            description="OMI/Aura Ozone(O3) Total Column 1-Orbit L2 Swath 13x24 km V003 (OMTO3) at GES DISC version: 003"
        )

    OMSO2E_V003_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMSO2e_003",
            provider="GES_DISC", 
            shortname="OMSO2e",
            version="003",
            description="OMI/Aura Sulfur Dioxide (SO2) Total Column Daily L3 1 day Best Pixel in 0.25 degree x 0.25 degree V3 (OMSO2e) at GES DISC version: 003"
        )

    OMSO2_V003_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMSO2_003",
            provider="GES_DISC", 
            shortname="OMSO2",
            version="003",
            description="OMI/Aura Sulphur Dioxide (SO2) Total Column 1-orbit L2 Swath 13x24 km V003 (OMSO2) at GES DISC version: 003"
        )

    OMSO2G_V003_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMSO2G_003",
            provider="GES_DISC", 
            shortname="OMSO2G",
            version="003",
            description="OMI/Aura Sulphur Dioxide (SO2) Total Column Daily L2 Global Gridded 0.125 degree x 0.125 degree V3 (OMSO2G) at GES DISC version: 003"
        )

    OMLER_V003_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMLER_003",
            provider="GES_DISC", 
            shortname="OMLER",
            version="003",
            description="OMI/Aura Surface Reflectance Climatology L3 Global Gridded 0.5 degree x 0.5 degree V3 (OMLER) at GES DISC version: 003"
        )

    OMUVB_V003_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMUVB_003",
            provider="GES_DISC", 
            shortname="OMUVB",
            version="003",
            description="OMI/Aura Surface UV Irradiance 1-orbit L2 Swath 13x24 km V003 (OMUVB) at GES DISC version: 003"
        )

    OMUVBG_V003_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMUVBG_003",
            provider="GES_DISC", 
            shortname="OMUVBG",
            version="003",
            description="OMI/Aura Surface UVB Irradiance and Erythemal Dose Daily L2 Global Gridded 0.25 degree x 0.25 degree V3 (OMUVBG) at GES DISC version: 003"
        )

    OMUVBD_V003_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMUVBd_003",
            provider="GES_DISC", 
            shortname="OMUVBd",
            version="003",
            description="OMI/Aura Surface UVB Irradiance and Erythemal Dose Daily L3 Global Gridded 1.0 degree x 1.0 degree V3 (OMUVBd) at GES DISC version: 003"
        )

    OMTO3E_V003_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMTO3e_003",
            provider="GES_DISC", 
            shortname="OMTO3e",
            version="003",
            description="OMI/Aura TOMS-Like Ozone and Radiative Cloud Fraction L3 1 day 0.25 degree x 0.25 degree V3 (OMTO3e) at GES DISC version: 003"
        )

    OMTO3D_V003_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMTO3d_003",
            provider="GES_DISC", 
            shortname="OMTO3d",
            version="003",
            description="OMI/Aura TOMS-Like Ozone, Aerosol Index, Cloud Radiance Fraction L3 1 day 1 degree x 1 degree V3 (OMTO3d) at GES DISC version: 003"
        )

    OMPIXCORZ_V003_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMPIXCORZ_003",
            provider="GES_DISC", 
            shortname="OMPIXCORZ",
            version="003",
            description="OMI/Aura Zoom-in Ground Pixel Corners 1-Orbit L2 Swath 13x12km V003 (OMPIXCORZ) at GES DISC version: 003"
        )

    OMMYDAGEO_V003_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMMYDAGEO_003",
            provider="GES_DISC", 
            shortname="OMMYDAGEO",
            version="003",
            description="OMI/Aura and MODIS/Aqua Aerosol Geo-colocation Product 1-Orbit L2 Swath 13x24 km V003 (OMMYDAGEO) at GES DISC version: 003"
        )

    OMMYDCLD_V003_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMMYDCLD_003",
            provider="GES_DISC", 
            shortname="OMMYDCLD",
            version="003",
            description="OMI/Aura and MODIS/Aqua Merged Cloud Product 1-Orbit L2 Swath 13x24 km V003 (OMMYDCLD) at GES DISC version: 003"
        )

    OMPS_N20_NMHCHO_L2_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMPS_N20_NMHCHO_L2_1",
            provider="GES_DISC", 
            shortname="OMPS_N20_NMHCHO_L2",
            version="1",
            description="OMPS-N20 L2 NM Formaldehyde (HCHO) Total Column swath orbital version: 1"
        )

    OMPS_N20_NMSO2_PCA_L2_STEP1_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMPS_N20_NMSO2_PCA_L2_Step1_1",
            provider="GES_DISC", 
            shortname="OMPS_N20_NMSO2_PCA_L2_Step1",
            version="1",
            description="OMPS-N20 NM PCA SO2 Step 1 Total Column 1-Orbit L2 Swath 17x13km version: 1"
        )

    OMPS_N21_LP_L1G_EV_V10_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMPS_N21_LP_L1G_EV_1.0",
            provider="GES_DISC", 
            shortname="OMPS_N21_LP_L1G_EV",
            version="1.0",
            description="OMPS-N21 L1G LP Radiance EV Wavelength-Altitude Grid swath orbital 3slit V1.0 (OMPS_N21_LP_L1G_EV) at GES DISC version: 1.0"
        )

    OMPS_N21_LP_L2_AER_DAILY_V10_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMPS_N21_LP_L2_AER_DAILY_1.0",
            provider="GES_DISC", 
            shortname="OMPS_N21_LP_L2_AER_DAILY",
            version="1.0",
            description="OMPS-N21 L2 LP Aerosol Extinction Vertical Profile swath daily 3slit V2 (OMPS_N21_LP_L2_AER_DAILY) at GES DISC version: 1.0"
        )

    OMPS_N21_LP_L2_O3_DAILY_V10_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMPS_N21_LP_L2_O3_DAILY_1.0",
            provider="GES_DISC", 
            shortname="OMPS_N21_LP_L2_O3_DAILY",
            version="1.0",
            description="OMPS-N21 L2 LP Ozone (O3) Vertical Profile swath daily 3slit V1.0 (OMPS_N21_LP_L2_O3_DAILY) at GES DISC version: 1.0"
        )

    OMPS_NPP_LP_L1G_EV_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMPS_NPP_LP_L1G_EV_2",
            provider="GES_DISC", 
            shortname="OMPS_NPP_LP_L1G_EV",
            version="2",
            description="OMPS-NPP L1G LP Radiance EV Wavelength-Altitude Grid swath orbital 3slit V2 (OMPS_NPP_LP_L1G_EV) at GES DISC version: 2"
        )

    OMPS_NPP_LP_L1G_EV_V26_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMPS_NPP_LP_L1G_EV_2.6",
            provider="GES_DISC", 
            shortname="OMPS_NPP_LP_L1G_EV",
            version="2.6",
            description="OMPS-NPP L1G LP Radiance EV Wavelength-Altitude Grid swath orbital 3slit V2.6 (OMPS_NPP_LP_L1G_EV) at GES DISC version: 2.6"
        )

    OMPS_NPP_LP_L2_AER_DAILY_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMPS_NPP_LP_L2_AER_DAILY_2",
            provider="GES_DISC", 
            shortname="OMPS_NPP_LP_L2_AER_DAILY",
            version="2",
            description="OMPS-NPP L2 LP Aerosol Extinction Vertical Profile swath daily 3slit V2 (OMPS_NPP_LP_L2_AER_DAILY) at GES DISC version: 2"
        )

    OMPS_NPP_LP_L2_O3_DAILY_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMPS_NPP_LP_L2_O3_DAILY_2",
            provider="GES_DISC", 
            shortname="OMPS_NPP_LP_L2_O3_DAILY",
            version="2",
            description="OMPS-NPP L2 LP Ozone (O3) Vertical Profile swath daily 3slit V2.5 (OMPS_NPP_LP_L2_O3_DAILY) at GES DISC version: 2"
        )

    OMPS_NPP_LP_L2_O3_DAILY_V26_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMPS_NPP_LP_L2_O3_DAILY_2.6",
            provider="GES_DISC", 
            shortname="OMPS_NPP_LP_L2_O3_DAILY",
            version="2.6",
            description="OMPS-NPP L2 LP Ozone (O3) Vertical Profile swath daily Center slit V2.6 (OMPS_NPP_LP_L2_O3_DAILY) at GES DISC version: 2.6"
        )

    OMPS_NPP_NMMIEAI_L2_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMPS_NPP_NMMIEAI_L2_2",
            provider="GES_DISC", 
            shortname="OMPS_NPP_NMMIEAI_L2",
            version="2",
            description="OMPS-NPP L2 NM Aerosol Index swath orbital version: 2"
        )

    OMPS_NPP_NMCLDRR_L2_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMPS_NPP_NMCLDRR_L2_2",
            provider="GES_DISC", 
            shortname="OMPS_NPP_NMCLDRR_L2",
            version="2",
            description="OMPS-NPP L2 NM Cloud Pressure and Fraction swath orbital V2 (OMPS_NPP_NMCLDRR_L2) at GES DISC version: 2"
        )

    OMPS_NPP_NMHCHO_L2_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMPS_NPP_NMHCHO_L2_1",
            provider="GES_DISC", 
            shortname="OMPS_NPP_NMHCHO_L2",
            version="1",
            description="OMPS-NPP L2 NM Formaldehyde (HCHO) Total Column swath orbital version: 1"
        )

    OMPS_NPP_NMNO2_L2_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMPS_NPP_NMNO2_L2_2",
            provider="GES_DISC", 
            shortname="OMPS_NPP_NMNO2_L2",
            version="2",
            description="OMPS-NPP L2 NM Nitrogen Dioxide (NO2) Total and Tropospheric Column swath orbital V2 (OMPS_NPP_NMNO2_L2) at GES DISC version: 2"
        )

    OMPS_NPP_NMTO3_L2_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMPS_NPP_NMTO3_L2_2",
            provider="GES_DISC", 
            shortname="OMPS_NPP_NMTO3_L2",
            version="2",
            description="OMPS-NPP L2 NM Ozone (O3) Total Column swath orbital version: 2"
        )

    OMPS_NPP_NMSO2_L2_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMPS_NPP_NMSO2_L2_2",
            provider="GES_DISC", 
            shortname="OMPS_NPP_NMSO2_L2",
            version="2",
            description="OMPS-NPP L2 NM Sulfur Dioxide (SO2) Total and Tropospheric Column swath orbital V2 (OMPS_NPP_NMSO2_L2) at GES DISC version: 2"
        )

    OMPS_NPP_NPBUVO3_L2_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMPS_NPP_NPBUVO3_L2_2",
            provider="GES_DISC", 
            shortname="OMPS_NPP_NPBUVO3_L2",
            version="2",
            description="OMPS-NPP L2 NP Ozone (O3) Vertical Profile swath orbital version: 2"
        )

    OMPS_NPP_NPBUVO3_L2_V29_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMPS_NPP_NPBUVO3_L2_2.9",
            provider="GES_DISC", 
            shortname="OMPS_NPP_NPBUVO3_L2",
            version="2.9",
            description="OMPS-NPP L2 NP Ozone (O3) Vertical Profile swath orbital V2.9 (OMPS_NPP_NPBUVO3_L2) at GES DISC version: 2.9"
        )

    OMPS_NPP_LP_L3_AER_MONTHLY_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMPS_NPP_LP_L3_AER_MONTHLY_1",
            provider="GES_DISC", 
            shortname="OMPS_NPP_LP_L3_AER_MONTHLY",
            version="1",
            description="OMPS-NPP L3 LP Aerosol Extinction Vertical Profile 5 x 15 deg lat-lon grid multi-wavelength monthly V1 (OMPS_NPP_LP_L3_AER_MONTHLY) at GES DISC version: 1"
        )

    OMPS_NPP_NMTO3_L3_DAILY_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMPS_NPP_NMTO3_L3_DAILY_2",
            provider="GES_DISC", 
            shortname="OMPS_NPP_NMTO3_L3_DAILY",
            version="2",
            description="OMPS-NPP L3 NM Ozone (O3) Total Column 1.0 deg grid daily V2 version: 2"
        )

    OMPS_NPP_LP_L2_TEMP_DAILY_V10_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMPS_NPP_LP_L2_Temp_DAILY_1.0",
            provider="GES_DISC", 
            shortname="OMPS_NPP_LP_L2_Temp_DAILY",
            version="1.0",
            description="OMPS-NPP LP L2 Temperature Vertical Profile swath daily 3-slit V1.0 (OMPS_NPP_LP_L2_Temp_DAILY) at GES DISC version: 1.0"
        )

    OMPS_NPP_NMEV_L1B_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMPS_NPP_NMEV_L1B_2",
            provider="GES_DISC", 
            shortname="OMPS_NPP_NMEV_L1B",
            version="2",
            description="OMPS/NPP L1B NM Radiance EV Calibrated Geolocated Swath Orbital V2 (OMPS_NPP_NMEV_L1B) at GES DISC version: 2"
        )

    OMPS_NPP_NPEV_L1B_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMPS_NPP_NPEV_L1B_2",
            provider="GES_DISC", 
            shortname="OMPS_NPP_NPEV_L1B",
            version="2",
            description="OMPS/NPP L1B NP Radiance EV Calibrated Geolocated Swath Orbital V2 (OMPS_NPP_NPEV_L1B) at GES DISC version: 2"
        )

    OMPS_NPP_NMSO2_PCA_L3_DAILY_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMPS_NPP_NMSO2_PCA_L3_DAILY_1",
            provider="GES_DISC", 
            shortname="OMPS_NPP_NMSO2_PCA_L3_DAILY",
            version="1",
            description="OMPS/NPP L3 NM PCA Sulfur Dioxide (SO2) Total Column Daily Best Pixel Global Gridded 0.25 degree x 0.25 degree V1 (OMPS_NPP_NMSO2_PCA_L3_DAILY) at GES DISC version: 1"
        )

    OMPS_NPP_NMSO2_PCA_L2_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMPS_NPP_NMSO2_PCA_L2_2",
            provider="GES_DISC", 
            shortname="OMPS_NPP_NMSO2_PCA_L2",
            version="2",
            description="OMPS/NPP PCA SO2 Total Column 1-Orbit L2 Swath 50x50km V2 (OMPS_NPP_NMSO2_PCA_L2) at GES DISC version: 2"
        )

    BGC_GLIDER_GNATS_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_BGC_glider_GNATS_1",
            provider="GES_DISC", 
            shortname="BGC_glider_GNATS",
            version="1",
            description="Ocean Biogeochemistry from Gliders as part of the Gulf of Maine North Atlantic Time Series version: 1"
        )

    CMS_OCE_BGC_CCS_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_CMS_OCE_BGC_CCS_1",
            provider="GES_DISC", 
            shortname="CMS_OCE_BGC_CCS",
            version="1",
            description="Ocean Biogeochemistry in the California Current System 2007-2010 L4 Monthly version: 1"
        )

    PMRN6L1RAD_CDROM_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_PMRN6L1RAD_CDROM_001",
            provider="GES_DISC", 
            shortname="PMRN6L1RAD_CDROM",
            version="001",
            description="PMR/Nimbus-6 Level 1 Radiance Data from CD-ROM V001 (PMRN6L1RAD_CDROM) at GES DISC version: 001"
        )

    PARASOLRB_CPR_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_PARASOLRB_CPR_001",
            provider="GES_DISC", 
            shortname="PARASOLRB_CPR",
            version="001",
            description="POLDER/Parasol L2 Radiation Budget subset along CloudSat track V001 (PARASOLRB_CPR) at GES DISC version: 001"
        )

    OMUANC_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMUANC_004",
            provider="GES_DISC", 
            shortname="OMUANC",
            version="004",
            description="Primary Ancillary Data Geo-Colocated to OMI/Aura UV2 1-Orbit L2 Swath 13x24km V4 (OMUANC) at GES DISC version: 004"
        )

    OMVANC_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_OMVANC_004",
            provider="GES_DISC", 
            shortname="OMVANC",
            version="004",
            description="Primary Ancillary Data Geo-Colocated to OMI/Aura VIS 1-Orbit L2 Swath 13x24km V4 (OMVANC) at GES DISC version: 004"
        )

    PET_PU_3H025_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_PET_PU_3H025_001",
            provider="GES_DISC", 
            shortname="PET_PU_3H025",
            version="001",
            description="RM-OBS/PU Potential Evapotranspiration and Supporting Forcing L4 3-hourly 0.25x0.25 degree V001 (PET_PU_3H025) at GES DISC version: 001"
        )

    PET_PU_3H025_V002_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_PET_PU_3H025_002",
            provider="GES_DISC", 
            shortname="PET_PU_3H025",
            version="002",
            description="RM-OBS/PU Potential Evapotranspiration and Supporting Forcing L4 3-hourly 0.25x0.25 degree V002 (PET_PU_3H025) at GES DISC version: 002"
        )

    SNDRSNCRISL1BIMG_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDRSNCrISL1BIMG_2",
            provider="GES_DISC", 
            shortname="SNDRSNCrISL1BIMG",
            version="2",
            description="S-NPP CrIS IMG: Collocated VIIRS level 1 / cloud mask statistical summary V2 (SNDRSNCrISL1BIMG) at GES DISC version: 2"
        )

    SNDRSNCRISL1BIMGC_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDRSNCrISL1BIMGC_2",
            provider="GES_DISC", 
            shortname="SNDRSNCrISL1BIMGC",
            version="2",
            description="S-NPP CrIS IMG_COL: Array indices for collocated VIIRS observations V2 (SNDRSNCrISL1BIMGC) at GES DISC version: 2"
        )

    SAMSN7L1RAT_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SAMSN7L1RAT_001",
            provider="GES_DISC", 
            shortname="SAMSN7L1RAT",
            version="001",
            description="SAMS/Nimbus-7 Level 1 Radiance Data V001 (SAMSN7L1RAT) at GES DISC version: 001"
        )

    SAMSN7L1RAD_CDROM_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SAMSN7L1RAD_CDROM_001",
            provider="GES_DISC", 
            shortname="SAMSN7L1RAD_CDROM",
            version="001",
            description="SAMS/Nimbus-7 Level 1 Radiance Data from CD-ROM V001 (SAMSN7L1RAD_CDROM) at GES DISC version: 001"
        )

    SAMSN7L3GRIDT_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SAMSN7L3GRIDT_001",
            provider="GES_DISC", 
            shortname="SAMSN7L3GRIDT",
            version="001",
            description="SAMS/Nimbus-7 Level 3 Gridded Retrieval Temperature Data V001 (SAMSN7L3GRIDT) at GES DISC version: 001"
        )

    SAMSN7L3ZMTG_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SAMSN7L3ZMTG_001",
            provider="GES_DISC", 
            shortname="SAMSN7L3ZMTG",
            version="001",
            description="SAMS/Nimbus-7 Level 3 Zonal Means Composition Data V001 (SAMSN7L3ZMTG) at GES DISC version: 001"
        )

    SBUVN7O3_V008_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SBUVN7O3_008",
            provider="GES_DISC", 
            shortname="SBUVN7O3",
            version="008",
            description="SBUV/Nimbus-7 Level 2 Daily Ozone Profile and Total Column from CD-ROM V008 (SBUVN7O3) at GES DISC version: 008"
        )

    SBUVN07L2_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SBUVN07L2_1",
            provider="GES_DISC", 
            shortname="SBUVN07L2",
            version="1",
            description="SBUV/Nimbus-7 Ozone (O3) Nadir Profile and Total Column 1 Day L2 V1 (SBUVN07L2) at GES DISC version: 1"
        )

    SBUVN07L3ZM_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SBUVN07L3zm_1",
            provider="GES_DISC", 
            shortname="SBUVN07L3zm",
            version="1",
            description="SBUV/Nimbus-7 Ozone (O3) Profile and Total Column Ozone 1 Month Zonal Mean L3 Global 5.0 degree Latitude Zones V1 (SBUVN07L3zm) at GES DISC version: 1"
        )

    SBUV2N11O3_V008_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SBUV2N11O3_008",
            provider="GES_DISC", 
            shortname="SBUV2N11O3",
            version="008",
            description="SBUV2/NOAA-11 Level 2 Daily Ozone Profile and Total Column from CD-ROM V008 (SBUV2N11O3) at GES DISC version: 008"
        )

    SBUV2N11L2_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SBUV2N11L2_1",
            provider="GES_DISC", 
            shortname="SBUV2N11L2",
            version="1",
            description="SBUV2/NOAA-11 Ozone (O3) Nadir Profile and Total Column 1 Day L2 V1 (SBUV2N11L2) at GES DISC version: 1"
        )

    SBUV2N11L3ZM_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SBUV2N11L3zm_1",
            provider="GES_DISC", 
            shortname="SBUV2N11L3zm",
            version="1",
            description="SBUV2/NOAA-11 Ozone (O3) Profile and Total Column Ozone 1 Month Zonal Mean L3 Global 5.0 degree Latitude Zones V1 (SBUV2N11L3zm) at GES DISC version: 1"
        )

    SBUV2N14L2_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SBUV2N14L2_1",
            provider="GES_DISC", 
            shortname="SBUV2N14L2",
            version="1",
            description="SBUV2/NOAA-14 Ozone (O3) Nadir Profile and Total Column 1 Day L2 V1 (SBUV2N14L2) at GES DISC version: 1"
        )

    SBUV2N14L3ZM_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SBUV2N14L3zm_1",
            provider="GES_DISC", 
            shortname="SBUV2N14L3zm",
            version="1",
            description="SBUV2/NOAA-14 Ozone (O3) Profile and Total Column Ozone 1 Month Zonal Mean L3 Global 5.0 degree Latitude Zones V1 (SBUV2N14L3zm) at GES DISC version: 1"
        )

    SBUV2N16O3_V008_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SBUV2N16O3_008",
            provider="GES_DISC", 
            shortname="SBUV2N16O3",
            version="008",
            description="SBUV2/NOAA-16 Level 2 Daily Ozone Profile and Total Column from CD-ROM V008 (SBUV2N16O3) at GES DISC version: 008"
        )

    SBUV2N16L2_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SBUV2N16L2_1",
            provider="GES_DISC", 
            shortname="SBUV2N16L2",
            version="1",
            description="SBUV2/NOAA-16 Ozone (O3) Nadir Profile and Total Column 1 Day L2 V1 (SBUV2N16L2) at GES DISC version: 1"
        )

    SBUV2N16L3ZM_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SBUV2N16L3zm_1",
            provider="GES_DISC", 
            shortname="SBUV2N16L3zm",
            version="1",
            description="SBUV2/NOAA-16 Ozone (O3) Profile and Total Column Ozone 1 Month Zonal Mean L3 Global 5.0 degree Latitude Zones V1 (SBUV2N16L3zm) at GES DISC version: 1"
        )

    SBUV2N17L2_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SBUV2N17L2_1",
            provider="GES_DISC", 
            shortname="SBUV2N17L2",
            version="1",
            description="SBUV2/NOAA-17 Ozone (O3) Nadir Profile and Total Column 1 Day L2 V1 (SBUV2N17L2) at GES DISC version: 1"
        )

    SBUV2N17L3ZM_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SBUV2N17L3zm_1",
            provider="GES_DISC", 
            shortname="SBUV2N17L3zm",
            version="1",
            description="SBUV2/NOAA-17 Ozone (O3) Profile and Total Column Ozone 1 Month Zonal Mean L3 Global 5.0 degree Latitude Zones V1 (SBUV2N17L3zm) at GES DISC version: 1"
        )

    SBUV2N18L2_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SBUV2N18L2_1",
            provider="GES_DISC", 
            shortname="SBUV2N18L2",
            version="1",
            description="SBUV2/NOAA-18 Ozone (O3) Nadir Profile and Total Column 1 Day L2 V1 (SBUV2N18L2) at GES DISC version: 1"
        )

    SBUV2N18L3ZM_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SBUV2N18L3zm_1",
            provider="GES_DISC", 
            shortname="SBUV2N18L3zm",
            version="1",
            description="SBUV2/NOAA-18 Ozone (O3) Profile and Total Column Ozone 1 Month Zonal Mean L3 Global 5.0 degree Latitude Zones V1 (SBUV2N18L3zm) at GES DISC version: 1"
        )

    SBUV2N19L2_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SBUV2N19L2_1",
            provider="GES_DISC", 
            shortname="SBUV2N19L2",
            version="1",
            description="SBUV2/NOAA-19 Ozone (O3) Nadir Profile and Total Column 1 Day L2 V1 (SBUV2N19L2) at GES DISC version: 1"
        )

    SBUV2N19L3ZM_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SBUV2N19L3zm_1",
            provider="GES_DISC", 
            shortname="SBUV2N19L3zm",
            version="1",
            description="SBUV2/NOAA-19 Ozone (O3) Profile and Total Column Ozone 1 Month Zonal Mean L3 Global 5.0 degree Latitude Zones V1 (SBUV2N19L3zm) at GES DISC version: 1"
        )

    SBUV2N09O3_V008_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SBUV2N09O3_008",
            provider="GES_DISC", 
            shortname="SBUV2N09O3",
            version="008",
            description="SBUV2/NOAA-9 Level 2 Daily Ozone Profile and Total Column from CD-ROM V008 (SBUV2N09O3) at GES DISC version: 008"
        )

    SBUV2N09L2_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SBUV2N09L2_1",
            provider="GES_DISC", 
            shortname="SBUV2N09L2",
            version="1",
            description="SBUV2/NOAA-9 Ozone (O3) Nadir Profile and Total Column 1 Day L2 V1 (SBUV2N09L2) at GES DISC version: 1"
        )

    SBUV2N09L3ZM_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SBUV2N09L3zm_1",
            provider="GES_DISC", 
            shortname="SBUV2N09L3zm",
            version="1",
            description="SBUV2/NOAA-9 Ozone (O3) Profile and Total Column Ozone 1 Month Zonal Mean L3 Global 5.0 degree Latitude Zones V1 (SBUV2N09L3zm) at GES DISC version: 1"
        )

    SCAMSN6IM_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SCAMSN6IM_001",
            provider="GES_DISC", 
            shortname="SCAMSN6IM",
            version="001",
            description="SCAMS/Nimbus-6 Images of Brightness Temperatures, Water Vapor and Temperature on 70-mm Film V001 (SCAMSN6IM) at GES DISC version: 001"
        )

    SCAMSN6L2_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SCAMSN6L2_001",
            provider="GES_DISC", 
            shortname="SCAMSN6L2",
            version="001",
            description="SCAMS/Nimbus-6 Level 2 Water Vapor and Temperature, as well as Antenna and Brightness Temperature V001 (SCAMSN6L2) at GES DISC version: 001"
        )

    SCMRN5L1RAD_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SCMRN5L1RAD_001",
            provider="GES_DISC", 
            shortname="SCMRN5L1RAD",
            version="001",
            description="SCMR/Nimbus-5 Level 1 Calibrated and Geolocated Radiances V001 (SCMRN5L1RAD) at GES DISC version: 001"
        )

    SCRN4L1RAD_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SCRN4L1RAD_001",
            provider="GES_DISC", 
            shortname="SCRN4L1RAD",
            version="001",
            description="SCR/Nimbus-4 Level 1 Calibrated Radiances V001 (SCRN4L1RAD) at GES DISC version: 001"
        )

    SCRN4L1RAD_CDROM_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SCRN4L1RAD_CDROM_001",
            provider="GES_DISC", 
            shortname="SCRN4L1RAD_CDROM",
            version="001",
            description="SCR/Nimbus-4 Level 1 Radiance Data from CD-ROM V001 (SCRN4L1RAD_CDROM) at GES DISC version: 001"
        )

    SCRN5L1RAD_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SCRN5L1RAD_001",
            provider="GES_DISC", 
            shortname="SCRN5L1RAD",
            version="001",
            description="SCR/Nimbus-5 Level 1 Calibrated Radiances V001 (SCRN5L1RAD) at GES DISC version: 001"
        )

    SCRN5L1RAD_CDROM_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SCRN5L1RAD_CDROM_001",
            provider="GES_DISC", 
            shortname="SCRN5L1RAD_CDROM",
            version="001",
            description="SCR/Nimbus-5 Level 1 Radiance Data from CD-ROM V001 (SCRN5L1RAD_CDROM) at GES DISC version: 001"
        )

    SIRSN3L1_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SIRSN3L1_001",
            provider="GES_DISC", 
            shortname="SIRSN3L1",
            version="001",
            description="SIRS/Nimbus-3 Level 1 Radiance Data V001 (SIRSN3L1) at GES DISC version: 001"
        )

    SIRSN4L1_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SIRSN4L1_001",
            provider="GES_DISC", 
            shortname="SIRSN4L1",
            version="001",
            description="SIRS/Nimbus-4 Level 1 Radiance Data V001 (SIRSN4L1) at GES DISC version: 001"
        )

    SMMRN7IM_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SMMRN7IM_001",
            provider="GES_DISC", 
            shortname="SMMRN7IM",
            version="001",
            description="SMMR/Nimbus-7 Color Images V001 (SMMRN7IM) at GES DISC version: 001"
        )

    SNPP_CRIS_VIIRS750M_IND_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNPP_CrIS_VIIRS750m_IND_1",
            provider="GES_DISC", 
            shortname="SNPP_CrIS_VIIRS750m_IND",
            version="1",
            description="SNPP CrIS-VIIRS 750-m Matchup Indexes V1 (SNPP_CrIS_VIIRS750m_IND) at GES_DISC version: 1"
        )

    SOR3D_COMBINED_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SOR3D_COMBINED_001",
            provider="GES_DISC", 
            shortname="SOR3D_COMBINED",
            version="001",
            description="SORCE Combined XPS, SOLSTICE, and SIM Solar Spectral Irradiance 24-Hour Means V001 (SOR3D_COMBINED_001) at GES DISC version: 001"
        )

    SOR3TSI6_V019_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SOR3TSI6_019",
            provider="GES_DISC", 
            shortname="SOR3TSI6",
            version="019",
            description="SORCE Level 3 Total Solar Irradiance 6-Hour Means V019 (SOR3TSI6) at GES DISC version: 019"
        )

    SOR3TSID_V019_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SOR3TSID_019",
            provider="GES_DISC", 
            shortname="SOR3TSID",
            version="019",
            description="SORCE Level 3 Total Solar Irradiance Daily Means V019 (SOR3TSID) at GES DISC version: 019"
        )

    SOR3SIMD_V027_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SOR3SIMD_027",
            provider="GES_DISC", 
            shortname="SOR3SIMD",
            version="027",
            description="SORCE SIM Level 3 Solar Spectral Irradiance Daily Means V027 (SOR3SIMD) at GES DISC version: 027"
        )

    SOR3SIMD_TAV_V002_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SOR3SIMD_TAV_002",
            provider="GES_DISC", 
            shortname="SOR3SIMD_TAV",
            version="002",
            description="SORCE SIM Level 3 TSIS-Adjusted Values Solar Spectral Irradiance 24-Hour Means V002 (SOR3SIMD_TAV) at GES DISC version: 002"
        )

    SOR3SOLFUVD_V018_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SOR3SOLFUVD_018",
            provider="GES_DISC", 
            shortname="SOR3SOLFUVD",
            version="018",
            description="SORCE SOLSTICE FUV Level 3 Solar Spectral Irradiance Daily Means V018 (SOR3SOLFUVD) at GES DISC version: 018"
        )

    SOR3SOLD_HIGH_V018_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SOR3SOLD_HIGH_018",
            provider="GES_DISC", 
            shortname="SOR3SOLD_HIGH",
            version="018",
            description="SORCE SOLSTICE FUV and MUV Level 3 Solar Spectral Irradiance 0.1nm Res 24-Hour Means V018 (SOR3SOLD_HIGH) at GES DISC version: 018"
        )

    SOR3SOLS_LA_V018_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SOR3SOLS_LA_018",
            provider="GES_DISC", 
            shortname="SOR3SOLS_LA",
            version="018",
            description="SORCE SOLSTICE Level 3 Lyman-alpha Irradiance As-Measured Cadence V018 (SOR3SOLS_LA_018) at GES DISC version: 018"
        )

    SOR3SOLD_MGII_V018_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SOR3SOLD_MGII_018",
            provider="GES_DISC", 
            shortname="SOR3SOLD_MGII",
            version="018",
            description="SORCE SOLSTICE Level 3 MgII Core-to-Wing Ratio 24 Hour Means V018 (SOR3SOLD_MGII_018) at GES DISC version: 018"
        )

    SOR3SOLS_MGII_V018_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SOR3SOLS_MGII_018",
            provider="GES_DISC", 
            shortname="SOR3SOLS_MGII",
            version="018",
            description="SORCE SOLSTICE Level 3 MgII Core-to-Wing Ratio As-Measured Cadence V018 (SOR3SOLS_MGII_018) at GES DISC version: 018"
        )

    SOR3SOLMUVD_V018_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SOR3SOLMUVD_018",
            provider="GES_DISC", 
            shortname="SOR3SOLMUVD",
            version="018",
            description="SORCE SOLSTICE MUV Level 3 Solar Spectral Irradiance Daily Means V018 (SOR3SOLMUVD) at GES DISC version: 018"
        )

    SOR3XPS6_V012_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SOR3XPS6_012",
            provider="GES_DISC", 
            shortname="SOR3XPS6",
            version="012",
            description="SORCE XPS Level 3 Solar Spectral Irradiance 6-Hour Means V012 (SOR3XPS6) at GES DISC version: 012"
        )

    SOR3XPSD_V012_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SOR3XPSD_012",
            provider="GES_DISC", 
            shortname="SOR3XPSD",
            version="012",
            description="SORCE XPS Level 3 Solar Spectral Irradiance Daily Means V012 (SOR3XPSD) at GES DISC version: 012"
        )

    SOR4XPSD_HIGH_V012_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SOR4XPSD_HIGH_012",
            provider="GES_DISC", 
            shortname="SOR4XPSD_HIGH",
            version="012",
            description="SORCE XPS Level 4 Solar Spectral Irradiance 0.1nm Res 24-Hour Means V012 (SOR4XPSD_HIGH) at GES DISC version: 012"
        )

    SOR4XPS5_V012_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SOR4XPS5_012",
            provider="GES_DISC", 
            shortname="SOR4XPS5",
            version="012",
            description="SORCE XPS Level 4 Solar Spectral Irradiance 0.1nm Res 5-Minute V012 (SOR4XPS5) at GES DISC version: 012"
        )

    SOR4XPSD_LOW_V012_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SOR4XPSD_LOW_012",
            provider="GES_DISC", 
            shortname="SOR4XPSD_LOW",
            version="012",
            description="SORCE XPS Level 4 Solar Spectral Irradiance 1.0nm Res 24-Hour Means V012 (SOR4XPSD_LOW) at GES DISC version: 012"
        )

    WC_PM_ET_050_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_WC_PM_ET_050_1",
            provider="GES_DISC", 
            shortname="WC_PM_ET_050",
            version="1",
            description="SRB/GEWEX evapotranspiration (Penman-Monteith) L4 3 hour 0.5 degree x 0.5 degree V1 (WC_PM_ET_050) at GES DISC version: 1"
        )

    SWDB_L305_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SWDB_L305_004",
            provider="GES_DISC", 
            shortname="SWDB_L305",
            version="004",
            description="SeaWiFS Deep Blue Aerosol Optical Depth and Angstrom Exponent Daily Level 3 Data Gridded at 0.5 Degrees V004 (SWDB_L305) at GES DISC version: 004"
        )

    SWDB_L310_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SWDB_L310_004",
            provider="GES_DISC", 
            shortname="SWDB_L310",
            version="004",
            description="SeaWiFS Deep Blue Aerosol Optical Depth and Angstrom Exponent Daily Level 3 Data Gridded at 1.0 Degrees V004 (SWDB_L310) at GES DISC version: 004"
        )

    SWDB_L2_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SWDB_L2_004",
            provider="GES_DISC", 
            shortname="SWDB_L2",
            version="004",
            description="SeaWiFS Deep Blue Aerosol Optical Depth and Angstrom Exponent Level 2 Data V004 (SWDB_L2) at GES DISC V004 version: 004"
        )

    SWDB_L3M05_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SWDB_L3M05_004",
            provider="GES_DISC", 
            shortname="SWDB_L3M05",
            version="004",
            description="SeaWiFS Deep Blue Aerosol Optical Depth and Angstrom Exponent Monthly Level 3 Data Gridded at 0.5 Degrees V004 (SWDB_L3M05) at GES DISC version: 004"
        )

    SWDB_L3M10_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SWDB_L3M10_004",
            provider="GES_DISC", 
            shortname="SWDB_L3M10",
            version="004",
            description="SeaWiFS Deep Blue Aerosol Optical Depth and Angstrom Exponent Monthly Level 3 Data Gridded at 1.0 Degrees V004 (SWDB_L3M10) at GES DISC version: 004"
        )

    SWDB_L3MC05_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SWDB_L3MC05_004",
            provider="GES_DISC", 
            shortname="SWDB_L3MC05",
            version="004",
            description="SeaWiFS Deep Blue Aerosol Optical Thickness Monthly Level 3 Climatology Data Gridded at 0.5 Degrees V004 (SWDB_L3MC05) at GES DISC version: 004"
        )

    SWDB_L3MC10_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SWDB_L3MC10_004",
            provider="GES_DISC", 
            shortname="SWDB_L3MC10",
            version="004",
            description="SeaWiFS Deep Blue Aerosol Optical Thickness Monthly Level 3 Climatology Data Gridded at 1.0 Degrees V004 (SWDB_L3MC10) at GES DISC version: 004"
        )

    S5P_L2__AER_AI_HIR_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_S5P_L2__AER_AI_HiR_1",
            provider="GES_DISC", 
            shortname="S5P_L2__AER_AI_HiR",
            version="1",
            description="Sentinel-5P TROPOMI Aerosol Index 1-Orbit L2 5.5km x 3.5km V1 (S5P_L2__AER_AI_HiR) at GES DISC version: 1"
        )

    S5P_L2__AER_AI_HIR_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_S5P_L2__AER_AI_HiR_2",
            provider="GES_DISC", 
            shortname="S5P_L2__AER_AI_HiR",
            version="2",
            description="Sentinel-5P TROPOMI Aerosol Index 1-Orbit L2 5.5km x 3.5km V2 (S5P_L2__AER_AI_HiR) at GES DISC version: 2"
        )

    S5P_L2__AER_AI_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_S5P_L2__AER_AI_1",
            provider="GES_DISC", 
            shortname="S5P_L2__AER_AI",
            version="1",
            description="Sentinel-5P TROPOMI Aerosol Index 1-Orbit L2 7km x 3.5km V1 (S5P_L2__AER_AI) at GES DISC version: 1"
        )

    S5P_L2__AER_LH_HIR_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_S5P_L2__AER_LH_HiR_1",
            provider="GES_DISC", 
            shortname="S5P_L2__AER_LH_HiR",
            version="1",
            description="Sentinel-5P TROPOMI Aerosol Layer Height 1-Orbit L2 5.5km x 3.5km V1 (S5P_L2__AER_LH_HiR) at GES DISC version: 1"
        )

    S5P_L2__AER_LH_HIR_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_S5P_L2__AER_LH_HiR_2",
            provider="GES_DISC", 
            shortname="S5P_L2__AER_LH_HiR",
            version="2",
            description="Sentinel-5P TROPOMI Aerosol Layer Height 1-Orbit L2 5.5km x 3.5km V2 (S5P_L2__AER_LH_HiR) at GES DISC version: 2"
        )

    S5P_L2__AER_LH_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_S5P_L2__AER_LH_1",
            provider="GES_DISC", 
            shortname="S5P_L2__AER_LH",
            version="1",
            description="Sentinel-5P TROPOMI Aerosol Layer Height 1-Orbit L2 7km x 3.5km V1 (S5P_L2__AER_LH) at GES DISC version: 1"
        )

    S5P_L2__CO_____HIR_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_S5P_L2__CO_____HiR_1",
            provider="GES_DISC", 
            shortname="S5P_L2__CO_____HiR",
            version="1",
            description="Sentinel-5P TROPOMI Carbon Monoxide CO Column 1-Orbit L2 5.5km x 7km V1 (S5P_L2__CO_____HiR) at GES DISC version: 1"
        )

    S5P_L2__CO_____HIR_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_S5P_L2__CO_____HiR_2",
            provider="GES_DISC", 
            shortname="S5P_L2__CO_____HiR",
            version="2",
            description="Sentinel-5P TROPOMI Carbon Monoxide CO Column 1-Orbit L2 5.5km x 7km V2 (S5P_L2__CO_____HiR) at GES DISC version: 2"
        )

    S5P_L2__CO_____V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_S5P_L2__CO_____1",
            provider="GES_DISC", 
            shortname="S5P_L2__CO____",
            version="1",
            description="Sentinel-5P TROPOMI Carbon Monoxide CO Column 1-Orbit L2 7km x 7km V1 (S5P_L2__CO____) at GES DISC version: 1"
        )

    S5P_L2__CLOUD__HIR_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_S5P_L2__CLOUD__HiR_1",
            provider="GES_DISC", 
            shortname="S5P_L2__CLOUD__HiR",
            version="1",
            description="Sentinel-5P TROPOMI Cloud 1-Orbit L2 5.5km x 3.5km V1 (S5P_L2__CLOUD__HiR) at GES DISC version: 1"
        )

    S5P_L2__CLOUD__HIR_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_S5P_L2__CLOUD__HiR_2",
            provider="GES_DISC", 
            shortname="S5P_L2__CLOUD__HiR",
            version="2",
            description="Sentinel-5P TROPOMI Cloud 1-Orbit L2 5.5km x 3.5km V2 (S5P_L2__CLOUD__HiR) at GES DISC version: 2"
        )

    S5P_L2__CLOUD__V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_S5P_L2__CLOUD__1",
            provider="GES_DISC", 
            shortname="S5P_L2__CLOUD_",
            version="1",
            description="Sentinel-5P TROPOMI Cloud 1-Orbit L2 7km x 3.5km V1 (S5P_L2__CLOUD_) at GES DISC version: 1"
        )

    S5P_L1B_IR_SIR_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_S5P_L1B_IR_SIR_1",
            provider="GES_DISC", 
            shortname="S5P_L1B_IR_SIR",
            version="1",
            description="Sentinel-5P TROPOMI Irradiance product SWIR module L1B V1 (S5P_L1B_IR_SIR) at GES DISC version: 1"
        )

    S5P_L1B_IR_SIR_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_S5P_L1B_IR_SIR_2",
            provider="GES_DISC", 
            shortname="S5P_L1B_IR_SIR",
            version="2",
            description="Sentinel-5P TROPOMI Irradiance product SWIR module L1B V2 (S5P_L1B_IR_SIR) at GES DISC version: 2"
        )

    S5P_L1B_IR_UVN_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_S5P_L1B_IR_UVN_1",
            provider="GES_DISC", 
            shortname="S5P_L1B_IR_UVN",
            version="1",
            description="Sentinel-5P TROPOMI Irradiance product UVN module L1B V1 (S5P_L1B_IR_UVN) at GES DISC version: 1"
        )

    S5P_L1B_IR_UVN_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_S5P_L1B_IR_UVN_2",
            provider="GES_DISC", 
            shortname="S5P_L1B_IR_UVN",
            version="2",
            description="Sentinel-5P TROPOMI Irradiance product UVN module L1B V2 (S5P_L1B_IR_UVN) at GES DISC version: 2"
        )

    S5P_L2__CH4____HIR_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_S5P_L2__CH4____HiR_1",
            provider="GES_DISC", 
            shortname="S5P_L2__CH4____HiR",
            version="1",
            description="Sentinel-5P TROPOMI Methane CH4 1-Orbit L2 5.5km x 7km V1 (S5P_L2__CH4____HiR) at GES DISC version: 1"
        )

    S5P_L2__CH4____HIR_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_S5P_L2__CH4____HiR_2",
            provider="GES_DISC", 
            shortname="S5P_L2__CH4____HiR",
            version="2",
            description="Sentinel-5P TROPOMI Methane CH4 1-Orbit L2 5.5km x 7km V2 (S5P_L2__CH4____HiR) at GES DISC version: 2"
        )

    S5P_L2__CH4____V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_S5P_L2__CH4____1",
            provider="GES_DISC", 
            shortname="S5P_L2__CH4___",
            version="1",
            description="Sentinel-5P TROPOMI Methane CH4 1-Orbit L2 7km x 7km V1 (S5P_L2__CH4___) at GES DISC version: 1"
        )

    S5P_L2__O3__PR_HIR_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_S5P_L2__O3__PR_HiR_2",
            provider="GES_DISC", 
            shortname="S5P_L2__O3__PR_HiR",
            version="2",
            description="Sentinel-5P TROPOMI Ozone Profile 1-Orbit L2 30km x 30km V2 (S5P_L2__O3__PR_HiR) at GES DISC version: 2"
        )

    S5P_L1B_RA_BD1_HIR_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_S5P_L1B_RA_BD1_HiR_1",
            provider="GES_DISC", 
            shortname="S5P_L1B_RA_BD1_HiR",
            version="1",
            description="Sentinel-5P TROPOMI Radiance product band 1 (UV detector) L1B 5.5km x 21km V1 (S5P_L1B_RA_BD1_HiR) at GES DISC version: 1"
        )

    S5P_L1B_RA_BD1_HIR_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_S5P_L1B_RA_BD1_HiR_2",
            provider="GES_DISC", 
            shortname="S5P_L1B_RA_BD1_HiR",
            version="2",
            description="Sentinel-5P TROPOMI Radiance product band 1 (UV detector) L1B 5.5km x 21km V2 (S5P_L1B_RA_BD1_HiR) at GES DISC version: 2"
        )

    S5P_L1B_RA_BD1_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_S5P_L1B_RA_BD1_1",
            provider="GES_DISC", 
            shortname="S5P_L1B_RA_BD1",
            version="1",
            description="Sentinel-5P TROPOMI Radiance product band 1 (UV detector) L1B V1 (S5P_L1B_RA_BD1) at GES DISC version: 1"
        )

    S5P_L1B_RA_BD2_HIR_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_S5P_L1B_RA_BD2_HiR_1",
            provider="GES_DISC", 
            shortname="S5P_L1B_RA_BD2_HiR",
            version="1",
            description="Sentinel-5P TROPOMI Radiance product band 2 (UV detector) L1B 5.5km x 3.5km V1 (S5P_L1B_RA_BD2_HiR) at GES DISC version: 1"
        )

    S5P_L1B_RA_BD2_HIR_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_S5P_L1B_RA_BD2_HiR_2",
            provider="GES_DISC", 
            shortname="S5P_L1B_RA_BD2_HiR",
            version="2",
            description="Sentinel-5P TROPOMI Radiance product band 2 (UV detector) L1B 5.5km x 3.5km V2 (S5P_L1B_RA_BD2_HiR) at GES DISC version: 2"
        )

    S5P_L1B_RA_BD2_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_S5P_L1B_RA_BD2_1",
            provider="GES_DISC", 
            shortname="S5P_L1B_RA_BD2",
            version="1",
            description="Sentinel-5P TROPOMI Radiance product band 2 (UV detector) L1B V1 (S5P_L1B_RA_BD2) at GES DISC version: 1"
        )

    S5P_L1B_RA_BD3_HIR_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_S5P_L1B_RA_BD3_HiR_1",
            provider="GES_DISC", 
            shortname="S5P_L1B_RA_BD3_HiR",
            version="1",
            description="Sentinel-5P TROPOMI Radiance product band 3 (UVIS detector) L1B 5.5km x 3.5km V1 (S5P_L1B_RA_BD3_HiR) at GES DISC version: 1"
        )

    S5P_L1B_RA_BD3_HIR_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_S5P_L1B_RA_BD3_HiR_2",
            provider="GES_DISC", 
            shortname="S5P_L1B_RA_BD3_HiR",
            version="2",
            description="Sentinel-5P TROPOMI Radiance product band 3 (UVIS detector) L1B 5.5km x 3.5km V2 (S5P_L1B_RA_BD3_HiR) at GES DISC version: 2"
        )

    S5P_L1B_RA_BD3_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_S5P_L1B_RA_BD3_1",
            provider="GES_DISC", 
            shortname="S5P_L1B_RA_BD3",
            version="1",
            description="Sentinel-5P TROPOMI Radiance product band 3 (UVIS detector) L1B V1 (S5P_L1B_RA_BD3) at GES DISC version: 1"
        )

    S5P_L1B_RA_BD4_HIR_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_S5P_L1B_RA_BD4_HiR_1",
            provider="GES_DISC", 
            shortname="S5P_L1B_RA_BD4_HiR",
            version="1",
            description="Sentinel-5P TROPOMI Radiance product band 4 (UVIS detector) L1B 5.5km x 3.5km V1 (S5P_L1B_RA_BD4_HiR) at GES DISC version: 1"
        )

    S5P_L1B_RA_BD4_HIR_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_S5P_L1B_RA_BD4_HiR_2",
            provider="GES_DISC", 
            shortname="S5P_L1B_RA_BD4_HiR",
            version="2",
            description="Sentinel-5P TROPOMI Radiance product band 4 (UVIS detector) L1B 5.5km x 3.5km V2 (S5P_L1B_RA_BD4_HiR) at GES DISC version: 2"
        )

    S5P_L1B_RA_BD4_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_S5P_L1B_RA_BD4_1",
            provider="GES_DISC", 
            shortname="S5P_L1B_RA_BD4",
            version="1",
            description="Sentinel-5P TROPOMI Radiance product band 4 (UVIS detector) L1B V1 (S5P_L1B_RA_BD4) at GES DISC version: 1"
        )

    S5P_L1B_RA_BD5_HIR_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_S5P_L1B_RA_BD5_HiR_1",
            provider="GES_DISC", 
            shortname="S5P_L1B_RA_BD5_HiR",
            version="1",
            description="Sentinel-5P TROPOMI Radiance product band 5 (NIR detector) L1B 5.5km x 3.5km V1 (S5P_L1B_RA_BD5_HiR) at GES DISC version: 1"
        )

    S5P_L1B_RA_BD5_HIR_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_S5P_L1B_RA_BD5_HiR_2",
            provider="GES_DISC", 
            shortname="S5P_L1B_RA_BD5_HiR",
            version="2",
            description="Sentinel-5P TROPOMI Radiance product band 5 (NIR detector) L1B 5.5km x 3.5km V2 (S5P_L1B_RA_BD5_HiR) at GES DISC version: 2"
        )

    S5P_L1B_RA_BD5_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_S5P_L1B_RA_BD5_1",
            provider="GES_DISC", 
            shortname="S5P_L1B_RA_BD5",
            version="1",
            description="Sentinel-5P TROPOMI Radiance product band 5 (NIR detector) L1B V1 (S5P_L1B_RA_BD5) at GES DISC version: 1"
        )

    S5P_L1B_RA_BD6_HIR_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_S5P_L1B_RA_BD6_HiR_1",
            provider="GES_DISC", 
            shortname="S5P_L1B_RA_BD6_HiR",
            version="1",
            description="Sentinel-5P TROPOMI Radiance product band 6 (NIR detector) L1B 5.5km x 3.5km V1 (S5P_L1B_RA_BD6_HiR) at GES DISC version: 1"
        )

    S5P_L1B_RA_BD6_HIR_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_S5P_L1B_RA_BD6_HiR_2",
            provider="GES_DISC", 
            shortname="S5P_L1B_RA_BD6_HiR",
            version="2",
            description="Sentinel-5P TROPOMI Radiance product band 6 (NIR detector) L1B 5.5km x 3.5km V2 (S5P_L1B_RA_BD6_HiR) at GES DISC version: 2"
        )

    S5P_L1B_RA_BD6_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_S5P_L1B_RA_BD6_1",
            provider="GES_DISC", 
            shortname="S5P_L1B_RA_BD6",
            version="1",
            description="Sentinel-5P TROPOMI Radiance product band 6 (NIR detector) L1B V1 (S5P_L1B_RA_BD6) at GES DISC version: 1"
        )

    S5P_L1B_RA_BD7_HIR_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_S5P_L1B_RA_BD7_HiR_1",
            provider="GES_DISC", 
            shortname="S5P_L1B_RA_BD7_HiR",
            version="1",
            description="Sentinel-5P TROPOMI Radiance product band 7 (SWIR detector) L1B 5.5km x 7km V1 (S5P_L1B_RA_BD7_HiR) at GES DISC version: 1"
        )

    S5P_L1B_RA_BD7_HIR_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_S5P_L1B_RA_BD7_HiR_2",
            provider="GES_DISC", 
            shortname="S5P_L1B_RA_BD7_HiR",
            version="2",
            description="Sentinel-5P TROPOMI Radiance product band 7 (SWIR detector) L1B 5.5km x 7km V2 (S5P_L1B_RA_BD7_HiR) at GES DISC version: 2"
        )

    S5P_L1B_RA_BD7_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_S5P_L1B_RA_BD7_1",
            provider="GES_DISC", 
            shortname="S5P_L1B_RA_BD7",
            version="1",
            description="Sentinel-5P TROPOMI Radiance product band 7 (SWIR detector) L1B V1 (S5P_L1B_RA_BD7) at GES DISC version: 1"
        )

    S5P_L1B_RA_BD8_HIR_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_S5P_L1B_RA_BD8_HiR_1",
            provider="GES_DISC", 
            shortname="S5P_L1B_RA_BD8_HiR",
            version="1",
            description="Sentinel-5P TROPOMI Radiance product band 8 (SWIR detector) L1B 5.5km x 7km V1 (S5P_L1B_RA_BD8_HiR) at GES DISC version: 1"
        )

    S5P_L1B_RA_BD8_HIR_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_S5P_L1B_RA_BD8_HiR_2",
            provider="GES_DISC", 
            shortname="S5P_L1B_RA_BD8_HiR",
            version="2",
            description="Sentinel-5P TROPOMI Radiance product band 8 (SWIR detector) L1B 5.5km x 7km V2 (S5P_L1B_RA_BD8_HiR) at GES DISC version: 2"
        )

    S5P_L1B_RA_BD8_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_S5P_L1B_RA_BD8_1",
            provider="GES_DISC", 
            shortname="S5P_L1B_RA_BD8",
            version="1",
            description="Sentinel-5P TROPOMI Radiance product band 8 (SWIR detector) L1B V1 (S5P_L1B_RA_BD8) at GES DISC version: 1"
        )

    S5P_L2__NP_BD3_HIR_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_S5P_L2__NP_BD3_HiR_1",
            provider="GES_DISC", 
            shortname="S5P_L2__NP_BD3_HiR",
            version="1",
            description="Sentinel-5P TROPOMI SNPP VIIRS cloud product band 3 (UVIS detector) 1-Orbit L2 5.5km x 3.5km V1 (S5P_L2__NP_BD3_HiR) at GES DISC version: 1"
        )

    S5P_L2__NP_BD3_HIR_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_S5P_L2__NP_BD3_HiR_2",
            provider="GES_DISC", 
            shortname="S5P_L2__NP_BD3_HiR",
            version="2",
            description="Sentinel-5P TROPOMI SNPP VIIRS cloud product band 3 (UVIS detector) 1-Orbit L2 5.5km x 3.5km V2 (S5P_L2__NP_BD3_HiR) at GES DISC version: 2"
        )

    S5P_L2__NP_BD3_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_S5P_L2__NP_BD3_1",
            provider="GES_DISC", 
            shortname="S5P_L2__NP_BD3",
            version="1",
            description="Sentinel-5P TROPOMI SNPP VIIRS cloud product band 3 (UVIS detector) 1-Orbit L2 7km x 3.5km V1 (S5P_L2__NP_BD3) at GES DISC version: 1"
        )

    S5P_L2__NP_BD6_HIR_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_S5P_L2__NP_BD6_HiR_1",
            provider="GES_DISC", 
            shortname="S5P_L2__NP_BD6_HiR",
            version="1",
            description="Sentinel-5P TROPOMI SNPP VIIRS cloud product band 6 (NIR detector) 1-Orbit L2 5.5km x 3.5km V1 (S5P_L2__NP_BD6_HiR) at GES DISC version: 1"
        )

    S5P_L2__NP_BD6_HIR_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_S5P_L2__NP_BD6_HiR_2",
            provider="GES_DISC", 
            shortname="S5P_L2__NP_BD6_HiR",
            version="2",
            description="Sentinel-5P TROPOMI SNPP VIIRS cloud product band 6 (NIR detector) 1-Orbit L2 5.5km x 3.5km V2 (S5P_L2__NP_BD6_HiR) at GES DISC version: 2"
        )

    S5P_L2__NP_BD6_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_S5P_L2__NP_BD6_1",
            provider="GES_DISC", 
            shortname="S5P_L2__NP_BD6",
            version="1",
            description="Sentinel-5P TROPOMI SNPP VIIRS cloud product band 6 (NIR detector) 1-Orbit L2 7km x 3.5km V1 (S5P_L2__NP_BD6) at GES DISC version: 1"
        )

    S5P_L2__NP_BD7_HIR_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_S5P_L2__NP_BD7_HiR_1",
            provider="GES_DISC", 
            shortname="S5P_L2__NP_BD7_HiR",
            version="1",
            description="Sentinel-5P TROPOMI SNPP cloud product band 7 (SWIR detector) 1-Orbit L2 5.5km x 7km V1 (S5P_L2__NP_BD7_HiR) at GES DISC version: 1"
        )

    S5P_L2__NP_BD7_HIR_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_S5P_L2__NP_BD7_HiR_2",
            provider="GES_DISC", 
            shortname="S5P_L2__NP_BD7_HiR",
            version="2",
            description="Sentinel-5P TROPOMI SNPP cloud product band 7 (SWIR detector) 1-Orbit L2 5.5km x 7km V2 (S5P_L2__NP_BD7_HiR) at GES DISC version: 2"
        )

    S5P_L2__NP_BD7_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_S5P_L2__NP_BD7_1",
            provider="GES_DISC", 
            shortname="S5P_L2__NP_BD7",
            version="1",
            description="Sentinel-5P TROPOMI SNPP cloud product band 7 (SWIR detector) 1-Orbit L2 7km x 7km V1 (S5P_L2__NP_BD7) at GES DISC version: 1"
        )

    S5P_L2__SO2____HIR_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_S5P_L2__SO2____HiR_1",
            provider="GES_DISC", 
            shortname="S5P_L2__SO2____HiR",
            version="1",
            description="Sentinel-5P TROPOMI Sulphur Dioxide SO2 1-Orbit L2 5.5km x 3.5km V1 (S5P_L2__SO2____HiR) at GES DISC version: 1"
        )

    S5P_L2__SO2____HIR_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_S5P_L2__SO2____HiR_2",
            provider="GES_DISC", 
            shortname="S5P_L2__SO2____HiR",
            version="2",
            description="Sentinel-5P TROPOMI Sulphur Dioxide SO2 1-Orbit L2 5.5km x 3.5km V2 (S5P_L2__SO2____HiR) at GES DISC version: 2"
        )

    S5P_L2__SO2____V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_S5P_L2__SO2____1",
            provider="GES_DISC", 
            shortname="S5P_L2__SO2___",
            version="1",
            description="Sentinel-5P TROPOMI Sulphur Dioxide SO2 1-Orbit L2 7km x 3.5km V1 (S5P_L2__SO2___) at GES DISC version: 1"
        )

    S5P_L2__O3_TOT_HIR_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_S5P_L2__O3_TOT_HiR_1",
            provider="GES_DISC", 
            shortname="S5P_L2__O3_TOT_HiR",
            version="1",
            description="Sentinel-5P TROPOMI Total Ozone Column 1-Orbit L2 5.5km x 3.5km V1 (S5P_L2__O3_TOT_HiR) at GES DISC version: 1"
        )

    S5P_L2__O3_TOT_HIR_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_S5P_L2__O3_TOT_HiR_2",
            provider="GES_DISC", 
            shortname="S5P_L2__O3_TOT_HiR",
            version="2",
            description="Sentinel-5P TROPOMI Total Ozone Column 1-Orbit L2 5.5km x 3.5km V2 (S5P_L2__O3_TOT_HiR) at GES DISC version: 2"
        )

    S5P_L2__O3_TOT_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_S5P_L2__O3_TOT_1",
            provider="GES_DISC", 
            shortname="S5P_L2__O3_TOT",
            version="1",
            description="Sentinel-5P TROPOMI Total Ozone Column 1-Orbit L2 7km x 3.5km V1 (S5P_L2__O3_TOT) at GES DISC version: 1"
        )

    S5P_L2__HCHO___HIR_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_S5P_L2__HCHO___HiR_1",
            provider="GES_DISC", 
            shortname="S5P_L2__HCHO___HiR",
            version="1",
            description="Sentinel-5P TROPOMI Tropospheric Formaldehyde HCHO 1-Orbit L2 5.5km x 3.5km V1 (S5P_L2__HCHO___HiR) at GES DISC version: 1"
        )

    S5P_L2__HCHO___HIR_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_S5P_L2__HCHO___HiR_2",
            provider="GES_DISC", 
            shortname="S5P_L2__HCHO___HiR",
            version="2",
            description="Sentinel-5P TROPOMI Tropospheric Formaldehyde HCHO 1-Orbit L2 5.5km x 3.5km V2 (S5P_L2__HCHO___HiR) at GES DISC version: 2"
        )

    S5P_L2__HCHO___V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_S5P_L2__HCHO___1",
            provider="GES_DISC", 
            shortname="S5P_L2__HCHO__",
            version="1",
            description="Sentinel-5P TROPOMI Tropospheric Formaldehyde HCHO 1-Orbit L2 7km x 3.5km V1 (S5P_L2__HCHO__) at GES DISC version: 1"
        )

    S5P_L2__NO2____HIR_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_S5P_L2__NO2____HiR_1",
            provider="GES_DISC", 
            shortname="S5P_L2__NO2____HiR",
            version="1",
            description="Sentinel-5P TROPOMI Tropospheric NO2 1-Orbit L2 5.5km x 3.5km V1 (S5P_L2__NO2____HiR) at GES DISC version: 1"
        )

    S5P_L2__NO2____HIR_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_S5P_L2__NO2____HiR_2",
            provider="GES_DISC", 
            shortname="S5P_L2__NO2____HiR",
            version="2",
            description="Sentinel-5P TROPOMI Tropospheric NO2 1-Orbit L2 5.5km x 3.5km V2 (S5P_L2__NO2____HiR) at GES DISC version: 2"
        )

    S5P_L2__NO2____V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_S5P_L2__NO2____1",
            provider="GES_DISC", 
            shortname="S5P_L2__NO2___",
            version="1",
            description="Sentinel-5P TROPOMI Tropospheric NO2 1-Orbit L2 7km x 3.5km V1 (S5P_L2__NO2___) at GES DISC version: 1"
        )

    S5P_L2__O3_TCL_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_S5P_L2__O3_TCL_1",
            provider="GES_DISC", 
            shortname="S5P_L2__O3_TCL",
            version="1",
            description="Sentinel-5P TROPOMI Tropospheric Ozone Column V1 (S5P_L2__O3_TCL) at GES DISC version: 1"
        )

    S5P_L2__O3_TCL_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_S5P_L2__O3_TCL_2",
            provider="GES_DISC", 
            shortname="S5P_L2__O3_TCL",
            version="2",
            description="Sentinel-5P TROPOMI Tropospheric Ozone Column V2 (S5P_L2__O3_TCL) at GES DISC version: 2"
        )

    SSBUVO3_V008_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SSBUVO3_008",
            provider="GES_DISC", 
            shortname="SSBUVO3",
            version="008",
            description="Shuttle SBUV (SSBUV) Level 2 Ozone Profile and Total Column, Aerosol Index, and UV-Reflectivity V008 (SSBUVO3) at GES DISC version: 008"
        )

    SSBUVIRR_V008_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SSBUVIRR_008",
            provider="GES_DISC", 
            shortname="SSBUVIRR",
            version="008",
            description="Shuttle SBUV (SSBUV) Solar Spectral Irradiance V008 (SSBUVIRR) at GES DISC version: 008"
        )

    SMERGE_RZSM0_40CM_V20_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SMERGE_RZSM0_40CM_2.0",
            provider="GES_DISC", 
            shortname="SMERGE_RZSM0_40CM",
            version="2.0",
            description="Smerge-Noah-CCI root zone soil moisture 0-40 cm L4 daily 0.125 x 0.125 degree V2.0 (SMERGE_RZSM0_40CM) at GES DISC version: 2.0"
        )

    SNDRAQIML2CCPRET_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDRAQIML2CCPRET_2",
            provider="GES_DISC", 
            shortname="SNDRAQIML2CCPRET",
            version="2",
            description="Sounder SIPS: AQUA AIRS IR + MW Level 2 CLIMCAPS: Atmosphere, cloud and surface geophysical state V2 (SNDRAQIML2CCPRET) at GES DISC version: 2"
        )

    SNDRAQIML2CCPCCR_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDRAQIML2CCPCCR_2",
            provider="GES_DISC", 
            shortname="SNDRAQIML2CCPCCR",
            version="2",
            description="Sounder SIPS: AQUA AIRS IR + MW Level 2 CLIMCAPS: Cloud Cleared Radiances V2 (SNDRAQIML2CCPCCR) at GES DISC version: 2"
        )

    SNDRAQIML2CPS_V21_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDRAQIML2CPS_2.1",
            provider="GES_DISC", 
            shortname="SNDRAQIML2CPS",
            version="2.1",
            description="Sounder SIPS: AQUA AIRS IR + MW Level 2 CLIMCAPS: Retrieved atmospheric state V2.1 (SNDRAQIML2CPS) at GES DISC version: 2.1"
        )

    SNDRAQIML2PLEVCPS_V21_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDRAQIML2PLEVCPS_2.1",
            provider="GES_DISC", 
            shortname="SNDRAQIML2PLEVCPS",
            version="2.1",
            description="Sounder SIPS: AQUA AIRS IR + MW Level 2: Atmospheric state at Standard Pressure Levels derived from CLIMCAPS V2.1 (SNDRAQIML2PLEVCPS) at GES DISC version: 2.1"
        )

    SNDRAQIML3CDCCP_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDRAQIML3CDCCP_2",
            provider="GES_DISC", 
            shortname="SNDRAQIML3CDCCP",
            version="2",
            description="Sounder SIPS: AQUA AIRS IR + MW Level 3 CLIMCAPS : Comprehensive Quality Control Gridded Daily V2 (SNDRAQIML3CDCCP) at GES DISC version: 2"
        )

    SNDRAQIML3CMCCP_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDRAQIML3CMCCP_2",
            provider="GES_DISC", 
            shortname="SNDRAQIML3CMCCP",
            version="2",
            description="Sounder SIPS: AQUA AIRS IR + MW Level 3 CLIMCAPS : Comprehensive Quality Control Gridded Monthly V2 (SNDRAQIML3CMCCP) at GES DISC version: 2"
        )

    SNDRAQIML3SMCCP_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDRAQIML3SMCCP_2",
            provider="GES_DISC", 
            shortname="SNDRAQIML3SMCCP",
            version="2",
            description="Sounder SIPS: AQUA AIRS IR + MW Level 3 CLIMCAPS: Specific Quality Control Gridded Monthly V2 (SNDRAQIML3SMCCP) at GES DISC version: 2"
        )

    SNDRAQIML3SDCCP_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDRAQIML3SDCCP_2",
            provider="GES_DISC", 
            shortname="SNDRAQIML3SDCCP",
            version="2",
            description="Sounder SIPS: AQUA AIRS IR MW Level 3 CLIMCAPS : Specific Quality Control Gridded Daily V2 (SNDRAQIML3SDCCP) at GES DISC version: 2"
        )

    SNDRAQIL2CCPRET_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDRAQIL2CCPRET_2",
            provider="GES_DISC", 
            shortname="SNDRAQIL2CCPRET",
            version="2",
            description="Sounder SIPS: AQUA AIRS IR-only Level 2 CLIMCAPS : Atmosphere, cloud and surface geophysical state V2 (SNDRAQIL2CCPRET) at GES DISC version: 2"
        )

    SNDRAQIL2CCPCCR_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDRAQIL2CCPCCR_2",
            provider="GES_DISC", 
            shortname="SNDRAQIL2CCPCCR",
            version="2",
            description="Sounder SIPS: AQUA AIRS IR-only Level 2 CLIMCAPS: Cloud Cleared Radiances V2 (SNDRAQIL2CCPCCR) at GES DISC version: 2"
        )

    SNDRAQIL2CPS_V21_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDRAQIL2CPS_2.1",
            provider="GES_DISC", 
            shortname="SNDRAQIL2CPS",
            version="2.1",
            description="Sounder SIPS: AQUA AIRS IR-only Level 2 CLIMCAPS: retrieved atmospheric state V2.1 (SNDRAQIL2CPS) at GES DISC version: 2.1"
        )

    SNDRAQIL2PLEVCPS_V21_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDRAQIL2PLEVCPS_2.1",
            provider="GES_DISC", 
            shortname="SNDRAQIL2PLEVCPS",
            version="2.1",
            description="Sounder SIPS: AQUA AIRS IR-only Level 2: Atmospheric state at Standard Pressure Levels derived from CLIMCAPS V2.1 (SNDRAQIL2PLEVCPS) at GES DISC version: 2.1"
        )

    SNDRAQIL3CDCCP_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDRAQIL3CDCCP_2",
            provider="GES_DISC", 
            shortname="SNDRAQIL3CDCCP",
            version="2",
            description="Sounder SIPS: AQUA AIRS IR-only Level 3 CLIMCAPS : Comprehensive Quality Control Gridded Daily V2 (SNDRAQIL3CDCCP) at GES DISC version: 2"
        )

    SNDRAQIL3CMCCP_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDRAQIL3CMCCP_2",
            provider="GES_DISC", 
            shortname="SNDRAQIL3CMCCP",
            version="2",
            description="Sounder SIPS: AQUA AIRS IR-only Level 3 CLIMCAPS: Comprehensive Quality Control Gridded Monthly V2 (SNDRAQIL3CMCCP) at GES DISC version: 2"
        )

    SNDRAQIL3SDCCP_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDRAQIL3SDCCP_2",
            provider="GES_DISC", 
            shortname="SNDRAQIL3SDCCP",
            version="2",
            description="Sounder SIPS: AQUA AIRS IR-only Level 3 CLIMCAPS: Specific Quality Control Gridded Daily V2 (SNDRAQIL3SDCCP) at GES DISC version: 2"
        )

    SNDRAQIL3SMCCP_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDRAQIL3SMCCP_2",
            provider="GES_DISC", 
            shortname="SNDRAQIL3SMCCP",
            version="2",
            description="Sounder SIPS: AQUA AIRS IR-only Level 3 CLIMCAPS: Specific Quality Control Gridded Monthly V2 (SNDRAQIL3SMCCP) at GES DISC version: 2"
        )

    SNDRAQIML1BCALSUBSUM_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDRAQIML1BCALSUBSUM_2",
            provider="GES_DISC", 
            shortname="SNDRAQIML1BCALSUBSUM",
            version="2",
            description="Sounder SIPS: Aqua AIRS Level-1B Calibration Subset: Summary, V2 (SNDRAQIML1BCALSUBSUM) at GES DISC version: 2"
        )

    SNDRAQIML1CCALSUBRND_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDRAQIML1CCALSUBRND_2",
            provider="GES_DISC", 
            shortname="SNDRAQIML1CCALSUBRND",
            version="2",
            description="Sounder SIPS: Aqua AIRS Level-1C Calibration Subset: Random Full Spectra V2 (SNDRAQIML1CCALSUBRND) at GES DISC version: 2"
        )

    SNDRJ1ATMSMAP_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDRJ1ATMSMAP_1",
            provider="GES_DISC", 
            shortname="SNDRJ1ATMSMAP",
            version="1",
            description="Sounder SIPS: JPSS-1 ATMS Level 1 Daily Polygon Granule Map at GES DISC version: 1"
        )

    SNDRJ1ML2RMS_V3_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDRJ1ML2RMS_3",
            provider="GES_DISC", 
            shortname="SNDRJ1ML2RMS",
            version="3",
            description="Sounder SIPS: JPSS-1 ATMS Level 2 RAMSES2 Standard: Atmosphere, precipitation and surface geophysical state V3 (SNDRJ1ML2RMS) at GES DISC version: 3"
        )

    SNDRJ1ML2RMSSUP_V3_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDRJ1ML2RMSSUP_3",
            provider="GES_DISC", 
            shortname="SNDRJ1ML2RMSSUP",
            version="3",
            description="Sounder SIPS: JPSS-1 ATMS Level 2 RAMSES2 Support V3 (SNDRJ1ML2RMSSUP) at GES DISC version: 3"
        )

    SNDRJ1ML3DRMS_V3_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDRJ1ML3DRMS_3",
            provider="GES_DISC", 
            shortname="SNDRJ1ML3DRMS",
            version="3",
            description="Sounder SIPS: JPSS-1 ATMS Level 3 RAMSES2 Standard Gridded Daily V3 at GES DISC version: 3"
        )

    SNDRJ1ML3MRMS_V3_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDRJ1ML3MRMS_3",
            provider="GES_DISC", 
            shortname="SNDRJ1ML3MRMS",
            version="3",
            description="Sounder SIPS: JPSS-1 ATMS Level 3 RAMSES2 Standard Gridded Monthly V3 at GES DISC version: 3"
        )

    SNDRJ1IML2CPS_V21_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDRJ1IML2CPS_2.1",
            provider="GES_DISC", 
            shortname="SNDRJ1IML2CPS",
            version="2.1",
            description="Sounder SIPS: JPSS-1 CrIMSS Level 2 CLIMCAPS: retrieved atmospheric state V2.1 (SNDRJ1IML2CPS) at GES DISC version: 2.1"
        )

    SNDRJ1IML2PLEVCPS_V21_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDRJ1IML2PLEVCPS_2.1",
            provider="GES_DISC", 
            shortname="SNDRJ1IML2PLEVCPS",
            version="2.1",
            description="Sounder SIPS: JPSS-1 CrIMSS Level 2: Atmospheric state at Standard Pressure Levels derived from CLIMCAPS V2.1 (SNDRJ1IML2PLEVCPS) at GES DISC version: 2.1"
        )

    SNDRJ1IML2CCPRET_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDRJ1IML2CCPRET_2",
            provider="GES_DISC", 
            shortname="SNDRJ1IML2CCPRET",
            version="2",
            description="Sounder SIPS: JPSS-1 CrIS Level 2 CLIMCAPS: Atmosphere cloud and surface geophysical state V2 (SNDRJ1IML2CCPRET) at GES DISC version: 2"
        )

    SNDRJ1IML2CCPCCR_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDRJ1IML2CCPCCR_2",
            provider="GES_DISC", 
            shortname="SNDRJ1IML2CCPCCR",
            version="2",
            description="Sounder SIPS: JPSS-1 CrIS Level 2 CLIMCAPS: Cloud Cleared Radiances V2 (SNDRJ1IML2CCPCCR) at GES DISC version: 2"
        )

    SNDRJ1IML3CDCCP_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDRJ1IML3CDCCP_2",
            provider="GES_DISC", 
            shortname="SNDRJ1IML3CDCCP",
            version="2",
            description="Sounder SIPS: JPSS-1 CrIS Level 3 Comprehensive Quality Control Gridded Daily CLIMCAPS V2 (SNDRJ1IML3CDCCP) at GES DISC version: 2"
        )

    SNDRJ1IML3CMCCP_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDRJ1IML3CMCCP_2",
            provider="GES_DISC", 
            shortname="SNDRJ1IML3CMCCP",
            version="2",
            description="Sounder SIPS: JPSS-1 CrIS Level 3 Comprehensive Quality Control Gridded Monthly CLIMCAPS V2 (SNDRJ1IML3CMCCP) at GES DISC version: 2"
        )

    SNDRJ1IML3SDCCP_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDRJ1IML3SDCCP_2",
            provider="GES_DISC", 
            shortname="SNDRJ1IML3SDCCP",
            version="2",
            description="Sounder SIPS: JPSS-1 CrIS Level 3 Specific Quality Control Gridded Daily CLIMCAPS V2 (SNDRJ1IML3SDCCP) at GES DISC version: 2"
        )

    SNDRJ1IML3SMCCP_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDRJ1IML3SMCCP_2",
            provider="GES_DISC", 
            shortname="SNDRJ1IML3SMCCP",
            version="2",
            description="Sounder SIPS: JPSS-1 CrIS Level 3 Specific Quality Control Gridded Monthly CLIMCAPS V2 (SNDRJ1IML3SMCCP) at GES DISC version: 2"
        )

    SNDR13CHRP1_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDR13CHRP1_2",
            provider="GES_DISC", 
            shortname="SNDR13CHRP1",
            version="2",
            description="Sounder SIPS: Sun Synchronous 13:30 orbit Climate Hyperspectral InfraRed Product (CHIRP): Calibrated Radiances from EOS-Aqua, S-NPP, JPSS-1/NOAA-20, V2 (SNDR13CHRP1) at GES DISC version: 2"
        )

    SNDR13CHRP1AQCAL_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDR13CHRP1AQCal_2",
            provider="GES_DISC", 
            shortname="SNDR13CHRP1AQCal",
            version="2",
            description="Sounder SIPS: Sun Synchronous 13:30 orbit Climate Hyperspectral InfraRed Product (CHIRP): Calibrated Radiances from EOS-Aqua, V2 (SNDR13CHRP1AQCal) at GES DISC version: 2"
        )

    SNDR13CHRP1J1CAL_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDR13CHRP1J1Cal_2",
            provider="GES_DISC", 
            shortname="SNDR13CHRP1J1Cal",
            version="2",
            description="Sounder SIPS: Sun Synchronous 13:30 orbit Climate Hyperspectral InfraRed Product (CHIRP): Calibrated Radiances from JPSS-1/NOAA-20, V2 (SNDR13CHRP1J1Cal) at GES DISC version: 2"
        )

    SNDR13CHRP1SNCAL_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDR13CHRP1SNCal_2",
            provider="GES_DISC", 
            shortname="SNDR13CHRP1SNCal",
            version="2",
            description="Sounder SIPS: Sun Synchronous 13:30 orbit Climate Hyperspectral InfraRed Product (CHIRP): Calibrated Radiances from S-NPP, V2 (SNDR13CHRP1SNCal) at GES DISC version: 2"
        )

    SNDRSNML2RMS_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDRSNML2RMS_1",
            provider="GES_DISC", 
            shortname="SNDRSNML2RMS",
            version="1",
            description="Sounder SIPS: Suomi NPP ATMS Level 2 RAMSES II: Atmosphere, cloud and surface geophysical state V1 (SNDRSNML2RMS) at GES DISC version: 1"
        )

    SNDRSNML2RMS_V3_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDRSNML2RMS_3",
            provider="GES_DISC", 
            shortname="SNDRSNML2RMS",
            version="3",
            description="Sounder SIPS: Suomi NPP ATMS Level 2 RAMSES2 Standard: Atmosphere, precipitation and surface geophysical state, V3 (SNDRSNML2RMS ) at GES DISC version: 3"
        )

    SNDRSNML2RMSSUP_V3_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDRSNML2RMSSUP_3",
            provider="GES_DISC", 
            shortname="SNDRSNML2RMSSUP",
            version="3",
            description="Sounder SIPS: Suomi NPP ATMS Level 2 RAMSES2 Support V3 (SNDRSNML2RMSSUP) at GES DISC version: 3"
        )

    SNDRSNML3DRMS_V3_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDRSNML3DRMS_3",
            provider="GES_DISC", 
            shortname="SNDRSNML3DRMS",
            version="3",
            description="Sounder SIPS: Suomi NPP ATMS Level 3 RAMSES2 Standard Gridded Daily V3 at GES DISC version: 3"
        )

    SNDRSNML3MRMS_V3_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDRSNML3MRMS_3",
            provider="GES_DISC", 
            shortname="SNDRSNML3MRMS",
            version="3",
            description="Sounder SIPS: Suomi NPP ATMS Level 3 RAMSES2 Standard Gridded Monthly V3 at GES DISC version: 3"
        )

    SNDRSNIML2CHTRETN_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDRSNIML2CHTRETN_1",
            provider="GES_DISC", 
            shortname="SNDRSNIML2CHTRETN",
            version="1",
            description="Sounder SIPS: Suomi NPP CrIMSS Level 2 CHART Normal Spectral Resolution: Atmosphere, cloud and surface geophysical state V1 version: 1"
        )

    SNDRSNIML2CHTCCRN_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDRSNIML2CHTCCRN_1",
            provider="GES_DISC", 
            shortname="SNDRSNIML2CHTCCRN",
            version="1",
            description="Sounder SIPS: Suomi NPP CrIMSS Level 2 CHART Normal Spectral Resolution: Cloud Cleared Radiances V1 version: 1"
        )

    SNDRSNIML2CCPRET_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDRSNIML2CCPRET_2",
            provider="GES_DISC", 
            shortname="SNDRSNIML2CCPRET",
            version="2",
            description="Sounder SIPS: Suomi NPP CrIMSS Level 2 CLIMCAPS Full Spectral Resolution: Atmosphere cloud and surface geophysical state V2 (SNDRSNIML2CCPRET) at GES DISC version: 2"
        )

    SNDRSNIML2PLEVCPS_V21_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDRSNIML2PLEVCPS_2.1",
            provider="GES_DISC", 
            shortname="SNDRSNIML2PLEVCPS",
            version="2.1",
            description="Sounder SIPS: Suomi NPP CrIMSS Level 2 CLIMCAPS Full Spectral Resolution: Atmospheric state at Standard Pressure Levels derived from CLIMCAPS V2.1 (SNDRSNIML2PLEVCPS) at GES DISC version: 2.1"
        )

    SNDRSNIML2CCPCCR_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDRSNIML2CCPCCR_2",
            provider="GES_DISC", 
            shortname="SNDRSNIML2CCPCCR",
            version="2",
            description="Sounder SIPS: Suomi NPP CrIMSS Level 2 CLIMCAPS Full Spectral Resolution: Cloud Cleared Radiances V2 (SNDRSNIML2CCPCCR) at GES DISC version: 2"
        )

    SNDRSNIML2CPS_V21_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDRSNIML2CPS_2.1",
            provider="GES_DISC", 
            shortname="SNDRSNIML2CPS",
            version="2.1",
            description="Sounder SIPS: Suomi NPP CrIMSS Level 2 CLIMCAPS Full Spectral Resolution: retrieved atmospheric state V2.1 (SNDRSNIML2CPS) at GES DISC version: 2.1"
        )

    SNDRSNIML2CCPRETN_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDRSNIML2CCPRETN_2",
            provider="GES_DISC", 
            shortname="SNDRSNIML2CCPRETN",
            version="2",
            description="Sounder SIPS: Suomi NPP CrIMSS Level 2 CLIMCAPS Normal Spectral Resolution: Atmosphere cloud and surface geophysical state V2 (SNDRSNIML2CCPRETN) at GES DISC version: 2"
        )

    SNDRSNIML2PLEVCPSN_V21_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDRSNIML2PLEVCPSN_2.1",
            provider="GES_DISC", 
            shortname="SNDRSNIML2PLEVCPSN",
            version="2.1",
            description="Sounder SIPS: Suomi NPP CrIMSS Level 2 CLIMCAPS Normal Spectral Resolution: Atmospheric state at Standard Pressure Levels derived from CLIMCAPS V2.1 (SNDRSNIML2PLEVCPSN) at GES DISC version: 2.1"
        )

    SNDRSNIML2CCPCCRN_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDRSNIML2CCPCCRN_2",
            provider="GES_DISC", 
            shortname="SNDRSNIML2CCPCCRN",
            version="2",
            description="Sounder SIPS: Suomi NPP CrIMSS Level 2 CLIMCAPS Normal Spectral Resolution: Cloud Cleared Radiances V2 (SNDRSNIML2CCPCCRN) at GES DISC version: 2"
        )

    SNDRSNIML2CPSN_V21_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDRSNIML2CPSN_2.1",
            provider="GES_DISC", 
            shortname="SNDRSNIML2CPSN",
            version="2.1",
            description="Sounder SIPS: Suomi NPP CrIMSS Level 2 CLIMCAPS Normal Spectral Resolution: retrieved atmospheric state V2.1 (SNDRSNIML2CPSN) at GES DISC version: 2.1"
        )

    SNDRSNIML2SFSPRET_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDRSNIML2SFSPRET_2",
            provider="GES_DISC", 
            shortname="SNDRSNIML2SFSPRET",
            version="2",
            description="Sounder SIPS: Suomi NPP CrIMSS Level 2 SiFSAP Standard: Atmosphere cloud and surface geophysical state per footprint V2 (at GESDISC) version: 2"
        )

    SNDRSNIML2SFSPSUP_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDRSNIML2SFSPSUP_2",
            provider="GES_DISC", 
            shortname="SNDRSNIML2SFSPSUP",
            version="2",
            description="Sounder SIPS: Suomi NPP CrIMSS Level 2 SiFSAP Support: Atmosphere cloud and surface geophysical state per footprint V2 at GES DISC version: 2"
        )

    SNDRSNIML3CDCHTN_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDRSNIML3CDCHTN_1",
            provider="GES_DISC", 
            shortname="SNDRSNIML3CDCHTN",
            version="1",
            description="Sounder SIPS: Suomi NPP CrIMSS Level 3 Comprehensive Quality Control Gridded Daily CHART Normal Spectral Resolution V1 version: 1"
        )

    SNDRSNIML3CDCCP_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDRSNIML3CDCCP_2",
            provider="GES_DISC", 
            shortname="SNDRSNIML3CDCCP",
            version="2",
            description="Sounder SIPS: Suomi NPP CrIMSS Level 3 Comprehensive Quality Control Gridded Daily CLIMCAPS Full Spectral Resolution V2 (SNDRSNIML3CDCCP) at GES DISC version: 2"
        )

    SNDRSNIML3CDCCPN_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDRSNIML3CDCCPN_2",
            provider="GES_DISC", 
            shortname="SNDRSNIML3CDCCPN",
            version="2",
            description="Sounder SIPS: Suomi NPP CrIMSS Level 3 Comprehensive Quality Control Gridded Daily CLIMCAPS Normal Spectral Resolution V2 (SNDRSNIML3CDCCPN) at GES DISC version: 2"
        )

    SNDRSNIML3CMCHTN_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDRSNIML3CMCHTN_1",
            provider="GES_DISC", 
            shortname="SNDRSNIML3CMCHTN",
            version="1",
            description="Sounder SIPS: Suomi NPP CrIMSS Level 3 Comprehensive Quality Control Gridded Monthly CHART Normal Spectral Resolution V1 version: 1"
        )

    SNDRSNIML3CMCCP_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDRSNIML3CMCCP_2",
            provider="GES_DISC", 
            shortname="SNDRSNIML3CMCCP",
            version="2",
            description="Sounder SIPS: Suomi NPP CrIMSS Level 3 Comprehensive Quality Control Gridded Monthly CLIMCAPS Full Spectral Resolution V2 (SNDRSNIML3CMCCP) at GES DISC version: 2"
        )

    SNDRSNIML3CMCCPN_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDRSNIML3CMCCPN_2",
            provider="GES_DISC", 
            shortname="SNDRSNIML3CMCCPN",
            version="2",
            description="Sounder SIPS: Suomi NPP CrIMSS Level 3 Comprehensive Quality Control Gridded Monthly CLIMCAPS Normal Spectral Resolution V2 (SNDRSNIML3CMCCPN) at GES DISC version: 2"
        )

    SNDRSNIML3SDCHTN_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDRSNIML3SDCHTN_1",
            provider="GES_DISC", 
            shortname="SNDRSNIML3SDCHTN",
            version="1",
            description="Sounder SIPS: Suomi NPP CrIMSS Level 3 Specific Quality Control Gridded Daily CHART Normal Spectral Resolution V1 version: 1"
        )

    SNDRSNIML3SDCCP_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDRSNIML3SDCCP_2",
            provider="GES_DISC", 
            shortname="SNDRSNIML3SDCCP",
            version="2",
            description="Sounder SIPS: Suomi NPP CrIMSS Level 3 Specific Quality Control Gridded Daily CLIMCAPS Full Spectral Resolution V2 (SNDRSNIML3SDCCP) at GES DISC version: 2"
        )

    SNDRSNIML3SDCCPN_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDRSNIML3SDCCPN_2",
            provider="GES_DISC", 
            shortname="SNDRSNIML3SDCCPN",
            version="2",
            description="Sounder SIPS: Suomi NPP CrIMSS Level 3 Specific Quality Control Gridded Daily CLIMCAPS Normal Spectral Resolution V2 (SNDRSNIML3SDCCPN) at GES DISC version: 2"
        )

    SNDRSNIML3SDSFSP_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDRSNIML3SDSFSP_2",
            provider="GES_DISC", 
            shortname="SNDRSNIML3SDSFSP",
            version="2",
            description="Sounder SIPS: Suomi NPP CrIMSS Level 3 Specific Quality Control Gridded Daily SiFSAP V2 (SNDRSNIML3SDSFSP) at GES DISC version: 2"
        )

    SNDRSNIML3SMCHTN_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDRSNIML3SMCHTN_1",
            provider="GES_DISC", 
            shortname="SNDRSNIML3SMCHTN",
            version="1",
            description="Sounder SIPS: Suomi NPP CrIMSS Level 3 Specific Quality Control Gridded Monthly CHART Normal Spectral Resolution V1 version: 1"
        )

    SNDRSNIML3SMCCP_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDRSNIML3SMCCP_2",
            provider="GES_DISC", 
            shortname="SNDRSNIML3SMCCP",
            version="2",
            description="Sounder SIPS: Suomi NPP CrIMSS Level 3 Specific Quality Control Gridded Monthly CLIMCAPS Full Spectral Resolution V2 (SNDRSNIML3SMCCP) at GES DISC version: 2"
        )

    SNDRSNIML3SMCCPN_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDRSNIML3SMCCPN_2",
            provider="GES_DISC", 
            shortname="SNDRSNIML3SMCCPN",
            version="2",
            description="Sounder SIPS: Suomi NPP CrIMSS Level 3 Specific Quality Control Gridded Monthly CLIMCAPS Normal Spectral Resolution V2 (SNDRSNIML3SMCCPN) at GES DISC version: 2"
        )

    SNDRSNIML3SMSFSP_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDRSNIML3SMSFSP_2",
            provider="GES_DISC", 
            shortname="SNDRSNIML3SMSFSP",
            version="2",
            description="Sounder SIPS: Suomi NPP CrIMSS Level 3 Specific Quality Control Gridded Monthly SiFSAP V2 (SNDRSNIML3SMSFSP) at GES DISC version: 2"
        )

    SNDRSNIL1BCALSUBRNDN_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDRSNIL1BCALSUBRNDN_2",
            provider="GES_DISC", 
            shortname="SNDRSNIL1BCALSUBRNDN",
            version="2",
            description="Sounder SIPS: Suomi NPP CrIS Level-1B NSR Calibration Subset: Random full spectra V2 (SNDRSNIL1BCALSUBRNDN) at GES DISC version: 2"
        )

    SNDRSNIL1BCALSUBSUMN_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDRSNIL1BCALSUBSUMN_2",
            provider="GES_DISC", 
            shortname="SNDRSNIL1BCALSUBSUMN",
            version="2",
            description="Sounder SIPS: Suomi NPP CrIS Level-1B NSR Calibration Subset: Summary V2 (SNDRSNIL1BCALSUBSUMN) at GES DISC version: 2"
        )

    SNDRSNATMSMAP_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDRSNATMSMAP_1",
            provider="GES_DISC", 
            shortname="SNDRSNATMSMAP",
            version="1",
            description="Sounder SIPS: Suomi-NPP ATMS Level 1 Daily Polygon Granule Map at GES DISC version: 1"
        )

    SNDRAQIL3SSDFCNSAT_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDRAQIL3SSDFCNSAT_2",
            provider="GES_DISC", 
            shortname="SNDRAQIL3SSDFCNSAT",
            version="2",
            description="Spatial Statistical Data Fusion (SSDF) Level 3: CONUS Near-Surface Atmospheric Temperature from Aqua AIRS, V2 (SNDRAQIL3SSDFCNSAT) version: 2"
        )

    SNDR13IML3SSDFCNSAT_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDR13IML3SSDFCNSAT_2",
            provider="GES_DISC", 
            shortname="SNDR13IML3SSDFCNSAT",
            version="2",
            description="Spatial Statistical Data Fusion (SSDF) Level 3: CONUS Near-Surface Atmospheric Temperature from SNPP CrIMSS and Aqua AIRS, V2 (SNDR13IML3SSDFCNSAT) version: 2"
        )

    SNDRAQIL3SSDFCVPD_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDRAQIL3SSDFCVPD_2",
            provider="GES_DISC", 
            shortname="SNDRAQIL3SSDFCVPD",
            version="2",
            description="Spatial Statistical Data Fusion (SSDF) Level 3: CONUS Near-Surface Vapor Pressure Deficit from Aqua AIRS, V2 (SNDRAQIL3SSDFCVPD) version: 2"
        )

    SNDR13IML3SSDFCVPD_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNDR13IML3SSDFCVPD_2",
            provider="GES_DISC", 
            shortname="SNDR13IML3SSDFCVPD",
            version="2",
            description="Spatial Statistical Data Fusion (SSDF) Level 3: CONUS Near-Surface Vapor Pressure Deficit from SNPP CrIMSS and Aqua AIRS, V2 (SNDR13IML3SSDFCVPD) version: 2"
        )

    SNPPATMSL1B_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNPPATMSL1B_2",
            provider="GES_DISC", 
            shortname="SNPPATMSL1B",
            version="2",
            description="Suomi NPP ATMS Sounder Science Investigator-led Processing System (SIPS) Level 1B Brightness Temperature V2 (SNPPATMSL1B) at GES DISC version: 2"
        )

    SNPPATMSL1B_V3_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNPPATMSL1B_3",
            provider="GES_DISC", 
            shortname="SNPPATMSL1B",
            version="3",
            description="Suomi NPP ATMS Sounder Science Investigator-led Processing System (SIPS) Level 1B Brightness Temperature V3 (SNPPATMSL1B) at GES DISC version: 3"
        )

    SNPPCRISL1B_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNPPCrISL1B_2",
            provider="GES_DISC", 
            shortname="SNPPCrISL1B",
            version="2",
            description="Suomi NPP CrIS Level 1B Full Spectral Resolution V2 (SNPPCrISL1B) at GES DISC version: 2"
        )

    SNPPCRISL1B_V3_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNPPCrISL1B_3",
            provider="GES_DISC", 
            shortname="SNPPCrISL1B",
            version="3",
            description="Suomi NPP CrIS Level 1B Full Spectral Resolution V3 (SNPPCrISL1B) at GES DISC version: 3"
        )

    SNPPCRISL1BNSR_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNPPCrISL1BNSR_2",
            provider="GES_DISC", 
            shortname="SNPPCrISL1BNSR",
            version="2",
            description="Suomi NPP CrIS Level 1B Normal Spectral Resolution V2 (SNPPCrISL1BNSR) at GES DISC version: 2"
        )

    SNPPCRISL1BNSR_V3_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_SNPPCrISL1BNSR_3",
            provider="GES_DISC", 
            shortname="SNPPCrISL1BNSR",
            version="3",
            description="Suomi NPP CrIS Level 1B Normal Spectral Resolution V3 (SNPPCrISL1BNSR) at GES DISC version: 3"
        )

    TCTE3TSI6_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TCTE3TSI6_004",
            provider="GES_DISC", 
            shortname="TCTE3TSI6",
            version="004",
            description="TCTE Level 3 Total Solar Irradiance 6-Hour Means V004 (TCTE3TSI6) at GES DISC version: 004"
        )

    TCTE3TSID_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TCTE3TSID_004",
            provider="GES_DISC", 
            shortname="TCTE3TSID",
            version="004",
            description="TCTE Level 3 Total Solar Irradiance Daily Means V004 (TCTE3TSID) at GES DISC version: 004"
        )

    THIRN4IMCH67_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_THIRN4IMCH67_001",
            provider="GES_DISC", 
            shortname="THIRN4IMCH67",
            version="001",
            description="THIR/Nimbus-4 Images of Daytime and Nighttime Brightness Temperature at 6.7 microns on 70 mm Film V001 (THIRN4IMCH67) at GES DISC version: 001"
        )

    THIRN4L1CH115_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_THIRN4L1CH115_001",
            provider="GES_DISC", 
            shortname="THIRN4L1CH115",
            version="001",
            description="THIR/Nimbus-4 Level 1 Meteorological Radiation Data at 11.5 microns V001 (THIRN4L1CH115) at GES DISC version: 001"
        )

    THIRN4L1CH67_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_THIRN4L1CH67_001",
            provider="GES_DISC", 
            shortname="THIRN4L1CH67",
            version="001",
            description="THIR/Nimbus-4 Level 1 Meteorological Radiation Data at 6.7 microns V001 (THIRN4L1CH67) at GES DISC version: 001"
        )

    THIRN5L1CH115_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_THIRN5L1CH115_001",
            provider="GES_DISC", 
            shortname="THIRN5L1CH115",
            version="001",
            description="THIR/Nimbus-5 Level 1 Meteorological Radiation Data at 11.5 microns V001 (THIRN5L1CH115) at GES DISC version: 001"
        )

    THIRN5L1CH67_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_THIRN5L1CH67_001",
            provider="GES_DISC", 
            shortname="THIRN5L1CH67",
            version="001",
            description="THIR/Nimbus-5 Level 1 Meteorological Radiation Data at 6.7 microns V001 (THIRN5L1CH67) at GES DISC version: 001"
        )

    THIRN6IM_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_THIRN6IM_001",
            provider="GES_DISC", 
            shortname="THIRN6IM",
            version="001",
            description="THIR/Nimbus-6 Images of Daytime and Nighttime Brightness Temperature on 70 mm Film V001 (THIRN6IM) at GES DISC version: 001"
        )

    THIRN6L1CH115_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_THIRN6L1CH115_001",
            provider="GES_DISC", 
            shortname="THIRN6L1CH115",
            version="001",
            description="THIR/Nimbus-6 Level 1 Meteorological Radiation Data at 11.5 microns V001 (THIRN6L1CH115) at GES DISC version: 001"
        )

    THIRN6L1CH67_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_THIRN6L1CH67_001",
            provider="GES_DISC", 
            shortname="THIRN6L1CH67",
            version="001",
            description="THIR/Nimbus-6 Level 1 Meteorological Radiation Data at 6.7 microns V001 (THIRN6L1CH67) at GES DISC version: 001"
        )

    THIRN7IM_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_THIRN7IM_001",
            provider="GES_DISC", 
            shortname="THIRN7IM",
            version="001",
            description="THIR/Nimbus-7 Images of Daytime and Nighttime Brightness Temperature on 70 mm Film V001 (THIRN7IM) at GES DISC version: 001"
        )

    THIRN7L1CLDT_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_THIRN7L1CLDT_001",
            provider="GES_DISC", 
            shortname="THIRN7L1CLDT",
            version="001",
            description="THIR/Nimbus-7 Level 1 Calibrated Located Radiation Data at 6.7 and 11.5 microns V001 (THIRN7L1CLDT) at GES DISC version: 001"
        )

    THIRN7L1BCLT_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_THIRN7L1BCLT_001",
            provider="GES_DISC", 
            shortname="THIRN7L1BCLT",
            version="001",
            description="THIR/Nimbus-7 Level 1 Cloud Data for SBUV/TOMS V001 (THIRN7L1BCLT) at GES DISC version: 001"
        )

    TIROS2L1FMRT_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TIROS2L1FMRT_001",
            provider="GES_DISC", 
            shortname="TIROS2L1FMRT",
            version="001",
            description="TIROS-2 Medium-Resolution Scanning Radiometer Level 1 Final Meteorological Radiation Data V001 (TIROS2L1FMRT) at GES DISC version: 001"
        )

    TIROS3L1ORT_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TIROS3L1ORT_001",
            provider="GES_DISC", 
            shortname="TIROS3L1ORT",
            version="001",
            description="TIROS-3 Low-Resolution Omnidirectional Radiometer Level 1 Temperature Data V001 (TIROS3L1ORT) at GES DISC version: 001"
        )

    TIROS3L1FMRT_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TIROS3L1FMRT_001",
            provider="GES_DISC", 
            shortname="TIROS3L1FMRT",
            version="001",
            description="TIROS-3 Medium-Resolution Scanning Radiometer Level 1 Final Meteorological Radiation Data V001 (TIROS3L1FMRT) at GES DISC version: 001"
        )

    TIROS4L1ORR_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TIROS4L1ORR_001",
            provider="GES_DISC", 
            shortname="TIROS4L1ORR",
            version="001",
            description="TIROS-4 Low-Resolution Omnidirectional Radiometer Level 1 Radiance Data V001 (TIROS4L1ORR) at GES DISC version: 001"
        )

    TIROS4L1ORT_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TIROS4L1ORT_001",
            provider="GES_DISC", 
            shortname="TIROS4L1ORT",
            version="001",
            description="TIROS-4 Low-Resolution Omnidirectional Radiometer Level 1 Temperature Data V001 (TIROS4L1ORT) at GES DISC version: 001"
        )

    TIROS4L1FMRT_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TIROS4L1FMRT_001",
            provider="GES_DISC", 
            shortname="TIROS4L1FMRT",
            version="001",
            description="TIROS-4 Medium-Resolution Scanning Radiometer Level 1 Final Meteorological Radiation Data V001 (TIROS4L1FMRT) at GES DISC version: 001"
        )

    TIROS7L1FMRT_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TIROS7L1FMRT_001",
            provider="GES_DISC", 
            shortname="TIROS7L1FMRT",
            version="001",
            description="TIROS-7 Medium-Resolution Scanning Radiometer Level 1 Final Meteorological Radiation Data V001 (TIROS7L1FMRT) at GES DISC version: 001"
        )

    WC_MULTISEN_PREC_025_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_WC_MULTISEN_PREC_025_001",
            provider="GES_DISC", 
            shortname="WC_MULTISEN_PREC_025",
            version="001",
            description="TMI/TRMM precipitation and uncertainty (TMPA) L3 3 hour 0.25 degree x 0.25 degree V001 (WC_MULTISEN_PREC_025) at GES DISC version: 001"
        )

    LPRM_TMI_SOILM2_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_LPRM_TMI_SOILM2_001",
            provider="GES_DISC", 
            shortname="LPRM_TMI_SOILM2",
            version="001",
            description="TMI/TRMM surface soil moisture (LPRM) L2 V001 (LPRM_TMI_SOILM2) at GES DISC version: 001"
        )

    LPRM_TMI_DY_SOILM3_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_LPRM_TMI_DY_SOILM3_001",
            provider="GES_DISC", 
            shortname="LPRM_TMI_DY_SOILM3",
            version="001",
            description="TMI/TRMM surface soil moisture (LPRM) L3 1 day 25 km x 25 km daytime V001 (LPRM_TMI_DY_SOILM3) at GES DISC version: 001"
        )

    LPRM_TMI_NT_SOILM3_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_LPRM_TMI_NT_SOILM3_001",
            provider="GES_DISC", 
            shortname="LPRM_TMI_NT_SOILM3",
            version="001",
            description="TMI/TRMM surface soil moisture (LPRM) L3 1 day 25 km x 25 km nighttime V001 (LPRM_TMI_NT_SOILM3) at GES DISC version: 001"
        )

    TOMSEPL3ZTOZ_V008_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TOMSEPL3ztoz_008",
            provider="GES_DISC", 
            shortname="TOMSEPL3ztoz",
            version="008",
            description="TOMS EP Total Column Ozone Daily and Monthly Zonal Means V008 (TOMSEPL3ztoz) at GES DISC version: 008"
        )

    TOMSEPL3ZAER_V008_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TOMSEPL3zaer_008",
            provider="GES_DISC", 
            shortname="TOMSEPL3zaer",
            version="008",
            description="TOMS EP UV Aerosol Index Daily and Monthly Zonal Means V008 (TOMSEPL3zaer) at GES DISC version: 008"
        )

    TOMSEPL3ZREF_V008_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TOMSEPL3zref_008",
            provider="GES_DISC", 
            shortname="TOMSEPL3zref",
            version="008",
            description="TOMS EP UV Reflectivity Daily and Monthly Zonal Means V008 (TOMSEPL3zref) at GES DISC version: 008"
        )

    TOMSEPOVP_V008_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TOMSEPOVP_008",
            provider="GES_DISC", 
            shortname="TOMSEPOVP",
            version="008",
            description="TOMS Earth Probe Ground Station Overpass Data V008 (TOMSEPOVP) at GES DISC version: 008"
        )

    TOMSEPL3DTOZ_V008_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TOMSEPL3dtoz_008",
            provider="GES_DISC", 
            shortname="TOMSEPL3dtoz",
            version="008",
            description="TOMS Earth Probe Total Column Ozone Daily L3 Global 1 deg x 1.25 deg Lat/Lon Grid V008 (TOMSEPL3dtoz) at GES DISC version: 008"
        )

    TOMSEPL3MTOZ_V008_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TOMSEPL3mtoz_008",
            provider="GES_DISC", 
            shortname="TOMSEPL3mtoz",
            version="008",
            description="TOMS Earth Probe Total Column Ozone Monthly L3 Global 1 deg x 1.25 deg Lat/Lon Grid V008 (TOMSEPL3mtoz) at GES DISC version: 008"
        )

    TOMSEPL3DAER_V008_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TOMSEPL3daer_008",
            provider="GES_DISC", 
            shortname="TOMSEPL3daer",
            version="008",
            description="TOMS Earth Probe UV Aerosol Index Daily L3 Global 1 deg x 1.25 deg Lat/Lon Grid V008 (TOMSEPL3daer) at GES DISC version: 008"
        )

    TOMSEPL3MAER_V008_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TOMSEPL3maer_008",
            provider="GES_DISC", 
            shortname="TOMSEPL3maer",
            version="008",
            description="TOMS Earth Probe UV Aerosol Index Monthly L3 Global 1 deg x 1.25 deg Lat/Lon Grid V008 (TOMSEPL3maer) at GES DISC version: 008"
        )

    TOMSEPL3DREF_V008_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TOMSEPL3dref_008",
            provider="GES_DISC", 
            shortname="TOMSEPL3dref",
            version="008",
            description="TOMS Earth Probe UV Reflectivity Daily L3 Global 1 deg x 1.25 deg Lat/Lon Grid V008 (TOMSEPL3dref) at GES DISC version: 008"
        )

    TOMSEPL3MREF_V008_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TOMSEPL3mref_008",
            provider="GES_DISC", 
            shortname="TOMSEPL3mref",
            version="008",
            description="TOMS Earth Probe UV Reflectivity Monthly L3 Global 1 deg x 1.25 deg Lat/Lon Grid V008 (TOMSEPL3mref) at GES DISC version: 008"
        )

    TOMSEPL3DERY_V008_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TOMSEPL3dery_008",
            provider="GES_DISC", 
            shortname="TOMSEPL3dery",
            version="008",
            description="TOMS Earth Probe UV-B Erythemal Local Noon Irradiance Daily L3 Global 1 deg x 1.25 deg Lat/Lon Grid V008 (TOMSEPL3dery) at GES DISC version: 008"
        )

    TOMSEPL3MERY_V008_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TOMSEPL3mery_008",
            provider="GES_DISC", 
            shortname="TOMSEPL3mery",
            version="008",
            description="TOMS Earth Probe UV-B Erythemal Local Noon Irradiance Monthly L3 Global 1 deg x 1.25 deg Lat/Lon Grid V008 (TOMSEPL3mery) at GES DISC version: 008"
        )

    TOMSEPL2_V008_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TOMSEPL2_008",
            provider="GES_DISC", 
            shortname="TOMSEPL2",
            version="008",
            description="TOMS Earth-Probe Ozone (O3) Total Column 1-Orbit L2 Swath 50 x 50 km V008 (TOMSEPL2) at GES DISC version: 008"
        )

    TOMSEPL3_V008_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TOMSEPL3_008",
            provider="GES_DISC", 
            shortname="TOMSEPL3",
            version="008",
            description="TOMS Earth-Probe Total Ozone (O3) Aerosol Index UV-Reflectivity UV-B Erythemal Irradiances Daily L3 Global 1 deg x 1.25 deg V008 (TOMSEPL3) at GES DISC version: 008"
        )

    TOMSM3OVP_V008_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TOMSM3OVP_008",
            provider="GES_DISC", 
            shortname="TOMSM3OVP",
            version="008",
            description="TOMS Meteor-3 Ground Station Overpass Data V008 (TOMSM3OVP) at GES DISC version: 008"
        )

    TOMSM3L3DTOZ_V008_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TOMSM3L3dtoz_008",
            provider="GES_DISC", 
            shortname="TOMSM3L3dtoz",
            version="008",
            description="TOMS Meteor-3 Total Column Ozone Daily L3 Global 1 deg x 1.25 deg Lat/Lon Grid V008 (TOMSM3L3dtoz) at GES DISC version: 008"
        )

    TOMSM3L3_V008_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TOMSM3L3_008",
            provider="GES_DISC", 
            shortname="TOMSM3L3",
            version="008",
            description="TOMS Meteor-3 Total Ozone UV-Reflectivity Daily L3 Global 1 deg x 1.25 deg V008 (TOMSM3L3) at GES DISC version: 008"
        )

    TOMSM3L3DREF_V008_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TOMSM3L3dref_008",
            provider="GES_DISC", 
            shortname="TOMSM3L3dref",
            version="008",
            description="TOMS Meteor-3 UV-Reflectivity Daily L3 Global 1 deg x 1.25 deg Lat/Lon Grid V008 (TOMSM3L3dref) at GES DISC version: 008"
        )

    TOMSN7OVP_V008_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TOMSN7OVP_008",
            provider="GES_DISC", 
            shortname="TOMSN7OVP",
            version="008",
            description="TOMS Nimbus-7 Ground Station Overpass Data V008 (TOMSN7OVP) at GES DISC version: 008"
        )

    TOMSN7L2_V008_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TOMSN7L2_008",
            provider="GES_DISC", 
            shortname="TOMSN7L2",
            version="008",
            description="TOMS Nimbus-7 Ozone (O3) Total Column 1-Orbit L2 Swath 50 km x 50 km V008 (TOMSN7L2) at GES DISC version: 008"
        )

    TOMSN7L3DTOZ_V008_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TOMSN7L3dtoz_008",
            provider="GES_DISC", 
            shortname="TOMSN7L3dtoz",
            version="008",
            description="TOMS Nimbus-7 Total Column Ozone Daily L3 Global 1 deg x 1.25 deg Lat/Lon Grid V008 (TOMSN7L3dtoz) at GES DISC version: 008"
        )

    TOMSN7L3ZTOZ_V008_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TOMSN7L3ztoz_008",
            provider="GES_DISC", 
            shortname="TOMSN7L3ztoz",
            version="008",
            description="TOMS Nimbus-7 Total Column Ozone Daily and Monthly Zonal Means V008 (TOMSN7L3ztoz) at GES DISC version: 008"
        )

    TOMSN7L3MTOZ_V008_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TOMSN7L3mtoz_008",
            provider="GES_DISC", 
            shortname="TOMSN7L3mtoz",
            version="008",
            description="TOMS Nimbus-7 Total Column Ozone Monthly L3 Global 1 deg x 1.25 deg Lat/Lon Grid V008 (TOMSN7L3mtoz) at GES DISC version: 008"
        )

    TOMSN7L3_V008_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TOMSN7L3_008",
            provider="GES_DISC", 
            shortname="TOMSN7L3",
            version="008",
            description="TOMS Nimbus-7 Total Ozone Aerosol Index UV-Reflectivity UV-B Erythemal Irradiances Daily L3 Global 1 deg x 1.25 deg V008 (TOMSN7L3) at GES DISC version: 008"
        )

    TOMSN7L3DAER_V008_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TOMSN7L3daer_008",
            provider="GES_DISC", 
            shortname="TOMSN7L3daer",
            version="008",
            description="TOMS Nimbus-7 UV Aerosol Index Daily L3 Global 1 deg x 1.25 deg Lat/Lon Grid V008 (TOMSN7L3daer) at GES DISC version: 008"
        )

    TOMSN7L3ZAER_V008_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TOMSN7L3zaer_008",
            provider="GES_DISC", 
            shortname="TOMSN7L3zaer",
            version="008",
            description="TOMS Nimbus-7 UV Aerosol Index Daily and Monthly Zonal Means V008 (TOMSN7L3zaer) at GES DISC version: 008"
        )

    TOMSN7L3MAER_V008_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TOMSN7L3maer_008",
            provider="GES_DISC", 
            shortname="TOMSN7L3maer",
            version="008",
            description="TOMS Nimbus-7 UV Aerosol Index Monthly L3 Global 1 deg x 1.25 deg Lat/Lon Grid V008 (TOMSN7L3maer) at GES DISC version: 008"
        )

    TOMSN7L3DREF_V008_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TOMSN7L3dref_008",
            provider="GES_DISC", 
            shortname="TOMSN7L3dref",
            version="008",
            description="TOMS Nimbus-7 UV Reflectivity Daily L3 Global 1 deg x 1.25 deg Lat/Lon Grid V008 (TOMSN7L3dref) at GES DISC version: 008"
        )

    TOMSN7L3ZREF_V008_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TOMSN7L3zref_008",
            provider="GES_DISC", 
            shortname="TOMSN7L3zref",
            version="008",
            description="TOMS Nimbus-7 UV Reflectivity Daily and Monthly Zonal Means V008 (TOMSN7L3zref) at GES DISC version: 008"
        )

    TOMSN7L3MREF_V008_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TOMSN7L3mref_008",
            provider="GES_DISC", 
            shortname="TOMSN7L3mref",
            version="008",
            description="TOMS Nimbus-7 UV Reflectivity Monthly L3 Global 1 deg x 1.25 deg Lat/Lon Grid V008 (TOMSN7L3mref) at GES DISC version: 008"
        )

    TOMSN7L3DERY_V008_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TOMSN7L3dery_008",
            provider="GES_DISC", 
            shortname="TOMSN7L3dery",
            version="008",
            description="TOMS Nimbus-7 UV-B Erythemal Local Noon Irradiance Daily L3 Global 1 deg x 1.25 deg Lat/Lon Grid V008 (TOMSN7L3dery) at GES DISC version: 008"
        )

    TOMSN7L3MERY_V008_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TOMSN7L3mery_008",
            provider="GES_DISC", 
            shortname="TOMSN7L3mery",
            version="008",
            description="TOMS Nimbus-7 UV-B Erythemal Local Noon Irradiance Monthly L3 Global 1 deg x 1.25 deg Lat/Lon Grid V008 (TOMSN7L3mery) at GES DISC version: 008"
        )

    TOMSEPAER_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TOMSEPAER_2",
            provider="GES_DISC", 
            shortname="TOMSEPAER",
            version="2",
            description="TOMS/EP Near UV Aerosol Index and LER 1-Orbit L2 40x40km at GES DISC version: 2"
        )

    TOMSN7SO2_V3_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TOMSN7SO2_3",
            provider="GES_DISC", 
            shortname="TOMSN7SO2",
            version="3",
            description="TOMS/N7 MS SO2 Vertical Column 1-Orbit L2 Swath 50x50 km V3 (TOMSN7SO2) at GES DISC version: 3"
        )

    TOMSN7AER_V2_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TOMSN7AER_2",
            provider="GES_DISC", 
            shortname="TOMSN7AER",
            version="2",
            description="TOMS/N7 Near UV Aerosol Index and LER 1-Orbit L2 50x50 km version: 2"
        )

    TOVSA5NG_V01_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TOVSA5NG_01",
            provider="GES_DISC", 
            shortname="TOVSA5NG",
            version="01",
            description="TOVS GLA 5 DAY GRIDS from NOAA-10 V01 (TOVSA5NG) at GES DISC version: 01"
        )

    TOVSA5NH_V01_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TOVSA5NH_01",
            provider="GES_DISC", 
            shortname="TOVSA5NH",
            version="01",
            description="TOVS GLA 5 DAY GRIDS from NOAA-11 V01 (TOVSA5NH) at GES DISC version: 01"
        )

    TOVSA5ND_V01_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TOVSA5ND_01",
            provider="GES_DISC", 
            shortname="TOVSA5ND",
            version="01",
            description="TOVS GLA 5 DAY GRIDS from NOAA-12 V01 (TOVSA5ND) at GES DISC version: 01"
        )

    TOVSA5NF_V01_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TOVSA5NF_01",
            provider="GES_DISC", 
            shortname="TOVSA5NF",
            version="01",
            description="TOVS GLA 5 DAY GRIDS from NOAA-9 V01 (TOVSA5NF) at GES DISC version: 01"
        )

    TOVSA5TN_V01_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TOVSA5TN_01",
            provider="GES_DISC", 
            shortname="TOVSA5TN",
            version="01",
            description="TOVS GLA 5 DAY GRIDS from TIROSN V01 (TOVSA5TN ) at GES DISC version: 01"
        )

    TOVSADNG_V01_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TOVSADNG_01",
            provider="GES_DISC", 
            shortname="TOVSADNG",
            version="01",
            description="TOVS GLA DAILY GRIDS from NOAA-10 V01 (TOVSADNG) at GES DISC version: 01"
        )

    TOVSADNH_V01_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TOVSADNH_01",
            provider="GES_DISC", 
            shortname="TOVSADNH",
            version="01",
            description="TOVS GLA DAILY GRIDS from NOAA-11 V01 (TOVSADNH) at GES DISC version: 01"
        )

    TOVSADND_V01_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TOVSADND_01",
            provider="GES_DISC", 
            shortname="TOVSADND",
            version="01",
            description="TOVS GLA DAILY GRIDS from NOAA-12 V01 (TOVSADND) at GES DISC version: 01"
        )

    TOVSADNF_V01_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TOVSADNF_01",
            provider="GES_DISC", 
            shortname="TOVSADNF",
            version="01",
            description="TOVS GLA DAILY GRIDS from NOAA-9 V01 (TOVSADNF) at GES DISC version: 01"
        )

    TOVSADTN_V01_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TOVSADTN_01",
            provider="GES_DISC", 
            shortname="TOVSADTN",
            version="01",
            description="TOVS GLA DAILY GRIDS from TIROSN V01 (TOVSADTN) at GES DISC version: 01"
        )

    TOVSAMNG_V02_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TOVSAMNG_02",
            provider="GES_DISC", 
            shortname="TOVSAMNG",
            version="02",
            description="TOVS GLA MONTHLY GRIDS from NOAA-10 02 (TOVSAMNG) at GES DISC version: 02"
        )

    TOVSAMNG_V01_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TOVSAMNG_01",
            provider="GES_DISC", 
            shortname="TOVSAMNG",
            version="01",
            description="TOVS GLA MONTHLY GRIDS from NOAA-10 V01 (TOVSAMNG) at GES DISC version: 01"
        )

    TOVSAMNH_V02_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TOVSAMNH_02",
            provider="GES_DISC", 
            shortname="TOVSAMNH",
            version="02",
            description="TOVS GLA MONTHLY GRIDS from NOAA-11 02 (TOVSAMNH) at GES DISC version: 02"
        )

    TOVSAMNH_V01_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TOVSAMNH_01",
            provider="GES_DISC", 
            shortname="TOVSAMNH",
            version="01",
            description="TOVS GLA MONTHLY GRIDS from NOAA-11 V01 (TOVSAMNH) at GES DISC version: 01"
        )

    TOVSAMND_V02_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TOVSAMND_02",
            provider="GES_DISC", 
            shortname="TOVSAMND",
            version="02",
            description="TOVS GLA MONTHLY GRIDS from NOAA-12 02 (TOVSAMND) at GES DISCc version: 02"
        )

    TOVSAMND_V01_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TOVSAMND_01",
            provider="GES_DISC", 
            shortname="TOVSAMND",
            version="01",
            description="TOVS GLA MONTHLY GRIDS from NOAA-12 V01 (TOVSAMND) at GES DISC version: 01"
        )

    TOVSAMNJ_V02_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TOVSAMNJ_02",
            provider="GES_DISC", 
            shortname="TOVSAMNJ",
            version="02",
            description="TOVS GLA MONTHLY GRIDS from NOAA-14 02 (TOVSAMNJ) at GES DISC version: 02"
        )

    TOVSAMNA_V02_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TOVSAMNA_02",
            provider="GES_DISC", 
            shortname="TOVSAMNA",
            version="02",
            description="TOVS GLA MONTHLY GRIDS from NOAA-6 02 (TOVSAMNA) at GES DISC version: 02"
        )

    TOVSAMNC_V02_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TOVSAMNC_02",
            provider="GES_DISC", 
            shortname="TOVSAMNC",
            version="02",
            description="TOVS GLA MONTHLY GRIDS from NOAA-7 02 (TOVSAMNC) at GES DISC version: 02"
        )

    TOVSAMNE_V02_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TOVSAMNE_02",
            provider="GES_DISC", 
            shortname="TOVSAMNE",
            version="02",
            description="TOVS GLA MONTHLY GRIDS from NOAA-8 02 (TOVSAMNE) at GES DISC version: 02"
        )

    TOVSAMNF_V02_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TOVSAMNF_02",
            provider="GES_DISC", 
            shortname="TOVSAMNF",
            version="02",
            description="TOVS GLA MONTHLY GRIDS from NOAA-9 02 (TOVSAMNF) at GES DISC version: 02"
        )

    TOVSAMNF_V01_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TOVSAMNF_01",
            provider="GES_DISC", 
            shortname="TOVSAMNF",
            version="01",
            description="TOVS GLA MONTHLY GRIDS from NOAA-9 V01 (TOVSAMNF) at GES DISC version: 01"
        )

    TOVSAMTN_V02_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TOVSAMTN_02",
            provider="GES_DISC", 
            shortname="TOVSAMTN",
            version="02",
            description="TOVS GLA MONTHLY GRIDS from TIROS-N 02 (TOVSAMTN) at GES DISC version: 02"
        )

    TOVSAMTN_V01_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TOVSAMTN_01",
            provider="GES_DISC", 
            shortname="TOVSAMTN",
            version="01",
            description="TOVS GLA MONTHLY GRIDS from TIROSN V01 (TOVSAMTN) at GES DISC version: 01"
        )

    TOVSB5NG_V01_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TOVSB5NG_01",
            provider="GES_DISC", 
            shortname="TOVSB5NG",
            version="01",
            description="TOVS LMD 5 DAY GRIDS from NOAA-10 V01 (TOVSB5NG) at GES DISC version: 01"
        )

    TOVSB5ND_V01_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TOVSB5ND_01",
            provider="GES_DISC", 
            shortname="TOVSB5ND",
            version="01",
            description="TOVS LMD 5 DAY GRIDS from NOAA-12 V01 (TOVSB5ND) at GES DISC version: 01"
        )

    TOVSBDNG_V01_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TOVSBDNG_01",
            provider="GES_DISC", 
            shortname="TOVSBDNG",
            version="01",
            description="TOVS LMD DAILY GRIDS from NOAA-10 V01 (TOVSBDNG) at GES DISC version: 01"
        )

    TOVSBDND_V01_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TOVSBDND_01",
            provider="GES_DISC", 
            shortname="TOVSBDND",
            version="01",
            description="TOVS LMD DAILY GRIDS from NOAA-12 V01 (TOVSBDND) at GES DISC version: 01"
        )

    TOVSBMNG_V01_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TOVSBMNG_01",
            provider="GES_DISC", 
            shortname="TOVSBMNG",
            version="01",
            description="TOVS LMD MONTHLY GRIDS from NOAA-10 V01 (TOVSBMNG) at GES DISC version: 01"
        )

    TOVSBMND_V01_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TOVSBMND_01",
            provider="GES_DISC", 
            shortname="TOVSBMND",
            version="01",
            description="TOVS LMD MONTHLY GRIDS from NOAA-12 V01 (TOVSBMND) at GES DISC version: 01"
        )

    TRMM_3B42_DAILY_V7_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRMM_3B42_Daily_7",
            provider="GES_DISC", 
            shortname="TRMM_3B42_Daily",
            version="7",
            description="TRMM (TMPA) Precipitation L3 1 day 0.25 degree x 0.25 degree V7 (TRMM_3B42_Daily) at GES DISC version: 7"
        )

    TRMM_3B42_V7_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRMM_3B42_7",
            provider="GES_DISC", 
            shortname="TRMM_3B42",
            version="7",
            description="TRMM (TMPA) Rainfall Estimate L3 3 hour 0.25 degree x 0.25 degree V7 (TRMM_3B42) at GES DISC version: 7"
        )

    TRMM_3B41RT_V7_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRMM_3B41RT_7",
            provider="GES_DISC", 
            shortname="TRMM_3B41RT",
            version="7",
            description="TRMM (TMPA-RT) Near Real-Time IR precipitation estimate L3 1-hour 0.25 degree x 0.25 degree V7 (TRMM_3B41RT) at GES DISC version: 7"
        )

    TRMM_3B40RT_V7_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRMM_3B40RT_7",
            provider="GES_DISC", 
            shortname="TRMM_3B40RT",
            version="7",
            description="TRMM (TMPA-RT) Near Real-Time Microwave precipitation estimate L3 3 hour 0.25 degree x 0.25 degree V7 (TRMM_3B40RT) at GES DISC version: 7"
        )

    TRMM_3B42RT_DAILY_V7_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRMM_3B42RT_Daily_7",
            provider="GES_DISC", 
            shortname="TRMM_3B42RT_Daily",
            version="7",
            description="TRMM (TMPA-RT) Near Real-Time Precipitation L3 1 day 0.25 degree x 0.25 degree V7 (TRMM_3B42RT_Daily) at GES DISC version: 7"
        )

    TRMM_3B42RT_V7_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRMM_3B42RT_7",
            provider="GES_DISC", 
            shortname="TRMM_3B42RT",
            version="7",
            description="TRMM (TMPA-RT) Near Real-Time Precipitation L3 3 hour 0.25 degree x 0.25 degree V7 (TRMM_3B42RT) at GES DISC version: 7"
        )

    TRMM_3B43_V7_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRMM_3B43_7",
            provider="GES_DISC", 
            shortname="TRMM_3B43",
            version="7",
            description="TRMM (TMPA/3B43) Rainfall Estimate L3 1 month 0.25 degree x 0.25 degree V7 (TRMM_3B43) at GES DISC version: 7"
        )

    TRMM_1A11_V7_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRMM_1A11_7",
            provider="GES_DISC", 
            shortname="TRMM_1A11",
            version="7",
            description="TRMM Attitude and TMI Packets and Header Record L1A V7 (TRMM_1A11) at GES DISC version: 7"
        )

    TRMM_1A01_V7_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRMM_1A01_7",
            provider="GES_DISC", 
            shortname="TRMM_1A01",
            version="7",
            description="TRMM Attitude and VIRS Packets and Header Record L1A V7 (TRMM_1A01) at GES DISC version: 7"
        )

    TRMM_2B31_V7_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRMM_2B31_7",
            provider="GES_DISC", 
            shortname="TRMM_2B31",
            version="7",
            description="TRMM Combined Precipitation Radar and Microwave Imager Rainfall Profile L2 1.5 hours V7 (TRMM_2B31) at GES DISC version: 7"
        )

    TRMM_CSH_V6_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRMM_CSH_6",
            provider="GES_DISC", 
            shortname="TRMM_CSH",
            version="6",
            description="TRMM Convective and Stratiform Heating L3 1 month 0.5 degree x 0.5 degree V6 (TRMM_CSH) at GES DISC version: 6"
        )

    TRMM_1C51_V7_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRMM_1C51_7",
            provider="GES_DISC", 
            shortname="TRMM_1C51",
            version="7",
            description="TRMM Ground Validation Calibrated QC Radar Reflectivity Full Volume Scan L1C 1 hour V7 (TRMM_1C51) at GES DISC version: 7"
        )

    TRMM_1C51UW_V7_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRMM_1C51UW_7",
            provider="GES_DISC", 
            shortname="TRMM_1C51UW",
            version="7",
            description="TRMM Ground Validation Calibrated QC Radar Reflectivity Full Volume Scan L1C 1 hour V7 (TRMM_1C51UW) at GES DISC version: 7"
        )

    TRMM_1B51_V7_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRMM_1B51_7",
            provider="GES_DISC", 
            shortname="TRMM_1B51",
            version="7",
            description="TRMM Ground Validation Radar Reflectivity L1B 1 hour V7 (TRMM_1B51) at GES DISC version: 7"
        )

    TRMM_BASEUW_V7_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRMM_baseUW_7",
            provider="GES_DISC", 
            shortname="TRMM_baseUW",
            version="7",
            description="TRMM Ground Validation Radar Reflectivity Single Level Cartesian Grid 1 hour V7 (TRMM_baseUW) at GES DISC version: 7"
        )

    TRMM_3A55_V7_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRMM_3A55_7",
            provider="GES_DISC", 
            shortname="TRMM_3A55",
            version="7",
            description="TRMM Ground Validation Radar Site 3D Rain Map L3 1 month 2 km V7 (TRMM_3A55) at GES DISC version: 7"
        )

    TRMM_2A55_V7_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRMM_2A55_7",
            provider="GES_DISC", 
            shortname="TRMM_2A55",
            version="7",
            description="TRMM Ground Validation Radar Site 3D Reflectivity L2 1 hour V7 (TRMM_2A55) at GES DISC version: 7"
        )

    TRMM_2A55UW_V7_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRMM_2A55UW_7",
            provider="GES_DISC", 
            shortname="TRMM_2A55UW",
            version="7",
            description="TRMM Ground Validation Radar Site 3D Reflectivity L2 1 hour V7 (TRMM_2A55UW) at GES DISC version: 7"
        )

    TRMM_2A53_V7_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRMM_2A53_7",
            provider="GES_DISC", 
            shortname="TRMM_2A53",
            version="7",
            description="TRMM Ground Validation Radar Site Rain Rate Map L2 1 hour 2 km V7 (TRMM_2A53) at GES DISC version: 7"
        )

    TRMM_2A53UW_V7_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRMM_2A53UW_7",
            provider="GES_DISC", 
            shortname="TRMM_2A53UW",
            version="7",
            description="TRMM Ground Validation Radar Site Rain Rate Map L2 1 hour 2 km V7 (TRMM_2A53UW) at GES DISC version: 7"
        )

    TRMM_3A53_V7_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRMM_3A53_7",
            provider="GES_DISC", 
            shortname="TRMM_3A53",
            version="7",
            description="TRMM Ground Validation Radar Site Rain Totals Map L3 5 days 2 km V7 (TRMM_3A53) at GES DISC version: 7"
        )

    TRMM_2A54_V7_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRMM_2A54_7",
            provider="GES_DISC", 
            shortname="TRMM_2A54",
            version="7",
            description="TRMM Ground Validation Radar Site Rain Type Map L2 1 hour 2 km V7 (TRMM_2A54) at GES DISC version: 7"
        )

    TRMM_2A54UW_V7_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRMM_2A54UW_7",
            provider="GES_DISC", 
            shortname="TRMM_2A54UW",
            version="7",
            description="TRMM Ground Validation Radar Site Rain Type Map L2 1 hour 2 km V7 (TRMM_2A54UW) at GES DISC version: 7"
        )

    TRMM_3A54_V7_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRMM_3A54_7",
            provider="GES_DISC", 
            shortname="TRMM_3A54",
            version="7",
            description="TRMM Ground Validation Radar Site Rain Type Totals Map L3 1 month 2 km V7 (TRMM_3A54) at GES DISC version: 7"
        )

    TRMM_3A54UW_V7_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRMM_3A54UW_7",
            provider="GES_DISC", 
            shortname="TRMM_3A54UW",
            version="7",
            description="TRMM Ground Validation Radar Site Rain Type Totals Map L3 1 month 2 km V7 (TRMM_3A54UW) at GES DISC version: 7"
        )

    TRMM_2A52_V7_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRMM_2A52_7",
            provider="GES_DISC", 
            shortname="TRMM_2A52",
            version="7",
            description="TRMM Ground Validation Rain Existence L2 1 month V7 (TRMM_2A52) at GES DISC version: 7"
        )

    TRMM_2A56_V7_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRMM_2A56_7",
            provider="GES_DISC", 
            shortname="TRMM_2A56",
            version="7",
            description="TRMM Ground Validation Rain Gauge Rain Rate L2 1 month V7 (TRMM_2A56) at GES DISC version: 7"
        )

    TRMM_1B11_V7_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRMM_1B11_7",
            provider="GES_DISC", 
            shortname="TRMM_1B11",
            version="7",
            description="TRMM Microwave Imager Calibrated Radiances L1B 1.5 hours V7 (TRMM_1B11) at GES DISC version: 7"
        )

    TRMM_2A12_V7_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRMM_2A12_7",
            provider="GES_DISC", 
            shortname="TRMM_2A12",
            version="7",
            description="TRMM Microwave Imager Hydrometeor Profile L2 1.5 hours V7 (TRMM_2A12) at GES DISC version: 7"
        )

    TRMM_3A11_V7_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRMM_3A11_7",
            provider="GES_DISC", 
            shortname="TRMM_3A11",
            version="7",
            description="TRMM Microwave Imager Oceanic Rainfall L3 1 month 5 degree x 5 degree V7 (TRMM_3A11) at GES DISC version: 7"
        )

    TRMM_3A12_V7_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRMM_3A12_7",
            provider="GES_DISC", 
            shortname="TRMM_3A12",
            version="7",
            description="TRMM Microwave Imager Precipitation Profile L3 1 month 0.5 degree x 0.5 degree V7 (TRMM_3A12) at GES DISC version: 7"
        )

    TRMM_3G25_V7_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRMM_3G25_7",
            provider="GES_DISC", 
            shortname="TRMM_3G25",
            version="7",
            description="TRMM PR Gridded Orbital Spectral Latent Heating Profiles L3 1.5 hours 0.5 degree x 0.5 degree V7 (TRMM_3G25) at GES DISC version: 7"
        )

    TRMM_1B21_V7_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRMM_1B21_7",
            provider="GES_DISC", 
            shortname="TRMM_1B21",
            version="7",
            description="TRMM Precipitation Radar Power and Reflectivity L1B 1.5 hours V7 (TRMM_1B21) at GES DISC version: 7"
        )

    TRMM_1C21_V7_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRMM_1C21_7",
            provider="GES_DISC", 
            shortname="TRMM_1C21",
            version="7",
            description="TRMM Precipitation Radar Power and Reflectivity L1C 1.5 hours V7 (TRMM_1C21) at GES DISC version: 7"
        )

    TRMM_2A23_V7_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRMM_2A23_7",
            provider="GES_DISC", 
            shortname="TRMM_2A23",
            version="7",
            description="TRMM Precipitation Radar Rain Characteristics L2 1.5 hours V7 (TRMM_2A23) at GES DISC version: 7"
        )

    TRMM_2A25_V7_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRMM_2A25_7",
            provider="GES_DISC", 
            shortname="TRMM_2A25",
            version="7",
            description="TRMM Precipitation Radar Rainfall Rate and Profile L2 1.5 hours V7 (TRMM_2A25) at GES DISC version: 7"
        )

    TRMM_3H25_V7_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRMM_3H25_7",
            provider="GES_DISC", 
            shortname="TRMM_3H25",
            version="7",
            description="TRMM Precipitation Radar Spectral Latent Heating L3 1 month 0.5 degree x 0.5 degree V7 (TRMM_3H25) at GES DISC version: 7"
        )

    TRMM_2A21_V7_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRMM_2A21_7",
            provider="GES_DISC", 
            shortname="TRMM_2A21",
            version="7",
            description="TRMM Precipitation Radar Surface Cross-Section L2 1.5 hours V7 (TRMM_2A21) at GES DISC version: 7"
        )

    TRMM_3A26_V7_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRMM_3A26_7",
            provider="GES_DISC", 
            shortname="TRMM_3A26",
            version="7",
            description="TRMM Radar Rain Distributions L3 1 month 5 degree x 5 degree V7 (TRMM_3A26) at GES DISC version: 7"
        )

    TRMM_3A25_V7_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRMM_3A25_7",
            provider="GES_DISC", 
            shortname="TRMM_3A25",
            version="7",
            description="TRMM Radar Rainfall Statistics L3 1 month (5 x 5) and (0.5 x 0.5) degree V7 (TRMM_3A25) at GES DISC version: 7"
        )

    TRMM_3H31_V7_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRMM_3H31_7",
            provider="GES_DISC", 
            shortname="TRMM_3H31",
            version="7",
            description="TRMM TMI/PR Combined Convective Stratiform Heating L3 1 month 0.5 degree x 0.5 degree V7 (TRMM_3H31) at GES DISC version: 7"
        )

    TRMM_3G31_V7_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRMM_3G31_7",
            provider="GES_DISC", 
            shortname="TRMM_3G31",
            version="7",
            description="TRMM TMI/PR Combined Gridded Orbital Spectral Latent Heating L3 1.5 hours 0.5 degree x 0.5 degree V7 (TRMM_3G31) at GES DISC version: 7"
        )

    TRMM_3B31_V7_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRMM_3B31_7",
            provider="GES_DISC", 
            shortname="TRMM_3B31",
            version="7",
            description="TRMM TMI/PR Combined Precipitation L3 1 month 0.5 degree x 0.5 degree V7 (TRMM_3B31) at GES DISC version: 7"
        )

    TRMM_1B01_V7_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRMM_1B01_7",
            provider="GES_DISC", 
            shortname="TRMM_1B01",
            version="7",
            description="TRMM Visible and Infrared Scanner Calibrated Radiances L1B 1.5 hours V7 (TRMM_1B01) at GES DISC version: 7"
        )

    TRPSDL2NH3AIRSFS_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSDL2NH3AIRSFS_1",
            provider="GES_DISC", 
            shortname="TRPSDL2NH3AIRSFS",
            version="1",
            description="TROPESS AIRS-Aqua L2 Ammonia for Forward Stream, Standard Product V1 (TRPSDL2NH3AIRSFS) at GES DISC version: 1"
        )

    TRPSYL2NH3AIRSFS_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSYL2NH3AIRSFS_1",
            provider="GES_DISC", 
            shortname="TRPSYL2NH3AIRSFS",
            version="1",
            description="TROPESS AIRS-Aqua L2 Ammonia for Forward Stream, Summary Product V1 (TRPSYL2NH3AIRSFS) at GES DISC version: 1"
        )

    TRPSDL2TATMAIRSFS_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSDL2TATMAIRSFS_1",
            provider="GES_DISC", 
            shortname="TRPSDL2TATMAIRSFS",
            version="1",
            description="TROPESS AIRS-Aqua L2 Atmospheric Temperature for Forward Stream, Standard Product V1 (TRPSDL2TATMAIRSFS) at GES DISC version: 1"
        )

    TRPSDL2COAIRSFS_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSDL2COAIRSFS_1",
            provider="GES_DISC", 
            shortname="TRPSDL2COAIRSFS",
            version="1",
            description="TROPESS AIRS-Aqua L2 Carbon Monoxide for Forward Stream, Standard Product V1 (TRPSDL2COAIRSFS) at GES DISC version: 1"
        )

    TRPSYL2COAIRSFS_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSYL2COAIRSFS_1",
            provider="GES_DISC", 
            shortname="TRPSYL2COAIRSFS",
            version="1",
            description="TROPESS AIRS-Aqua L2 Carbon Monoxide for Forward Stream, Summary Product V1 (TRPSYL2COAIRSFS) at GES DISC version: 1"
        )

    TRPSYL2COAIRSORS_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSYL2COAIRSORS_1",
            provider="GES_DISC", 
            shortname="TRPSYL2COAIRSORS",
            version="1",
            description="TROPESS AIRS-Aqua L2 Carbon Monoxide for Reanalysis Stream, Summary Product V1 (TRPSYL2COAIRSORS) at GES DISC version: 1"
        )

    TRPSDL2HDOAIRSFS_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSDL2HDOAIRSFS_1",
            provider="GES_DISC", 
            shortname="TRPSDL2HDOAIRSFS",
            version="1",
            description="TROPESS AIRS-Aqua L2 Deuterated Water Vapor for Forward Stream, Standard Product V1 (TRPSDL2HDOAIRSFS) at GES DISC version: 1"
        )

    TRPSYL2HDOAIRSFS_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSYL2HDOAIRSFS_1",
            provider="GES_DISC", 
            shortname="TRPSYL2HDOAIRSFS",
            version="1",
            description="TROPESS AIRS-Aqua L2 Deuterated Water Vapor for Forward Stream, Summary Product V1 (TRPSYL2HDOAIRSFS) at GES DISC version: 1"
        )

    TRPSYL2HDOAIRSORS_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSYL2HDOAIRSORS_1",
            provider="GES_DISC", 
            shortname="TRPSYL2HDOAIRSORS",
            version="1",
            description="TROPESS AIRS-Aqua L2 Deuterated Water Vapor for Reanalysis Stream, Summary Product V1 (TRPSYL2HDOAIRSORS) at GES DISC version: 1"
        )

    TRPSDL2CH4AIRSFS_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSDL2CH4AIRSFS_1",
            provider="GES_DISC", 
            shortname="TRPSDL2CH4AIRSFS",
            version="1",
            description="TROPESS AIRS-Aqua L2 Methane for Forward Stream, Standard Product V1 (TRPSDL2CH4AIRSFS) at GES DISC version: 1"
        )

    TRPSYL2CH4AIRSFS_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSYL2CH4AIRSFS_1",
            provider="GES_DISC", 
            shortname="TRPSYL2CH4AIRSFS",
            version="1",
            description="TROPESS AIRS-Aqua L2 Methane for Forward Stream, Summary Product V1 (TRPSYL2CH4AIRSFS) at GES DISC version: 1"
        )

    TRPSYL2CH4AIRSORS_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSYL2CH4AIRSORS_1",
            provider="GES_DISC", 
            shortname="TRPSYL2CH4AIRSORS",
            version="1",
            description="TROPESS AIRS-Aqua L2 Methane for Reanalysis Stream, Summary Product V1 (TRPSYL2CH4AIRSORS) at GES DISC version: 1"
        )

    TRPSDL2O3AIRSFS_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSDL2O3AIRSFS_1",
            provider="GES_DISC", 
            shortname="TRPSDL2O3AIRSFS",
            version="1",
            description="TROPESS AIRS-Aqua L2 Ozone for Forward Stream, Standard Product V1 (TRPSDL2O3AIRSFS) at GES DISC version: 1"
        )

    TRPSYL2O3AIRSFS_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSYL2O3AIRSFS_1",
            provider="GES_DISC", 
            shortname="TRPSYL2O3AIRSFS",
            version="1",
            description="TROPESS AIRS-Aqua L2 Ozone for Forward Stream, Summary Product V1 (TRPSYL2O3AIRSFS) at GES DISC version: 1"
        )

    TRPSYL2O3AIRSORS_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSYL2O3AIRSORS_1",
            provider="GES_DISC", 
            shortname="TRPSYL2O3AIRSORS",
            version="1",
            description="TROPESS AIRS-Aqua L2 Ozone for Reanalysis Stream, Summary Product V1 (TRPSYL2O3AIRSORS) at GES DISC version: 1"
        )

    TRPSDL2H2OAIRSFS_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSDL2H2OAIRSFS_1",
            provider="GES_DISC", 
            shortname="TRPSDL2H2OAIRSFS",
            version="1",
            description="TROPESS AIRS-Aqua L2 Water for Forward Stream, Standard Product V1 (TRPSDL2H2OAIRSFS) at GES DISC version: 1"
        )

    TRPSDL2O3AIRSOMIFS_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSDL2O3AIRSOMIFS_1",
            provider="GES_DISC", 
            shortname="TRPSDL2O3AIRSOMIFS",
            version="1",
            description="TROPESS AIRS-Aqua and OMI-Aura L2 Ozone for Forward Stream, Standard Product V1 (TRPSDL2O3AIRSOMIFS) at GES DISC version: 1"
        )

    TRPSYL2O3AIRSOMIFS_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSYL2O3AIRSOMIFS_1",
            provider="GES_DISC", 
            shortname="TRPSYL2O3AIRSOMIFS",
            version="1",
            description="TROPESS AIRS-Aqua and OMI-Aura L2 Ozone for Forward Stream, Summary Product V1 (TRPSYL2O3AIRSOMIFS) at GES DISC version: 1"
        )

    TRPSCRAERNH46H3D_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSCRAERNH46H3D_1",
            provider="GES_DISC", 
            shortname="TRPSCRAERNH46H3D",
            version="1",
            description="TROPESS Chemical Reanalysis Aerosol NH4 6-Hourly 3-dimensional Product V1 (TRPSCRAERNH46H3D) at GES DISC version: 1"
        )

    TRPSCRAERNH4M3D_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSCRAERNH4M3D_1",
            provider="GES_DISC", 
            shortname="TRPSCRAERNH4M3D",
            version="1",
            description="TROPESS Chemical Reanalysis Aerosol NH4 Monthly 3-dimensional Product V1 (TRPSCRAERNH4M3D) at GES DISC version: 1"
        )

    TRPSCRAERNO36H3D_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSCRAERNO36H3D_1",
            provider="GES_DISC", 
            shortname="TRPSCRAERNO36H3D",
            version="1",
            description="TROPESS Chemical Reanalysis Aerosol NO3 6-Hourly 3-dimensional Product V1 (TRPSCRAERNO36H3D) at GES DISC version: 1"
        )

    TRPSCRAERNO3M3D_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSCRAERNO3M3D_1",
            provider="GES_DISC", 
            shortname="TRPSCRAERNO3M3D",
            version="1",
            description="TROPESS Chemical Reanalysis Aerosol NO3 Monthly 3-dimensional Product V1 (TRPSCRAERNO3M3D) at GES DISC version: 1"
        )

    TRPSCRAERSO46H3D_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSCRAERSO46H3D_1",
            provider="GES_DISC", 
            shortname="TRPSCRAERSO46H3D",
            version="1",
            description="TROPESS Chemical Reanalysis Aerosol SO4 6-Hourly 3-dimensional Product V1 (TRPSCRAERSO46H3D) at GES DISC version: 1"
        )

    TRPSCRAERSO4M3D_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSCRAERSO4M3D_1",
            provider="GES_DISC", 
            shortname="TRPSCRAERSO4M3D",
            version="1",
            description="TROPESS Chemical Reanalysis Aerosol SO4 Monthly 3-dimensional Product V1 (TRPSCRAERSO4M3D) at GES DISC version: 1"
        )

    TRPSCRCH2O6H3D_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSCRCH2O6H3D_1",
            provider="GES_DISC", 
            shortname="TRPSCRCH2O6H3D",
            version="1",
            description="TROPESS Chemical Reanalysis CH2O 6-Hourly 3-dimensional Product V1 (TRPSCRCH2O6H3D) at GES DISC version: 1"
        )

    TRPSCRCH2OM3D_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSCRCH2OM3D_1",
            provider="GES_DISC", 
            shortname="TRPSCRCH2OM3D",
            version="1",
            description="TROPESS Chemical Reanalysis CH2O Monthly 3-dimensional Product V1 (TRPSCRCH2OM3D) at GES DISC version: 1"
        )

    TRPSCRCO6H3D_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSCRCO6H3D_1",
            provider="GES_DISC", 
            shortname="TRPSCRCO6H3D",
            version="1",
            description="TROPESS Chemical Reanalysis CO 6-Hourly 3-dimensional Product V1 (TRPSCRCO6H3D) at GES DISC version: 1"
        )

    TRPSCRCOM3D_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSCRCOM3D_1",
            provider="GES_DISC", 
            shortname="TRPSCRCOM3D",
            version="1",
            description="TROPESS Chemical Reanalysis CO Monthly 3-dimensional Product V1 (TRPSCRCOM3D) at GES DISC version: 1"
        )

    TRPSCRCOS6H3D_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSCRCOS6H3D_1",
            provider="GES_DISC", 
            shortname="TRPSCRCOS6H3D",
            version="1",
            description="TROPESS Chemical Reanalysis CO Spread 6-Hourly 3-dimensional Product V1 (TRPSCRCOS6H3D) at GES DISC version: 1"
        )

    TRPSCRCOSM3D_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSCRCOSM3D_1",
            provider="GES_DISC", 
            shortname="TRPSCRCOSM3D",
            version="1",
            description="TROPESS Chemical Reanalysis CO Spread Monthly 3-dimensional Product V1 (TRPSCRCOSM3D) at GES DISC version: 1"
        )

    TRPSCRHNO36H3D_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSCRHNO36H3D_1",
            provider="GES_DISC", 
            shortname="TRPSCRHNO36H3D",
            version="1",
            description="TROPESS Chemical Reanalysis HNO3 6-Hourly 3-dimensional Product V1 (TRPSCRHNO36H3D) at GES DISC version: 1"
        )

    TRPSCRHNO3M3D_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSCRHNO3M3D_1",
            provider="GES_DISC", 
            shortname="TRPSCRHNO3M3D",
            version="1",
            description="TROPESS Chemical Reanalysis HNO3 Monthly 3-dimensional Product V1 (TRPSCRHNO3M3D) at GES DISC version: 1"
        )

    TRPSCRENOXLM2D_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSCRENOXLM2D_1",
            provider="GES_DISC", 
            shortname="TRPSCRENOXLM2D",
            version="1",
            description="TROPESS Chemical Reanalysis Lightning NOx emissions Monthly 2-dimensional Product V1 (TRPSCRENOXLM2D) at GES DISC version: 1"
        )

    TRPSCRV6H3D_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSCRV6H3D_1",
            provider="GES_DISC", 
            shortname="TRPSCRV6H3D",
            version="1",
            description="TROPESS Chemical Reanalysis Meridional Wind 6-Hourly 3-dimensional Product V1 (TRPSCRV6H3D) at GES DISC version: 1"
        )

    TRPSCRVM3D_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSCRVM3D_1",
            provider="GES_DISC", 
            shortname="TRPSCRVM3D",
            version="1",
            description="TROPESS Chemical Reanalysis Meridional Wind Monthly 3-dimensional Product V1 (TRPSCRVM3D) at GES DISC version: 1"
        )

    TRPSCRNO6H3D_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSCRNO6H3D_1",
            provider="GES_DISC", 
            shortname="TRPSCRNO6H3D",
            version="1",
            description="TROPESS Chemical Reanalysis NO 6-Hourly 3-dimensional Product V1 (TRPSCRNO6H3D) at GES DISC version: 1"
        )

    TRPSCRNOM3D_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSCRNOM3D_1",
            provider="GES_DISC", 
            shortname="TRPSCRNOM3D",
            version="1",
            description="TROPESS Chemical Reanalysis NO Monthly 3-dimensional Product V1 (TRPSCRNOM3D) at GES DISC version: 1"
        )

    TRPSCRNO26H3D_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSCRNO26H3D_1",
            provider="GES_DISC", 
            shortname="TRPSCRNO26H3D",
            version="1",
            description="TROPESS Chemical Reanalysis NO2 6-Hourly 3-dimensional Product V1 (TRPSCRNO26H3D) at GES DISC version: 1"
        )

    TRPSCRNO2M3D_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSCRNO2M3D_1",
            provider="GES_DISC", 
            shortname="TRPSCRNO2M3D",
            version="1",
            description="TROPESS Chemical Reanalysis NO2 Monthly 3-dimensional Product V1 (TRPSCRNO2M3D) at GES DISC version: 1"
        )

    TRPSCRNO2S6H3D_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSCRNO2S6H3D_1",
            provider="GES_DISC", 
            shortname="TRPSCRNO2S6H3D",
            version="1",
            description="TROPESS Chemical Reanalysis NO2 Spread 6-Hourly 3-dimensional Product V1 (TRPSCRNO2S6H3D) at GES DISC version: 1"
        )

    TRPSCRNO2SM3D_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSCRNO2SM3D_1",
            provider="GES_DISC", 
            shortname="TRPSCRNO2SM3D",
            version="1",
            description="TROPESS Chemical Reanalysis NO2 Spread Monthly 3-dimensional Product V1 (TRPSCRNO2SM3D) at GES DISC version: 1"
        )

    TRPSCRO36H3D_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSCRO36H3D_1",
            provider="GES_DISC", 
            shortname="TRPSCRO36H3D",
            version="1",
            description="TROPESS Chemical Reanalysis O3 6-Hourly 3-dimensional Product V1 (TRPSCRO36H3D) at GES DISC version: 1"
        )

    TRPSCRO3I6H3D_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSCRO3I6H3D_1",
            provider="GES_DISC", 
            shortname="TRPSCRO3I6H3D",
            version="1",
            description="TROPESS Chemical Reanalysis O3 Increment 6-Hourly 3-dimensional Product V1 (TRPSCRO3I6H3D) at GES DISC version: 1"
        )

    TRPSCRO3IM3D_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSCRO3IM3D_1",
            provider="GES_DISC", 
            shortname="TRPSCRO3IM3D",
            version="1",
            description="TROPESS Chemical Reanalysis O3 Increment Monthly 3-dimensional Product V1 (TRPSCRO3IM3D) at GES DISC version: 1"
        )

    TRPSCRO3M3D_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSCRO3M3D_1",
            provider="GES_DISC", 
            shortname="TRPSCRO3M3D",
            version="1",
            description="TROPESS Chemical Reanalysis O3 Monthly 3-dimensional Product V1 (TRPSCRO3M3D) at GES DISC version: 1"
        )

    TRPSCRO3S6H3D_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSCRO3S6H3D_1",
            provider="GES_DISC", 
            shortname="TRPSCRO3S6H3D",
            version="1",
            description="TROPESS Chemical Reanalysis O3 Spread 6-Hourly 3-dimensional Product V1 (TRPSCRO3S6H3D) at GES DISC version: 1"
        )

    TRPSCRO3SM3D_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSCRO3SM3D_1",
            provider="GES_DISC", 
            shortname="TRPSCRO3SM3D",
            version="1",
            description="TROPESS Chemical Reanalysis O3 Spread Monthly 3-dimensional Product V1 (TRPSCRO3SM3D) at GES DISC version: 1"
        )

    TRPSCROH6H3D_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSCROH6H3D_1",
            provider="GES_DISC", 
            shortname="TRPSCROH6H3D",
            version="1",
            description="TROPESS Chemical Reanalysis OH 6-Hourly 3-dimensional Product V1 (TRPSCROH6H3D) at GES DISC version: 1"
        )

    TRPSCROHM3D_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSCROHM3D_1",
            provider="GES_DISC", 
            shortname="TRPSCROHM3D",
            version="1",
            description="TROPESS Chemical Reanalysis OH Monthly 3-dimensional Product V1 (TRPSCROHM3D) at GES DISC version: 1"
        )

    TRPSCRPAN6H3D_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSCRPAN6H3D_1",
            provider="GES_DISC", 
            shortname="TRPSCRPAN6H3D",
            version="1",
            description="TROPESS Chemical Reanalysis PAN 6-Hourly 3-dimensional Product V1 (TRPSCRPAN6H3D) at GES DISC version: 1"
        )

    TRPSCRPANM3D_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSCRPANM3D_1",
            provider="GES_DISC", 
            shortname="TRPSCRPANM3D",
            version="1",
            description="TROPESS Chemical Reanalysis PAN Monthly 3-dimensional Product V1 (TRPSCRPANM3D) at GES DISC version: 1"
        )

    TRPSCRSO26H3D_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSCRSO26H3D_1",
            provider="GES_DISC", 
            shortname="TRPSCRSO26H3D",
            version="1",
            description="TROPESS Chemical Reanalysis SO2 6-Hourly 3-dimensional Product V1 (TRPSCRSO26H3D) at GES DISC version: 1"
        )

    TRPSCRSO2M3D_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSCRSO2M3D_1",
            provider="GES_DISC", 
            shortname="TRPSCRSO2M3D",
            version="1",
            description="TROPESS Chemical Reanalysis SO2 Monthly 3-dimensional Product V1 (TRPSCRSO2M3D) at GES DISC version: 1"
        )

    TRPSCRQ6H3D_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSCRQ6H3D_1",
            provider="GES_DISC", 
            shortname="TRPSCRQ6H3D",
            version="1",
            description="TROPESS Chemical Reanalysis Specific Humidity 6-Hourly 3-dimensional Product V1 (TRPSCRQ6H3D) at GES DISC version: 1"
        )

    TRPSCRQM3D_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSCRQM3D_1",
            provider="GES_DISC", 
            shortname="TRPSCRQM3D",
            version="1",
            description="TROPESS Chemical Reanalysis Specific Humidity Monthly 3-dimensional Product V1 (TRPSCRQM3D) at GES DISC version: 1"
        )

    TRPSCRAERNH42H2D_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSCRAERNH42H2D_1",
            provider="GES_DISC", 
            shortname="TRPSCRAERNH42H2D",
            version="1",
            description="TROPESS Chemical Reanalysis Surface Aerosol NH4 2-Hourly 2-dimensional Product V1 (TRPSCRAERNH42H2D) at GES DISC version: 1"
        )

    TRPSCRAERNO32H2D_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSCRAERNO32H2D_1",
            provider="GES_DISC", 
            shortname="TRPSCRAERNO32H2D",
            version="1",
            description="TROPESS Chemical Reanalysis Surface Aerosol NO3 2-Hourly 2-dimensional Product V1 (TRPSCRAERNO32H2D) at GES DISC version: 1"
        )

    TRPSCRAERSO42H2D_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSCRAERSO42H2D_1",
            provider="GES_DISC", 
            shortname="TRPSCRAERSO42H2D",
            version="1",
            description="TROPESS Chemical Reanalysis Surface Aerosol SO4 2-Hourly 2-dimensional Product V1 (TRPSCRAERSO42H2D) at GES DISC version: 1"
        )

    TRPSCRECOAM2D_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSCRECOAM2D_1",
            provider="GES_DISC", 
            shortname="TRPSCRECOAM2D",
            version="1",
            description="TROPESS Chemical Reanalysis Surface Anthropogenic CO emissions Monthly 2-dimensional Product V1 (TRPSCRECOAM2D) at GES DISC version: 1"
        )

    TRPSCRENOXAM2D_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSCRENOXAM2D_1",
            provider="GES_DISC", 
            shortname="TRPSCRENOXAM2D",
            version="1",
            description="TROPESS Chemical Reanalysis Surface Anthropogenic NOx emissions Monthly 2-dimensional Product V1 (TRPSCRENOXAM2D) at GES DISC version: 1"
        )

    TRPSCRECOBM2D_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSCRECOBM2D_1",
            provider="GES_DISC", 
            shortname="TRPSCRECOBM2D",
            version="1",
            description="TROPESS Chemical Reanalysis Surface Biomass Burning CO emissions Monthly 2-dimensional Product V1 (TRPSCRECOBM2D) at GES DISC version: 1"
        )

    TRPSCRENOXBM2D_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSCRENOXBM2D_1",
            provider="GES_DISC", 
            shortname="TRPSCRENOXBM2D",
            version="1",
            description="TROPESS Chemical Reanalysis Surface Biomass Burning NOx emissions Monthly 2-dimensional Product V1 (TRPSCRENOXBM2D) at GES DISC version: 1"
        )

    TRPSCRCH2O2H2D_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSCRCH2O2H2D_1",
            provider="GES_DISC", 
            shortname="TRPSCRCH2O2H2D",
            version="1",
            description="TROPESS Chemical Reanalysis Surface CH2O 2-Hourly 2-dimensional Product V1 (TRPSCRCH2O2H2D) at GES DISC version: 1"
        )

    TRPSCRCO2H2D_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSCRCO2H2D_1",
            provider="GES_DISC", 
            shortname="TRPSCRCO2H2D",
            version="1",
            description="TROPESS Chemical Reanalysis Surface CO 2-Hourly 2-dimensional Product V1 (TRPSCRCO2H2D) at GES DISC version: 1"
        )

    TRPSCRHNO32H2D_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSCRHNO32H2D_1",
            provider="GES_DISC", 
            shortname="TRPSCRHNO32H2D",
            version="1",
            description="TROPESS Chemical Reanalysis Surface HNO3 2-Hourly 2-dimensional Product V1 (TRPSCRHNO32H2D) at GES DISC version: 1"
        )

    TRPSCRV2H2D_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSCRV2H2D_1",
            provider="GES_DISC", 
            shortname="TRPSCRV2H2D",
            version="1",
            description="TROPESS Chemical Reanalysis Surface Meridional Wind 2-Hourly 2-dimensional Product V1 (TRPSCRV2H2D) at GES DISC version: 1"
        )

    TRPSCRNO2H2D_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSCRNO2H2D_1",
            provider="GES_DISC", 
            shortname="TRPSCRNO2H2D",
            version="1",
            description="TROPESS Chemical Reanalysis Surface NO 2-Hourly 2-dimensional Product V1 (TRPSCRNO2H2D) at GES DISC version: 1"
        )

    TRPSCRNO22H2D_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSCRNO22H2D_1",
            provider="GES_DISC", 
            shortname="TRPSCRNO22H2D",
            version="1",
            description="TROPESS Chemical Reanalysis Surface NO2 2-Hourly 2-dimensional Product V1 (TRPSCRNO22H2D) at GES DISC version: 1"
        )

    TRPSCRO32H2D_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSCRO32H2D_1",
            provider="GES_DISC", 
            shortname="TRPSCRO32H2D",
            version="1",
            description="TROPESS Chemical Reanalysis Surface O3 2-Hourly 2-dimensional Product V1 (TRPSCRO32H2D) at GES DISC version: 1"
        )

    TRPSCROH2H2D_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSCROH2H2D_1",
            provider="GES_DISC", 
            shortname="TRPSCROH2H2D",
            version="1",
            description="TROPESS Chemical Reanalysis Surface OH 2-Hourly 2-dimensional Product V1 (TRPSCROH2H2D) at GES DISC version: 1"
        )

    TRPSCRPAN2H2D_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSCRPAN2H2D_1",
            provider="GES_DISC", 
            shortname="TRPSCRPAN2H2D",
            version="1",
            description="TROPESS Chemical Reanalysis Surface PAN 2-Hourly 2-dimensional Product V1 (TRPSCRPAN2H2D) at GES DISC version: 1"
        )

    TRPSCRPS2H2D_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSCRPS2H2D_1",
            provider="GES_DISC", 
            shortname="TRPSCRPS2H2D",
            version="1",
            description="TROPESS Chemical Reanalysis Surface Pressure 2-Hourly 2-dimensional Product V1 (TRPSCRPS2H2D) at GES DISC version: 1"
        )

    TRPSCRPS6H2D_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSCRPS6H2D_1",
            provider="GES_DISC", 
            shortname="TRPSCRPS6H2D",
            version="1",
            description="TROPESS Chemical Reanalysis Surface Pressure 6-Hourly 2-dimensional Product V1 (TRPSCRPS6H2D) at GES DISC version: 1"
        )

    TRPSCRPSM2D_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSCRPSM2D_1",
            provider="GES_DISC", 
            shortname="TRPSCRPSM2D",
            version="1",
            description="TROPESS Chemical Reanalysis Surface Pressure Monthly 2-dimensional Product V1 (TRPSCRPSM2D) at GES DISC version: 1"
        )

    TRPSCRSO22H2D_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSCRSO22H2D_1",
            provider="GES_DISC", 
            shortname="TRPSCRSO22H2D",
            version="1",
            description="TROPESS Chemical Reanalysis Surface SO2 2-Hourly 2-dimensional Product V1 (TRPSCRSO22H2D) at GES DISC version: 1"
        )

    TRPSCRENOXSM2D_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSCRENOXSM2D_1",
            provider="GES_DISC", 
            shortname="TRPSCRENOXSM2D",
            version="1",
            description="TROPESS Chemical Reanalysis Surface Soil NOx emissions Monthly 2-dimensional Product V1 (TRPSCRENOXSM2D) at GES DISC version: 1"
        )

    TRPSCRQ2H2D_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSCRQ2H2D_1",
            provider="GES_DISC", 
            shortname="TRPSCRQ2H2D",
            version="1",
            description="TROPESS Chemical Reanalysis Surface Specific Humidity 2-Hourly 2-dimensional Product V1 (TRPSCRQ2H2D) at GES DISC version: 1"
        )

    TRPSCRT2H2D_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSCRT2H2D_1",
            provider="GES_DISC", 
            shortname="TRPSCRT2H2D",
            version="1",
            description="TROPESS Chemical Reanalysis Surface Temperature 2-Hourly 2-dimensional Product V1 (TRPSCRT2H2D) at GES DISC version: 1"
        )

    TRPSCRECOTM2D_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSCRECOTM2D_1",
            provider="GES_DISC", 
            shortname="TRPSCRECOTM2D",
            version="1",
            description="TROPESS Chemical Reanalysis Surface Total CO emissions Monthly 2-dimensional Product V1 (TRPSCRECOTM2D) at GES DISC version: 1"
        )

    TRPSCRENOXTM2D_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSCRENOXTM2D_1",
            provider="GES_DISC", 
            shortname="TRPSCRENOXTM2D",
            version="1",
            description="TROPESS Chemical Reanalysis Surface Total NOx emissions Monthly 2-dimensional Product V1 (TRPSCRENOXTM2D) at GES DISC version: 1"
        )

    TRPSCRESO2TM2D_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSCRESO2TM2D_1",
            provider="GES_DISC", 
            shortname="TRPSCRESO2TM2D",
            version="1",
            description="TROPESS Chemical Reanalysis Surface Total SO2 emissions Monthly 2-dimensional Product V1 (TRPSCRESO2TM2D) at GES DISC version: 1"
        )

    TRPSCRU2H2D_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSCRU2H2D_1",
            provider="GES_DISC", 
            shortname="TRPSCRU2H2D",
            version="1",
            description="TROPESS Chemical Reanalysis Surface Zonal Wind 2-Hourly 2-dimensional Product V1 (TRPSCRU2H2D) at GES DISC version: 1"
        )

    TRPSCRT6H3D_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSCRT6H3D_1",
            provider="GES_DISC", 
            shortname="TRPSCRT6H3D",
            version="1",
            description="TROPESS Chemical Reanalysis Temperature 6-Hourly 3-dimensional Product V1 (TRPSCRT6H3D) at GES DISC version: 1"
        )

    TRPSCRTM3D_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSCRTM3D_1",
            provider="GES_DISC", 
            shortname="TRPSCRTM3D",
            version="1",
            description="TROPESS Chemical Reanalysis Temperature Monthly 3-dimensional Product V1 (TRPSCRTM3D) at GES DISC version: 1"
        )

    TRPSCRU6H3D_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSCRU6H3D_1",
            provider="GES_DISC", 
            shortname="TRPSCRU6H3D",
            version="1",
            description="TROPESS Chemical Reanalysis Zonal Wind 6-Hourly 3-dimensional Product V1 (TRPSCRU6H3D) at GES DISC version: 1"
        )

    TRPSCRUM3D_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSCRUM3D_1",
            provider="GES_DISC", 
            shortname="TRPSCRUM3D",
            version="1",
            description="TROPESS Chemical Reanalysis Zonal Wind Monthly 3-dimensional Product V1 (TRPSCRUM3D) at GES DISC version: 1"
        )

    TRPSDL2NH3CRS1FS_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSDL2NH3CRS1FS_1",
            provider="GES_DISC", 
            shortname="TRPSDL2NH3CRS1FS",
            version="1",
            description="TROPESS CrIS-JPSS1 L2 Ammonia for Forward Stream, Standard Product V1 (TRPSDL2NH3CRS1FS) at GES DISC version: 1"
        )

    TRPSYL2NH3CRS1FS_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSYL2NH3CRS1FS_1",
            provider="GES_DISC", 
            shortname="TRPSYL2NH3CRS1FS",
            version="1",
            description="TROPESS CrIS-JPSS1 L2 Ammonia for Forward Stream, Summary Product V1 (TRPSYL2NH3CRS1FS) at GES DISC version: 1"
        )

    TRPSDL2TATMCRS1FS_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSDL2TATMCRS1FS_1",
            provider="GES_DISC", 
            shortname="TRPSDL2TATMCRS1FS",
            version="1",
            description="TROPESS CrIS-JPSS1 L2 Atmospheric Temperature for Forward Stream, Standard Product V1 (TRPSDL2TATMCRS1FS) at GES DISC version: 1"
        )

    TRPSDL2COCRS1FS_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSDL2COCRS1FS_1",
            provider="GES_DISC", 
            shortname="TRPSDL2COCRS1FS",
            version="1",
            description="TROPESS CrIS-JPSS1 L2 Carbon Monoxide for Forward Stream, Standard Product V1 (TRPSDL2COCRS1FS) at GES DISC version: 1"
        )

    TRPSYL2COCRS1FS_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSYL2COCRS1FS_1",
            provider="GES_DISC", 
            shortname="TRPSYL2COCRS1FS",
            version="1",
            description="TROPESS CrIS-JPSS1 L2 Carbon Monoxide for Forward Stream, Summary Product V1 (TRPSYL2COCRS1FS) at GES DISC version: 1"
        )

    TRPSDL2HDOCRS1FS_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSDL2HDOCRS1FS_1",
            provider="GES_DISC", 
            shortname="TRPSDL2HDOCRS1FS",
            version="1",
            description="TROPESS CrIS-JPSS1 L2 Deuterated Water Vapor for Forward Stream, Standard Product V1 (TRPSDL2HDOCRS1FS) at GES DISC version: 1"
        )

    TRPSYL2HDOCRS1FS_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSYL2HDOCRS1FS_1",
            provider="GES_DISC", 
            shortname="TRPSYL2HDOCRS1FS",
            version="1",
            description="TROPESS CrIS-JPSS1 L2 Deuterated Water Vapor for Forward Stream, Summary Product V1 (TRPSYL2HDOCRS1FS) at GES DISC version: 1"
        )

    TRPSDL2CH4CRS1FS_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSDL2CH4CRS1FS_1",
            provider="GES_DISC", 
            shortname="TRPSDL2CH4CRS1FS",
            version="1",
            description="TROPESS CrIS-JPSS1 L2 Methane for Forward Stream, Standard Product V1 (TRPSDL2CH4CRS1FS) at GES DISC version: 1"
        )

    TRPSYL2CH4CRS1FS_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSYL2CH4CRS1FS_1",
            provider="GES_DISC", 
            shortname="TRPSYL2CH4CRS1FS",
            version="1",
            description="TROPESS CrIS-JPSS1 L2 Methane for Forward Stream, Summary Product V1 (TRPSYL2CH4CRS1FS) at GES DISC version: 1"
        )

    TRPSDL2O3CRS1FS_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSDL2O3CRS1FS_1",
            provider="GES_DISC", 
            shortname="TRPSDL2O3CRS1FS",
            version="1",
            description="TROPESS CrIS-JPSS1 L2 Ozone for Forward Stream, Standard Product V1 (TRPSDL2O3CRS1FS) at GES DISC version: 1"
        )

    TRPSYL2O3CRS1FS_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSYL2O3CRS1FS_1",
            provider="GES_DISC", 
            shortname="TRPSYL2O3CRS1FS",
            version="1",
            description="TROPESS CrIS-JPSS1 L2 Ozone for Forward Stream, Summary Product V1 (TRPSYL2O3CRS1FS) at GES DISC version: 1"
        )

    TRPSDL2PANCRS1FS_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSDL2PANCRS1FS_1",
            provider="GES_DISC", 
            shortname="TRPSDL2PANCRS1FS",
            version="1",
            description="TROPESS CrIS-JPSS1 L2 Peroxyacetyl Nitrate for Forward Stream, Standard Product V1 (TRPSDL2PANCRS1FS) at GES DISC version: 1"
        )

    TRPSYL2PANCRS1FS_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSYL2PANCRS1FS_1",
            provider="GES_DISC", 
            shortname="TRPSYL2PANCRS1FS",
            version="1",
            description="TROPESS CrIS-JPSS1 L2 Peroxyacetyl Nitrate for Forward Stream, Summary Product V1 (TRPSYL2PANCRS1FS) at GES DISC version: 1"
        )

    TRPSDL2H2OCRS1FS_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSDL2H2OCRS1FS_1",
            provider="GES_DISC", 
            shortname="TRPSDL2H2OCRS1FS",
            version="1",
            description="TROPESS CrIS-JPSS1 L2 Water for Forward Stream, Standard Product V1 (TRPSDL2H2OCRS1FS) at GES DISC version: 1"
        )

    TRPSDL2NH3CRSAUS_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSDL2NH3CRSAUS_1",
            provider="GES_DISC", 
            shortname="TRPSDL2NH3CRSAUS",
            version="1",
            description="TROPESS CrIS-SNPP L2 Ammonia for Australian Fires, Standard Product V1 (TRPSDL2NH3CRSAUS) at GES DISC version: 1"
        )

    TRPSDL2NH3CRSFS_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSDL2NH3CRSFS_1",
            provider="GES_DISC", 
            shortname="TRPSDL2NH3CRSFS",
            version="1",
            description="TROPESS CrIS-SNPP L2 Ammonia for Forward Stream, Standard Product V1 (TRPSDL2NH3CRSFS) at GES DISC version: 1"
        )

    TRPSYL2NH3CRSFS_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSYL2NH3CRSFS_1",
            provider="GES_DISC", 
            shortname="TRPSYL2NH3CRSFS",
            version="1",
            description="TROPESS CrIS-SNPP L2 Ammonia for Forward Stream, Summary Product V1 (TRPSYL2NH3CRSFS) at GES DISC version: 1"
        )

    TRPSYL2NH3CRSRS_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSYL2NH3CRSRS_1",
            provider="GES_DISC", 
            shortname="TRPSYL2NH3CRSRS",
            version="1",
            description="TROPESS CrIS-SNPP L2 Ammonia for Reanalysis Stream, Summary Product V1 (TRPSYL2NH3CRSRS) at GES DISC version: 1"
        )

    TRPSDL2NH3CRSWCFHI_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSDL2NH3CRSWCFHI_1",
            provider="GES_DISC", 
            shortname="TRPSDL2NH3CRSWCFHI",
            version="1",
            description="TROPESS CrIS-SNPP L2 Ammonia for West Coast Fires HiRes, Standard Product V1 (TRPSDL2NH3CRSWCFHI) at GES DISC version: 1"
        )

    TRPSDL2NH3CRSWCF_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSDL2NH3CRSWCF_1",
            provider="GES_DISC", 
            shortname="TRPSDL2NH3CRSWCF",
            version="1",
            description="TROPESS CrIS-SNPP L2 Ammonia for West Coast Fires, Standard Product V1 (TRPSDL2NH3CRSWCF) at GES DISC version: 1"
        )

    TRPSDL2TATMCRSAUS_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSDL2TATMCRSAUS_1",
            provider="GES_DISC", 
            shortname="TRPSDL2TATMCRSAUS",
            version="1",
            description="TROPESS CrIS-SNPP L2 Atmospheric Temperature for Australian Fires, Standard Product V1 (TRPSDL2TATMCRSAUS) at GES DISC version: 1"
        )

    TRPSDL2TATMCRSFS_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSDL2TATMCRSFS_1",
            provider="GES_DISC", 
            shortname="TRPSDL2TATMCRSFS",
            version="1",
            description="TROPESS CrIS-SNPP L2 Atmospheric Temperature for Forward Stream, Standard Product V1 (TRPSDL2TATMCRSFS) at GES DISC version: 1"
        )

    TRPSDL2COCRSAUS_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSDL2COCRSAUS_1",
            provider="GES_DISC", 
            shortname="TRPSDL2COCRSAUS",
            version="1",
            description="TROPESS CrIS-SNPP L2 Carbon Monoxide for Australian Fires, Standard Product V1 (TRPSDL2COCRSAUS) at GES DISC version: 1"
        )

    TRPSDL2COCRSTS1_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSDL2COCRSTS1_1",
            provider="GES_DISC", 
            shortname="TRPSDL2COCRSTS1",
            version="1",
            description="TROPESS CrIS-SNPP L2 Carbon Monoxide for Buchholz2021 TS1, Standard Product V1 (TRPSDL2COCRSTS1) at GES DISC version: 1"
        )

    TRPSDL2COCRSTS2_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSDL2COCRSTS2_1",
            provider="GES_DISC", 
            shortname="TRPSDL2COCRSTS2",
            version="1",
            description="TROPESS CrIS-SNPP L2 Carbon Monoxide for Buchholz2021 TS2, Standard Product V1 (TRPSDL2COCRSTS2) at GES DISC version: 1"
        )

    TRPSDL2COCRSFS_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSDL2COCRSFS_1",
            provider="GES_DISC", 
            shortname="TRPSDL2COCRSFS",
            version="1",
            description="TROPESS CrIS-SNPP L2 Carbon Monoxide for Forward Stream, Standard Product V1 (TRPSDL2COCRSFS) at GES DISC version: 1"
        )

    TRPSYL2COCRSFS_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSYL2COCRSFS_1",
            provider="GES_DISC", 
            shortname="TRPSYL2COCRSFS",
            version="1",
            description="TROPESS CrIS-SNPP L2 Carbon Monoxide for Forward Stream, Summary Product V1 (TRPSYL2COCRSFS) at GES DISC version: 1"
        )

    TRPSYL2COCRSRS_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSYL2COCRSRS_1",
            provider="GES_DISC", 
            shortname="TRPSYL2COCRSRS",
            version="1",
            description="TROPESS CrIS-SNPP L2 Carbon Monoxide for Reanalysis Stream, Summary Product V1 (TRPSYL2COCRSRS) at GES DISC version: 1"
        )

    TRPSDL2COCRSWCFHI_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSDL2COCRSWCFHI_1",
            provider="GES_DISC", 
            shortname="TRPSDL2COCRSWCFHI",
            version="1",
            description="TROPESS CrIS-SNPP L2 Carbon Monoxide for West Coast Fires HiRes, Standard Product V1 (TRPSDL2COCRSWCFHI) at GES DISC version: 1"
        )

    TRPSDL2COCRSWCF_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSDL2COCRSWCF_1",
            provider="GES_DISC", 
            shortname="TRPSDL2COCRSWCF",
            version="1",
            description="TROPESS CrIS-SNPP L2 Carbon Monoxide for West Coast Fires, Standard Product V1 (TRPSDL2COCRSWCF) at GES DISC version: 1"
        )

    TRPSDL2HDOCRSAUS_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSDL2HDOCRSAUS_1",
            provider="GES_DISC", 
            shortname="TRPSDL2HDOCRSAUS",
            version="1",
            description="TROPESS CrIS-SNPP L2 Deuterated Water Vapor for Australian Fires, Standard Product V1 (TRPSDL2HDOCRSAUS) at GES DISC version: 1"
        )

    TRPSDL2HDOCRSFS_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSDL2HDOCRSFS_1",
            provider="GES_DISC", 
            shortname="TRPSDL2HDOCRSFS",
            version="1",
            description="TROPESS CrIS-SNPP L2 Deuterated Water Vapor for Forward Stream, Standard Product V1 (TRPSDL2HDOCRSFS) at GES DISC version: 1"
        )

    TRPSYL2HDOCRSFS_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSYL2HDOCRSFS_1",
            provider="GES_DISC", 
            shortname="TRPSYL2HDOCRSFS",
            version="1",
            description="TROPESS CrIS-SNPP L2 Deuterated Water Vapor for Forward Stream, Summary Product V1 (TRPSYL2HDOCRSFS) at GES DISC version: 1"
        )

    TRPSYL2HDOCRSRS_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSYL2HDOCRSRS_1",
            provider="GES_DISC", 
            shortname="TRPSYL2HDOCRSRS",
            version="1",
            description="TROPESS CrIS-SNPP L2 Deuterated Water Vapor for Reanalysis Stream, Summary Product V1 (TRPSYL2HDOCRSRS) at GES DISC version: 1"
        )

    TRPSDL2CH4CRSAUS_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSDL2CH4CRSAUS_1",
            provider="GES_DISC", 
            shortname="TRPSDL2CH4CRSAUS",
            version="1",
            description="TROPESS CrIS-SNPP L2 Methane for Australian Fires, Standard Product V1 (TRPSDL2CH4CRSAUS) at GES DISC version: 1"
        )

    TRPSDL2CH4CRSFS_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSDL2CH4CRSFS_1",
            provider="GES_DISC", 
            shortname="TRPSDL2CH4CRSFS",
            version="1",
            description="TROPESS CrIS-SNPP L2 Methane for Forward Stream, Standard Product V1 (TRPSDL2CH4CRSFS) at GES DISC version: 1"
        )

    TRPSYL2CH4CRSFS_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSYL2CH4CRSFS_1",
            provider="GES_DISC", 
            shortname="TRPSYL2CH4CRSFS",
            version="1",
            description="TROPESS CrIS-SNPP L2 Methane for Forward Stream, Summary Product V1 (TRPSYL2CH4CRSFS) at GES DISC version: 1"
        )

    TRPSYL2CH4CRSRS_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSYL2CH4CRSRS_1",
            provider="GES_DISC", 
            shortname="TRPSYL2CH4CRSRS",
            version="1",
            description="TROPESS CrIS-SNPP L2 Methane for Reanalysis Stream, Summary Product V1 (TRPSYL2CH4CRSRS) at GES DISC version: 1"
        )

    TRPSDL2O3CRSAUS_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSDL2O3CRSAUS_1",
            provider="GES_DISC", 
            shortname="TRPSDL2O3CRSAUS",
            version="1",
            description="TROPESS CrIS-SNPP L2 Ozone for Australian Fires, Standard Product V1 (TRPSDL2O3CRSAUS) at GES DISC version: 1"
        )

    TRPSDL2O3CRSFS_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSDL2O3CRSFS_1",
            provider="GES_DISC", 
            shortname="TRPSDL2O3CRSFS",
            version="1",
            description="TROPESS CrIS-SNPP L2 Ozone for Forward Stream, Standard Product V1 (TRPSDL2O3CRSFS) at GES DISC version: 1"
        )

    TRPSYL2O3CRSFS_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSYL2O3CRSFS_1",
            provider="GES_DISC", 
            shortname="TRPSYL2O3CRSFS",
            version="1",
            description="TROPESS CrIS-SNPP L2 Ozone for Forward Stream, Summary Product V1 (TRPSYL2O3CRSFS) at GES DISC version: 1"
        )

    TRPSYL2O3CRSRS_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSYL2O3CRSRS_1",
            provider="GES_DISC", 
            shortname="TRPSYL2O3CRSRS",
            version="1",
            description="TROPESS CrIS-SNPP L2 Ozone for Reanalysis Stream, Summary Product V1 (TRPSYL2O3CRSRS) at GES DISC version: 1"
        )

    TRPSDL2O3CRSWCFHI_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSDL2O3CRSWCFHI_1",
            provider="GES_DISC", 
            shortname="TRPSDL2O3CRSWCFHI",
            version="1",
            description="TROPESS CrIS-SNPP L2 Ozone for West Coast Fires HiRes, Standard Product V1 (TRPSDL2O3CRSWCFHI) at GES DISC version: 1"
        )

    TRPSDL2O3CRSWCF_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSDL2O3CRSWCF_1",
            provider="GES_DISC", 
            shortname="TRPSDL2O3CRSWCF",
            version="1",
            description="TROPESS CrIS-SNPP L2 Ozone for West Coast Fires, Standard Product V1 (TRPSDL2O3CRSWCF) at GES DISC version: 1"
        )

    TRPSDL2PANCRSAUS_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSDL2PANCRSAUS_1",
            provider="GES_DISC", 
            shortname="TRPSDL2PANCRSAUS",
            version="1",
            description="TROPESS CrIS-SNPP L2 Peroxyacetyl Nitrate for Australian Fires, Standard Product V1 (TRPSDL2PANCRSAUS) at GES DISC version: 1"
        )

    TRPSDL2PANCRSFS_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSDL2PANCRSFS_1",
            provider="GES_DISC", 
            shortname="TRPSDL2PANCRSFS",
            version="1",
            description="TROPESS CrIS-SNPP L2 Peroxyacetyl Nitrate for Forward Stream, Standard Product V1 (TRPSDL2PANCRSFS) at GES DISC version: 1"
        )

    TRPSYL2PANCRSFS_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSYL2PANCRSFS_1",
            provider="GES_DISC", 
            shortname="TRPSYL2PANCRSFS",
            version="1",
            description="TROPESS CrIS-SNPP L2 Peroxyacetyl Nitrate for Forward Stream, Summary Product V1 (TRPSYL2PANCRSFS) at GES DISC version: 1"
        )

    TRPSYL2PANCRSRS_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSYL2PANCRSRS_1",
            provider="GES_DISC", 
            shortname="TRPSYL2PANCRSRS",
            version="1",
            description="TROPESS CrIS-SNPP L2 Peroxyacetyl Nitrate for Reanalysis Stream, Summary Product V1 (TRPSYL2PANCRSRS) at GES DISC version: 1"
        )

    TRPSDL2PANCRSWCFHI_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSDL2PANCRSWCFHI_1",
            provider="GES_DISC", 
            shortname="TRPSDL2PANCRSWCFHI",
            version="1",
            description="TROPESS CrIS-SNPP L2 Peroxyacetyl Nitrate for West Coast Fires HiRes, Standard Product V1 (TRPSDL2PANCRSWCFHI) at GES DISC version: 1"
        )

    TRPSDL2PANCRSWCF_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSDL2PANCRSWCF_1",
            provider="GES_DISC", 
            shortname="TRPSDL2PANCRSWCF",
            version="1",
            description="TROPESS CrIS-SNPP L2 Peroxyacetyl Nitrate for West Coast Fires, Standard Product V1 (TRPSDL2PANCRSWCF) at GES DISC version: 1"
        )

    TRPSDL2H2OCRSAUS_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSDL2H2OCRSAUS_1",
            provider="GES_DISC", 
            shortname="TRPSDL2H2OCRSAUS",
            version="1",
            description="TROPESS CrIS-SNPP L2 Water for Australian Fires, Standard Product V1 (TRPSDL2H2OCRSAUS) at GES DISC version: 1"
        )

    TRPSDL2H2OCRSFS_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSDL2H2OCRSFS_1",
            provider="GES_DISC", 
            shortname="TRPSDL2H2OCRSFS",
            version="1",
            description="TROPESS CrIS-SNPP L2 Water for Forward Stream, Standard Product V1 (TRPSDL2H2OCRSFS) at GES DISC version: 1"
        )

    TRPSDL2ALLCRSMGBEI_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSDL2ALLCRSMGBEI_1",
            provider="GES_DISC", 
            shortname="TRPSDL2ALLCRSMGBEI",
            version="1",
            description="TROPESS CrIS-SNPP L2 for Beijing Megacity, Standard Product V1 (TRPSDL2ALLCRSMGBEI) at GES DISC version: 1"
        )

    TRPSYL2ALLCRSMGBEI_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSYL2ALLCRSMGBEI_1",
            provider="GES_DISC", 
            shortname="TRPSYL2ALLCRSMGBEI",
            version="1",
            description="TROPESS CrIS-SNPP L2 for Beijing Megacity, Summary Product V1 (TRPSYL2ALLCRSMGBEI) at GES DISC version: 1"
        )

    TRPSDL2ALLCRSMGDEL_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSDL2ALLCRSMGDEL_1",
            provider="GES_DISC", 
            shortname="TRPSDL2ALLCRSMGDEL",
            version="1",
            description="TROPESS CrIS-SNPP L2 for Delhi Megacity, Standard Product V1 (TRPSDL2ALLCRSMGDEL) at GES DISC version: 1"
        )

    TRPSYL2ALLCRSMGDEL_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSYL2ALLCRSMGDEL_1",
            provider="GES_DISC", 
            shortname="TRPSYL2ALLCRSMGDEL",
            version="1",
            description="TROPESS CrIS-SNPP L2 for Delhi Megacity, Summary Product V1 (TRPSYL2ALLCRSMGDEL) at GES DISC version: 1"
        )

    TRPSDL2ALLCRSMGKAR_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSDL2ALLCRSMGKAR_1",
            provider="GES_DISC", 
            shortname="TRPSDL2ALLCRSMGKAR",
            version="1",
            description="TROPESS CrIS-SNPP L2 for Karachi Megacity, Standard Product V1 (TRPSDL2ALLCRSMGKAR) at GES DISC version: 1"
        )

    TRPSYL2ALLCRSMGKAR_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSYL2ALLCRSMGKAR_1",
            provider="GES_DISC", 
            shortname="TRPSYL2ALLCRSMGKAR",
            version="1",
            description="TROPESS CrIS-SNPP L2 for Karachi Megacity, Summary Product V1 (TRPSYL2ALLCRSMGKAR) at GES DISC version: 1"
        )

    TRPSDL2ALLCRSMGLAG_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSDL2ALLCRSMGLAG_1",
            provider="GES_DISC", 
            shortname="TRPSDL2ALLCRSMGLAG",
            version="1",
            description="TROPESS CrIS-SNPP L2 for Lagos Megacity, Standard Product V1 (TRPSDL2ALLCRSMGLAG) at GES DISC version: 1"
        )

    TRPSYL2ALLCRSMGLAG_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSYL2ALLCRSMGLAG_1",
            provider="GES_DISC", 
            shortname="TRPSYL2ALLCRSMGLAG",
            version="1",
            description="TROPESS CrIS-SNPP L2 for Lagos Megacity, Summary Product V1 (TRPSYL2ALLCRSMGLAG) at GES DISC version: 1"
        )

    TRPSDL2ALLCRSMGLOS_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSDL2ALLCRSMGLOS_1",
            provider="GES_DISC", 
            shortname="TRPSDL2ALLCRSMGLOS",
            version="1",
            description="TROPESS CrIS-SNPP L2 for Los Angeles Megacity, Standard Product V1 (TRPSDL2ALLCRSMGLOS) at GES DISC version: 1"
        )

    TRPSYL2ALLCRSMGLOS_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSYL2ALLCRSMGLOS_1",
            provider="GES_DISC", 
            shortname="TRPSYL2ALLCRSMGLOS",
            version="1",
            description="TROPESS CrIS-SNPP L2 for Los Angeles Megacity, Summary Product V1 (TRPSYL2ALLCRSMGLOS) at GES DISC version: 1"
        )

    TRPSDL2ALLCRSMGMEX_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSDL2ALLCRSMGMEX_1",
            provider="GES_DISC", 
            shortname="TRPSDL2ALLCRSMGMEX",
            version="1",
            description="TROPESS CrIS-SNPP L2 for Mexico City Megacity, Standard Product V1 (TRPSDL2ALLCRSMGMEX) at GES DISC version: 1"
        )

    TRPSYL2ALLCRSMGMEX_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSYL2ALLCRSMGMEX_1",
            provider="GES_DISC", 
            shortname="TRPSYL2ALLCRSMGMEX",
            version="1",
            description="TROPESS CrIS-SNPP L2 for Mexico City Megacity, Summary Product V1 (TRPSYL2ALLCRSMGMEX) at GES DISC version: 1"
        )

    TRPSDL2ALLCRSMGSAO_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSDL2ALLCRSMGSAO_1",
            provider="GES_DISC", 
            shortname="TRPSDL2ALLCRSMGSAO",
            version="1",
            description="TROPESS CrIS-SNPP L2 for Sao Paulo Megacity, Standard Product V1 (TRPSDL2ALLCRSMGSAO) at GES DISC version: 1"
        )

    TRPSYL2ALLCRSMGSAO_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSYL2ALLCRSMGSAO_1",
            provider="GES_DISC", 
            shortname="TRPSYL2ALLCRSMGSAO",
            version="1",
            description="TROPESS CrIS-SNPP L2 for Sao Paulo Megacity, Summary Product V1 (TRPSYL2ALLCRSMGSAO) at GES DISC version: 1"
        )

    TRPSDL2ALLCRSMGTOK_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSDL2ALLCRSMGTOK_1",
            provider="GES_DISC", 
            shortname="TRPSDL2ALLCRSMGTOK",
            version="1",
            description="TROPESS CrIS-SNPP L2 for Tokyo Megacity, Standard Product V1 (TRPSDL2ALLCRSMGTOK) at GES DISC version: 1"
        )

    TRPSYL2ALLCRSMGTOK_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSYL2ALLCRSMGTOK_1",
            provider="GES_DISC", 
            shortname="TRPSYL2ALLCRSMGTOK",
            version="1",
            description="TROPESS CrIS-SNPP L2 for Tokyo Megacity, Summary Product V1 (TRPSYL2ALLCRSMGTOK) at GES DISC version: 1"
        )

    TRPSDL2O3OMIFS_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSDL2O3OMIFS_1",
            provider="GES_DISC", 
            shortname="TRPSDL2O3OMIFS",
            version="1",
            description="TROPESS OMI-Aura L2 Ozone for Forward Stream, Standard Product V1 (TRPSDL2O3OMIFS) at GES DISC version: 1"
        )

    TRPSYL2O3OMIFS_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TRPSYL2O3OMIFS_1",
            provider="GES_DISC", 
            shortname="TRPSYL2O3OMIFS",
            version="1",
            description="TROPESS OMI-Aura L2 Ozone for Forward Stream, Summary Product V1 (TRPSYL2O3OMIFS) at GES DISC version: 1"
        )

    TROPICS01ANTTL1A_V10_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TROPICS01ANTTL1A_1.0",
            provider="GES_DISC", 
            shortname="TROPICS01ANTTL1A",
            version="1.0",
            description="TROPICS01 Pathfinder L1A Orbital Geolocated Native-Resolution Antenna Temperatures V1.0 version: 1.0"
        )

    TROPICS01BRTTL1B_V10_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TROPICS01BRTTL1B_1.0",
            provider="GES_DISC", 
            shortname="TROPICS01BRTTL1B",
            version="1.0",
            description="TROPICS01 Pathfinder L1B Orbital Geolocated Native-Resolution Brightness Temperatures V1.0 version: 1.0"
        )

    TROPICS01URADL2A_V10_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TROPICS01URADL2A_1.0",
            provider="GES_DISC", 
            shortname="TROPICS01URADL2A",
            version="1.0",
            description="TROPICS01 Pathfinder L2A Unified Resolution Brightness Temperatures V1.0 version: 1.0"
        )

    TROPICS01MIRSL2B_V10_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TROPICS01MIRSL2B_1.0",
            provider="GES_DISC", 
            shortname="TROPICS01MIRSL2B",
            version="1.0",
            description="TROPICS01 Pathfinder L2B Atmospheric Vertical Temperature and Moisture Profiles (AVTP, AVMP) V1.0 version: 1.0"
        )

    TROPICS01PRPSL2B_V10_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TROPICS01PRPSL2B_1.0",
            provider="GES_DISC", 
            shortname="TROPICS01PRPSL2B",
            version="1.0",
            description="TROPICS01 Pathfinder L2B Instantaneous Surface Rain Rate (ISRR) V1.0 version: 1.0"
        )

    TROPICS01TCIEL2B_V10_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TROPICS01TCIEL2B_1.0",
            provider="GES_DISC", 
            shortname="TROPICS01TCIEL2B",
            version="1.0",
            description="TROPICS01 Pathfinder L2B Tropical Cyclone Intensity Estimate (TCIE) Algorithm V1.0 version: 1.0"
        )

    TROPICS03ANTTL1A_V10_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TROPICS03ANTTL1A_1.0",
            provider="GES_DISC", 
            shortname="TROPICS03ANTTL1A",
            version="1.0",
            description="TROPICS03 L1A Orbital Geolocated Native-Resolution Antenna Temperatures V1.0 version: 1.0"
        )

    TROPICS03BRTTL1B_V10_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TROPICS03BRTTL1B_1.0",
            provider="GES_DISC", 
            shortname="TROPICS03BRTTL1B",
            version="1.0",
            description="TROPICS03 L1B Orbital Geolocated Native-Resolution Brightness Temperatures V1.0 version: 1.0"
        )

    TROPICS03URADL2A_V10_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TROPICS03URADL2A_1.0",
            provider="GES_DISC", 
            shortname="TROPICS03URADL2A",
            version="1.0",
            description="TROPICS03 L2A Unified Resolution Brightness Temperatures V1.0 version: 1.0"
        )

    TROPICS03MIRSL2B_V10_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TROPICS03MIRSL2B_1.0",
            provider="GES_DISC", 
            shortname="TROPICS03MIRSL2B",
            version="1.0",
            description="TROPICS03 L2B Atmospheric Vertical Temperature and Moisture Profiles (AVTP, AVMP) V1.0 version: 1.0"
        )

    TROPICS03TCIEL2B_V10_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TROPICS03TCIEL2B_1.0",
            provider="GES_DISC", 
            shortname="TROPICS03TCIEL2B",
            version="1.0",
            description="TROPICS03 L2B Tropical Cyclone Intensity Estimate (TCIE) Algorithm V1.0 version: 1.0"
        )

    TROPICS03PRPSL2B_V10_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TROPICS03PRPSL2B_1.0",
            provider="GES_DISC", 
            shortname="TROPICS03PRPSL2B",
            version="1.0",
            description="TROPICS03 Pathfinder L2B Instantaneous Surface Rain Rate (ISRR) V1.0 version: 1.0"
        )

    TROPICS05ANTTL1A_V02_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TROPICS05ANTTL1A_0.2",
            provider="GES_DISC", 
            shortname="TROPICS05ANTTL1A",
            version="0.2",
            description="TROPICS05 L1A Orbital Geolocated Native-Resolution Antenna Temperatures V0.2 version: 0.2"
        )

    TROPICS05BRTTL1B_V02_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TROPICS05BRTTL1B_0.2",
            provider="GES_DISC", 
            shortname="TROPICS05BRTTL1B",
            version="0.2",
            description="TROPICS05 L1B Orbital Geolocated Native-Resolution Brightness Temperatures V0.2 version: 0.2"
        )

    TROPICS05URADL2A_V02_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TROPICS05URADL2A_0.2",
            provider="GES_DISC", 
            shortname="TROPICS05URADL2A",
            version="0.2",
            description="TROPICS05 L2A Unified Resolution Brightness Temperatures V0.2 version: 0.2"
        )

    TROPICS05TCIEL2B_V10_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TROPICS05TCIEL2B_1.0",
            provider="GES_DISC", 
            shortname="TROPICS05TCIEL2B",
            version="1.0",
            description="TROPICS05 L2B Tropical Cyclone Intensity Estimate (TCIE) Algorithm V1.0 version: 1.0"
        )

    TROPICS05PRPSL2B_V02_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TROPICS05PRPSL2B_0.2",
            provider="GES_DISC", 
            shortname="TROPICS05PRPSL2B",
            version="0.2",
            description="TROPICS05 Pathfinder L2B Instantaneous Surface Rain Rate (ISRR) V0.2 version: 0.2"
        )

    TROPICS06ANTTL1A_V10_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TROPICS06ANTTL1A_1.0",
            provider="GES_DISC", 
            shortname="TROPICS06ANTTL1A",
            version="1.0",
            description="TROPICS06 L1A Orbital Geolocated Native-Resolution Antenna Temperatures V1.0 version: 1.0"
        )

    TROPICS06BRTTL1B_V10_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TROPICS06BRTTL1B_1.0",
            provider="GES_DISC", 
            shortname="TROPICS06BRTTL1B",
            version="1.0",
            description="TROPICS06 L1B Orbital Geolocated Native-Resolution Brightness Temperatures V1.0 version: 1.0"
        )

    TROPICS06URADL2A_V10_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TROPICS06URADL2A_1.0",
            provider="GES_DISC", 
            shortname="TROPICS06URADL2A",
            version="1.0",
            description="TROPICS06 L2A Unified Resolution Brightness Temperatures V1.0 version: 1.0"
        )

    TROPICS06MIRSL2B_V10_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TROPICS06MIRSL2B_1.0",
            provider="GES_DISC", 
            shortname="TROPICS06MIRSL2B",
            version="1.0",
            description="TROPICS06 L2B Atmospheric Vertical Temperature and Moisture Profiles (AVTP, AVMP) V1.0 version: 1.0"
        )

    TROPICS06TCIEL2B_V10_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TROPICS06TCIEL2B_1.0",
            provider="GES_DISC", 
            shortname="TROPICS06TCIEL2B",
            version="1.0",
            description="TROPICS06 L2B Tropical Cyclone Intensity Estimate (TCIE) Algorithm V1.0 version: 1.0"
        )

    TROPICS06PRPSL2B_V10_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TROPICS06PRPSL2B_1.0",
            provider="GES_DISC", 
            shortname="TROPICS06PRPSL2B",
            version="1.0",
            description="TROPICS06 Pathfinder L2B Instantaneous Surface Rain Rate (ISRR) V1.0 version: 1.0"
        )

    TROPICS07ANTTL1A_V02_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TROPICS07ANTTL1A_0.2",
            provider="GES_DISC", 
            shortname="TROPICS07ANTTL1A",
            version="0.2",
            description="TROPICS07 L1A Orbital Geolocated Native-Resolution Antenna Temperatures V0.2 version: 0.2"
        )

    TROPICS07BRTTL1B_V02_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TROPICS07BRTTL1B_0.2",
            provider="GES_DISC", 
            shortname="TROPICS07BRTTL1B",
            version="0.2",
            description="TROPICS07 L1B Orbital Geolocated Native-Resolution Brightness Temperatures V0.2 version: 0.2"
        )

    TROPICS07URADL2A_V02_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TROPICS07URADL2A_0.2",
            provider="GES_DISC", 
            shortname="TROPICS07URADL2A",
            version="0.2",
            description="TROPICS07 L2A Unified Resolution Brightness Temperatures V0.2 version: 0.2"
        )

    TROPICS07TCIEL2B_V10_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TROPICS07TCIEL2B_1.0",
            provider="GES_DISC", 
            shortname="TROPICS07TCIEL2B",
            version="1.0",
            description="TROPICS07 L2B Tropical Cyclone Intensity Estimate (TCIE) Algorithm V1.0 version: 1.0"
        )

    TROPOMI_MINDS_NO2_V11_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TROPOMI_MINDS_NO2_1.1",
            provider="GES_DISC", 
            shortname="TROPOMI_MINDS_NO2",
            version="1.1",
            description="TROPOMI/S5P NO2 Tropospheric, Stratospheric and Total Columns MINDS 1-Orbit L2 Swath 5.5 km x 3.5 km V1.1 (TROPOMI_MINDS_NO2) at GES DISC version: 1.1"
        )

    TROPOMAER_V1_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TROPOMAER_1",
            provider="GES_DISC", 
            shortname="TROPOMAER",
            version="1",
            description="TROPOMI/Sentinel-5P Near UV Aerosol Optical Depth and Single Scattering Albedo L2 1-Orbit Snapshot 7.5 km x 3 km version: 1"
        )

    TSIS_SSI_L3_12HR_V12_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TSIS_SSI_L3_12HR_12",
            provider="GES_DISC", 
            shortname="TSIS_SSI_L3_12HR",
            version="12",
            description="TSIS SIM Level 3 Solar Spectral Irradiance 12-Hour Means V12 (TSIS_SSI_L3_12HR) at GES DISC version: 12"
        )

    TSIS_SSI_L3_24HR_V12_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TSIS_SSI_L3_24HR_12",
            provider="GES_DISC", 
            shortname="TSIS_SSI_L3_24HR",
            version="12",
            description="TSIS SIM Level 3 Solar Spectral Irradiance 24-Hour Means V12 (TSIS_SSI_L3_24HR) at GES DISC version: 12"
        )

    TSIS_TSI_L3_24HR_V04_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TSIS_TSI_L3_24HR_04",
            provider="GES_DISC", 
            shortname="TSIS_TSI_L3_24HR",
            version="04",
            description="TSIS TIM Level 3 Total Solar Irradiance 24-Hour Means V04 (TSIS_TSI_L3_24HR) at GES DISC version: 04"
        )

    TSIS_TSI_L3_06HR_V04_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_TSIS_TSI_L3_06HR_04",
            provider="GES_DISC", 
            shortname="TSIS_TSI_L3_06HR",
            version="04",
            description="TSIS TIM Level 3 Total Solar Irradiance 6-Hour Means V04 (TSIS_TSI_L3_06HR) at GES DISC version: 04"
        )

    UARZCNMC_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_UARZCNMC_001",
            provider="GES_DISC", 
            shortname="UARZCNMC",
            version="001",
            description="UARS Correlative NMC Daily Gridded Stratospheric Assimilated Data V001 (UARZCNMC) at GES DISC version: 001"
        )

    UARZCUKM_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_UARZCUKM_001",
            provider="GES_DISC", 
            shortname="UARZCUKM",
            version="001",
            description="UARS Correlative UKMO Daily Gridded Stratospheric Assimilated Data V001 (UARZCUKM) at GES DISC version: 001"
        )

    UARCL3AL_V009_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_UARCL3AL_009",
            provider="GES_DISC", 
            shortname="UARCL3AL",
            version="009",
            description="UARS Cryogenic Limb Array Etalon Spectrometer (CLAES) Level 3AL V009 (UARCL3AL) at GES DISC version: 009"
        )

    UARCL3AT_V009_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_UARCL3AT_009",
            provider="GES_DISC", 
            shortname="UARCL3AT",
            version="009",
            description="UARS Cryogenic Limb Array Etalon Spectrometer (CLAES) Level 3AT V009 (UARCL3AT) at GES DISC version: 009"
        )

    UARHA2FN_V019_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_UARHA2FN_019",
            provider="GES_DISC", 
            shortname="UARHA2FN",
            version="019",
            description="UARS Halogen Occultation Experiment (HALOE) Level 2 V019 (UARHA2FN) at GES DISC version: 019"
        )

    UARHA3AT_V019_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_UARHA3AT_019",
            provider="GES_DISC", 
            shortname="UARHA3AT",
            version="019",
            description="UARS Halogen Occultation Experiment (HALOE) Level 3AT V019 (UARHA3AT) at GES DISC version: 019"
        )

    UARHR3AL_V011_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_UARHR3AL_011",
            provider="GES_DISC", 
            shortname="UARHR3AL",
            version="011",
            description="UARS High Resolution Doppler Imager (HRDI) Level 3AL V011 (UARHR3AL) at GES DISC version: 011"
        )

    UARHR3AT_V011_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_UARHR3AT_011",
            provider="GES_DISC", 
            shortname="UARHR3AT",
            version="011",
            description="UARS High Resolution Doppler Imager (HRDI) Level 3AT V011 (UARHR3AT) at GES DISC version: 011"
        )

    UARIS3AL_V010_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_UARIS3AL_010",
            provider="GES_DISC", 
            shortname="UARIS3AL",
            version="010",
            description="UARS Improved Stratospheric and Mesospheric Sounder (ISAMS) Level 3AL V010 (UARIS3AL) at GES DISC version: 010"
        )

    UARIS3AT_V010_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_UARIS3AT_010",
            provider="GES_DISC", 
            shortname="UARIS3AT",
            version="010",
            description="UARS Improved Stratospheric and Mesospheric Sounder (ISAMS) Level 3AT V010 (UARIS3AT) at GES DISC version: 010"
        )

    UARML3AL_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_UARML3AL_005",
            provider="GES_DISC", 
            shortname="UARML3AL",
            version="005",
            description="UARS Microwave Limb Sounder (MLS) Level 3AL V005 (UARML3AL) at GES DISC version: 005"
        )

    UARML3AT_V005_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_UARML3AT_005",
            provider="GES_DISC", 
            shortname="UARML3AT",
            version="005",
            description="UARS Microwave Limb Sounder (MLS) Level 3AT V005 (UARML3AT) at GES DISC version: 005"
        )

    UARPE2AXIS1_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_UARPE2AXIS1_001",
            provider="GES_DISC", 
            shortname="UARPE2AXIS1",
            version="001",
            description="UARS PEM Level 2 AXIS 1 V001 (UARPE2AXIS1) at GES DISC version: 001"
        )

    UARPE2AXIS2_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_UARPE2AXIS2_001",
            provider="GES_DISC", 
            shortname="UARPE2AXIS2",
            version="001",
            description="UARS PEM Level 2 AXIS 2 V001 (UARPE2AXIS2) at GES DISC version: 001"
        )

    UARPE2HEPSA_V002_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_UARPE2HEPSA_002",
            provider="GES_DISC", 
            shortname="UARPE2HEPSA",
            version="002",
            description="UARS PEM Level 2 HEPS A V002 (UARPE2HEPSA) at GES DISC version: 002"
        )

    UARPE2HEPSB_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_UARPE2HEPSB_001",
            provider="GES_DISC", 
            shortname="UARPE2HEPSB",
            version="001",
            description="UARS PEM Level 2 HEPS B V001 (UARPE2HEPSB) at GES DISC version: 001"
        )

    UARPE2MEPS_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_UARPE2MEPS_001",
            provider="GES_DISC", 
            shortname="UARPE2MEPS",
            version="001",
            description="UARS PEM Level 2 MEPS V001 (UARPE2MEPS) at GES DISC version: 001"
        )

    UARPE2VMAGAC_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_UARPE2VMAGAC_001",
            provider="GES_DISC", 
            shortname="UARPE2VMAGAC",
            version="001",
            description="UARS PEM Level 2 VMAG AC V001 (UARPE2VMAGAC) at GES DISC version: 001"
        )

    UARPE2VMAGDC_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_UARPE2VMAGDC_001",
            provider="GES_DISC", 
            shortname="UARPE2VMAGDC",
            version="001",
            description="UARS PEM Level 2 VMAG DC V001 (UARPE2VMAGDC) at GES DISC version: 001"
        )

    UARPE3AT_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_UARPE3AT_004",
            provider="GES_DISC", 
            shortname="UARPE3AT",
            version="004",
            description="UARS Particle Environment Monitor (PEM) Level 3AT V004 (UARPE3AT) at GES DISC version: 004"
        )

    UARPE3TP_V004_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_UARPE3TP_004",
            provider="GES_DISC", 
            shortname="UARPE3TP",
            version="004",
            description="UARS Particle Environment Monitor (PEM) Level 3TP V004 (UARPE3TP) at GES DISC version: 004"
        )

    UARSU3BS_V022_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_UARSU3BS_022",
            provider="GES_DISC", 
            shortname="UARSU3BS",
            version="022",
            description="UARS Solar Ultraviolet Spectral Irradiance Monitor (SUSIM) Level 3BS V022 (UARSU3BS) at GES DISC version: 022"
        )

    UARSO3BS_V018_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_UARSO3BS_018",
            provider="GES_DISC", 
            shortname="UARSO3BS",
            version="018",
            description="UARS Solar-Stellar Irradiance Comparison Experiment (SOLSTICE) Level 3BS V018 (UARSO3BS) at GES DISC version: 018"
        )

    UARWI3AL_V011_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_UARWI3AL_011",
            provider="GES_DISC", 
            shortname="UARWI3AL",
            version="011",
            description="UARS Wind Imaging Interferometer (WINDII) Level 3AL V011 (UARWI3AL) at GES DISC version: 011"
        )

    UARWI3AT_V011_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_UARWI3AT_011",
            provider="GES_DISC", 
            shortname="UARWI3AT",
            version="011",
            description="UARS Wind Imaging Interferometer (WINDII) Level 3AT V011 (UARWI3AT) at GES DISC version: 011"
        )

    VISSRGOES1IMIR_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_VISSRGOES1IMIR_001",
            provider="GES_DISC", 
            shortname="VISSRGOES1IMIR",
            version="001",
            description="VISSR/GOES-1 Infrared Imagery on 70mm Film V001 (VISSRGOES1IMIR) at GES DISC version: 001"
        )

    VISSRGOES1IMVIS_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_VISSRGOES1IMVIS_001",
            provider="GES_DISC", 
            shortname="VISSRGOES1IMVIS",
            version="001",
            description="VISSR/GOES-1 Visible Imagery on 70mm Film V001 (VISSRGOES1IMVIS) at GES DISC version: 001"
        )

    VISSRGOES2IMIR_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_VISSRGOES2IMIR_001",
            provider="GES_DISC", 
            shortname="VISSRGOES2IMIR",
            version="001",
            description="VISSR/GOES-2 Infrared Imagery on 70mm Film V001 (VISSRGOES2IMIR) at GES DISC version: 001"
        )

    VISSRGOES2IMVIS_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_VISSRGOES2IMVIS_001",
            provider="GES_DISC", 
            shortname="VISSRGOES2IMVIS",
            version="001",
            description="VISSR/GOES-2 Visible Imagery on 70mm Film V001 (VISSRGOES2IMVIS) at GES DISC version: 001"
        )

    VISSRGOES3IMIR_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_VISSRGOES3IMIR_001",
            provider="GES_DISC", 
            shortname="VISSRGOES3IMIR",
            version="001",
            description="VISSR/GOES-3 Infrared Imagery on 70mm Film V001 (VISSRGOES3IMIR) at GES DISC version: 001"
        )

    VISSRGOES3IMVIS_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_VISSRGOES3IMVIS_001",
            provider="GES_DISC", 
            shortname="VISSRGOES3IMVIS",
            version="001",
            description="VISSR/GOES-3 Visible Imagery on 70mm Film V001 (VISSRGOES3IMVIS) at GES DISC version: 001"
        )

    VISSRSMS1IMIR_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_VISSRSMS1IMIR_001",
            provider="GES_DISC", 
            shortname="VISSRSMS1IMIR",
            version="001",
            description="VISSR/SMS-1 Infrared Imagery on 70mm Film V001 (VISSRSMS1IMIR) at GES DISC version: 001"
        )

    VISSRSMS1L1AOIPS_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_VISSRSMS1L1AOIPS_001",
            provider="GES_DISC", 
            shortname="VISSRSMS1L1AOIPS",
            version="001",
            description="VISSR/SMS-1 Level 1 Atmospheric and Oceanographic Image Processing System (AOIPS) Data V001 (VISSRSMS1L1AOIPS) at GES DISC version: 001"
        )

    VISSRSMS1L1EHT_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_VISSRSMS1L1EHT_001",
            provider="GES_DISC", 
            shortname="VISSRSMS1L1EHT",
            version="001",
            description="VISSR/SMS-1 Level 1 Experimenter History Data V001 (VISSRSMS1L1EHT) at GES DISC version: 001"
        )

    VISSRSMS1IMVIS_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_VISSRSMS1IMVIS_001",
            provider="GES_DISC", 
            shortname="VISSRSMS1IMVIS",
            version="001",
            description="VISSR/SMS-1 Visible Imagery on 70mm Film V001 (VISSRSMS1IMVIS) at GES DISC version: 001"
        )

    VISSRSMS2IMIR_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_VISSRSMS2IMIR_001",
            provider="GES_DISC", 
            shortname="VISSRSMS2IMIR",
            version="001",
            description="VISSR/SMS-2 Infrared Imagery on 70mm Film V001 (VISSRSMS2IMIR) at GES DISC version: 001"
        )

    VISSRSMS2L1AOIPS_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_VISSRSMS2L1AOIPS_001",
            provider="GES_DISC", 
            shortname="VISSRSMS2L1AOIPS",
            version="001",
            description="VISSR/SMS-2 Level 1 Atmospheric and Oceanographic Image Processing System (AOIPS) Data V001 (VISSRSMS2L1AOIPS) at GES DISC version: 001"
        )

    VISSRSMS2L1EHT_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_VISSRSMS2L1EHT_001",
            provider="GES_DISC", 
            shortname="VISSRSMS2L1EHT",
            version="001",
            description="VISSR/SMS-2 Level 1 Experimenter History Data V001 (VISSRSMS2L1EHT) at GES DISC version: 001"
        )

    VISSRSMS2IMVIS_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_VISSRSMS2IMVIS_001",
            provider="GES_DISC", 
            shortname="VISSRSMS2IMVIS",
            version="001",
            description="VISSR/SMS-2 Visible Imagery on 70mm Film V001 (VISSRSMS2IMVIS) at GES DISC version: 001"
        )

    WLDAS_NOAHMP001_DA1_VD10_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_WLDAS_NOAHMP001_DA1_D1.0",
            provider="GES_DISC", 
            shortname="WLDAS_NOAHMP001_DA1",
            version="D1.0",
            description="WLDAS Noah-MP 3.6 Land Surface Model L4 Daily 0.01 degree x 0.01 degree Version D1.0 (WLDAS_NOAHMP001_DA1) at GES DISC version: D1.0"
        )

    LPRM_WINDSAT_SOILM2_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_LPRM_WINDSAT_SOILM2_001",
            provider="GES_DISC", 
            shortname="LPRM_WINDSAT_SOILM2",
            version="001",
            description="WindSat/Coriolis surface soil moisture (LPRM) L2 V001 (LPRM_WINDSAT_SOILM2) at GES DISC version: 001"
        )

    LPRM_WINDSAT_DY_SOILM3_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_LPRM_WINDSAT_DY_SOILM3_001",
            provider="GES_DISC", 
            shortname="LPRM_WINDSAT_DY_SOILM3",
            version="001",
            description="WindSat/Coriolis surface soil moisture (LPRM) L3 1 day 25 km x 25 km daytime V001 (LPRM_WINDSAT_DY_SOILM3) at GES DISC version: 001"
        )

    LPRM_WINDSAT_NT_SOILM3_V001_GES_DISC = DataCollectionDefinition(
            api_id="CMR",
            collections="GES_DISC_LPRM_WINDSAT_NT_SOILM3_001",
            provider="GES_DISC", 
            shortname="LPRM_WINDSAT_NT_SOILM3",
            version="001",
            description="WindSat/Coriolis surface soil moisture (LPRM) L3 1 day 25 km x 25 km nighttime V001 (LPRM_WINDSAT_NT_SOILM3) at GES DISC version: 001"
        )

