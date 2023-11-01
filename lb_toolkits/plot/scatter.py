# -*- coding:utf-8 -*-
'''
@Project     : lb_toolkits

@File        : scatter.py

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
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rc('font',family='Times New Roman')
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
plt.rcParams['font.family'] = 'sans-serif'  # 用来正常显示负号

def scatter(outname, x, y, dict_text={}, vmin=None, vmax=None, title=None,
            xlabel=None, ylabel=None, fontsize=16, txtpos=0.95, space=0.05, **kwargs):
    ''' 绘制散点图 '''

    x = np.array(x)
    y = np.array(y)

    # 获取数据的范围
    if vmin is None :
        vmin = np.nanmin([x, y])*(1-0.001)

    if vmax is None :
        vmax = np.nanmax([x, y])*(1+0.001)

    fig, ax = plt.subplots()

    # 绘制散点以及绘制拟合线
    ax.scatter(x, y, **kwargs)
    # ax.plot(np.array([vmin, vmax]), np.array([vmin, vmax]), color='black', linestyle='-',lw=0.8)
    # ax.plot(np.array([vmin, vmax]), y2, color='red', linestyle='-',lw=0.8)

    # 设置轴的label
    ax.set_xlabel(xlabel, fontsize=fontsize)
    ax.set_ylabel(ylabel, fontsize=fontsize)

    # 设置轴的范围
    ax.set_xlim(vmin, vmax)
    ax.set_ylim(vmin, vmax)

    # 获取轴的范围
    xmin, xmax = ax.get_xlim()
    ymin, ymax = ax.get_ylim()

    # 设置text
    for item in dict_text :
        ax.text(xmin+(xmax-xmin)*0.05, ymin+(ymax-ymin)*txtpos, s=item, fontsize=fontsize)
        txtpos = txtpos - space

    # 设置标题
    ax.set_title(title, fontsize=fontsize+2)

    # 输出图像
    plt.savefig(outname, dpi=200, bbox_inches='tight')

    # 清理图像内存
    plt.close(fig)
    print('成功绘制【%s】' %(outname))


