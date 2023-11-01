# -*- coding:utf-8 -*-
'''
@Project     : lb_toolkits

@File        : time2bar.py

@Modify Time :  2023/2/17 15:33   

@Author      : Lee    

@Version     : 1.0   

@Description :

'''
import os
import sys
import numpy as np
import datetime

import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from matplotlib.dates import AutoDateLocator,AutoDateFormatter, DateFormatter

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rc('font',family='Times New Roman')
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
plt.rcParams['font.family'] = 'sans-serif'  # 用来正常显示负号

def time2bar(outname, timelist, data, title=None, xlabel=None, ylabel=None, fontsize=16, **kwargs):

    fig, ax = plt.subplots()

    timelist = np.array(timelist)
    p1 = ax.bar(timelist, data, **kwargs)

    # ax.axhline(0, color='k', linewidth=0.8)
    ax.set_xlabel(xlabel, fontsize=fontsize)
    ax.set_ylabel(ylabel, fontsize=fontsize)
    ax.set_title(title, fontsize=fontsize+2)
    ax.legend()

    fig.autofmt_xdate()
    # # 确定刻度方式
    x_locator = AutoDateLocator(minticks=5, maxticks=8, interval_multiples=True) #
    # x_format = AutoDateFormatter(x_locator, defaultfmt='%Y年%m月')
    x_format = DateFormatter('%Y年%m月')
    # x_format.scaled = {
    #     0.5: u'%Y-%m-%d\n%H:%M',
    #     1.0: u'%Y-%m-%d',
    #     30.0: u'%Y年%m月',
    #     365.0: u'%Y-%m-%d'
    # }
    ax.xaxis.set_major_formatter(x_format)
    ax.xaxis.set_major_locator(x_locator)

    # 保存图像
    plt.savefig(outname, dpi = 200, bbox_inches = 'tight')
    plt.close(fig)
    print('成功绘制【%s】' %(outname))

