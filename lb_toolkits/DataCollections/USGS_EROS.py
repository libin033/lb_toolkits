# -*- coding:utf-8 -*-

from lb_toolkits.DataCollections.DataCollectionDefinition import DataCollectionDefinition 

class DataCollectionUSGS_EROS : 
    ISERV_V1_USGS_EROS = DataCollectionDefinition(
            api_id="CMR",
            collections="USGS_EROS_ISERV_1",
            provider="USGS_EROS", 
            shortname="ISERV",
            version="1",
            description="International Space Station SERVIR Environmental Research and Visualization System V1 version: 1"
        )

