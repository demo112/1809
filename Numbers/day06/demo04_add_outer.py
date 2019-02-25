# -*- coding: utf-8 -*-
from __future__ import unicode_literals
'''
测试加法的通用函数
'''
import numpy as np

a = np.arange(1, 7)
print(a)
print(np.add(a, a))
print(np.add.reduce(a))
print(np.add.accumulate(a))
print(np.outer([10, 20, 30], a))
print(np.add.outer([10, 20, 30], a))


a = np.array([20, 20, -20, -20])
b = np.array([3, -3, 6, -6])
print(a)
print(b)
# 开始测试
print(np.true_divide(a, b))
print(np.divide(a, b))

print(np.floor_divide(a, b))
print(np.ceil(a / b))
print(np.trunc(a / b))
print(np.round(a / b))