# -*- coding:utf-8 -*-
'''
@Project     : lb_toolkits

@File        : imshow.py

@Modify Time :  2023/2/17 16:55   

@Author      : Lee    

@Version     : 1.0   

@Description :

'''
import os
import sys
import numpy as np
import datetime

import matplotlib
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rc('font',family='Times New Roman')
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
plt.rcParams['font.family'] = 'sans-serif'  # 用来正常显示负号


def imshow(outname, data, title=None, xlabel=None, ylabel=None, fontsize=16, **kwargs):

    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111)

    ax.set_title(title, fontsize=fontsize+2)
    Pixel, Level = data.shape
    Level = Pixel

    ffim = ax.imshow(data, extent=(0, Pixel, 0, Level), interpolation='nearest', **kwargs)

    ax2 = fig.add_axes([0.95, .12, 0.03, .75])
    cb2 = matplotlib.colorbar.ColorbarBase(ax2,
                                           # boundaries=[-10] + bounds + [10],
                                           # extend='both', # max, min, both
                                           # Make the length of each extension
                                           # the same as the length of the
                                           # interior colors:
                                           # extendfrac='auto',
                                           # ticks=bounds,
                                           # ticklocation='left',
                                           spacing='uniform',
                                           orientation='vertical', **kwargs)

    plt.savefig(outname, dpi=200, bbox_inches='tight')

    plt.close(fig)
    print('成功绘制【%s】' %(outname))
