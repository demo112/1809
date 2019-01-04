# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sklearn.linear_model as lm
import numpy as np
import matplotlib.pyplot as mp


x = np.array([
    [4, 7],
    [3.5, 8],
    [3.1, 6.2],
    [0.5, 1],
    [1, 2],
    [1.2, 1.9],
    [6, 2],
    [5.7, 1.5],
    [5.4, 2.2]

])

# print(x[1, 0])
y = np.array([0, 0, 0, 1, 1, 1, 2, 2, 2])


# 逻辑分类
model = lm.LogisticRegression(solver='liblinear', C=10)

model.fit(x, y)


l, r, h = x[:, 0].min() - 1, x[:, 0].max() + 1, 0.005

b, t, v = x[:, 1].min() - 1, x[:, 1].max() + 1, 0.005
grid_x = np.meshgrid(np.arange(l, r, h), np.arange(b, t, v))


# print((grid_x[0]))
flat_x = np.c_[grid_x[0].ravel(), grid_x[1].ravel()]

flat_y = model.predict(flat_x)
print(flat_y.shape)

# print(flat_x)
# flat_y = np.zeros(len(flat_x), dtype=int)

# flat_y[flat_x[:, 0] < flat_x[:, 1]] = 1
print(grid_x[0].shape)
grid_y = flat_y.reshape(grid_x[0].shape)


mp.figure('Simple', facecolor='lightgray')
mp.title('Simple', fontsize=12)

mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)

mp.pcolormesh(grid_x[0], grid_x[1], grid_y, cmap='gray')

mp.scatter(x[:, 0], x[:, 1], c=y, cmap='brg')
mp.show()
