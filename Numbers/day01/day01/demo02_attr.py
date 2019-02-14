# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
demo02_attr.py 
ndarray数组对象属性操作
"""
import numpy as np

a = np.arange(1, 9)
print(a.shape, a)

# 修改数组对象的维度
a.shape = (2, 4)
print(a.shape, a, sep='\n')
a.shape = (2, 2, 2)
print(a.shape, a, sep='\n')

# 测试元素的类型相关操作
b = np.arange(10)
print(b.dtype, b)
# 把b中的每个元素当做float来看
# 返回新类型的数组
c = b.astype('float32')
print(b.dtype, b)
print(c.dtype, c)

# 测试数组元素的个数
a = np.arange(8).reshape(2, 4)
print(a)
print(a.size)
print(len(a))

# 测试数组索引操作
c = np.arange(1, 28).reshape(3, 3, 3)
print(c)
print(c[0])  # 0页
print(c[0][0])  # 0页 0行
print(c[0][0][0])  # 0页 0行 0列
print(c[0, 0, 0])  # 0页 0行 0列

for i in range(c.shape[0]):
    for j in range(c.shape[1]):
        for k in range(c.shape[2]):
            print(c[i, j, k], end=' ')
