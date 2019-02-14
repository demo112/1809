# -*- coding: utf-8 -*-
from __future__ import unicode_literals
'''
测试ndarray数组的属性
'''
import numpy as np

a = np.array([[1 + 1j, 2 + 4j, 3 + 7j],
              [4 + 2j, 5 + 5j, 6 + 8j],
              [7 + 3j, 8 + 6j, 9 + 9j]])

# print('a.dtype:', a.dtype,
#       '; a.ndim:', a.ndim)
# print(a.real)
# print(a.imag)
# print(a.imag.T)
# c = a[:, :2]
# print(c)
# print(c.T)
# # 测试ndarray数组的扁平迭代器
# print([e for e in a.flat])


### numpy数组的其他属性

print('1', '维度', '\n', a.shape)
print('2', '元素类型', '\n', a.dtype)
print('3', '数组元素个数', '\n', a.size)
print('4', '维数', '\n', a.ndim)
print('5', '元素字节数', '\n', a.itemsize)
print('6', '数组总字节数', '\n', a.nbytes)
print('7', '复数数组的实部', '\n', a.real)
print('8', '复数数组的虚部', '\n', a.imag)
print('9', '数组对象的转置视图', '\n', a.T)
print('10', '返回数组的扁平迭代器', '\n', a.flat)
print('11', '转换为列表', '\n', a.tolist())
