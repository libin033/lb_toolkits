# -*- coding:utf-8 -*-
'''
@Project     : lb_toolkits

@File        : downloadGithub.py

@Modify Time :  2023/3/13 15:18   

@Author      : Lee    

@Version     : 1.0   

@Description :

'''
import json
import os
import requests
from urllib import parse

from lb_toolkits import parm

exedir = os.path.abspath(list(parm.__path__)[0])
from lb_toolkits.utils import spiderdownload

class downloadGithub :

    def __init__(self, username=None):

        self.username=username

    def searfile(self, giturl=None, repositories=None,
                       srcdir=None, branches='master') :

        if giturl is None :
            if self.username is None or repositories is None or srcdir is None :
                raise Exception('请设置【giturl】或者【username, repositories, srcdir】参数')
            else:
                giturl = 'https://github.com/{username}/{repositories}/tree/{branches}/{srcdir}'.format(
                    username=self.username,
                    repositories=repositories,
                    srcdir=srcdir,
                    branches=branches)

        return self.GetGitUrl(giturl)

    def download(self, dstdir, srcurl):
        spider = spiderdownload()

        url = srcurl.replace('github.com', 'raw.githubusercontent.com')
        url = url.replace('/blob', '')
        url = url.replace('/tree', '')
        urlunqot = parse.unquote(url)

        filename = spider.download(dstdir, urlunqot)
        del spider

        return filename

    def GetGitUrl(self, giturl):
        ''' 爬虫获取url中的链接'''

        # print(giturl)
        session = requests.Session()
        res = session.get(giturl)
        if not 'payload' in res.text :
            return []

        resjson = json.loads(res.text)
        session.close()

        matchurl = []

        if 'payload' in resjson :
            payload = resjson['payload']
            if 'tree' in payload :
                for item in payload['tree']['items'] :
                    if item['contentType'] in ['directory'] :
                        srcurl = giturl + '/' + item['name']

                        url = self.GetGitUrl(srcurl)
                        if len(url) != 0 :
                            matchurl.extend(url)
                    elif item['contentType'] in ['file'] :
                        srcurl = giturl + '/' + item['name']
                        matchurl.append(srcurl)

            if 'fileTree' in payload :
                return [giturl]
                for tree in payload['fileTree'] :
                    for item in payload['fileTree'][tree]['items'] :
                        if item['contentType'] in ['directory'] :
                            srcurl = giturl + '/' + item['name']

                            url = self.GetGitUrl(srcurl)
                            if len(url) != 0 :
                                matchurl.extend(url)
                        elif item['contentType'] in ['file'] :
                            srcurl = giturl + '/' + item['name']
                            matchurl.append(srcurl)

        return matchurl

