# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sklearn.preprocessing as sp
import numpy as np
r = np.array([
    [3, -1.5, 2, -5.4],
    [0, 4, -0.3, 2.1],
    [1, 3.3, -1.9, -4.3]
])

bin_s = r.copy()

bin_s[bin_s <= 1.4] = 0
bin_s[bin_s > 1.4] = 1
print(bin_s)

bin_t = sp.Binarizer(threshold=6)
t = bin_t.transform(r)
print(t)
