# -*- coding:utf-8 -*-
'''
@Project  : lb_toolkits
@File     : __init__.py
@Modify Time      @Author    @Version    
--------------    -------    --------    
2022/7/20 11:29      Lee       1.0         
@Description
------------------------------------
 
'''

from . import downloadcentre

from .version import get_versions
__version__ = get_versions()['version']
del get_versions