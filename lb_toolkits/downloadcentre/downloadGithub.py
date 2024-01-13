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
import sys
import numpy as np
import datetime
import shutil
import zipfile
import requests
from urllib import parse

from lb_toolkits import parm

exedir = os.path.abspath(list(parm.__path__)[0])

def downloadGithub(dstdir, giturl=None,
                   username=None, repositories=None,
                   srcdir=None, branches='master') :

    from lb_toolkits.tools import spiderdownload

    if giturl is None :
        if username is None or repositories is None or srcdir is None :
            raise Exception('请设置【giturl】或者【username, repositories, srcdir】参数')
        else:
            # url = 'https://raw.githubusercontent.com/{username}/{repositories}/{branches}/{srcdir}'.format(
            #     username=username,
            #     repositories=repositories,
            #     srcdir=srcdir,
            #     branches=branches)
            giturl = 'https://github.com/{username}/{repositories}/tree/{branches}/{srcdir}'.format(
                username=username,
                repositories=repositories,
                srcdir=srcdir,
                branches=branches)

    urllist = GetGitUrl(giturl)

    spider = spiderdownload()
    for srcurl in urllist :

        url = srcurl.replace('github.com', 'raw.githubusercontent.com')
        url = url.replace('/blob', '')
        url = url.replace('/tree', '')
        urlunqot = parse.unquote(url)
        print(urlunqot)
        spider.download(dstdir, urlunqot)

def GetGitUrl(giturl):
    ''' 爬虫获取url中的链接'''

    # print(giturl)
    session = requests.Session()
    res = session.get(giturl)
    # print(res.text)
    if not 'payload' in res.text :
        return []

    resjson = json.loads(res.text)
    session.close()

    matchurl = []

    if 'payload' in resjson :
        payload = resjson['payload']
        for item in payload['tree']['items'] :
            if item['contentType'] in ['directory'] :
                srcurl = giturl + '/' + item['name']
                url = GetGitUrl(srcurl)
                if len(url) != 0 :
                    matchurl.extend(url)
            elif item['contentType'] in ['file'] :
                srcurl = giturl + '/' + item['name']
                matchurl.append(srcurl)

    return matchurl


def unzip(outname, srcname):
    outdir = os.path.dirname(outname)
    basename = os.path.basename(outname)

    if os.path.isfile(srcname) :
        fp = zipfile.ZipFile(srcname, 'r')
        for item in fp.filelist :
            srcfile = item.filename

            if os.path.basename(srcfile) in [basename] :
                if not os.path.isdir(outdir) :
                    os.makedirs(outdir)
                fp.extract(item, outdir)
                shutil.move(os.path.join(outdir, item.filename), outdir)
                shutil.rmtree(os.path.join(outdir, 'lb_toolkits-master'))
        fp.close()
        os.remove(srcname)


def downwgetfromgithub(dstfile, github_url='https://github.com/libin033/lb_toolkits/archive/refs/heads/master.zip'):
    from lb_toolkits.tools import spiderdownload
    spider = spiderdownload()
    spider.download(exedir, github_url)
    filename = os.path.join(exedir, 'master.zip')
    unzip(dstfile, filename)

