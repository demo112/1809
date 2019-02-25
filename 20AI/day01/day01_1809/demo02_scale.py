# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
demo02_scale.py 均值移除（标准化）
"""
import numpy as np
import sklearn.preprocessing as sp

raw_samples = np.array([
    [17., 100., 4000.],
    [20., 80., 5000.],
    [23., 75., 5500.]])

std_samples = sp.scale(raw_samples)
print(std_samples)
# 输出每一列的均值与标准差
print(std_samples.mean(axis=0))
print(std_samples.std(axis=0))
