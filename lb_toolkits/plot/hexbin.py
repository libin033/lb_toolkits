# -*- coding:utf-8 -*-
'''
@Project     : lb_toolkits

@File        : hexbin.py

@Modify Time :  2023/2/17 15:03   

@Author      : Lee    

@Version     : 1.0   

@Description :

'''
import os
import sys
import numpy as np
import datetime

import matplotlib.pyplot as plt

def hexbin(outname, x, y, dict_text={}, xmin=None, xmax=None, ymin=None, ymax=None,
           title=None, xlabel=None, ylabel=None, fontsize=16, txtpos=0.95, space=0.05, **kwargs):

    outpath = os.path.dirname(outname)
    if not os.path.isdir(outpath):
        print('创建路径【%s】' % (outpath))
        os.makedirs(outpath)

    flag = (np.isnan(x)) | (np.isnan(y))
    x1 = x[~flag]
    y1 = y[~flag]
    if xmin == None or xmax == None :
        xmin = np.nanmin(x1)
        xmax = np.nanmax(x1)
    if ymin == None or ymax == None:
        ymin = np.nanmin(y1)
        ymax = np.nanmax(y1)

    flag = (x1 >= xmin) & (x1 <= xmax) & (y1 >= ymin) & (y1 <= ymax)
    x1 = x1[flag]
    y1 = y1[flag]


    fig, ax = plt.subplots(ncols=1, figsize=(8, 8))

    hb = ax.hexbin(x1, y1,  **kwargs)
    cb = fig.colorbar(hb, ax=ax)

    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)

    ax.set_xlabel(xlabel, fontsize=fontsize)
    ax.set_ylabel(ylabel, fontsize=fontsize)

    xmin, xmax = ax.get_xlim()
    ymin, ymax = ax.get_ylim()

    for item in dict_text :
        ax.text(xmin+(xmax-xmin)*0.05, ymin+(ymax-ymin)*txtpos, s=item, fontsize=fontsize)
        txtpos = txtpos - space

    # plt.plot([xmin, xmax], [ymin, ymax], c='w', ls='-.', lw=0.7)
    # plt.plot([xmin, xmax], [k*xmin+b, k*xmax+b], 'r-', lw=0.7)

    plt.savefig(outname, dpi=200, bbox_inches='tight')
    plt.close(fig)
    print('成功绘制【%s】' % (outname))