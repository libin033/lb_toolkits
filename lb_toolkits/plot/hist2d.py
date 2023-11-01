# -*- coding:utf-8 -*-
'''
@Project     : lb_toolkits

@File        : hist2d.py

@Modify Time :  2023/2/17 15:18   

@Author      : Lee    

@Version     : 1.0   

@Description :

'''
import os
import sys
import numpy as np
import datetime

import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm, Normalize

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rc('font',family='Times New Roman')
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
plt.rcParams['font.family'] = 'sans-serif'  # 用来正常显示负号

def hist2d(outname, x, y, xmin=None, xmax=None, ymin=None, ymax=None,
           title=None, xlabel=None, ylabel=None, fontsize=16, **kwargs):

    x = np.array(x)
    y = np.array(y)

    y = y - x

    if xmin is None :
        xmin = np.nanmin(x)

    if ymin is None:
        ymin = np.nanmin(y)

    if xmax is None :
        xmax = np.nanmax(x)

    if ymax is None:
        ymax = np.nanmax(y)

    ymax = np.nanmax(np.fabs([ymin, ymax]))
    ymin = -ymax
    # 相关性
    # coef = np.corrcoef(x, y)
    def func(x, a, b):
        return a * x + b
    a, b = optimize.curve_fit(func, x, y)[0]
    y2 = a * np.array([xmin, xmax]) + b

    fig, ax = plt.subplots()

    ax.axhline(y=0, color='black', lw=0.8)

    _,_,_,hist = ax.hist2d(x, y, bins=100,  norm=Normalize(), cmap='jet', cmin=1)
    plt.colorbar(hist)

    # ax.set_xlim(vmin, vmax)
    # ax.set_ylim(vmin, vmax)

    # ax.plot(np.array([xmin, xmax]), np.array([ymin, ymax]), color='black', linestyle='-',lw=0.8)
    # ax.plot(np.array([xmin, xmax]), y2, color='red', linestyle='-',lw=0.8)

    ax.set_xlabel(xlabel, fontsize=fontsize)
    ax.set_ylabel(ylabel, fontsize=fontsize)
    ax.set_xlim(xmin*(1-0.001), xmax*(1+0.001))
    ax.set_ylim(ymin*(1-0.05), ymax*(1+0.05))

    # 标注统计参数
    ax.text(xmin+(xmax-xmin)*0.03, ymin+(ymax-ymin)*0.97, s='Count = %d' %(len(x)), fontsize=fontsize)
    ax.text(xmin+(xmax-xmin)*0.03, ymin+(ymax-ymin)*0.90, s='Bias = %.3f' %(np.nanmean(y)), fontsize=fontsize)
    ax.text(xmin+(xmax-xmin)*0.03, ymin+(ymax-ymin)*0.83, s='STD = %.3f' %(cal_std(y)), fontsize=fontsize)
    # ax.text(xmin+(xmax-xmin)*0.05, ymin+(ymax-ymin)*0.80, s='RMSE = %.3f' %(cal_rmse(x, y)), fontsize=fontsize)
    # if b > 0 :
    #     ax.text(xmin+(xmax-xmin)*0.05, ymin+(ymax-ymin)*0.8, s='Y = %.3f * X + %.3f' %(a, b), fontsize=fontsize)
    # else:
    #     ax.text(xmin+(xmax-xmin)*0.05, ymin+(ymax-ymin)*0.8, s='Y = %.3f * X - %.3f' %(a, np.fabs(b)), fontsize=fontsize)

    # now determine nice limits by hand:
    # binwidth = (xmax - xmin) / 20.
    # bins = np.arange(xmin, xmax + binwidth, binwidth)
    # n, bins, patches = ax_histx.hist(x, bins=bins, color='#1B73CC', alpha=0.5)
    #
    # binwidth = (ymax - ymin) /20.
    # bins = np.arange(ymin, ymax + binwidth, binwidth)
    # n, bins, patches = ax_histy.hist(y, bins=bins, color='#1B73CC', alpha=0.5, orientation='horizontal')

    plt.savefig(outname, dpi=200, bbox_inches='tight')

    plt.close(fig)
    print('成功绘制【%s】' %(outname))


