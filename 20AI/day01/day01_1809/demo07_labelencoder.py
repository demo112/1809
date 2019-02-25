# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
labelencoder.py: 标签编码
"""
import numpy as np
import sklearn.preprocessing as sp

raw_samples = np.array([
    'audi', 'ford', 'audi', 'toyota',
    'ford', 'bmw', 'toyota', 'byd',
    'audi'])
# 执行标签编码
lbe = sp.LabelEncoder()
lbe_samples = lbe.fit_transform(raw_samples)
print(lbe_samples)

inv_sampls = lbe.inverse_transform(lbe_samples)
print(inv_sampls)
