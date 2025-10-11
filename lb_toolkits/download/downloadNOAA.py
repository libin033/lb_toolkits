# -*- coding:utf-8 -*-
'''
@Project     : lb_toolkits  
----------------------------------------
@File        : downloadNOAA.py  
----------------------------------------
@Modify Time : 2025/7/27  
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

import requests
import logging
import json
from lb_toolkits.utils.wget import wget

Base_Url = 'https://www.ncdc.noaa.gov'

class downloadNOAA :
    logger = logging.getLogger(__name__)

    def __init__(self, emailId, timeout=60):
        self.emailId = emailId
        self.session = requests.Session()
        self.session.timeout = timeout

    def searchfile(self,
                   startdate,
                   enddate,
                   datatype,
                   prodtype=None,
                   channelId=None,
                   scanSector='F',
                   satellite='G19'):

        option = []

        # TODO 针对不同的datatype，需要提供不同的可选参数
        if prodtype is not None:
            if isinstance(prodtype, str):
                value = [prodtype]
            elif isinstance(prodtype, list):
                value = prodtype

            option.append({
                "key": "Product Type",
                "values": { "value": value }
            })

        if channelId is not None:
            if isinstance(channelId, str):
                value = [channelId]
            elif isinstance(channelId, list):
                value = []
                for item in channelId:
                    if isinstance(item, str):
                        value.append(item)
                    elif isinstance(item, int) :
                        value.append('C%02d' %item)

            option.append({
                "key": "ABI Channel",
                "values": { "value": value }
            },)

        if scanSector is not None:
            if isinstance(scanSector, str):
                value = [scanSector]
            elif isinstance(scanSector, list):
                value = scanSector
            option.append({
                "key": "ABI Scan Sector",
                "values": { "value": value }
            },)

        if satellite is not None:
            if isinstance(satellite, str):
                value=[satellite]
            elif isinstance(satellite, list):
                value = satellite
            option.append({
                "key": "Satellite",
                "values": { "value": value }
            })

        data = {
            "dataTypeID" : datatype,
            "level" : "SUMMARY",
            "beginDateTime" : startdate.strftime('%Y-%m-%dT%H:%M:%S'),   #"2025-07-25T21:00:00",
            "endDateTime" : enddate.strftime('%Y-%m-%dT%H:%M:%S'),      #"2025-07-25T21:59:59",
            "options" : {
                "option": option
            }
        }

        searchid = self.getSearchID(data)
        if searchid is None:
            return None

        files = self.selectFile(searchid)
        if len(files) == 0:
            return None

        orderId = self.commitOrder(searchid, number=len(files))
        if orderId is None:
            return None

        return (f'https://www.ncdc.noaa.gov/airs/GetOrders?email={self.emailId}&limit=10&offset=1&id={orderId}', searchid)

    def getSearchID(self, data):
        headers = {
            "Content-Type": "application/json;charset=UTF-8"
        }
        url = 'https://www.ncdc.noaa.gov/airs-web/api/v1/submitSearch'
        resp = requests.post(url, headers=headers, json=data)
        if resp.status_code == 200 :
            res = json.loads(resp.text)
            searchId = res['searchId']
        else:
            raise Exception('请求失败【%s】' %(url))

        return searchId

    def selectFile(self, searchId):
        url = 'https://www.ncdc.noaa.gov/airs-web/api/v1/getSearchResults?searchId=%s' %(searchId)
        resp = requests.get(url)
        if resp.status_code == 200 :
            pass

        # NOTE : 该操作需要进行两次请求，第一次失败，第二次才能成功
        resp = requests.get(url)
        if resp.status_code == 200 :
            res = json.loads(resp.text)
        else:
            print('请求失败【%s】' %(url))
            return None

        if res['errors'] is not None :
            print('请求失败【%s】' %(url))
            return None

        if res['number'] > 1000 :
            print('文件数限制：查找到文件个数【%d】,超过1000个文件' %(res['number']))
            return None

        matchfiles = []
        for item in res['results'] :
            matchfiles.append(item['datasetname'])
        print('应匹配文件数【%d】, 实际匹配文件数【%d】' %(res['number'], len(matchfiles)))

        return matchfiles


    def commitOrder(self, searchId, number):
        headers = {
            "Content-Type": "application/json;charset=UTF-8"
        }
        url = 'https://www.ncdc.noaa.gov/airs-web/api/v1/submitSearchOrder'
        data = {
            "searchId": str(searchId),
            "items": str(number),
            # "datasetName":"ABI L1b Radiances Data",
            # "datasetId":"ABIL1RAD",
            "email": self.emailId,
        }
        resp = requests.post(url, headers=headers, json=data)
        if resp.status_code == 200 :
            res = json.loads(resp.text)
        else:
            print('请求失败【%s】' %(url))
            return None

        if not res['success'] :
            print('请求失败【%s】' %(url))
            print(res['errorMessage'])
            return None

        return res["order"]["orderId"]

    def getDownloadUrl(self, url):

        resp = requests.get(url)
        if resp.status_code == 200 :
            res = json.loads(resp.text)
        else:
            print('请求失败【%s】' %(url))
            return None

        downloadURL = res['orders'][0]['downloadURL']
        if downloadURL is None:
            return None

        return os.path.basename(downloadURL)

    def getdownurl(self, url, files):

        downfiles = []
        for file in files :
            downfiles.append(f'https://order.class.noaa.gov/downloads/public/{url}/001/{file}')

        return downfiles

    def download(self, outdir,
                 url,
                 tries=3,
                 timeout=300,
                 skip_download=False,
                 cover=False,
                 continuing=True,
                 **kwargs):

        if url is None:
            return None

        orderurl, searchid = url

        orderid = self.getDownloadUrl(orderurl)
        if orderid is None:
            return None

        files = self.selectFile(searchid)
        downurls = self.getdownurl(orderid, files)

        downfiles = []
        for downurl in downurls :
            print(downurl)

            filename = wget(outdir=outdir,
                            url=downurl,
                            tries=tries,
                            skip_download=skip_download,
                            continuing=continuing,
                            timeout=timeout)
            downfiles.append(filename)

        return downfiles
