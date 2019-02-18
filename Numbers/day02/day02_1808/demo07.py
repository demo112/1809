# -*- coding: utf-8 -*-
from __future__ import unicode_literals

'''
绘制刻度网格线
'''

import numpy as np
import matplotlib.pyplot as mp

y_point_list = [1, 10, 100, 1000, 100, 10, 1]

mp.figure('GridLine', facecolor='lightgray')

mp.subplot(2, 1, 1)
mp.title('GridLine', fontsize=18)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
ax = mp.gca()
ax.xaxis.set_major_locator(mp.MultipleLocator(1.0))
ax.xaxis.set_minor_locator(mp.MultipleLocator(0.333))
ax.yaxis.set_minor_locator(mp.MultipleLocator(250))
ax.yaxis.set_minor_locator(mp.MultipleLocator(50))
ax.grid(which='major', axis='both', linewidth=0.75, color='orange')
ax.grid(which='minor', axis='both', linewidth=0.25, color='orange', alpha=0.5)
mp.plot(y_point_list, 'o--', c='dodgerblue', label='diandian')
mp.legend()
mp.tight_layout()


mp.subplot(2, 1, 2)
mp.title('GridLine', fontsize=18)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
ax = mp.gca()
ax.xaxis.set_major_locator(mp.MultipleLocator())
ax.xaxis.set_minor_locator(mp.MultipleLocator(0.1))
ax.grid(which='major', axis='both', linewidth=0.75, color='orange')
ax.grid(which='minor', axis='both', linewidth=0.25, color='orange')
mp.semilogx(y_point_list, 'o-.', c='dodgerblue', label='diandian')
mp.legend()
mp.tight_layout()

mp.show()
