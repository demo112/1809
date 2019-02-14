# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
demo06_mask.py
ndarray对象的掩码操作
"""
import numpy as np

a = np.array([43, 70, 34, 76, 34, 57, 23, 45])
print(a)
b = a >= 60
print(b)
print(a[b])
indices = [1, 7, 6, 5, 4, 3, 2, 0]
print(a[indices])

# 输出100以内3与7的倍数
b = np.arange(100)
mask = (b % 3 == 0) & (b % 7 == 0)
print(b[mask])
