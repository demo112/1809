# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import sklearn.preprocessing as sp
raw_samples = np.array([
    [3, -1.5, 2, -5.4],
    [0, 4, -0.3, 2.1],
    [1, 3.3, -1.9, -4.3]
])

print('min', raw_samples.min(axis=0))
print('max', raw_samples.max(axis=0))

mms_samples = raw_samples.copy()
for col in mms_samples.T:
    col -= col.min()
    col /= col.ptp()
    print(col)
print(mms_samples)
print('min', mms_samples.min(axis=0))
print('max', mms_samples.max(axis=0))
print('--------------')

mms = sp.MinMaxScaler(feature_range=(0, 1))
print(mms.fit_transform(raw_samples))
