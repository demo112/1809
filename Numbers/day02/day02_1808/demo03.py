# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp
from Numbers.day02.day02_1808.demo01 import Simple
from Numbers.day02.day02_1808.demo01_sin import Sanjiao

'''
绘制9宫格子图
'''
# 生成图片对象
mp.figure('Sub Layout', facecolor='gray')
# 生成子图
for i in range(1, 10):
    mp.subplot(3, 3, i)
    mp.text(0.5, 0.5, i, ha='center',
            va='center', size=36, alpha=0.8)
    mp.xticks([])
    mp.yticks([])
    mp.tight_layout()


# todo 处理变量冲突
mp.subplot(331)
simple = Simple()
simple.simple1()

mp.subplot(332)
sanjiao = Sanjiao()
sanjiao.sanjiao1()
mp.tight_layout()


mp.show()
