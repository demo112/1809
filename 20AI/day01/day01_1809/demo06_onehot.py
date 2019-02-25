# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
onehot.py  独热编码
"""
import numpy as np
import sklearn.preprocessing as sp

raw_samples = np.array([
    [17., 100., 4000.],
    [20., 80., 5000.],
    [23., 75., 5500.]])

print(raw_samples)
# 独热编码
ohe = sp.OneHotEncoder(sparse=False, dtype=int)
ohe_samples = ohe.fit_transform(raw_samples)
print(ohe_samples)
# 获取ohe的编码字典
ohe_dict = ohe.fit(raw_samples)
ohe_samples = ohe_dict.transform(raw_samples)
print(ohe_samples)
