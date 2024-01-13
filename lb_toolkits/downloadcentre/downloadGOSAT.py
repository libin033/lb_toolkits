# -*- coding:utf-8 -*-
'''
@Project     : lb_toolkits

@File        : downloadGOSAT.py

@Modify Time :  2022/11/16 16:02   

@Author      : Lee    

@Version     : 1.0   

@Description :

'''
import os
import sys
import numpy as np
import datetime
import shutil
import platform
from lb_toolkits.tools import wget

CH4_L2_Info = {
    'V03.05' : [datetime.datetime.strptime('20090401', '%Y%m%d'), datetime.datetime.utcnow()],
    'V02.96' : [datetime.datetime.strptime('20200601', '%Y%m%d'), datetime.datetime.strptime('20221231', '%Y%m%d')],
    'V02.95' : [datetime.datetime.strptime('20090401', '%Y%m%d'), datetime.datetime.strptime('20200531', '%Y%m%d')]
}

CO2_L2_Info = {
    'V03.05' : [datetime.datetime.strptime('20090401', '%Y%m%d'), datetime.datetime.utcnow()],
    'V02.98' : [datetime.datetime.strptime('20200601', '%Y%m%d'), datetime.datetime.strptime('20221231', '%Y%m%d')],
    'V02.97' : [datetime.datetime.strptime('20090401', '%Y%m%d'), datetime.datetime.strptime('20200531', '%Y%m%d')]
}

CH4_L3_Info = {
    'V03.05' : [datetime.datetime.strptime('20090601', '%Y%m%d'), datetime.datetime.utcnow()],
    # 'V03.00' : [datetime.datetime.strptime('20230601', '%Y%m%d'), datetime.datetime.utcnow()],
    'V02.91' : [datetime.datetime.strptime('20200601', '%Y%m%d'), datetime.datetime.strptime('20230331', '%Y%m%d')],
    'V02.90' : [datetime.datetime.strptime('20090601', '%Y%m%d'), datetime.datetime.strptime('20200531', '%Y%m%d')],

}

CO2_L3_Info = {
    'V03.05' : [datetime.datetime.strptime('20090601', '%Y%m%d'), datetime.datetime.utcnow()],
    # 'V03.00' : [datetime.datetime.strptime('20230601', '%Y%m%d'), datetime.datetime.strptime('20230331', '%Y%m%d')],
    'V02.91' : [datetime.datetime.strptime('20200601', '%Y%m%d'), datetime.datetime.strptime('20230331', '%Y%m%d')],
    'V02.90' : [datetime.datetime.strptime('20090601', '%Y%m%d'), datetime.datetime.strptime('20200531', '%Y%m%d')],

}


# H2O_Info = {
#     'V02.98' : [datetime.datetime.strptime('20200601', '%Y%m%d'), datetime.datetime.strptime('20221231', '%Y%m%d')]
#     'V02.97' : [datetime.datetime.strptime('20090401', '%Y%m%d'), datetime.datetime.strptime('20200531', '%Y%m%d')]
# }

def downloadGOSAT(outdir, nowdate, username, password, prod='CO2', level='L2'):
    '''
    https://data2.gosat.nies.go.jp/GosatDataArchiveService/usr/download/ProductPage/view

    ------------------------------------------------------------------------------------
    Observation period	            Input FTS L1B	Bias uncorrected    Bias corrected
                                                    FTS SWIR L2 CO2	    FTS SWIR L2 CO2
    Jun. 01, 2020 - Sep. 30, 2022	V220.221	       V02.91	          V02.98
    Apr. 23, 2009 - May 31, 2020	V220.220	       V02.90	          V02.97
    Jun. 01, 2020 - Jul. 31, 2021	V220.221	       V02.91	          V02.96
    Apr. 23, 2009 - May 31, 2020	V220.220	       V02.90	          V02.95
    Apr. 23, 2009 - Jun. 30, 2020	V210.210	       V02.81	          -
    ====================================================================================
    Observation period	           Input FTS L1B	Bias uncorrected     Bias corrected
                                                     FTS SWIR L2 CH4	 FTS SWIR L2 CH4
    Jun. 01, 2020 - Sep. 30, 2022	V220.221	     V02.91	                V02.96
    Apr. 23, 2009 - May 31, 2020	V220.220	     V02.90	                V02.95
    Apr. 23, 2009 - Jun. 30, 2020	V210.210	     V02.81	                -


    Parameters
    ----------
    outdir
    nowdate
    username
    password
    prod

    Returns
    -------

    '''

    if prod in ['CO2', 'co2'] :
        if level in ['L2', 'l2', 'level2', 'Level2'] :
            for version in CO2_L2_Info :
                if nowdate >= CO2_L2_Info[version][0] and nowdate <= CO2_L2_Info[version][1] :
                    break
        elif level in ['L3', 'l3', 'level3', 'Level3'] :
            for version in CO2_L3_Info :
                if nowdate >= CO2_L3_Info[version][0] and nowdate <= CO2_L3_Info[version][1] :
                    break

    if prod in ['CH4', 'ch4'] :
        if level in ['L2', 'l2', 'level2', 'Level2'] :
            for version in CH4_L2_Info :
                if nowdate >= CH4_L2_Info[version][0] and nowdate <= CH4_L2_Info[version][1] :
                    break
        elif level in ['L3', 'l3', 'level3', 'Level3'] :
            for version in CH4_L3_Info :
                if nowdate >= CH4_L3_Info[version][0] and nowdate <= CH4_L3_Info[version][1] :
                    break

    url = r'https://data2.gosat.nies.go.jp/wgetdata/GU/SWIR{level}{prod}/{YYYY}/SWIR{level}{prod}_{YYYY}{MM}_{version}.tar'.format(
        prod=prod,
        version=version,
        level=level,
        YYYY=nowdate.strftime('%Y'),
        MM=nowdate.strftime('%m'),
    )
    print('文件下载地址【%s】' %(url))

    if not os.path.isdir(outdir) :
        os.makedirs(outdir)

    filename = wget(outdir, url, username, password)

    return filename

# def wget(outdir, url, username, password, tries=3, skip=False, cover=False):
#     '''通过wget方式进行数据下载'''
#     local_filename = os.path.basename(url)
#     local_filename = os.path.join(outdir, local_filename)
#     if skip :
#         return local_filename
#
#     if os.path.isfile(local_filename) :
#         if cover :
#             print('文件已存在，将删除后下载【%s】' %(local_filename))
#             os.remove(local_filename)
#         else:
#             print('文件已存在，将跳过下载【%s】' %(local_filename))
#             return local_filename
#
#     tempfile = local_filename + '.download'
#
#     if platform.system().lower() == 'windows' :
#         cmd = f'{WGET} --tries={tries} -c -np {url} ' \
#               f'--http-user={username} --http-passwd={password} -O {tempfile}'
#     else:
#         cmd = f'{WGET} --tries={tries} -c -np {url} ' \
#               f'--http-user={username} --http-passwd={password} -O {tempfile}'
#
#     print('执行下载命令: 【%s】' %(cmd))
#     os.system(cmd)
#
#     if os.path.isfile(local_filename) :
#         os.remove(local_filename)
#
#     if os.path.isfile(tempfile) :
#         shutil.move(tempfile, local_filename)
#
#     if os.path.isfile(local_filename) and os.stat(local_filename).st_size == 0 :
#         os.remove(local_filename)
#
#     return local_filename
#
