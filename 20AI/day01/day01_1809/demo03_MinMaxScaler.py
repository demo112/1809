# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
demo03_MinMaxScaler.py 范围缩放
"""
import numpy as np
import sklearn.preprocessing as sp

raw_samples = np.array([
    [17., 100., 4000.],
    [20., 80., 5000.],
    [23., 75., 5500.]])

print(raw_samples)
# 执行范围缩放
mms = sp.MinMaxScaler(feature_range=(0, 1))
result = mms.fit_transform(raw_samples)
print(result)

# 使用解方程的方式求解k与b，实现线性范围缩放
mms_samples = raw_samples.copy()
for col in mms_samples.T:
    col_min = col.min()
    col_max = col.max()
    a = np.array([[col_min, 1],
                  [col_max, 1]])
    b = np.array([0, 1])
    x = np.linalg.solve(a, b)
    # 计算 kx + b
    col *= x[0]
    col += x[1]
print(mms_samples)
