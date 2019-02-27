# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
demo06_poly.py 多项式回归 single.txt
"""
import numpy as np
import matplotlib.pyplot as mp
import sklearn.linear_model as lm
import sklearn.preprocessing as sp
import sklearn.metrics as sm
import sklearn.pipeline as pl

# 读取数据
x, y = np.loadtxt(
    '../ml_data/single.txt', delimiter=',',
    usecols=(0, 1),  unpack=True)
x = x.reshape(-1, 1)  # x变为n行1列

# 创建管线
model = pl.make_pipeline(
    sp.PolynomialFeatures(6),  # 多项式特征扩展
    lm.LinearRegression()  # 线性回归器
)
model.fit(x, y)
pred_y = model.predict(x)
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
# 绘制多项式曲线
x = np.linspace(x.min(), x.max(), 1000)
x = x.reshape(-1, 1)
y = model.predict(x)
mp.plot(x, y, color='orangered',
        linewidth=2, label='PolyFit Line')

mp.legend()
mp.show()
