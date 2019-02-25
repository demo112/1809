# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
binarizer.py  二值化
"""
import numpy as np
import sklearn.preprocessing as sp

raw_samples = np.array([
    [17., 100., 4000.],
    [20., 80., 5000.],
    [23., 75., 5500.]])

print(raw_samples)
# 二值化处理
bin = sp.Binarizer(threshold=80)
bin_samples = bin.transform(raw_samples)
print(bin_samples)
# 自己做：
bin_samples = raw_samples.copy()
bin_samples[bin_samples <= 80] = 0
bin_samples[bin_samples > 80] = 1
print(bin_samples)
