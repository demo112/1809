# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
demo04_shape.py
测试ndaray数组对象的维度操作
"""
import numpy as np

a = np.arange(1, 9)
print(a)
a = a.reshape(2, 4)
print(a)
b = a.reshape(2, 2, 2)
print(b)
a[0, 0] = 999
print(a)
print(b)
b = b.ravel()
print(b)

# 复制变维 数据独立
c = a.flatten()
print(a)
print(c)
c[0] = 1000
print(a)
print(c)

# 就地变维
c.shape = (2, 4)
print(c)
c.resize(2, 2, 2)
print(c)
