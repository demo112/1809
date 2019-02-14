# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
demo07_cs.py  测试多维数组的组合与拆分
"""
import numpy as np
a = np.arange(1, 7).reshape(2, 3)
b = np.arange(7, 13).reshape(2, 3)
print(a, b, sep='\n')
# 垂直方向组合与拆分
c = np.vstack((a, b))
print(c)
a, b = np.vsplit(c, 2)
print(a, b, sep='\n')

# 水平方向的操作：
d = np.hstack((a, b))
print(d)
a, b = np.hsplit(d, 2)
print(a, b, sep='\n')

# 深度方向的操作：
e = np.dstack((a, b))
print(e)
a, b = np.dsplit(e, 2)
print(a, b, sep='\n')

# 长度不等的数组的组合
a = np.array([1, 2, 3, 4, 5])
b = np.array([6, 7, 8, 9])
# 把b补成5个元素, 头部补0个，尾部补1个，
# 新增元素的默认值为-1
b = np.pad(
    b, pad_width=(3, 1), mode='constant',
    constant_values=-1)
print(b)

a = np.arange(1, 10)
b = np.arange(11, 20)
print(np.row_stack((a, b)))
print(np.column_stack((a, b)))
