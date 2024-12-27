# -*- coding:utf-8 -*-
'''
@Project  : lb_toolkits
@File     : spider.py
@Modify Time      @Author    @Version    
--------------    -------    --------    
2022/7/14 10:28      Lee       1.0         
@Description
------------------------------------
 
'''
import datetime
import os
import shutil
import re
import time

import requests

from tqdm import tqdm
from bs4 import BeautifulSoup
from lb_toolkits.utils.jsonpro import writejson


class spiderdownload(object):

    def __init__(self, username=None, password=None):

        self.session = requests.Session()
        # if username is not None and password is not None :
        #     self.login(username, password)

    def logged_in(self):
        """Check if the log-in has been successfull based on session cookies."""
        eros_sso = self.session.cookies.get("EROS_SSO_production_secure")
        return bool(eros_sso)

    def login(self, username, password, url_login):
        """Login to URL."""

        rsp = self.session.get(url_login)
        csrf = self.get_tokens(rsp.text)
        payload = {
            "username": username,
            "password": password,
            "csrf": csrf,
        }
        rsp = self.session.post(url_login, data=payload, allow_redirects=True)

        if not self.logged_in():
            raise Exception("login failed.")

    def logout(self, url_logout):
        """Log out from URL."""
        self.session.get(url_logout)

    def get_tokens(self, body, pattern=r'name="csrf" value="(.+?)"'):
        """Get `csrf_token` and `__ncforminfo`."""
        tokens = re.findall(pattern, body)[0]
        # ncform = re.findall(r'name="__ncforminfo" value="(.+?)"', body)[0]

        if not tokens:
            raise Exception("login failed (token not found).")

        return tokens

    def download(self, outdir, url, timeout=5 * 60, skip_download=False, cover=False):
        """Download a Landsat scene.

        Parameters
        ----------
        identifier : str
            Scene Entity ID or Display ID.
        outdir : str
            Output directory. Automatically created if it does not exist.
        dataset : str, optional
            Dataset name. If not provided, automatically guessed from scene id.
        timeout : int, optional
            Connection timeout in seconds.
        skip_download : bool, optional
            Skip download, only returns the remote filename.

        cover : bool, optional
            如果为TRUE，文件存在则会被覆盖，如果为FALSE，文件存在会跳过下载

        Returns
        -------
        filename : str
            Path to downloaded file.
        """
        os.makedirs(outdir, exist_ok=True)

        filename = self._download(outdir, url, timeout=timeout, skip_download=skip_download, cover=cover)

        return filename

    # def _download(self, outdir, url, timeout, chunk_size=1024, skip=False, cover=False):
    #     """ 根据url连接下载远程文件 """
    #     download_url = url
    #     basename = os.path.basename(download_url)
    #     local_filename = os.path.join(outdir, basename)
    #     tempfile = local_filename + '.download'
    #     if skip:
    #         return local_filename
    #
    #     if os.path.isfile(local_filename) :
    #         if cover :
    #             os.remove(local_filename)
    #             print('文件已存在，删除该文件后重新下载【%s】' %(local_filename))
    #         else:
    #             print('文件已存在，跳过下载该文件【%s】' %(local_filename))
    #             return local_filename
    #
    #     headers = {}
    #
    #     already_downloaded_bytes = 0
    #
    #     file_size = self._getremotefilesize(url, timeout)
    #     try:
    #         with self.session.get(
    #                 download_url, stream=True, allow_redirects=True,
    #                 timeout=timeout
    #         ) as r:
    #
    #             with tqdm(
    #                     total=file_size, unit_scale=True, unit="B", desc=f"正在下载【{basename}】",
    #                     unit_divisor=1024, initial=already_downloaded_bytes,
    #             ) as pbar:
    #
    #                 mode = "wb"
    #                 with open(tempfile, mode) as f:
    #                     for chunk in r.iter_content(chunk_size=chunk_size):
    #                         if chunk:
    #                             f.write(chunk)
    #                             pbar.update(len(chunk))
    #
    #         if file_size == os.path.getsize(tempfile):
    #             shutil.move(tempfile, local_filename)
    #         if file_size == -1 :
    #             shutil.move(tempfile, local_filename)
    #     except requests.exceptions.Timeout:
    #         raise Exception(
    #             "Connection timeout after {} seconds.".format(timeout)
    #         )
    #     print('成功下载【%s】' %(local_filename))
    #
    #     return local_filename

    def _download(self, outdir, url, timeout=5*60, chunk_size=1024, skip_download=False, cover=False, continuing=False):
        """ 根据url连接下载远程文件 """

        download_url = url
        basename = os.path.basename(download_url)
        local_filename = os.path.join(outdir, basename)
        tempfile = local_filename + '.download'
        if skip_download:
            return local_filename

        if os.path.isfile(local_filename) :
            if cover :
                os.remove(local_filename)
                print('文件已存在，删除该文件后重新下载【%s】' %(local_filename))
            else:
                print('文件已存在，跳过下载该文件【%s】' %(local_filename))
                return local_filename

        file_size = self._getremotefilesize(url, timeout)

        headers = {}

        if continuing and os.path.isfile(tempfile) and file_size > 0:
            already_downloaded_bytes = os.path.getsize(tempfile)
            if already_downloaded_bytes < file_size :
                headers = {"Range": "bytes={}-".format(already_downloaded_bytes)}
                print('将继续断点续传：原数据【%dB】, 已下载【%dB】' %(file_size, already_downloaded_bytes))
            else:
                already_downloaded_bytes = 0
                continuing = False
        else:
            already_downloaded_bytes = 0
            continuing = False

        try:
            with self.session.get(
                    download_url, stream=True, allow_redirects=True,
                    timeout=timeout, headers=headers
            ) as r:
                if r.status_code != 200 :
                    return None

                nowtime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                with tqdm(
                        total=file_size, unit_scale=True, unit="B", desc=f"【{nowtime}】正在下载【{basename}】",
                        unit_divisor=1024, initial=already_downloaded_bytes,
                ) as pbar:

                    mode = "ab" if continuing else "wb"
                    with open(tempfile, mode) as f:
                        for chunk in r.iter_content(chunk_size=chunk_size):
                            if chunk:
                                f.write(chunk)
                                pbar.update(len(chunk))
            # print(file_size, os.path.getsize(tempfile))
            time.sleep(1)
            if file_size == os.path.getsize(tempfile):
                shutil.move(tempfile, local_filename)
                print('成功下载【%s】' %(local_filename))
            elif file_size == -1 :
                shutil.move(tempfile, local_filename)
                print('成功下载【%s】' %(local_filename))
            elif file_size <  os.path.getsize(tempfile) :
                print('该文件下载大小不一致【%d】【%d】【%s】' %(file_size,
                                                   os.path.getsize(tempfile),
                                                   local_filename))
                shutil.move(tempfile, local_filename)
            else:
                print('下载失败【%s】' %(local_filename))
        except requests.exceptions.Timeout:
            print("连接超时【{}】".format(timeout))
            return None

        return local_filename

    def searchfile(self, url, pattern='.tif', attrs={}):
        '''

        :param nowdate:
        :return:
        '''

        url = url.replace('\\', '/')

        res = self.session.get(url)

        soup = BeautifulSoup(res.text, 'lxml')
        r = soup.find_all(href=re.compile(pattern), attrs=attrs)
        filelist = []
        for name in r :
            if name['href'].endswith(pattern) :
                filelist.append(name['href'])
        # print(filelist)

        return filelist

    def _getremotefilesize(self, url, timeout):
        try:
            with self.session.get(
                    url, stream=True, allow_redirects=True,
                    timeout=timeout) as r:
                return int(r.headers.get("Content-Length"))
        except BaseException as e :
            return -1

    def __del__(self):
        if self.session is not None :
            self.session.close()
        self.session = None

def spiderhref( url, pattern=None, attrs={}):
    ''' 爬虫获取url中的链接'''
    session = requests.Session()
    res = session.get(url)

    soup = BeautifulSoup(res.text, 'lxml')
    if pattern is None :
        r = soup.find_all('a', attrs=attrs)
    else:
        r = soup.find_all('a', href=re.compile(pattern), attrs=attrs)
    urllist = []
    for name in r :
        href = name.get('href')
        urllist.append(href)

    return urllist

def spidertable( url, outname=None, format='dict'):
    ''' 爬虫获取URL中的table'''
    import pandas as pd

    df1 = pd.read_html(url)
    df = df1[0]

    data = df.to_dict(orient='list')
    if outname is not None :
        if outname.endswith('.json') :
            writejson(outname, data)
        elif outname.endswith('.xls') :
            df.to_excel(outname)
    return df

def spidertable1(url):
    import pandas as pd

    df1 = pd.read_html(url)
    df = df1[0]

    data = df.to_dict(orient='list')

    return data




