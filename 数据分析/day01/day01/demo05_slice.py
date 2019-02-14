# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
demo05_slice.py
测试切片操作
"""
import numpy as np
a = np.arange(1, 10)
print(a)
print(a[:3])
print(a[3:6])
print(a[6:])
print(a[::-1])
print(a[:-4:-1])
print(a[-4:-7:-1])
print(a[-7::-1])
print(a[::])
print(a[::3])
print(a[1::3])
print(a[2::3])

a = a.reshape(3, 3)
print(a)
print(a[:2, :2])
print(a[:, 2])  # 所有行的最后一列
