# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sklearn.preprocessing as sp
import numpy as np
r = np.array(
    [[1, 3, 2],
     [7, 5, 4],
     [1, 8, 5],
     [7, 3, 9]])

# 构建编码字典，按列编码
code_tables = []
for col in r.T:
    code_table = {}
    for var in col:
        code_table[var] = None
    code_tables.append(code_table)

for code_table in code_tables:
    size = len(code_table)
    for one, key in enumerate(sorted(code_table.keys())):
        code_table[key] = np.zeros(shape=size, dtype=int)
    code_table[key][one] = 1

ohe_ss = []
for R in r:
    ohe_s = np.array([], dtype=int)
    for i, key in enumerate(R):
        ohe_s = np.hstack((ohe_s, code_tables[i][key]))
    ohe_ss.append(ohe_s)
ohe_ss = np.array(ohe_ss)
print(ohe_ss)


ohe = sp.OneHotEncoder(sparse=False, dtype=int)
t = ohe.fit_transform(r)
print(t)
