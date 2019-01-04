# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sklearn.preprocessing as sp
import numpy as np

R = np.array(['audi', 'fort', 'audi', 'bmw',
              'toyoto', 'fort', 'toyoto', 'audi'])

lbe = sp.LabelEncoder()
lbe_s = lbe.fit_transform(R)
print(lbe_s)

r = lbe.inverse_transform(lbe_s)
print(r)
