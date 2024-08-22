# -*- coding:utf-8 -*-
'''
@Project     : lb_toolkits  
----------------------------------------
@File        : USGS.py  
----------------------------------------
@Modify Time : 2024/8/22  
----------------------------------------
@Author      : Lee  
----------------------------------------
@Desciption
----------------------------------------
      
 
'''

from .DataCollectionDefinition import DataCollectionDefinition

class DataCollectionUSGS :

    USGS_LANDSAT_TM_C2_L1 = DataCollectionDefinition(
        api_id='M2M',
        collections="landsat_tm_c2_l1",
        bands=["B01","B02","B03","B04","B05","B06","B07"],
        dataset_id=["5e81f14f92acf9ef", "5e83d0a0f94d7d8d", "63231219fdd8c4e5"],
        has_cloud_coverage=True,
        description='Landsat 5 TM Collection 2 Level 1'
    )

    USGS_LANDSAT_TM_C2_L2 = DataCollectionDefinition(
        api_id='M2M',
        collections="landsat_tm_c2_l2",
        bands=["B01","B02","B03","B04","B05","B06","B07"],
        dataset_id=["5e83d11933473426", "5e83d11933473426", "632312ba6c0988ef"],
        has_cloud_coverage=True,
        description='Landsat 5 TM Collection 2 Level 2'
    )

    USGS_LANDSAT_ETM_C2_L1 = DataCollectionDefinition(
        api_id='M2M',
        collections="landsat_etm_c2_l1",
        bands=["B01","B02","B03","B04","B05","B06","B07"],
        dataset_id=[ "5e83d0d0d2aaa488", "5e83d0d08fec8a66"],
        has_cloud_coverage=True,
        description='Landsat 7 ETM+ Collection 2 Level 1'
    )

    USGS_LANDSAT_ETM_C2_L2 = DataCollectionDefinition(
        api_id='M2M',
        collections="landsat_etm_c2_l2",
        bands=["B01","B02","B03","B04","B05","B06","B07"],
        dataset_id=["5e83d12aada2e3c5", "5e83d12aed0efa58", "632311068b0935a8"],
        has_cloud_coverage=True,
        description='Landsat 7 ETM+ Collection 2 Level 2'
    )

    USGS_LANDSAT_OT_C2_L1 = DataCollectionDefinition(
        api_id='M2M',
        collections="landsat_ot_c2_l1",
        bands=["B01","B02","B03","B04","B05","B06","B07"],
        dataset_id=["5e81f14ff4f9941c", "5e81f14f92acf9ef"],
        has_cloud_coverage=True,
        description='Landsat 8/9 Collection 2 Level 1'
    )

    USGS_LANDSAT_OT_C2_L2 = DataCollectionDefinition(
        api_id='M2M',
        collections="landsat_ot_c2_l2",
        bands=["B01","B02","B03","B04","B05","B06","B07"],
        dataset_id=["5e83d14f30ea90a9", "5e83d14fec7cae84", "632210d4770592cf"],
        has_cloud_coverage=True,
        description='Landsat 8/9 Collection 2 Level 2'
    )
