# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sklearn.preprocessing as sp
import numpy as np
r = np.array([
    [3, -1.5, 2, -5.4],
    [0, 4, -0.3, 2.1],
    [1, 3.3, -1.9, -4.3]
])
print(np.abs(r).sum(axis=1))
s = r.copy()

for row in s:
    row /= np.abs(row).sum()
    print(row)
print(s)
print(np.abs(s).sum(axis=1))
nor_mal = sp.normalize(r, norm='l1')
print(np.abs(nor_mal).sum(axis=1))
