# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
demo01_reg.py  线性回归
"""
import numpy as np
import matplotlib.pyplot as mp
import mpl_toolkits.mplot3d as axes3d

train_x = np.array([0.5, 0.6, 0.8, 1.1, 1.4])
train_y = np.array([5.0, 5.5, 6.0, 6.8, 7.0])
test_x = np.array([0.45, 0.55, 1.0, 1.3, 1.5])
test_y = np.array([4.8, 5.3, 6.4, 6.9, 7.3])
# 基于梯度下降理论，完成线性回归，求w0与w1
times = 1000  # 梯度下降次数
lrate = 0.01  # 每次梯度下降参数的变化率
epoches = []  # 记录每次梯度下降的索引
w0, w1, losses = [1], [1], []  # 参数
# 做1000次梯度下降
for i in range(1, times + 1):
    epoches.append(i)
    loss = ((w0[-1] + w1[-1] * train_x
             - train_y)**2).sum() / 2
    losses.append(loss)
    # 使用偏导数取出w0与w1梯度下降值
    d0 = ((w0[-1] + w1[-1] * train_x)
          - train_y).sum()
    d1 = ((w0[-1] + w1[-1] * train_x - train_y)
          * train_x).sum()
    print('{: 4} > w0={: .8f}, w1={: .8f}, \
          loss={: .8f}'.format(
        epoches[-1], w0[-1], w1[-1],
        losses[-1]))
    # w0, w1梯度下降：
    w0.append(w0[-1] - lrate * d0)
    w1.append(w1[-1] - lrate * d1)


mp.figure('Linear Regression')
mp.title('Linear Regression', fontsize=18)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.scatter(train_x, train_y, marker='s',
           c='dodgerblue', alpha=0.5, s=80,
           label='Training Points')

# 通过w0与w1，绘制回归线
pred_train_y = w1[-1] * train_x + w0[-1]
mp.plot(train_x, pred_train_y,
        color='orangered', linewidth=2,
        label='Regression Line')

# 绘制测试点
mp.scatter(test_x, test_y, marker='D',
           c='#732721', alpha=0.5,
           s=60, label='Testing Points')
mp.legend()

# 绘制每次梯度下降过程中w0 w1 loss值的变化。
mp.figure('Training Progress')
mp.subplot(311)
mp.title('Training Progress', fontsize=16)
mp.ylabel('w0', fontsize=14)
mp.tick_params(labelsize=12)
mp.grid(linestyle=":")
mp.plot(epoches, w0[1:], label='w0')
mp.legend()
mp.subplot(312)
mp.title('Training Progress', fontsize=16)
mp.ylabel('w1', fontsize=14)
mp.tick_params(labelsize=12)
mp.grid(linestyle=":")
mp.plot(epoches, w1[1:], label='w1')
mp.legend()
mp.subplot(313)
mp.title('Training Progress', fontsize=16)
mp.ylabel('loss', fontsize=14)
mp.tick_params(labelsize=12)
mp.grid(linestyle=":")
mp.plot(epoches, losses, label='loss')
mp.legend()
mp.tight_layout()

# 绘制空间曲面，观察梯度下降过程
grid_w0, grid_w1 = np.meshgrid(
    np.linspace(0, 9, 500),
    np.linspace(0, 3.5, 500))
# 构建一个数组，结构与grid_w0一致，元素全是0
grid_loss = np.zeros_like(grid_w0)
for x, y in zip(train_x, train_y):
    grid_loss += \
        (grid_w0 + x * grid_w1 - y)**2 / 2
# 绘制曲面
mp.figure("Loss Function")
ax = mp.gca(projection='3d')
mp.title('Loss Function')
ax.set_xlabel('w0', fontsize=12)
ax.set_ylabel('w1', fontsize=12)
ax.set_zlabel('loss', fontsize=12)
ax.plot_surface(
    grid_w0, grid_w1, grid_loss,
    rstride=10, cstride=10, cmap='jet')
ax.plot(w0[:-1], w1[:-1], losses,
        'o-', color='orangered')

# 以等高线的方式绘制梯度下降的过程。
mp.figure('Contour')
mp.xlabel('w0', fontsize=14)
mp.ylabel('w1', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.contourf(grid_w0, grid_w1, grid_loss,
            10, cmap='jet')
cntr = mp.contour(grid_w0, grid_w1, grid_loss,
                  10, colors='black',
                  linewidths=0.5)
mp.clabel(cntr, inline_spacing=0.1,
          fmt='%.2f', fontsize=8)
mp.plot(w0, w1, 'o-', c='orangered',
        label='BGD')
mp.legend()

mp.show()
