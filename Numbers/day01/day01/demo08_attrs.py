# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
demo08_attrs.py 测试常用属性
"""
import numpy as np

a = np.array([
    [1 + 1j, 2 + 4j, 3 + 7j],
    [4 + 2j, 5 + 5j, 6 + 8j],
    [7 + 3j, 8 + 6j, 9 + 9j]])
print(a.ndim)
print(a.size)
print(a.itemsize)
print(a.nbytes)
print(a.real, a.imag, sep='\n')
print(a.T)
for i in a.flat:
    print(i)
print(type(a.tolist()))
