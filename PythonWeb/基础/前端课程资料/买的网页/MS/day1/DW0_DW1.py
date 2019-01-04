# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sklearn.preprocessing as sp
import numpy as np
import matplotlib.pyplot as mp
from mpl_toolkits.mplot3d import axes3d
# 批量梯度下降
train_x = np.array([0.5, 0.6, 0.8, 1.1, 1.4])
train_y = np.array([5.0, 5.5, 6.0, 6.8, 7.0])

n_epoches = 1000
lrate = 0.01
epoches, losses = [], []
w0, w1 = [1], [1]
for epoch in range(1, n_epoches + 1):
    epoches.append(epoch)
    losses.append(((train_y - (w0[-1] + w1[-1] * train_x))**2).sum() / 2)
    print('{:4} w0={:.8f},w1={:.8f},loss={:.8f}'.format(
        epoches[-1], w0[-1], w1[-1], losses[-1]))

    # 偏微分计算
    d0 = -(train_y - (w0[-1] + w1[-1] * train_x)).sum()
    d1 = -((train_y - (w0[-1] + w1[-1] * train_x)) * train_x).sum()

    w0.append(w0[-1] - lrate * d0)
    w1.append(w1[-1] - lrate * d1)
w0 = np.array(w0[:-1])
w1 = np.array(w1[:-1])

sorted_indices = train_x.argsort()
test_x = train_x[sorted_indices]
test_y = train_y[sorted_indices]
print(test_y)
pred_test_y = w0[-1] + w1[-1] * test_x

grid_w0, grid_w1 = np.meshgrid(
    np.linspace(0, 9, 500),
    np.linspace(0, 3.5, 500))

flat_w0, flat_w1 = grid_w0.ravel(), grid_w1.ravel()
flat_loss = ((flat_w0 + np.outer(train_x, flat_w1) -
              train_y.reshape(-1, 1))**2).sum(axis=0) / 2

grid_loss = flat_loss.reshape(grid_w0.shape)


mp.figure("Linear Regression")

mp.grid(linestyle=':')
mp.scatter(train_x, train_y, marker='s', c='r', s=80)

mp.scatter(test_x, pred_test_y, c='orange', s=80)
mp.plot(test_x, pred_test_y, c='green', linewidth=1)
for x, y, pred_y in zip(test_x, test_y, pred_test_y):
    mp.plot([x, x], [y, pred_y])


mp.figure('Training', facecolor='lightgray')
mp.subplot(311)
mp.title('Training')
mp.gca().xaxis.set_major_locator(mp.MultipleLocator(100))
mp.plot(epoches, w0, c='blue', label=w0)

mp.subplot(312)
mp.gca().xaxis.set_major_locator(mp.MultipleLocator(100))
mp.
mp.plot(epoches, w1, c='blue', label=w1)

mp.legend()

mp.tight_layout()

mp.figure("3D")
ax = mp.gca(projection='3d')
ax.plot_surface(grid_w0, grid_w1, grid_loss, rstride=10, cmap='jet')

ax.plot(w0, w1, losses)

mp.figure("Batch")
mp.contourf(grid_w0, grid_w1, grid_loss, 1000, cmap='jet')
mp.plot(w0, w1)


mp.show()
