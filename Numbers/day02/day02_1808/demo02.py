# -*- coding: utf-8 -*-
from __future__ import unicode_literals
'''
mp的窗口操作
'''
import numpy as np
import matplotlib.pyplot as mp


mp.figure('Figure1', figsize=(4, 3),
          facecolor='lightgray')
mp.figure('Figure2', figsize=(6, 5),
          facecolor='yellowgreen')

mp.figure('Figure1')
mp.title('Figure1', fontsize=18)
mp.xlabel('Date', fontsize=14)
mp.ylabel('Price', fontsize=14)
mp.tick_params(labelsize=8)
mp.grid(linestyle=':')
mp.tight_layout()

mp.figure('Figure2')
mp.xlabel('Date——2', fontsize=14)
mp.ylabel('Price——2', fontsize=14)
mp.tick_params(labelsize=8)
mp.grid(linestyle=':')
# mp.tight_layout()


mp.show()
