# -*- coding:utf-8 -*-
'''
@Project     : lb_toolkits  
----------------------------------------
@File        : data_collections.py  
----------------------------------------
@Modify Time : 2024/8/21  
----------------------------------------
@Author      : Lee  
----------------------------------------
@Desciption
----------------------------------------
      
 
'''
import numpy as np

from lb_toolkits.downloadcentre.DataCollections import *


class DataCollection(
    DataCollectionASF,
    DataCollectionCDDIS,
    DataCollectionGES_DISC,
    DataCollectionGHRC_DAAC,
    DataCollectionLAADS,
    DataCollectionLANCEAMSR2,
    DataCollectionLANCEMODIS,
    DataCollectionLARC,
    DataCollectionLARC_ASDC,
    DataCollectionLARC_CLOUD,
    DataCollectionLM_FIRMS,
    DataCollectionLPCLOUD,
    DataCollectionLPDAAC_ECS,
    DataCollectionNSIDCV0,
    DataCollectionNSIDC_CPRD,
    DataCollectionNSIDC_ECS,
    DataCollectionOB_DAAC,
    DataCollectionOMINRT,
    DataCollectionORNL_CLOUD,
    DataCollectionPOCLOUD,
    DataCollectionSEDAC,
    DataCollectionUSGS_EROS,
    DataCollectionUSGS_LTA,
    DataCollectionESA,
    DataCollectionUSGS
) :

    def __init__(self):
        pass






def spidertable(url, **kwargs):
    import pandas as pd

    try:
        df1 = pd.read_html(url, **kwargs)
        df = df1[0]

        data = df.to_dict(orient='list')

        return data
    except BaseException as e :
        print(e)
        return None

if __name__ == '__main__':

    count = 1
    for item in dir(DataCollection) :
        print(count, item)
        count += 1
    exit(0)

    Dict_Match_Info = {}

    # 第一次查询：从静态JSON文件中
    Dict_Site_Info = spidertable(url = r'https://cmr.earthdata.nasa.gov/search/site/collections/directory/eosdis')

    CMR_Provider = Dict_Site_Info['Provider Name']
    # print('在JSON文件中未匹配到相应的产品信息，进行在线搜索方式查询')
    count = 1

    for prodid in CMR_Provider :
        dict_data = spidertable(r'https://cmr.earthdata.nasa.gov/search/site/'
                                'collections/directory/{url}/gov.nasa.eosdis'.format(url=prodid))
        if dict_data is None :
            continue
        # fp = open('./DataCollections/%s.py' %(prodid), 'w', encoding='utf-8')
        # fp.write('from lb_toolkits.downloadcentre.DataCollections.DataCollectionDefinition import DataCollectionDefinition \n\n')
        # fp.write('class DataCollection%s : \n' %(prodid))

        # print('from .%s import DataCollection%s' %(prodid, prodid))
        for collection, shortname, version in zip(dict_data['Collection'],
                                                  dict_data['Short Name'],
                                                  np.array(dict_data['Version'], dtype=np.str_)) :
            # print(count, shortname, version, collection)
            count += 1
            if version in ['Not provided'] :
                varl = f'{prodid}_{shortname}'
            else:
                varl = f'{prodid}_{shortname}_V{version.replace(".", "")}'
            if ' ' in shortname :
                print(prodid, shortname)

            varl = varl.replace('+', '_')
            varl = varl.replace('-', '_')
            varl = varl.replace('.', '')
            varl = varl.replace('/', '_')
            varl = varl.replace(' ', '_')

            info = f'    {varl} = DataCollectionDefinition(\n\
            api_id="CMR",\n\
            collections="{prodid}_{shortname}_{version}",\n\
            provider="{prodid}", \n\
            shortname="{shortname}",\n\
            version="{version}",\n\
            description="{collection} version: {version}"\n\
        )\n\n'
            # print(info)
            # fp.write(info)
            if varl not in Dict_Match_Info :
                Dict_Match_Info[varl] = info
            else :
                print('='*100)
                print(info)
                print(Dict_Match_Info[varl])
        # fp.close()
    print(', '.join(CMR_Provider))
