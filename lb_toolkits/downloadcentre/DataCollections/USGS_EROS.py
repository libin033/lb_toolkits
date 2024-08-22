from lb_toolkits.downloadcentre.DataCollections.DataCollectionDefinition import DataCollectionDefinition 

class DataCollectionUSGS_EROS : 
    USGS_EROS_ISERV_V1 = DataCollectionDefinition(
            api_id="CMR",
            collections="USGS_EROS_ISERV_1",
            provider="USGS_EROS", 
            shortname="ISERV",
            version="1",
            description="International Space Station SERVIR Environmental Research and Visualization System V1 version: 1"
        )

