# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import numpy as np

array = np.array([1, 2, 3, 4, 5])
print(array)
array = array + 10
print(type(array))

print(np.arange(0, 10, 1))
print(np.arange(0, 10))
print(np.arange(10))

a = np.zeros(10, dtype='int32')
print(a.dtype, a)
a = np.ones(10, dtype='float32')
print(a.dtype, a)
a = np.ones(5, dtype='bool')
print(a.dtype, a)
