# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import sklearn.linear_model as lm
import matplotlib.pyplot as mp
x, y = [], []
with open('abnormal.txt', 'r') as f:
    for line in f.readlines():
        data = [float(substr) for substr
                in line.split(',')]
        x.append(data[:-1])
        y.append(data[-1])
x = np.array(x)
y = np.array(y)
model1 = lm.LinearRegression()
model1.fit(x, y)
pred_y1 = model1.predict(x)
model2 = lm.Ridge(300, fit_intercept=True, max_iter=10000)
model2.fit(x, y)
pred_y2 = model2.predict(x)
mp.figure('Linear & Ridge Regression',
          facecolor='lightgray')
mp.title('Linear & Ridge Regression', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.scatter(x, y, c='dodgerblue', alpha=0.75, s=60,
           label='Sample')
sorted_indices = x.ravel().argsort()
mp.plot(x[sorted_indices], pred_y1[sorted_indices],
        c='orangered', label='Linear')
mp.plot(x[sorted_indices], pred_y2[sorted_indices],
        c='limegreen', label='Ridge')
mp.legend()
mp.show()
