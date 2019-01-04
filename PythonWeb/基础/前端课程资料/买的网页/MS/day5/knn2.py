# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sklearn.neighbors as sn
import numpy as np
import matplotlib.pyplot as mp

train_x = 10 * np.random.rand(100, 1) - 5
train_y = np.sinc(train_x).ravel()
train_y += 0.2 * (0.5 - np.random.rand(train_y.size))

# KNN分类器模型回归
model = sn.KNeighborsRegressor(n_neighbors=10, weights='distance')
# 惰性学习，什么都没做
model.fit(train_x, train_y)

test_x = np.linspace(-5, 5, 10000).reshape(-1, 1)
test_y = np.sinc(test_x).ravel()

pred_test_y = model.predict(test_x)

# 绘制训练样本和分类边界
mp.figure("KNN", facecolor='lightgray')
mp.xlabel('x')
mp.ylabel('y')
mp.tick_params(labelsize=20)
mp.grid(linestyle=':')
mp.scatter(train_x, train_y, c='green')
mp.plot(test_x, test_y, c='orange')
mp.plot(test_x, pred_test_y, c=' red')
mp.show()
