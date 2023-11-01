# -*- coding:utf-8 -*-
'''
@Project     : lb_toolkits

@File        : timeseries.py

@Modify Time :  2023/2/17 15:13   

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

# 正常显示中文标签
plt.rcParams["font.family"] = "SimHei"
# 正常显示负号
plt.rcParams['axes.unicode_minus'] = False


def timeseries(outname, x, y, title=None, xlabel=None, ylabel=None, fontsize=16, **kwargs):
    '''
    绘制时间序列图

    Parameters
    ----------
    outname
    x : datetime, np.array
        时间序列集
    y : np.array
    title : str
        标题
    xlabel ： str
    ylabel : str
    fontsize : int
        设置字体大小
    kwargs

    Returns
    -------

    '''

    plt.figure(figsize=(20, 10))

    # 设置刻度方向
    plt.rcParams['xtick.direction'] = 'in'  # 将x周的刻度线方向设置向内
    plt.rcParams['ytick.direction'] = 'in'  # 将y轴的刻度方向设置向内

    # plt.plot(x, y, label=plotset[label]['label'], linewidth=1,
    #          color=plotset[label]['color'], marker=plotset[label]['marker'],
    #          markersize=5, markerfacecolor='none')

    # 绘制时间曲线
    plt.plot(x, y, **kwargs)

    plt.xticks(rotation=0)

    # 设置刻度大小
    plt.xticks(fontsize=fontsize)  # x轴刻度大小
    plt.yticks(fontsize=fontsize)  # y轴刻度大小

    # 设置轴的label
    plt.xlabel(xlabel, fontsize=fontsize)  # x轴标题字体大小
    plt.ylabel(ylabel, fontsize=fontsize)  # y轴标题字体大小

    # 设置标题
    plt.title(title, fontdict={'weight': 'normal', 'size': fontsize+2})

    # 设置图例
    plt.rcParams.update({'font.size': fontsize})  # 图例字体大小
    plt.legend(**kwargs)

    # 保持图像和内存清理
    plt.savefig(outname, dpi = 200, bbox_inches = 'tight')
    plt.close()
    print('成功绘制【%s】' %(outname))