# -*- coding:utf-8 -*-
'''
@Project     : lb_toolkits

@File        : version.py

@Modify Time :  2022/11/11 14:09   

@Author      : Lee    

@Version     : 1.0   

@Description :

'''

import json

version_json = '''
{
 "version": "25.10.11"
}
'''  # END VERSION_JSON


def get_versions():
    return json.loads(version_json)
