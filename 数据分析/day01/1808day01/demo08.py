# -*- coding: utf-8 -*-
from __future__ import unicode_literals
'''
多维数组的组合与拆分
'''
import numpy as np
a = np.arange(1, 7).reshape(2, 3)
b = np.arange(7, 13).reshape(2, 3)

# 垂直方向操作
c = np.vstack((a, b))
print('垂直合并', c)
a, b = np.vsplit(c, 2)  # 拆成2份
print('垂直拆分', a, '\n', b)

# 水平方向操作
d = np.hstack((a, b))
print('水平合并', d)
a, b = np.hsplit(d, 2)
print('水平拆分', a, '\n', b)

# 深度方向操作
e = np.dstack((a, b))
print('深度合并', e)
a, b = np.dsplit(e, 2)
print('深度拆分', a, '\n', b)

f = np.concatenate((a, b), axis=2)
print(f)

a = a.reshape(2, 3)
b = b.reshape(2, 3)
print(a, '\n', b)
# 多维数组组合与拆分的相关函数:
c = np.concatenate((a, b), axis=1)
print(c)

# 测试不同长度的数组的组合
a = np.arange(1, 7)
b = np.arange(11, 16)
c = np.pad(b,
           pad_width=(2, 2),
           mode='constant',
           constant_values=-1)
print('_________________________________________________')
print(a)
print(b)
print(c)

a = np.arange(1, 10)
b = np.arange(11, 20)
# 把a与b摞在一起成为两行
print(np.row_stack((a, b)))
# 把a与b并在一起成为两列
print(np.column_stack((a, b)))
