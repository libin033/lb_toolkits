# -*- coding:utf-8 -*-

from lb_toolkits.DataCollections.DataCollectionDefinition import DataCollectionDefinition 

class DataCollectionPOCLOUD : 
    SEAGLIDER_GUAM_2019_VV1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SEAGLIDER_GUAM_2019_V1",
            provider="POCLOUD", 
            shortname="SEAGLIDER_GUAM_2019",
            version="V1",
            description="Adaptive Sampling of Rain and Ocean Salinity from Autonomous Seagliders (Guam 2019-2020) version: V1"
        )

    AQUARIUS_L2_SSS_CAP_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L2_SSS_CAP_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L2_SSS_CAP_V5",
            version="5.0",
            description="Aquarius CAP Level 2 Sea Surface Salinity, Wind Speed & Direction Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SSS_RAINCORRECTED_CAP_7DAY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SSS_RAINCORRECTED_CAP_7DAY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SSS_RAINCORRECTED_CAP_7DAY_V5",
            version="5.0",
            description="Aquarius CAP Level 3 Sea Surface Salinity Rain Corrected Standard Mapped Image 7-Day Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SSS_RAINCORRECTED_CAP_MONTHLY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SSS_RAINCORRECTED_CAP_MONTHLY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SSS_RAINCORRECTED_CAP_MONTHLY_V5",
            version="5.0",
            description="Aquarius CAP Level 3 Sea Surface Salinity Rain Corrected Standard Mapped Image Monthly Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SSS_CAP_7DAY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SSS_CAP_7DAY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SSS_CAP_7DAY_V5",
            version="5.0",
            description="Aquarius CAP Level 3 Sea Surface Salinity Standard Mapped Image 7-Day Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SSS_CAP_MONTHLY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SSS_CAP_MONTHLY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SSS_CAP_MONTHLY_V5",
            version="5.0",
            description="Aquarius CAP Level 3 Sea Surface Salinity Standard Mapped Image Monthly Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_WIND_SPEED_CAP_7DAY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_WIND_SPEED_CAP_7DAY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_WIND_SPEED_CAP_7DAY_V5",
            version="5.0",
            description="Aquarius CAP Level 3 Wind Speed Standard Mapped Image 7-Day Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_WIND_SPEED_CAP_MONTHLY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_WIND_SPEED_CAP_MONTHLY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_WIND_SPEED_CAP_MONTHLY_V5",
            version="5.0",
            description="Aquarius CAP Level 3 Wind Speed Standard Mapped Image Monthly Data V5.0 version: 5.0"
        )

    AQUARIUS_ANCILLARY_CELESTIALSKY_V1_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_ANCILLARY_CELESTIALSKY_V1_1",
            provider="POCLOUD", 
            shortname="AQUARIUS_ANCILLARY_CELESTIALSKY_V1",
            version="1",
            description="Aquarius Celestial Sky Microwave Emission Map Ancillary Dataset V1.0 version: 1"
        )

    AQUARIUS_L2_SSS_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L2_SSS_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L2_SSS_V5",
            version="5.0",
            description="Aquarius Official Release Level 2 Sea Surface Salinity & Wind Speed Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_ANCILLARY_SST_SMI_28DAY_RUNNINGMEAN_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_ANCILLARY_SST_SMI_28DAY-RUNNINGMEAN_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_ANCILLARY_SST_SMI_28DAY-RUNNINGMEAN_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Ancillary Reynolds Sea Surface Temperature Standard Mapped Image 28-Day Running Mean Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_ANCILLARY_SST_SMI_7DAY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_ANCILLARY_SST_SMI_7DAY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_ANCILLARY_SST_SMI_7DAY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Ancillary Reynolds Sea Surface Temperature Standard Mapped Image 7-Day Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_ANCILLARY_SST_SMI_7DAY_RUNNINGMEAN_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_ANCILLARY_SST_SMI_7DAY-RUNNINGMEAN_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_ANCILLARY_SST_SMI_7DAY-RUNNINGMEAN_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Ancillary Reynolds Sea Surface Temperature Standard Mapped Image 7-Day Running Mean Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_ANCILLARY_SST_SMI_ANNUAL_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_ANCILLARY_SST_SMI_ANNUAL_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_ANCILLARY_SST_SMI_ANNUAL_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Ancillary Reynolds Sea Surface Temperature Standard Mapped Image Annual Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_ANCILLARY_SST_SMIA_28DAY_RUNNINGMEAN_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_ANCILLARY_SST_SMIA_28DAY-RUNNINGMEAN_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_ANCILLARY_SST_SMIA_28DAY-RUNNINGMEAN_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Ancillary Reynolds Sea Surface Temperature Standard Mapped Image Ascending 28-Day Running Mean Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_ANCILLARY_SST_SMIA_7DAY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_ANCILLARY_SST_SMIA_7DAY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_ANCILLARY_SST_SMIA_7DAY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Ancillary Reynolds Sea Surface Temperature Standard Mapped Image Ascending 7-Day Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_ANCILLARY_SST_SMIA_ANNUAL_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_ANCILLARY_SST_SMIA_ANNUAL_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_ANCILLARY_SST_SMIA_ANNUAL_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Ancillary Reynolds Sea Surface Temperature Standard Mapped Image Ascending Annual Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_ANCILLARY_SST_SMIA_DAILY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_ANCILLARY_SST_SMIA_DAILY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_ANCILLARY_SST_SMIA_DAILY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Ancillary Reynolds Sea Surface Temperature Standard Mapped Image Ascending Daily Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_ANCILLARY_SST_SMIA_CUMULATIVE_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_ANCILLARY_SST_SMIA_CUMULATIVE_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_ANCILLARY_SST_SMIA_CUMULATIVE_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Ancillary Reynolds Sea Surface Temperature Standard Mapped Image Ascending Mission Cumulative Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_ANCILLARY_SST_SMIA_MONTHLY_CLIMATOLOGY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_ANCILLARY_SST_SMIA_MONTHLY-CLIMATOLOGY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_ANCILLARY_SST_SMIA_MONTHLY-CLIMATOLOGY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Ancillary Reynolds Sea Surface Temperature Standard Mapped Image Ascending Monthly Climatology Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_ANCILLARY_SST_SMIA_MONTHLY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_ANCILLARY_SST_SMIA_MONTHLY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_ANCILLARY_SST_SMIA_MONTHLY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Ancillary Reynolds Sea Surface Temperature Standard Mapped Image Ascending Monthly Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_ANCILLARY_SST_SMIA_SEASONAL_CLIMATOLOGY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_ANCILLARY_SST_SMIA_SEASONAL-CLIMATOLOGY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_ANCILLARY_SST_SMIA_SEASONAL-CLIMATOLOGY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Ancillary Reynolds Sea Surface Temperature Standard Mapped Image Ascending Seasonal Climatology Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_ANCILLARY_SST_SMIA_3MONTH_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_ANCILLARY_SST_SMIA_3MONTH_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_ANCILLARY_SST_SMIA_3MONTH_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Ancillary Reynolds Sea Surface Temperature Standard Mapped Image Ascending Seasonal Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_ANCILLARY_SST_SMI_DAILY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_ANCILLARY_SST_SMI_DAILY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_ANCILLARY_SST_SMI_DAILY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Ancillary Reynolds Sea Surface Temperature Standard Mapped Image Daily Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_ANCILLARY_SST_SMID_28DAY_RUNNINGMEAN_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_ANCILLARY_SST_SMID_28DAY-RUNNINGMEAN_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_ANCILLARY_SST_SMID_28DAY-RUNNINGMEAN_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Ancillary Reynolds Sea Surface Temperature Standard Mapped Image Descending 28-Day Running Mean Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_ANCILLARY_SST_SMID_7DAY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_ANCILLARY_SST_SMID_7DAY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_ANCILLARY_SST_SMID_7DAY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Ancillary Reynolds Sea Surface Temperature Standard Mapped Image Descending 7-Day Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_ANCILLARY_SST_SMID_ANNUAL_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_ANCILLARY_SST_SMID_ANNUAL_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_ANCILLARY_SST_SMID_ANNUAL_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Ancillary Reynolds Sea Surface Temperature Standard Mapped Image Descending Annual Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_ANCILLARY_SST_SMID_DAILY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_ANCILLARY_SST_SMID_DAILY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_ANCILLARY_SST_SMID_DAILY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Ancillary Reynolds Sea Surface Temperature Standard Mapped Image Descending Daily Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_ANCILLARY_SST_SMID_CUMULATIVE_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_ANCILLARY_SST_SMID_CUMULATIVE_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_ANCILLARY_SST_SMID_CUMULATIVE_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Ancillary Reynolds Sea Surface Temperature Standard Mapped Image Descending Mission Cumulative Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_ANCILLARY_SST_SMID_MONTHLY_CLIMATOLOGY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_ANCILLARY_SST_SMID_MONTHLY-CLIMATOLOGY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_ANCILLARY_SST_SMID_MONTHLY-CLIMATOLOGY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Ancillary Reynolds Sea Surface Temperature Standard Mapped Image Descending Monthly Climatology Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_ANCILLARY_SST_SMID_MONTHLY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_ANCILLARY_SST_SMID_MONTHLY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_ANCILLARY_SST_SMID_MONTHLY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Ancillary Reynolds Sea Surface Temperature Standard Mapped Image Descending Monthly Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_ANCILLARY_SST_SMID_SEASONAL_CLIMATOLOGY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_ANCILLARY_SST_SMID_SEASONAL-CLIMATOLOGY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_ANCILLARY_SST_SMID_SEASONAL-CLIMATOLOGY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Ancillary Reynolds Sea Surface Temperature Standard Mapped Image Descending Seasonal Climatology Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_ANCILLARY_SST_SMID_3MONTH_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_ANCILLARY_SST_SMID_3MONTH_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_ANCILLARY_SST_SMID_3MONTH_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Ancillary Reynolds Sea Surface Temperature Standard Mapped Image Descending Seasonal Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_ANCILLARY_SST_SMI_CUMULATIVE_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_ANCILLARY_SST_SMI_CUMULATIVE_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_ANCILLARY_SST_SMI_CUMULATIVE_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Ancillary Reynolds Sea Surface Temperature Standard Mapped Image Mission Cumulative Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_ANCILLARY_SST_SMI_MONTHLY_CLIMATOLOGY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_ANCILLARY_SST_SMI_MONTHLY-CLIMATOLOGY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_ANCILLARY_SST_SMI_MONTHLY-CLIMATOLOGY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Ancillary Reynolds Sea Surface Temperature Standard Mapped Image Monthly Climatology Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_ANCILLARY_SST_SMI_MONTHLY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_ANCILLARY_SST_SMI_MONTHLY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_ANCILLARY_SST_SMI_MONTHLY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Ancillary Reynolds Sea Surface Temperature Standard Mapped Image Monthly Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_ANCILLARY_SST_SMI_SEASONAL_CLIMATOLOGY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_ANCILLARY_SST_SMI_SEASONAL-CLIMATOLOGY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_ANCILLARY_SST_SMI_SEASONAL-CLIMATOLOGY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Ancillary Reynolds Sea Surface Temperature Standard Mapped Image Seasonal Climatology Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_ANCILLARY_SST_SMI_3MONTH_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_ANCILLARY_SST_SMI_3MONTH_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_ANCILLARY_SST_SMI_3MONTH_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Ancillary Reynolds Sea Surface Temperature Standard Mapped Image Seasonal Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SSS_RAINFLAGGED_SM_SMIA_MONTHLY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SSS-RainFlagged_SM_SMIA_MONTHLY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SSS-RainFlagged_SM_SMIA_MONTHLY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Smoothed Standard Mapped Image Ascending Monthly Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SSS_RAINFLAGGED_SM_SMID_MONTHLY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SSS-RainFlagged_SM_SMID_MONTHLY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SSS-RainFlagged_SM_SMID_MONTHLY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Smoothed Standard Mapped Image Descending Monthly Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SSS_RAINFLAGGED_SM_SMI_MONTHLY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SSS-RainFlagged_SM_SMI_MONTHLY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SSS-RainFlagged_SM_SMI_MONTHLY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Smoothed Standard Mapped Image Monthly Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SSS_RAINFLAGGED_SMI_28DAY_RUNNINGMEAN_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SSS-RainFlagged_SMI_28DAY-RUNNINGMEAN_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SSS-RainFlagged_SMI_28DAY-RUNNINGMEAN_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image 28-Day Running Mean Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SSS_RAINFLAGGED_SMI_7DAY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SSS-RainFlagged_SMI_7DAY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SSS-RainFlagged_SMI_7DAY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image 7-Day Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SSS_RAINFLAGGED_SMI_7DAY_RUNNINGMEAN_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SSS-RainFlagged_SMI_7DAY-RUNNINGMEAN_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SSS-RainFlagged_SMI_7DAY-RUNNINGMEAN_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image 7-Day Running Mean Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SSS_RAINFLAGGED_SMI_ANNUAL_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SSS-RainFlagged_SMI_ANNUAL_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SSS-RainFlagged_SMI_ANNUAL_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image Annual Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SSS_RAINFLAGGED_SMIA_28DAY_RUNNINGMEAN_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SSS-RainFlagged_SMIA_28DAY-RUNNINGMEAN_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SSS-RainFlagged_SMIA_28DAY-RUNNINGMEAN_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image Ascending 28-Day Running Mean Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SSS_RAINFLAGGED_SMIA_7DAY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SSS-RainFlagged_SMIA_7DAY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SSS-RainFlagged_SMIA_7DAY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image Ascending 7-Day Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SSS_RAINFLAGGED_SMIA_ANNUAL_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SSS-RainFlagged_SMIA_ANNUAL_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SSS-RainFlagged_SMIA_ANNUAL_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image Ascending Annual Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SSS_RAINFLAGGED_SMIA_DAILY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SSS-RainFlagged_SMIA_DAILY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SSS-RainFlagged_SMIA_DAILY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image Ascending Daily Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SSS_RAINFLAGGED_SMIA_CUMULATIVE_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SSS-RainFlagged_SMIA_CUMULATIVE_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SSS-RainFlagged_SMIA_CUMULATIVE_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image Ascending Mission Cumulative Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SSS_RAINFLAGGED_SMIA_MONTHLY_CLIMATOLOGY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SSS-RainFlagged_SMIA_MONTHLY-CLIMATOLOGY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SSS-RainFlagged_SMIA_MONTHLY-CLIMATOLOGY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image Ascending Monthly Climatology Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SSS_RAINFLAGGED_SMIA_MONTHLY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SSS-RainFlagged_SMIA_MONTHLY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SSS-RainFlagged_SMIA_MONTHLY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image Ascending Monthly Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SSS_RAINFLAGGED_SMIA_SEASONAL_CLIMATOLOGY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SSS-RainFlagged_SMIA_SEASONAL-CLIMATOLOGY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SSS-RainFlagged_SMIA_SEASONAL-CLIMATOLOGY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image Ascending Seasonal Climatology Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SSS_RAINFLAGGED_SMIA_3MONTH_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SSS-RainFlagged_SMIA_3MONTH_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SSS-RainFlagged_SMIA_3MONTH_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image Ascending Seasonal Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SSS_RAINFLAGGED_SMI_DAILY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SSS-RainFlagged_SMI_DAILY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SSS-RainFlagged_SMI_DAILY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image Daily Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SSS_RAINFLAGGED_SMID_28DAY_RUNNINGMEAN_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SSS-RainFlagged_SMID_28DAY-RUNNINGMEAN_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SSS-RainFlagged_SMID_28DAY-RUNNINGMEAN_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image Descending 28-Day Running Mean Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SSS_RAINFLAGGED_SMID_7DAY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SSS-RainFlagged_SMID_7DAY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SSS-RainFlagged_SMID_7DAY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image Descending 7-Day Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SSS_RAINFLAGGED_SMID_ANNUAL_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SSS-RainFlagged_SMID_ANNUAL_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SSS-RainFlagged_SMID_ANNUAL_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image Descending Annual Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SSS_RAINFLAGGED_SMID_DAILY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SSS-RainFlagged_SMID_DAILY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SSS-RainFlagged_SMID_DAILY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image Descending Daily Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SSS_RAINFLAGGED_SMID_CUMULATIVE_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SSS-RainFlagged_SMID_CUMULATIVE_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SSS-RainFlagged_SMID_CUMULATIVE_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image Descending Mission Cumulative Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SSS_RAINFLAGGED_SMID_MONTHLY_CLIMATOLOGY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SSS-RainFlagged_SMID_MONTHLY-CLIMATOLOGY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SSS-RainFlagged_SMID_MONTHLY-CLIMATOLOGY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image Descending Monthly Climatology Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SSS_RAINFLAGGED_SMID_MONTHLY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SSS-RainFlagged_SMID_MONTHLY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SSS-RainFlagged_SMID_MONTHLY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image Descending Monthly Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SSS_RAINFLAGGED_SMID_SEASONAL_CLIMATOLOGY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SSS-RainFlagged_SMID_SEASONAL-CLIMATOLOGY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SSS-RainFlagged_SMID_SEASONAL-CLIMATOLOGY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image Descending Seasonal Climatology Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SSS_RAINFLAGGED_SMID_3MONTH_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SSS-RainFlagged_SMID_3MONTH_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SSS-RainFlagged_SMID_3MONTH_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image Descending Seasonal Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SSS_RAINFLAGGED_SMI_CUMULATIVE_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SSS-RainFlagged_SMI_CUMULATIVE_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SSS-RainFlagged_SMI_CUMULATIVE_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image Mission Cumulative Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SSS_RAINFLAGGED_SMI_MONTHLY_CLIMATOLOGY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SSS-RainFlagged_SMI_MONTHLY-CLIMATOLOGY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SSS-RainFlagged_SMI_MONTHLY-CLIMATOLOGY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image Monthly Climatology Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SSS_RAINFLAGGED_SMI_MONTHLY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SSS-RainFlagged_SMI_MONTHLY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SSS-RainFlagged_SMI_MONTHLY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image Monthly Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SSS_RAINFLAGGED_SMI_SEASONAL_CLIMATOLOGY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SSS-RainFlagged_SMI_SEASONAL-CLIMATOLOGY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SSS-RainFlagged_SMI_SEASONAL-CLIMATOLOGY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image Seasonal Climatology Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SSS_RAINFLAGGED_SMI_3MONTH_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SSS-RainFlagged_SMI_3MONTH_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SSS-RainFlagged_SMI_3MONTH_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image Seasonal Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_DENSITY_SMI_28DAY_RUNNINGMEAN_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_DENSITY_SMI_28DAY-RUNNINGMEAN_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_DENSITY_SMI_28DAY-RUNNINGMEAN_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Density Standard Mapped Image 28-Day Running Mean Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_DENSITY_SMI_7DAY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_DENSITY_SMI_7DAY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_DENSITY_SMI_7DAY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Density Standard Mapped Image 7-Day Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_DENSITY_SMI_7DAY_RUNNINGMEAN_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_DENSITY_SMI_7DAY-RUNNINGMEAN_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_DENSITY_SMI_7DAY-RUNNINGMEAN_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Density Standard Mapped Image 7-Day Running Mean Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_DENSITY_SMI_ANNUAL_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_DENSITY_SMI_ANNUAL_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_DENSITY_SMI_ANNUAL_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Density Standard Mapped Image Annual Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_DENSITY_SMIA_28DAY_RUNNINGMEAN_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_DENSITY_SMIA_28DAY-RUNNINGMEAN_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_DENSITY_SMIA_28DAY-RUNNINGMEAN_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Density Standard Mapped Image Ascending 28-Day Running Mean Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_DENSITY_SMIA_7DAY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_DENSITY_SMIA_7DAY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_DENSITY_SMIA_7DAY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Density Standard Mapped Image Ascending 7-Day Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_DENSITY_SMIA_ANNUAL_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_DENSITY_SMIA_ANNUAL_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_DENSITY_SMIA_ANNUAL_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Density Standard Mapped Image Ascending Annual Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_DENSITY_SMIA_DAILY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_DENSITY_SMIA_DAILY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_DENSITY_SMIA_DAILY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Density Standard Mapped Image Ascending Daily Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_DENSITY_SMIA_CUMULATIVE_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_DENSITY_SMIA_CUMULATIVE_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_DENSITY_SMIA_CUMULATIVE_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Density Standard Mapped Image Ascending Mission Cumulative Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_DENSITY_SMIA_MONTHLY_CLIMATOLOGY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_DENSITY_SMIA_MONTHLY-CLIMATOLOGY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_DENSITY_SMIA_MONTHLY-CLIMATOLOGY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Density Standard Mapped Image Ascending Monthly Climatology Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_DENSITY_SMIA_MONTHLY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_DENSITY_SMIA_MONTHLY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_DENSITY_SMIA_MONTHLY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Density Standard Mapped Image Ascending Monthly Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_DENSITY_SMIA_SEASONAL_CLIMATOLOGY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_DENSITY_SMIA_SEASONAL-CLIMATOLOGY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_DENSITY_SMIA_SEASONAL-CLIMATOLOGY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Density Standard Mapped Image Ascending Seasonal Climatology Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_DENSITY_SMIA_3MONTH_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_DENSITY_SMIA_3MONTH_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_DENSITY_SMIA_3MONTH_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Density Standard Mapped Image Ascending Seasonal Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_DENSITY_SMI_DAILY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_DENSITY_SMI_DAILY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_DENSITY_SMI_DAILY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Density Standard Mapped Image Daily Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_DENSITY_SMID_28DAY_RUNNINGMEAN_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_DENSITY_SMID_28DAY-RUNNINGMEAN_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_DENSITY_SMID_28DAY-RUNNINGMEAN_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Density Standard Mapped Image Descending 28-Day Running Mean Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_DENSITY_SMID_7DAY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_DENSITY_SMID_7DAY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_DENSITY_SMID_7DAY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Density Standard Mapped Image Descending 7-Day Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_DENSITY_SMID_ANNUAL_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_DENSITY_SMID_ANNUAL_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_DENSITY_SMID_ANNUAL_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Density Standard Mapped Image Descending Annual Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_DENSITY_SMID_DAILY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_DENSITY_SMID_DAILY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_DENSITY_SMID_DAILY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Density Standard Mapped Image Descending Daily Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_DENSITY_SMID_CUMULATIVE_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_DENSITY_SMID_CUMULATIVE_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_DENSITY_SMID_CUMULATIVE_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Density Standard Mapped Image Descending Mission Cumulative Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_DENSITY_SMID_MONTHLY_CLIMATOLOGY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_DENSITY_SMID_MONTHLY-CLIMATOLOGY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_DENSITY_SMID_MONTHLY-CLIMATOLOGY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Density Standard Mapped Image Descending Monthly Climatology Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_DENSITY_SMID_MONTHLY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_DENSITY_SMID_MONTHLY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_DENSITY_SMID_MONTHLY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Density Standard Mapped Image Descending Monthly Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_DENSITY_SMID_SEASONAL_CLIMATOLOGY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_DENSITY_SMID_SEASONAL-CLIMATOLOGY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_DENSITY_SMID_SEASONAL-CLIMATOLOGY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Density Standard Mapped Image Descending Seasonal Climatology Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_DENSITY_SMID_3MONTH_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_DENSITY_SMID_3MONTH_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_DENSITY_SMID_3MONTH_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Density Standard Mapped Image Descending Seasonal Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_DENSITY_SMI_CUMULATIVE_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_DENSITY_SMI_CUMULATIVE_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_DENSITY_SMI_CUMULATIVE_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Density Standard Mapped Image Mission Cumulative Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_DENSITY_SMI_MONTHLY_CLIMATOLOGY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_DENSITY_SMI_MONTHLY-CLIMATOLOGY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_DENSITY_SMI_MONTHLY-CLIMATOLOGY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Density Standard Mapped Image Monthly Climatology Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_DENSITY_SMI_MONTHLY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_DENSITY_SMI_MONTHLY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_DENSITY_SMI_MONTHLY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Density Standard Mapped Image Monthly Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_DENSITY_SMI_SEASONAL_CLIMATOLOGY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_DENSITY_SMI_SEASONAL-CLIMATOLOGY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_DENSITY_SMI_SEASONAL-CLIMATOLOGY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Density Standard Mapped Image Seasonal Climatology Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_DENSITY_SMI_3MONTH_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_DENSITY_SMI_3MONTH_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_DENSITY_SMI_3MONTH_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Density Standard Mapped Image Seasonal Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SSS_SM_SMIA_MONTHLY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SSS_SM_SMIA_MONTHLY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SSS_SM_SMIA_MONTHLY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Salinity Smoothed Standard Mapped Image Ascending Monthly Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SSS_SM_SMID_MONTHLY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SSS_SM_SMID_MONTHLY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SSS_SM_SMID_MONTHLY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Salinity Smoothed Standard Mapped Image Descending Monthly Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SSS_SM_SMI_MONTHLY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SSS_SM_SMI_MONTHLY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SSS_SM_SMI_MONTHLY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Salinity Smoothed Standard Mapped Image Monthly Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SSS_SMI_28DAY_RUNNINGMEAN_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SSS_SMI_28DAY-RUNNINGMEAN_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SSS_SMI_28DAY-RUNNINGMEAN_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Salinity Standard Mapped Image 28-Day Running Mean Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SSS_SMI_7DAY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SSS_SMI_7DAY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SSS_SMI_7DAY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Salinity Standard Mapped Image 7-Day Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SSS_SMI_7DAY_RUNNINGMEAN_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SSS_SMI_7DAY-RUNNINGMEAN_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SSS_SMI_7DAY-RUNNINGMEAN_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Salinity Standard Mapped Image 7-Day Running Mean Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SSS_SMI_ANNUAL_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SSS_SMI_ANNUAL_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SSS_SMI_ANNUAL_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Salinity Standard Mapped Image Annual Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SSS_SMIA_28DAY_RUNNINGMEAN_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SSS_SMIA_28DAY-RUNNINGMEAN_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SSS_SMIA_28DAY-RUNNINGMEAN_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Salinity Standard Mapped Image Ascending 28-Day Running Mean Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SSS_SMIA_7DAY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SSS_SMIA_7DAY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SSS_SMIA_7DAY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Salinity Standard Mapped Image Ascending 7-Day Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SSS_SMIA_ANNUAL_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SSS_SMIA_ANNUAL_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SSS_SMIA_ANNUAL_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Salinity Standard Mapped Image Ascending Annual Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SSS_SMIA_DAILY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SSS_SMIA_DAILY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SSS_SMIA_DAILY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Salinity Standard Mapped Image Ascending Daily Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SSS_SMIA_CUMULATIVE_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SSS_SMIA_CUMULATIVE_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SSS_SMIA_CUMULATIVE_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Salinity Standard Mapped Image Ascending Mission Cumulative Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SSS_SMIA_MONTHLY_CLIMATOLOGY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SSS_SMIA_MONTHLY-CLIMATOLOGY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SSS_SMIA_MONTHLY-CLIMATOLOGY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Salinity Standard Mapped Image Ascending Monthly Climatology Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SSS_SMIA_MONTHLY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SSS_SMIA_MONTHLY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SSS_SMIA_MONTHLY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Salinity Standard Mapped Image Ascending Monthly Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SSS_SMIA_SEASONAL_CLIMATOLOGY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SSS_SMIA_SEASONAL-CLIMATOLOGY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SSS_SMIA_SEASONAL-CLIMATOLOGY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Salinity Standard Mapped Image Ascending Seasonal Climatology Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SSS_SMIA_3MONTH_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SSS_SMIA_3MONTH_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SSS_SMIA_3MONTH_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Salinity Standard Mapped Image Ascending Seasonal Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SSS_SMI_DAILY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SSS_SMI_DAILY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SSS_SMI_DAILY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Salinity Standard Mapped Image Daily Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SSS_SMID_28DAY_RUNNINGMEAN_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SSS_SMID_28DAY-RUNNINGMEAN_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SSS_SMID_28DAY-RUNNINGMEAN_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Salinity Standard Mapped Image Descending 28-Day Running Mean Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SSS_SMID_7DAY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SSS_SMID_7DAY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SSS_SMID_7DAY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Salinity Standard Mapped Image Descending 7-Day Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SSS_SMID_ANNUAL_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SSS_SMID_ANNUAL_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SSS_SMID_ANNUAL_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Salinity Standard Mapped Image Descending Annual Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SSS_SMID_DAILY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SSS_SMID_DAILY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SSS_SMID_DAILY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Salinity Standard Mapped Image Descending Daily Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SSS_SMID_CUMULATIVE_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SSS_SMID_CUMULATIVE_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SSS_SMID_CUMULATIVE_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Salinity Standard Mapped Image Descending Mission Cumulative Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SSS_SMID_MONTHLY_CLIMATOLOGY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SSS_SMID_MONTHLY-CLIMATOLOGY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SSS_SMID_MONTHLY-CLIMATOLOGY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Salinity Standard Mapped Image Descending Monthly Climatology Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SSS_SMID_MONTHLY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SSS_SMID_MONTHLY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SSS_SMID_MONTHLY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Salinity Standard Mapped Image Descending Monthly Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SSS_SMID_SEASONAL_CLIMATOLOGY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SSS_SMID_SEASONAL-CLIMATOLOGY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SSS_SMID_SEASONAL-CLIMATOLOGY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Salinity Standard Mapped Image Descending Seasonal Climatology Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SSS_SMID_3MONTH_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SSS_SMID_3MONTH_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SSS_SMID_3MONTH_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Salinity Standard Mapped Image Descending Seasonal Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SSS_SMI_CUMULATIVE_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SSS_SMI_CUMULATIVE_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SSS_SMI_CUMULATIVE_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Salinity Standard Mapped Image Mission Cumulative Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SSS_SMI_MONTHLY_CLIMATOLOGY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SSS_SMI_MONTHLY-CLIMATOLOGY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SSS_SMI_MONTHLY-CLIMATOLOGY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Salinity Standard Mapped Image Monthly Climatology Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SSS_SMI_MONTHLY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SSS_SMI_MONTHLY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SSS_SMI_MONTHLY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Salinity Standard Mapped Image Monthly Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SSS_SMI_SEASONAL_CLIMATOLOGY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SSS_SMI_SEASONAL-CLIMATOLOGY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SSS_SMI_SEASONAL-CLIMATOLOGY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Salinity Standard Mapped Image Seasonal Climatology Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SSS_SMI_3MONTH_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SSS_SMI_3MONTH_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SSS_SMI_3MONTH_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Salinity Standard Mapped Image Seasonal Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SPICINESS_SMI_28DAY_RUNNINGMEAN_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SPICINESS_SMI_28DAY-RUNNINGMEAN_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SPICINESS_SMI_28DAY-RUNNINGMEAN_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Spiciness Standard Mapped Image 28-Day Running Mean Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SPICINESS_SMI_7DAY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SPICINESS_SMI_7DAY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SPICINESS_SMI_7DAY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Spiciness Standard Mapped Image 7-Day Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SPICINESS_SMI_7DAY_RUNNINGMEAN_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SPICINESS_SMI_7DAY-RUNNINGMEAN_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SPICINESS_SMI_7DAY-RUNNINGMEAN_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Spiciness Standard Mapped Image 7-Day Running Mean Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SPICINESS_SMI_ANNUAL_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SPICINESS_SMI_ANNUAL_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SPICINESS_SMI_ANNUAL_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Spiciness Standard Mapped Image Annual Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SPICINESS_SMIA_28DAY_RUNNINGMEAN_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SPICINESS_SMIA_28DAY-RUNNINGMEAN_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SPICINESS_SMIA_28DAY-RUNNINGMEAN_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Spiciness Standard Mapped Image Ascending 28-Day Running Mean Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SPICINESS_SMIA_7DAY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SPICINESS_SMIA_7DAY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SPICINESS_SMIA_7DAY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Spiciness Standard Mapped Image Ascending 7-Day Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SPICINESS_SMIA_ANNUAL_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SPICINESS_SMIA_ANNUAL_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SPICINESS_SMIA_ANNUAL_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Spiciness Standard Mapped Image Ascending Annual Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SPICINESS_SMIA_DAILY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SPICINESS_SMIA_DAILY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SPICINESS_SMIA_DAILY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Spiciness Standard Mapped Image Ascending Daily Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SPICINESS_SMIA_CUMULATIVE_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SPICINESS_SMIA_CUMULATIVE_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SPICINESS_SMIA_CUMULATIVE_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Spiciness Standard Mapped Image Ascending Mission Cumulative Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SPICINESS_SMIA_MONTHLY_CLIMATOLOGY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SPICINESS_SMIA_MONTHLY-CLIMATOLOGY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SPICINESS_SMIA_MONTHLY-CLIMATOLOGY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Spiciness Standard Mapped Image Ascending Monthly Climatology Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SPICINESS_SMIA_MONTHLY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SPICINESS_SMIA_MONTHLY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SPICINESS_SMIA_MONTHLY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Spiciness Standard Mapped Image Ascending Monthly Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SPICINESS_SMIA_SEASONAL_CLIMATOLOGY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SPICINESS_SMIA_SEASONAL-CLIMATOLOGY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SPICINESS_SMIA_SEASONAL-CLIMATOLOGY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Spiciness Standard Mapped Image Ascending Seasonal Climatology Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SPICINESS_SMIA_3MONTH_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SPICINESS_SMIA_3MONTH_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SPICINESS_SMIA_3MONTH_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Spiciness Standard Mapped Image Ascending Seasonal Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SPICINESS_SMI_DAILY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SPICINESS_SMI_DAILY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SPICINESS_SMI_DAILY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Spiciness Standard Mapped Image Daily Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SPICINESS_SMID_28DAY_RUNNINGMEAN_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SPICINESS_SMID_28DAY-RUNNINGMEAN_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SPICINESS_SMID_28DAY-RUNNINGMEAN_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Spiciness Standard Mapped Image Descending 28-Day Running Mean Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SPICINESS_SMID_7DAY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SPICINESS_SMID_7DAY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SPICINESS_SMID_7DAY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Spiciness Standard Mapped Image Descending 7-Day Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SPICINESS_SMID_ANNUAL_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SPICINESS_SMID_ANNUAL_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SPICINESS_SMID_ANNUAL_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Spiciness Standard Mapped Image Descending Annual Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SPICINESS_SMID_DAILY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SPICINESS_SMID_DAILY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SPICINESS_SMID_DAILY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Spiciness Standard Mapped Image Descending Daily Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SPICINESS_SMID_CUMULATIVE_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SPICINESS_SMID_CUMULATIVE_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SPICINESS_SMID_CUMULATIVE_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Spiciness Standard Mapped Image Descending Mission Cumulative Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SPICINESS_SMID_MONTHLY_CLIMATOLOGY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SPICINESS_SMID_MONTHLY-CLIMATOLOGY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SPICINESS_SMID_MONTHLY-CLIMATOLOGY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Spiciness Standard Mapped Image Descending Monthly Climatology Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SPICINESS_SMID_MONTHLY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SPICINESS_SMID_MONTHLY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SPICINESS_SMID_MONTHLY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Spiciness Standard Mapped Image Descending Monthly Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SPICINESS_SMID_SEASONAL_CLIMATOLOGY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SPICINESS_SMID_SEASONAL-CLIMATOLOGY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SPICINESS_SMID_SEASONAL-CLIMATOLOGY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Spiciness Standard Mapped Image Descending Seasonal Climatology Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SPICINESS_SMID_3MONTH_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SPICINESS_SMID_3MONTH_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SPICINESS_SMID_3MONTH_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Spiciness Standard Mapped Image Descending Seasonal Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SPICINESS_SMI_CUMULATIVE_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SPICINESS_SMI_CUMULATIVE_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SPICINESS_SMI_CUMULATIVE_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Spiciness Standard Mapped Image Mission Cumulative Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SPICINESS_SMI_MONTHLY_CLIMATOLOGY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SPICINESS_SMI_MONTHLY-CLIMATOLOGY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SPICINESS_SMI_MONTHLY-CLIMATOLOGY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Spiciness Standard Mapped Image Monthly Climatology Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SPICINESS_SMI_MONTHLY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SPICINESS_SMI_MONTHLY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SPICINESS_SMI_MONTHLY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Spiciness Standard Mapped Image Monthly Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SPICINESS_SMI_SEASONAL_CLIMATOLOGY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SPICINESS_SMI_SEASONAL-CLIMATOLOGY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SPICINESS_SMI_SEASONAL-CLIMATOLOGY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Spiciness Standard Mapped Image Seasonal Climatology Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_SPICINESS_SMI_3MONTH_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_SPICINESS_SMI_3MONTH_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_SPICINESS_SMI_3MONTH_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Sea Surface Spiciness Standard Mapped Image Seasonal Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_WIND_SPEED_SMI_28DAY_RUNNINGMEAN_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_WIND_SPEED_SMI_28DAY-RUNNINGMEAN_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_WIND_SPEED_SMI_28DAY-RUNNINGMEAN_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Wind Speed Standard Mapped Image 28-Day Running Mean Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_WIND_SPEED_SMI_7DAY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_WIND_SPEED_SMI_7DAY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_WIND_SPEED_SMI_7DAY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Wind Speed Standard Mapped Image 7-Day Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_WIND_SPEED_SMI_7DAY_RUNNINGMEAN_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_WIND_SPEED_SMI_7DAY-RUNNINGMEAN_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_WIND_SPEED_SMI_7DAY-RUNNINGMEAN_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Wind Speed Standard Mapped Image 7-Day Running Mean Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_WIND_SPEED_SMI_ANNUAL_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_WIND_SPEED_SMI_ANNUAL_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_WIND_SPEED_SMI_ANNUAL_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Wind Speed Standard Mapped Image Annual Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_WIND_SPEED_SMIA_28DAY_RUNNINGMEAN_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_WIND_SPEED_SMIA_28DAY-RUNNINGMEAN_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_WIND_SPEED_SMIA_28DAY-RUNNINGMEAN_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Wind Speed Standard Mapped Image Ascending 28-Day Running Mean Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_WIND_SPEED_SMIA_7DAY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_WIND_SPEED_SMIA_7DAY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_WIND_SPEED_SMIA_7DAY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Wind Speed Standard Mapped Image Ascending 7-Day Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_WIND_SPEED_SMIA_ANNUAL_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_WIND_SPEED_SMIA_ANNUAL_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_WIND_SPEED_SMIA_ANNUAL_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Wind Speed Standard Mapped Image Ascending Annual Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_WIND_SPEED_SMIA_DAILY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_WIND_SPEED_SMIA_DAILY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_WIND_SPEED_SMIA_DAILY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Wind Speed Standard Mapped Image Ascending Daily Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_WIND_SPEED_SMIA_CUMULATIVE_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_WIND_SPEED_SMIA_CUMULATIVE_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_WIND_SPEED_SMIA_CUMULATIVE_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Wind Speed Standard Mapped Image Ascending Mission Cumulative Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_WIND_SPEED_SMIA_MONTHLY_CLIMATOLOGY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_WIND_SPEED_SMIA_MONTHLY-CLIMATOLOGY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_WIND_SPEED_SMIA_MONTHLY-CLIMATOLOGY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Wind Speed Standard Mapped Image Ascending Monthly Climatology Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_WIND_SPEED_SMIA_MONTHLY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_WIND_SPEED_SMIA_MONTHLY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_WIND_SPEED_SMIA_MONTHLY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Wind Speed Standard Mapped Image Ascending Monthly Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_WIND_SPEED_SMIA_SEASONAL_CLIMATOLOGY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_WIND_SPEED_SMIA_SEASONAL-CLIMATOLOGY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_WIND_SPEED_SMIA_SEASONAL-CLIMATOLOGY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Wind Speed Standard Mapped Image Ascending Seasonal Climatology Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_WIND_SPEED_SMIA_3MONTH_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_WIND_SPEED_SMIA_3MONTH_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_WIND_SPEED_SMIA_3MONTH_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Wind Speed Standard Mapped Image Ascending Seasonal Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_WIND_SPEED_SMI_DAILY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_WIND_SPEED_SMI_DAILY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_WIND_SPEED_SMI_DAILY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Wind Speed Standard Mapped Image Daily Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_WIND_SPEED_SMID_28DAY_RUNNINGMEAN_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_WIND_SPEED_SMID_28DAY-RUNNINGMEAN_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_WIND_SPEED_SMID_28DAY-RUNNINGMEAN_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Wind Speed Standard Mapped Image Descending 28-Day Running Mean Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_WIND_SPEED_SMID_7DAY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_WIND_SPEED_SMID_7DAY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_WIND_SPEED_SMID_7DAY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Wind Speed Standard Mapped Image Descending 7-Day Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_WIND_SPEED_SMID_ANNUAL_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_WIND_SPEED_SMID_ANNUAL_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_WIND_SPEED_SMID_ANNUAL_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Wind Speed Standard Mapped Image Descending Annual Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_WIND_SPEED_SMID_DAILY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_WIND_SPEED_SMID_DAILY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_WIND_SPEED_SMID_DAILY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Wind Speed Standard Mapped Image Descending Daily Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_WIND_SPEED_SMID_CUMULATIVE_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_WIND_SPEED_SMID_CUMULATIVE_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_WIND_SPEED_SMID_CUMULATIVE_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Wind Speed Standard Mapped Image Descending Mission Cumulative Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_WIND_SPEED_SMID_MONTHLY_CLIMATOLOGY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_WIND_SPEED_SMID_MONTHLY-CLIMATOLOGY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_WIND_SPEED_SMID_MONTHLY-CLIMATOLOGY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Wind Speed Standard Mapped Image Descending Monthly Climatology Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_WIND_SPEED_SMID_MONTHLY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_WIND_SPEED_SMID_MONTHLY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_WIND_SPEED_SMID_MONTHLY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Wind Speed Standard Mapped Image Descending Monthly Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_WIND_SPEED_SMID_SEASONAL_CLIMATOLOGY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_WIND_SPEED_SMID_SEASONAL-CLIMATOLOGY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_WIND_SPEED_SMID_SEASONAL-CLIMATOLOGY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Wind Speed Standard Mapped Image Descending Seasonal Climatology Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_WIND_SPEED_SMID_3MONTH_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_WIND_SPEED_SMID_3MONTH_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_WIND_SPEED_SMID_3MONTH_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Wind Speed Standard Mapped Image Descending Seasonal Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_WIND_SPEED_SMI_CUMULATIVE_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_WIND_SPEED_SMI_CUMULATIVE_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_WIND_SPEED_SMI_CUMULATIVE_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Wind Speed Standard Mapped Image Mission Cumulative V5.0 version: 5.0"
        )

    AQUARIUS_L3_WIND_SPEED_SMI_MONTHLY_CLIMATOLOGY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_WIND_SPEED_SMI_MONTHLY-CLIMATOLOGY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_WIND_SPEED_SMI_MONTHLY-CLIMATOLOGY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Wind Speed Standard Mapped Image Monthly Climatology Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_WIND_SPEED_SMI_MONTHLY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_WIND_SPEED_SMI_MONTHLY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_WIND_SPEED_SMI_MONTHLY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Wind Speed Standard Mapped Image Monthly Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_WIND_SPEED_SMI_SEASONAL_CLIMATOLOGY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_WIND_SPEED_SMI_SEASONAL-CLIMATOLOGY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_WIND_SPEED_SMI_SEASONAL-CLIMATOLOGY_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Wind Speed Standard Mapped Image Seasonal Climatology Data V5.0 version: 5.0"
        )

    AQUARIUS_L3_WIND_SPEED_SMI_3MONTH_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L3_WIND_SPEED_SMI_3MONTH_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L3_WIND_SPEED_SMI_3MONTH_V5",
            version="5.0",
            description="Aquarius Official Release Level 3 Wind Speed Standard Mapped Image Seasonal Data V5.0 version: 5.0"
        )

    AQUARIUS_ANCILLARY_RFI_V1_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_ANCILLARY_RFI_V1_1",
            provider="POCLOUD", 
            shortname="AQUARIUS_ANCILLARY_RFI_V1",
            version="1",
            description="Aquarius Radio Frequency Interference (RFI) Ancillary Dataset V1.0 version: 1"
        )

    SPURS1_ARGO_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SPURS1_ARGO_1.0",
            provider="POCLOUD", 
            shortname="SPURS1_ARGO",
            version="1.0",
            description="Argo float CTD profile data within the scope of the SPURS-1 N. Atlantic field campaign version: 1.0"
        )

    MITGCM_LLC4320_PRE_SWOT_JPL_L4_BASSSTRAIT_V10_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_MITgcm_LLC4320_Pre-SWOT_JPL_L4_BassStrait_v1.0_1.0",
            provider="POCLOUD", 
            shortname="MITgcm_LLC4320_Pre-SWOT_JPL_L4_BassStrait_v1.0",
            version="1.0",
            description="Bass Strait Pre-SWOT Level-4 Hourly MITgcm LLC4320 Native Grid 2km Oceanographic Dataset Version 1.0 version: 1.0"
        )

    OISST_HR_NRT_GOS_L4_BLK_V20_V20_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_OISST_HR_NRT-GOS-L4-BLK-v2.0_2.0",
            provider="POCLOUD", 
            shortname="OISST_HR_NRT-GOS-L4-BLK-v2.0",
            version="2.0",
            description="Black Sea High Resolution SST L4 Analysis 0.0625 deg Resolution version: 2.0"
        )

    OISST_UHR_NRT_GOS_L4_BLK_V20_V20_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_OISST_UHR_NRT-GOS-L4-BLK-v2.0_2.0",
            provider="POCLOUD", 
            shortname="OISST_UHR_NRT-GOS-L4-BLK-v2.0",
            version="2.0",
            description="Black Sea Ultra High Resolution SST L4 Analysis 0.01 deg Resolution version: 2.0"
        )

    MITGCM_LLC4320_PRE_SWOT_JPL_L4_BOKNIS_V10_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_MITgcm_LLC4320_Pre-SWOT_JPL_L4_Boknis_v1.0_1.0",
            provider="POCLOUD", 
            shortname="MITgcm_LLC4320_Pre-SWOT_JPL_L4_Boknis_v1.0",
            version="1.0",
            description="Boknis Pre-SWOT Level-4 Hourly MITgcm LLC4320 Native Grid 2km Oceanographic Dataset Version 1.0 version: 1.0"
        )

    COWVR_STPH8_L1_TSDR_V100_V100_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_COWVR_STPH8_L1_TSDR_V10.0_10.0",
            provider="POCLOUD", 
            shortname="COWVR_STPH8_L1_TSDR_V10.0",
            version="10.0",
            description="COWVR STP-H8 Antenna and Microwave Brightness Temperatures Version 10.0 version: 10.0"
        )

    COWVR_STPH8_L2_EDR_V100_V100_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_COWVR_STPH8_L2_EDR_V10.0_10.0",
            provider="POCLOUD", 
            shortname="COWVR_STPH8_L2_EDR_V10.0",
            version="10.0",
            description="COWVR STP-H8 Surface Wind Vector and Column-Integrated Atmospheric Water Measurements Version 10.0 version: 10.0"
        )

    TELLUS_GRAC_L3_CSR_RL06_LND_V04_VRL06V04_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_TELLUS_GRAC_L3_CSR_RL06_LND_v04_RL06v04",
            provider="POCLOUD", 
            shortname="TELLUS_GRAC_L3_CSR_RL06_LND_v04",
            version="RL06v04",
            description="CSR TELLUS GRACE Level-3 Monthly Land Water-Equivalent-Thickness Surface Mass Anomaly Release 6.0 version 04 version: RL06v04"
        )

    TELLUS_GRAC_L3_CSR_RL06_OCN_V04_VRL06V04_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_TELLUS_GRAC_L3_CSR_RL06_OCN_v04_RL06v04",
            provider="POCLOUD", 
            shortname="TELLUS_GRAC_L3_CSR_RL06_OCN_v04",
            version="RL06v04",
            description="CSR TELLUS GRACE Level-3 Monthly Ocean Bottom Pressure Anomaly Release 6.0 version 04 version: RL06v04"
        )

    TELLUS_GRFO_L3_CSR_RL063_LND_V04_VRL063V04_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_TELLUS_GRFO_L3_CSR_RL06.3_LND_v04_RL06.3v04",
            provider="POCLOUD", 
            shortname="TELLUS_GRFO_L3_CSR_RL06.3_LND_v04",
            version="RL06.3v04",
            description="CSR TELLUS GRACE-FO Level-3 Monthly Land Water-Equivalent-Thickness Surface Mass Anomaly Release 6.3 version 04 version: RL06.3v04"
        )

    TELLUS_GRFO_L3_CSR_RL063_OCN_V04_VRL063V04_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_TELLUS_GRFO_L3_CSR_RL06.3_OCN_v04_RL06.3v04",
            provider="POCLOUD", 
            shortname="TELLUS_GRFO_L3_CSR_RL06.3_OCN_v04",
            version="RL06.3v04",
            description="CSR TELLUS GRACE-FO Level-3 Monthly Ocean Bottom Pressure Anomaly Release 6.3 version 04 version: RL06.3v04"
        )

    CYGNSS_L3_MICROPLASTIC_V10_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_CYGNSS_L3_MICROPLASTIC_V1.0_1.0",
            provider="POCLOUD", 
            shortname="CYGNSS_L3_MICROPLASTIC_V1.0",
            version="1.0",
            description="CYGNSS L3 Ocean Microplastic Concentration V1.0 version: 1.0"
        )

    CYGNSS_L1_CAL_RAW_IF_V10_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_CYGNSS_L1_CAL_RAW_IF_V1.0_1.0",
            provider="POCLOUD", 
            shortname="CYGNSS_L1_CAL_RAW_IF_V1.0",
            version="1.0",
            description="CYGNSS Level 1 Calibrated Raw IF Version 1.0 version: 1.0"
        )

    CYGNSS_L1_CDR_V10_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_CYGNSS_L1_CDR_V1.0_1.0",
            provider="POCLOUD", 
            shortname="CYGNSS_L1_CDR_V1.0",
            version="1.0",
            description="CYGNSS Level 1 Climate Data Record Version 1.0 version: 1.0"
        )

    CYGNSS_L1_CDR_V11_V11_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_CYGNSS_L1_CDR_V1.1_1.1",
            provider="POCLOUD", 
            shortname="CYGNSS_L1_CDR_V1.1",
            version="1.1",
            description="CYGNSS Level 1 Climate Data Record Version 1.1 version: 1.1"
        )

    CYGNSS_L1_CDR_V12_V12_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_CYGNSS_L1_CDR_V1.2_1.2",
            provider="POCLOUD", 
            shortname="CYGNSS_L1_CDR_V1.2",
            version="1.2",
            description="CYGNSS Level 1 Climate Data Record Version 1.2 version: 1.2"
        )

    CYGNSS_L1_FULL_DDM_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_CYGNSS_L1_FULL_DDM_1.0",
            provider="POCLOUD", 
            shortname="CYGNSS_L1_FULL_DDM",
            version="1.0",
            description="CYGNSS Level 1 Full Delay Doppler Map Data Record version: 1.0"
        )

    CYGNSS_L1_FULL_DDM_V30_V30_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_CYGNSS_L1_FULL_DDM_V3.0_3.0",
            provider="POCLOUD", 
            shortname="CYGNSS_L1_FULL_DDM_V3.0",
            version="3.0",
            description="CYGNSS Level 1 Full Delay Doppler Map Data Record Version 3.0 version: 3.0"
        )

    CYGNSS_L1_RAW_IF_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_CYGNSS_L1_RAW_IF_1.0",
            provider="POCLOUD", 
            shortname="CYGNSS_L1_RAW_IF",
            version="1.0",
            description="CYGNSS Level 1 Raw Intermediate Frequency Data Record version: 1.0"
        )

    CYGNSS_L1_V21_V21_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_CYGNSS_L1_V2.1_2.1",
            provider="POCLOUD", 
            shortname="CYGNSS_L1_V2.1",
            version="2.1",
            description="CYGNSS Level 1 Science Data Record Version 2.1 version: 2.1"
        )

    CYGNSS_L1_V30_V30_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_CYGNSS_L1_V3.0_3.0",
            provider="POCLOUD", 
            shortname="CYGNSS_L1_V3.0",
            version="3.0",
            description="CYGNSS Level 1 Science Data Record Version 3.0 version: 3.0"
        )

    CYGNSS_L1_V31_V31_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_CYGNSS_L1_V3.1_3.1",
            provider="POCLOUD", 
            shortname="CYGNSS_L1_V3.1",
            version="3.1",
            description="CYGNSS Level 1 Science Data Record Version 3.1 version: 3.1"
        )

    CYGNSS_L1_V32_V32_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_CYGNSS_L1_V3.2_3.2",
            provider="POCLOUD", 
            shortname="CYGNSS_L1_V3.2",
            version="3.2",
            description="CYGNSS Level 1 Science Data Record Version 3.2 version: 3.2"
        )

    CYGNSS_L2_CDR_V10_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_CYGNSS_L2_CDR_V1.0_1.0",
            provider="POCLOUD", 
            shortname="CYGNSS_L2_CDR_V1.0",
            version="1.0",
            description="CYGNSS Level 2 Climate Data Record Version 1.0 version: 1.0"
        )

    CYGNSS_L2_CDR_V11_V11_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_CYGNSS_L2_CDR_V1.1_1.1",
            provider="POCLOUD", 
            shortname="CYGNSS_L2_CDR_V1.1",
            version="1.1",
            description="CYGNSS Level 2 Climate Data Record Version 1.1 version: 1.1"
        )

    CYGNSS_L2_CDR_V12_V12_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_CYGNSS_L2_CDR_V1.2_1.2",
            provider="POCLOUD", 
            shortname="CYGNSS_L2_CDR_V1.2",
            version="1.2",
            description="CYGNSS Level 2 Climate Data Record Version 1.2 version: 1.2"
        )

    CYGNSS_L2_SURFACE_FLUX_CDR_V10_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_CYGNSS_L2_SURFACE_FLUX_CDR_V1.0_1.0",
            provider="POCLOUD", 
            shortname="CYGNSS_L2_SURFACE_FLUX_CDR_V1.0",
            version="1.0",
            description="CYGNSS Level 2 Ocean Surface Heat Flux Climate Data Record Version 1.0 version: 1.0"
        )

    CYGNSS_L2_SURFACE_FLUX_CDR_V11_V11_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_CYGNSS_L2_SURFACE_FLUX_CDR_V1.1_1.1",
            provider="POCLOUD", 
            shortname="CYGNSS_L2_SURFACE_FLUX_CDR_V1.1",
            version="1.1",
            description="CYGNSS Level 2 Ocean Surface Heat Flux Climate Data Record Version 1.1 version: 1.1"
        )

    CYGNSS_L2_SURFACE_FLUX_CDR_V12_V12_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_CYGNSS_L2_SURFACE_FLUX_CDR_V1.2_1.2",
            provider="POCLOUD", 
            shortname="CYGNSS_L2_SURFACE_FLUX_CDR_V1.2",
            version="1.2",
            description="CYGNSS Level 2 Ocean Surface Heat Flux Climate Data Record Version 1.2 version: 1.2"
        )

    CYGNSS_L2_SURFACE_FLUX_V10_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_CYGNSS_L2_SURFACE_FLUX_V1.0_1.0",
            provider="POCLOUD", 
            shortname="CYGNSS_L2_SURFACE_FLUX_V1.0",
            version="1.0",
            description="CYGNSS Level 2 Ocean Surface Heat Flux Science Data Record Version 1.0 version: 1.0"
        )

    CYGNSS_L2_SURFACE_FLUX_V20_V20_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_CYGNSS_L2_SURFACE_FLUX_V2.0_2.0",
            provider="POCLOUD", 
            shortname="CYGNSS_L2_SURFACE_FLUX_V2.0",
            version="2.0",
            description="CYGNSS Level 2 Ocean Surface Heat Flux Science Data Record Version 2.0 version: 2.0"
        )

    CYGNSS_L2_SURFACE_FLUX_V32_V32_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_CYGNSS_L2_SURFACE_FLUX_V3.2_3.2",
            provider="POCLOUD", 
            shortname="CYGNSS_L2_SURFACE_FLUX_V3.2",
            version="3.2",
            description="CYGNSS Level 2 Ocean Surface Heat Flux Science Data Record Version 3.2 version: 3.2"
        )

    CYGNSS_L2_V21_V21_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_CYGNSS_L2_V2.1_2.1",
            provider="POCLOUD", 
            shortname="CYGNSS_L2_V2.1",
            version="2.1",
            description="CYGNSS Level 2 Science Data Record Version 2.1 version: 2.1"
        )

    CYGNSS_L2_V30_V30_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_CYGNSS_L2_V3.0_3.0",
            provider="POCLOUD", 
            shortname="CYGNSS_L2_V3.0",
            version="3.0",
            description="CYGNSS Level 2 Science Data Record Version 3.0 version: 3.0"
        )

    CYGNSS_L2_V31_V31_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_CYGNSS_L2_V3.1_3.1",
            provider="POCLOUD", 
            shortname="CYGNSS_L2_V3.1",
            version="3.1",
            description="CYGNSS Level 2 Science Data Record Version 3.1 version: 3.1"
        )

    CYGNSS_L2_V32_V32_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_CYGNSS_L2_V3.2_3.2",
            provider="POCLOUD", 
            shortname="CYGNSS_L2_V3.2",
            version="3.2",
            description="CYGNSS Level 2 Science Data Record Version 3.2 version: 3.2"
        )

    CYGNSS_L3_CDR_V10_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_CYGNSS_L3_CDR_V1.0_1.0",
            provider="POCLOUD", 
            shortname="CYGNSS_L3_CDR_V1.0",
            version="1.0",
            description="CYGNSS Level 3 Climate Data Record Version 1.0 version: 1.0"
        )

    CYGNSS_L3_CDR_V11_V11_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_CYGNSS_L3_CDR_V1.1_1.1",
            provider="POCLOUD", 
            shortname="CYGNSS_L3_CDR_V1.1",
            version="1.1",
            description="CYGNSS Level 3 Climate Data Record Version 1.1 version: 1.1"
        )

    CYGNSS_L3_CDR_V12_V12_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_CYGNSS_L3_CDR_V1.2_1.2",
            provider="POCLOUD", 
            shortname="CYGNSS_L3_CDR_V1.2",
            version="1.2",
            description="CYGNSS Level 3 Climate Data Record Version 1.2 version: 1.2"
        )

    CYGNSS_L3_MRG_NRT_V32_V32_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_CYGNSS_L3_MRG_NRT_V3.2_3.2",
            provider="POCLOUD", 
            shortname="CYGNSS_L3_MRG_NRT_V3.2",
            version="3.2",
            description="CYGNSS Level 3 MRG Science Data Record Near Real Time Version 3.2 version: 3.2"
        )

    CYGNSS_L3_MRG_NRT_V321_V321_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_CYGNSS_L3_MRG_NRT_V3.2.1_3.2.1",
            provider="POCLOUD", 
            shortname="CYGNSS_L3_MRG_NRT_V3.2.1",
            version="3.2.1",
            description="CYGNSS Level 3 MRG Science Data Record Near Real Time Version 3.2.1 version: 3.2.1"
        )

    CYGNSS_L3_MRG_V32_V32_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_CYGNSS_L3_MRG_V3.2_3.2",
            provider="POCLOUD", 
            shortname="CYGNSS_L3_MRG_V3.2",
            version="3.2",
            description="CYGNSS Level 3 MRG Science Data Record Version 3.2 version: 3.2"
        )

    CYGNSS_L3_MRG_V321_V321_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_CYGNSS_L3_MRG_V3.2.1_3.2.1",
            provider="POCLOUD", 
            shortname="CYGNSS_L3_MRG_V3.2.1",
            version="3.2.1",
            description="CYGNSS Level 3 MRG Science Data Record Version 3.2.1 version: 3.2.1"
        )

    CYGNSS_L3_MICROPLASTIC_V32_V32_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_CYGNSS_L3_MICROPLASTIC_V3.2_3.2",
            provider="POCLOUD", 
            shortname="CYGNSS_L3_MICROPLASTIC_V3.2",
            version="3.2",
            description="CYGNSS Level 3 Ocean Microplastic Concentration Version 3.2 version: 3.2"
        )

    CYGNSS_L3_V21_V21_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_CYGNSS_L3_V2.1_2.1",
            provider="POCLOUD", 
            shortname="CYGNSS_L3_V2.1",
            version="2.1",
            description="CYGNSS Level 3 Science Data Record Version 2.1 version: 2.1"
        )

    CYGNSS_L3_V30_V30_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_CYGNSS_L3_V3.0_3.0",
            provider="POCLOUD", 
            shortname="CYGNSS_L3_V3.0",
            version="3.0",
            description="CYGNSS Level 3 Science Data Record Version 3.0 version: 3.0"
        )

    CYGNSS_L3_V31_V31_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_CYGNSS_L3_V3.1_3.1",
            provider="POCLOUD", 
            shortname="CYGNSS_L3_V3.1",
            version="3.1",
            description="CYGNSS Level 3 Science Data Record Version 3.1 version: 3.1"
        )

    CYGNSS_L3_V32_V32_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_CYGNSS_L3_V3.2_3.2",
            provider="POCLOUD", 
            shortname="CYGNSS_L3_V3.2",
            version="3.2",
            description="CYGNSS Level 3 Science Data Record Version 3.2 version: 3.2"
        )

    CYGNSS_L3_SOIL_MOISTURE_V32_V32_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_CYGNSS_L3_SOIL_MOISTURE_V3.2_3.2",
            provider="POCLOUD", 
            shortname="CYGNSS_L3_SOIL_MOISTURE_V3.2",
            version="3.2",
            description="CYGNSS Level 3 Soil Moisture Version 3.2 version: 3.2"
        )

    CYGNSS_L3_S10_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_CYGNSS_L3_S1.0_1.0",
            provider="POCLOUD", 
            shortname="CYGNSS_L3_S1.0",
            version="1.0",
            description="CYGNSS Level 3 Storm Centric Grid Science Data Record Version 1.0 version: 1.0"
        )

    MITGCM_LLC4320_PRE_SWOT_JPL_L4_CAPEBASIN_V10_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_MITgcm_LLC4320_Pre-SWOT_JPL_L4_CapeBasin_v1.0_1.0",
            provider="POCLOUD", 
            shortname="MITgcm_LLC4320_Pre-SWOT_JPL_L4_CapeBasin_v1.0",
            version="1.0",
            description="Cape Basin Pre-SWOT Level-4 Hourly MITgcm LLC4320 Native Grid 2km Oceanographic Dataset Version 1.0 version: 1.0"
        )

    NEUROST_SSH_SST_L4_V20240_V20240_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_NEUROST_SSH-SST_L4_V2024.0_2024.0",
            provider="POCLOUD", 
            shortname="NEUROST_SSH-SST_L4_V2024.0",
            version="2024.0",
            description="Daily NeurOST L4 Sea Surface Height and Surface Geostrophic Currents version: 2024.0"
        )

    SPURS1_DRIFTER_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SPURS1_DRIFTER_1.0",
            provider="POCLOUD", 
            shortname="SPURS1_DRIFTER",
            version="1.0",
            description="Drifter data for the SPURS-1 N. Atlantic field campaign version: 1.0"
        )

    ECCO_L4_ANCILLARY_DATA_V4R4_VV4R4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_ANCILLARY_DATA_V4R4_V4r4",
            provider="POCLOUD", 
            shortname="ECCO_L4_ANCILLARY_DATA_V4R4",
            version="V4r4",
            description="ECCO Ancillary Data (Version 4 Release 4) version: V4r4"
        )

    ECCO_L4_ATM_STATE_05DEG_DAILY_V4R4_VV4R4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_ATM_STATE_05DEG_DAILY_V4R4_V4r4",
            provider="POCLOUD", 
            shortname="ECCO_L4_ATM_STATE_05DEG_DAILY_V4R4",
            version="V4r4",
            description="ECCO Atmosphere Surface Temperature, Humidity, Wind, and Pressure - Daily Mean 0.5 Degree (Version 4 Release 4) version: V4r4"
        )

    ECCO_L4_ATM_STATE_LLC0090GRID_DAILY_V4R4_VV4R4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_ATM_STATE_LLC0090GRID_DAILY_V4R4_V4r4",
            provider="POCLOUD", 
            shortname="ECCO_L4_ATM_STATE_LLC0090GRID_DAILY_V4R4",
            version="V4r4",
            description="ECCO Atmosphere Surface Temperature, Humidity, Wind, and Pressure - Daily Mean llc90 Grid (Version 4 Release 4) version: V4r4"
        )

    ECCO_L4_ATM_STATE_05DEG_MONTHLY_V4R4_VV4R4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_ATM_STATE_05DEG_MONTHLY_V4R4_V4r4",
            provider="POCLOUD", 
            shortname="ECCO_L4_ATM_STATE_05DEG_MONTHLY_V4R4",
            version="V4r4",
            description="ECCO Atmosphere Surface Temperature, Humidity, Wind, and Pressure - Monthly Mean 0.5 Degree (Version 4 Release 4) version: V4r4"
        )

    ECCO_L4_ATM_STATE_LLC0090GRID_MONTHLY_V4R4_VV4R4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_ATM_STATE_LLC0090GRID_MONTHLY_V4R4_V4r4",
            provider="POCLOUD", 
            shortname="ECCO_L4_ATM_STATE_LLC0090GRID_MONTHLY_V4R4",
            version="V4r4",
            description="ECCO Atmosphere Surface Temperature, Humidity, Wind, and Pressure - Monthly Mean llc90 Grid (Version 4 Release 4) version: V4r4"
        )

    ECCO_L4_OCEAN_BOLUS_STREAMFUNCTION_LLC0090GRID_DAILY_V4R4_VV4R4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_OCEAN_BOLUS_STREAMFUNCTION_LLC0090GRID_DAILY_V4R4_V4r4",
            provider="POCLOUD", 
            shortname="ECCO_L4_OCEAN_BOLUS_STREAMFUNCTION_LLC0090GRID_DAILY_V4R4",
            version="V4r4",
            description="ECCO Gent-McWilliams Bolus Transport Streamfunction - Daily Mean llc90 Grid (Version 4 Release 4) version: V4r4"
        )

    ECCO_L4_OCEAN_BOLUS_STREAMFUNCTION_LLC0090GRID_MONTHLY_V4R4_VV4R4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_OCEAN_BOLUS_STREAMFUNCTION_LLC0090GRID_MONTHLY_V4R4_V4r4",
            provider="POCLOUD", 
            shortname="ECCO_L4_OCEAN_BOLUS_STREAMFUNCTION_LLC0090GRID_MONTHLY_V4R4",
            version="V4r4",
            description="ECCO Gent-McWilliams Bolus Transport Streamfunction - Monthly Mean llc90 Grid (Version 4 Release 4) version: V4r4"
        )

    ECCO_L4_BOLUS_05DEG_DAILY_V4R4_VV4R4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_BOLUS_05DEG_DAILY_V4R4_V4r4",
            provider="POCLOUD", 
            shortname="ECCO_L4_BOLUS_05DEG_DAILY_V4R4",
            version="V4r4",
            description="ECCO Gent-McWilliams Ocean Bolus Velocity - Daily Mean 0.5 Degree (Version 4 Release 4) version: V4r4"
        )

    ECCO_L4_BOLUS_LLC0090GRID_DAILY_V4R4_VV4R4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_BOLUS_LLC0090GRID_DAILY_V4R4_V4r4",
            provider="POCLOUD", 
            shortname="ECCO_L4_BOLUS_LLC0090GRID_DAILY_V4R4",
            version="V4r4",
            description="ECCO Gent-McWilliams Ocean Bolus Velocity - Daily Mean llc90 Grid (Version 4 Release 4) version: V4r4"
        )

    ECCO_L4_BOLUS_05DEG_MONTHLY_V4R4_VV4R4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_BOLUS_05DEG_MONTHLY_V4R4_V4r4",
            provider="POCLOUD", 
            shortname="ECCO_L4_BOLUS_05DEG_MONTHLY_V4R4",
            version="V4r4",
            description="ECCO Gent-McWilliams Ocean Bolus Velocity - Monthly Mean 0.5 Degree (Version 4 Release 4) version: V4r4"
        )

    ECCO_L4_BOLUS_LLC0090GRID_MONTHLY_V4R4_VV4R4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_BOLUS_LLC0090GRID_MONTHLY_V4R4_V4r4",
            provider="POCLOUD", 
            shortname="ECCO_L4_BOLUS_LLC0090GRID_MONTHLY_V4R4",
            version="V4r4",
            description="ECCO Gent-McWilliams Ocean Bolus Velocity - Monthly Mean llc90 Grid (Version 4 Release 4) version: V4r4"
        )

    ECCO_L4_GEOMETRY_05DEG_V4R4_VV4R4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_GEOMETRY_05DEG_V4R4_V4r4",
            provider="POCLOUD", 
            shortname="ECCO_L4_GEOMETRY_05DEG_V4R4",
            version="V4r4",
            description="ECCO Geometry Parameters for the 0.5 degree Lat-Lon Model Grid (Version 4 Release 4) version: V4r4"
        )

    ECCO_L4_GEOMETRY_LLC0090GRID_V4R4_VV4R4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_GEOMETRY_LLC0090GRID_V4R4_V4r4",
            provider="POCLOUD", 
            shortname="ECCO_L4_GEOMETRY_LLC0090GRID_V4R4",
            version="V4r4",
            description="ECCO Geometry Parameters for the Lat-Lon-Cap 90 (llc90) Native Model Grid (Version 4 Release 4) version: V4r4"
        )

    ECCO_L4_GMAP_TIME_SERIES_SNAPSHOT_V4R4_VV4R4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_GMAP_TIME_SERIES_SNAPSHOT_V4R4_V4r4",
            provider="POCLOUD", 
            shortname="ECCO_L4_GMAP_TIME_SERIES_SNAPSHOT_V4R4",
            version="V4r4",
            description="ECCO Global Mean Atmospheric Pressure - Snapshot (Version 4 Release 4) version: V4r4"
        )

    ECCO_L4_GMAP_TIME_SERIES_SNAPSHOT_V4R4B_VV4R4B_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_GMAP_TIME_SERIES_SNAPSHOT_V4R4B_V4r4b",
            provider="POCLOUD", 
            shortname="ECCO_L4_GMAP_TIME_SERIES_SNAPSHOT_V4R4B",
            version="V4r4b",
            description="ECCO Global Mean Atmospheric Pressure - Snapshot (Version 4 Release 4b) version: V4r4b"
        )

    ECCO_L4_GMSL_TIME_SERIES_DAILY_V4R4_VV4R4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_GMSL_TIME_SERIES_DAILY_V4R4_V4r4",
            provider="POCLOUD", 
            shortname="ECCO_L4_GMSL_TIME_SERIES_DAILY_V4R4",
            version="V4r4",
            description="ECCO Global Mean Sea Level - Daily Mean (Version 4 Release 4) version: V4r4"
        )

    ECCO_L4_GMSL_TIME_SERIES_MONTHLY_V4R4_VV4R4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_GMSL_TIME_SERIES_MONTHLY_V4R4_V4r4",
            provider="POCLOUD", 
            shortname="ECCO_L4_GMSL_TIME_SERIES_MONTHLY_V4R4",
            version="V4r4",
            description="ECCO Global Mean Sea Level - Monthly Mean (Version 4 Release 4) version: V4r4"
        )

    ECCO_L4_OCEAN_3D_MIX_COEFFS_05DEG_V4R4_VV4R4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_OCEAN_3D_MIX_COEFFS_05DEG_V4R4_V4r4",
            provider="POCLOUD", 
            shortname="ECCO_L4_OCEAN_3D_MIX_COEFFS_05DEG_V4R4",
            version="V4r4",
            description="ECCO Ocean 3D Gent-Mcwilliams, Redi, and Background Vertical Diffusivity Coefficients for the 0.5 degree Lat-Lon Model Grid (Version 4 Release 4) version: V4r4"
        )

    ECCO_L4_OCEAN_3D_MIX_COEFFS_LLC0090GRID_V4R4_VV4R4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_OCEAN_3D_MIX_COEFFS_LLC0090GRID_V4R4_V4r4",
            provider="POCLOUD", 
            shortname="ECCO_L4_OCEAN_3D_MIX_COEFFS_LLC0090GRID_V4R4",
            version="V4r4",
            description="ECCO Ocean 3D Gent-Mcwilliams, Redi, and Background Vertical Diffusivity Coefficients for the Lat-Lon-Cap 90 (llc90) Native Model Grid (Version 4 Release 4) version: V4r4"
        )

    ECCO_L4_OBP_05DEG_DAILY_V4R4_VV4R4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_OBP_05DEG_DAILY_V4R4_V4r4",
            provider="POCLOUD", 
            shortname="ECCO_L4_OBP_05DEG_DAILY_V4R4",
            version="V4r4",
            description="ECCO Ocean Bottom Pressure - Daily Mean 0.5 Degree (Version 4 Release 4) version: V4r4"
        )

    ECCO_L4_OBP_05DEG_DAILY_V4R4B_VV4R4B_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_OBP_05DEG_DAILY_V4R4B_V4r4b",
            provider="POCLOUD", 
            shortname="ECCO_L4_OBP_05DEG_DAILY_V4R4B",
            version="V4r4b",
            description="ECCO Ocean Bottom Pressure - Daily Mean 0.5 Degree (Version 4 Release 4b) version: V4r4b"
        )

    ECCO_L4_OBP_LLC0090GRID_DAILY_V4R4_VV4R4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_OBP_LLC0090GRID_DAILY_V4R4_V4r4",
            provider="POCLOUD", 
            shortname="ECCO_L4_OBP_LLC0090GRID_DAILY_V4R4",
            version="V4r4",
            description="ECCO Ocean Bottom Pressure - Daily Mean llc90 Grid (Version 4 Release 4) version: V4r4"
        )

    ECCO_L4_OBP_LLC0090GRID_DAILY_V4R4B_VV4R4B_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_OBP_LLC0090GRID_DAILY_V4R4B_V4r4b",
            provider="POCLOUD", 
            shortname="ECCO_L4_OBP_LLC0090GRID_DAILY_V4R4B",
            version="V4r4b",
            description="ECCO Ocean Bottom Pressure - Daily Mean llc90 Grid (Version 4 Release 4b) version: V4r4b"
        )

    ECCO_L4_OBP_05DEG_MONTHLY_V4R4_VV4R4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_OBP_05DEG_MONTHLY_V4R4_V4r4",
            provider="POCLOUD", 
            shortname="ECCO_L4_OBP_05DEG_MONTHLY_V4R4",
            version="V4r4",
            description="ECCO Ocean Bottom Pressure - Monthly Mean 0.5 Degree (Version 4 Release 4) version: V4r4"
        )

    ECCO_L4_OBP_05DEG_MONTHLY_V4R4B_VV4R4B_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_OBP_05DEG_MONTHLY_V4R4B_V4r4b",
            provider="POCLOUD", 
            shortname="ECCO_L4_OBP_05DEG_MONTHLY_V4R4B",
            version="V4r4b",
            description="ECCO Ocean Bottom Pressure - Monthly Mean 0.5 Degree (Version 4 Release 4b) version: V4r4b"
        )

    ECCO_L4_OBP_LLC0090GRID_MONTHLY_V4R4_VV4R4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_OBP_LLC0090GRID_MONTHLY_V4R4_V4r4",
            provider="POCLOUD", 
            shortname="ECCO_L4_OBP_LLC0090GRID_MONTHLY_V4R4",
            version="V4r4",
            description="ECCO Ocean Bottom Pressure - Monthly Mean llc90 Grid (Version 4 Release 4) version: V4r4"
        )

    ECCO_L4_OBP_LLC0090GRID_MONTHLY_V4R4B_VV4R4B_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_OBP_LLC0090GRID_MONTHLY_V4R4B_V4r4b",
            provider="POCLOUD", 
            shortname="ECCO_L4_OBP_LLC0090GRID_MONTHLY_V4R4B",
            version="V4r4b",
            description="ECCO Ocean Bottom Pressure - Monthly Mean llc90 Grid (Version 4 Release 4b) version: V4r4b"
        )

    ECCO_L4_OBP_LLC0090GRID_SNAPSHOT_V4R4_VV4R4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_OBP_LLC0090GRID_SNAPSHOT_V4R4_V4r4",
            provider="POCLOUD", 
            shortname="ECCO_L4_OBP_LLC0090GRID_SNAPSHOT_V4R4",
            version="V4r4",
            description="ECCO Ocean Bottom Pressure - Snapshot llc90 Grid (Version 4 Release 4) version: V4r4"
        )

    ECCO_L4_DENS_STRAT_PRESS_05DEG_DAILY_V4R4_VV4R4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_DENS_STRAT_PRESS_05DEG_DAILY_V4R4_V4r4",
            provider="POCLOUD", 
            shortname="ECCO_L4_DENS_STRAT_PRESS_05DEG_DAILY_V4R4",
            version="V4r4",
            description="ECCO Ocean Density, Stratification, and Hydrostatic Pressure - Daily Mean 0.5 Degree (Version 4 Release 4) version: V4r4"
        )

    ECCO_L4_DENS_STRAT_PRESS_LLC0090GRID_DAILY_V4R4_VV4R4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_DENS_STRAT_PRESS_LLC0090GRID_DAILY_V4R4_V4r4",
            provider="POCLOUD", 
            shortname="ECCO_L4_DENS_STRAT_PRESS_LLC0090GRID_DAILY_V4R4",
            version="V4r4",
            description="ECCO Ocean Density, Stratification, and Hydrostatic Pressure - Daily Mean llc90 Grid (Version 4 Release 4) version: V4r4"
        )

    ECCO_L4_DENS_STRAT_PRESS_05DEG_MONTHLY_V4R4_VV4R4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_DENS_STRAT_PRESS_05DEG_MONTHLY_V4R4_V4r4",
            provider="POCLOUD", 
            shortname="ECCO_L4_DENS_STRAT_PRESS_05DEG_MONTHLY_V4R4",
            version="V4r4",
            description="ECCO Ocean Density, Stratification, and Hydrostatic Pressure - Monthly Mean 0.5 Degree (Version 4 Release 4) version: V4r4"
        )

    ECCO_L4_DENS_STRAT_PRESS_LLC0090GRID_MONTHLY_V4R4_VV4R4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_DENS_STRAT_PRESS_LLC0090GRID_MONTHLY_V4R4_V4r4",
            provider="POCLOUD", 
            shortname="ECCO_L4_DENS_STRAT_PRESS_LLC0090GRID_MONTHLY_V4R4",
            version="V4r4",
            description="ECCO Ocean Density, Stratification, and Hydrostatic Pressure - Monthly Mean llc90 Grid (Version 4 Release 4) version: V4r4"
        )

    ECCO_L4_MIXED_LAYER_DEPTH_05DEG_DAILY_V4R4_VV4R4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_MIXED_LAYER_DEPTH_05DEG_DAILY_V4R4_V4r4",
            provider="POCLOUD", 
            shortname="ECCO_L4_MIXED_LAYER_DEPTH_05DEG_DAILY_V4R4",
            version="V4r4",
            description="ECCO Ocean Mixed Layer Depth - Daily Mean 0.5 Degree (Version 4 Release 4) version: V4r4"
        )

    ECCO_L4_MIXED_LAYER_DEPTH_LLC0090GRID_DAILY_V4R4_VV4R4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_MIXED_LAYER_DEPTH_LLC0090GRID_DAILY_V4R4_V4r4",
            provider="POCLOUD", 
            shortname="ECCO_L4_MIXED_LAYER_DEPTH_LLC0090GRID_DAILY_V4R4",
            version="V4r4",
            description="ECCO Ocean Mixed Layer Depth - Daily Mean llc90 Grid (Version 4 Release 4) version: V4r4"
        )

    ECCO_L4_MIXED_LAYER_DEPTH_05DEG_MONTHLY_V4R4_VV4R4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_MIXED_LAYER_DEPTH_05DEG_MONTHLY_V4R4_V4r4",
            provider="POCLOUD", 
            shortname="ECCO_L4_MIXED_LAYER_DEPTH_05DEG_MONTHLY_V4R4",
            version="V4r4",
            description="ECCO Ocean Mixed Layer Depth - Monthly Mean 0.5 Degree (Version 4 Release 4) version: V4r4"
        )

    ECCO_L4_MIXED_LAYER_DEPTH_LLC0090GRID_MONTHLY_V4R4_VV4R4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_MIXED_LAYER_DEPTH_LLC0090GRID_MONTHLY_V4R4_V4r4",
            provider="POCLOUD", 
            shortname="ECCO_L4_MIXED_LAYER_DEPTH_LLC0090GRID_MONTHLY_V4R4",
            version="V4r4",
            description="ECCO Ocean Mixed Layer Depth - Monthly Mean llc90 Grid (Version 4 Release 4) version: V4r4"
        )

    ECCO_L4_TEMP_SALINITY_05DEG_DAILY_V4R4_VV4R4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_TEMP_SALINITY_05DEG_DAILY_V4R4_V4r4",
            provider="POCLOUD", 
            shortname="ECCO_L4_TEMP_SALINITY_05DEG_DAILY_V4R4",
            version="V4r4",
            description="ECCO Ocean Temperature and Salinity - Daily Mean 0.5 Degree (Version 4 Release 4) version: V4r4"
        )

    ECCO_L4_TEMP_SALINITY_LLC0090GRID_DAILY_V4R4_VV4R4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_TEMP_SALINITY_LLC0090GRID_DAILY_V4R4_V4r4",
            provider="POCLOUD", 
            shortname="ECCO_L4_TEMP_SALINITY_LLC0090GRID_DAILY_V4R4",
            version="V4r4",
            description="ECCO Ocean Temperature and Salinity - Daily Mean llc90 Grid (Version 4 Release 4) version: V4r4"
        )

    ECCO_L4_TEMP_SALINITY_05DEG_MONTHLY_V4R4_VV4R4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_TEMP_SALINITY_05DEG_MONTHLY_V4R4_V4r4",
            provider="POCLOUD", 
            shortname="ECCO_L4_TEMP_SALINITY_05DEG_MONTHLY_V4R4",
            version="V4r4",
            description="ECCO Ocean Temperature and Salinity - Monthly Mean 0.5 Degree (Version 4 Release 4) version: V4r4"
        )

    ECCO_L4_TEMP_SALINITY_LLC0090GRID_MONTHLY_V4R4_VV4R4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_TEMP_SALINITY_LLC0090GRID_MONTHLY_V4R4_V4r4",
            provider="POCLOUD", 
            shortname="ECCO_L4_TEMP_SALINITY_LLC0090GRID_MONTHLY_V4R4",
            version="V4r4",
            description="ECCO Ocean Temperature and Salinity - Monthly Mean llc90 Grid (Version 4 Release 4) version: V4r4"
        )

    ECCO_L4_TEMP_SALINITY_LLC0090GRID_SNAPSHOT_V4R4_VV4R4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_TEMP_SALINITY_LLC0090GRID_SNAPSHOT_V4R4_V4r4",
            provider="POCLOUD", 
            shortname="ECCO_L4_TEMP_SALINITY_LLC0090GRID_SNAPSHOT_V4R4",
            version="V4r4",
            description="ECCO Ocean Temperature and Salinity - Snapshot llc90 Grid (Version 4 Release 4) version: V4r4"
        )

    ECCO_L4_OCEAN_3D_MOMENTUM_TEND_LLC0090GRID_DAILY_V4R4_VV4R4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_OCEAN_3D_MOMENTUM_TEND_LLC0090GRID_DAILY_V4R4_V4r4",
            provider="POCLOUD", 
            shortname="ECCO_L4_OCEAN_3D_MOMENTUM_TEND_LLC0090GRID_DAILY_V4R4",
            version="V4r4",
            description="ECCO Ocean Three-Dimensional Momentum Tendency - Daily Mean llc90 Grid (Version 4 Release 4) version: V4r4"
        )

    ECCO_L4_OCEAN_3D_MOMENTUM_TEND_LLC0090GRID_MONTHLY_V4R4_VV4R4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_OCEAN_3D_MOMENTUM_TEND_LLC0090GRID_MONTHLY_V4R4_V4r4",
            provider="POCLOUD", 
            shortname="ECCO_L4_OCEAN_3D_MOMENTUM_TEND_LLC0090GRID_MONTHLY_V4R4",
            version="V4r4",
            description="ECCO Ocean Three-Dimensional Momentum Tendency - Monthly Mean llc90 Grid (Version 4 Release 4) version: V4r4"
        )

    ECCO_L4_OCEAN_3D_TEMPERATURE_FLUX_LLC0090GRID_DAILY_V4R4_VV4R4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_OCEAN_3D_TEMPERATURE_FLUX_LLC0090GRID_DAILY_V4R4_V4r4",
            provider="POCLOUD", 
            shortname="ECCO_L4_OCEAN_3D_TEMPERATURE_FLUX_LLC0090GRID_DAILY_V4R4",
            version="V4r4",
            description="ECCO Ocean Three-Dimensional Potential Temperature Fluxes - Daily Mean llc90 Grid (Version 4 Release 4) version: V4r4"
        )

    ECCO_L4_OCEAN_3D_TEMPERATURE_FLUX_LLC0090GRID_MONTHLY_V4R4_VV4R4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_OCEAN_3D_TEMPERATURE_FLUX_LLC0090GRID_MONTHLY_V4R4_V4r4",
            provider="POCLOUD", 
            shortname="ECCO_L4_OCEAN_3D_TEMPERATURE_FLUX_LLC0090GRID_MONTHLY_V4R4",
            version="V4r4",
            description="ECCO Ocean Three-Dimensional Potential Temperature Fluxes - Monthly Mean llc90 Grid (Version 4 Release 4) version: V4r4"
        )

    ECCO_L4_OCEAN_3D_SALINITY_FLUX_LLC0090GRID_DAILY_V4R4_VV4R4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_OCEAN_3D_SALINITY_FLUX_LLC0090GRID_DAILY_V4R4_V4r4",
            provider="POCLOUD", 
            shortname="ECCO_L4_OCEAN_3D_SALINITY_FLUX_LLC0090GRID_DAILY_V4R4",
            version="V4r4",
            description="ECCO Ocean Three-Dimensional Salinity Fluxes - Daily Mean llc90 Grid (Version 4 Release 4) version: V4r4"
        )

    ECCO_L4_OCEAN_3D_SALINITY_FLUX_LLC0090GRID_MONTHLY_V4R4_VV4R4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_OCEAN_3D_SALINITY_FLUX_LLC0090GRID_MONTHLY_V4R4_V4r4",
            provider="POCLOUD", 
            shortname="ECCO_L4_OCEAN_3D_SALINITY_FLUX_LLC0090GRID_MONTHLY_V4R4",
            version="V4r4",
            description="ECCO Ocean Three-Dimensional Salinity Fluxes - Monthly Mean llc90 Grid (Version 4 Release 4) version: V4r4"
        )

    ECCO_L4_OCEAN_3D_VOLUME_FLUX_LLC0090GRID_DAILY_V4R4_VV4R4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_OCEAN_3D_VOLUME_FLUX_LLC0090GRID_DAILY_V4R4_V4r4",
            provider="POCLOUD", 
            shortname="ECCO_L4_OCEAN_3D_VOLUME_FLUX_LLC0090GRID_DAILY_V4R4",
            version="V4r4",
            description="ECCO Ocean Three-Dimensional Volume Fluxes - Daily Mean llc90 Grid (Version 4 Release 4) version: V4r4"
        )

    ECCO_L4_OCEAN_3D_VOLUME_FLUX_LLC0090GRID_MONTHLY_V4R4_VV4R4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_OCEAN_3D_VOLUME_FLUX_LLC0090GRID_MONTHLY_V4R4_V4r4",
            provider="POCLOUD", 
            shortname="ECCO_L4_OCEAN_3D_VOLUME_FLUX_LLC0090GRID_MONTHLY_V4R4",
            version="V4r4",
            description="ECCO Ocean Three-Dimensional Volume Fluxes - Monthly Mean llc90 Grid (Version 4 Release 4) version: V4r4"
        )

    ECCO_L4_OCEAN_VEL_05DEG_DAILY_V4R4_VV4R4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_OCEAN_VEL_05DEG_DAILY_V4R4_V4r4",
            provider="POCLOUD", 
            shortname="ECCO_L4_OCEAN_VEL_05DEG_DAILY_V4R4",
            version="V4r4",
            description="ECCO Ocean Velocity - Daily Mean 0.5 Degree (Version 4 Release 4) version: V4r4"
        )

    ECCO_L4_OCEAN_VEL_LLC0090GRID_DAILY_V4R4_VV4R4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_OCEAN_VEL_LLC0090GRID_DAILY_V4R4_V4r4",
            provider="POCLOUD", 
            shortname="ECCO_L4_OCEAN_VEL_LLC0090GRID_DAILY_V4R4",
            version="V4r4",
            description="ECCO Ocean Velocity - Daily Mean llc90 Grid (Version 4 Release 4) version: V4r4"
        )

    ECCO_L4_OCEAN_VEL_05DEG_MONTHLY_V4R4_VV4R4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_OCEAN_VEL_05DEG_MONTHLY_V4R4_V4r4",
            provider="POCLOUD", 
            shortname="ECCO_L4_OCEAN_VEL_05DEG_MONTHLY_V4R4",
            version="V4r4",
            description="ECCO Ocean Velocity - Monthly Mean 0.5 Degree (Version 4 Release 4) version: V4r4"
        )

    ECCO_L4_OCEAN_VEL_LLC0090GRID_MONTHLY_V4R4_VV4R4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_OCEAN_VEL_LLC0090GRID_MONTHLY_V4R4_V4r4",
            provider="POCLOUD", 
            shortname="ECCO_L4_OCEAN_VEL_LLC0090GRID_MONTHLY_V4R4",
            version="V4r4",
            description="ECCO Ocean Velocity - Monthly Mean llc90 Grid (Version 4 Release 4) version: V4r4"
        )

    ECCO_L4_FRESH_FLUX_05DEG_DAILY_V4R4_VV4R4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_FRESH_FLUX_05DEG_DAILY_V4R4_V4r4",
            provider="POCLOUD", 
            shortname="ECCO_L4_FRESH_FLUX_05DEG_DAILY_V4R4",
            version="V4r4",
            description="ECCO Ocean and Sea-Ice Surface Freshwater Fluxes - Daily Mean 0.5 Degree (Version 4 Release 4) version: V4r4"
        )

    ECCO_L4_FRESH_FLUX_LLC0090GRID_DAILY_V4R4_VV4R4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_FRESH_FLUX_LLC0090GRID_DAILY_V4R4_V4r4",
            provider="POCLOUD", 
            shortname="ECCO_L4_FRESH_FLUX_LLC0090GRID_DAILY_V4R4",
            version="V4r4",
            description="ECCO Ocean and Sea-Ice Surface Freshwater Fluxes - Daily Mean llc90 Grid (Version 4 Release 4) version: V4r4"
        )

    ECCO_L4_FRESH_FLUX_05DEG_MONTHLY_V4R4_VV4R4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_FRESH_FLUX_05DEG_MONTHLY_V4R4_V4r4",
            provider="POCLOUD", 
            shortname="ECCO_L4_FRESH_FLUX_05DEG_MONTHLY_V4R4",
            version="V4r4",
            description="ECCO Ocean and Sea-Ice Surface Freshwater Fluxes - Monthly Mean 0.5 Degree (Version 4 Release 4) version: V4r4"
        )

    ECCO_L4_FRESH_FLUX_LLC0090GRID_MONTHLY_V4R4_VV4R4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_FRESH_FLUX_LLC0090GRID_MONTHLY_V4R4_V4r4",
            provider="POCLOUD", 
            shortname="ECCO_L4_FRESH_FLUX_LLC0090GRID_MONTHLY_V4R4",
            version="V4r4",
            description="ECCO Ocean and Sea-Ice Surface Freshwater Fluxes - Monthly Mean llc90 Grid (Version 4 Release 4) version: V4r4"
        )

    ECCO_L4_HEAT_FLUX_05DEG_DAILY_V4R4_VV4R4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_HEAT_FLUX_05DEG_DAILY_V4R4_V4r4",
            provider="POCLOUD", 
            shortname="ECCO_L4_HEAT_FLUX_05DEG_DAILY_V4R4",
            version="V4r4",
            description="ECCO Ocean and Sea-Ice Surface Heat Fluxes - Daily Mean 0.5 Degree (Version 4 Release 4) version: V4r4"
        )

    ECCO_L4_HEAT_FLUX_LLC0090GRID_DAILY_V4R4_VV4R4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_HEAT_FLUX_LLC0090GRID_DAILY_V4R4_V4r4",
            provider="POCLOUD", 
            shortname="ECCO_L4_HEAT_FLUX_LLC0090GRID_DAILY_V4R4",
            version="V4r4",
            description="ECCO Ocean and Sea-Ice Surface Heat Fluxes - Daily Mean llc90 Grid (Version 4 Release 4) version: V4r4"
        )

    ECCO_L4_HEAT_FLUX_05DEG_MONTHLY_V4R4_VV4R4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_HEAT_FLUX_05DEG_MONTHLY_V4R4_V4r4",
            provider="POCLOUD", 
            shortname="ECCO_L4_HEAT_FLUX_05DEG_MONTHLY_V4R4",
            version="V4r4",
            description="ECCO Ocean and Sea-Ice Surface Heat Fluxes - Monthly Mean 0.5 Degree (Version 4 Release 4) version: V4r4"
        )

    ECCO_L4_HEAT_FLUX_LLC0090GRID_MONTHLY_V4R4_VV4R4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_HEAT_FLUX_LLC0090GRID_MONTHLY_V4R4_V4r4",
            provider="POCLOUD", 
            shortname="ECCO_L4_HEAT_FLUX_LLC0090GRID_MONTHLY_V4R4",
            version="V4r4",
            description="ECCO Ocean and Sea-Ice Surface Heat Fluxes - Monthly Mean llc90 Grid (Version 4 Release 4) version: V4r4"
        )

    ECCO_L4_STRESS_05DEG_DAILY_V4R4_VV4R4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_STRESS_05DEG_DAILY_V4R4_V4r4",
            provider="POCLOUD", 
            shortname="ECCO_L4_STRESS_05DEG_DAILY_V4R4",
            version="V4r4",
            description="ECCO Ocean and Sea-Ice Surface Stress - Daily Mean 0.5 Degree (Version 4 Release 4) version: V4r4"
        )

    ECCO_L4_STRESS_LLC0090GRID_DAILY_V4R4_VV4R4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_STRESS_LLC0090GRID_DAILY_V4R4_V4r4",
            provider="POCLOUD", 
            shortname="ECCO_L4_STRESS_LLC0090GRID_DAILY_V4R4",
            version="V4r4",
            description="ECCO Ocean and Sea-Ice Surface Stress - Daily Mean llc90 Grid (Version 4 Release 4) version: V4r4"
        )

    ECCO_L4_STRESS_05DEG_MONTHLY_V4R4_VV4R4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_STRESS_05DEG_MONTHLY_V4R4_V4r4",
            provider="POCLOUD", 
            shortname="ECCO_L4_STRESS_05DEG_MONTHLY_V4R4",
            version="V4r4",
            description="ECCO Ocean and Sea-Ice Surface Stress - Monthly Mean 0.5 Degree (Version 4 Release 4) version: V4r4"
        )

    ECCO_L4_STRESS_LLC0090GRID_MONTHLY_V4R4_VV4R4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_STRESS_LLC0090GRID_MONTHLY_V4R4_V4r4",
            provider="POCLOUD", 
            shortname="ECCO_L4_STRESS_LLC0090GRID_MONTHLY_V4R4",
            version="V4r4",
            description="ECCO Ocean and Sea-Ice Surface Stress - Monthly Mean llc90 Grid (Version 4 Release 4) version: V4r4"
        )

    ECCO_L4_SBO_CORE_TIME_SERIES_SNAPSHOT_V4R4_VV4R4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_SBO_CORE_TIME_SERIES_SNAPSHOT_V4R4_V4r4",
            provider="POCLOUD", 
            shortname="ECCO_L4_SBO_CORE_TIME_SERIES_SNAPSHOT_V4R4",
            version="V4r4",
            description="ECCO SBO Core Products - Snapshot (Version 4 Release 4) version: V4r4"
        )

    ECCO_L4_SBO_CORE_TIME_SERIES_SNAPSHOT_V4R4B_VV4R4B_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_SBO_CORE_TIME_SERIES_SNAPSHOT_V4R4B_V4r4b",
            provider="POCLOUD", 
            shortname="ECCO_L4_SBO_CORE_TIME_SERIES_SNAPSHOT_V4R4B",
            version="V4r4b",
            description="ECCO SBO Core Products - Snapshot (Version 4 Release 4b) version: V4r4b"
        )

    ECCO_L4_SSH_05DEG_DAILY_V4R4_VV4R4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_SSH_05DEG_DAILY_V4R4_V4r4",
            provider="POCLOUD", 
            shortname="ECCO_L4_SSH_05DEG_DAILY_V4R4",
            version="V4r4",
            description="ECCO Sea Surface Height - Daily Mean 0.5 Degree (Version 4 Release 4) version: V4r4"
        )

    ECCO_L4_SSH_05DEG_DAILY_V4R4B_VV4R4B_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_SSH_05DEG_DAILY_V4R4B_V4r4b",
            provider="POCLOUD", 
            shortname="ECCO_L4_SSH_05DEG_DAILY_V4R4B",
            version="V4r4b",
            description="ECCO Sea Surface Height - Daily Mean 0.5 Degree (Version 4 Release 4b) version: V4r4b"
        )

    ECCO_L4_SSH_LLC0090GRID_DAILY_V4R4_VV4R4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_SSH_LLC0090GRID_DAILY_V4R4_V4r4",
            provider="POCLOUD", 
            shortname="ECCO_L4_SSH_LLC0090GRID_DAILY_V4R4",
            version="V4r4",
            description="ECCO Sea Surface Height - Daily Mean llc90 Grid (Version 4 Release 4) version: V4r4"
        )

    ECCO_L4_SSH_LLC0090GRID_DAILY_V4R4B_VV4R4B_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_SSH_LLC0090GRID_DAILY_V4R4B_V4r4b",
            provider="POCLOUD", 
            shortname="ECCO_L4_SSH_LLC0090GRID_DAILY_V4R4B",
            version="V4r4b",
            description="ECCO Sea Surface Height - Daily Mean llc90 Grid (Version 4 Release 4b) version: V4r4b"
        )

    ECCO_L4_SSH_05DEG_MONTHLY_V4R4_VV4R4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_SSH_05DEG_MONTHLY_V4R4_V4r4",
            provider="POCLOUD", 
            shortname="ECCO_L4_SSH_05DEG_MONTHLY_V4R4",
            version="V4r4",
            description="ECCO Sea Surface Height - Monthly Mean 0.5 Degree (Version 4 Release 4) version: V4r4"
        )

    ECCO_L4_SSH_05DEG_MONTHLY_V4R4B_VV4R4B_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_SSH_05DEG_MONTHLY_V4R4B_V4r4b",
            provider="POCLOUD", 
            shortname="ECCO_L4_SSH_05DEG_MONTHLY_V4R4B",
            version="V4r4b",
            description="ECCO Sea Surface Height - Monthly Mean 0.5 Degree (Version 4 Release 4b) version: V4r4b"
        )

    ECCO_L4_SSH_LLC0090GRID_MONTHLY_V4R4_VV4R4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_SSH_LLC0090GRID_MONTHLY_V4R4_V4r4",
            provider="POCLOUD", 
            shortname="ECCO_L4_SSH_LLC0090GRID_MONTHLY_V4R4",
            version="V4r4",
            description="ECCO Sea Surface Height - Monthly Mean llc90 Grid (Version 4 Release 4) version: V4r4"
        )

    ECCO_L4_SSH_LLC0090GRID_MONTHLY_V4R4B_VV4R4B_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_SSH_LLC0090GRID_MONTHLY_V4R4B_V4r4b",
            provider="POCLOUD", 
            shortname="ECCO_L4_SSH_LLC0090GRID_MONTHLY_V4R4B",
            version="V4r4b",
            description="ECCO Sea Surface Height - Monthly Mean llc90 Grid (Version 4 Release 4b) version: V4r4b"
        )

    ECCO_L4_SSH_LLC0090GRID_SNAPSHOT_V4R4_VV4R4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_SSH_LLC0090GRID_SNAPSHOT_V4R4_V4r4",
            provider="POCLOUD", 
            shortname="ECCO_L4_SSH_LLC0090GRID_SNAPSHOT_V4R4",
            version="V4r4",
            description="ECCO Sea Surface Height - Snapshot llc90 Grid (Version 4 Release 4) version: V4r4"
        )

    ECCO_L4_SEA_ICE_SALT_PLUME_FLUX_LLC0090GRID_DAILY_V4R4_VV4R4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_SEA_ICE_SALT_PLUME_FLUX_LLC0090GRID_DAILY_V4R4_V4r4",
            provider="POCLOUD", 
            shortname="ECCO_L4_SEA_ICE_SALT_PLUME_FLUX_LLC0090GRID_DAILY_V4R4",
            version="V4r4",
            description="ECCO Sea-Ice Salt Plume Fluxes - Daily Mean llc90 Grid (Version 4 Release 4) version: V4r4"
        )

    ECCO_L4_SEA_ICE_SALT_PLUME_FLUX_LLC0090GRID_MONTHLY_V4R4_VV4R4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_SEA_ICE_SALT_PLUME_FLUX_LLC0090GRID_MONTHLY_V4R4_V4r4",
            provider="POCLOUD", 
            shortname="ECCO_L4_SEA_ICE_SALT_PLUME_FLUX_LLC0090GRID_MONTHLY_V4R4",
            version="V4r4",
            description="ECCO Sea-Ice Salt Plume Fluxes - Monthly Mean llc90 Grid (Version 4 Release 4) version: V4r4"
        )

    ECCO_L4_SEA_ICE_VELOCITY_05DEG_DAILY_V4R4_VV4R4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_SEA_ICE_VELOCITY_05DEG_DAILY_V4R4_V4r4",
            provider="POCLOUD", 
            shortname="ECCO_L4_SEA_ICE_VELOCITY_05DEG_DAILY_V4R4",
            version="V4r4",
            description="ECCO Sea-Ice Velocity - Daily Mean 0.5 Degree (Version 4 Release 4) version: V4r4"
        )

    ECCO_L4_SEA_ICE_VELOCITY_LLC0090GRID_DAILY_V4R4_VV4R4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_SEA_ICE_VELOCITY_LLC0090GRID_DAILY_V4R4_V4r4",
            provider="POCLOUD", 
            shortname="ECCO_L4_SEA_ICE_VELOCITY_LLC0090GRID_DAILY_V4R4",
            version="V4r4",
            description="ECCO Sea-Ice Velocity - Daily Mean llc90 Grid (Version 4 Release 4) version: V4r4"
        )

    ECCO_L4_SEA_ICE_VELOCITY_05DEG_MONTHLY_V4R4_VV4R4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_SEA_ICE_VELOCITY_05DEG_MONTHLY_V4R4_V4r4",
            provider="POCLOUD", 
            shortname="ECCO_L4_SEA_ICE_VELOCITY_05DEG_MONTHLY_V4R4",
            version="V4r4",
            description="ECCO Sea-Ice Velocity - Monthly Mean 0.5 Degree (Version 4 Release 4) version: V4r4"
        )

    ECCO_L4_SEA_ICE_VELOCITY_LLC0090GRID_MONTHLY_V4R4_VV4R4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_SEA_ICE_VELOCITY_LLC0090GRID_MONTHLY_V4R4_V4r4",
            provider="POCLOUD", 
            shortname="ECCO_L4_SEA_ICE_VELOCITY_LLC0090GRID_MONTHLY_V4R4",
            version="V4r4",
            description="ECCO Sea-Ice Velocity - Monthly Mean llc90 Grid (Version 4 Release 4) version: V4r4"
        )

    ECCO_L4_SEA_ICE_VELOCITY_LLC0090GRID_SNAPSHOT_V4R4_VV4R4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_SEA_ICE_VELOCITY_LLC0090GRID_SNAPSHOT_V4R4_V4r4",
            provider="POCLOUD", 
            shortname="ECCO_L4_SEA_ICE_VELOCITY_LLC0090GRID_SNAPSHOT_V4R4",
            version="V4r4",
            description="ECCO Sea-Ice Velocity - Snapshot llc90 Grid (Version 4 Release 4) version: V4r4"
        )

    ECCO_L4_SEA_ICE_CONC_THICKNESS_05DEG_DAILY_V4R4_VV4R4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_SEA_ICE_CONC_THICKNESS_05DEG_DAILY_V4R4_V4r4",
            provider="POCLOUD", 
            shortname="ECCO_L4_SEA_ICE_CONC_THICKNESS_05DEG_DAILY_V4R4",
            version="V4r4",
            description="ECCO Sea-Ice and Snow Concentration and Thickness - Daily Mean 0.5 Degree (Version 4 Release 4) version: V4r4"
        )

    ECCO_L4_SEA_ICE_CONC_THICKNESS_LLC0090GRID_DAILY_V4R4_VV4R4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_SEA_ICE_CONC_THICKNESS_LLC0090GRID_DAILY_V4R4_V4r4",
            provider="POCLOUD", 
            shortname="ECCO_L4_SEA_ICE_CONC_THICKNESS_LLC0090GRID_DAILY_V4R4",
            version="V4r4",
            description="ECCO Sea-Ice and Snow Concentration and Thickness - Daily Mean llc90 Grid (Version 4 Release 4) version: V4r4"
        )

    ECCO_L4_SEA_ICE_CONC_THICKNESS_05DEG_MONTHLY_V4R4_VV4R4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_SEA_ICE_CONC_THICKNESS_05DEG_MONTHLY_V4R4_V4r4",
            provider="POCLOUD", 
            shortname="ECCO_L4_SEA_ICE_CONC_THICKNESS_05DEG_MONTHLY_V4R4",
            version="V4r4",
            description="ECCO Sea-Ice and Snow Concentration and Thickness - Monthly Mean 0.5 Degree (Version 4 Release 4) version: V4r4"
        )

    ECCO_L4_SEA_ICE_CONC_THICKNESS_LLC0090GRID_MONTHLY_V4R4_VV4R4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_SEA_ICE_CONC_THICKNESS_LLC0090GRID_MONTHLY_V4R4_V4r4",
            provider="POCLOUD", 
            shortname="ECCO_L4_SEA_ICE_CONC_THICKNESS_LLC0090GRID_MONTHLY_V4R4",
            version="V4r4",
            description="ECCO Sea-Ice and Snow Concentration and Thickness - Monthly Mean llc90 Grid (Version 4 Release 4) version: V4r4"
        )

    ECCO_L4_SEA_ICE_CONC_THICKNESS_LLC0090GRID_SNAPSHOT_V4R4_VV4R4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_SEA_ICE_CONC_THICKNESS_LLC0090GRID_SNAPSHOT_V4R4_V4r4",
            provider="POCLOUD", 
            shortname="ECCO_L4_SEA_ICE_CONC_THICKNESS_LLC0090GRID_SNAPSHOT_V4R4",
            version="V4r4",
            description="ECCO Sea-Ice and Snow Concentration and Thickness - Snapshot llc90 Grid (Version 4 Release 4) version: V4r4"
        )

    ECCO_L4_SEA_ICE_HORIZ_VOLUME_FLUX_LLC0090GRID_DAILY_V4R4_VV4R4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_SEA_ICE_HORIZ_VOLUME_FLUX_LLC0090GRID_DAILY_V4R4_V4r4",
            provider="POCLOUD", 
            shortname="ECCO_L4_SEA_ICE_HORIZ_VOLUME_FLUX_LLC0090GRID_DAILY_V4R4",
            version="V4r4",
            description="ECCO Sea-Ice and Snow Horizontal Volume Fluxes - Daily Mean llc90 Grid (Version 4 Release 4) version: V4r4"
        )

    ECCO_L4_SEA_ICE_HORIZ_VOLUME_FLUX_LLC0090GRID_MONTHLY_V4R4_VV4R4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ECCO_L4_SEA_ICE_HORIZ_VOLUME_FLUX_LLC0090GRID_MONTHLY_V4R4_V4r4",
            provider="POCLOUD", 
            shortname="ECCO_L4_SEA_ICE_HORIZ_VOLUME_FLUX_LLC0090GRID_MONTHLY_V4R4",
            version="V4r4",
            description="ECCO Sea-Ice and Snow Horizontal Volume Fluxes - Monthly Mean llc90 Grid (Version 4 Release 4) version: V4r4"
        )

    ERS_1_BYU_L3_OW_SIGMA0_ENHANCED_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ERS-1_BYU_L3_OW_SIGMA0_ENHANCED_1",
            provider="POCLOUD", 
            shortname="ERS-1_BYU_L3_OW_SIGMA0_ENHANCED",
            version="1",
            description="ERS-1 Gridded Level 3 Enhanced Resolution Sigma-0 from BYU version: 1"
        )

    ERS_2_BYU_L3_OW_SIGMA0_ENHANCED_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ERS-2_BYU_L3_OW_SIGMA0_ENHANCED_1",
            provider="POCLOUD", 
            shortname="ERS-2_BYU_L3_OW_SIGMA0_ENHANCED",
            version="1",
            description="ERS-2 Gridded Level 3 Enhanced Resolution Sigma-0 from BYU version: 1"
        )

    SPURS1_ECOMAPPER_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SPURS1_ECOMAPPER_1.0",
            provider="POCLOUD", 
            shortname="SPURS1_ECOMAPPER",
            version="1.0",
            description="Ecomapper data for the SPURS-1 N. Atlantic field campaign version: 1.0"
        )

    GEOS_3_ALT_GDR_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_GEOS-3_ALT_GDR_1",
            provider="POCLOUD", 
            shortname="GEOS-3_ALT_GDR",
            version="1",
            description="GEOS-3 ALTIMETER GEOPHYSICAL DATA RECORD 1975-1978 version: 1"
        )

    TELLUS_GRAC_L3_GFZ_RL06_LND_V04_VRL06V04_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_TELLUS_GRAC_L3_GFZ_RL06_LND_v04_RL06v04",
            provider="POCLOUD", 
            shortname="TELLUS_GRAC_L3_GFZ_RL06_LND_v04",
            version="RL06v04",
            description="GFZ TELLUS GRACE Level-3 Monthly Land Water-Equivalent-Thickness Surface Mass Anomaly Release 6.0 version 04 version: RL06v04"
        )

    TELLUS_GRAC_L3_GFZ_RL06_OCN_V04_VRL06V04_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_TELLUS_GRAC_L3_GFZ_RL06_OCN_v04_RL06v04",
            provider="POCLOUD", 
            shortname="TELLUS_GRAC_L3_GFZ_RL06_OCN_v04",
            version="RL06v04",
            description="GFZ TELLUS GRACE Level-3 Monthly Ocean Bottom Pressure Anomaly Release 6.0 version 04 version: RL06v04"
        )

    TELLUS_GRFO_L3_GFZ_RL063_LND_V04_VRL063V04_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_TELLUS_GRFO_L3_GFZ_RL06.3_LND_v04_RL06.3v04",
            provider="POCLOUD", 
            shortname="TELLUS_GRFO_L3_GFZ_RL06.3_LND_v04",
            version="RL06.3v04",
            description="GFZ TELLUS GRACE-FO Level-3 Monthly Land Water-Equivalent-Thickness Surface Mass Anomaly Release 6.3 version 04 version: RL06.3v04"
        )

    TELLUS_GRFO_L3_GFZ_RL063_OCN_V04_VRL063V04_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_TELLUS_GRFO_L3_GFZ_RL06.3_OCN_v04_RL06.3v04",
            provider="POCLOUD", 
            shortname="TELLUS_GRFO_L3_GFZ_RL06.3_OCN_v04",
            version="RL06.3v04",
            description="GFZ TELLUS GRACE-FO Level-3 Monthly Ocean Bottom Pressure Anomaly Release 6.3 version 04 version: RL06.3v04"
        )

    G18_ABI_L2P_ACSPO_V290_V290_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_G18-ABI-L2P-ACSPO-v2.90_2.90",
            provider="POCLOUD", 
            shortname="G18-ABI-L2P-ACSPO-v2.90",
            version="2.90",
            description="GHRSST L2P NOAA/ACSPO GOES-18/ABI West America Region Sea Surface Temperature v2.90 dataset version: 2.90"
        )

    H09_AHI_L2P_ACSPO_V290_V290_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_H09-AHI-L2P-ACSPO-v2.90_2.90",
            provider="POCLOUD", 
            shortname="H09-AHI-L2P-ACSPO-v2.90",
            version="2.90",
            description="GHRSST L2P NOAA/ACSPO Himawari-09 AHI Pacific Ocean Region Sea Surface Temperature v2.90 dataset version: 2.90"
        )

    G18_ABI_L3C_ACSPO_V290_V290_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_G18-ABI-L3C-ACSPO-v2.90_2.90",
            provider="POCLOUD", 
            shortname="G18-ABI-L3C-ACSPO-v2.90",
            version="2.90",
            description="GHRSST L3C NOAA/ACSPO GOES-18/ABI West America Region Sea Surface Temperature v2.90 dataset version: 2.90"
        )

    H09_AHI_L3C_ACSPO_V290_V290_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_H09-AHI-L3C-ACSPO-v2.90_2.90",
            provider="POCLOUD", 
            shortname="H09-AHI-L3C-ACSPO-v2.90",
            version="2.90",
            description="GHRSST L3C NOAA/ACSPO Himawari-09 AHI Pacific Ocean Region Sea Surface Temperature v2.90 dataset version: 2.90"
        )

    AVHRR_SST_METOP_A_GLB_OSISAF_L3C_V10_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AVHRR_SST_METOP_A_GLB-OSISAF-L3C-v1.0_1",
            provider="POCLOUD", 
            shortname="AVHRR_SST_METOP_A_GLB-OSISAF-L3C-v1.0",
            version="1",
            description="GHRSST L3C global sub-skin Sea Surface Temperature from the Advanced Very High Resolution Radiometer (AVHRR) on Metop satellites (currently Metop-A) (GDS V2) produced by OSI SAF version: 1"
        )

    AVHRR_SST_METOP_B_GLB_OSISAF_L3C_V10_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AVHRR_SST_METOP_B_GLB-OSISAF-L3C-v1.0_1",
            provider="POCLOUD", 
            shortname="AVHRR_SST_METOP_B_GLB-OSISAF-L3C-v1.0",
            version="1",
            description="GHRSST L3C global sub-skin Sea Surface Temperature from the Advanced Very High Resolution Radiometer (AVHRR) on Metop satellites (currently Metop-B) (GDS V2) produced by OSI SAF version: 1"
        )

    GOES16_SST_OSISAF_L3C_V10_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_GOES16-SST-OSISAF-L3C-v1.0_1.0",
            provider="POCLOUD", 
            shortname="GOES16-SST-OSISAF-L3C-v1.0",
            version="1.0",
            description="GHRSST L3C hourly America Region sub-skin Sea Surface Temperature v1.0 from ABI on GOES16 produced by OSISAF version: 1.0"
        )

    SEVIRI_SST_DR_OSISAF_L3C_V10_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SEVIRI_SST_DR-OSISAF-L3C-v1.0_1.0",
            provider="POCLOUD", 
            shortname="SEVIRI_SST_DR-OSISAF-L3C-v1.0",
            version="1.0",
            description="GHRSST L3C hourly Atlantic reprocessed sub-skin sea surface temperature data record v1.0 from SEVIRI on MSG produced by OSISAF version: 1.0"
        )

    VIIRS_NPP_NAVO_L2P_V10_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_VIIRS_NPP-NAVO-L2P-v1.0_1.0",
            provider="POCLOUD", 
            shortname="VIIRS_NPP-NAVO-L2P-v1.0",
            version="1.0",
            description="GHRSST Level 2P 1 m Depth Global Sea Surface Temperature from VIIRS on Suomi NPP (GDS2) V1 version: 1.0"
        )

    VIIRS_NPP_NAVO_L2P_V20_V20_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_VIIRS_NPP-NAVO-L2P-v2.0_2.0",
            provider="POCLOUD", 
            shortname="VIIRS_NPP-NAVO-L2P-v2.0",
            version="2.0",
            description="GHRSST Level 2P 1 m Depth Global Sea Surface Temperature from VIIRS on Suomi NPP (GDS2) V2 version: 2.0"
        )

    VIIRS_NPP_NAVO_L2P_V30_V30_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_VIIRS_NPP-NAVO-L2P-v3.0_3.0",
            provider="POCLOUD", 
            shortname="VIIRS_NPP-NAVO-L2P-v3.0",
            version="3.0",
            description="GHRSST Level 2P 1 m Depth Global Sea Surface Temperature version 3.0 from the Visible Infrared Imaging Radiometer Suite (VIIRS) on the Suomi NPP satellite (GDS2) version: 3.0"
        )

    MSG03_OSPO_L2P_V10_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_MSG03-OSPO-L2P-v1.0_1.0",
            provider="POCLOUD", 
            shortname="MSG03-OSPO-L2P-v1.0",
            version="1.0",
            description="GHRSST Level 2P Atlantic Regional Skin Sea Surface Temperature from the Spinning Enhanced Visible and InfraRed Imager (SEVIRI) on the Meteosat Second Generation (MSG-3) satellite (GDS version 2) version: 1.0"
        )

    GOES15_OSPO_L2P_V10_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_GOES15-OSPO-L2P-v1.0_1.0",
            provider="POCLOUD", 
            shortname="GOES15-OSPO-L2P-v1.0",
            version="1.0",
            description="GHRSST Level 2P Central Pacific Regional Skin Sea Surface Temperature from the Geostationary Operational Environmental Satellites (GOES) Imager on the GOES-15 satellite (GDS version 2) version: 1.0"
        )

    AVHRRMTA_G_NAVO_L2P_V10_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AVHRRMTA_G-NAVO-L2P-v1.0_1.0",
            provider="POCLOUD", 
            shortname="AVHRRMTA_G-NAVO-L2P-v1.0",
            version="1.0",
            description="GHRSST Level 2P Global 1m Sea Surface Temperature from the Advanced Very High Resolution Radiometer (AVHRR) on the MetOp-A satellite produced by NAVO version: 1.0"
        )

    AVHRRMTB_G_NAVO_L2P_V10_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AVHRRMTB_G-NAVO-L2P-v1.0_1.0",
            provider="POCLOUD", 
            shortname="AVHRRMTB_G-NAVO-L2P-v1.0",
            version="1.0",
            description="GHRSST Level 2P Global 1m Sea Surface Temperature from the Advanced Very High Resolution Radiometer (AVHRR) on the MetOp-B satellite produced by NAVO version: 1.0"
        )

    AVHRR18_G_NAVO_L2P_V10_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AVHRR18_G-NAVO-L2P-v1.0_1.0",
            provider="POCLOUD", 
            shortname="AVHRR18_G-NAVO-L2P-v1.0",
            version="1.0",
            description="GHRSST Level 2P Global 1m Sea Surface Temperature from the Advanced Very High Resolution Radiometer (AVHRR) on the NOAA-18 satellite produced by NAVO version: 1.0"
        )

    AVHRR19_G_NAVO_L2P_V10_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AVHRR19_G-NAVO-L2P-v1.0_1",
            provider="POCLOUD", 
            shortname="AVHRR19_G-NAVO-L2P-v1.0",
            version="1",
            description="GHRSST Level 2P Global 1m Sea Surface Temperature from the Advanced Very High Resolution Radiometer (AVHRR) on the NOAA-19 satellite produced by NAVO version: 1"
        )

    AMSR2_REMSS_L2P_RT_V82_V82_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AMSR2-REMSS-L2P_RT-v8.2_8.2",
            provider="POCLOUD", 
            shortname="AMSR2-REMSS-L2P_RT-v8.2",
            version="8.2",
            description="GHRSST Level 2P Global Near-Real-Time Subskin Sea Surface Temperature version 8.2 (v8.2) from the Advanced Microwave Scanning Radiometer 2 (AMSR2) on the GCOM-W satellite by REMSS version: 8.2"
        )

    VIIRS_NPP_JPL_L2P_V20162_V20162_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_VIIRS_NPP-JPL-L2P-v2016.2_2016.2",
            provider="POCLOUD", 
            shortname="VIIRS_NPP-JPL-L2P-v2016.2",
            version="2016.2",
            description="GHRSST Level 2P Global Sea Surface Skin Temperature from the Visible and Infrared Imager/Radiometer Suite (VIIRS) on the Suomi-NPP satellite (GDS2) version: 2016.2"
        )

    MODIS_A_JPL_L2P_V20190_V20190_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_MODIS_A-JPL-L2P-v2019.0_2019.0",
            provider="POCLOUD", 
            shortname="MODIS_A-JPL-L2P-v2019.0",
            version="2019.0",
            description="GHRSST Level 2P Global Sea Surface Skin Temperature from the Moderate Resolution Imaging Spectroradiometer (MODIS) on the NASA Aqua satellite (GDS2) version: 2019.0"
        )

    MODIS_T_JPL_L2P_V20190_V20190_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_MODIS_T-JPL-L2P-v2019.0_2019.0",
            provider="POCLOUD", 
            shortname="MODIS_T-JPL-L2P-v2019.0",
            version="2019.0",
            description="GHRSST Level 2P Global Sea Surface Skin Temperature from the Moderate Resolution Imaging Spectroradiometer (MODIS) on the NASA Terra satellite (GDS2) version: 2019.0"
        )

    AVHRRMTA_G_NAVO_L2P_V20_V20_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AVHRRMTA_G-NAVO-L2P-v2.0_2.0",
            provider="POCLOUD", 
            shortname="AVHRRMTA_G-NAVO-L2P-v2.0",
            version="2.0",
            description="GHRSST Level 2P Global Sea Surface Temperature v2.0 from the AVHRR on the MetOp-A satellite produced by NAVO version: 2.0"
        )

    AVHRRMTB_G_NAVO_L2P_V20_V20_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AVHRRMTB_G-NAVO-L2P-v2.0_2.0",
            provider="POCLOUD", 
            shortname="AVHRRMTB_G-NAVO-L2P-v2.0",
            version="2.0",
            description="GHRSST Level 2P Global Sea Surface Temperature v2.0 from the AVHRR on the MetOp-B satellite produced by NAVO version: 2.0"
        )

    AVHRRMTC_G_NAVO_L2P_V20_V20_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AVHRRMTC_G-NAVO-L2P-v2.0_2.0",
            provider="POCLOUD", 
            shortname="AVHRRMTC_G-NAVO-L2P-v2.0",
            version="2.0",
            description="GHRSST Level 2P Global Sea Surface Temperature v2.0 from the AVHRR on the MetOp-C satellite produced by NAVO version: 2.0"
        )

    TMI_REMSS_L2P_V4_V40_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_TMI-REMSS-L2P-v4_4.0",
            provider="POCLOUD", 
            shortname="TMI-REMSS-L2P-v4",
            version="4.0",
            description="GHRSST Level 2P Global Subskin Sea Surface Temperature from TRMM Microwave Imager (TMI) onboard Tropical Rainfall Measurement Mission (TRMM) satellite version: 4.0"
        )

    AMSRE_REMSS_L2P_V7A_V7A_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AMSRE-REMSS-L2P-v7a_7a",
            provider="POCLOUD", 
            shortname="AMSRE-REMSS-L2P-v7a",
            version="7a",
            description="GHRSST Level 2P Global Subskin Sea Surface Temperature from the Advanced Scanning Microwave Radiometer - Earth Observing System (AMSR-E) on the NASA Aqua Satellite version: 7a"
        )

    AMSR2_REMSS_L2P_V82_V82_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AMSR2-REMSS-L2P-v8.2_8.2",
            provider="POCLOUD", 
            shortname="AMSR2-REMSS-L2P-v8.2",
            version="8.2",
            description="GHRSST Level 2P Global Subskin Sea Surface Temperature version 8.2 (v8.2) from the Advanced Microwave Scanning Radiometer 2 (AMSR2) by REMSS version: 8.2"
        )

    IASI_SST_METOP_A_OSISAF_L2P_V10_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_IASI_SST_METOP_A-OSISAF-L2P-v1.0_1",
            provider="POCLOUD", 
            shortname="IASI_SST_METOP_A-OSISAF-L2P-v1.0",
            version="1",
            description="GHRSST Level 2P Global skin Sea Surface Temperature from the Infrared Atmospheric Sounding Interferometer (IASI) on the Metop-A satellite (GDS V2) produced by OSI SAF version: 1"
        )

    IASI_SST_METOP_B_OSISAF_L2P_V10_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_IASI_SST_METOP_B-OSISAF-L2P-v1.0_1",
            provider="POCLOUD", 
            shortname="IASI_SST_METOP_B-OSISAF-L2P-v1.0",
            version="1",
            description="GHRSST Level 2P Global skin Sea Surface Temperature from the Infrared Atmospheric Sounding Interferometer (IASI) on the Metop-B satellite (GDS V2) produced by OSI SAF version: 1"
        )

    VIIRS_N20_NAVO_L2P_V30_V30_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_VIIRS_N20-NAVO-L2P-v3.0_3.0",
            provider="POCLOUD", 
            shortname="VIIRS_N20-NAVO-L2P-v3.0",
            version="3.0",
            description="GHRSST Level 2P NAVO 1 m Depth Global Sea Surface Temperature version 3.0 from the Visible Infrared Imaging Radiometer Suite (VIIRS) on the NOAA-20 satellite version: 3.0"
        )

    VIIRS_N21_NAVO_L2P_V30_V30_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_VIIRS_N21-NAVO-L2P-v3.0_3.0",
            provider="POCLOUD", 
            shortname="VIIRS_N21-NAVO-L2P-v3.0",
            version="3.0",
            description="GHRSST Level 2P NAVO 1 m Depth Global Sea Surface Temperature version 3.0 from the Visible Infrared Imaging Radiometer Suite (VIIRS) on the NOAA-21 satellite version: 3.0"
        )

    N21_VIIRS_L2P_ACSPO_V280_V280_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_N21-VIIRS-L2P-ACSPO-v2.80_2.80",
            provider="POCLOUD", 
            shortname="N21-VIIRS-L2P-ACSPO-v2.80",
            version="2.80",
            description="GHRSST Level 2P NOAA ACSPO SST v2.80 from VIIRS on NOAA-21 Satellite version: 2.80"
        )

    VIIRS_N20_STAR_L2P_V280_V280_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_VIIRS_N20-STAR-L2P-v2.80_2.80",
            provider="POCLOUD", 
            shortname="VIIRS_N20-STAR-L2P-v2.80",
            version="2.80",
            description="GHRSST Level 2P NOAA STAR SST v2.80 from VIIRS on NOAA-20 Satellite version: 2.80"
        )

    VIIRS_NPP_STAR_L2P_V280_V280_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_VIIRS_NPP-STAR-L2P-v2.80_2.80",
            provider="POCLOUD", 
            shortname="VIIRS_NPP-STAR-L2P-v2.80",
            version="2.80",
            description="GHRSST Level 2P NOAA STAR SST v2.80 from VIIRS on S-NPP Satellite version: 2.80"
        )

    AVHRR19_L_NAVO_L2P_V10_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AVHRR19_L-NAVO-L2P-v1.0_1",
            provider="POCLOUD", 
            shortname="AVHRR19_L-NAVO-L2P-v1.0",
            version="1",
            description="GHRSST Level 2P Regional 1m Sea Surface Temperature from the Advanced Very High Resolution Radiometer (AVHRR) on the NOAA-19 satellite produced by NAVO version: 1"
        )

    EWSG1_NAVO_L2P_V01_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_EWSG1-NAVO-L2P-v01_1.0",
            provider="POCLOUD", 
            shortname="EWSG1-NAVO-L2P-v01",
            version="1.0",
            description="GHRSST Level 2P Sea Surface Temperature version 1.0 from the Electro-Optical Infrared Weather System Geostationary (EWSG1) produced by NAVO version: 1.0"
        )

    GOES13_OSPO_L2P_V10_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_GOES13-OSPO-L2P-v1.0_1.0",
            provider="POCLOUD", 
            shortname="GOES13-OSPO-L2P-v1.0",
            version="1.0",
            description="GHRSST Level 2P Western Atlantic Regional Skin Sea Surface Temperature from the Geostationary Operational Environmental Satellites (GOES) Imager on the GOES-13 satellite (GDS version 2) version: 1.0"
        )

    MTSAT2_OSPO_L2P_V10_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_MTSAT2-OSPO-L2P-v1.0_1.0",
            provider="POCLOUD", 
            shortname="MTSAT2-OSPO-L2P-v1.0",
            version="1.0",
            description="GHRSST Level 2P Western Pacific Regional Skin Sea Surface Temperature from the Multifunctional Transport Satellite 2 (MTSAT-2) (GDS version 2) version: 1.0"
        )

    AVHRR_SST_METOP_A_OSISAF_L2P_V10_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AVHRR_SST_METOP_A-OSISAF-L2P-v1.0_1",
            provider="POCLOUD", 
            shortname="AVHRR_SST_METOP_A-OSISAF-L2P-v1.0",
            version="1",
            description="GHRSST Level 2P sub-skin Sea Surface Temperature from the Advanced Very High Resolution Radiometer (AVHRR) on Metop satellites (currently Metop-A) (GDS V2) produced by OSI SAF version: 1"
        )

    AVHRR_SST_METOP_B_OSISAF_L2P_V10_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AVHRR_SST_METOP_B-OSISAF-L2P-v1.0_1",
            provider="POCLOUD", 
            shortname="AVHRR_SST_METOP_B-OSISAF-L2P-v1.0",
            version="1",
            description="GHRSST Level 2P sub-skin Sea Surface Temperature from the Advanced Very High Resolution Radiometer (AVHRR) on Metop satellites (currently Metop-B) (GDS V2) produced by OSI SAF version: 1"
        )

    SEVIRI_SST_OSISAF_L3C_V10_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SEVIRI_SST-OSISAF-L3C-v1.0_1",
            provider="POCLOUD", 
            shortname="SEVIRI_SST-OSISAF-L3C-v1.0",
            version="1",
            description="GHRSST Level 3C Atlantic sub-skin Sea Surface Temperature from the Spinning Enhanced Visible and Infrared Imager (SEVIRI) on MSG at 0 degree longitude (GDS V2) produced by OSI SAF version: 1"
        )

    SEVIRI_IO_SST_OSISAF_L3C_V10_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SEVIRI_IO_SST-OSISAF-L3C-v1.0_1.0",
            provider="POCLOUD", 
            shortname="SEVIRI_IO_SST-OSISAF-L3C-v1.0",
            version="1.0",
            description="GHRSST Level 3C Indian-Ocean (IO) sub-skin Sea Surface Temperature from the Spinning Enhanced Visible and Infrared Imager (SEVIRI) on MSG in GDS2 format produced by OSISAF version: 1.0"
        )

    AVHRR_SST_METOP_B_NAR_OSISAF_L3C_V10_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AVHRR_SST_METOP_B_NAR-OSISAF-L3C-v1.0_1",
            provider="POCLOUD", 
            shortname="AVHRR_SST_METOP_B_NAR-OSISAF-L3C-v1.0",
            version="1",
            description="GHRSST Level 3C North Atlantic Regional (NAR) subskin Sea Surface Temperature from Metop/AVHRR (GDS V2) produced by OSI SAF version: 1"
        )

    VIIRS_SST_NPP_NAR_OSISAF_L3C_V10_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_VIIRS_SST_NPP_NAR-OSISAF-L3C-v1.0_1",
            provider="POCLOUD", 
            shortname="VIIRS_SST_NPP_NAR-OSISAF-L3C-v1.0",
            version="1",
            description="GHRSST Level 3C North Atlantic Regional (NAR) subskin Sea Surface Temperature from SNPP/VIIRS (GDS V2) produced by OSI SAF version: 1"
        )

    AVHRR_SST_METOP_A_NAR_OSISAF_L3C_V10_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AVHRR_SST_METOP_A_NAR-OSISAF-L3C-v1.0_1",
            provider="POCLOUD", 
            shortname="AVHRR_SST_METOP_A_NAR-OSISAF-L3C-v1.0",
            version="1",
            description="GHRSST Level 3C North Atlantic Regional (NAR) subskin Sea Surface Temperature from SNPP/VIIRS and Metop-A/AVHRR (GDS V2) produced by OSI SAF version: 1"
        )

    AVHRR_SST_NOAA19_NAR_OSISAF_L3C_V10_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AVHRR_SST_NOAA19_NAR-OSISAF-L3C-v1.0_1",
            provider="POCLOUD", 
            shortname="AVHRR_SST_NOAA19_NAR-OSISAF-L3C-v1.0",
            version="1",
            description="GHRSST Level 3C North Atlantic Regional Subskin Sea Surface Temperature from the Advanced Very High Resolution Radiometer (AVHRR) on NOAA-19 (GDS2 version) version: 1"
        )

    GOES13_OSISAF_L3C_V10_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_GOES13-OSISAF-L3C-v1.0_1",
            provider="POCLOUD", 
            shortname="GOES13-OSISAF-L3C-v1.0",
            version="1",
            description="GHRSST Level 3C sub-skin Sea Surface Temperature from the Geostationary Operational Environmental Satellites (GOES 13) Imager in East position (GDS V2) produced by OSI SAF version: 1"
        )

    AMSR2_REMSS_L3U_RT_V82_V82_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AMSR2-REMSS-L3U_RT-v8.2_8.2",
            provider="POCLOUD", 
            shortname="AMSR2-REMSS-L3U_RT-v8.2",
            version="8.2",
            description="GHRSST Level 3U Global Global Near-Real Subskin Sea Surface Temperature version 8.2 (v8.2) from the Advanced Microwave Scanning Radiometer 2 (AMSR2) on the GCOM-W satellite by REMSS version: 8.2"
        )

    AMSR2_REMSS_L3U_RT_V8A_V8A_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AMSR2-REMSS-L3U_RT-v8a_8a",
            provider="POCLOUD", 
            shortname="AMSR2-REMSS-L3U_RT-v8a",
            version="8a",
            description="GHRSST Level 3U Global Near-Real-Time Subskin Sea Surface Temperature version 8a from the Advanced Microwave Scanning Radiometer 2 on the GCOM-W satellite version: 8a"
        )

    GMI_REMSS_L3U_V82A_V82A_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_GMI-REMSS-L3U-v8.2a_8.2a",
            provider="POCLOUD", 
            shortname="GMI-REMSS-L3U-v8.2a",
            version="8.2a",
            description="GHRSST Level 3U Global Subskin Sea Surface Temperature from GMI onboard GPM satellite version: 8.2a"
        )

    TMI_REMSS_L3U_V71A_V71A_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_TMI-REMSS-L3U-v7.1a_7.1a",
            provider="POCLOUD", 
            shortname="TMI-REMSS-L3U-v7.1a",
            version="7.1a",
            description="GHRSST Level 3U Global Subskin Sea Surface Temperature from TMI onboard TRMM satellite version: 7.1a"
        )

    AMSRE_REMSS_L3U_V7A_V7A_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AMSRE-REMSS-L3U-v7a_7a",
            provider="POCLOUD", 
            shortname="AMSRE-REMSS-L3U-v7a",
            version="7a",
            description="GHRSST Level 3U Global Subskin Sea Surface Temperature from the Advanced Scanning Microwave Radiometer - Earth Observing System (AMSR-E) on the NASA Aqua Satellite version: 7a"
        )

    AMSR2_REMSS_L3U_V82_V82_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AMSR2-REMSS-L3U-v8.2_8.2",
            provider="POCLOUD", 
            shortname="AMSR2-REMSS-L3U-v8.2",
            version="8.2",
            description="GHRSST Level 3U Global Subskin Sea Surface Temperature version 8.2 from the Advanced Microwave Scanning Radiometer 2 on the GCOM-W satellite by REMSS version: 8.2"
        )

    AMSR2_REMSS_L3U_V8A_V8A_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AMSR2-REMSS-L3U-v8a_8a",
            provider="POCLOUD", 
            shortname="AMSR2-REMSS-L3U-v8a",
            version="8a",
            description="GHRSST Level 3U Global Subskin Sea Surface Temperature version 8a from the Advanced Microwave Scanning Radiometer 2 on the GCOM-W satellite version: 8a"
        )

    WINDSAT_REMSS_L3U_V701A_V701A_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_WindSat-REMSS-L3U-v7.0.1a_7.0.1a",
            provider="POCLOUD", 
            shortname="WindSat-REMSS-L3U-v7.0.1a",
            version="7.0.1a",
            description="GHRSST Level 3U Global Subskin Sea Surface Temperature version7.0.1a from the WindSat Polarimetric Radiometer on the Coriolis satellite version: 7.0.1a"
        )

    N21_VIIRS_L3U_ACSPO_V280_V280_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_N21-VIIRS-L3U-ACSPO-v2.80_2.80",
            provider="POCLOUD", 
            shortname="N21-VIIRS-L3U-ACSPO-v2.80",
            version="2.80",
            description="GHRSST Level 3U NOAA ACSPO SST v2.80 from VIIRS on NOAA-21 Satellite version: 2.80"
        )

    VIIRS_N20_STAR_L3U_V280_V280_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_VIIRS_N20-STAR-L3U-v2.80_2.80",
            provider="POCLOUD", 
            shortname="VIIRS_N20-STAR-L3U-v2.80",
            version="2.80",
            description="GHRSST Level 3U NOAA STAR SST v2.80 from VIIRS on NOAA-20 Satellite version: 2.80"
        )

    VIIRS_NPP_STAR_L3U_V280_V280_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_VIIRS_NPP-STAR-L3U-v2.80_2.80",
            provider="POCLOUD", 
            shortname="VIIRS_NPP-STAR-L3U-v2.80",
            version="2.80",
            description="GHRSST Level 3U NOAA STAR SST v2.80 from VIIRS on S-NPP Satellite version: 2.80"
        )

    AVHRR_OI_NCEI_L4_GLOB_V20_V20_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AVHRR_OI-NCEI-L4-GLOB-v2.0_2.0",
            provider="POCLOUD", 
            shortname="AVHRR_OI-NCEI-L4-GLOB-v2.0",
            version="2.0",
            description="GHRSST Level 4 AVHRR_OI Global Blended Sea Surface Temperature Analysis (GDS version 2) from NCEI version: 2.0"
        )

    AVHRR_OI_NCEI_L4_GLOB_V21_V21_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AVHRR_OI-NCEI-L4-GLOB-v2.1_2.1",
            provider="POCLOUD", 
            shortname="AVHRR_OI-NCEI-L4-GLOB-v2.1",
            version="2.1",
            description="GHRSST Level 4 AVHRR_OI Global Blended Sea Surface Temperature Analysis (GDS2) from NCEI version: 2.1"
        )

    CMC01DEG_CMC_L4_GLOB_V30_V30_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_CMC0.1deg-CMC-L4-GLOB-v3.0_3.0",
            provider="POCLOUD", 
            shortname="CMC0.1deg-CMC-L4-GLOB-v3.0",
            version="3.0",
            description="GHRSST Level 4 CMC0.1deg Global Foundation Sea Surface Temperature Analysis (GDS version 2) version: 3.0"
        )

    CMC02DEG_CMC_L4_GLOB_V20_V20_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_CMC0.2deg-CMC-L4-GLOB-v2.0_2.0",
            provider="POCLOUD", 
            shortname="CMC0.2deg-CMC-L4-GLOB-v2.0",
            version="2.0",
            description="GHRSST Level 4 CMC0.2deg Global Foundation Sea Surface Temperature Analysis (GDS version 2) version: 2.0"
        )

    DMI_OI_DMI_L4_GLOB_V10_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_DMI_OI-DMI-L4-GLOB-v1.0_1.0",
            provider="POCLOUD", 
            shortname="DMI_OI-DMI-L4-GLOB-v1.0",
            version="1.0",
            description="GHRSST Level 4 DMI_OI Global Foundation Sea Surface Temperature Analysis (GDS version 2) version: 1.0"
        )

    GAMSSA_28KM_ABOM_L4_GLOB_V01_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_GAMSSA_28km-ABOM-L4-GLOB-v01_1.0",
            provider="POCLOUD", 
            shortname="GAMSSA_28km-ABOM-L4-GLOB-v01",
            version="1.0",
            description="GHRSST Level 4 GAMSSA_28km Global Foundation Sea Surface Temperature Analysis v1.0 dataset (GDS2) version: 1.0"
        )

    K10_SST_NAVO_L4_GLOB_V01_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_K10_SST-NAVO-L4-GLOB-v01_1.0",
            provider="POCLOUD", 
            shortname="K10_SST-NAVO-L4-GLOB-v01",
            version="1.0",
            description="GHRSST Level 4 K10_SST Global 10 km Analyzed Sea Surface Temperature from Naval Oceanographic Office (NAVO) in GDS2.0 version: 1.0"
        )

    MUR25_JPL_L4_GLOB_V042_V42_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_MUR25-JPL-L4-GLOB-v04.2_4.2",
            provider="POCLOUD", 
            shortname="MUR25-JPL-L4-GLOB-v04.2",
            version="4.2",
            description="GHRSST Level 4 MUR 0.25deg Global Foundation Sea Surface Temperature Analysis (v4.2) version: 4.2"
        )

    MUR_JPL_L4_GLOB_V41_V41_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_MUR-JPL-L4-GLOB-v4.1_4.1",
            provider="POCLOUD", 
            shortname="MUR-JPL-L4-GLOB-v4.1",
            version="4.1",
            description="GHRSST Level 4 MUR Global Foundation Sea Surface Temperature Analysis (v4.1) version: 4.1"
        )

    MW_IR_OI_REMSS_L4_GLOB_V50_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_MW_IR_OI-REMSS-L4-GLOB-v5.0_5.0",
            provider="POCLOUD", 
            shortname="MW_IR_OI-REMSS-L4-GLOB-v5.0",
            version="5.0",
            description="GHRSST Level 4 MW_IR_OI Global Foundation Sea Surface Temperature analysis version 5.0 from REMSS version: 5.0"
        )

    MW_IR_OI_REMSS_L4_GLOB_V51_V51_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_MW_IR_OI-REMSS-L4-GLOB-v5.1_5.1",
            provider="POCLOUD", 
            shortname="MW_IR_OI-REMSS-L4-GLOB-v5.1",
            version="5.1",
            description="GHRSST Level 4 MW_IR_OI Global Foundation Sea Surface Temperature analysis version 5.1 from REMSS version: 5.1"
        )

    MW_OI_REMSS_L4_GLOB_V50_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_MW_OI-REMSS-L4-GLOB-v5.0_5.0",
            provider="POCLOUD", 
            shortname="MW_OI-REMSS-L4-GLOB-v5.0",
            version="5.0",
            description="GHRSST Level 4 MW_OI Global Foundation Sea Surface Temperature analysis version 5.0 from REMSS version: 5.0"
        )

    MW_OI_REMSS_L4_GLOB_V51_V51_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_MW_OI-REMSS-L4-GLOB-v5.1_5.1",
            provider="POCLOUD", 
            shortname="MW_OI-REMSS-L4-GLOB-v5.1",
            version="5.1",
            description="GHRSST Level 4 MW_OI Global Foundation Sea Surface Temperature analysis version 5.1 from REMSS version: 5.1"
        )

    GEO_POLAR_BLENDED_OSPO_L4_GLOB_V10_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_Geo_Polar_Blended-OSPO-L4-GLOB-v1.0_1.0",
            provider="POCLOUD", 
            shortname="Geo_Polar_Blended-OSPO-L4-GLOB-v1.0",
            version="1.0",
            description="GHRSST Level 4 OSPO Global Foundation Sea Surface Temperature Analysis (GDS version 2) version: 1.0"
        )

    GEO_POLAR_BLENDED_NIGHT_OSPO_L4_GLOB_V10_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_Geo_Polar_Blended_Night-OSPO-L4-GLOB-v1.0_1.0",
            provider="POCLOUD", 
            shortname="Geo_Polar_Blended_Night-OSPO-L4-GLOB-v1.0",
            version="1.0",
            description="GHRSST Level 4 OSPO Global Nighttime Foundation Sea Surface Temperature Analysis (GDS version 2) version: 1.0"
        )

    OSTIA_UKMO_L4_GLOB_V20_V20_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_OSTIA-UKMO-L4-GLOB-v2.0_2.0",
            provider="POCLOUD", 
            shortname="OSTIA-UKMO-L4-GLOB-v2.0",
            version="2.0",
            description="GHRSST Level 4 OSTIA Global Foundation Sea Surface Temperature Analysis (GDS version 2) version: 2.0"
        )

    OSTIA_UKMO_L4_GLOB_REP_V20_V20_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_OSTIA-UKMO-L4-GLOB-REP-v2.0_2.0",
            provider="POCLOUD", 
            shortname="OSTIA-UKMO-L4-GLOB-REP-v2.0",
            version="2.0",
            description="GHRSST Level 4 OSTIA Global Historical Reprocessed Foundation Sea Surface Temperature Analysis produced by the UK Meteorological Office version: 2.0"
        )

    RAMSSA_09KM_ABOM_L4_AUS_V01_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_RAMSSA_09km-ABOM-L4-AUS-v01_1.0",
            provider="POCLOUD", 
            shortname="RAMSSA_09km-ABOM-L4-AUS-v01",
            version="1.0",
            description="GHRSST Level 4 RAMSSA_9km Australian Regional Foundation Sea Surface Temperature Analysis v1.0 dataset (GDS2) version: 1.0"
        )

    REMO_OI_SST_5KM_UFRJ_L4_SAMERICA_V10_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_REMO_OI_SST_5km-UFRJ-L4-SAMERICA-v1.0_1.0",
            provider="POCLOUD", 
            shortname="REMO_OI_SST_5km-UFRJ-L4-SAMERICA-v1.0",
            version="1.0",
            description="GHRSST Level 4 REMO_OI_SST_5km Regional Foundation Sea Surface Temperature Analysis (GDS version 2) version: 1.0"
        )

    L3S_LEO_AM_STAR_V280_V280_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_L3S_LEO_AM-STAR-v2.80_2.80",
            provider="POCLOUD", 
            shortname="L3S_LEO_AM-STAR-v2.80",
            version="2.80",
            description="GHRSST NOAA/STAR ACSPO v2.80 0.02 degree L3S Dataset from mid-Morning LEO Satellites (GDS v2) version: 2.80"
        )

    L3S_LEO_DY_STAR_V281_V281_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_L3S_LEO_DY-STAR-v2.81_2.81",
            provider="POCLOUD", 
            shortname="L3S_LEO_DY-STAR-v2.81",
            version="2.81",
            description="GHRSST NOAA/STAR ACSPO v2.81 0.02 degree L3S Daily Dataset from LEO Satellites version: 2.81"
        )

    L3S_LEO_PM_STAR_V281_V281_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_L3S_LEO_PM-STAR-v2.81_2.81",
            provider="POCLOUD", 
            shortname="L3S_LEO_PM-STAR-v2.81",
            version="2.81",
            description="GHRSST NOAA/STAR ACSPO v2.81 0.02 degree L3S Dataset from Afternoon LEO Satellites version: 2.81"
        )

    ABI_G16_STAR_L3C_V270_V270_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ABI_G16-STAR-L3C-v2.70_2.70",
            provider="POCLOUD", 
            shortname="ABI_G16-STAR-L3C-v2.70",
            version="2.70",
            description="GHRSST NOAA/STAR GOES-16 ABI L3C America Region SST v2.70 dataset in GDS2 version: 2.70"
        )

    ABI_G16_STAR_L2P_V270_V270_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ABI_G16-STAR-L2P-v2.70_2.70",
            provider="POCLOUD", 
            shortname="ABI_G16-STAR-L2P-v2.70",
            version="2.70",
            description="GHRSST NOAA/STAR GOES-16 ABI L2P America Region SST v2.70 dataset in GDS2 version: 2.70"
        )

    ABI_G17_STAR_L3C_V271_V271_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ABI_G17-STAR-L3C-v2.71_2.71",
            provider="POCLOUD", 
            shortname="ABI_G17-STAR-L3C-v2.71",
            version="2.71",
            description="GHRSST NOAA/STAR GOES-17 ABI L3C America Region SST v2.71 dataset in GDS2 version: 2.71"
        )

    ABI_G17_STAR_L2P_V271_V271_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ABI_G17-STAR-L2P-v2.71_2.71",
            provider="POCLOUD", 
            shortname="ABI_G17-STAR-L2P-v2.71",
            version="2.71",
            description="GHRSST NOAA/STAR GOES-17 ABI L2P America Region SST v2.71 dataset in GDS2 version: 2.71"
        )

    AHI_H08_STAR_L2P_V270_V270_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AHI_H08-STAR-L2P-v2.70_2.70",
            provider="POCLOUD", 
            shortname="AHI_H08-STAR-L2P-v2.70",
            version="2.70",
            description="GHRSST NOAA/STAR Himawari-08 AHI L2P Pacific Ocean Region SST v2.70 dataset in GDS2 version: 2.70"
        )

    AHI_H08_STAR_L3C_V270_V270_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AHI_H08-STAR-L3C-v2.70_2.70",
            provider="POCLOUD", 
            shortname="AHI_H08-STAR-L3C-v2.70",
            version="2.70",
            description="GHRSST NOAA/STAR Himawari-08 AHI L3C Pacific Ocean Region SST v2.70 dataset in GDS2 version: 2.70"
        )

    AVHRRF_MA_STAR_L3U_V280_V280_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AVHRRF_MA-STAR-L3U-v2.80_2.80",
            provider="POCLOUD", 
            shortname="AVHRRF_MA-STAR-L3U-v2.80",
            version="2.80",
            description="GHRSST NOAA/STAR Metop-A AVHRR FRAC ACSPO v2.80 0.02 L3U Dataset (GDS v2) version: 2.80"
        )

    AVHRRF_MA_STAR_L2P_V280_V280_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AVHRRF_MA-STAR-L2P-v2.80_2.80",
            provider="POCLOUD", 
            shortname="AVHRRF_MA-STAR-L2P-v2.80",
            version="2.80",
            description="GHRSST NOAA/STAR Metop-A AVHRR FRAC ACSPO v2.80 1km L2P Dataset (GDS v2) version: 2.80"
        )

    AVHRRF_MB_STAR_L3U_V280_V280_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AVHRRF_MB-STAR-L3U-v2.80_2.80",
            provider="POCLOUD", 
            shortname="AVHRRF_MB-STAR-L3U-v2.80",
            version="2.80",
            description="GHRSST NOAA/STAR Metop-B AVHRR FRAC ACSPO v2.80 0.02 L3U Dataset (GDS v2) version: 2.80"
        )

    AVHRRF_MB_STAR_L2P_V280_V280_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AVHRRF_MB-STAR-L2P-v2.80_2.80",
            provider="POCLOUD", 
            shortname="AVHRRF_MB-STAR-L2P-v2.80",
            version="2.80",
            description="GHRSST NOAA/STAR Metop-B AVHRR FRAC ACSPO v2.80 1km L2P Dataset (GDS v2) version: 2.80"
        )

    AVHRRF_MC_STAR_L3U_V280_V280_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AVHRRF_MC-STAR-L3U-v2.80_2.80",
            provider="POCLOUD", 
            shortname="AVHRRF_MC-STAR-L3U-v2.80",
            version="2.80",
            description="GHRSST NOAA/STAR Metop-C AVHRR FRAC ACSPO v2.80 0.02 L3U Dataset (GDS v2) version: 2.80"
        )

    AVHRRF_MC_STAR_L2P_V280_V280_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AVHRRF_MC-STAR-L2P-v2.80_2.80",
            provider="POCLOUD", 
            shortname="AVHRRF_MC-STAR-L2P-v2.80",
            version="2.80",
            description="GHRSST NOAA/STAR Metop-C AVHRR FRAC ACSPO v2.80 1km L2P Dataset (GDS v2) version: 2.80"
        )

    GRACE_AOD1B_GRAV_GFZ_RL06_V60_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_GRACE_AOD1B_GRAV_GFZ_RL06_6.0",
            provider="POCLOUD", 
            shortname="GRACE_AOD1B_GRAV_GFZ_RL06",
            version="6.0",
            description="GRACE ATMOSPHERE AND OCEAN DE-ALIASING GFZ RELEASE 6.0 version: 6.0"
        )

    GRACE_GSM_L2_GRAV_CSR_RL06_V60_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_GRACE_GSM_L2_GRAV_CSR_RL06_6.0",
            provider="POCLOUD", 
            shortname="GRACE_GSM_L2_GRAV_CSR_RL06",
            version="6.0",
            description="GRACE FIELD GEOPOTENTIAL COEFFICIENTS CSR RELEASE 6.0 version: 6.0"
        )

    GRACE_GSM_L2_GRAV_GFZ_RL06_V60_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_GRACE_GSM_L2_GRAV_GFZ_RL06_6.0",
            provider="POCLOUD", 
            shortname="GRACE_GSM_L2_GRAV_GFZ_RL06",
            version="6.0",
            description="GRACE FIELD GEOPOTENTIAL COEFFICIENTS GFZ RELEASE 6.0 version: 6.0"
        )

    GRACE_GSM_L2_GRAV_JPL_RL06_V60_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_GRACE_GSM_L2_GRAV_JPL_RL06_6.0",
            provider="POCLOUD", 
            shortname="GRACE_GSM_L2_GRAV_JPL_RL06",
            version="6.0",
            description="GRACE FIELD GEOPOTENTIAL COEFFICIENTS JPL RELEASE 6.0 version: 6.0"
        )

    GRACE_L1B_GRAV_JPL_RL02_V2_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_GRACE_L1B_GRAV_JPL_RL02_2",
            provider="POCLOUD", 
            shortname="GRACE_L1B_GRAV_JPL_RL02",
            version="2",
            description="GRACE LEVEL 1B JPL RELEASE 2.0 version: 2"
        )

    GRACE_L1B_GRAV_JPL_RL03_V3_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_GRACE_L1B_GRAV_JPL_RL03_3",
            provider="POCLOUD", 
            shortname="GRACE_L1B_GRAV_JPL_RL03",
            version="3",
            description="GRACE LEVEL 1B JPL RELEASE 3.0 version: 3"
        )

    GRACE_GAC_L2_GRAV_CSR_RL06_V60_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_GRACE_GAC_L2_GRAV_CSR_RL06_6.0",
            provider="POCLOUD", 
            shortname="GRACE_GAC_L2_GRAV_CSR_RL06",
            version="6.0",
            description="GRACE NON-TIDAL ATMOSPHERE AND OCEAN GEOPOTENTIAL COEFFICIENTS CSR RELEASE 6.0 GAC version: 6.0"
        )

    GRACE_GAC_L2_GRAV_GFZ_RL06_V60_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_GRACE_GAC_L2_GRAV_GFZ_RL06_6.0",
            provider="POCLOUD", 
            shortname="GRACE_GAC_L2_GRAV_GFZ_RL06",
            version="6.0",
            description="GRACE NON-TIDAL ATMOSPHERE AND OCEAN GEOPOTENTIAL COEFFICIENTS GFZ RELEASE 6.0 GAC version: 6.0"
        )

    GRACE_GAC_L2_GRAV_JPL_RL06_V60_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_GRACE_GAC_L2_GRAV_JPL_RL06_6.0",
            provider="POCLOUD", 
            shortname="GRACE_GAC_L2_GRAV_JPL_RL06",
            version="6.0",
            description="GRACE NON-TIDAL ATMOSPHERE AND OCEAN GEOPOTENTIAL COEFFICIENTS JPL RELEASE 6.0 GAC version: 6.0"
        )

    GRACE_GAA_L2_GRAV_GFZ_RL06_V60_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_GRACE_GAA_L2_GRAV_GFZ_RL06_6.0",
            provider="POCLOUD", 
            shortname="GRACE_GAA_L2_GRAV_GFZ_RL06",
            version="6.0",
            description="GRACE NON-TIDAL ATMOSPHERE GEOPOTENTIAL COEFFICIENTS GFZ RELEASE 6.0 GAA version: 6.0"
        )

    GRACE_GAA_L2_GRAV_JPL_RL06_V60_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_GRACE_GAA_L2_GRAV_JPL_RL06_6.0",
            provider="POCLOUD", 
            shortname="GRACE_GAA_L2_GRAV_JPL_RL06",
            version="6.0",
            description="GRACE NON-TIDAL ATMOSPHERE GEOPOTENTIAL COEFFICIENTS JPL RELEASE 6.0 GAA version: 6.0"
        )

    GRACE_GAB_L2_GRAV_GFZ_RL06_V60_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_GRACE_GAB_L2_GRAV_GFZ_RL06_6.0",
            provider="POCLOUD", 
            shortname="GRACE_GAB_L2_GRAV_GFZ_RL06",
            version="6.0",
            description="GRACE NON-TIDAL OCEAN GEOPOTENTIAL COEFFICIENTS GFZ RELEASE 6.0 GAB version: 6.0"
        )

    GRACE_GAB_L2_GRAV_JPL_RL06_V60_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_GRACE_GAB_L2_GRAV_JPL_RL06_6.0",
            provider="POCLOUD", 
            shortname="GRACE_GAB_L2_GRAV_JPL_RL06",
            version="6.0",
            description="GRACE NON-TIDAL OCEAN GEOPOTENTIAL COEFFICIENTS JPL RELEASE 6.0 GAB version: 6.0"
        )

    GRACE_GAD_L2_GRAV_CSR_RL06_V60_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_GRACE_GAD_L2_GRAV_CSR_RL06_6.0",
            provider="POCLOUD", 
            shortname="GRACE_GAD_L2_GRAV_CSR_RL06",
            version="6.0",
            description="GRACE OCEAN BOTTOM GEOPOTENTIAL COEFFICIENTS CSR RELEASE 6.0 GAD version: 6.0"
        )

    GRACE_GAD_L2_GRAV_GFZ_RL06_V60_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_GRACE_GAD_L2_GRAV_GFZ_RL06_6.0",
            provider="POCLOUD", 
            shortname="GRACE_GAD_L2_GRAV_GFZ_RL06",
            version="6.0",
            description="GRACE OCEAN BOTTOM GEOPOTENTIAL COEFFICIENTS GFZ RELEASE 6.0 GAD version: 6.0"
        )

    GRACE_GAD_L2_GRAV_JPL_RL06_V60_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_GRACE_GAD_L2_GRAV_JPL_RL06_6.0",
            provider="POCLOUD", 
            shortname="GRACE_GAD_L2_GRAV_JPL_RL06",
            version="6.0",
            description="GRACE OCEAN BOTTOM GEOPOTENTIAL COEFFICIENTS JPL RELEASE 6.0 GAD version: 6.0"
        )

    GRACEFO_L1A_ASCII_GRAV_JPL_RL04_V4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_GRACEFO_L1A_ASCII_GRAV_JPL_RL04_4",
            provider="POCLOUD", 
            shortname="GRACEFO_L1A_ASCII_GRAV_JPL_RL04",
            version="4",
            description="GRACE-FO Level-1A Release version 4.0 from JPL in ASCII version: 4"
        )

    GRACEFO_L1B_ASCII_GRAV_JPL_RL04_V4_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_GRACEFO_L1B_ASCII_GRAV_JPL_RL04_4",
            provider="POCLOUD", 
            shortname="GRACEFO_L1B_ASCII_GRAV_JPL_RL04",
            version="4",
            description="GRACE-FO Level-1B Release version 4.0 from JPL in ASCII version: 4"
        )

    GRACEFO_L2_JPL_MONTHLY_0063_V63_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_GRACEFO_L2_JPL_MONTHLY_0063_6.3",
            provider="POCLOUD", 
            shortname="GRACEFO_L2_JPL_MONTHLY_0063",
            version="6.3",
            description="GRACE-FO Level-2 Monthly Geopotential Spherical Harmonics JPL Release 6.3 (RL06.3) version: 6.3"
        )

    GRACEFO_L2_CSR_MONTHLY_0063_V63_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_GRACEFO_L2_CSR_MONTHLY_0063_6.3",
            provider="POCLOUD", 
            shortname="GRACEFO_L2_CSR_MONTHLY_0063",
            version="6.3",
            description="GRACE-FO Level-2 Monthly Geopotential Spherical Harmonics CSR Release 06.3 (RL06.3) version: 6.3"
        )

    GRACEFO_L2_GFZ_MONTHLY_0063_V63_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_GRACEFO_L2_GFZ_MONTHLY_0063_6.3",
            provider="POCLOUD", 
            shortname="GRACEFO_L2_GFZ_MONTHLY_0063",
            version="6.3",
            description="GRACE-FO Level-2 Monthly Geopotential Spherical Harmonics GFZ Release 6.3 (RL06.3) version: 6.3"
        )

    HOMAGE_GGFO_L4_GOMA_MONTHLY_V01_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_HOMAGE_GGFO_L4_GOMA_Monthly_v01_1.0",
            provider="POCLOUD", 
            shortname="HOMAGE_GGFO_L4_GOMA_Monthly_v01",
            version="1.0",
            description="GRACE/GRACE-FO Level-4 Monthly Global Ocean Mass Anomaly version 01 from NASA MEaSUREs HOMaGE project version: 1.0"
        )

    MERGED_TP_J1_OSTM_OST_GMSL_ASCII_V51_V51_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_MERGED_TP_J1_OSTM_OST_GMSL_ASCII_V51_5.1",
            provider="POCLOUD", 
            shortname="MERGED_TP_J1_OSTM_OST_GMSL_ASCII_V51",
            version="5.1",
            description="Global Mean Sea Level Trend from Integrated Multi-Mission Ocean Altimeters TOPEX/Poseidon, Jason-1, OSTM/Jason-2, and Jason-3 Version 5.1 version: 5.1"
        )

    MITGCM_LLC4320_PRE_SWOT_JPL_L4_GOTLANDBASIN_V10_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_MITgcm_LLC4320_Pre-SWOT_JPL_L4_GotlandBasin_v1.0_1.0",
            provider="POCLOUD", 
            shortname="MITgcm_LLC4320_Pre-SWOT_JPL_L4_GotlandBasin_v1.0",
            version="1.0",
            description="Gotland Basin Pre-SWOT Level-4 Hourly MITgcm LLC4320 Native Grid 2km Oceanographic Dataset Version 1.0 version: 1.0"
        )

    ALT_TIDE_GAUGE_L4_OST_SLA_US_WEST_COAST_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ALT_TIDE_GAUGE_L4_OST_SLA_US_WEST_COAST_1",
            provider="POCLOUD", 
            shortname="ALT_TIDE_GAUGE_L4_OST_SLA_US_WEST_COAST",
            version="1",
            description="Gridded Altimeter Fields with Enhanced Coastal Coverage version: 1"
        )

    ALT_TIDE_GAUGE_L4_OST_SLA_US_WEST_COAST_DAILY_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ALT_TIDE_GAUGE_L4_OST_SLA_US_WEST_COAST_DAILY_1",
            provider="POCLOUD", 
            shortname="ALT_TIDE_GAUGE_L4_OST_SLA_US_WEST_COAST_DAILY",
            version="1",
            description="Gridded Altimeter Fields with Enhanced Coastal Coverage Daily version: 1"
        )

    HOMAGE_STERIC_OHC_TIME_SERIES_V01_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_HOMAGE_STERIC_OHC_TIME_SERIES_v01_1.0",
            provider="POCLOUD", 
            shortname="HOMAGE_STERIC_OHC_TIME_SERIES_v01",
            version="1.0",
            description="HOMAGE Monthly Time series of global average steric height anomalies and ocean heat content estimates from gridded in-situ ocean observations version 01 version: 1.0"
        )

    BAROCLINIC_HRET14_V14_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_BAROCLINIC_HRET14_14",
            provider="POCLOUD", 
            shortname="BAROCLINIC_HRET14",
            version="14",
            description="Harmonic Constants for Baroclinic Tide Prediction version: 14"
        )

    GRACE_ABPR_FO_L2_V10_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_GRACE_ABPR_FO_L2_V1.0_1.0",
            provider="POCLOUD", 
            shortname="GRACE_ABPR_FO_L2_V1.0",
            version="1.0",
            description="Hourly Ocean Bottom Pressure at the North Pole from the Arctic Bottom Pressure Recorder Follow On Version 1.0 version: 1.0"
        )

    AQUARIUS_L4_OISSS_IPRC_7DAY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_AQUARIUS_L4_OISSS_IPRC_7DAY_V5_5.0",
            provider="POCLOUD", 
            shortname="AQUARIUS_L4_OISSS_IPRC_7DAY_V5",
            version="5.0",
            description="IPRC/SOEST Aquarius V5.0 Optimally Interpolated Sea Surface Salinity 7-Day global Dataset version: 5.0"
        )

    MERGED_TP_J1_OSTM_OST_CYCLES_V52_V52_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_MERGED_TP_J1_OSTM_OST_CYCLES_V52_5.2",
            provider="POCLOUD", 
            shortname="MERGED_TP_J1_OSTM_OST_CYCLES_V52",
            version="5.2",
            description="Integrated Multi-Mission Ocean Altimeter Data for Climate Research Version 5.2 version: 5.2"
        )

    MERGED_TP_J1_OSTM_OST_ALL_V52_V52_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_MERGED_TP_J1_OSTM_OST_ALL_V52_5.2",
            provider="POCLOUD", 
            shortname="MERGED_TP_J1_OSTM_OST_ALL_V52",
            version="5.2",
            description="Integrated Multi-Mission Ocean Altimeter Data for Climate Research complete time series Version 5.2 version: 5.2"
        )

    JASON_1_JMR_ENH_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_JASON-1_JMR_ENH_1",
            provider="POCLOUD", 
            shortname="JASON-1_JMR_ENH",
            version="1",
            description="JASON-1 ENHANCED JASON MICROWAVE RADIOMETER version: 1"
        )

    TELLUS_GRAC_GRFO_MASCON_CRI_GRID_RL063_V4_VRL063MV04_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_TELLUS_GRAC-GRFO_MASCON_CRI_GRID_RL06.3_V4_RL06.3Mv04",
            provider="POCLOUD", 
            shortname="TELLUS_GRAC-GRFO_MASCON_CRI_GRID_RL06.3_V4",
            version="RL06.3Mv04",
            description="JPL GRACE and GRACE-FO Mascon Ocean, Ice, and Hydrology Equivalent Water Height Coastal Resolution Improvement (CRI) Filtered Release 06.3 Version 04 version: RL06.3Mv04"
        )

    TELLUS_GRAC_GRFO_MASCON_GRID_RL063_V4_VRL063MV04_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_TELLUS_GRAC-GRFO_MASCON_GRID_RL06.3_V4_RL06.3Mv04",
            provider="POCLOUD", 
            shortname="TELLUS_GRAC-GRFO_MASCON_GRID_RL06.3_V4",
            version="RL06.3Mv04",
            description="JPL GRACE and GRACE-FO Mascon Ocean, Ice, and Hydrology Equivalent Water Height JPL Release 06.3 Version 04 version: RL06.3Mv04"
        )

    GRC_GFO_GRIDDED_AOD1B_JPL_1_DEG_RL06_VRL06_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_GRC-GFO_GRIDDED_AOD1B_JPL_1-DEG_RL06_RL06",
            provider="POCLOUD", 
            shortname="GRC-GFO_GRIDDED_AOD1B_JPL_1-DEG_RL06",
            version="RL06",
            description="JPL GRACE/GRACE-FO Gridded-AOD1B Water-Equivalent-Thickness Surface-Mass Anomaly RL06 dataset for Tellus Level-3 1.0-degree grid version: RL06"
        )

    GRC_GFO_GRIDDED_AOD1B_JPL_MASCON_RL06_VRL06_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_GRC-GFO_GRIDDED_AOD1B_JPL_MASCON_RL06_RL06",
            provider="POCLOUD", 
            shortname="GRC-GFO_GRIDDED_AOD1B_JPL_MASCON_RL06",
            version="RL06",
            description="JPL GRACE/GRACE-FO Gridded-AOD1B Water-Equivalent-Thickness Surface-Mass Anomaly RL06 dataset for Tellus Level-3 mascon 0.5-degree grid version: RL06"
        )

    GRC_GFO_GRIDDED_AOD1B_JPL_1_DEG_RL063_VRL063_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_GRC-GFO_GRIDDED_AOD1B_JPL_1-DEG_RL06.3_RL06.3",
            provider="POCLOUD", 
            shortname="GRC-GFO_GRIDDED_AOD1B_JPL_1-DEG_RL06.3",
            version="RL06.3",
            description="JPL GRACE/GRACE-FO Gridded-AOD1B Water-Equivalent-Thickness Surface-Mass Anomaly RL06.3 dataset for Tellus Level-3 1.0-degree grid version: RL06.3"
        )

    GRC_GFO_GRIDDED_AOD1B_JPL_MASCON_RL063_VRL063_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_GRC-GFO_GRIDDED_AOD1B_JPL_MASCON_RL06.3_RL06.3",
            provider="POCLOUD", 
            shortname="GRC-GFO_GRIDDED_AOD1B_JPL_MASCON_RL06.3",
            version="RL06.3",
            description="JPL GRACE/GRACE-FO Gridded-AOD1B Water-Equivalent-Thickness Surface-Mass Anomaly RL06.3 dataset for Tellus Level-3 mascon 0.5-degree grid version: RL06.3"
        )

    SMAP_JPL_L2B_SSS_CAP_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SMAP_JPL_L2B_SSS_CAP_V5_5.0",
            provider="POCLOUD", 
            shortname="SMAP_JPL_L2B_SSS_CAP_V5",
            version="5.0",
            description="JPL SMAP Level 2B CAP Sea Surface Salinity V5.0 Validated Dataset version: 5.0"
        )

    SMAP_JPL_L2B_NRT_SSS_CAP_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SMAP_JPL_L2B_NRT_SSS_CAP_V5_5.0",
            provider="POCLOUD", 
            shortname="SMAP_JPL_L2B_NRT_SSS_CAP_V5",
            version="5.0",
            description="JPL SMAP Level 2B Near Real-time CAP Sea Surface Salinity V5.0 Validated Dataset version: 5.0"
        )

    SMAP_JPL_L2B_NRT2_SSS_CAP_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SMAP_JPL_L2B_NRT2_SSS_CAP_V5_5.0",
            provider="POCLOUD", 
            shortname="SMAP_JPL_L2B_NRT2_SSS_CAP_V5",
            version="5.0",
            description="JPL SMAP Level 2B Near Real-time CAP Sea Surface Salinity V5.0 Validated Dataset (2 hour latency) version: 5.0"
        )

    SMAP_JPL_L3_SSS_CAP_8DAY_RUNNINGMEAN_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SMAP_JPL_L3_SSS_CAP_8DAY-RUNNINGMEAN_V5_5.0",
            provider="POCLOUD", 
            shortname="SMAP_JPL_L3_SSS_CAP_8DAY-RUNNINGMEAN_V5",
            version="5.0",
            description="JPL SMAP Level 3 CAP Sea Surface Salinity Standard Mapped Image 8-Day Running Mean V5.0 Validated Dataset version: 5.0"
        )

    SMAP_JPL_L3_SSS_CAP_MONTHLY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SMAP_JPL_L3_SSS_CAP_MONTHLY_V5_5.0",
            provider="POCLOUD", 
            shortname="SMAP_JPL_L3_SSS_CAP_MONTHLY_V5",
            version="5.0",
            description="JPL SMAP Level 3 CAP Sea Surface Salinity Standard Mapped Image Monthly V5.0 Validated Dataset version: 5.0"
        )

    TELLUS_GRAC_L3_JPL_RL06_LND_V04_VRL06V04_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_TELLUS_GRAC_L3_JPL_RL06_LND_v04_RL06v04",
            provider="POCLOUD", 
            shortname="TELLUS_GRAC_L3_JPL_RL06_LND_v04",
            version="RL06v04",
            description="JPL TELLUS GRACE Level-3 Monthly Land Water-Equivalent-Thickness Surface Mass Anomaly Release 6.0 version 04 version: RL06v04"
        )

    TELLUS_GRAC_L3_JPL_RL06_OCN_V04_VRL06V04_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_TELLUS_GRAC_L3_JPL_RL06_OCN_v04_RL06v04",
            provider="POCLOUD", 
            shortname="TELLUS_GRAC_L3_JPL_RL06_OCN_v04",
            version="RL06v04",
            description="JPL TELLUS GRACE Level-3 Monthly Ocean Bottom Pressure Anomaly Release 6.0 version 04 version: RL06v04"
        )

    TELLUS_GRFO_L3_JPL_RL063_LND_V04_VRL063V04_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_TELLUS_GRFO_L3_JPL_RL06.3_LND_v04_RL06.3v04",
            provider="POCLOUD", 
            shortname="TELLUS_GRFO_L3_JPL_RL06.3_LND_v04",
            version="RL06.3v04",
            description="JPL TELLUS GRACE-FO Level-3 Monthly Land Water-Equivalent-Thickness Surface Mass Anomaly Release 6.3 version 04 version: RL06.3v04"
        )

    TELLUS_GRFO_L3_JPL_RL063_OCN_V04_VRL063V04_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_TELLUS_GRFO_L3_JPL_RL06.3_OCN_v04_RL06.3v04",
            provider="POCLOUD", 
            shortname="TELLUS_GRFO_L3_JPL_RL06.3_OCN_v04",
            version="RL06.3v04",
            description="JPL TELLUS GRACE-FO Level-3 Monthly Ocean Bottom Pressure Anomaly Release 6.3 version 04 version: RL06.3v04"
        )

    JASON_1_L2_OST_GPR_E_VE_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_JASON-1_L2_OST_GPR_E_E",
            provider="POCLOUD", 
            shortname="JASON-1_L2_OST_GPR_E",
            version="E",
            description="Jason-1 GDR SSHA version E NetCDF version: E"
        )

    JASON_1_L2_OST_GPR_E_GEODETIC_VE_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_JASON-1_L2_OST_GPR_E_GEODETIC_E",
            provider="POCLOUD", 
            shortname="JASON-1_L2_OST_GPR_E_GEODETIC",
            version="E",
            description="Jason-1 GDR SSHA version E NetCDF Geodetic version: E"
        )

    JASON_1_L2_OST_GPN_E_VE_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_JASON-1_L2_OST_GPN_E_E",
            provider="POCLOUD", 
            shortname="JASON-1_L2_OST_GPN_E",
            version="E",
            description="Jason-1 GDR version E NetCDF version: E"
        )

    JASON_1_L2_OST_GPN_E_GEODETIC_VE_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_JASON-1_L2_OST_GPN_E_GEODETIC_E",
            provider="POCLOUD", 
            shortname="JASON-1_L2_OST_GPN_E_GEODETIC",
            version="E",
            description="Jason-1 GDR version E NetCDF Geodetic version: E"
        )

    JASON_1_L2_OST_GPS_E_VE_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_JASON-1_L2_OST_GPS_E_E",
            provider="POCLOUD", 
            shortname="JASON-1_L2_OST_GPS_E",
            version="E",
            description="Jason-1 SGDR version E NetCDF version: E"
        )

    JASON_1_L2_OST_GPS_E_GEODETIC_VE_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_JASON-1_L2_OST_GPS_E_GEODETIC_E",
            provider="POCLOUD", 
            shortname="JASON-1_L2_OST_GPS_E_GEODETIC",
            version="E",
            description="Jason-1 SGDR version E NetCDF Geodetic version: E"
        )

    JASON_3_L2_OST_OGDR_GPS_VF_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_JASON_3_L2_OST_OGDR_GPS_F",
            provider="POCLOUD", 
            shortname="JASON_3_L2_OST_OGDR_GPS",
            version="F",
            description="Jason-3 GPS based orbit and SSHA OGDR version: F"
        )

    JASON_3_PD_CORRECTION_VF_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_JASON_3_PD_CORRECTION_F",
            provider="POCLOUD", 
            shortname="JASON_3_PD_CORRECTION",
            version="F",
            description="Jason-3 Wet Path Delay Correction version: F"
        )

    MITGCM_LLC4320_PRE_SWOT_JPL_L4_LABRADORSEA_V10_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_MITgcm_LLC4320_Pre-SWOT_JPL_L4_LabradorSea_v1.0_1.0",
            provider="POCLOUD", 
            shortname="MITgcm_LLC4320_Pre-SWOT_JPL_L4_LabradorSea_v1.0",
            version="1.0",
            description="Labrador Sea Pre-SWOT Level-4 Hourly MITgcm LLC4320 Native Grid 2km Oceanographic Dataset Version 1.0 version: 1.0"
        )

    SEA_SURFACE_HEIGHT_ALT_GRIDS_L4_2SATS_5DAY_6THDEG_V_JPL2205_V2205_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SEA_SURFACE_HEIGHT_ALT_GRIDS_L4_2SATS_5DAY_6THDEG_V_JPL2205_2205",
            provider="POCLOUD", 
            shortname="SEA_SURFACE_HEIGHT_ALT_GRIDS_L4_2SATS_5DAY_6THDEG_V_JPL2205",
            version="2205",
            description="MEaSUREs Gridded Sea Surface Height Anomalies Version 2205 version: 2205"
        )

    MODIS_AQUA_L3_SST_MID_IR_8DAY_4KM_NIGHTTIME_V20190_V20190_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_MODIS_AQUA_L3_SST_MID-IR_8DAY_4KM_NIGHTTIME_V2019.0_2019.0",
            provider="POCLOUD", 
            shortname="MODIS_AQUA_L3_SST_MID-IR_8DAY_4KM_NIGHTTIME_V2019.0",
            version="2019.0",
            description="MODIS Aqua Level 3 SST MID-IR 8 Day 4km Nighttime V2019.0 version: 2019.0"
        )

    MODIS_AQUA_L3_SST_MID_IR_8DAY_9KM_NIGHTTIME_V20190_V20190_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_MODIS_AQUA_L3_SST_MID-IR_8DAY_9KM_NIGHTTIME_V2019.0_2019.0",
            provider="POCLOUD", 
            shortname="MODIS_AQUA_L3_SST_MID-IR_8DAY_9KM_NIGHTTIME_V2019.0",
            version="2019.0",
            description="MODIS Aqua Level 3 SST MID-IR 8 Day 9km Nighttime V2019.0 version: 2019.0"
        )

    MODIS_AQUA_L3_SST_MID_IR_ANNUAL_4KM_NIGHTTIME_V20190_V20190_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_MODIS_AQUA_L3_SST_MID-IR_ANNUAL_4KM_NIGHTTIME_V2019.0_2019.0",
            provider="POCLOUD", 
            shortname="MODIS_AQUA_L3_SST_MID-IR_ANNUAL_4KM_NIGHTTIME_V2019.0",
            version="2019.0",
            description="MODIS Aqua Level 3 SST MID-IR Annual 4km Nighttime V2019.0 version: 2019.0"
        )

    MODIS_AQUA_L3_SST_MID_IR_ANNUAL_9KM_NIGHTTIME_V20190_V20190_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_MODIS_AQUA_L3_SST_MID-IR_ANNUAL_9KM_NIGHTTIME_V2019.0_2019.0",
            provider="POCLOUD", 
            shortname="MODIS_AQUA_L3_SST_MID-IR_ANNUAL_9KM_NIGHTTIME_V2019.0",
            version="2019.0",
            description="MODIS Aqua Level 3 SST MID-IR Annual 9km Nighttime V2019.0 version: 2019.0"
        )

    MODIS_AQUA_L3_SST_MID_IR_DAILY_4KM_NIGHTTIME_V20190_V20190_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_MODIS_AQUA_L3_SST_MID-IR_DAILY_4KM_NIGHTTIME_V2019.0_2019.0",
            provider="POCLOUD", 
            shortname="MODIS_AQUA_L3_SST_MID-IR_DAILY_4KM_NIGHTTIME_V2019.0",
            version="2019.0",
            description="MODIS Aqua Level 3 SST MID-IR Daily 4km Nighttime V2019.0 version: 2019.0"
        )

    MODIS_AQUA_L3_SST_MID_IR_DAILY_9KM_NIGHTTIME_V20190_V20190_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_MODIS_AQUA_L3_SST_MID-IR_DAILY_9KM_NIGHTTIME_V2019.0_2019.0",
            provider="POCLOUD", 
            shortname="MODIS_AQUA_L3_SST_MID-IR_DAILY_9KM_NIGHTTIME_V2019.0",
            version="2019.0",
            description="MODIS Aqua Level 3 SST MID-IR Daily 9km Nighttime V2019.0 version: 2019.0"
        )

    MODIS_AQUA_L3_SST_MID_IR_MONTHLY_4KM_NIGHTTIME_V20190_V20190_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_MODIS_AQUA_L3_SST_MID-IR_MONTHLY_4KM_NIGHTTIME_V2019.0_2019.0",
            provider="POCLOUD", 
            shortname="MODIS_AQUA_L3_SST_MID-IR_MONTHLY_4KM_NIGHTTIME_V2019.0",
            version="2019.0",
            description="MODIS Aqua Level 3 SST MID-IR Monthly 4km Nighttime V2019.0 version: 2019.0"
        )

    MODIS_AQUA_L3_SST_MID_IR_MONTHLY_9KM_NIGHTTIME_V20190_V20190_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_MODIS_AQUA_L3_SST_MID-IR_MONTHLY_9KM_NIGHTTIME_V2019.0_2019.0",
            provider="POCLOUD", 
            shortname="MODIS_AQUA_L3_SST_MID-IR_MONTHLY_9KM_NIGHTTIME_V2019.0",
            version="2019.0",
            description="MODIS Aqua Level 3 SST MID-IR Monthly 9km Nighttime V2019.0 version: 2019.0"
        )

    MODIS_AQUA_L3_SST_THERMAL_DAILY_4KM_DAYTIME_V20190_V20190_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_MODIS_AQUA_L3_SST_THERMAL_DAILY_4KM_DAYTIME_V2019.0_2019.0",
            provider="POCLOUD", 
            shortname="MODIS_AQUA_L3_SST_THERMAL_DAILY_4KM_DAYTIME_V2019.0",
            version="2019.0",
            description="MODIS Aqua Level 3 SST Thermal IR Daily 4km Daytime V2019.0 version: 2019.0"
        )

    MODIS_AQUA_L3_SST_THERMAL_8DAY_4KM_DAYTIME_V20190_V20190_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_MODIS_AQUA_L3_SST_THERMAL_8DAY_4KM_DAYTIME_V2019.0_2019.0",
            provider="POCLOUD", 
            shortname="MODIS_AQUA_L3_SST_THERMAL_8DAY_4KM_DAYTIME_V2019.0",
            version="2019.0",
            description="MODIS Aqua Level 3 SST Thermal IR 8 Day 4km Daytime V2019.0 version: 2019.0"
        )

    MODIS_AQUA_L3_SST_THERMAL_8DAY_4KM_NIGHTTIME_V20190_V20190_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_MODIS_AQUA_L3_SST_THERMAL_8DAY_4KM_NIGHTTIME_V2019.0_2019.0",
            provider="POCLOUD", 
            shortname="MODIS_AQUA_L3_SST_THERMAL_8DAY_4KM_NIGHTTIME_V2019.0",
            version="2019.0",
            description="MODIS Aqua Level 3 SST Thermal IR 8 Day 4km Nighttime V2019.0 version: 2019.0"
        )

    MODIS_AQUA_L3_SST_THERMAL_8DAY_9KM_DAYTIME_V20190_V20190_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_MODIS_AQUA_L3_SST_THERMAL_8DAY_9KM_DAYTIME_V2019.0_2019.0",
            provider="POCLOUD", 
            shortname="MODIS_AQUA_L3_SST_THERMAL_8DAY_9KM_DAYTIME_V2019.0",
            version="2019.0",
            description="MODIS Aqua Level 3 SST Thermal IR 8 Day 9km Daytime V2019.0 version: 2019.0"
        )

    MODIS_AQUA_L3_SST_THERMAL_8DAY_9KM_NIGHTTIME_V20190_V20190_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_MODIS_AQUA_L3_SST_THERMAL_8DAY_9KM_NIGHTTIME_V2019.0_2019.0",
            provider="POCLOUD", 
            shortname="MODIS_AQUA_L3_SST_THERMAL_8DAY_9KM_NIGHTTIME_V2019.0",
            version="2019.0",
            description="MODIS Aqua Level 3 SST Thermal IR 8 Day 9km Nighttime V2019.0 version: 2019.0"
        )

    MODIS_AQUA_L3_SST_THERMAL_ANNUAL_4KM_DAYTIME_V20190_V20190_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_MODIS_AQUA_L3_SST_THERMAL_ANNUAL_4KM_DAYTIME_V2019.0_2019.0",
            provider="POCLOUD", 
            shortname="MODIS_AQUA_L3_SST_THERMAL_ANNUAL_4KM_DAYTIME_V2019.0",
            version="2019.0",
            description="MODIS Aqua Level 3 SST Thermal IR Annual 4km Daytime V2019.0 version: 2019.0"
        )

    MODIS_AQUA_L3_SST_THERMAL_ANNUAL_4KM_NIGHTTIME_V20190_V20190_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_MODIS_AQUA_L3_SST_THERMAL_ANNUAL_4KM_NIGHTTIME_V2019.0_2019.0",
            provider="POCLOUD", 
            shortname="MODIS_AQUA_L3_SST_THERMAL_ANNUAL_4KM_NIGHTTIME_V2019.0",
            version="2019.0",
            description="MODIS Aqua Level 3 SST Thermal IR Annual 4km Nighttime V2019.0 version: 2019.0"
        )

    MODIS_AQUA_L3_SST_THERMAL_ANNUAL_9KM_DAYTIME_V20190_V20190_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_MODIS_AQUA_L3_SST_THERMAL_ANNUAL_9KM_DAYTIME_V2019.0_2019.0",
            provider="POCLOUD", 
            shortname="MODIS_AQUA_L3_SST_THERMAL_ANNUAL_9KM_DAYTIME_V2019.0",
            version="2019.0",
            description="MODIS Aqua Level 3 SST Thermal IR Annual 9km Daytime V2019.0 version: 2019.0"
        )

    MODIS_AQUA_L3_SST_THERMAL_ANNUAL_9KM_NIGHTTIME_V20190_V20190_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_MODIS_AQUA_L3_SST_THERMAL_ANNUAL_9KM_NIGHTTIME_V2019.0_2019.0",
            provider="POCLOUD", 
            shortname="MODIS_AQUA_L3_SST_THERMAL_ANNUAL_9KM_NIGHTTIME_V2019.0",
            version="2019.0",
            description="MODIS Aqua Level 3 SST Thermal IR Annual 9km Nighttime V2019.0 version: 2019.0"
        )

    MODIS_AQUA_L3_SST_THERMAL_DAILY_4KM_NIGHTTIME_V20190_V20190_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_MODIS_AQUA_L3_SST_THERMAL_DAILY_4KM_NIGHTTIME_V2019.0_2019.0",
            provider="POCLOUD", 
            shortname="MODIS_AQUA_L3_SST_THERMAL_DAILY_4KM_NIGHTTIME_V2019.0",
            version="2019.0",
            description="MODIS Aqua Level 3 SST Thermal IR Daily 4km Nighttime V2019.0 version: 2019.0"
        )

    MODIS_AQUA_L3_SST_THERMAL_DAILY_9KM_DAYTIME_V20190_V20190_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_MODIS_AQUA_L3_SST_THERMAL_DAILY_9KM_DAYTIME_V2019.0_2019.0",
            provider="POCLOUD", 
            shortname="MODIS_AQUA_L3_SST_THERMAL_DAILY_9KM_DAYTIME_V2019.0",
            version="2019.0",
            description="MODIS Aqua Level 3 SST Thermal IR Daily 9km Daytime V2019.0 version: 2019.0"
        )

    MODIS_AQUA_L3_SST_THERMAL_DAILY_9KM_NIGHTTIME_V20190_V20190_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_MODIS_AQUA_L3_SST_THERMAL_DAILY_9KM_NIGHTTIME_V2019.0_2019.0",
            provider="POCLOUD", 
            shortname="MODIS_AQUA_L3_SST_THERMAL_DAILY_9KM_NIGHTTIME_V2019.0",
            version="2019.0",
            description="MODIS Aqua Level 3 SST Thermal IR Daily 9km Nighttime V2019.0 version: 2019.0"
        )

    MODIS_AQUA_L3_SST_THERMAL_MONTHLY_4KM_DAYTIME_V20190_V20190_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_MODIS_AQUA_L3_SST_THERMAL_MONTHLY_4KM_DAYTIME_V2019.0_2019.0",
            provider="POCLOUD", 
            shortname="MODIS_AQUA_L3_SST_THERMAL_MONTHLY_4KM_DAYTIME_V2019.0",
            version="2019.0",
            description="MODIS Aqua Level 3 SST Thermal IR Monthly 4km Daytime V2019.0 version: 2019.0"
        )

    MODIS_AQUA_L3_SST_THERMAL_MONTHLY_4KM_NIGHTTIME_V20190_V20190_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_MODIS_AQUA_L3_SST_THERMAL_MONTHLY_4KM_NIGHTTIME_V2019.0_2019.0",
            provider="POCLOUD", 
            shortname="MODIS_AQUA_L3_SST_THERMAL_MONTHLY_4KM_NIGHTTIME_V2019.0",
            version="2019.0",
            description="MODIS Aqua Level 3 SST Thermal IR Monthly 4km Nighttime V2019.0 version: 2019.0"
        )

    MODIS_AQUA_L3_SST_THERMAL_MONTHLY_9KM_DAYTIME_V20190_V20190_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_MODIS_AQUA_L3_SST_THERMAL_MONTHLY_9KM_DAYTIME_V2019.0_2019.0",
            provider="POCLOUD", 
            shortname="MODIS_AQUA_L3_SST_THERMAL_MONTHLY_9KM_DAYTIME_V2019.0",
            version="2019.0",
            description="MODIS Aqua Level 3 SST Thermal IR Monthly 9km Daytime V2019.0 version: 2019.0"
        )

    MODIS_AQUA_L3_SST_THERMAL_MONTHLY_9KM_NIGHTTIME_V20190_V20190_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_MODIS_AQUA_L3_SST_THERMAL_MONTHLY_9KM_NIGHTTIME_V2019.0_2019.0",
            provider="POCLOUD", 
            shortname="MODIS_AQUA_L3_SST_THERMAL_MONTHLY_9KM_NIGHTTIME_V2019.0",
            version="2019.0",
            description="MODIS Aqua Level 3 SST Thermal IR Monthly 9km Nighttime V2019.0 version: 2019.0"
        )

    MODIS_TERRA_L3_SST_THERMAL_DAILY_9KM_DAYTIME_V20190_V20190_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_MODIS_TERRA_L3_SST_THERMAL_DAILY_9KM_DAYTIME_V2019.0_2019.0",
            provider="POCLOUD", 
            shortname="MODIS_TERRA_L3_SST_THERMAL_DAILY_9KM_DAYTIME_V2019.0",
            version="2019.0",
            description="MODIS Terra Level 3 SST Thermal IR Daily 9km Daytime V2019.0 version: 2019.0"
        )

    MODIS_TERRA_L3_SST_MID_IR_8DAY_9KM_NIGHTTIME_V20190_V20190_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_MODIS_TERRA_L3_SST_MID-IR_8DAY_9KM_NIGHTTIME_V2019.0_2019.0",
            provider="POCLOUD", 
            shortname="MODIS_TERRA_L3_SST_MID-IR_8DAY_9KM_NIGHTTIME_V2019.0",
            version="2019.0",
            description="MODIS Terra Level 3 SST MID-IR 8 Day 9km Nighttime V2019.0 version: 2019.0"
        )

    MODIS_TERRA_L3_SST_MID_IR_8DAY_4KM_NIGHTTIME_V20190_V20190_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_MODIS_TERRA_L3_SST_MID-IR_8DAY_4KM_NIGHTTIME_V2019.0_2019.0",
            provider="POCLOUD", 
            shortname="MODIS_TERRA_L3_SST_MID-IR_8DAY_4KM_NIGHTTIME_V2019.0",
            version="2019.0",
            description="MODIS Terra Level 3 SST MID-IR 8 day 4km Nighttime V2019.0 version: 2019.0"
        )

    MODIS_TERRA_L3_SST_MID_IR_ANNUAL_4KM_NIGHTTIME_V20190_V20190_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_MODIS_TERRA_L3_SST_MID-IR_ANNUAL_4KM_NIGHTTIME_V2019.0_2019.0",
            provider="POCLOUD", 
            shortname="MODIS_TERRA_L3_SST_MID-IR_ANNUAL_4KM_NIGHTTIME_V2019.0",
            version="2019.0",
            description="MODIS Terra Level 3 SST MID-IR Annual 4km Nighttime V2019.0 version: 2019.0"
        )

    MODIS_TERRA_L3_SST_MID_IR_ANNUAL_9KM_NIGHTTIME_V20190_V20190_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_MODIS_TERRA_L3_SST_MID-IR_ANNUAL_9KM_NIGHTTIME_V2019.0_2019.0",
            provider="POCLOUD", 
            shortname="MODIS_TERRA_L3_SST_MID-IR_ANNUAL_9KM_NIGHTTIME_V2019.0",
            version="2019.0",
            description="MODIS Terra Level 3 SST MID-IR Annual 9km Nighttime V2019.0 version: 2019.0"
        )

    MODIS_TERRA_L3_SST_MID_IR_DAILY_9KM_NIGHTTIME_V20190_V20190_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_MODIS_TERRA_L3_SST_MID-IR_DAILY_9KM_NIGHTTIME_V2019.0_2019.0",
            provider="POCLOUD", 
            shortname="MODIS_TERRA_L3_SST_MID-IR_DAILY_9KM_NIGHTTIME_V2019.0",
            version="2019.0",
            description="MODIS Terra Level 3 SST MID-IR Daily 9km Nighttime V2019.0 version: 2019.0"
        )

    MODIS_TERRA_L3_SST_MID_IR_MONTHLY_4KM_NIGHTTIME_V20190_V20190_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_MODIS_TERRA_L3_SST_MID-IR_MONTHLY_4KM_NIGHTTIME_V2019.0_2019.0",
            provider="POCLOUD", 
            shortname="MODIS_TERRA_L3_SST_MID-IR_MONTHLY_4KM_NIGHTTIME_V2019.0",
            version="2019.0",
            description="MODIS Terra Level 3 SST MID-IR Monthly 4km Nighttime V2019.0 version: 2019.0"
        )

    MODIS_TERRA_L3_SST_MID_IR_MONTHLY_9KM_NIGHTTIME_V20190_V20190_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_MODIS_TERRA_L3_SST_MID-IR_MONTHLY_9KM_NIGHTTIME_V2019.0_2019.0",
            provider="POCLOUD", 
            shortname="MODIS_TERRA_L3_SST_MID-IR_MONTHLY_9KM_NIGHTTIME_V2019.0",
            version="2019.0",
            description="MODIS Terra Level 3 SST MID-IR Monthly 9km Nighttime V2019.0 version: 2019.0"
        )

    MODIS_TERRA_L3_SST_MID_IR_DAILY_4KM_NIGHTTIME_V20190_V20190_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_MODIS_TERRA_L3_SST_MID-IR_DAILY_4KM_NIGHTTIME_V2019.0_2019.0",
            provider="POCLOUD", 
            shortname="MODIS_TERRA_L3_SST_MID-IR_DAILY_4KM_NIGHTTIME_V2019.0",
            version="2019.0",
            description="MODIS Terra Level 3 SST Mid-IR Daily 4km Nighttime V2019.0 version: 2019.0"
        )

    MODIS_TERRA_L3_SST_THERMAL_8DAY_4KM_DAYTIME_V20190_V20190_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_MODIS_TERRA_L3_SST_THERMAL_8DAY_4KM_DAYTIME_V2019.0_2019.0",
            provider="POCLOUD", 
            shortname="MODIS_TERRA_L3_SST_THERMAL_8DAY_4KM_DAYTIME_V2019.0",
            version="2019.0",
            description="MODIS Terra Level 3 SST Thermal IR 8 Day 4km Daytime V2019.0 version: 2019.0"
        )

    MODIS_TERRA_L3_SST_THERMAL_8DAY_4KM_NIGHTTIME_V20190_V20190_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_MODIS_TERRA_L3_SST_THERMAL_8DAY_4KM_NIGHTTIME_V2019.0_2019.0",
            provider="POCLOUD", 
            shortname="MODIS_TERRA_L3_SST_THERMAL_8DAY_4KM_NIGHTTIME_V2019.0",
            version="2019.0",
            description="MODIS Terra Level 3 SST Thermal IR 8 Day 4km Nighttime V2019.0 version: 2019.0"
        )

    MODIS_TERRA_L3_SST_THERMAL_8DAY_9KM_DAYTIME_V20190_V20190_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_MODIS_TERRA_L3_SST_THERMAL_8DAY_9KM_DAYTIME_V2019.0_2019.0",
            provider="POCLOUD", 
            shortname="MODIS_TERRA_L3_SST_THERMAL_8DAY_9KM_DAYTIME_V2019.0",
            version="2019.0",
            description="MODIS Terra Level 3 SST Thermal IR 8 Day 9km Daytime V2019.0 version: 2019.0"
        )

    MODIS_TERRA_L3_SST_THERMAL_8DAY_9KM_NIGHTTIME_V20190_V20190_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_MODIS_TERRA_L3_SST_THERMAL_8DAY_9KM_NIGHTTIME_V2019.0_2019.0",
            provider="POCLOUD", 
            shortname="MODIS_TERRA_L3_SST_THERMAL_8DAY_9KM_NIGHTTIME_V2019.0",
            version="2019.0",
            description="MODIS Terra Level 3 SST Thermal IR 8 Day 9km Nighttime V2019.0 version: 2019.0"
        )

    MODIS_TERRA_L3_SST_THERMAL_ANNUAL_4KM_DAYTIME_V20190_V20190_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_MODIS_TERRA_L3_SST_THERMAL_ANNUAL_4KM_DAYTIME_V2019.0_2019.0",
            provider="POCLOUD", 
            shortname="MODIS_TERRA_L3_SST_THERMAL_ANNUAL_4KM_DAYTIME_V2019.0",
            version="2019.0",
            description="MODIS Terra Level 3 SST Thermal IR Annual 4km Daytime V2019.0 version: 2019.0"
        )

    MODIS_TERRA_L3_SST_THERMAL_ANNUAL_4KM_NIGHTTIME_V20190_V20190_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_MODIS_TERRA_L3_SST_THERMAL_ANNUAL_4KM_NIGHTTIME_V2019.0_2019.0",
            provider="POCLOUD", 
            shortname="MODIS_TERRA_L3_SST_THERMAL_ANNUAL_4KM_NIGHTTIME_V2019.0",
            version="2019.0",
            description="MODIS Terra Level 3 SST Thermal IR Annual 4km Nighttime V2019.0 version: 2019.0"
        )

    MODIS_TERRA_L3_SST_THERMAL_ANNUAL_9KM_DAYTIME_V20190_V20190_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_MODIS_TERRA_L3_SST_THERMAL_ANNUAL_9KM_DAYTIME_V2019.0_2019.0",
            provider="POCLOUD", 
            shortname="MODIS_TERRA_L3_SST_THERMAL_ANNUAL_9KM_DAYTIME_V2019.0",
            version="2019.0",
            description="MODIS Terra Level 3 SST Thermal IR Annual 9km Daytime V2019.0 version: 2019.0"
        )

    MODIS_TERRA_L3_SST_THERMAL_ANNUAL_9KM_NIGHTTIME_V20190_V20190_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_MODIS_TERRA_L3_SST_THERMAL_ANNUAL_9KM_NIGHTTIME_V2019.0_2019.0",
            provider="POCLOUD", 
            shortname="MODIS_TERRA_L3_SST_THERMAL_ANNUAL_9KM_NIGHTTIME_V2019.0",
            version="2019.0",
            description="MODIS Terra Level 3 SST Thermal IR Annual 9km Nighttime V2019.0 version: 2019.0"
        )

    MODIS_TERRA_L3_SST_THERMAL_DAILY_4KM_DAYTIME_V20190_V20190_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_MODIS_TERRA_L3_SST_THERMAL_DAILY_4KM_DAYTIME_V2019.0_2019.0",
            provider="POCLOUD", 
            shortname="MODIS_TERRA_L3_SST_THERMAL_DAILY_4KM_DAYTIME_V2019.0",
            version="2019.0",
            description="MODIS Terra Level 3 SST Thermal IR Daily 4km Daytime V2019.0 version: 2019.0"
        )

    MODIS_TERRA_L3_SST_THERMAL_DAILY_4KM_NIGHTTIME_V20190_V20190_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_MODIS_TERRA_L3_SST_THERMAL_DAILY_4KM_NIGHTTIME_V2019.0_2019.0",
            provider="POCLOUD", 
            shortname="MODIS_TERRA_L3_SST_THERMAL_DAILY_4KM_NIGHTTIME_V2019.0",
            version="2019.0",
            description="MODIS Terra Level 3 SST Thermal IR Daily 4km Nighttime V2019.0 version: 2019.0"
        )

    MODIS_TERRA_L3_SST_THERMAL_DAILY_9KM_NIGHTTIME_V20190_V20190_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_MODIS_TERRA_L3_SST_THERMAL_DAILY_9KM_NIGHTTIME_V2019.0_2019.0",
            provider="POCLOUD", 
            shortname="MODIS_TERRA_L3_SST_THERMAL_DAILY_9KM_NIGHTTIME_V2019.0",
            version="2019.0",
            description="MODIS Terra Level 3 SST Thermal IR Daily 9km Nighttime V2019.0 version: 2019.0"
        )

    MODIS_TERRA_L3_SST_THERMAL_MONTHLY_4KM_DAYTIME_V20190_V20190_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_MODIS_TERRA_L3_SST_THERMAL_MONTHLY_4KM_DAYTIME_V2019.0_2019.0",
            provider="POCLOUD", 
            shortname="MODIS_TERRA_L3_SST_THERMAL_MONTHLY_4KM_DAYTIME_V2019.0",
            version="2019.0",
            description="MODIS Terra Level 3 SST Thermal IR Monthly 4km Daytime V2019.0 version: 2019.0"
        )

    MODIS_TERRA_L3_SST_THERMAL_MONTHLY_4KM_NIGHTTIME_V20190_V20190_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_MODIS_TERRA_L3_SST_THERMAL_MONTHLY_4KM_NIGHTTIME_V2019.0_2019.0",
            provider="POCLOUD", 
            shortname="MODIS_TERRA_L3_SST_THERMAL_MONTHLY_4KM_NIGHTTIME_V2019.0",
            version="2019.0",
            description="MODIS Terra Level 3 SST Thermal IR Monthly 4km Nighttime V2019.0 version: 2019.0"
        )

    MODIS_TERRA_L3_SST_THERMAL_MONTHLY_9KM_DAYTIME_V20190_V20190_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_MODIS_TERRA_L3_SST_THERMAL_MONTHLY_9KM_DAYTIME_V2019.0_2019.0",
            provider="POCLOUD", 
            shortname="MODIS_TERRA_L3_SST_THERMAL_MONTHLY_9KM_DAYTIME_V2019.0",
            version="2019.0",
            description="MODIS Terra Level 3 SST Thermal IR Monthly 9km Daytime V2019.0 version: 2019.0"
        )

    MODIS_TERRA_L3_SST_THERMAL_MONTHLY_9KM_NIGHTTIME_V20190_V20190_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_MODIS_TERRA_L3_SST_THERMAL_MONTHLY_9KM_NIGHTTIME_V2019.0_2019.0",
            provider="POCLOUD", 
            shortname="MODIS_TERRA_L3_SST_THERMAL_MONTHLY_9KM_NIGHTTIME_V2019.0",
            version="2019.0",
            description="MODIS Terra Level 3 SST Thermal IR Monthly 9km Nighttime V2019.0 version: 2019.0"
        )

    MITGCM_LLC4320_PRE_SWOT_JPL_L4_MARMARASEA_V10_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_MITgcm_LLC4320_Pre-SWOT_JPL_L4_MarmaraSea_v1.0_1.0",
            provider="POCLOUD", 
            shortname="MITgcm_LLC4320_Pre-SWOT_JPL_L4_MarmaraSea_v1.0",
            version="1.0",
            description="Marmara Sea Pre-SWOT Level-4 Hourly MITgcm LLC4320 Native Grid 2km Oceanographic Dataset Version 1.0 version: 1.0"
        )

    OISST_HR_NRT_GOS_L4_MED_V20_V20_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_OISST_HR_NRT-GOS-L4-MED-v2.0_2.0",
            provider="POCLOUD", 
            shortname="OISST_HR_NRT-GOS-L4-MED-v2.0",
            version="2.0",
            description="Mediterranean Sea High Resolution SST L4 Analysis 1/16deg Resolution version: 2.0"
        )

    MITGCM_LLC4320_PRE_SWOT_JPL_L4_WESTERNMED_V10_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_MITgcm_LLC4320_Pre-SWOT_JPL_L4_WesternMed_v1.0_1.0",
            provider="POCLOUD", 
            shortname="MITgcm_LLC4320_Pre-SWOT_JPL_L4_WesternMed_v1.0",
            version="1.0",
            description="Mediterranean Sea Pre-SWOT Level-4 Hourly MITgcm LLC4320 Native Grid 2km Oceanographic Dataset Version 1.0 version: 1.0"
        )

    OISST_UHR_NRT_GOS_L4_MED_V20_V20_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_OISST_UHR_NRT-GOS-L4-MED-v2.0_2.0",
            provider="POCLOUD", 
            shortname="OISST_UHR_NRT-GOS-L4-MED-v2.0",
            version="2.0",
            description="Mediterranean Sea Ultra High Resolution SST L4 Analysis 0.01 deg Resolution version: 2.0"
        )

    ASCATA_ESDR_ANCILLARY_L2_V11_V11_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ASCATA_ESDR_ANCILLARY_L2_V1.1_1.1",
            provider="POCLOUD", 
            shortname="ASCATA_ESDR_ANCILLARY_L2_V1.1",
            version="1.1",
            description="MetOp-A ASCAT ESDR Level 2 Ancillary Ocean Surface Fields Version 1.1 version: 1.1"
        )

    ASCATA_L2_COASTAL_CDR_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ASCATA_L2_COASTAL_CDR_1.0",
            provider="POCLOUD", 
            shortname="ASCATA_L2_COASTAL_CDR",
            version="1.0",
            description="MetOp-A ASCAT Level 2 12.5-km Ocean Surface Wind Vector Climate Data Record Optimized for Coastal Ocean version: 1.0"
        )

    ASCATA_L2_25KM_CDR_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ASCATA_L2_25KM_CDR_1.0",
            provider="POCLOUD", 
            shortname="ASCATA_L2_25KM_CDR",
            version="1.0",
            description="MetOp-A ASCAT Level 2 25-km Ocean Surface Wind Vector Climate Data Record version: 1.0"
        )

    ASCATA_L2_25KM_VOPERATIONAL_NEAR_REAL_TIME_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ASCATA-L2-25km_Operational/Near-Real-Time",
            provider="POCLOUD", 
            shortname="ASCATA-L2-25km",
            version="Operational/Near-Real-Time",
            description="MetOp-A ASCAT Level 2 25.0 km Ocean Surface Wind Vectors version: Operational/Near-Real-Time"
        )

    ASCATA_L2_COASTAL_VOPERATIONAL_NEAR_REAL_TIME_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ASCATA-L2-Coastal_Operational/Near-Real-Time",
            provider="POCLOUD", 
            shortname="ASCATA-L2-Coastal",
            version="Operational/Near-Real-Time",
            description="MetOp-A ASCAT Level 2 Ocean Surface Wind Vectors Optimized for Coastal Ocean version: Operational/Near-Real-Time"
        )

    ASCATA_ESDR_L2_WIND_STRESS_V11_V11_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ASCATA_ESDR_L2_WIND_STRESS_V1.1_1.1",
            provider="POCLOUD", 
            shortname="ASCATA_ESDR_L2_WIND_STRESS_V1.1",
            version="1.1",
            description="MetOp-A ASCAT Scatterometer Inter-Calibrated ESDR Level 2 Ocean Surface Equivalent Neutral Wind Vectors and Wind Stress Vectors Version 1.1 version: 1.1"
        )

    ASCATB_ESDR_ANCILLARY_L2_V11_V11_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ASCATB_ESDR_ANCILLARY_L2_V1.1_1.1",
            provider="POCLOUD", 
            shortname="ASCATB_ESDR_ANCILLARY_L2_V1.1",
            version="1.1",
            description="MetOp-B ASCAT ESDR Level 2 Ancillary Ocean Surface Fields Version 1.1 version: 1.1"
        )

    ASCATB_L2_25KM_VOPERATIONAL_NEAR_REAL_TIME_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ASCATB-L2-25km_Operational/Near-Real-Time",
            provider="POCLOUD", 
            shortname="ASCATB-L2-25km",
            version="Operational/Near-Real-Time",
            description="MetOp-B ASCAT Level 2 25.0km Ocean Surface Wind Vectors in Full Orbit Swath version: Operational/Near-Real-Time"
        )

    ASCATB_L2_COASTAL_VOPERATIONAL_NEAR_REAL_TIME_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ASCATB-L2-Coastal_Operational/Near-Real-Time",
            provider="POCLOUD", 
            shortname="ASCATB-L2-Coastal",
            version="Operational/Near-Real-Time",
            description="MetOp-B ASCAT Level 2 Ocean Surface Wind Vectors Optimized for Coastal Ocean version: Operational/Near-Real-Time"
        )

    ASCATB_ESDR_L2_WIND_STRESS_V11_V11_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ASCATB_ESDR_L2_WIND_STRESS_V1.1_1.1",
            provider="POCLOUD", 
            shortname="ASCATB_ESDR_L2_WIND_STRESS_V1.1",
            version="1.1",
            description="MetOp-B ASCAT Scatterometer Inter-Calibrated ESDR Level 2 Ocean Surface Equivalent Neutral Wind Vectors and Wind Stress Vectors Version 1.1 version: 1.1"
        )

    ASCATC_L2_25KM_VOPERATIONAL_NEAR_REAL_TIME_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ASCATC-L2-25km_Operational/Near-Real-Time",
            provider="POCLOUD", 
            shortname="ASCATC-L2-25km",
            version="Operational/Near-Real-Time",
            description="MetOp-C ASCAT Level 2 25.0km Ocean Surface Wind Vectors in Full Orbit Swath version: Operational/Near-Real-Time"
        )

    ASCATC_L2_COASTAL_VOPERATIONAL_NEAR_REAL_TIME_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ASCATC-L2-Coastal_Operational/Near-Real-Time",
            provider="POCLOUD", 
            shortname="ASCATC-L2-Coastal",
            version="Operational/Near-Real-Time",
            description="MetOp-C ASCAT Level 2 Ocean Surface Wind Vectors Optimized for Coastal Ocean version: Operational/Near-Real-Time"
        )

    TELLUS_GLDAS_NOAH_33_TWS_ANOMALY_MONTHLY_V33_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_TELLUS_GLDAS-NOAH-3.3_TWS-ANOMALY_MONTHLY_3.3",
            provider="POCLOUD", 
            shortname="TELLUS_GLDAS-NOAH-3.3_TWS-ANOMALY_MONTHLY",
            version="3.3",
            description="Monthly gridded Global Land Data Assimilation System (GLDAS) from Noah-v3.3 land hydrology model for GRACE and GRACE-FO over nominal months version: 3.3"
        )

    OISSS_L4_MULTIMISSION_7DAY_V1_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_OISSS_L4_multimission_7day_v1_1.0",
            provider="POCLOUD", 
            shortname="OISSS_L4_multimission_7day_v1",
            version="1.0",
            description="Multi-Mission Optimally Interpolated Sea Surface Salinity Global Dataset V1 version: 1.0"
        )

    OISSS_L4_MULTIMISSION_7DAY_V2_V20_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_OISSS_L4_multimission_7day_v2_2.0",
            provider="POCLOUD", 
            shortname="OISSS_L4_multimission_7day_v2",
            version="2.0",
            description="Multi-Mission Optimally Interpolated Sea Surface Salinity Global Dataset V2 version: 2.0"
        )

    OISSS_L4_MULTIMISSION_MONTHLY_V1_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_OISSS_L4_multimission_monthly_v1_1.0",
            provider="POCLOUD", 
            shortname="OISSS_L4_multimission_monthly_v1",
            version="1.0",
            description="Multi-Mission Optimally Interpolated Sea Surface Salinity Global Monthly Dataset V1 version: 1.0"
        )

    OISSS_L4_MULTIMISSION_MONTHLY_V2_V20_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_OISSS_L4_multimission_monthly_v2_2.0",
            provider="POCLOUD", 
            shortname="OISSS_L4_multimission_monthly_v2",
            version="2.0",
            description="Multi-Mission Optimally Interpolated Sea Surface Salinity Global Monthly Dataset V2 version: 2.0"
        )

    WENTZ_NIMBUS_7_SMMR_L2_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_WENTZ_NIMBUS-7_SMMR_L2_1",
            provider="POCLOUD", 
            shortname="WENTZ_NIMBUS-7_SMMR_L2",
            version="1",
            description="NIMBUS-7 SMMR GLOBAL AIR-SEA PARAMETERS IN SWATH (Wentz) version: 1"
        )

    CYGNSS_NOAA_L2_SWSP_25KM_V11_V11_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_CYGNSS_NOAA_L2_SWSP_25KM_V1.1_1.1",
            provider="POCLOUD", 
            shortname="CYGNSS_NOAA_L2_SWSP_25KM_V1.1",
            version="1.1",
            description="NOAA CYGNSS Level 2 Science Wind Speed 25-km Product Version 1.1 version: 1.1"
        )

    CYGNSS_NOAA_L2_SWSP_25KM_V12_V12_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_CYGNSS_NOAA_L2_SWSP_25KM_V1.2_1.2",
            provider="POCLOUD", 
            shortname="CYGNSS_NOAA_L2_SWSP_25KM_V1.2",
            version="1.2",
            description="NOAA CYGNSS Level 2 Science Wind Speed 25-km Product Version 1.2 version: 1.2"
        )

    MSG04_OSPO_L2P_V10_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_MSG04-OSPO-L2P-v1.0_1.0",
            provider="POCLOUD", 
            shortname="MSG04-OSPO-L2P-v1.0",
            version="1.0",
            description="NOAA GHRSST Level 2P Atlantic Ocean Regional Skin Sea Surface Temperature v1.0 from the Spinning Enhanced Visible and InfraRed Imager (SEVIRI) on the Meteosat Second Generation-4 (MSG-4) satellite version: 1.0"
        )

    MSG01_OSPO_L2P_V10_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_MSG01-OSPO-L2P-v1.0_1.0",
            provider="POCLOUD", 
            shortname="MSG01-OSPO-L2P-v1.0",
            version="1.0",
            description="NOAA GHRSST Level 2P Indian Ocean Regional Skin Sea Surface Temperature v1.0 from the Spinning Enhanced Visible and InfraRed Imager (SEVIRI) on the Meteosat Second Generation-1 (MSG-1) satellite version: 1.0"
        )

    MSG02_OSPO_L2P_V10_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_MSG02-OSPO-L2P-v1.0_1.0",
            provider="POCLOUD", 
            shortname="MSG02-OSPO-L2P-v1.0",
            version="1.0",
            description="NOAA GHRSST Level 2P Indian Ocean Regional Skin Sea Surface Temperature v1.0 from the Spinning Enhanced Visible and InfraRed Imager (SEVIRI) on the Meteosat Second Generation-2 (MSG-2) satellite version: 1.0"
        )

    REYNOLDS_NCDC_L4_MONTHLY_V5_V5_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_REYNOLDS_NCDC_L4_MONTHLY_V5_5",
            provider="POCLOUD", 
            shortname="REYNOLDS_NCDC_L4_MONTHLY_V5",
            version="5",
            description="NOAA Smith and Reynolds Extended Reconstructed Sea Surface Temperature (ERSST) Level 4 Monthly Version 5 Dataset in netCDF version: 5"
        )

    NSCAT_BYU_L3_OW_SIGMA0_ENHANCED_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_NSCAT_BYU_L3_OW_SIGMA0_ENHANCED_1",
            provider="POCLOUD", 
            shortname="NSCAT_BYU_L3_OW_SIGMA0_ENHANCED",
            version="1",
            description="NSCAT Gridded Level 3 Enhanced Resolution Sigma-0 from BYU version: 1"
        )

    NSCAT_W25_RMGDR_V2_V2_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_NSCAT_W25_RMGDR_V2_2",
            provider="POCLOUD", 
            shortname="NSCAT_W25_RMGDR_V2",
            version="2",
            description="NSCAT High Resolution R-MGDR, Selected Ocean Wind Vectors (JPL) version: 2"
        )

    NSCAT_25KM_MGDR_V2_V2_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_NSCAT_25KM_MGDR_V2_2",
            provider="POCLOUD", 
            shortname="NSCAT_25KM_MGDR_V2",
            version="2",
            description="NSCAT High-Resolution MGDR, Sigma-0 and Ocean Wind Vectors (Dunbar) version: 2"
        )

    NSCAT_LEVEL_17_V2_V2_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_NSCAT_LEVEL_1.7_V2_2",
            provider="POCLOUD", 
            shortname="NSCAT_LEVEL_1.7_V2",
            version="2",
            description="NSCAT Level 1.7 SDR, Sigma-0 Cells version: 2"
        )

    NSCAT_AER_HOFFMAN_L2_OW_WIND_VECTOR_AMBIGUITY_REMOVAL_V2_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_NSCAT_AER_HOFFMAN_L2_OW_WIND_VECTOR_AMBIGUITY_REMOVAL_2",
            provider="POCLOUD", 
            shortname="NSCAT_AER_HOFFMAN_L2_OW_WIND_VECTOR_AMBIGUITY_REMOVAL",
            version="2",
            description="NSCAT Level 2 Ocean Wind Vector Ambiguity Removal Overlay (Hoffman, AER) version: 2"
        )

    NSCAT_LEVEL_2_V2_V2_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_NSCAT_LEVEL_2_V2_2",
            provider="POCLOUD", 
            shortname="NSCAT_LEVEL_2_V2",
            version="2",
            description="NSCAT Level 2 Ocean Wind Vector Geophysical Data Record version: 2"
        )

    NSCAT_LEVEL_3_BROWSE_IMAGES_V2_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_NSCAT_LEVEL_3_BROWSE_IMAGES_2",
            provider="POCLOUD", 
            shortname="NSCAT_LEVEL_3_BROWSE_IMAGES",
            version="2",
            description="NSCAT Level 3 Daily Gridded Ocean Surface Wind Vector Browse Images (JPL) version: 2"
        )

    NSCAT_LEVEL_3_V2_V2_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_NSCAT_LEVEL_3_V2_2",
            provider="POCLOUD", 
            shortname="NSCAT_LEVEL_3_V2",
            version="2",
            description="NSCAT Level 3 Daily Gridded Ocean Surface Wind Vectors (JPL) version: 2"
        )

    SPURS1_FLOAT_NEUTRALLYBUOYANT_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SPURS1_FLOAT_NEUTRALLYBUOYANT_1.0",
            provider="POCLOUD", 
            shortname="SPURS1_FLOAT_NEUTRALLYBUOYANT",
            version="1.0",
            description="Neutrally buoyant float data for the SPURS-1 N. Atlantic field campaign version: 1.0"
        )

    MITGCM_LLC4320_PRE_SWOT_JPL_L4_NEWCALEDONIA_V10_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_MITgcm_LLC4320_Pre-SWOT_JPL_L4_NewCaledonia_v1.0_1.0",
            provider="POCLOUD", 
            shortname="MITgcm_LLC4320_Pre-SWOT_JPL_L4_NewCaledonia_v1.0",
            version="1.0",
            description="New Caledonia Pre-SWOT Level-4 Hourly MITgcm LLC4320 Native Grid 2km Oceanographic Dataset Version 1.0 version: 1.0"
        )

    MITGCM_LLC4320_PRE_SWOT_JPL_L4_ROAM_MIZ_V10_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_MITgcm_LLC4320_Pre-SWOT_JPL_L4_ROAM_MIZ_v1.0_1.0",
            provider="POCLOUD", 
            shortname="MITgcm_LLC4320_Pre-SWOT_JPL_L4_ROAM_MIZ_v1.0",
            version="1.0",
            description="Northeast Weddell Sea Pre-SWOT Level-4 Hourly MITgcm LLC4320 Native Grid 2km Oceanographic Dataset Version 1.0 version: 1.0"
        )

    MITGCM_LLC4320_PRE_SWOT_JPL_L4_NWAUSTRALIA_V10_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_MITgcm_LLC4320_Pre-SWOT_JPL_L4_NWAustralia_v1.0_1.0",
            provider="POCLOUD", 
            shortname="MITgcm_LLC4320_Pre-SWOT_JPL_L4_NWAustralia_v1.0",
            version="1.0",
            description="Northwest Australian Shelf Pre-SWOT Level-4 Hourly MITgcm LLC4320 Native Grid 2km Oceanographic Dataset Version 1.0 version: 1.0"
        )

    MITGCM_LLC4320_PRE_SWOT_JPL_L4_NWPACIFIC_V10_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_MITgcm_LLC4320_Pre-SWOT_JPL_L4_NWPacific_v1.0_1.0",
            provider="POCLOUD", 
            shortname="MITgcm_LLC4320_Pre-SWOT_JPL_L4_NWPacific_v1.0",
            version="1.0",
            description="Northwest Pacific Pre-SWOT Level-4 Hourly MITgcm LLC4320 Native Grid 2km Oceanographic Dataset Version 1.0 version: 1.0"
        )

    OMG_L1B_AIRGRAV_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_OMG_L1B_AIRGRAV_1",
            provider="POCLOUD", 
            shortname="OMG_L1B_AIRGRAV",
            version="1",
            description="OMG Airborne Gravity (AirGRAV) Data from Airborne Bathymetry Surveys Version 1 version: 1"
        )

    OMG_L2_AXCTD_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_OMG_L2_AXCTD_1",
            provider="POCLOUD", 
            shortname="OMG_L2_AXCTD",
            version="1",
            description="OMG Airborne eXpendable Conductivity Temperature Depth (AXCTD) Profiles version: 1"
        )

    OMG_L2_CTD_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_OMG_L2_CTD_1",
            provider="POCLOUD", 
            shortname="OMG_L2_CTD",
            version="1",
            description="OMG Conductivity Temperature Depth (CTD) Profiles version: 1"
        )

    OMG_L3_ICE_ELEV_GLISTINA_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_OMG_L3_ICE_ELEV_GLISTINA_1",
            provider="POCLOUD", 
            shortname="OMG_L3_ICE_ELEV_GLISTINA",
            version="1",
            description="OMG Glacial Elevations from GLISTIN-A Ver. 1 version: 1"
        )

    OMG_L2_AXBT_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_OMG_L2_AXBT_1",
            provider="POCLOUD", 
            shortname="OMG_L2_AXBT",
            version="1",
            description="OMG Level 2 Airborne eXpendable Bathy Thermograph (AXBT) Profiles version: 1"
        )

    OMG_NARWHALS_SHIPBOARD_CTD_10_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_OMG_NARWHALS_SHIPBOARD_CTD_1.0_1.0",
            provider="POCLOUD", 
            shortname="OMG_NARWHALS_SHIPBOARD_CTD_1.0",
            version="1.0",
            description="OMG Narwhals Shipboard Conductivity, Temperature, and Depth (CTD) profiles, 2018-2020 version: 1.0"
        )

    OMG_NARWHALS_MOORING_TEMP_CTD_10_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_OMG_NARWHALS_MOORING_TEMP_CTD_1.0_1.0",
            provider="POCLOUD", 
            shortname="OMG_NARWHALS_MOORING_TEMP_CTD_1.0",
            version="1.0",
            description="OMG Narwhals oceanographic data from moorings, 2018-2020 version: 1.0"
        )

    OMG_L1_FLOAT_APEX_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_OMG_L1_FLOAT_APEX_1",
            provider="POCLOUD", 
            shortname="OMG_L1_FLOAT_APEX",
            version="1",
            description="OMG Ocean Water Properties Data from APEX Floats Version 1 version: 1"
        )

    OMG_L1_FLOAT_ALAMO_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_OMG_L1_FLOAT_ALAMO_1",
            provider="POCLOUD", 
            shortname="OMG_L1_FLOAT_ALAMO",
            version="1",
            description="OMG Ocean Water Properties Data from Alamo Floats Version 1 version: 1"
        )

    OMG_L2_BATHY_MBES_GRIDDED_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_OMG_L2_Bathy_MBES_Gridded_1",
            provider="POCLOUD", 
            shortname="OMG_L2_Bathy_MBES_Gridded",
            version="1",
            description="OMG Swath Gridded Multibeam Echo Sounding (MBES) Bathymetry version: 1"
        )

    OMG_L2_BATHY_SBES_GRIDDED_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_OMG_L2_Bathy_SBES_Gridded_1",
            provider="POCLOUD", 
            shortname="OMG_L2_Bathy_SBES_Gridded",
            version="1",
            description="OMG Swath Gridded Singlebeam Echo Sounding (SBES) Bathymetry version: 1"
        )

    OPERA_L3_DSWX_HLS_V1_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_OPERA_L3_DSWX-HLS_V1_1.0",
            provider="POCLOUD", 
            shortname="OPERA_L3_DSWX-HLS_V1",
            version="1.0",
            description="OPERA Dynamic Surface Water Extent from Harmonized Landsat Sentinel-2 product (Version 1) version: 1.0"
        )

    OPERA_L3_DSWX_S1_V1_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_OPERA_L3_DSWX-S1_V1_1.0",
            provider="POCLOUD", 
            shortname="OPERA_L3_DSWX-S1_V1",
            version="1.0",
            description="OPERA Dynamic Surface Water Extent from Sentinel-1 (Version 1) version: 1.0"
        )

    OSCAR_L4_OC_FINAL_V20_V20_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_OSCAR_L4_OC_FINAL_V2.0_2.0",
            provider="POCLOUD", 
            shortname="OSCAR_L4_OC_FINAL_V2.0",
            version="2.0",
            description="Ocean Surface Current Analyses Real-time (OSCAR) Surface Currents - Final 0.25 Degree (Version 2.0) version: 2.0"
        )

    OSCAR_L4_OC_INTERIM_V20_V20_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_OSCAR_L4_OC_INTERIM_V2.0_2.0",
            provider="POCLOUD", 
            shortname="OSCAR_L4_OC_INTERIM_V2.0",
            version="2.0",
            description="Ocean Surface Current Analyses Real-time (OSCAR) Surface Currents - Interim 0.25 Degree (Version 2.0) version: 2.0"
        )

    OSCAR_L4_OC_NRT_V20_V20_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_OSCAR_L4_OC_NRT_V2.0_2.0",
            provider="POCLOUD", 
            shortname="OSCAR_L4_OC_NRT_V2.0",
            version="2.0",
            description="Ocean Surface Current Analyses Real-time (OSCAR) Surface Currents - Near Real Time 0.25 Degree (Version 2.0) version: 2.0"
        )

    OS2_OSCAT_LEVEL_2B_OWV_COMP_12_V2_V2_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_OS2_OSCAT_LEVEL_2B_OWV_COMP_12_V2_2",
            provider="POCLOUD", 
            shortname="OS2_OSCAT_LEVEL_2B_OWV_COMP_12_V2",
            version="2",
            description="Oceansat-2 Scatterometer Level 2B Ocean Wind Vectors in 12.5km Slice Composites Version 2 version: 2"
        )

    SPURS1_MOORING_PICO_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SPURS1_MOORING_PICO_1.0",
            provider="POCLOUD", 
            shortname="SPURS1_MOORING_PICO",
            version="1.0",
            description="PICO Mooring data for the SPURS-1 N. Atlantic field campaign version: 1.0"
        )

    PRIM_SMAP_L2_V1_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_PRIM_SMAP_L2_V1_1.0",
            provider="POCLOUD", 
            shortname="PRIM_SMAP_L2_V1",
            version="1.0",
            description="Parametrized Rain Impact Model for SMAP L2 V1.0 version: 1.0"
        )

    PRESWOT_HYDRO_GRRATS_L2_DAILY_VIRTUAL_STATION_HEIGHTS_V2_V2_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_PRESWOT_HYDRO_GRRATS_L2_DAILY_VIRTUAL_STATION_HEIGHTS_V2_2",
            provider="POCLOUD", 
            shortname="PRESWOT_HYDRO_GRRATS_L2_DAILY_VIRTUAL_STATION_HEIGHTS_V2",
            version="2",
            description="Pre SWOT Hydrology GRRATS Daily River Heights and Storage Version 2 version: 2"
        )

    PRESWOT_HYDRO_GRRATS_L2_VIRTUAL_STATION_HEIGHTS_V2_V2_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_PRESWOT_HYDRO_GRRATS_L2_VIRTUAL_STATION_HEIGHTS_V2_2",
            provider="POCLOUD", 
            shortname="PRESWOT_HYDRO_GRRATS_L2_VIRTUAL_STATION_HEIGHTS_V2",
            version="2",
            description="Pre SWOT Hydrology GRRATS Virtual Station River Heights Version 2 version: 2"
        )

    PRESWOT_HYDRO_L4_LAKE_STORAGE_TIME_SERIES_V2_V2_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_PRESWOT_HYDRO_L4_LAKE_STORAGE_TIME_SERIES_V2_2",
            provider="POCLOUD", 
            shortname="PRESWOT_HYDRO_L4_LAKE_STORAGE_TIME_SERIES_V2",
            version="2",
            description="Pre SWOT Hydrology Global Lake/Reservoir Storage Time Series V2 version: 2"
        )

    PRESWOT_HYDRO_L3_LAKE_RESEVOIR_AREA_V2_V2_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_PRESWOT_HYDRO_L3_LAKE_RESEVOIR_AREA_V2_2",
            provider="POCLOUD", 
            shortname="PRESWOT_HYDRO_L3_LAKE_RESEVOIR_AREA_V2",
            version="2",
            description="Pre SWOT Hydrology Global Lake/Reservoir Surface Inland Water Area Extent V2 version: 2"
        )

    PRESWOT_HYDRO_L2_GREALM_LAKE_HEIGHT_V2_V2_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_PRESWOT_HYDRO_L2_GREALM_LAKE_HEIGHT_V2_2",
            provider="POCLOUD", 
            shortname="PRESWOT_HYDRO_L2_GREALM_LAKE_HEIGHT_V2",
            version="2",
            description="Pre SWOT Hydrology Global Lake/Reservoir Surface Inland Water Height GREALM V.2 version: 2"
        )

    QSCAT_ESDR_MODELED_L2_AUX_V10_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_QSCAT_ESDR_MODELED_L2_AUX_V1.0_1.0",
            provider="POCLOUD", 
            shortname="QSCAT_ESDR_MODELED_L2_AUX_V1.0",
            version="1.0",
            description="QuikSCAT ESDR Level 2 Modeled Ocean Surface Auxiliary Fields Version 1.0 version: 1.0"
        )

    QSCAT_L1C_NONSPINNING_SIGMA0_WINDS_V2_V20_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_QSCAT_L1C_NONSPINNING_SIGMA0_WINDS_V2_2.0",
            provider="POCLOUD", 
            shortname="QSCAT_L1C_NONSPINNING_SIGMA0_WINDS_V2",
            version="2.0",
            description="QuikSCAT Level 1C Averaged Sigma-0 and Winds from Non-spinning Antenna Version 2.0 version: 2.0"
        )

    QSCAT_LEVEL_2B_OWV_COMP_12_V3_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_QSCAT_LEVEL_2B_OWV_COMP_12_3",
            provider="POCLOUD", 
            shortname="QSCAT_LEVEL_2B_OWV_COMP_12",
            version="3",
            description="QuikSCAT Level 2B Ocean Wind Vectors in 12.5km Slice Composites Version 3 version: 3"
        )

    QSCAT_LEVEL_2B_OWV_COMP_12_LCR_31_V31_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_QSCAT_LEVEL_2B_OWV_COMP_12_LCR_3.1_3.1",
            provider="POCLOUD", 
            shortname="QSCAT_LEVEL_2B_OWV_COMP_12_LCR_3.1",
            version="3.1",
            description="QuikSCAT Level 2B Ocean Wind Vectors in 12.5km Slice Composites Version 3.1 version: 3.1"
        )

    QSCAT_LEVEL_2B_OWV_COMP_12_KUSST_LCRES_41_V41_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_QSCAT_LEVEL_2B_OWV_COMP_12_KUSST_LCRES_4.1_4.1",
            provider="POCLOUD", 
            shortname="QSCAT_LEVEL_2B_OWV_COMP_12_KUSST_LCRES_4.1",
            version="4.1",
            description="QuikSCAT Level 2B Ocean Wind Vectors in 12.5km Slice Composites Version 4.1 version: 4.1"
        )

    QUIKSCAT_ESDR_L2_WIND_STRESS_V10_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_QUIKSCAT_ESDR_L2_WIND_STRESS_V1.0_1.0",
            provider="POCLOUD", 
            shortname="QUIKSCAT_ESDR_L2_WIND_STRESS_V1.0",
            version="1.0",
            description="QuikSCAT Scatterometer Inter-Calibrated ESDR Level 2 Ocean Surface Equivalent Neutral Wind Vectors and Wind Stress Vectors Version 1.0 version: 1.0"
        )

    CCMP_WINDS_10M6HR_L4_V31_V31_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_CCMP_WINDS_10M6HR_L4_V3.1_3.1",
            provider="POCLOUD", 
            shortname="CCMP_WINDS_10M6HR_L4_V3.1",
            version="3.1",
            description="RSS CCMP 6-Hourly 10 Meter Surface Winds Level 4 Version 3.1 version: 3.1"
        )

    CCMP_WINDS_10MMONTHLY_L4_V31_V31_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_CCMP_WINDS_10MMONTHLY_L4_V3.1_3.1",
            provider="POCLOUD", 
            shortname="CCMP_WINDS_10MMONTHLY_L4_V3.1",
            version="3.1",
            description="RSS CCMP Monthly 10 Meter Surface Winds Level 4 Version 3.1 version: 3.1"
        )

    SMAP_RSS_L2_SSS_NRT_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SMAP_RSS_L2_SSS_NRT_V5_5.0",
            provider="POCLOUD", 
            shortname="SMAP_RSS_L2_SSS_NRT_V5",
            version="5.0",
            description="RSS SMAP Level 2C Sea Surface Salinity NRT V5.0 Validated Dataset version: 5.0"
        )

    SMAP_RSS_L2_SSS_NRT_V6_V60_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SMAP_RSS_L2_SSS_NRT_V6_6.0",
            provider="POCLOUD", 
            shortname="SMAP_RSS_L2_SSS_NRT_V6",
            version="6.0",
            description="RSS SMAP Level 2C Sea Surface Salinity NRT V6.0 Validated Dataset version: 6.0"
        )

    SMAP_RSS_L2_SSS_V4_V40_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SMAP_RSS_L2_SSS_V4_4.0",
            provider="POCLOUD", 
            shortname="SMAP_RSS_L2_SSS_V4",
            version="4.0",
            description="RSS SMAP Level 2C Sea Surface Salinity V4.0 Validated Dataset version: 4.0"
        )

    SMAP_RSS_L2_SSS_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SMAP_RSS_L2_SSS_V5_5.0",
            provider="POCLOUD", 
            shortname="SMAP_RSS_L2_SSS_V5",
            version="5.0",
            description="RSS SMAP Level 2C Sea Surface Salinity V5.0 Validated Dataset version: 5.0"
        )

    SMAP_RSS_L2_SSS_V53_V53_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SMAP_RSS_L2_SSS_V5.3_5.3",
            provider="POCLOUD", 
            shortname="SMAP_RSS_L2_SSS_V5.3",
            version="5.3",
            description="RSS SMAP Level 2C Sea Surface Salinity V5.3 Evaluation Dataset version: 5.3"
        )

    SMAP_RSS_L2_SSS_V6_V60_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SMAP_RSS_L2_SSS_V6_6.0",
            provider="POCLOUD", 
            shortname="SMAP_RSS_L2_SSS_V6",
            version="6.0",
            description="RSS SMAP Level 2C Sea Surface Salinity V6.0 Validated Dataset version: 6.0"
        )

    SMAP_RSS_L3_SSS_SMI_8DAY_RUNNINGMEAN_V4_V40_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SMAP_RSS_L3_SSS_SMI_8DAY-RUNNINGMEAN_V4_4.0",
            provider="POCLOUD", 
            shortname="SMAP_RSS_L3_SSS_SMI_8DAY-RUNNINGMEAN_V4",
            version="4.0",
            description="RSS SMAP Level 3 Sea Surface Salinity Standard Mapped Image 8-Day Running Mean V4.0 Validated Dataset version: 4.0"
        )

    SMAP_RSS_L3_SSS_SMI_8DAY_RUNNINGMEAN_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SMAP_RSS_L3_SSS_SMI_8DAY-RUNNINGMEAN_V5_5.0",
            provider="POCLOUD", 
            shortname="SMAP_RSS_L3_SSS_SMI_8DAY-RUNNINGMEAN_V5",
            version="5.0",
            description="RSS SMAP Level 3 Sea Surface Salinity Standard Mapped Image 8-Day Running Mean V5.0 Validated Dataset version: 5.0"
        )

    SMAP_RSS_L3_SSS_SMI_8DAY_RUNNINGMEAN_V53_V53_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SMAP_RSS_L3_SSS_SMI_8DAY-RUNNINGMEAN_V5.3_5.3",
            provider="POCLOUD", 
            shortname="SMAP_RSS_L3_SSS_SMI_8DAY-RUNNINGMEAN_V5.3",
            version="5.3",
            description="RSS SMAP Level 3 Sea Surface Salinity Standard Mapped Image 8-Day Running Mean V5.3 Evaluation Dataset version: 5.3"
        )

    SMAP_RSS_L3_SSS_SMI_8DAY_RUNNINGMEAN_V6_V60_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SMAP_RSS_L3_SSS_SMI_8DAY-RUNNINGMEAN_V6_6.0",
            provider="POCLOUD", 
            shortname="SMAP_RSS_L3_SSS_SMI_8DAY-RUNNINGMEAN_V6",
            version="6.0",
            description="RSS SMAP Level 3 Sea Surface Salinity Standard Mapped Image 8-Day Running Mean V6.0 Validated Dataset version: 6.0"
        )

    SMAP_RSS_L3_SSS_SMI_MONTHLY_V4_V40_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SMAP_RSS_L3_SSS_SMI_MONTHLY_V4_4.0",
            provider="POCLOUD", 
            shortname="SMAP_RSS_L3_SSS_SMI_MONTHLY_V4",
            version="4.0",
            description="RSS SMAP Level 3 Sea Surface Salinity Standard Mapped Image Monthly V4.0 Validated Dataset version: 4.0"
        )

    SMAP_RSS_L3_SSS_SMI_MONTHLY_V5_V50_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SMAP_RSS_L3_SSS_SMI_MONTHLY_V5_5.0",
            provider="POCLOUD", 
            shortname="SMAP_RSS_L3_SSS_SMI_MONTHLY_V5",
            version="5.0",
            description="RSS SMAP Level 3 Sea Surface Salinity Standard Mapped Image Monthly V5.0 Validated Dataset version: 5.0"
        )

    SMAP_RSS_L3_SSS_SMI_MONTHLY_V53_V53_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SMAP_RSS_L3_SSS_SMI_MONTHLY_V5.3_5.3",
            provider="POCLOUD", 
            shortname="SMAP_RSS_L3_SSS_SMI_MONTHLY_V5.3",
            version="5.3",
            description="RSS SMAP Level 3 Sea Surface Salinity Standard Mapped Image Monthly V5.3 Evaluation Dataset version: 5.3"
        )

    SMAP_RSS_L3_SSS_SMI_MONTHLY_V6_V60_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SMAP_RSS_L3_SSS_SMI_MONTHLY_V6_6.0",
            provider="POCLOUD", 
            shortname="SMAP_RSS_L3_SSS_SMI_MONTHLY_V6",
            version="6.0",
            description="RSS SMAP Level 3 Sea Surface Salinity Standard Mapped Image Monthly V6.0 Validated Dataset version: 6.0"
        )

    RSS_WINDSAT_L1C_TB_V080_V80_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_RSS_WindSat_L1C_TB_V08.0_8.0",
            provider="POCLOUD", 
            shortname="RSS_WindSat_L1C_TB_V08.0",
            version="8.0",
            description="RSS WindSat L1C Calibrated TB Version 8 version: 8.0"
        )

    RSCAT_L1B_V20_V20_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_RSCAT_L1B_V2.0_2.0",
            provider="POCLOUD", 
            shortname="RSCAT_L1B_V2.0",
            version="2.0",
            description="RapidScat Level 1B Time-Ordered Geo-Located Sigma-0 Version 2.0 version: 2.0"
        )

    RSCAT_L2A_12KM_V20_V20_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_RSCAT_L2A_12KM_V2.0_2.0",
            provider="POCLOUD", 
            shortname="RSCAT_L2A_12KM_V2.0",
            version="2.0",
            description="RapidScat Level 2A Surface Flagged Sigma-0 and Attenuations in 12.5km Swath Grid Version 2.0 version: 2.0"
        )

    RSCAT_L2A_25KM_V20_V20_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_RSCAT_L2A_25KM_V2.0_2.0",
            provider="POCLOUD", 
            shortname="RSCAT_L2A_25KM_V2.0",
            version="2.0",
            description="RapidScat Level 2A Surface Flagged Sigma-0 and Attenuations in 25km Swath Grid Version 2.0 version: 2.0"
        )

    RSCAT_LEVEL_2B_OWV_CLIM_12_V1_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_RSCAT_LEVEL_2B_OWV_CLIM_12_V1_1.0",
            provider="POCLOUD", 
            shortname="RSCAT_LEVEL_2B_OWV_CLIM_12_V1",
            version="1.0",
            description="RapidScat Level 2B Climate Ocean Wind Vectors in 12.5km Footprints version: 1.0"
        )

    RSCAT_LEVEL_2B_OWV_CLIM_12_V2_V20_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_RSCAT_LEVEL_2B_OWV_CLIM_12_V2_2.0",
            provider="POCLOUD", 
            shortname="RSCAT_LEVEL_2B_OWV_CLIM_12_V2",
            version="2.0",
            description="RapidScat Level 2B Climate Ocean Wind Vectors in 12.5km Footprints Version 2.0 version: 2.0"
        )

    RSCAT_LEVEL_2B_OWV_COMP_12_V11_V11_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_RSCAT_LEVEL_2B_OWV_COMP_12_V1.1_1.1",
            provider="POCLOUD", 
            shortname="RSCAT_LEVEL_2B_OWV_COMP_12_V1.1",
            version="1.1",
            description="RapidScat Level 2B Ocean Wind Vectors in 12.5km Slice Composites Version 1.1 version: 1.1"
        )

    RSCAT_LEVEL_2B_OWV_COMP_12_V12_V12_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_RSCAT_LEVEL_2B_OWV_COMP_12_V1.2_1.2",
            provider="POCLOUD", 
            shortname="RSCAT_LEVEL_2B_OWV_COMP_12_V1.2",
            version="1.2",
            description="RapidScat Level 2B Ocean Wind Vectors in 12.5km Slice Composites Version 1.2 version: 1.2"
        )

    RSCAT_LEVEL_2B_OWV_COMP_12_V13_V13_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_RSCAT_LEVEL_2B_OWV_COMP_12_V1.3_1.3",
            provider="POCLOUD", 
            shortname="RSCAT_LEVEL_2B_OWV_COMP_12_V1.3",
            version="1.3",
            description="RapidScat Level 2B Ocean Wind Vectors in 12.5km Slice Composites Version 1.3 version: 1.3"
        )

    JPL_RECON_GMSL_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_JPL_RECON_GMSL_1.0",
            provider="POCLOUD", 
            shortname="JPL_RECON_GMSL",
            version="1.0",
            description="Reconstructed Global Mean Sea Level 1900-2018 version: 1.0"
        )

    RECON_SEA_LEVEL_OST_L4_V1_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_RECON_SEA_LEVEL_OST_L4_V1_1",
            provider="POCLOUD", 
            shortname="RECON_SEA_LEVEL_OST_L4_V1",
            version="1",
            description="Reconstructed Sea Level Version 1 version: 1"
        )

    RSCAT_COLOCATED_RSS_RADIOMETER_LEVEL_2B_V1_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_RSCAT_COLOCATED_RSS_RADIOMETER_LEVEL_2B_V1_1.0",
            provider="POCLOUD", 
            shortname="RSCAT_COLOCATED_RSS_RADIOMETER_LEVEL_2B_V1",
            version="1.0",
            description="Remote Sensing Systems Radiometer Rain Collocations with JPL RapidScat L2B Swath Grid version: 1.0"
        )

    MITGCM_LLC4320_PRE_SWOT_JPL_L4_ROCKALLTROUGH_V10_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_MITgcm_LLC4320_Pre-SWOT_JPL_L4_RockallTrough_v1.0_1.0",
            provider="POCLOUD", 
            shortname="MITgcm_LLC4320_Pre-SWOT_JPL_L4_RockallTrough_v1.0",
            version="1.0",
            description="Rockall Trough Pre-SWOT Level-4 Hourly MITgcm LLC4320 Native Grid 2km Oceanographic Dataset Version 1.0 version: 1.0"
        )

    RONGOWAI_L1_SDR_V10_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_RONGOWAI_L1_SDR_V1.0_1.0",
            provider="POCLOUD", 
            shortname="RONGOWAI_L1_SDR_V1.0",
            version="1.0",
            description="Rongowai-CYGNSS Airborne Level 1 Science Data Record Version 1.0 version: 1.0"
        )

    SMODE_L1_DOPPLERSCATT_V1_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SMODE_L1_DOPPLERSCATT_V1_1",
            provider="POCLOUD", 
            shortname="SMODE_L1_DOPPLERSCATT_V1",
            version="1",
            description="S-MODE DopplerScatt Level 1 Surface Doppler and Radar Backscatter Version 1 version: 1"
        )

    SMODE_L2_DOPPLERSCATT_WINDS_CURRENT_V1_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SMODE_L2_DOPPLERSCATT_WINDS_CURRENT_V1_1",
            provider="POCLOUD", 
            shortname="SMODE_L2_DOPPLERSCATT_WINDS_CURRENT_V1",
            version="1",
            description="S-MODE DopplerScatt Level 2 Ocean Winds and Currents Version 1 version: 1"
        )

    SMODE_L2_DOPPLERSCATT_WINDS_CURRENT_V2_V2_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SMODE_L2_DOPPLERSCATT_WINDS_CURRENT_V2_2",
            provider="POCLOUD", 
            shortname="SMODE_L2_DOPPLERSCATT_WINDS_CURRENT_V2",
            version="2",
            description="S-MODE DopplerScatt Level 2 Ocean Winds and Currents Version 2 version: 2"
        )

    SMODE_L2_DRIFTER_POSITIONS_V1_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SMODE_L2_DRIFTER_POSITIONS_V1_1",
            provider="POCLOUD", 
            shortname="SMODE_L2_DRIFTER_POSITIONS_V1",
            version="1",
            description="S-MODE L2 Position Data from Surface Drifters Version 1 version: 1"
        )

    SMODE_L2_SHIPBOARD_ADCP_V1_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SMODE_L2_SHIPBOARD_ADCP_V1_1",
            provider="POCLOUD", 
            shortname="SMODE_L2_SHIPBOARD_ADCP_V1",
            version="1",
            description="S-MODE L2 Shipboard Acoustic Doppler Current Profiler Measurements Version 1 version: 1"
        )

    SMODE_L2_SHIPBOARD_BOTTLES_V1_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SMODE_L2_SHIPBOARD_BOTTLES_V1_1",
            provider="POCLOUD", 
            shortname="SMODE_L2_SHIPBOARD_BOTTLES_V1",
            version="1",
            description="S-MODE L2 Shipboard Bottle Data Version 1 version: 1"
        )

    SMODE_L2_SHIPBOARD_CTD_V1_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SMODE_L2_SHIPBOARD_CTD_V1_1",
            provider="POCLOUD", 
            shortname="SMODE_L2_SHIPBOARD_CTD_V1",
            version="1",
            description="S-MODE L2 Shipboard Conductivity, Temperature, and Depth Measurements Version 1 version: 1"
        )

    SMODE_L2_SHIPBOARD_RADIOSONDES_METEOROLOGY_V1_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SMODE_L2_SHIPBOARD_RADIOSONDES_METEOROLOGY_V1_1",
            provider="POCLOUD", 
            shortname="SMODE_L2_SHIPBOARD_RADIOSONDES_METEOROLOGY_V1",
            version="1",
            description="S-MODE L2 Shipboard Meteorological Data from Rawinsondes Version 1 version: 1"
        )

    SMODE_L2_SHIPBOARD_SUNA_V1_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SMODE_L2_SHIPBOARD_SUNA_V1_1",
            provider="POCLOUD", 
            shortname="SMODE_L2_SHIPBOARD_SUNA_V1",
            version="1",
            description="S-MODE L2 Shipboard SUNA nitrate data Version 1 version: 1"
        )

    SMODE_L2_SHIPBOARD_TSG_V1_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SMODE_L2_SHIPBOARD_TSG_V1_1",
            provider="POCLOUD", 
            shortname="SMODE_L2_SHIPBOARD_TSG_V1",
            version="1",
            description="S-MODE L2 Shipboard Thermosalinograph, Meteorology, and Bio-optics Measurements Version 1 version: 1"
        )

    SMODE_L2_SAILDRONES_V1_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SMODE_L2_SAILDRONES_V1_1",
            provider="POCLOUD", 
            shortname="SMODE_L2_SAILDRONES_V1",
            version="1",
            description="S-MODE L2 Temperature and Salinity from Saildrones Version 1 version: 1"
        )

    SMODE_L2_LAGRANGIAN_FLOATS_V1_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SMODE_L2_LAGRANGIAN_FLOATS_V1_1",
            provider="POCLOUD", 
            shortname="SMODE_L2_LAGRANGIAN_FLOATS_V1",
            version="1",
            description="S-MODE Lagrangian Float Observations Version 1 version: 1"
        )

    SMODE_L1_MASS_DOPPVIS_V1_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SMODE_L1_MASS_DOPPVIS_V1_1",
            provider="POCLOUD", 
            shortname="SMODE_L1_MASS_DOPPVIS_V1",
            version="1",
            description="S-MODE Level 1 MASS DoppVis Imagery Version 1 version: 1"
        )

    SMODE_L3_SEAGLIDERS_TEMP_SALINITY_V1_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SMODE_L3_SEAGLIDERS_TEMP_SALINITY_V1_1",
            provider="POCLOUD", 
            shortname="SMODE_L3_SEAGLIDERS_TEMP_SALINITY_V1",
            version="1",
            description="S-MODE Level 3 Seaglider Observations Version 1 version: 1"
        )

    SMODE_L3_SHIPBOARD_UCTD_ECOCTD_V1_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SMODE_L3_SHIPBOARD_UCTD_ECOCTD_V1_1",
            provider="POCLOUD", 
            shortname="SMODE_L3_SHIPBOARD_UCTD_ECOCTD_V1",
            version="1",
            description="S-MODE Level 3 Shipboard uCTD and EcoCTD Measurements Version 1 version: 1"
        )

    SMODE_L1_MASS_HYPERSPECTRAL_V1_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SMODE_L1_MASS_HYPERSPECTRAL_V1_1",
            provider="POCLOUD", 
            shortname="SMODE_L1_MASS_HYPERSPECTRAL_V1",
            version="1",
            description="S-MODE MASS Level 1 Hyperspectral Imagery Version 1 version: 1"
        )

    SMODE_L1_MASS_LWIR_V1_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SMODE_L1_MASS_LWIR_V1_1",
            provider="POCLOUD", 
            shortname="SMODE_L1_MASS_LWIR_V1",
            version="1",
            description="S-MODE MASS Level 1 LWIR Version 1 version: 1"
        )

    SMODE_L1_MASS_LIDAR_V1_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SMODE_L1_MASS_LIDAR_V1_1",
            provider="POCLOUD", 
            shortname="SMODE_L1_MASS_LIDAR_V1",
            version="1",
            description="S-MODE MASS Level 1 Lidar Point Cloud Version 1 version: 1"
        )

    SMODE_L1_MASS_VISIBLE_V1_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SMODE_L1_MASS_VISIBLE_V1_1",
            provider="POCLOUD", 
            shortname="SMODE_L1_MASS_VISIBLE_V1",
            version="1",
            description="S-MODE MASS Level 1 Visible Imagery Version 1 version: 1"
        )

    SMODE_L2_MOSES_LWIR_SST_V1_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SMODE_L2_MOSES_LWIR_SST_V1_1",
            provider="POCLOUD", 
            shortname="SMODE_L2_MOSES_LWIR_SST_V1",
            version="1",
            description="S-MODE MOSES Level 2 Atmospherically-Corrected Sea Surface Temperature Version 1 version: 1"
        )

    SMODE_L4_NCOM_V1_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SMODE_L4_NCOM_V1_1",
            provider="POCLOUD", 
            shortname="SMODE_L4_NCOM_V1",
            version="1",
            description="S-MODE NCOM Model Output Version 1 version: 1"
        )

    SMODE_L1_PRISM_V1_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SMODE_L1_PRISM_V1_1",
            provider="POCLOUD", 
            shortname="SMODE_L1_PRISM_V1",
            version="1",
            description="S-MODE PRISM Level 1 Radiance and Ancillary Products Version 1 version: 1"
        )

    SMODE_L2_PRISM_CHLA_V1_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SMODE_L2_PRISM_CHLA_V1_1",
            provider="POCLOUD", 
            shortname="SMODE_L2_PRISM_CHLA_V1",
            version="1",
            description="S-MODE PRISM Level 2 Water Surface Chlorophyll-a Version 1 version: 1"
        )

    SMODE_L2A_PRISM_REFL_V1_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SMODE_L2a_PRISM_REFL_V1_1",
            provider="POCLOUD", 
            shortname="SMODE_L2a_PRISM_REFL_V1",
            version="1",
            description="S-MODE PRISM Level 2a Reflectance Version 1 version: 1"
        )

    SMODE_L1_ASIT_KABODS_V1_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SMODE_L1_ASIT_KABODS_V1_1",
            provider="POCLOUD", 
            shortname="SMODE_L1_ASIT_KABODS_V1",
            version="1",
            description="S-MODE Pre-Pilot Level 1 Data from the Ka-band Ocean Doppler Scatterometer (KaBODS) at the Air-Sea Interaction Tower Version 1 version: 1"
        )

    SMODE_L1_ASIT_SLOPEFIELDS_V1_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SMODE_L1_ASIT_SLOPEFIELDS_V1_1",
            provider="POCLOUD", 
            shortname="SMODE_L1_ASIT_SLOPEFIELDS_V1",
            version="1",
            description="S-MODE Pre-Pilot Ocean Wave Slope from Visible-Band Polarimetry at the Air-Sea Interaction Tower Version 1 version: 1"
        )

    SMODE_L1_SAILDRONES_V1_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SMODE_L1_SAILDRONES_V1_1",
            provider="POCLOUD", 
            shortname="SMODE_L1_SAILDRONES_V1",
            version="1",
            description="S-MODE Saildrone Level 1 Observations version: 1"
        )

    SMODE_L2_SEAGLIDERS_V1_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SMODE_L2_SEAGLIDERS_V1_1",
            provider="POCLOUD", 
            shortname="SMODE_L2_SEAGLIDERS_V1",
            version="1",
            description="S-MODE Seaglider Observations Version 1 version: 1"
        )

    SMODE_L2_SHIPBOARD_BIO_V1_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SMODE_L2_SHIPBOARD_BIO_V1_1",
            provider="POCLOUD", 
            shortname="SMODE_L2_SHIPBOARD_BIO_V1",
            version="1",
            description="S-MODE Shipboard Bio-optical Measurements Version 1 version: 1"
        )

    SMODE_L2_SHIPBOARD_RADIOMETER_METEOROLOGY_V1_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SMODE_L2_SHIPBOARD_RADIOMETER_METEOROLOGY_V1_1",
            provider="POCLOUD", 
            shortname="SMODE_L2_SHIPBOARD_RADIOMETER_METEOROLOGY_V1",
            version="1",
            description="S-MODE Shipboard Radiometer Measurements Version 1 version: 1"
        )

    SMODE_L2_SHIPBOARD_UCTD_ECOCTD_V1_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SMODE_L2_SHIPBOARD_UCTD_ECOCTD_V1_1",
            provider="POCLOUD", 
            shortname="SMODE_L2_SHIPBOARD_UCTD_ECOCTD_V1",
            version="1",
            description="S-MODE Shipboard uCTD and EcoCTD Measurements Version 1 version: 1"
        )

    SMODE_L2_APEX_FLOAT_V1_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SMODE_L2_APEX_FLOAT_V1_1",
            provider="POCLOUD", 
            shortname="SMODE_L2_APEX_FLOAT_V1",
            version="1",
            description="S-MODE Temperature and Salinity from NAVO Floats Version 1 version: 1"
        )

    SMODE_L2_SLOCUM_GLIDERS_V1_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SMODE_L2_SLOCUM_GLIDERS_V1_1",
            provider="POCLOUD", 
            shortname="SMODE_L2_SLOCUM_GLIDERS_V1",
            version="1",
            description="S-MODE Temperature and Salinity from Slocum Gliders Version 1 version: 1"
        )

    SMODE_L2_WAVEGLIDERS_TEMP_SALINITY_V1_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SMODE_L2_WAVEGLIDERS_TEMP_SALINITY_V1_1",
            provider="POCLOUD", 
            shortname="SMODE_L2_WAVEGLIDERS_TEMP_SALINITY_V1",
            version="1",
            description="S-MODE Waveglider Observations version: 1"
        )

    ALTIKA_SARAL_L2_OST_XOGDR_VF_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ALTIKA_SARAL_L2_OST_XOGDR_f",
            provider="POCLOUD", 
            shortname="ALTIKA_SARAL_L2_OST_XOGDR",
            version="f",
            description="SARAL Near-Real-Time Value-added Operational Geophysical Data Record Sea Surface Height Anomaly version: f"
        )

    SASSIE_L2_ALTO_ALAMO_FLOATS_V1_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SASSIE_L2_ALTO_ALAMO_FLOATS_V1_1",
            provider="POCLOUD", 
            shortname="SASSIE_L2_ALTO_ALAMO_FLOATS_V1",
            version="1",
            description="SASSIE Arctic Field Campaign ALTO/ALAMO Profiling Float Data Fall 2022 Version 1 version: 1"
        )

    SASSIE_L2_DRIFTER_UPTEMPO_V1_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SASSIE_L2_DRIFTER_UPTEMPO_V1_1",
            provider="POCLOUD", 
            shortname="SASSIE_L2_DRIFTER_UPTEMPO_V1",
            version="1",
            description="SASSIE Arctic Field Campaign Drifter Hydrography Data Fall 2022 Version 1 version: 1"
        )

    SASSIE_L2_DRIFTER_UPTEMPO_V2P_V2P_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SASSIE_L2_DRIFTER_UPTEMPO_V2p_2p",
            provider="POCLOUD", 
            shortname="SASSIE_L2_DRIFTER_UPTEMPO_V2p",
            version="2p",
            description="SASSIE Arctic Field Campaign Drifter Hydrography Data Fall 2022 Version 2p version: 2p"
        )

    SASSIE_L2_JET_SSP_V1_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SASSIE_L2_JET_SSP_V1_1",
            provider="POCLOUD", 
            shortname="SASSIE_L2_JET_SSP_V1",
            version="1",
            description="SASSIE Arctic Field Campaign Jet Surface Salinity Profiler Data Fall 2022 Version 1 version: 1"
        )

    SASSIE_L1_SWIFT_V1_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SASSIE_L1_SWIFT_V1_1",
            provider="POCLOUD", 
            shortname="SASSIE_L1_SWIFT_V1",
            version="1",
            description="SASSIE Arctic Field Campaign L1 SWIFT Data Fall 2022 version: 1"
        )

    SASSIE_L1_WAVEGLIDER_V1_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SASSIE_L1_WAVEGLIDER_V1_1",
            provider="POCLOUD", 
            shortname="SASSIE_L1_WAVEGLIDER_V1",
            version="1",
            description="SASSIE Arctic Field Campaign L1 Wave Glider Data Fall 2022 version: 1"
        )

    SASSIE_L2_PALS_V1_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SASSIE_L2_PALS_V1_1",
            provider="POCLOUD", 
            shortname="SASSIE_L2_PALS_V1",
            version="1",
            description="SASSIE Arctic Field Campaign PALS Data Fall 2022 version: 1"
        )

    SASSIE_L2_SWIFT_V1_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SASSIE_L2_SWIFT_V1_1",
            provider="POCLOUD", 
            shortname="SASSIE_L2_SWIFT_V1",
            version="1",
            description="SASSIE Arctic Field Campaign SWIFT Data Fall 2022 Version 1 version: 1"
        )

    SASSIE_L2_SHIPBOARD_ADCP_V1_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SASSIE_L2_SHIPBOARD_ADCP_V1_1",
            provider="POCLOUD", 
            shortname="SASSIE_L2_SHIPBOARD_ADCP_V1",
            version="1",
            description="SASSIE Arctic Field Campaign Shipboard Acoustic Doppler Current Profiler Data Fall 2022 version: 1"
        )

    SASSIE_L2_SHIPBOARD_CASTAWAY_CTD_V1_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SASSIE_L2_SHIPBOARD_CASTAWAY_CTD_V1_1",
            provider="POCLOUD", 
            shortname="SASSIE_L2_SHIPBOARD_CASTAWAY_CTD_V1",
            version="1",
            description="SASSIE Arctic Field Campaign Shipboard Castaway CTD Data Fall 2022 Version 1 version: 1"
        )

    SASSIE_L2_SHIPBOARD_DELTA_18O_V1_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SASSIE_L2_SHIPBOARD_DELTA_18O_V1_1",
            provider="POCLOUD", 
            shortname="SASSIE_L2_SHIPBOARD_DELTA_18O_V1",
            version="1",
            description="SASSIE Arctic Field Campaign Shipboard Delta-18O Data Fall 2022 version: 1"
        )

    SASSIE_L2_SHIPBOARD_METEOROLOGY_V1_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SASSIE_L2_SHIPBOARD_METEOROLOGY_V1_1",
            provider="POCLOUD", 
            shortname="SASSIE_L2_SHIPBOARD_METEOROLOGY_V1",
            version="1",
            description="SASSIE Arctic Field Campaign Shipboard Meteorology Data Fall 2022 version: 1"
        )

    SASSIE_L3_SHIPBOARD_SBAND_V1_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SASSIE_L3_SHIPBOARD_SBAND_V1_1",
            provider="POCLOUD", 
            shortname="SASSIE_L3_SHIPBOARD_SBAND_V1",
            version="1",
            description="SASSIE Arctic Field Campaign Shipboard S-Band Radar Level 3 Data Fall 2022 version: 1"
        )

    SASSIE_L4_SHIPBOARD_SBAND_V1_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SASSIE_L4_SHIPBOARD_SBAND_V1_1",
            provider="POCLOUD", 
            shortname="SASSIE_L4_SHIPBOARD_SBAND_V1",
            version="1",
            description="SASSIE Arctic Field Campaign Shipboard S-Band Radar Level 4 Data Fall 2022 version: 1"
        )

    SASSIE_L2_SHIPBOARD_SALINITY_SNAKE_V1_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SASSIE_L2_SHIPBOARD_SALINITY_SNAKE_V1_1",
            provider="POCLOUD", 
            shortname="SASSIE_L2_SHIPBOARD_SALINITY_SNAKE_V1",
            version="1",
            description="SASSIE Arctic Field Campaign Shipboard Salinity Snake Data Fall 2022 version: 1"
        )

    SASSIE_L2_SHIPBOARD_TSG_V1_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SASSIE_L2_SHIPBOARD_TSG_V1_1",
            provider="POCLOUD", 
            shortname="SASSIE_L2_SHIPBOARD_TSG_V1",
            version="1",
            description="SASSIE Arctic Field Campaign Shipboard Thermosalinograph Data Fall 2022 Version 1 version: 1"
        )

    SASSIE_L2_SHIPBOARD_UCTD_V1_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SASSIE_L2_SHIPBOARD_UCTD_V1_1",
            provider="POCLOUD", 
            shortname="SASSIE_L2_SHIPBOARD_UCTD_V1",
            version="1",
            description="SASSIE Arctic Field Campaign Shipboard uCTD Data Fall 2022 Version 1 version: 1"
        )

    SASSIE_L2_SBAND_ML_V1_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SASSIE_L2_SBAND_ML_V1_1",
            provider="POCLOUD", 
            shortname="SASSIE_L2_SBAND_ML_V1",
            version="1",
            description="SASSIE Arctic Field Campaign Summary Ice Concentration Rankings from ML analysis of SBAND Images Fall 2022 version: 1"
        )

    SASSIE_L2_UNDER_ICE_FLOAT_V1_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SASSIE_L2_UNDER_ICE_FLOAT_V1_1",
            provider="POCLOUD", 
            shortname="SASSIE_L2_UNDER_ICE_FLOAT_V1",
            version="1",
            description="SASSIE Arctic Field Campaign Under Ice Float Fall 2022 Version 1 version: 1"
        )

    SASSIE_L2_WAVEGLIDERS_V1_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SASSIE_L2_WAVEGLIDERS_V1_1",
            provider="POCLOUD", 
            shortname="SASSIE_L2_WAVEGLIDERS_V1",
            version="1",
            description="SASSIE Arctic Field Campaign Wave Glider Data Fall 2022 Version 1 version: 1"
        )

    SCATSAT1_ESDR_ANCILLARY_L2_V11_V11_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SCATSAT1_ESDR_ANCILLARY_L2_V1.1_1.1",
            provider="POCLOUD", 
            shortname="SCATSAT1_ESDR_ANCILLARY_L2_V1.1",
            version="1.1",
            description="SCATSAT-1 ESDR Level 2 Ancillary Ocean Surface Fields Version 1.1 version: 1.1"
        )

    SCATSAT1_ESDR_L2_WIND_STRESS_V11_V11_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SCATSAT1_ESDR_L2_WIND_STRESS_V1.1_1.1",
            provider="POCLOUD", 
            shortname="SCATSAT1_ESDR_L2_WIND_STRESS_V1.1",
            version="1.1",
            description="SCATSAT-1 Scatterometer Inter-Calibrated ESDR Level 2 Ocean Surface Equivalent Neutral Wind Vectors and Wind Stress Vectors Version 1.1 version: 1.1"
        )

    WENTZ_SASS_SIGMA0_L2_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_WENTZ_SASS_SIGMA0_L2_1",
            provider="POCLOUD", 
            shortname="WENTZ_SASS_SIGMA0_L2",
            version="1",
            description="SEASAT SCATTEROMETER BINNED 50KM SIGMA-0 DATA (Wentz) version: 1"
        )

    ATLAS_DEALIASED_SASS_L2_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ATLAS_DEALIASED_SASS_L2_1",
            provider="POCLOUD", 
            shortname="ATLAS_DEALIASED_SASS_L2",
            version="1",
            description="SEASAT SCATTEROMETER DEALIASED OCEAN WIND VECTORS (Atlas) version: 1"
        )

    UCLA_DEALIASED_SASS_L3_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_UCLA_DEALIASED_SASS_L3_1",
            provider="POCLOUD", 
            shortname="UCLA_DEALIASED_SASS_L3",
            version="1",
            description="SEASAT SCATTEROMETER DEALIASED OCEAN WIND VECTORS (JPL-UCLA-AES) version: 1"
        )

    WAF_DEALIASED_SASS_L2_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_WAF_DEALIASED_SASS_L2_1",
            provider="POCLOUD", 
            shortname="WAF_DEALIASED_SASS_L2",
            version="1",
            description="SEASAT SCATTEROMETER DEALIASED OCEAN WIND VECTORS (Wentz et al.) version: 1"
        )

    CHELTON_SEASAT_SASS_L3_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_CHELTON_SEASAT_SASS_L3_1",
            provider="POCLOUD", 
            shortname="CHELTON_SEASAT_SASS_L3",
            version="1",
            description="SEASAT SCATTEROMETER DERIVED GLOBAL GRIDDED MONTHLY OCEAN WIND STRESS (Chelton) version: 1"
        )

    SPURS1_ADCP_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SPURS1_ADCP_1.0",
            provider="POCLOUD", 
            shortname="SPURS1_ADCP",
            version="1.0",
            description="SPURS-1 shipboard Acoustic Doppler Current Profiler data for N. Atlantic Endeavor and Knorr cruises version: 1.0"
        )

    SPURS1_METEO_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SPURS1_METEO_1.0",
            provider="POCLOUD", 
            shortname="SPURS1_METEO",
            version="1.0",
            description="SPURS-1 research vessel Meteorological series data for N. Atlantic Endeavor cruises version: 1.0"
        )

    SPURS1_CTD_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SPURS1_CTD_1.0",
            provider="POCLOUD", 
            shortname="SPURS1_CTD",
            version="1.0",
            description="SPURS-1 research vessel CTD profile data for N. Atlantic cruises version: 1.0"
        )

    SPURS1_TSG_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SPURS1_TSG_1.0",
            provider="POCLOUD", 
            shortname="SPURS1_TSG",
            version="1.0",
            description="SPURS-1 research vessel Thermosalinograph series data for N. Atlantic cruises version: 1.0"
        )

    SPURS1_UCTD_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SPURS1_UCTD_1.0",
            provider="POCLOUD", 
            shortname="SPURS1_UCTD",
            version="1.0",
            description="SPURS-1 research vessel Underway-CTD trajectory profile data for N. Atlantic Endeavor and Knorr cruises version: 1.0"
        )

    SPURS2_ARGO_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SPURS2_ARGO_1.0",
            provider="POCLOUD", 
            shortname="SPURS2_ARGO",
            version="1.0",
            description="SPURS-2 Argo float CTD profile data from the E. Tropical Pacific field campaign version: 1.0"
        )

    SPURS2_MOORING_CENTRAL_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SPURS2_MOORING_CENTRAL_1.0",
            provider="POCLOUD", 
            shortname="SPURS2_MOORING_CENTRAL",
            version="1.0",
            description="SPURS-2 Central mooring CTD, surface flux and meterorological data for the E. Tropical Pacific field campaign version: 1.0"
        )

    SPURS2_CFT_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SPURS2_CFT_1.0",
            provider="POCLOUD", 
            shortname="SPURS2_CFT",
            version="1.0",
            description="SPURS-2 Controlled Flux Technique (CFT) data for the E. Tropical Pacific field campaign R/V Revelle cruises version: 1.0"
        )

    SPURS2_DRIFTER_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SPURS2_DRIFTER_1.0",
            provider="POCLOUD", 
            shortname="SPURS2_DRIFTER",
            version="1.0",
            description="SPURS-2 Drifter data for the E. Tropical Pacific field campaign version: 1.0"
        )

    SPURS2_FLOAT_NEUTRALLYBUOYANT_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SPURS2_FLOAT_NEUTRALLYBUOYANT_1.0",
            provider="POCLOUD", 
            shortname="SPURS2_FLOAT_NEUTRALLYBUOYANT",
            version="1.0",
            description="SPURS-2 Neutrally buoyant float data for the E. Tropical Pacific field campaign version: 1.0"
        )

    SPURS2_MOORING_PICO_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SPURS2_MOORING_PICO_1.0",
            provider="POCLOUD", 
            shortname="SPURS2_MOORING_PICO",
            version="1.0",
            description="SPURS-2 PICO mooring data for the E. Tropical Pacific field campaign version: 1.0"
        )

    SPURS2_PALS_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SPURS2_PALS_1.0",
            provider="POCLOUD", 
            shortname="SPURS2_PALS",
            version="1.0",
            description="SPURS-2 Passive Accoustic Listener (PAL) data from ARGO float deployments during the E. Tropical Pacific field campaign version: 1.0"
        )

    SPURS2_RAWINSONDE_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SPURS2_RAWINSONDE_1.0",
            provider="POCLOUD", 
            shortname="SPURS2_RAWINSONDE",
            version="1.0",
            description="SPURS-2 Rawinsonde meteorological data for the E. Tropical Pacific field campaign R/V Revelle cruises version: 1.0"
        )

    SPURS2_METEO_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SPURS2_METEO_1.0",
            provider="POCLOUD", 
            shortname="SPURS2_METEO",
            version="1.0",
            description="SPURS-2 Research vessel Meteorological series data for the E. Tropical Pacific field campaign R/V Revelle cruises version: 1.0"
        )

    SPURS2_LADYAMBER_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SPURS2_LADYAMBER_1.0",
            provider="POCLOUD", 
            shortname="SPURS2_LADYAMBER",
            version="1.0",
            description="SPURS-2 S/V Lady Amber underway Thermosalinograph and Sea Snake data for the E. Tropical Pacific field campaign version: 1.0"
        )

    SPURS2_SAILDRONE_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SPURS2_SAILDRONE_1.0",
            provider="POCLOUD", 
            shortname="SPURS2_SAILDRONE",
            version="1.0",
            description="SPURS-2 Saildrone data for the E. Tropical Pacific field campaign version: 1.0"
        )

    SPURS2_SEAGLIDER_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SPURS2_SEAGLIDER_1.0",
            provider="POCLOUD", 
            shortname="SPURS2_SEAGLIDER",
            version="1.0",
            description="SPURS-2 Seaglider data for the E. Tropical Pacific field campaign version: 1.0"
        )

    SPURS2_SALINITYSNAKE_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SPURS2_SALINITYSNAKE_1.0",
            provider="POCLOUD", 
            shortname="SPURS2_SALINITYSNAKE",
            version="1.0",
            description="SPURS-2 Surface Salinity Snake data for the E. Tropical Pacific field campaign R/V Revelle cruises version: 1.0"
        )

    SPURS2_SSP_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SPURS2_SSP_1.0",
            provider="POCLOUD", 
            shortname="SPURS2_SSP",
            version="1.0",
            description="SPURS-2 Towed surface salinity profile (SSP) data for the E. Tropical Pacific R/V Revelle cruises version: 1.0"
        )

    SPURS2_WAVEGLIDER_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SPURS2_WAVEGLIDER_1.0",
            provider="POCLOUD", 
            shortname="SPURS2_WAVEGLIDER",
            version="1.0",
            description="SPURS-2 Waveglider data for the E. Tropical Pacific field campaign version: 1.0"
        )

    SPURS2_CTD_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SPURS2_CTD_1.0",
            provider="POCLOUD", 
            shortname="SPURS2_CTD",
            version="1.0",
            description="SPURS-2 research vessel CTD profile data for E. Tropical Pacific R/V Revelle cruises version: 1.0"
        )

    SPURS2_XBT_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SPURS2_XBT_1.0",
            provider="POCLOUD", 
            shortname="SPURS2_XBT",
            version="1.0",
            description="SPURS-2 research vessel Expendable Bathythermograph (XBT) profile data for E. Tropical Pacific R/V Revelle cruises version: 1.0"
        )

    SPURS2_UCTD_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SPURS2_UCTD_1.0",
            provider="POCLOUD", 
            shortname="SPURS2_UCTD",
            version="1.0",
            description="SPURS-2 research vessel Underway CTD (uCTD) data for the E. Tropical Pacific R/V Revelle cruises version: 1.0"
        )

    SPURS2_USPS_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SPURS2_USPS_1.0",
            provider="POCLOUD", 
            shortname="SPURS2_USPS",
            version="1.0",
            description="SPURS-2 research vessel Underway Salinity Profiling System (USPS) data for the E. Tropical Pacific R/V Revelle cruises version: 1.0"
        )

    SPURS2_RAINRADAR_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SPURS2_RAINRADAR_1.0",
            provider="POCLOUD", 
            shortname="SPURS2_RAINRADAR",
            version="1.0",
            description="SPURS-2 research vessel along track SEA-POL rain radar imaging data for E. Tropical Pacific R/V Revelle-2 cruise version: 1.0"
        )

    SPURS2_WAMOS_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SPURS2_WAMOS_1.0",
            provider="POCLOUD", 
            shortname="SPURS2_WAMOS",
            version="1.0",
            description="SPURS-2 research vessel along track WAMOS wave radar data for the second R/V Revelle cruise in the E. Tropical Pacific version: 1.0"
        )

    SPURS2_ADCP_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SPURS2_ADCP_1.0",
            provider="POCLOUD", 
            shortname="SPURS2_ADCP",
            version="1.0",
            description="SPURS-2 shipboard Acoustic Doppler Current Profiler data for E. Tropical Pacific R/V Revelle cruises version: 1.0"
        )

    SPURS2_XBAND_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SPURS2_XBAND_1.0",
            provider="POCLOUD", 
            shortname="SPURS2_XBAND",
            version="1.0",
            description="SPURS-2 shipboard X-band radar backscatter data for the E. Tropical Pacific field campaign version: 1.0"
        )

    SPURS2_XBAND_IMG_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SPURS2_XBAND_IMG_1.0",
            provider="POCLOUD", 
            shortname="SPURS2_XBAND_IMG",
            version="1.0",
            description="SPURS-2 shipboard X-band radar backscatter images for the 2016 E. Tropical Pacific field campaign version: 1.0"
        )

    SPURS2_DISDR_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SPURS2_DISDR_1.0",
            provider="POCLOUD", 
            shortname="SPURS2_DISDR",
            version="1.0",
            description="SPURS-2 shipboard disdrometer data for the E. Tropical Pacific field campaign version: 1.0"
        )

    SPURS2_UNDERWAY_PCO2_DIC_PH_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SPURS2_UNDERWAY_pCO2_DIC_pH_1.0",
            provider="POCLOUD", 
            shortname="SPURS2_UNDERWAY_pCO2_DIC_pH",
            version="1.0",
            description="SPURS-2 underway surface pCO2, DIC and pH data for the E. Tropical Pacific field campaign R/V Revelle cruises version: 1.0"
        )

    SWOT_PRELAUNCH_L2_GPS_V1_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_PRELAUNCH_L2_GPS_V1_1.0",
            provider="POCLOUD", 
            shortname="SWOT_PRELAUNCH_L2_GPS_V1",
            version="1.0",
            description="SWOT 2019-2020 Prelaunch Oceanography Field Campaign JPL Global Positioning Systems (GPS) version: 1.0"
        )

    SWOT_PRELAUNCH_L2_BPR_V1_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_PRELAUNCH_L2_BPR_V1_1.0",
            provider="POCLOUD", 
            shortname="SWOT_PRELAUNCH_L2_BPR_V1",
            version="1.0",
            description="SWOT 2019-2020 Prelaunch Oceanography Field Campaign NOAA Bottom Pressure Recorders (BPR) version: 1.0"
        )

    SWOT_PRELAUNCH_L2_PRAWLER_V1_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_PRELAUNCH_L2_PRAWLER_V1_1.0",
            provider="POCLOUD", 
            shortname="SWOT_PRELAUNCH_L2_PRAWLER_V1",
            version="1.0",
            description="SWOT 2019-2020 Prelaunch Oceanography Field Campaign NOAA Prawlers version: 1.0"
        )

    SWOT_PRELAUNCH_L2_GLIDER_V1_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_PRELAUNCH_L2_GLIDER_V1_1.0",
            provider="POCLOUD", 
            shortname="SWOT_PRELAUNCH_L2_GLIDER_V1",
            version="1.0",
            description="SWOT 2019-2020 Prelaunch Oceanography Field Campaign Rutgers Slocum Gliders version: 1.0"
        )

    SWOT_PRELAUNCH_L2_SIOCTD_V1_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_PRELAUNCH_L2_SIOCTD_V1_1.0",
            provider="POCLOUD", 
            shortname="SWOT_PRELAUNCH_L2_SIOCTD_V1",
            version="1.0",
            description="SWOT 2019-2020 Prelaunch Oceanography Field Campaign SIO Moored Fixed-Depth CTDs version: 1.0"
        )

    SWOT_PRELAUNCH_L2_WW_V1_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_PRELAUNCH_L2_WW_V1_1.0",
            provider="POCLOUD", 
            shortname="SWOT_PRELAUNCH_L2_WW_V1",
            version="1.0",
            description="SWOT 2019-2020 Prelaunch Oceanography Field Campaign SIO Mooring WireWalker (WW) version: 1.0"
        )

    SWOT_PRELAUNCH_L2_PIES_V1_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_PRELAUNCH_L2_PIES_V1_1.0",
            provider="POCLOUD", 
            shortname="SWOT_PRELAUNCH_L2_PIES_V1",
            version="1.0",
            description="SWOT 2019-2020 Prelaunch Oceanography Field Campaign SIO Pressure-sensing Inverted Echo Sounder (PIES) version: 1.0"
        )

    SWOT_PRELAUNCH_L2_WHOICTD_V1_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_PRELAUNCH_L2_WHOICTD_V1_1.0",
            provider="POCLOUD", 
            shortname="SWOT_PRELAUNCH_L2_WHOICTD_V1",
            version="1.0",
            description="SWOT 2019-2020 Prelaunch Oceanography Field Campaign WHOI/NOAA Moored Fixed-Depth CTDs version: 1.0"
        )

    SWOT_L1_DORIS_RINEX_10_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_L1_DORIS_RINEX_1.0_1.0",
            provider="POCLOUD", 
            shortname="SWOT_L1_DORIS_RINEX_1.0",
            version="1.0",
            description="SWOT Level 1 Onboard Tracking Data from Doppler Orbitography and Radiopositioning Integrated by Satellite (DORIS) version: 1.0"
        )

    SWOT_L1_GPSP_RINEX_10_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_L1_GPSP_RINEX_1.0_1.0",
            provider="POCLOUD", 
            shortname="SWOT_L1_GPSP_RINEX_1.0",
            version="1.0",
            description="SWOT Level 1 Onboard Tracking Data from Global Positioning System Payload (GPSP) version: 1.0"
        )

    SWOT_L1B_HR_SLC_11_V11_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_L1B_HR_SLC_1.1_1.1",
            provider="POCLOUD", 
            shortname="SWOT_L1B_HR_SLC_1.1",
            version="1.1",
            description="SWOT Level 1B High-Rate Single-look Complex Data Product, Version 1.1 version: 1.1"
        )

    SWOT_L1B_HR_SLC_20_V20_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_L1B_HR_SLC_2.0_2.0",
            provider="POCLOUD", 
            shortname="SWOT_L1B_HR_SLC_2.0",
            version="2.0",
            description="SWOT Level 1B High-Rate Single-look Complex Data Product, Version C version: 2.0"
        )

    SWOT_L1B_LR_INTF_10_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_L1B_LR_INTF_1.0_1.0",
            provider="POCLOUD", 
            shortname="SWOT_L1B_LR_INTF_1.0",
            version="1.0",
            description="SWOT Level 1B Low-Rate Interferogram Data Product, Version 1.0 version: 1.0"
        )

    SWOT_L1B_LR_INTF_11_V11_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_L1B_LR_INTF_1.1_1.1",
            provider="POCLOUD", 
            shortname="SWOT_L1B_LR_INTF_1.1",
            version="1.1",
            description="SWOT Level 1B Low-Rate Interferogram Data Product, Version 1.1 version: 1.1"
        )

    SWOT_L1B_LR_INTF_20_V20_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_L1B_LR_INTF_2.0_2.0",
            provider="POCLOUD", 
            shortname="SWOT_L1B_LR_INTF_2.0",
            version="2.0",
            description="SWOT Level 1B Low-Rate Interferogram Data Product, Version C version: 2.0"
        )

    SWOT_L2_LR_SSH_BASIC_20_V20_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_L2_LR_SSH_BASIC_2.0_2.0",
            provider="POCLOUD", 
            shortname="SWOT_L2_LR_SSH_BASIC_2.0",
            version="2.0",
            description="SWOT Level 2 KaRIn Low Rate Sea Surface Height Data Product - Basic, Version C version: 2.0"
        )

    SWOT_L2_LR_SSH_EXPERT_20_V20_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_L2_LR_SSH_EXPERT_2.0_2.0",
            provider="POCLOUD", 
            shortname="SWOT_L2_LR_SSH_EXPERT_2.0",
            version="2.0",
            description="SWOT Level 2 KaRIn Low Rate Sea Surface Height Data Product - Expert, Version C version: 2.0"
        )

    SWOT_L2_LR_SSH_UNSMOOTHED_20_V20_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_L2_LR_SSH_UNSMOOTHED_2.0_2.0",
            provider="POCLOUD", 
            shortname="SWOT_L2_LR_SSH_UNSMOOTHED_2.0",
            version="2.0",
            description="SWOT Level 2 KaRIn Low Rate Sea Surface Height Data Product - Unsmoothed, Version C version: 2.0"
        )

    SWOT_L2_LR_SSH_WINDWAVE_20_V20_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_L2_LR_SSH_WINDWAVE_2.0_2.0",
            provider="POCLOUD", 
            shortname="SWOT_L2_LR_SSH_WINDWAVE_2.0",
            version="2.0",
            description="SWOT Level 2 KaRIn Low Rate Sea Surface Height Data Product - WindWave, Version C version: 2.0"
        )

    SWOT_L2_LR_SSH_10_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_L2_LR_SSH_1.0_1.0",
            provider="POCLOUD", 
            shortname="SWOT_L2_LR_SSH_1.0",
            version="1.0",
            description="SWOT Level 2 KaRIn Low Rate Sea Surface Height Data Product, Version 1.0 version: 1.0"
        )

    SWOT_L2_LR_SSH_11_V11_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_L2_LR_SSH_1.1_1.1",
            provider="POCLOUD", 
            shortname="SWOT_L2_LR_SSH_1.1",
            version="1.1",
            description="SWOT Level 2 KaRIn Low Rate Sea Surface Height Data Product, Version 1.1 version: 1.1"
        )

    SWOT_L2_LR_SSH_20_V20_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_L2_LR_SSH_2.0_2.0",
            provider="POCLOUD", 
            shortname="SWOT_L2_LR_SSH_2.0",
            version="2.0",
            description="SWOT Level 2 KaRIn Low Rate Sea Surface Height Data Product, Version C version: 2.0"
        )

    SWOT_L2_HR_LAKEAVG_20_V20_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_L2_HR_LakeAvg_2.0_2.0",
            provider="POCLOUD", 
            shortname="SWOT_L2_HR_LakeAvg_2.0",
            version="2.0",
            description="SWOT Level 2 Lake Cycle-Averaged Data Product, Version 2.0 version: 2.0"
        )

    SWOT_L2_HR_LAKESP_11_V11_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_L2_HR_LakeSP_1.1_1.1",
            provider="POCLOUD", 
            shortname="SWOT_L2_HR_LakeSP_1.1",
            version="1.1",
            description="SWOT Level 2 Lake Single-Pass Vector Data Product, Version 1.1 version: 1.1"
        )

    SWOT_L2_HR_LAKESP_20_V20_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_L2_HR_LakeSP_2.0_2.0",
            provider="POCLOUD", 
            shortname="SWOT_L2_HR_LakeSP_2.0",
            version="2.0",
            description="SWOT Level 2 Lake Single-Pass Vector Data Product, Version C version: 2.0"
        )

    SWOT_L2_HR_LAKESP_OBS_20_V20_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_L2_HR_LakeSP_obs_2.0_2.0",
            provider="POCLOUD", 
            shortname="SWOT_L2_HR_LakeSP_obs_2.0",
            version="2.0",
            description="SWOT Level 2 Lake Single-Pass Vector Obs Data Product, Version C version: 2.0"
        )

    SWOT_L2_HR_LAKESP_PRIOR_20_V20_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_L2_HR_LakeSP_prior_2.0_2.0",
            provider="POCLOUD", 
            shortname="SWOT_L2_HR_LakeSP_prior_2.0",
            version="2.0",
            description="SWOT Level 2 Lake Single-Pass Vector Prior Data Product, Version C version: 2.0"
        )

    SWOT_L2_HR_LAKESP_UNASSIGNED_20_V20_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_L2_HR_LakeSP_unassigned_2.0_2.0",
            provider="POCLOUD", 
            shortname="SWOT_L2_HR_LakeSP_unassigned_2.0",
            version="2.0",
            description="SWOT Level 2 Lake Single-Pass Vector Unassigned Data Product, Version C version: 2.0"
        )

    SWOT_L2_NALT_GDR_20_V20_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_L2_NALT_GDR_2.0_2.0",
            provider="POCLOUD", 
            shortname="SWOT_L2_NALT_GDR_2.0",
            version="2.0",
            description="SWOT Level 2 Nadir Altimeter Geophysical Data Record with Waveforms version: 2.0"
        )

    SWOT_L2_NALT_GDR_GDR_20_V20_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_L2_NALT_GDR_GDR_2.0_2.0",
            provider="POCLOUD", 
            shortname="SWOT_L2_NALT_GDR_GDR_2.0",
            version="2.0",
            description="SWOT Level 2 Nadir Altimeter Geophysical Data Record with Waveforms - GDR version: 2.0"
        )

    SWOT_L2_NALT_GDR_SGDR_20_V20_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_L2_NALT_GDR_SGDR_2.0_2.0",
            provider="POCLOUD", 
            shortname="SWOT_L2_NALT_GDR_SGDR_2.0",
            version="2.0",
            description="SWOT Level 2 Nadir Altimeter Geophysical Data Record with Waveforms - SGDR version: 2.0"
        )

    SWOT_L2_NALT_GDR_SSHA_20_V20_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_L2_NALT_GDR_SSHA_2.0_2.0",
            provider="POCLOUD", 
            shortname="SWOT_L2_NALT_GDR_SSHA_2.0",
            version="2.0",
            description="SWOT Level 2 Nadir Altimeter Geophysical Data Record with Waveforms - SSHA version: 2.0"
        )

    SWOT_L2_NALT_IGDR_20_V20_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_L2_NALT_IGDR_2.0_2.0",
            provider="POCLOUD", 
            shortname="SWOT_L2_NALT_IGDR_2.0",
            version="2.0",
            description="SWOT Level 2 Nadir Altimeter Interim Geophysical Data Record with Waveforms version: 2.0"
        )

    SWOT_L2_NALT_IGDR_GDR_20_V20_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_L2_NALT_IGDR_GDR_2.0_2.0",
            provider="POCLOUD", 
            shortname="SWOT_L2_NALT_IGDR_GDR_2.0",
            version="2.0",
            description="SWOT Level 2 Nadir Altimeter Interim Geophysical Data Record with Waveforms - GDR version: 2.0"
        )

    SWOT_L2_NALT_IGDR_GDR_10_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_L2_NALT_IGDR_GDR_1.0_1.0",
            provider="POCLOUD", 
            shortname="SWOT_L2_NALT_IGDR_GDR_1.0",
            version="1.0",
            description="SWOT Level 2 Nadir Altimeter Interim Geophysical Data Record with Waveforms - GDR, Version 1.0 version: 1.0"
        )

    SWOT_L2_NALT_IGDR_SGDR_20_V20_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_L2_NALT_IGDR_SGDR_2.0_2.0",
            provider="POCLOUD", 
            shortname="SWOT_L2_NALT_IGDR_SGDR_2.0",
            version="2.0",
            description="SWOT Level 2 Nadir Altimeter Interim Geophysical Data Record with Waveforms - SGDR version: 2.0"
        )

    SWOT_L2_NALT_IGDR_SGDR_10_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_L2_NALT_IGDR_SGDR_1.0_1.0",
            provider="POCLOUD", 
            shortname="SWOT_L2_NALT_IGDR_SGDR_1.0",
            version="1.0",
            description="SWOT Level 2 Nadir Altimeter Interim Geophysical Data Record with Waveforms - SGDR, Version 1.0 version: 1.0"
        )

    SWOT_L2_NALT_IGDR_SSHA_20_V20_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_L2_NALT_IGDR_SSHA_2.0_2.0",
            provider="POCLOUD", 
            shortname="SWOT_L2_NALT_IGDR_SSHA_2.0",
            version="2.0",
            description="SWOT Level 2 Nadir Altimeter Interim Geophysical Data Record with Waveforms - SSHA version: 2.0"
        )

    SWOT_L2_NALT_IGDR_SSHA_10_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_L2_NALT_IGDR_SSHA_1.0_1.0",
            provider="POCLOUD", 
            shortname="SWOT_L2_NALT_IGDR_SSHA_1.0",
            version="1.0",
            description="SWOT Level 2 Nadir Altimeter Interim Geophysical Data Record with Waveforms - SSHA, Version 1.0 version: 1.0"
        )

    SWOT_L2_NALT_IGDR_10_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_L2_NALT_IGDR_1.0_1.0",
            provider="POCLOUD", 
            shortname="SWOT_L2_NALT_IGDR_1.0",
            version="1.0",
            description="SWOT Level 2 Nadir Altimeter Interim Geophysical Data Record with Waveforms, Version 1.0 version: 1.0"
        )

    SWOT_L2_NALT_OGDR_20_V20_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_L2_NALT_OGDR_2.0_2.0",
            provider="POCLOUD", 
            shortname="SWOT_L2_NALT_OGDR_2.0",
            version="2.0",
            description="SWOT Level 2 Nadir Altimeter Operational Geophysical Data Record with Waveforms version: 2.0"
        )

    SWOT_L2_NALT_OGDR_GDR_20_V20_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_L2_NALT_OGDR_GDR_2.0_2.0",
            provider="POCLOUD", 
            shortname="SWOT_L2_NALT_OGDR_GDR_2.0",
            version="2.0",
            description="SWOT Level 2 Nadir Altimeter Operational Geophysical Data Record with Waveforms - GDR version: 2.0"
        )

    SWOT_L2_NALT_OGDR_GDR_10_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_L2_NALT_OGDR_GDR_1.0_1.0",
            provider="POCLOUD", 
            shortname="SWOT_L2_NALT_OGDR_GDR_1.0",
            version="1.0",
            description="SWOT Level 2 Nadir Altimeter Operational Geophysical Data Record with Waveforms - GDR, Version 1.0 version: 1.0"
        )

    SWOT_L2_NALT_OGDR_SSHA_20_V20_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_L2_NALT_OGDR_SSHA_2.0_2.0",
            provider="POCLOUD", 
            shortname="SWOT_L2_NALT_OGDR_SSHA_2.0",
            version="2.0",
            description="SWOT Level 2 Nadir Altimeter Operational Geophysical Data Record with Waveforms - SSHA version: 2.0"
        )

    SWOT_L2_NALT_OGDR_SSHA_10_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_L2_NALT_OGDR_SSHA_1.0_1.0",
            provider="POCLOUD", 
            shortname="SWOT_L2_NALT_OGDR_SSHA_1.0",
            version="1.0",
            description="SWOT Level 2 Nadir Altimeter Operational Geophysical Data Record with Waveforms - SSHA, Version 1.0 version: 1.0"
        )

    SWOT_L2_NALT_OGDR_10_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_L2_NALT_OGDR_1.0_1.0",
            provider="POCLOUD", 
            shortname="SWOT_L2_NALT_OGDR_1.0",
            version="1.0",
            description="SWOT Level 2 Nadir Altimeter Operational Geophysical Data Record with Waveforms, Version 1.0 version: 1.0"
        )

    SWOT_L2_RAD_GDR_20_V20_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_L2_RAD_GDR_2.0_2.0",
            provider="POCLOUD", 
            shortname="SWOT_L2_RAD_GDR_2.0",
            version="2.0",
            description="SWOT Level 2 Radiometer Brightness Temperatures and Troposphere Data Product version: 2.0"
        )

    SWOT_L2_RAD_IGDR_20_V20_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_L2_RAD_IGDR_2.0_2.0",
            provider="POCLOUD", 
            shortname="SWOT_L2_RAD_IGDR_2.0",
            version="2.0",
            description="SWOT Level 2 Radiometer Brightness Temperatures and Troposphere Interim Data Product version: 2.0"
        )

    SWOT_L2_RAD_IGDR_10_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_L2_RAD_IGDR_1.0_1.0",
            provider="POCLOUD", 
            shortname="SWOT_L2_RAD_IGDR_1.0",
            version="1.0",
            description="SWOT Level 2 Radiometer Brightness Temperatures and Troposphere Interim Data Product, Version 1.0 version: 1.0"
        )

    SWOT_L2_RAD_OGDR_20_V20_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_L2_RAD_OGDR_2.0_2.0",
            provider="POCLOUD", 
            shortname="SWOT_L2_RAD_OGDR_2.0",
            version="2.0",
            description="SWOT Level 2 Radiometer Brightness Temperatures and Troposphere Operational Data Product version: 2.0"
        )

    SWOT_L2_RAD_OGDR_10_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_L2_RAD_OGDR_1.0_1.0",
            provider="POCLOUD", 
            shortname="SWOT_L2_RAD_OGDR_1.0",
            version="1.0",
            description="SWOT Level 2 Radiometer Brightness Temperatures and Troposphere Operational Data Product, Version 1.0 version: 1.0"
        )

    SWOT_L2_HR_RIVERAVG_20_V20_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_L2_HR_RiverAvg_2.0_2.0",
            provider="POCLOUD", 
            shortname="SWOT_L2_HR_RiverAvg_2.0",
            version="2.0",
            description="SWOT Level 2 River Cycle-Averaged Data Product, Version C version: 2.0"
        )

    SWOT_L2_HR_RIVERSP_11_V11_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_L2_HR_RiverSP_1.1_1.1",
            provider="POCLOUD", 
            shortname="SWOT_L2_HR_RiverSP_1.1",
            version="1.1",
            description="SWOT Level 2 River Single-Pass Vector Data Product, Version 1.1 version: 1.1"
        )

    SWOT_L2_HR_RIVERSP_20_V20_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_L2_HR_RiverSP_2.0_2.0",
            provider="POCLOUD", 
            shortname="SWOT_L2_HR_RiverSP_2.0",
            version="2.0",
            description="SWOT Level 2 River Single-Pass Vector Data Product, Version C version: 2.0"
        )

    SWOT_L2_HR_RIVERSP_NODE_20_V20_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_L2_HR_RiverSP_node_2.0_2.0",
            provider="POCLOUD", 
            shortname="SWOT_L2_HR_RiverSP_node_2.0",
            version="2.0",
            description="SWOT Level 2 River Single-Pass Vector Node Data Product, Version C version: 2.0"
        )

    SWOT_L2_HR_RIVERSP_REACH_20_V20_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_L2_HR_RiverSP_reach_2.0_2.0",
            provider="POCLOUD", 
            shortname="SWOT_L2_HR_RiverSP_reach_2.0",
            version="2.0",
            description="SWOT Level 2 River Single-Pass Vector Reach Data Product, Version C version: 2.0"
        )

    SWOT_L2_HR_PIXCVEC_11_V11_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_L2_HR_PIXCVec_1.1_1.1",
            provider="POCLOUD", 
            shortname="SWOT_L2_HR_PIXCVec_1.1",
            version="1.1",
            description="SWOT Level 2 Water Mask Pixel Cloud Auxiliary Data Product, Version 1.1 version: 1.1"
        )

    SWOT_L2_HR_PIXCVEC_20_V20_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_L2_HR_PIXCVec_2.0_2.0",
            provider="POCLOUD", 
            shortname="SWOT_L2_HR_PIXCVec_2.0",
            version="2.0",
            description="SWOT Level 2 Water Mask Pixel Cloud Auxiliary Data Product, Version C version: 2.0"
        )

    SWOT_L2_HR_PIXC_11_V11_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_L2_HR_PIXC_1.1_1.1",
            provider="POCLOUD", 
            shortname="SWOT_L2_HR_PIXC_1.1",
            version="1.1",
            description="SWOT Level 2 Water Mask Pixel Cloud Data Product, Version 1.1 version: 1.1"
        )

    SWOT_L2_HR_PIXC_20_V20_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_L2_HR_PIXC_2.0_2.0",
            provider="POCLOUD", 
            shortname="SWOT_L2_HR_PIXC_2.0",
            version="2.0",
            description="SWOT Level 2 Water Mask Pixel Cloud Data Product, Version C version: 2.0"
        )

    SWOT_L2_HR_RASTER_100M_20_V20_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_L2_HR_Raster_100m_2.0_2.0",
            provider="POCLOUD", 
            shortname="SWOT_L2_HR_Raster_100m_2.0",
            version="2.0",
            description="SWOT Level 2 Water Mask Raster Image 100m Data Product, Version C version: 2.0"
        )

    SWOT_L2_HR_RASTER_250M_20_V20_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_L2_HR_Raster_250m_2.0_2.0",
            provider="POCLOUD", 
            shortname="SWOT_L2_HR_Raster_250m_2.0",
            version="2.0",
            description="SWOT Level 2 Water Mask Raster Image 250m Data Product, Version C version: 2.0"
        )

    SWOT_L2_HR_RASTER_11_V11_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_L2_HR_Raster_1.1_1.1",
            provider="POCLOUD", 
            shortname="SWOT_L2_HR_Raster_1.1",
            version="1.1",
            description="SWOT Level 2 Water Mask Raster Image Data Product, Version 1.1 version: 1.1"
        )

    SWOT_L2_HR_RASTER_20_V20_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_L2_HR_Raster_2.0_2.0",
            provider="POCLOUD", 
            shortname="SWOT_L2_HR_Raster_2.0",
            version="2.0",
            description="SWOT Level 2 Water Mask Raster Image Data Product, Version C version: 2.0"
        )

    SWOT_MOE_10_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_MOE_1.0_1.0",
            provider="POCLOUD", 
            shortname="SWOT_MOE_1.0",
            version="1.0",
            description="SWOT Medium-accuracy Orbit Ephemeris (MOE) version: 1.0"
        )

    SWOT_POE_20_V20_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_POE_2.0_2.0",
            provider="POCLOUD", 
            shortname="SWOT_POE_2.0",
            version="2.0",
            description="SWOT Precise Orbit Ephemeris (POE) version: 2.0"
        )

    SWOT_SAT_COM_10_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_SAT_COM_1.0_1.0",
            provider="POCLOUD", 
            shortname="SWOT_SAT_COM_1.0",
            version="1.0",
            description="SWOT Satellite Center of Mass Position Data version: 1.0"
        )

    SWOT_ATTD_RECONST_20_V20_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_ATTD_RECONST_2.0_2.0",
            provider="POCLOUD", 
            shortname="SWOT_ATTD_RECONST_2.0",
            version="2.0",
            description="SWOT Satellite Reconstructed Attitude Data version: 2.0"
        )

    SWOT_SIMULATED_NA_CONTINENT_L2_HR_PIXC_V1_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_SIMULATED_NA_CONTINENT_L2_HR_PIXC_V1_1.0",
            provider="POCLOUD", 
            shortname="SWOT_SIMULATED_NA_CONTINENT_L2_HR_PIXC_V1",
            version="1.0",
            description="SWOT Simulated Level 2 North America Continent KaRIn High Rate Water Mask Pixel Cloud Product Version 1.0 version: 1.0"
        )

    SWOT_SIMULATED_NA_CONTINENT_L2_HR_LAKESP_V1_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_SIMULATED_NA_CONTINENT_L2_HR_LAKESP_V1_1.0",
            provider="POCLOUD", 
            shortname="SWOT_SIMULATED_NA_CONTINENT_L2_HR_LAKESP_V1",
            version="1.0",
            description="SWOT Simulated Level 2 North America Continent High Rate Lake Vectors Product Version 1.0 version: 1.0"
        )

    SWOT_SIMULATED_NA_CONTINENT_L2_HR_RASTER_V1_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_SIMULATED_NA_CONTINENT_L2_HR_RASTER_V1_1.0",
            provider="POCLOUD", 
            shortname="SWOT_SIMULATED_NA_CONTINENT_L2_HR_RASTER_V1",
            version="1.0",
            description="SWOT Simulated Level 2 North America Continent High Rate Raster Product Version 1.0 version: 1.0"
        )

    SWOT_SIMULATED_NA_CONTINENT_L2_HR_RIVERSP_V1_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_SIMULATED_NA_CONTINENT_L2_HR_RIVERSP_V1_1.0",
            provider="POCLOUD", 
            shortname="SWOT_SIMULATED_NA_CONTINENT_L2_HR_RIVERSP_V1",
            version="1.0",
            description="SWOT Simulated Level 2 North America Continent High Rate River Vectors Product Version 1.0 version: 1.0"
        )

    SWOT_SIMULATED_NA_CONTINENT_L2_HR_PIXCVEC_V1_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_SIMULATED_NA_CONTINENT_L2_HR_PIXCVEC_V1_1.0",
            provider="POCLOUD", 
            shortname="SWOT_SIMULATED_NA_CONTINENT_L2_HR_PIXCVEC_V1",
            version="1.0",
            description="SWOT Simulated Level 2 North America Continent KaRIn High Rate Pixel Cloud Vector Attribute Product Version 1.0 version: 1.0"
        )

    SWOT_SIMULATED_L2_KARIN_SSH_GLORYS_CALVAL_V1_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_SIMULATED_L2_KARIN_SSH_GLORYS_CALVAL_V1_1",
            provider="POCLOUD", 
            shortname="SWOT_SIMULATED_L2_KARIN_SSH_GLORYS_CALVAL_V1",
            version="1",
            description="SWOT Simulated Level-2 KaRIn SSH from GLORYS for Cal/Val Version 1 version: 1"
        )

    SWOT_SIMULATED_L2_KARIN_SSH_GLORYS_SCIENCE_V1_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_SIMULATED_L2_KARIN_SSH_GLORYS_SCIENCE_V1_1",
            provider="POCLOUD", 
            shortname="SWOT_SIMULATED_L2_KARIN_SSH_GLORYS_SCIENCE_V1",
            version="1",
            description="SWOT Simulated Level-2 KaRIn SSH from GLORYS for Science Version 1 version: 1"
        )

    SWOT_SIMULATED_L2_KARIN_SSH_ECCO_LLC4320_CALVAL_V1_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_SIMULATED_L2_KARIN_SSH_ECCO_LLC4320_CALVAL_V1_1",
            provider="POCLOUD", 
            shortname="SWOT_SIMULATED_L2_KARIN_SSH_ECCO_LLC4320_CALVAL_V1",
            version="1",
            description="SWOT Simulated Level-2 KaRIn SSH from MITgcm ECCO LLC4320 for Cal/Val Version 1 version: 1"
        )

    SWOT_SIMULATED_L2_KARIN_SSH_ECCO_LLC4320_SCIENCE_V1_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_SIMULATED_L2_KARIN_SSH_ECCO_LLC4320_SCIENCE_V1_1",
            provider="POCLOUD", 
            shortname="SWOT_SIMULATED_L2_KARIN_SSH_ECCO_LLC4320_SCIENCE_V1",
            version="1",
            description="SWOT Simulated Level-2 KaRIn SSH from MITgcm ECCO LLC4320 for Science Version 1 version: 1"
        )

    SWOT_SIMULATED_L2_NADIR_SSH_GLORYS_CALVAL_V1_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_SIMULATED_L2_NADIR_SSH_GLORYS_CALVAL_V1_1",
            provider="POCLOUD", 
            shortname="SWOT_SIMULATED_L2_NADIR_SSH_GLORYS_CALVAL_V1",
            version="1",
            description="SWOT Simulated Level-2 Nadir SSH from GLORYS for Cal/Val Version 1 version: 1"
        )

    SWOT_SIMULATED_L2_NADIR_SSH_GLORYS_SCIENCE_V1_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_SIMULATED_L2_NADIR_SSH_GLORYS_SCIENCE_V1_1",
            provider="POCLOUD", 
            shortname="SWOT_SIMULATED_L2_NADIR_SSH_GLORYS_SCIENCE_V1",
            version="1",
            description="SWOT Simulated Level-2 Nadir SSH from GLORYS for Science Version 1 version: 1"
        )

    SWOT_SIMULATED_L2_NADIR_SSH_ECCO_LLC4320_CALVAL_V1_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_SIMULATED_L2_NADIR_SSH_ECCO_LLC4320_CALVAL_V1_1",
            provider="POCLOUD", 
            shortname="SWOT_SIMULATED_L2_NADIR_SSH_ECCO_LLC4320_CALVAL_V1",
            version="1",
            description="SWOT Simulated Level-2 Nadir SSH from MITgcm ECCO LLC4320 for Cal/Val Version 1 version: 1"
        )

    SWOT_SIMULATED_L2_NADIR_SSH_ECCO_LLC4320_SCIENCE_V1_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_SIMULATED_L2_NADIR_SSH_ECCO_LLC4320_SCIENCE_V1_1",
            provider="POCLOUD", 
            shortname="SWOT_SIMULATED_L2_NADIR_SSH_ECCO_LLC4320_SCIENCE_V1",
            version="1",
            description="SWOT Simulated Level-2 Nadir SSH from MITgcm ECCO LLC4320 for Science Version 1 version: 1"
        )

    SWOT_L4_DAWG_SOS_DISCHARGE_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_L4_DAWG_SOS_DISCHARGE_1",
            provider="POCLOUD", 
            shortname="SWOT_L4_DAWG_SOS_DISCHARGE",
            version="1",
            description="SWOT Sword of Science River Discharge Products Version 1 version: 1"
        )

    SWOT_L3_LR_SSH_10_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SWOT_L3_LR_SSH_1.0_1.0",
            provider="POCLOUD", 
            shortname="SWOT_L3_LR_SSH_1.0",
            version="1.0",
            description="SWOT-AVISO Level 3 KaRIn Low Rate Sea Surface Height Data Products, Version 1.0 version: 1.0"
        )

    SAILDRONE_ARCTIC_2021_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SAILDRONE_ARCTIC_2021_1",
            provider="POCLOUD", 
            shortname="SAILDRONE_ARCTIC_2021",
            version="1",
            description="Saildrone 2021 Arctic field campaign for the Multi-Sensor Improved SST (MISST) project version: 1"
        )

    SAILDRONE_ARCTIC_2022_V1_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SAILDRONE_ARCTIC_2022_1",
            provider="POCLOUD", 
            shortname="SAILDRONE_ARCTIC_2022",
            version="1",
            description="Saildrone 2022 Arctic field campaign for the Multi-Sensor Improved SST (MISST) project version: 1"
        )

    SAILDRONE_ARCTIC_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SAILDRONE_ARCTIC_1.0",
            provider="POCLOUD", 
            shortname="SAILDRONE_ARCTIC",
            version="1.0",
            description="Saildrone Arctic field campaign surface and ADCP measurements for NOPP-MISST project version: 1.0"
        )

    SAILDRONE_BAJA_SURFACE_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SAILDRONE_BAJA_SURFACE_1.0",
            provider="POCLOUD", 
            shortname="SAILDRONE_BAJA_SURFACE",
            version="1.0",
            description="Saildrone Baja field campaign surface and ADCP measurements version: 1.0"
        )

    SAILDRONE_ATOMIC_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SAILDRONE_ATOMIC_1.0",
            provider="POCLOUD", 
            shortname="SAILDRONE_ATOMIC",
            version="1.0",
            description="Saildrone field campaign surface and ADCP measurements for the Atlantic Tradewind Ocean-Atmosphere Mesoscale Interaction Campaign (ATOMIC) project version: 1.0"
        )

    QSCAT_LEVEL_1B_V2_V2_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_QSCAT_LEVEL_1B_V2_2",
            provider="POCLOUD", 
            shortname="QSCAT_LEVEL_1B_V2",
            version="2",
            description="SeaWinds on QuikSCAT Level 1B Time-Ordered Earth-Located Sigma0 Version 2 version: 2"
        )

    SPURS1_SEAGLIDER_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SPURS1_SEAGLIDER_1.0",
            provider="POCLOUD", 
            shortname="SPURS1_SEAGLIDER",
            version="1.0",
            description="Seaglider CTD data for the SPURS-1 N. Atlantic field campaign version: 1.0"
        )

    SPURS1_SEASOAR_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SPURS1_SEASOAR_1.0",
            provider="POCLOUD", 
            shortname="SPURS1_SEASOAR",
            version="1.0",
            description="Seasoar CTD data for the SPURS-1 N. Atlantic field campaign version: 1.0"
        )

    JASON_CS_S6A_L1A_ALT_HR_NTC_F08_VF08_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_JASON_CS_S6A_L1A_ALT_HR_NTC_F08_F08",
            provider="POCLOUD", 
            shortname="JASON_CS_S6A_L1A_ALT_HR_NTC_F08",
            version="F08",
            description="Sentinel-6A MF Jason-CS L1A P4 Altimeter High Resolution (HR) NTC Intermediate Outputs with Instrument Calibrations F08 version: F08"
        )

    JASON_CS_S6A_L1A_ALT_HR_STC_F_VF_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_JASON_CS_S6A_L1A_ALT_HR_STC_F_F",
            provider="POCLOUD", 
            shortname="JASON_CS_S6A_L1A_ALT_HR_STC_F",
            version="F",
            description="Sentinel-6A MF Jason-CS L1A P4 Altimeter High Resolution (HR) STC Intermediate Outputs with Instrument Calibrations version: F"
        )

    JASON_CS_S6A_L1B_GNSS_POD_DAILY_VF_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_JASON_CS_S6A_L1B_GNSS_POD_DAILY_F",
            provider="POCLOUD", 
            shortname="JASON_CS_S6A_L1B_GNSS_POD_DAILY",
            version="F",
            description="Sentinel-6A MF Jason-CS L1B GNSS-POD Tracking Data Daily version: F"
        )

    JASON_CS_S6A_L1B_GNSS_POD_HOURLY_VF_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_JASON_CS_S6A_L1B_GNSS_POD_HOURLY_F",
            provider="POCLOUD", 
            shortname="JASON_CS_S6A_L1B_GNSS_POD_HOURLY",
            version="F",
            description="Sentinel-6A MF Jason-CS L1B GNSS-POD Tracking Data Hourly version: F"
        )

    JASON_CS_S6A_L1B_GNSS_RO_POD_HOURLY_VF_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_JASON_CS_S6A_L1B_GNSS_RO_POD_HOURLY_F",
            provider="POCLOUD", 
            shortname="JASON_CS_S6A_L1B_GNSS_RO_POD_HOURLY",
            version="F",
            description="Sentinel-6A MF Jason-CS L1B GNSS-RO-POD Tracking Data Hourly version: F"
        )

    JASON_CS_S6A_L1B_ALT_HR_NTC_F08_VF08_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_JASON_CS_S6A_L1B_ALT_HR_NTC_F08_F08",
            provider="POCLOUD", 
            shortname="JASON_CS_S6A_L1B_ALT_HR_NTC_F08",
            version="F08",
            description="Sentinel-6A MF Jason-CS L1B P4 Altimeter High Resolution (HR) NTC Geolocated Waveforms F08 version: F08"
        )

    JASON_CS_S6A_L1B_ALT_HR_STC_F_VF_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_JASON_CS_S6A_L1B_ALT_HR_STC_F_F",
            provider="POCLOUD", 
            shortname="JASON_CS_S6A_L1B_ALT_HR_STC_F",
            version="F",
            description="Sentinel-6A MF Jason-CS L1B P4 Altimeter High Resolution (HR) STC Geolocated Waveforms version: F"
        )

    JASON_CS_S6A_L1B_ALT_LR_NTC_F08_VF08_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_JASON_CS_S6A_L1B_ALT_LR_NTC_F08_F08",
            provider="POCLOUD", 
            shortname="JASON_CS_S6A_L1B_ALT_LR_NTC_F08",
            version="F08",
            description="Sentinel-6A MF Jason-CS L1B P4 Altimeter Low Resolution (LR) NTC Geolocated Waveforms F08 version: F08"
        )

    JASON_CS_S6A_L1B_ALT_LR_STC_F_VF_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_JASON_CS_S6A_L1B_ALT_LR_STC_F_F",
            provider="POCLOUD", 
            shortname="JASON_CS_S6A_L1B_ALT_LR_STC_F",
            version="F",
            description="Sentinel-6A MF Jason-CS L1B P4 Altimeter Low Resolution (LR) STC Geolocated Waveforms version: F"
        )

    JASON_CS_S6A_L2_AMR_RAD_NRT_VF_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_JASON_CS_S6A_L2_AMR_RAD_NRT_F",
            provider="POCLOUD", 
            shortname="JASON_CS_S6A_L2_AMR_RAD_NRT",
            version="F",
            description="Sentinel-6A MF Jason-CS L2 Advanced Microwave Radiometer (AMR-C) NRT Geophysical Parameters version: F"
        )

    JASON_CS_S6A_L2_AMR_RAD_NTC_F08_UNVALIDATED_VF08_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_JASON_CS_S6A_L2_AMR_RAD_NTC_F08_UNVALIDATED_F08",
            provider="POCLOUD", 
            shortname="JASON_CS_S6A_L2_AMR_RAD_NTC_F08_UNVALIDATED",
            version="F08",
            description="Sentinel-6A MF Jason-CS L2 Advanced Microwave Radiometer (AMR-C) NTC Geophysical Parameters (Unvalidated) F08 version: F08"
        )

    JASON_CS_S6A_L2_AMR_RAD_NTC_F08_VF08_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_JASON_CS_S6A_L2_AMR_RAD_NTC_F08_F08",
            provider="POCLOUD", 
            shortname="JASON_CS_S6A_L2_AMR_RAD_NTC_F08",
            version="F08",
            description="Sentinel-6A MF Jason-CS L2 Advanced Microwave Radiometer (AMR-C) NTC Geophysical Parameters F08 version: F08"
        )

    JASON_CS_S6A_L2_AMR_RAD_STC_VF_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_JASON_CS_S6A_L2_AMR_RAD_STC_F",
            provider="POCLOUD", 
            shortname="JASON_CS_S6A_L2_AMR_RAD_STC",
            version="F",
            description="Sentinel-6A MF Jason-CS L2 Advanced Microwave Radiometer (AMR-C) STC Geophysical Parameters version: F"
        )

    JASON_CS_S6A_L2_ALT_HR_STD_OST_NRT_F_VF_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_JASON_CS_S6A_L2_ALT_HR_STD_OST_NRT_F_F",
            provider="POCLOUD", 
            shortname="JASON_CS_S6A_L2_ALT_HR_STD_OST_NRT_F",
            version="F",
            description="Sentinel-6A MF Jason-CS L2 P4 Altimeter High Resolution (HR) NRT Ocean Surface Topography version: F"
        )

    JASON_CS_S6A_L2_ALT_HR_RED_OST_NRT_F_VF_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_JASON_CS_S6A_L2_ALT_HR_RED_OST_NRT_F_F",
            provider="POCLOUD", 
            shortname="JASON_CS_S6A_L2_ALT_HR_RED_OST_NRT_F",
            version="F",
            description="Sentinel-6A MF Jason-CS L2 P4 Altimeter High Resolution (HR) NRT Reduced Ocean Surface Topography version: F"
        )

    JASON_CS_S6A_L2_ALT_HR_STD_OST_NTC_F08_UNVALIDATED_VF08_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_JASON_CS_S6A_L2_ALT_HR_STD_OST_NTC_F08_UNVALIDATED_F08",
            provider="POCLOUD", 
            shortname="JASON_CS_S6A_L2_ALT_HR_STD_OST_NTC_F08_UNVALIDATED",
            version="F08",
            description="Sentinel-6A MF Jason-CS L2 P4 Altimeter High Resolution (HR) NTC Ocean Surface Topography (Unvalidated) F08 version: F08"
        )

    JASON_CS_S6A_L2_ALT_HR_STD_OST_NTC_F08_VF08_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_JASON_CS_S6A_L2_ALT_HR_STD_OST_NTC_F08_F08",
            provider="POCLOUD", 
            shortname="JASON_CS_S6A_L2_ALT_HR_STD_OST_NTC_F08",
            version="F08",
            description="Sentinel-6A MF Jason-CS L2 P4 Altimeter High Resolution (HR) NTC Ocean Surface Topography F08 version: F08"
        )

    JASON_CS_S6A_L2_ALT_HR_RED_OST_NTC_F08_UNVALIDATED_VF08_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_JASON_CS_S6A_L2_ALT_HR_RED_OST_NTC_F08_UNVALIDATED_F08",
            provider="POCLOUD", 
            shortname="JASON_CS_S6A_L2_ALT_HR_RED_OST_NTC_F08_UNVALIDATED",
            version="F08",
            description="Sentinel-6A MF Jason-CS L2 P4 Altimeter High Resolution (HR) NTC Reduced Ocean Surface Topography (Unvalidated) F08 version: F08"
        )

    JASON_CS_S6A_L2_ALT_HR_RED_OST_NTC_F08_VF08_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_JASON_CS_S6A_L2_ALT_HR_RED_OST_NTC_F08_F08",
            provider="POCLOUD", 
            shortname="JASON_CS_S6A_L2_ALT_HR_RED_OST_NTC_F08",
            version="F08",
            description="Sentinel-6A MF Jason-CS L2 P4 Altimeter High Resolution (HR) NTC Reduced Ocean Surface Topography F08 version: F08"
        )

    JASON_CS_S6A_L2_ALT_HR_STD_OST_STC_F_VF_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_JASON_CS_S6A_L2_ALT_HR_STD_OST_STC_F_F",
            provider="POCLOUD", 
            shortname="JASON_CS_S6A_L2_ALT_HR_STD_OST_STC_F",
            version="F",
            description="Sentinel-6A MF Jason-CS L2 P4 Altimeter High Resolution (HR) STC Ocean Surface Topography version: F"
        )

    JASON_CS_S6A_L2_ALT_HR_RED_OST_STC_F_VF_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_JASON_CS_S6A_L2_ALT_HR_RED_OST_STC_F_F",
            provider="POCLOUD", 
            shortname="JASON_CS_S6A_L2_ALT_HR_RED_OST_STC_F",
            version="F",
            description="Sentinel-6A MF Jason-CS L2 P4 Altimeter High Resolution (HR) STC Reduced Ocean Surface Topography version: F"
        )

    JASON_CS_S6A_L2_ALT_LR_STD_OST_NRT_F_VF_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_JASON_CS_S6A_L2_ALT_LR_STD_OST_NRT_F_F",
            provider="POCLOUD", 
            shortname="JASON_CS_S6A_L2_ALT_LR_STD_OST_NRT_F",
            version="F",
            description="Sentinel-6A MF Jason-CS L2 P4 Altimeter Low Resolution (LR) NRT Ocean Surface Topography version: F"
        )

    JASON_CS_S6A_L2_ALT_LR_RED_OST_NRT_F_VF_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_JASON_CS_S6A_L2_ALT_LR_RED_OST_NRT_F_F",
            provider="POCLOUD", 
            shortname="JASON_CS_S6A_L2_ALT_LR_RED_OST_NRT_F",
            version="F",
            description="Sentinel-6A MF Jason-CS L2 P4 Altimeter Low Resolution (LR) NRT Reduced Ocean Surface Topography version: F"
        )

    JASON_CS_S6A_L2_ALT_LR_STD_OST_NTC_F08_UNVALIDATED_VF08_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_JASON_CS_S6A_L2_ALT_LR_STD_OST_NTC_F08_UNVALIDATED_F08",
            provider="POCLOUD", 
            shortname="JASON_CS_S6A_L2_ALT_LR_STD_OST_NTC_F08_UNVALIDATED",
            version="F08",
            description="Sentinel-6A MF Jason-CS L2 P4 Altimeter Low Resolution (LR) NTC Ocean Surface Topography (Unvalidated) F08 version: F08"
        )

    JASON_CS_S6A_L2_ALT_LR_STD_OST_NTC_F08_VF08_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_JASON_CS_S6A_L2_ALT_LR_STD_OST_NTC_F08_F08",
            provider="POCLOUD", 
            shortname="JASON_CS_S6A_L2_ALT_LR_STD_OST_NTC_F08",
            version="F08",
            description="Sentinel-6A MF Jason-CS L2 P4 Altimeter Low Resolution (LR) NTC Ocean Surface Topography F08 version: F08"
        )

    JASON_CS_S6A_L2_ALT_LR_RED_OST_NTC_F08_UNVALIDATED_VF08_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_JASON_CS_S6A_L2_ALT_LR_RED_OST_NTC_F08_UNVALIDATED_F08",
            provider="POCLOUD", 
            shortname="JASON_CS_S6A_L2_ALT_LR_RED_OST_NTC_F08_UNVALIDATED",
            version="F08",
            description="Sentinel-6A MF Jason-CS L2 P4 Altimeter Low Resolution (LR) NTC Reduced Ocean Surface Topography (Unvalidated) F08 version: F08"
        )

    JASON_CS_S6A_L2_ALT_LR_RED_OST_NTC_F08_VF08_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_JASON_CS_S6A_L2_ALT_LR_RED_OST_NTC_F08_F08",
            provider="POCLOUD", 
            shortname="JASON_CS_S6A_L2_ALT_LR_RED_OST_NTC_F08",
            version="F08",
            description="Sentinel-6A MF Jason-CS L2 P4 Altimeter Low Resolution (LR) NTC Reduced Ocean Surface Topography F08 version: F08"
        )

    JASON_CS_S6A_L2_ALT_LR_STD_OST_STC_F_VF_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_JASON_CS_S6A_L2_ALT_LR_STD_OST_STC_F_F",
            provider="POCLOUD", 
            shortname="JASON_CS_S6A_L2_ALT_LR_STD_OST_STC_F",
            version="F",
            description="Sentinel-6A MF Jason-CS L2 P4 Altimeter Low Resolution (LR) STC Ocean Surface Topography version: F"
        )

    JASON_CS_S6A_L2_ALT_LR_RED_OST_STC_F_VF_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_JASON_CS_S6A_L2_ALT_LR_RED_OST_STC_F_F",
            provider="POCLOUD", 
            shortname="JASON_CS_S6A_L2_ALT_LR_RED_OST_STC_F",
            version="F",
            description="Sentinel-6A MF Jason-CS L2 P4 Altimeter Low Resolution (LR) STC Reduced Ocean Surface Topography version: F"
        )

    JASON_CS_S6A_L2P_ALT_HR_OST_NTC_F08_VF08_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_JASON_CS_S6A_L2P_ALT_HR_OST_NTC_F08_F08",
            provider="POCLOUD", 
            shortname="JASON_CS_S6A_L2P_ALT_HR_OST_NTC_F08",
            version="F08",
            description="Sentinel-6A MF Jason-CS L2P P4 Altimeter High Resolution (HR) NTC Ocean Surface Topography F08 version: F08"
        )

    JASON_CS_S6A_L2P_ALT_LR_OST_NTC_F08_VF08_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_JASON_CS_S6A_L2P_ALT_LR_OST_NTC_F08_F08",
            provider="POCLOUD", 
            shortname="JASON_CS_S6A_L2P_ALT_LR_OST_NTC_F08",
            version="F08",
            description="Sentinel-6A MF Jason-CS L2P P4 Altimeter Low Resolution (LR) NTC Ocean Surface Topography F08 version: F08"
        )

    JASON_CS_S6A_L3_ALT_HR_OST_NTC_F08_VF08_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_JASON_CS_S6A_L3_ALT_HR_OST_NTC_F08_F08",
            provider="POCLOUD", 
            shortname="JASON_CS_S6A_L3_ALT_HR_OST_NTC_F08",
            version="F08",
            description="Sentinel-6A MF Jason-CS L3 P4 Altimeter High Resolution (HR) NTC Ocean Surface Topography (Unfiltered) Version F08 version: F08"
        )

    JASON_CS_S6A_L3_ALT_LR_OST_NTC_F08_VF08_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_JASON_CS_S6A_L3_ALT_LR_OST_NTC_F08_F08",
            provider="POCLOUD", 
            shortname="JASON_CS_S6A_L3_ALT_LR_OST_NTC_F08",
            version="F08",
            description="Sentinel-6A MF Jason-CS L3 P4 Altimeter High Resolution (LR) NTC Ocean Surface Topography (Unfiltered) Version F08 version: F08"
        )

    MITGCM_LLC4320_PRE_SWOT_JPL_L4_ACC_SMST_V10_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_MITgcm_LLC4320_Pre-SWOT_JPL_L4_ACC_SMST_v1.0_1.0",
            provider="POCLOUD", 
            shortname="MITgcm_LLC4320_Pre-SWOT_JPL_L4_ACC_SMST_v1.0",
            version="1.0",
            description="Southern Ocean Pre-SWOT Level-4 Hourly MITgcm LLC4320 Native Grid 2km Oceanographic Dataset Version 1.0 version: 1.0"
        )

    TELLUS_GIA_L3_05_DEG_V10_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_TELLUS_GIA_L3_0.5-DEG_V1.0_1.0",
            provider="POCLOUD", 
            shortname="TELLUS_GIA_L3_0.5-DEG_V1.0",
            version="1.0",
            description="TELLUS GRACE Level-3 0.5-degree Glacial Isostatic Adjustment v1.0 datasets produced by JPL version: 1.0"
        )

    TELLUS_GIA_L3_1_DEG_V10_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_TELLUS_GIA_L3_1-DEG_V1.0_1.0",
            provider="POCLOUD", 
            shortname="TELLUS_GIA_L3_1-DEG_V1.0",
            version="1.0",
            description="TELLUS GRACE Level-3 1.0-degree Glacial Isostatic Adjustment v1.0 datasets produced by JPL version: 1.0"
        )

    TEMPEST_STPH8_L1_TSDR_V100_V100_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_TEMPEST_STPH8_L1_TSDR_V10.0_10.0",
            provider="POCLOUD", 
            shortname="TEMPEST_STPH8_L1_TSDR_V10.0",
            version="10.0",
            description="TEMPEST STP-H8 Antenna and Microwave Brightness Temperatures Version 10.0 version: 10.0"
        )

    TOPEX_ALTSDR_VA_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_TOPEX_ALTSDR_A",
            provider="POCLOUD", 
            shortname="TOPEX_ALTSDR",
            version="A",
            description="TOPEX ALTIMETER SENSOR DATA RECORD version: A"
        )

    TOPEX_POSEIDON_GDR_F_VF_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_TOPEX_POSEIDON_GDR_F_F",
            provider="POCLOUD", 
            shortname="TOPEX_POSEIDON_GDR_F",
            version="F",
            description="TOPEX/POSEIDON Geophysical Data Record Version F version: F"
        )

    ANTARCTICA_MASS_TELLUS_MASCON_CRI_TIME_SERIES_RL063_V4_VRL063MV04_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_ANTARCTICA_MASS_TELLUS_MASCON_CRI_TIME_SERIES_RL06.3_V4_RL06.3Mv04",
            provider="POCLOUD", 
            shortname="ANTARCTICA_MASS_TELLUS_MASCON_CRI_TIME_SERIES_RL06.3_V4",
            version="RL06.3Mv04",
            description="Tellus Level-4 Antarctica Mass Anomaly Time Series from JPL GRACE/GRACE-FO Mascon CRI Filtered Release 06.3 version 04 version: RL06.3Mv04"
        )

    GREENLAND_MASS_TELLUS_MASCON_CRI_TIME_SERIES_RL063_V4_VRL063MV04_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_GREENLAND_MASS_TELLUS_MASCON_CRI_TIME_SERIES_RL06.3_V4_RL06.3Mv04",
            provider="POCLOUD", 
            shortname="GREENLAND_MASS_TELLUS_MASCON_CRI_TIME_SERIES_RL06.3_V4",
            version="RL06.3Mv04",
            description="Tellus Level-4 Greenland Mass Anomaly Time Series from JPL GRACE/GRACE-FO Mascon CRI Filtered Release 06.3 version 04 version: RL06.3Mv04"
        )

    OCEAN_MASS_TELLUS_MASCON_CRI_TIME_SERIES_RL063_V4_VRL063MV04_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_OCEAN_MASS_TELLUS_MASCON_CRI_TIME_SERIES_RL06.3_V4_RL06.3Mv04",
            provider="POCLOUD", 
            shortname="OCEAN_MASS_TELLUS_MASCON_CRI_TIME_SERIES_RL06.3_V4",
            version="RL06.3Mv04",
            description="Tellus Level-4 Ocean Mass Anomaly Time Series from JPL GRACE/GRACE-FO Mascon CRI Filtered Release 06.3 version 04 version: RL06.3Mv04"
        )

    SPURS1_TENUSEGLIDER_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SPURS1_TENUSEGLIDER_1.0",
            provider="POCLOUD", 
            shortname="SPURS1_TENUSEGLIDER",
            version="1.0",
            description="Tenuse Glider CTD data for the SPURS-1 N. Atlantic field campaign version: 1.0"
        )

    LOCSS_L1_V1_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_LOCSS_L1_V1_1.0",
            provider="POCLOUD", 
            shortname="LOCSS_L1_V1",
            version="1.0",
            description="The Lake Observations by Citizen Scientists & Satellites (LOCSS) Level 1 Version 1.0 version: 1.0"
        )

    CYGNSS_L3_UC_BERKELEY_WATERMASK_DAILY_V32_V32_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_CYGNSS_L3_UC_BERKELEY_WATERMASK_DAILY_V3.2_3.2",
            provider="POCLOUD", 
            shortname="CYGNSS_L3_UC_BERKELEY_WATERMASK_DAILY_V3.2",
            version="3.2",
            description="UC Berkeley CYGNSS Level 3 Daily RWAWC Watermask Version 3.2 version: 3.2"
        )

    CYGNSS_L3_UC_BERKELEY_WATERMASK_V31_V31_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_CYGNSS_L3_UC_BERKELEY_WATERMASK_V3.1_3.1",
            provider="POCLOUD", 
            shortname="CYGNSS_L3_UC_BERKELEY_WATERMASK_V3.1",
            version="3.1",
            description="UC Berkeley CYGNSS Level 3 Monthly RWAWC Watermask Version 3.1 version: 3.1"
        )

    CYGNSS_L3_SOIL_MOISTURE_V10_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_CYGNSS_L3_SOIL_MOISTURE_V1.0_1.0",
            provider="POCLOUD", 
            shortname="CYGNSS_L3_SOIL_MOISTURE_V1.0",
            version="1.0",
            description="UCAR-CU CYGNSS Level 3 Soil Moisture Version 1.0 version: 1.0"
        )

    SPURS1_MOORING_WHOI_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SPURS1_MOORING_WHOI_1.0",
            provider="POCLOUD", 
            shortname="SPURS1_MOORING_WHOI",
            version="1.0",
            description="WHOI mooring CTD, surface flux and meterorological data for the SPURS-1 N. Atlantic field campaign version: 1.0"
        )

    SPURS1_WAVEGLIDER_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_SPURS1_WAVEGLIDER_1.0",
            provider="POCLOUD", 
            shortname="SPURS1_WAVEGLIDER",
            version="1.0",
            description="Waveglider data for the SPURS-1 N. Atlantic field campaign version: 1.0"
        )

    MITGCM_LLC4320_PRE_SWOT_JPL_L4_WESTATLANTIC_V10_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_MITgcm_LLC4320_Pre-SWOT_JPL_L4_WestAtlantic_v1.0_1.0",
            provider="POCLOUD", 
            shortname="MITgcm_LLC4320_Pre-SWOT_JPL_L4_WestAtlantic_v1.0",
            version="1.0",
            description="West Atlantic Pre-SWOT Level-4 Hourly MITgcm LLC4320 Native Grid 2km Oceanographic Dataset Version 1.0 version: 1.0"
        )

    MITGCM_LLC4320_PRE_SWOT_JPL_L4_YONGALA_V10_V10_POCLOUD = DataCollectionDefinition(
            api_id="CMR",
            collections="POCLOUD_MITgcm_LLC4320_Pre-SWOT_JPL_L4_Yongala_v1.0_1.0",
            provider="POCLOUD", 
            shortname="MITgcm_LLC4320_Pre-SWOT_JPL_L4_Yongala_v1.0",
            version="1.0",
            description="Yongala Pre-SWOT Level-4 Hourly MITgcm LLC4320 Native Grid 2km Oceanographic Dataset Version 1.0 version: 1.0"
        )

