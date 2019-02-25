# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import sklearn.preprocessing as sp
# 只能是一维的数组
raw_samples = np.array([
    ['audi', 'ford', 'audi'],
    ['toyota', 'ford', 'bmw'],
    ['toyota', 'ford', 'audi']]).reshape(1, 9)[0]
print(raw_samples)
lbe = sp.LabelEncoder()
lbe_samples = lbe.fit_transform(raw_samples)
print(lbe_samples)
inv_samples = lbe.inverse_transform(lbe_samples)
print(inv_samples)
