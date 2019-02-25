# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import sklearn.preprocessing as sp
raw_samples = np\
    .array([[17, 100, 4000], [20, 80, 5000], [23, 75, 5500]])\
    .astype('float64')

print(raw_samples)
nor_samples = raw_samples.copy()
for row in nor_samples.T:
    # 横竖转至
    row /= abs(row).sum()
print(nor_samples)
print(abs(nor_samples).sum(axis=0))
print("归一化预处理")
# 归一化预处理
nor_samples = sp.normalize(
    raw_samples, norm='l1', axis=0)
print(nor_samples)
print(abs(nor_samples).sum(axis=0))
