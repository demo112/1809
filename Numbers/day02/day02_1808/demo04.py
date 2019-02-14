# -*- coding: utf-8 -*-
from __future__ import unicode_literals
'''
测试网格子图布局
'''
import matplotlib.pyplot as mp
import matplotlib.gridspec as mg


def default(i):
    """
    :param i:
    """
    mp.text(0.5, 0.5, i, va='center', ha='center', size=36)
    mp.xticks([])
    mp.yticks([])
    mp.tight_layout()


mp.figure('Gird layout', facecolor='gray')
gs = mg.GridSpec(3, 3)

mp.subplot(gs[0, :2])
default(1)

mp.subplot(gs[:2, 2])
default(2)

mp.subplot(gs[1, 1])
default(3)

mp.subplot(gs[1:, 0])
default(4)

mp.subplot(gs[2, 1:])
default(5)

mp.show()
