# -*- coding:utf-8 -*-
'''
@Project     : lb_toolkits  
----------------------------------------
@File        : downloadGK2.py  
----------------------------------------
@Modify Time : 2024/8/22  
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
import urllib.request as rq
import os

DataLevelInfo = {
    'LE1B': 'AMI / Level 1B',
    'LE2': 'AMI / Level 2',
    'LV1': 'KSEM / Level 1',
}
DataAreaInfo = {
    'EA': 'East Asia',
    'ELA' : 'Extended Local Area',
    'ENH' : 'Extended Northern Hemisphere',
    'FD' : 'Full Disk',
    'KO' : 'Korea',
    'LA' : 'Local Area',
    'NA' : 'Not applicable',
    'NK' : 'North Korea',
    'SK' : 'South Korea',
    'TP' : 'Typhoon Area',
}

DataProdTypeInfo = {
    'VI004' : 'Visible(0.47㎛)',
    'VI005' : 'Visible(0.51㎛)',
    'VI006' : 'Visible(0.64㎛)',
    'VI008' : 'Visible(0.86㎛)',
    'NR013' : 'Near infrared(1.38㎛)',
    'NR016' : 'Near infrared(1.6㎛)',
    'SW038' : 'Shortwave infrared(3.8㎛)',
    'WV063' : 'Vapor(6.3㎛)',
    'WV069' : 'Vapor(6.9㎛)',
    'WV073' : 'Vapor(7.3㎛)',
    'IR087' : 'Infrared(8.7㎛)',
    'IR096' : 'Infrared(9.6㎛)',
    'IR105' : 'Infrared(10.5㎛)',
    'IR112' : 'Infrared(11.2㎛)',
    'IR123' : 'Infrared(12.3㎛)',
    'IR133' : 'Infrared(13.3㎛)',
    'AMV-VI006-CD' : 'Atmospheric Motion Vector-Visible(0.6㎛)-Cloud target',
    'AMV-SW038-CD' : 'Atmospheric Motion Vector- Shortwave infrared(3.8㎛)-Cloud target',
    'AMV-WV063-CS' : 'Atmospheric Motion Vector-Vapor(6.3㎛)-Clear Sky target',
    'AMV-WV063-CD' : 'Atmospheric Motion Vector-Vapor(6.3㎛)-Cloud target',
    'AMV-WV069-CS' : 'Atmospheric Motion Vector-Vapor(6.9㎛)-Clear Sky target',
    'AMV-WV069-CD' : 'Atmospheric Motion Vector-Vapor(6.9㎛)-Cloud target',
    'AMV-WV073-CS' : 'Atmospheric Motion Vector-Vapor(7.3㎛)-Clear Sky target',
    'AMV-WV073-CD' : 'Atmospheric Motion Vector-Vapor(7.3㎛)-Cloud target',
    'AMV-IR105-CD' : 'Atmospheric Motion Vector- Infrared(10.5㎛) –Cloud target',
    'AMV-IR112-CD' : 'Atmospheric Motion Vector- Infrared(11.2㎛) –Cloud target',
    'CLD' : 'Cloud Detection (Cloud Mask)',
    'CTPS' : 'Cloud top properties (phase, temperature, height, pressure)',
    'CLA' : 'Cloud analysis (type, cloud fraction, amount at ground view, layer)',
    'CTCLUST' : 'Cloud Type-Clustering Method',
    'DCOEW' : 'Daytime Cloud microphysics (optical thickness, effective radius, liquid water path, ice water path)',
    'NCOT' : 'Nighttime Cloud Optical Thickness (IR channel based)',
    'CI' : 'Convective Initiation',
    'OT' : 'Overshooting-top cloud',
    'FOG' : 'Fog',
    'ICING' : 'Aircraft icing',
    'TFTD' : 'Tropopause folding turbulence',
    'RR' : 'Rainfall Rate',
    'QPN' : 'Quantitative precipitation nowcasting (potential rainfall rate, probability of rainfall))',
    'TQPROF' : 'Vertical temperature and humidity profiles (T, q, RH)',
    'TPW' : 'Total precipitable water (tpw, lpw1(low), lpw2(mid), lpw3(high))',
    'AII' : 'Atmospheric instability indices (CAPE, KI, LI, SSI, TTI)',
    'ANN' : 'ANN CAPE and TPW (based on artificial neural network method)',
    'ADPS' : 'Aerosol Detection Products',
    'APPS' : 'Aerosol properties (aerosol optical depth @ 0.55 μm, dust optical depth @ 11 μm & @ 0.55 μm, Angstrom component)',
    'AVIS' : 'Aerosol visibility',
    'VAP' : 'Volcanic ash height and mass',
    'TOZ' : 'Total ozone',
    'SO2D' : 'Sulfur dioxide detection',
    'FF' : 'Forest fire',
    'LST' : 'Land surface temperature',
    'SAL' : 'Surface albedo',
    'LSE' : 'Surface emissivity',
    'VGT' : 'Vegetation index (NDVI, vegetation green fraction)',
    'SCSI' : 'Snow and Sea Ice cover (10 minutes) ?',
    'SD' : 'Snow depth',
    'SSC' : 'Sea surface current',
    'SST' : 'Sea surface temperature',
    'RAD' : 'radiance',
    'CSR' : 'Clear Sky Radiance',
    'SWRAD' : 'Shortwave radiation (surface absorbed, surface downward, TOA reflected)',
    'LWRAD' : 'Longwave radiation (surface downward, surface upward, TOA upward)',
}

class downloadGK2():
    def __init__(self, API_Key, ):

        self.API_Key = API_Key

    def searchfile(self,
                   productType,
                   startDate,
                   endDate=None,
                   area='FD',
                   form='dataList',
                   satellite='GK2A',
                   fomat='json'
                   ):

        if endDate is None :
            endDate = startDate

        dataLevel = self.getDataLevel(productType)

        searchUrl = (f'http://api.nmsc.kma.go.kr:9080/api/'
                     f'{satellite}/{dataLevel}/{productType}/{area}/{form}?'
                     f'sDate={startDate.strftime("%Y%m%d%H%M")}&eDate={endDate.strftime("%Y%m%d%H%M")}&'
                     f'format={fomat}&key={self.API_Key}')

        print(searchUrl)

        return searchUrl


    def download(self,
                 dstdir,
                  productType,
                  startDate,
                  endDate=None,
                  area='FD',
                  form='data',
                  satellite='GK2A',
                  fomat='json'):

        if endDate is None :
            endDate = startDate

        dataLevel = self.getDataLevel(productType)

        downUrl = (f'http://api.nmsc.kma.go.kr:9080/api/'
                     f'{satellite}/{dataLevel}/{productType}/{area}/{form}?'
                     f'sDate={startDate.strftime("%Y%m%d%H%M")}&'
                     f'format={fomat}&key={self.API_Key}')

        request = rq.Request(downUrl)
        response = rq.urlopen(request)
        rescode = response.getcode()

        if not os.path.isdir(dstdir) and len(dstdir) > 5:
            os.makedirs(dstdir)

        if rescode == 200:
            fn = response.headers.get_filename()
            rq.urlretrieve(downUrl, os.path.join(dstdir, fn))
            print('Complete to download: ' + fn)
        else:                                                                                                                               #에러 출력 / print error
            print('Error code: ' + str(rescode))

    def getDataLevel(self, productType):

        if productType in ['VI004', 'VI005', 'VI006', 'VI008',
                           'NR013', 'NR016', 'SW038', 'WV063',
                           'WV069', 'WV073', 'IR087', 'IR096',
                           'IR105', 'IR112', 'IR123', 'IR133',] :
            return 'LE1B'
        else:
            return 'LE2'