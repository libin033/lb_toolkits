# -*- coding:utf-8 -*-
'''
@Project     : lb_toolkits

@File        : downloadGithub.py

@Modify Time :  2023/3/13 15:18   

@Author      : Lee    

@Version     : 1.0   

@Description :

'''
import os
import sys
import numpy as np
import datetime
import shutil
import zipfile

from lb_toolkits import parm

exedir = os.path.abspath(list(parm.__path__)[0])

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

