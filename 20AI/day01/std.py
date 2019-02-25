# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import sklearn.preprocessing as sp

raw_samples = np.array([[17, 100, 4000], [20, 80, 5000], [23, 75, 5500]])

# 均值移除，消除样本数据本身的数值大小影响该维度的整体权重
std_samples = sp.scale(raw_samples)
print(std_samples)
print(std_samples.mean(axis=0))
print(std_samples.std(axis=0))

# std_samples = raw_samples.copy()
# for col in std_samples.T:
#     col_mean = col.mean()
#     col_std = col.std()
#     col -= col_mean
#     col /= col_std
# print(std_samples)
# print(std_samples.mean(axis=0))
# print(std_samples.std(axis=0))
# std_samples = sp.scale(raw_samples)
# print(std_samples)
# print(std_samples.mean(axis=0))
# print(std_samples.std(axis=0))
