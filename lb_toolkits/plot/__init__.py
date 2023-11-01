# -*- coding:utf-8 -*-
'''
@Project     : lb_toolkits

@File        : __init__.py.py

@Modify Time :  2023/2/17 15:02   

@Author      : Lee    

@Version     : 1.0   

@Description :

'''
import os
import sys
import numpy as np
import datetime


from scipy import optimize

def cal_std(x) :
    return np.nanstd(x)

def cal_rmse(x, y):

    diff = (x - y)**2

    return np.nanmean(diff)

def cal_R(x, y) :
    # 相关性
    coef = np.corrcoef(x, y)

    return coef[0, 1]

def cal_ax_b(x, y):
    def func(x, a, b):
        return a * x + b
    a, b = optimize.curve_fit(func, x, y)[0]

    return a, b

    # count = len(x1)
    # bias = np.nanmean(y1 - x1)
    #
    # k, b = np.polyfit(x1, y1, deg=1)
    # # k, b = curve_fit(func, x, y)[0]
    # stdd = np.nanstd(x1 - y1)
    # rmse = np.sqrt(np.nanmean((x1 - y1) ** 2))
    # cof = np.corrcoef(x1, y1)[0, 1]

'''

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rc('font',family='Times New Roman')
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
plt.rcParams['font.family'] = 'sans-serif'  # 用来正常显示负号

（1）导入外源字体
    font = FontProperties(fname=os.path.join(os.getcwd(), 'resource', 'simsun.ttf'))

（2）加载系统字体
    plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
    plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

（3）设置字体
fontdict={'family': 'Times New Roman', 'size': 16}

fontproperties = 'Times New Roman', size = 14


plt.rc('font',family='Times New Roman')

**************************************************************************
设置刻度方向和轴显示
ax.tick_params(axis="x", labelbottom=True, top=True, direction='in', labelsize=fontsize)
ax.tick_params(axis="x", labelbottom=True, top=True, direction='in', labelsize=fontsize, which="minor")
ax.tick_params(axis="y", labelleft=True, right=True, direction='in', labelsize=fontsize)
ax.tick_params(axis="y", labelleft=True, right=True, direction='in', labelsize=fontsize, which="minor")

**************************************************************************
重新设置刻度label
ylabels = np.array(np.linspace(bottom, top, 7) )
ax1.set_yticks(ticks=(ylabels - bottom) / (top - bottom) * 100)
ax1.set_yticklabels(['%.1f' %(ylabel) for ylabel in ylabels] )

**************************************************************************
设置log轴
ax.set_yscale('log')  # 设置轴为Log轴
ax.invert_yaxis()   # 将值的大小颠倒

**************************************************************************
设置网格
ax.xaxis.set_major_locator(plt.MultipleLocator(1.0))#设置x主坐标间隔 1
#ax.xaxis.set_minor_locator(plt.MultipleLocator(0.1))#设置x从坐标间隔 0.1
ax.yaxis.set_major_locator(plt.MultipleLocator(1.0))#设置y主坐标间隔 1
#ax.yaxis.set_minor_locator(plt.MultipleLocator(0.1))#设置y从坐标间隔 0.1
ax.grid(which='major', axis='x', linewidth=1, linestyle='-', color='w')#由每个x主坐标出发对x主坐标画垂直于x轴的线段
#ax.grid(which='minor', axis='x', linewidth=0.25, linestyle='-', color='0.75')#由每个x主坐标出发对x主坐标画垂直于x轴的线段
ax.grid(which='major', axis='y', linewidth=1, linestyle='-', color='w')
#ax.grid(which='minor', axis='y', linewidth=0.25, linestyle='-', color='0.75')

**************************************************************************
设置标注
plt.annotate(str, xy=(ix+0.3, iy+0.3) )

**************************************************************************
# 保存图像
plt.savefig(outname, dpi = 200, bbox_inches = 'tight')
plt.close(fig)
print('成功绘制【%s】' %(outname))

**************************************************************************
**************************************************************************
**************************************************************************
**************************************************************************


'''


