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
 "version": "2.1.2"
}
'''  # END VERSION_JSON


def get_versions():
    return json.loads(version_json)

# file generated by setuptools_scm
# don't change, don't track in version control
# version = '1.1.13'
# version_tuple = (1, 1, 13)