from lb_toolkits.DataCollections.DataCollectionDefinition import DataCollectionDefinition

class DataCollectionLM_FIRMS : 
    LM_FIRMS_MCD14DL_C5_NRT_V5 = DataCollectionDefinition(
            api_id="CMR",
            collections="LM_FIRMS_MCD14DL_C5_NRT_5",
            provider="LM_FIRMS", 
            shortname="MCD14DL_C5_NRT",
            version="5",
            description="MODIS/Aqua+Terra Thermal Anomalies/Fire locations 1km FIRMS V005 NRT version: 5"
        )

