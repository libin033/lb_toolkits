# -*- coding:utf-8 -*-
'''
@Project     : lb_toolkits  
----------------------------------------
@File        : USGSToken.py  
----------------------------------------
@Modify Time : 2025/8/14  
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
import logging
import requests
from urllib.parse import urljoin
import re
import json
from bs4 import BeautifulSoup

API_URL = "https://m2m.cr.usgs.gov/api/api/json/stable/"
USGS_ROOT_URL   = "https://ers.cr.usgs.gov/"
USGS_LOGIN_URL  = "https://ers.cr.usgs.gov/login/"
USGS_LOGOUT_URL  = "https://ers.cr.usgs.gov/logout/"

class USGSToken :
    def __init__(self, username, password):
        self.session_usgs = requests.Session()
        self.login(username, password)

    def login(self, username, password):
        rsp = self.session_usgs.get(USGS_LOGIN_URL)
        csrf = self._get_csrf(rsp.text)
        payload = {
            "username": username,
            "password": password,
            "csrf": csrf,
        }
        # 登录USGS官网
        rsp = self.session_usgs.post(USGS_LOGIN_URL, data=payload, allow_redirects=True)

        # 创建Token
        self.token_id, self.token = self.createToken()

    def logout(self):
        """Logout from USGS M2M API."""
        self.session_usgs.get(USGS_LOGOUT_URL)
        self.session = requests.Session()

    def createToken(self, token_id=None):
        url = urljoin(USGS_ROOT_URL, "password/appgenerate?operation=generate")

        if token_id is None:
            token_id = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        payload = {
            'date_expires' : (datetime.datetime.now()+datetime.timedelta(days=30)).strftime("%Y-%m-%d"),
            'scopes' : 'M2M',
            'token_description' : token_id
        }

        rsp = self.session_usgs.post(url, data=payload, allow_redirects=True)

        text = json.loads(rsp.text)

        token = None
        cnt = None
        if 'token' in text:
            token = text['token']
            cnt = text['tokenCount']

        return token_id, token

    def deleteToken(self, token_id):

        url = urljoin(USGS_ROOT_URL, 'password/appremove')
        payload = {
            'token_id' : token_id
        }
        rsp = self.session_usgs.post(url, data=payload, allow_redirects=True)
        if rsp.json().get('success') :
            logging.info('成功删除Token【%s】' % token_id)
        else:
            logging.error('失败删除Token【%s】' % token_id)

    def searchToken(self, token_id):

        rsp = self.session_usgs.get(USGS_ROOT_URL)
        html_content = rsp.text

        soup = BeautifulSoup(html_content, 'html.parser')
        table = soup.find('table')

        for row in table.find_all('tr'):
            cells = row.find_all('td')
            row_data = [cell.text.strip() for cell in cells]
            logging.info(row_data)

            if 'M2M API' in row_data:
                rowdata = list(row_data)
                if len(rowdata) == 6 :
                    if datetime.datetime.strptime(rowdata[3], "%Y-%m-%d") <= datetime.datetime.now():
                        self.deleteToken(row.get('data-tokenid'))

            if token_id in row_data :
                return row.get('data-tokenid')
        return None

    def _get_csrf(self, body):
        """Get `csrf_token`."""
        csrf = re.findall(r'name="csrf" value="(.+?)"', body)[0]

        return csrf

    def __del__(self):
        try:
            token_id  = self.searchToken(self.token_id)
            self.deleteToken(token_id)
        except Exception as e:
            logging.error(e)
