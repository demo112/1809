# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
mormalize.py  归一化
"""
import numpy as np
import sklearn.preprocessing as sp

raw_samples = np.array([
    [17., 100., 4000.],
    [20., 80., 5000.],
    [23., 75., 5500.]])

print(raw_samples)
# 归一化处理
nor_samps = sp.normalize(raw_samples, norm='l1')
print(nor_samps)
print(abs(nor_samps).sum(axis=1))

# 自己算：
nor_samps = raw_samples.copy()
for row in nor_samps:
    row /= abs(row).sum()
print(nor_samps)
print(abs(nor_samps).sum(axis=1))
