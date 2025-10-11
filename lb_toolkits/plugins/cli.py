# -*- coding:utf-8 -*-
'''
@Project     : lb_toolkits  
----------------------------------------
@File        : cli.py  
----------------------------------------
@Modify Time : 2025/5/26  
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

from pkg_resources import require

"""Command-line interface."""

import json
import csv
from io import StringIO
from lb_toolkits.downloadcentre import DownloadCentre
from lb_toolkits.DataCollections import DataCollections
from lb_toolkits.utils.spider import spiderdownload
from lb_toolkits.utils.ftppro import ftppro
from lb_toolkits.utils.sftppro import sftppro

import click

@click.group()
def cli():
    pass


@click.command()
@click.option("--ip",           required=True, default=None, help="下载地址")
@click.option("--url", '-i',    required=True, default=None, help="下载文件位置")
@click.option("--outdir", '-o', required=False, default='./', help="输出路径，默认当前文件夹")
@click.option("--user", "-u",                  default=None, help="账号")
@click.option("--password", "-p",              default=None, help="密码")
@click.option("--skip_download", is_flag=True, default=False, help="是否跳过下载")
@click.option("--cover",         is_flag=True, default=False, help="是否覆盖原文件")
def ftp(ip, url, outdir, user, password, skip_download, cover):
    """查找链接"""
    mftp = ftppro(ip, user, password)
    mftp.downloadFile(url, outdir, blocksize=1*1024, skip_download=skip_download, cover=cover)
    del mftp

@click.command()
@click.option("--collection", "-c", type=click.STRING, required=True, help="数据唯一编码")
@click.option("--startdate", "-s", type=click.STRING, required=False, default=None, help="yyyy-MM-ddTHH:mm:ssZ")
@click.option("--enddate", "-e", type=click.STRING, required=False, default=None, help="yyyy-MM-ddTHH:mm:ssZ")
@click.option(
    "-b",
    "--bbox",
    type=click.FLOAT,
    nargs=4,
    help="Bounding box (xmin, ymin, xmax, ymax).",
)
def search(collection, startdate, enddate, bbox):

    if startdate is not None:
        startDate = datetime.datetime.strptime(startdate, "%Y-%m-%dT%H:%M:%SZ")

    if enddate is not None:
        endDate = datetime.datetime.strptime(enddate, "%Y-%m-%dT%H:%M:%SZ")

@click.command()
@click.option("--collection", "-c", type=click.STRING, required=True, help="数据唯一编码")
@click.option("--startdate", "-s", type=click.STRING, required=False, default=None, help="yyyy-MM-ddTHH:mm:ssZ")
@click.option("--enddate", "-e", type=click.STRING, required=False, default=None, help="yyyy-MM-ddTHH:mm:ssZ")
@click.option("-b", "--bbox", type=click.FLOAT, nargs=4, default=None, help="Bounding box (xmin, ymin, xmax, ymax).")
@click.option("--outdir", '-o', required=False, default='./', help="输出路径，默认当前文件夹")
@click.option("--user", "-u",                  default=None, help="账号")
@click.option("--password", "-p",              default=None, help="密码")
@click.option("--skip_download", is_flag=True, default=False, help="是否跳过下载")
@click.option("--cover",         is_flag=True, default=False, help="是否覆盖原文件")
def download(collection, startdate, enddate, user, password, bbox, outdir):

    if startdate is not None:
        startDate = datetime.datetime.strptime(startdate, "%Y-%m-%dT%H:%M:%SZ")

    if enddate is not None:
        endDate = datetime.datetime.strptime(enddate, "%Y-%m-%dT%H:%M:%SZ")

    if not hasattr(DataCollections, collection):
        print('不支持该数据集下载【%s】' %(collection))
        sys.exit(1)

    collection = getattr(DataCollections, collection)

    downloader = DownloadCentre(collection=collection,
                                username=user,
                                password=password)
    urls = downloader.searchfile(startDate=startDate, endDate=endDate)

    downloader.download(url=urls, outdir=outdir)


cli.add_command(ftp)
cli.add_command(search)
cli.add_command(download)

if __name__ == "__main__":
    cli()
