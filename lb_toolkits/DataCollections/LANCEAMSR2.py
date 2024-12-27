# -*- coding:utf-8 -*-

from lb_toolkits.DataCollections.DataCollectionDefinition import DataCollectionDefinition 

class DataCollectionLANCEAMSR2 : 
    AU_RAIN_NRT_R02_V2_LANCEAMSR2 = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEAMSR2_AU_Rain_NRT_R02_2",
            provider="LANCEAMSR2", 
            shortname="AU_Rain_NRT_R02",
            version="2",
            description="NRT AMSR2 Unified Global Swath Surface Precipitation GSFC Profiling Algorithm V2 version: 2"
        )

    AU_OCEAN_NRT_R01_V1_LANCEAMSR2 = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEAMSR2_AU_Ocean_NRT_R01_1",
            provider="LANCEAMSR2", 
            shortname="AU_Ocean_NRT_R01",
            version="1",
            description="NRT AMSR2 Unified L2B Global Swath Ocean Products V1 version: 1"
        )

    AU_LAND_NRT_R02_V2_LANCEAMSR2 = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEAMSR2_AU_Land_NRT_R02_2",
            provider="LANCEAMSR2", 
            shortname="AU_Land_NRT_R02",
            version="2",
            description="NRT AMSR2 Unified L2B Half-Orbit 25 km EASE-Grid Surface Soil Moisture Beta V2 version: 2"
        )

    AU_SI12_NRT_R04_V4_LANCEAMSR2 = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEAMSR2_AU_SI12_NRT_R04_4",
            provider="LANCEAMSR2", 
            shortname="AU_SI12_NRT_R04",
            version="4",
            description="NRT AMSR2 Unified L3 Daily 12.5 km Brightness Temperature & Sea Ice Concentration V4 version: 4"
        )

    AU_SI25_NRT_R04_V4_LANCEAMSR2 = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEAMSR2_AU_SI25_NRT_R04_4",
            provider="LANCEAMSR2", 
            shortname="AU_SI25_NRT_R04",
            version="4",
            description="NRT AMSR2 Unified L3 Daily 25 km Brightness Temperature & Sea Ice Concentration Polar Grids V4 version: 4"
        )

    AU_SI6_NRT_R04_V4_LANCEAMSR2 = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEAMSR2_AU_SI6_NRT_R04_4",
            provider="LANCEAMSR2", 
            shortname="AU_SI6_NRT_R04",
            version="4",
            description="NRT AMSR2 Unified L3 Daily 6.25 km Polar Gridded 89 GHz Brightness Temperatures V4 version: 4"
        )

    AU_DYSNO_NRT_R02_V2_LANCEAMSR2 = DataCollectionDefinition(
            api_id="CMR",
            collections="LANCEAMSR2_AU_DySno_NRT_R02_2",
            provider="LANCEAMSR2", 
            shortname="AU_DySno_NRT_R02",
            version="2",
            description="NRT AMSR2 Unified L3 Global Daily 25 km EASE-Grid Snow Water Equivalent V2 version: 2"
        )

