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
import netrc
import shutil
import ssl
import sys

import numpy as np
import requests
import datetime
import platform
import glob

from lb_toolkits import docs
from lb_toolkits.tools import readjson, writejson
from lb_toolkits.tools import wget
from urllib.request import urlopen, Request

# from .config import WGET

CMR_URL = 'https://cmr.earthdata.nasa.gov'
URS_URL = 'https://urs.earthdata.nasa.gov'

class cmr() :

    def __init__(self):
        pass

    def Options(self, sort_key='start_date', scroll=True,
                polygon=None, point=None, line=None, circle=None,
                bounding_box=None, data_center=None, provider=None,
                project=None, processing_level_id=None,
                spatial_keyword=None, collection_data_type=None,
                granule_data_format=None, downloadable=False,
                cloud_cover=None, version=None, pattern=None, **kwargs):

        new_options =''
        if sort_key is not None:
            new_options += '&sort_key[]=' + sort_key

        if scroll:
            new_options += '&scroll=true'

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
                   page_size=2000, **kwargs):

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
        print('查询链接:\n{0}\n'.format(parms))

        return self.cmr_get_urls(parms)

    def cmr_get_urls(self, cmr_query_url):
        cmr_scroll_id = None
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        urls = []

        try:
            while True:
                req = Request(cmr_query_url)
                if cmr_scroll_id:
                    req.add_header('cmr-scroll-id', cmr_scroll_id)
                response = urlopen(req, context=ctx)
                if not cmr_scroll_id:
                    headers = {k.lower(): v for k, v in dict(response.info()).items()}
                    cmr_scroll_id = headers['cmr-scroll-id']
                    hits = int(headers['cmr-hits'])
                    if hits > 0:
                        print('共匹配【{count}】个文件'.format(count=hits))
                    else:
                        print('未查询到满足相应条件的文件')
                search_page = response.read()
                search_page = json.loads(search_page.decode('utf-8'))
                url_scroll_results = self.cmr_filter_urls(search_page)
                if not url_scroll_results:
                    break
                if hits > 2000:
                    print('.', end='')
                    sys.stdout.flush()
                urls += url_scroll_results

            return urls
        except KeyboardInterrupt:
            quit()

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
        for link in links:
            if 'href' not in link:
                # Exclude links with nothing to download
                continue
            if 'inherited' in link and link['inherited'] is True:
                # Why are we excluding these links?
                continue
            if 'rel' in link and 'data#' not in link['rel']:
                # Exclude links which are not classified by CMR as "data" or "metadata"
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
                     timeout=5*60, skip=False, cover=False, wgetpath=None, **kwargs):
        '''
        根据输入url下载相应的文件

        Args:
            outdir: str, 输出路径
            url: str, 下载链接
            timeout: int
                时间限制
            skip: bool
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

        filename = wget(outdir, url, token=token, timeout=timeout,
                        skip=skip, cover=cover, wgetpath=wgetpath)
        # filename = self._cmr_download(outdir, url, token=token,
        #                               timeout=timeout, skip=skip, cover=cover)

        return filename

    # def _cmr_download(self, outdir, url, token=None, timeout=5*60, tries=3,
    #                   chunk_size=1024, skip=False, cover=False):
    #     '''通过wget方式进行数据下载'''
    #     local_filename = os.path.basename(url)
    #     local_filename = os.path.join(outdir, local_filename)
    #     if skip :
    #         return local_filename
    #
    #     if os.path.isfile(local_filename) :
    #         if cover :
    #             print('文件已存在，将执行删除文件【%s】' %(local_filename))
    #             os.remove(local_filename)
    #         else:
    #             print('文件已存在，跳过下载【%s】' %(local_filename))
    #             return local_filename
    #
    #     tempfile = local_filename + '.download'
    #
    #     if platform.system().lower() == 'windows' :
    #         cmd = f'{WGET} --tries={tries} --no-check-certificate ' \
    #               f'-e robots=off -c -np -R .html,.tmp -nH --cut-dirs=10 {url} ' \
    #               f'--header "Authorization: Bearer {token}" -O {tempfile}'
    #     else:
    #         cmd = f'{WGET} --tries={tries} --no-check-certificate ' \
    #               f'-e robots=off -c -np -R .html,.tmp -nH --cut-dirs=10 {url} ' \
    #               f'--header "Authorization: Bearer {token}" -O {tempfile}'
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
    #     return local_filename

    def spidertable(self, url):
        import pandas as pd

        df1 = pd.read_html(url)
        df = df1[0]

        data = df.to_dict(orient='list')

        return data

    def cmr_check_provider(self, shortname, provider=None, collection=None, version=None):

        providerFlag = False
        shortnameFlag = False
        CollectionFlag = False
        versionFlag = False

        CMR_Provider_List = []
        CMR_ShortName_List = []
        CMR_Collection_List = []
        CMR_Version_List = []

        # 第一次查询：从静态JSON文件中
        CMR_Provider_Jsons = glob.glob(os.path.join(os.path.abspath(list(docs.__path__)[0]),
                                                    'provider', '*.json'))
        for filename in CMR_Provider_Jsons :
            basename = os.path.basename(filename)
            prodid = basename.split('.')[0]
            if provider is not None :
                if not prodid in [provider] :
                    continue

            # 读取JSON文件，获取提供站点信息
            dict_data = readjson(filename)
            if not shortname in dict_data['Short Name'] :
                continue

            index = self.get_list_index(dict_data['Short Name'], shortname)
            if len(index) == 0 :
                continue

            provider = prodid
            CMR_Provider_List.append(prodid)
            CMR_ShortName_List.extend(np.array(dict_data['Short Name'])[index])
            CMR_Collection_List.extend(np.array(dict_data['Collection'])[index])
            CMR_Version_List.extend(list(np.array(dict_data['Version'], dtype=np.str_)[index]))

        if len(CMR_Provider_List) > 1 :
            raise Exception('该shortname【{}】有多个生产单位，请指定生产单位provider:{}'.format(
                shortname, CMR_Provider_List))
        elif len(CMR_Provider_List) == 1 :
            provider = CMR_Provider_List[0]

        if not shortname in CMR_ShortName_List :
            shortnameFlag = False

        if version is not None :
            if not version in CMR_Version_List :
                versionFlag = False
        else:
            if len(CMR_Version_List) > 1 :
                raise Exception('该shortname【{}】有多个版本，请指定生产版本version:{}'.format(
                    shortname, CMR_Version_List))
            elif len(CMR_Version_List) == 1 :
                version = CMR_Version_List[0]

        # 在JSON文件中未匹配到相应的产品信息
        # 第二次查询：通过在线搜索方式进行查询
        if not shortnameFlag or not versionFlag:
            CMR_Provider_List = []
            CMR_ShortName_List = []
            CMR_Collection_List = []
            CMR_Version_List = []

            if provider is None :
                Dict_Site_Info = self.spidertable(
                    url = r'https://cmr.earthdata.nasa.gov/search/site/collections/directory/eosdis')
                CMR_Provider = Dict_Site_Info['Provider Name']
            else:
                CMR_Provider = [provider]

            for prodid in CMR_Provider :
                dict_data = self.spidertable(r'https://cmr.earthdata.nasa.gov/search/site/'
                                             'collections/directory/{url}/gov.nasa.eosdis'.format(url=prodid))

                index = self.get_list_index(dict_data['Short Name'], shortname)
                if len(index) == 0 :
                    continue

                CMR_Provider_List.append(prodid)
                CMR_ShortName_List.extend(np.array(dict_data['Short Name'])[index])
                CMR_Collection_List.extend(np.array(dict_data['Collection'])[index])
                CMR_Version_List.extend(list(np.array(dict_data['Version'], dtype=np.str_)[index]))

                provider = prodid
                CMR_Provider_Json = os.path.join(os.path.abspath(list(docs.__path__)[0]),
                                                            'provider', '%s.json' %(prodid))
                print(CMR_Provider_Json)
                writejson(CMR_Provider_Json, dict_data)

        if len(CMR_Provider_List) > 1 :
            raise Exception('该shortname【{}】有多个生产单位，请指定生产单位provider:{}'.format(
                shortname, CMR_Provider_List))
        elif len(CMR_Provider_List) == 1 :
            provider = CMR_Provider_List[0]
            providerFlag = True

        if shortname is not None :
            if shortname in CMR_ShortName_List :
                shortnameFlag = True
            else:
                raise Exception('输入的shortname参数【{}】错误，当前仅支持shortname:{}'.format(
                    shortname, CMR_ShortName_List))

        if collection is not None :
            if collection in CMR_Collection_List :
                CollectionFlag = True
            else:
                raise Exception('输入的Collection参数【{}】错误，当前仅支持Collection:{}'.format(
                    collection, CMR_Collection_List))
        else:
            CollectionFlag = True

        if version is not None :
            if not version in CMR_Version_List :
                raise Exception('输入的version参数【{}】错误，当前仅支持version:{}'.format(
                    version, set(CMR_Version_List)))
                versionFlag = False
            else:
                versionFlag = True

        print('='*100)
        print('本产品【%s】生产单位：【%s】' %(shortname, provider))
        print('相关详细信息参考："https://cmr.earthdata.nasa.gov/search/site/'
              'collections/directory/{url}/gov.nasa.eosdis"'.format(url=provider))
        print('='*100)

        return providerFlag & shortnameFlag & CollectionFlag & versionFlag

    def get_cmr_product_info(self, provider, shortname):

        dict_data = self.spidertable(r'https://cmr.earthdata.nasa.gov/search/site/'
                                     'collections/directory/{url}/gov.nasa.eosdis'.format(url=provider))

        return dict_data


    def get_list_index(self, srclist, patter) :

        index = []
        if patter in srclist :
            for i in range(len(srclist)) :
                item = srclist[i]
                if patter in [item] :
                    index.append(i)

        return np.array(index, dtype=np.int)