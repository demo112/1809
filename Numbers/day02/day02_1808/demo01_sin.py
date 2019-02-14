# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp

class Sanjiao(object):
    def sanjiao1(self):
        m = np.linspace(-np.pi, np.pi, 10000)
        sinm = np.sin(m)
        cosm = np.cos(m) / 2
        tanm = np.tan(m)
        cotm = 1 / tanm
        mp.plot(m, sinm, linestyle='-.', linewidth=2, color='dodgerblue', alpha=0.8, label=r'$y=sin(x)$')
        mp.plot(m, cosm, linestyle='--', linewidth=2, color='r', alpha=1, label=r'$y=\frac{1}{2}cos(x)$')
        # mp.plot(m, tanm)
        # mp.plot(m, cotm)
        mp.legend(loc='best')


        # 设置坐标刻度
        x_var_list = [-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi]
        x_text_list = [r'${\pi}$',
                       r'$-\frac{\pi}{2}$',
                       '0',
                       r'$\frac{\pi}{2}$',
                       r'${\pi}$',
                       ]

        mp.xticks(x_var_list, x_text_list)
        y_var_list = [-1, -0.5, 0, 0.5, 1]
        mp.yticks(y_var_list)
        # 移动坐标轴
        ax = mp.gca()
        ax.spines['top'].set_color('none')
        ax.spines['right'].set_color('none')
        ax_left = ax.spines['left']
        ax_bottom = ax.spines['bottom']
        ax_left.set_position(('data', 0))
        ax_bottom.set_position(('data', 0))

        # 设置可视范围
        mp.xlim(0, np.pi)
        mp.ylim(0, 1)

        # 绘制特殊点
        xpoints = [np.pi / 2, np.pi / 2]
        ypoints = [1, 0]
        mp.scatter(xpoints,
                   ypoints,
                   marker='s',
                   s =60,
                   edgecolors='green',
                   facecolor='red',
                   zorder=10)

        # 添加备注文本
        mp.annotate(r'$abc$',  # 备注内容
                    xycoords='data',  # 备注目标点使用的坐标系
                    xy=[np.pi / 2, 0],  # 备注目标点的坐标
                    textcoords='offset points',  # 备注文本使用的坐标系
                    xytext=(70, 0),  # 备注文本的坐标
                    fontsize=20,  # 备注文本字体大小
                    arrowprops=dict(
                        arrowstyle='-|>',
                        connectionstyle='angle3')  # 指示箭头的属性
                    )
        mp.annotate(r'$abc$',  # 备注内容
                    xycoords='data',  # 备注目标点使用的坐标系
                    xy=[np.pi / 2, 1],  # 备注目标点的坐标
                    textcoords='offset points',  # 备注文本使用的坐标系
                    xytext=(-60, -30),  # 备注文本的坐标
                    fontsize=20,  # 备注文本字体大小
                    arrowprops=dict(
                        arrowstyle='-|>',
                        connectionstyle='angle3')  # 指示箭头的属性
                    )
        mp.show()

if __name__ == '__main__':
    sanjiao = Sanjiao()
    sanjiao.sanjiao1()
