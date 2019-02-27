# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
demo05_ridge.py 岭回归模型
"""
import numpy as np
import matplotlib.pyplot as mp
import sklearn.linear_model as lm
import sklearn.metrics as sm
import pickle

# 读取数据
x, y = np.loadtxt(
    '../ml_data/abnormal.txt', delimiter=',',
    usecols=(0, 1),  unpack=True)
x = x.reshape(-1, 1)  # x变为n行1列
# 创建模型->训练模型->使用模型
model = lm.LinearRegression()
model.fit(x, y)
pred_y = model.predict(x)
# 输出误差指标
print(sm.mean_absolute_error(y, pred_y))
print(sm.mean_squared_error(y, pred_y))
print(sm.median_absolute_error(y, pred_y))
print(sm.r2_score(y, pred_y))

# 把这些点画出来
mp.figure('Linear Regression', facecolor='lightgray')
mp.title('Linear Regression', fontsize=14)
mp.xlabel('x', fontsize=12)
mp.ylabel('y', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=":")
mp.scatter(x, y, c='dodgerblue', alpha=0.5,
           s=60, label='Sample Points')
mp.plot(x, pred_y, c='orangered',
        linewidth=3, label='Regression Line')

# 使用岭回归
model = lm.Ridge(150, fit_intercept=True,
                 max_iter=10000)
model.fit(x, y)
pred_y = model.predict(x)
print(sm.r2_score(y, pred_y))
mp.plot(x, pred_y, c='limegreen',
        linewidth=3, label='Ridge Regression')

mp.legend()
mp.show()
