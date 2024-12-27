# -*- coding:utf-8 -*-
'''
@Project     : lb_toolkits  
----------------------------------------
@File        : DataCollectionDefinition.py  
----------------------------------------
@Modify Time : 2024/8/21  
----------------------------------------
@Author      : Lee  
----------------------------------------
@Desciption
----------------------------------------
      
 
'''
import os
import sys
import numpy as np
import datetime

class DataCollectionDefinition:
    """An immutable definition of a data collection

    Check `DataCollection.define` for more info about attributes of this class
    """

    # pylint: disable=too-many-instance-attributes
    api_id: str | None = None
    collections: str | None = None
    provider: str | None = None
    shortname: str | None = None
    productType: str | None = None
    version: str | None = None
    bands: list[...] | None = None
    dataset_id: list[...] | None = None
    description: str | None = None
    sensor_type: str | None = None
    processing_level: str | None = None
    polarization: str | None = None
    resolution: str | None = None
    orbit_direction: str | None = None
    has_cloud_coverage: bool = False


    def __init__(self, **kwargs) :

        for k, v in kwargs.items():
            setattr(self, k, v)
