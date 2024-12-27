# -*- coding:utf-8 -*-
'''
@Project     : lb_toolkits

@File        : cmr.py

@Modify Time :  2022/10/19 16:38   

@Author      : Lee    

@Version     : 1.0   

@Description :

'''
import os
import base64
import itertools
import json
import ssl
import sys
import time
import numpy as np
import requests
import datetime

from lb_toolkits import docs
from lb_toolkits.utils.jsonpro import readjson, writejson
from lb_toolkits.utils import wget
from urllib.request import urlopen, Request


CMR_URL = 'https://cmr.earthdata.nasa.gov'
URS_URL = 'https://urs.earthdata.nasa.gov'

class cmr() :

    def __init__(self):
        pass

    def Options(self, sort_key='start_date',
                polygon=None, point=None, line=None, circle=None,
                bounding_box=None, bbox=None, data_center=None, provider=None,
                project=None, processing_level_id=None,
                spatial_keyword=None, collection_data_type=None,
                granule_data_format=None, downloadable=False,
                cloud_cover=None, version=None, pattern=None, **kwargs):

        new_options =''
        if sort_key is not None:
            new_options += '&sort_key[]=' + sort_key

        # if page_size is not None and isinstance(page_size, int):
        #     new_options += '&page_size=%d' %(page_size)

        if data_center is not None :
            new_options += '&data_center[]=' + data_center

        if provider is not None :
            new_options += '&provider=' + provider

        if project is not None :
            new_options += '&project[]=' + project

        if processing_level_id is not None :
            new_options += '&processing_level_id[]=' + processing_level_id

        if spatial_keyword is not None :
            new_options += '&spatial_keyword[]=' + spatial_keyword

        if collection_data_type is not None :
            # "NEAR_REAL_TIME": "near_real_time", "nrt", "NRT",
            # "near real time", "near-real time", "near-real-time", "near real-time". OTHER.
            new_options += '&collection_data_type[]=' + collection_data_type

        if granule_data_format is not None : # granule_data_format=NetCDF"
            new_options += '&granule_data_format=' + granule_data_format

        if downloadable  :
            new_options += '&downloadable=true'

        if polygon is not None :
            # Polygon points are provided in counter-clockwise order.
            # The last point should match the first point to close the polygon.
            # The values are listed comma separated in longitude latitude order,
            # i.e. lon1, lat1, lon2, lat2, lon3, lat3, and so on.
            new_options += '&polygon={polygon}'.format(polygon=polygon)

        if point is not None :
            new_options += '&point=%s,%s' %(str(point[0]), str(point[1]))

        if line is not None :
            new_options += '&line=' + line

        if circle is not None :
            new_options += '&circle=' + circle

        if bounding_box is not None :
            # Bounding boxes define an area on the earth aligned with longitude and latitude.
            # The Bounding box parameters must be 4 comma-separated numbers:
            #   lower left longitude, lower left latitude,
            #   upper right longitude, upper right latitude.
            new_options += '&bounding_box[]=%f,%f,%f,%f' %(bounding_box[0], bounding_box[1],
                                                           bounding_box[2], bounding_box[3])

        if bbox is not None :
            # Bounding boxes define an area on the earth aligned with longitude and latitude.
            # The Bounding box parameters must be 4 comma-separated numbers:
            #   lower left longitude, lower left latitude,
            #   upper right longitude, upper right latitude.
            new_options += '&bounding_box[]=%f,%f,%f,%f' %(bbox[0], bbox[1],
                                                           bbox[2], bbox[3])

        if 'bbox' in kwargs :
            new_options += '&bounding_box[]=%f,%f,%f,%f' %(kwargs['bbox'][0], kwargs['bbox'][1],
                                                           kwargs['bbox'][2], kwargs['bbox'][3])

        if cloud_cover is not None :
            new_options += '&cloud_cover=,' + str(cloud_cover)

        if version is not None :
            new_options += '&version=' + version

        if pattern is not None :
            new_options += '&producer_granule_id[]={0}&options[producer_granule_id][pattern]=true'.format(pattern)

        return new_options

    def cmr_search(self, starttime=None, endtime=None,
                   platform=None, instrument=None,
                   sensor=None, short_name=None,
                   page_size=1000, **kwargs):

        if 'options' not in kwargs or isinstance(kwargs['options'], (list, str)):
            opts = self.Options(**kwargs)
        else:
            opts = kwargs['options']

        parms = '{ROOT_URL}/search/granules.json?'.format(ROOT_URL=CMR_URL)

        if starttime is not None and endtime is not None :
            parms += 'temporal[]={starttime},{endtime}'.format(starttime=starttime.strftime('%Y-%m-%dT%H:%M:%SZ'),
                                                            endtime=endtime.strftime('%Y-%m-%dT%H:%M:%SZ'))
            parms += '&page_size=%d' %(page_size)
        else:
            parms += 'page_size=%d' %(page_size)

        if short_name is not None :
            parms += '&short_name={short_name}'.format(short_name=short_name)

        if platform is not None :
            parms += '&platform[]=' + platform

        if instrument is not None :
            parms += '&instrument[]=' + instrument

        if sensor is not None :
            parms += '&sensor[]=' + sensor

        parms += opts
        # parms += '&producer_granule_id[]={0}&options[producer_granule_id][pattern]=true'.format('*hdf')
        print('查询链接:\n【{0}】\n'.format(parms))

        return self.cmr_get_urls(parms)

    def cmr_get_urls(self, cmr_query_url):
        # cmr_scroll_id = None

        cmr_search_after = None
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        urls = []

        try:
            cnt = 1
            while True:
                req = Request(cmr_query_url)

                # 通过after来获取下一页检索结果
                if cmr_search_after :
                    req.add_header('cmr-search-after', cmr_search_after)
                response = urlopen(req, context=ctx)
                # if not cmr_search_after:
                headers = {k.lower(): v for k, v in dict(response.info()).items()}
                if not cmr_search_after :
                    hits = int(headers['cmr-hits'])
                    if hits > 0:
                        print('共匹配【{count}】个文件'.format(count=hits))
                    else:
                        print('未查询到满足相应条件的文件')
                        break

                cmr_search_after = headers['cmr-search-after']
                search_page = response.read()
                search_page = json.loads(search_page.decode('utf-8'))
                url_scroll_results = self.cmr_filter_urls(search_page)
                # print(len(url_scroll_results), cmr_search_after)

                # 当url_scroll_results为空的时候，结束请求
                if not url_scroll_results:
                    break
                urls += url_scroll_results

                if len(urls) < hits :
                    print('%d,' %(cnt), end='')
                    sys.stdout.flush()
                cnt += 1

            return urls
        except BaseException :
            return urls

    def get_credentials(self, username, password):
        """Get user credentials from .netrc or prompt for input."""
        credentials = None
        credentials = '{username}:{password}'.format(username=username,
                                                     password=password)
        credentials = base64.b64encode(credentials.encode('ascii')).decode('ascii')
        print('credentials:', credentials)

        return credentials

    def get_tokens(self, username, password):
        ''' 通过cmr包进行token获取'''

        token = self.searchtoken(username=username, password=password)
        if token is None :
            token = self.createtoken(username=username, password=password)

        return token

    def searchtoken(self, username, password):
        '''查询token'''
        credentials = '{username}:{password}'.format(username=username,
                                                     password=password)
        credentials = base64.b64encode(credentials.encode('ascii')).decode('ascii')

        headers = {'Authorization': 'Basic {credentials}'.format(credentials=credentials) }
        resp = requests.get('https://urs.earthdata.nasa.gov/api/users/tokens', headers=headers)
        res = json.loads(resp.text)

        token = None
        validdate = None
        for item in res :
            token = item["access_token"]
            validdate = datetime.datetime.strptime(item['expiration_date'],'%m/%d/%Y')
            if validdate > datetime.datetime.utcnow() :
                print('【%s】' %(token))
                print('该token有效时间至%s' %(validdate.strftime('%Y-%m-%d')))
                return token

            if validdate <= datetime.datetime.utcnow() :
                print('该token有效时间至%s，当前已失效，将其删除后重新创建新的token' %(validdate.strftime('%Y-%m-%d')))
                self.deletetoken(username, password, token)
                token = self.createtoken(username, password)

        if token is None :
            print('账号【%s】未存在token,请使用createtoken接口进行token创建' %(username))

        return token

    def createtoken(self, username, password):
        '''创建token'''
        credentials = '{username}:{password}'.format(username=username,
                                                     password=password)
        credentials = base64.b64encode(credentials.encode('ascii')).decode('ascii')

        headers = {'Authorization': 'Basic {credentials}'.format(credentials=credentials) }
        resp = requests.post('https://urs.earthdata.nasa.gov/api/users/token', headers=headers)
        if resp.status_code == 200 :
            res = json.loads(resp.text)
            token = res["access_token"]
            print('成功创建token【%s】' %(token))

            return token
        else:
            print('创建token失败')
            return None

    def deletetoken(self, username, password, token):
        '''删除token'''
        credentials = '{username}:{password}'.format(username=username,
                                                     password=password)
        credentials = base64.b64encode(credentials.encode('ascii')).decode('ascii')

        headers = {'Authorization': 'Basic {credentials}'.format(credentials=credentials) }
        data = {'token': token}

        resp = requests.post('https://urs.earthdata.nasa.gov/api/users/revoke_token',
                             data=data, headers=headers)
        if resp.status_code == 200 :
            print('成功删除token【%s】' %(token))
            return True
        else:
            print('删除token失败【%s】' %(token))
            return False

    def cmr_filter_urls(self, search_results):
        """Select only the desired data files from CMR response."""
        if 'feed' not in search_results or 'entry' not in search_results['feed']:
            return []

        entries = [e['links']
                   for e in search_results['feed']['entry']
                   if 'links' in e]
        # Flatten "entries" to a simple list of links
        links = list(itertools.chain(*entries))

        urls = []
        unique_filenames = set()
        for link in links :
            # for entry in search_results['feed']['entry'] :
            #     if 'links' not in entry :
            #         continue
            #
            #     for link in entry['links'] :
            if 'rel' in link and '/data#' not in link['rel']:
                # Exclude links which are not classified by CMR as "data" or "metadata"
                continue

            if 'href' not in link:
                # Exclude links with nothing to download
                continue

            if 'inherited' in link and link['inherited'] is True:
                # Why are we excluding these links?
                continue

            if 'title' in link and 'opendap' in link['title'].lower():
                # Exclude OPeNDAP links--they are responsible for many duplicates
                # This is a hack; when the metadata is updated to properly identify
                # non-datapool links, we should be able to do this in a non-hack way
                continue

            filename = link['href'].split('/')[-1]
            if filename in unique_filenames:
                # Exclude links with duplicate filenames (they would overwrite)
                continue
            unique_filenames.add(filename)

            urls.append(link['href'])

        return urls

    def cmr_download(self, outdir, url, token=None, username=None, password=None,
                     tries=3, timeout=5*60, skip_download=False, cover=False,
                     continuing=True, wgetpath=None, **kwargs):
        '''
        根据输入url下载相应的文件

        Args:
            outdir: str, 输出路径
            url: str, 下载链接
            timeout: int
                时间限制
            skip_download: bool
                是否不做数据下载，直接返回文件名。默认是FALSE，下载文件。

        Returns: str
            下载数据的文件名
        '''
        if token is None and username is None :
            raise Exception('请传入Token或者账号密码')

        if not os.path.isdir(outdir) :
            os.makedirs(outdir, exist_ok=True)

        if token is None :
            token = self.get_tokens(username=username, password=password)

        if token is None :
            raise Exception('获取token失败')

        filename = wget(outdir,
                        url,
                        token=token,
                        timeout=timeout,
                        tries=tries,
                        skip_download=skip_download,
                        cover=cover,
                        continuing=continuing,
                        wgetpath=wgetpath)

        return filename

    def spidertable(self, url, **kwargs):
        import pandas as pd

        try:
            df1 = pd.read_html(url, **kwargs)
            df = df1[0]

            data = df.to_dict(orient='list')

            return data
        except BaseException as e :
            print(e)
            return None

    def cmr_check_provider(self, shortname, provider=None, version=None):

        Dict_Match_Info = []

        # 第一次查询：从静态JSON文件中
        Dict_Site_Info = self.spidertable(url = r'https://cmr.earthdata.nasa.gov/search/site/collections/directory/eosdis')
        if Dict_Site_Info is None :
            return False

        CMR_Provider = Dict_Site_Info['Provider Name']
        for prodid in CMR_Provider :
            if provider is not None :
                if not prodid in [provider] :
                    continue

            # 读取JSON文件，获取提供站点信息
            dict_data = self.get_cmr_product_info(prodid)
            if not shortname in dict_data['Short Name'] :
                continue

            index = self.get_list_index(dict_data['Short Name'], shortname)
            if len(index) == 0 :
                continue

            for ind in index :
                dict_temp = {
                    'Provider' : prodid,
                    'Short Name' : np.array(dict_data['Short Name'])[ind],
                    'Collection' : np.array(dict_data['Collection'])[ind],
                    'Version' : np.array(dict_data['Version'], dtype=np.str_)[ind],
                }
                if provider is not None :
                    if not provider in [dict_temp['Provider']] :
                        continue

                if version is not None :
                    if not version in [dict_temp['Version']] :
                        continue

                Dict_Match_Info.append(dict_temp)

        if len(Dict_Match_Info) == 1:
            print('='*100)
            print('产品【%s】\n生产单位【%s】\n版本【%s】\n产品描述【%s】' %(
                shortname,
                Dict_Match_Info[0]['Provider'],
                Dict_Match_Info[0]['Version'],
                Dict_Match_Info[0]['Collection']))
            print('相关详细信息参考："https://cmr.earthdata.nasa.gov/search/site/'
                  'collections/directory/{url}/gov.nasa.eosdis"'.format(url=Dict_Match_Info[0]['Provider']))
            print('='*100)
            return True
        elif len(Dict_Match_Info) > 1 :
            for item in Dict_Match_Info :
                print('~'*100)
                print('生产单位【%s】\n版本【%s】\n产品描述【%s】' %(item['Provider'], item['Version'], item['Collection']))
                CMR_ProviderURL = 'https://cmr.earthdata.nasa.gov/search/site/' \
                                  'collections/directory/{Provider}/gov.nasa.eosdis'.format(Provider=provider)

                print('请参考Short Name【%s】"' %(CMR_ProviderURL))
                print('~'*100)

            print('该shortname【{}】有多个生产单位或版本，请指定生产单位或版本'.format(shortname))
            return False

        print('在JSON文件中未匹配到相应的产品信息，进行在线搜索方式查询')
        for prodid in CMR_Provider :
            dict_data = self.spidertable(r'https://cmr.earthdata.nasa.gov/search/site/'
                                         'collections/directory/{url}/gov.nasa.eosdis'.format(url=prodid))
            if dict_data is None :
                continue

            if not shortname in dict_data['Short Name'] :
                continue

            index = self.get_list_index(dict_data['Short Name'], shortname)
            if len(index) == 0 :
                continue

            for ind in index :
                dict_temp = {
                    'Provider' : prodid,
                    'Short Name' : np.array(dict_data['Short Name'])[ind],
                    'Collection' : np.array(dict_data['Collection'])[ind],
                    'Version' : np.array(dict_data['Version'], dtype=np.str_)[ind],
                }
                Dict_Match_Info.append(dict_temp)

            CMR_Provider_Json = os.path.join(os.path.abspath(list(docs.__path__)[0]),
                                             'provider', '%s.json' %(prodid))
            print(CMR_Provider_Json)
            writejson(CMR_Provider_Json, dict_data)

        if len(Dict_Match_Info) == 1:
            print('='*100)
            print('本产品【%s】生产单位：【%s】，版本【%s】' %(shortname, provider, version))
            print('相关详细信息参考："https://cmr.earthdata.nasa.gov/search/site/'
                  'collections/directory/{url}/gov.nasa.eosdis"'.format(url=provider))
            print('='*100)
            return True
        elif len(Dict_Match_Info) > 1 :
            for item in Dict_Match_Info :
                print('生产单位【%s】, 版本【%s】, 产品描述【%s】' %(item['Provider'], item['Version'], item['Collection']))
                CMR_ProviderURL = 'https://cmr.earthdata.nasa.gov/search/site/' \
                                  'collections/directory/{Provider}/gov.nasa.eosdis'.format(Provider=provider)

                print('请参考Short Name【%s】"' %(CMR_ProviderURL))
                print('~'*100)

            print('该shortname【{}】有多个生产单位或版本，请指定生产单位或版本'.format(shortname))
            return False

        print('未匹配到shortname【%s】相关信息，可通过接口【self.searchShortName】进行模糊查询获取' %(shortname))

        return False

    def searchShortName(self, shortname):
        ''' 根据shortname进行模糊查询 '''

        searchNameList = shortname.split('*')

        Dict_Match_Info = []
        # 第一次查询：从静态JSON文件中
        Dict_Site_Info = self.spidertable(
            url = r'https://cmr.earthdata.nasa.gov/search/site/collections/directory/eosdis')
        if Dict_Site_Info is None :
            return {}

        CMR_Provider = Dict_Site_Info['Provider Name']
        for prodid in CMR_Provider :

            # 读取JSON文件，获取提供站点信息
            dict_data = self.get_cmr_product_info(prodid)
            for item in dict_data['Short Name'] :
                matchflag = False
                for key in searchNameList :
                    if key.lower() not in item.lower() :
                        matchflag = False
                        break
                    else:
                        matchflag = True

                if not matchflag :
                    continue

                index = self.get_list_index(dict_data['Short Name'], item)
                if len(index) == 0 :
                    continue

                for ind in index :
                    dict_temp = {
                        'Provider' : prodid,
                        'Short Name' : np.array(dict_data['Short Name'])[ind],
                        'Collection' : np.array(dict_data['Collection'])[ind],
                        'Version' : np.array(dict_data['Version'], dtype=np.str_)[ind],
                    }
                    Dict_Match_Info.append(dict_temp)

        # 匹配成功则返回匹配信息
        if len(Dict_Match_Info) > 0 :
            return Dict_Match_Info

        # 在JSON文件中未匹配到相应的产品信息，则进行在线搜索方式进行查询
        for prodid in CMR_Provider :
            dict_data = self.spidertable(r'https://cmr.earthdata.nasa.gov/search/site/'
                                         'collections/directory/{url}/gov.nasa.eosdis'.format(url=prodid))
            if dict_data is None :
                return {}

            for item in dict_data['Short Name'] :
                matchflag = False
            for key in searchNameList :
                if key not in item :
                    matchflag = False
                    break
                else:
                    matchflag = True

            if not matchflag :
                continue

            index = self.get_list_index(dict_data['Short Name'], item)
            if len(index) == 0 :
                continue

            for ind in index :
                dict_temp = {
                    'Provider' : prodid,
                    'Short Name' : np.array(dict_data['Short Name'])[ind],
                    'Collection' : np.array(dict_data['Collection'])[ind],
                    'Version' : np.array(dict_data['Version'], dtype=np.str_)[ind],
                }
                Dict_Match_Info.append(dict_temp)

            # 在线匹配成功后，更新库里的文件信息
            CMR_Provider_Json = os.path.join(os.path.abspath(list(docs.__path__)[0]),
                                             'provider', '%s.json' %(prodid))
            writejson(CMR_Provider_Json, dict_data)

        return Dict_Match_Info


    def get_cmr_product_info(self, provider):

        CMR_Provider_Json = os.path.join(os.path.abspath(list(docs.__path__)[0]),
                                         'provider', '%s.json' %(provider))

        if os.path.isfile(CMR_Provider_Json) and ((time.time() - os.stat(CMR_Provider_Json).st_mtime ) < 24*60*60*10) :
            dict_data = readjson(CMR_Provider_Json)
        else:
            dict_data = self.spidertable(r'https://cmr.earthdata.nasa.gov/search/site/'
                                         'collections/directory/{url}/gov.nasa.eosdis'.format(url=provider),
                                         converters={'Version':str})
            if dict_data is None :
                return None

            dirname = os.path.dirname(CMR_Provider_Json)
            if not os.path.isdir(dirname) :
                os.makedirs(dirname)

            writejson(CMR_Provider_Json, dict_data)

        return dict_data

    def get_list_index(self, srclist, patter) :

        index = []
        if patter in srclist :
            for i in range(len(srclist)) :
                item = srclist[i]
                if patter in [item] :
                    index.append(i)

        return np.array(index, dtype=np.int32)