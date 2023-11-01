# -*- coding:utf-8 -*-
'''
@Project     : lb_toolkits

@File        : hist.py

@Modify Time :  2023/2/17 15:17   

@Author      : Lee    

@Version     : 1.0   

@Description :

'''
import os
import sys
import numpy as np
import datetime

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rc('font',family='Times New Roman')
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
plt.rcParams['font.family'] = 'sans-serif'  # 用来正常显示负号

def plotHist(outname, x, y, threshold=5, title=None, xlabel=None, ylabel=None, fontsize=16, **kwargs):
    x = np.array(x)
    y = np.array(y)
    fig = plt.figure(figsize=(8, 8)) #,tight_layout=True)
    ax = fig.add_subplot(111)
    # ax = fig.sub_(rect_scatter, facecolor="#EAEAF2")
    # ax_histx = fig.add_axes(rect_histx, sharex=ax, facecolor="#EAEAF2")
    # ax_histy = fig.add_axes(rect_histy, sharey=ax, facecolor="#EAEAF2")
    #
    # ax.grid(color="#FFFFFF")
    # ax_histx.grid(color="#FFFFFF")
    # ax_histy.grid(color="#FFFFFF")

    # ax.set_xlim(vmin, vmax)
    # ax.set_ylim(vmin, vmax)

    # def set_ax(ax1):
    #     ax1.spines['top'].set_color('white')
    #     ax1.spines['left'].set_color('white')
    #     ax1.spines['right'].set_color('white')
    #     ax1.spines['bottom'].set_color('white')
    #     ax1.tick_params(axis='both',length=0, labelsize=fontsize)
    #     # ax.spines['left'].set_visible(False)
    # set_ax(ax)

    diff = y - x

    flag = np.fabs(diff) <= threshold
    diff = diff[flag]

    # now determine nice limits by hand:
    binwidth = threshold * 2 / 100.
    bins = np.arange(-threshold, threshold + binwidth, binwidth)
    n, bins, patches = ax.hist(diff, bins=bins, color='#1B73CC', alpha=0.8, align='left')

    xmin, xmax = ax.get_xlim()
    ymin, ymax = ax.get_ylim()

    ax.text(xmin+(xmax-xmin)*0.05, ymin+(ymax-ymin)*0.95, s='Count = %d' %(len(x)), fontsize=fontsize)
    ax.text(xmin+(xmax-xmin)*0.05, ymin+(ymax-ymin)*0.90, s='Bias = %.3f' %(np.nanmean(diff)), fontsize=fontsize)
    ax.text(xmin+(xmax-xmin)*0.05, ymin+(ymax-ymin)*0.85, s='R = %.3f' %(cal_R(x, y)), fontsize=fontsize)
    ax.text(xmin+(xmax-xmin)*0.05, ymin+(ymax-ymin)*0.80, s='STD = %.3f' %(cal_std(diff)), fontsize=fontsize)
    ax.text(xmin+(xmax-xmin)*0.05, ymin+(ymax-ymin)*0.75, s='RMSE = %.3f' %(cal_rmse(x, y)), fontsize=fontsize)

    ax.set_xlabel('偏差(%s-%s)（ppm）' %(satid, xlabel), fontsize=fontsize)
    ax.set_ylabel('频次', fontsize=fontsize)

    xmajorLocator = MultipleLocator(1) # 将x主刻度标签设置为10的倍数
    xmajorFormatter = FormatStrFormatter('%.0f') # 设置x轴标签文本的格式
    xminorLocator   = MultipleLocator(0.5) # 将x轴次刻度标签设置为5的倍数
    ymajorLocator = MultipleLocator(0.5) # 将y轴主刻度标签设置为0.5的倍数
    ymajorFormatter = FormatStrFormatter('%.1f') # 设置y轴标签文本的格式
    yminorLocator   = MultipleLocator(0.05) # 将此y轴次刻度标签设置为0.1的倍数

    ax.xaxis.set_major_locator(xmajorLocator)  # 设置x轴主刻度
    ax.xaxis.set_major_formatter(xmajorFormatter)  # 设置x轴标签文本格式
    ax.xaxis.set_minor_locator(xminorLocator)  # 设置x轴次刻度
    # ax.yaxis.set_minor_locator(yminorLocator)  # 设置x轴次刻度

    # no labels
    ax.tick_params(axis="x", labelbottom=True, top=True, direction='in', labelsize=fontsize)
    ax.tick_params(axis="x", labelbottom=True, top=True, direction='in', labelsize=fontsize, which="minor")
    ax.tick_params(axis="y", labelleft=True, right=True, direction='in', labelsize=fontsize)
    ax.tick_params(axis="y", labelleft=True, right=True, direction='in', labelsize=fontsize, which="minor")

    plt.rcParams['xtick.direction'] = 'in'  # 将x周的刻度线方向设置向内
    plt.rcParams['ytick.direction'] = 'in'  # 将y轴的刻度方向设置向内
    # plt.tick_params(axis="x", labelleft=False, labelbottom=True, labeltop=False)
    # plt.tick_params(axis="y", labelleft=False, labelbottom=False)

    plt.savefig(outname, dpi=200, bbox_inches='tight')

    plt.close(fig)
    print('成功绘制【%s】' %(outname))


