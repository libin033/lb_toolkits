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
import datetime
from dateutil.relativedelta import relativedelta
from lb_toolkits.utils import wget

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

class downloadGOSAT :

    def __init__(self, username, password):

        self.username = username
        self.password = password

    def searchfile(self, startDate, endDate=None, prod='CO2', level='L2', version=None):
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

        urls = []

        if endDate is None:
            endDate = startDate

        nowdate = startDate
        while nowdate <= endDate:
            # if prod in ['CO2', 'co2'] :
            #     if level in ['L2', 'l2', 'level2', 'Level2'] :
            #         for version in CO2_L2_Info :
            #             if nowdate >= CO2_L2_Info[version][0] and nowdate <= CO2_L2_Info[version][1] :
            #                 break
            #     elif level in ['L3', 'l3', 'level3', 'Level3'] :
            #         for version in CO2_L3_Info :
            #             if nowdate >= CO2_L3_Info[version][0] and nowdate <= CO2_L3_Info[version][1] :
            #                 break
            #
            # if prod in ['CH4', 'ch4'] :
            #     if level in ['L2', 'l2', 'level2', 'Level2'] :
            #         for version in CH4_L2_Info :
            #             if nowdate >= CH4_L2_Info[version][0] and nowdate <= CH4_L2_Info[version][1] :
            #                 break
            #     elif level in ['L3', 'l3', 'level3', 'Level3'] :
            #         for version in CH4_L3_Info :
            #             if nowdate >= CH4_L3_Info[version][0] and nowdate <= CH4_L3_Info[version][1] :
            #                 break

            url = r'https://data2.gosat.nies.go.jp/wgetdata/GU/SWIR{level}{prod}/{YYYY}/SWIR{level}{prod}_{YYYY}{MM}_{version}.tar'.format(
                prod=prod,
                version=version,
                level=level,
                YYYY=nowdate.strftime('%Y'),
                MM=nowdate.strftime('%m'),
            )
            urls.append(url)
            nowdate += relativedelta(months=1)
        # print('文件下载地址【%s】' %(url))

        return urls

    def download(self, outdir, url, tries=3, timeout=5*60, skip_download=False,
                 cover=False, continuing=True, wgetpath=None, **kwargs):
        if not os.path.isdir(outdir) :
            os.makedirs(outdir)

        if isinstance(url, list):
            files = []
            for url1 in url:
                filename = wget(outdir,
                                url1,
                                username=self.username,
                                password=self.password,
                                timeout=timeout,
                                tries=tries,
                                skip_download=skip_download,
                                cover=cover,
                                continuing=continuing,
                                wgetpath=wgetpath)
                files.append(filename)
            return files
        elif isinstance(url, str):
            filename = wget(outdir,
                            url,
                            username=self.username,
                            password=self.password,
                            timeout=timeout,
                            tries=tries,
                            skip_download=skip_download,
                            cover=cover,
                            continuing=continuing,
                            wgetpath=wgetpath)

            return filename

