# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sklearn.naive_bayes as nb
import numpy as np
import matplotlib.pyplot as mp

x, y = [], []
with open('multiple1.txt', 'r') as f:
    for line in f:
        data = [float(substr) for substr in line.split(',')]

        x.append(data[:-1])
        print(x)
        y.append(data[-1])
x = np.array(x)

y = np.array(y, dtype=int)
# 朴素贝叶斯分类,-----高斯分类 正态分布
model = nb.GaussianNB()
# 训练集
model.fit(x, y)
# 点阵水平边界
l, r, h = x[:, 0].min() - 1, x[:, 0].max() + 1, 0.005
# 点阵垂直边界
b, t, v = x[:, 1].min() - 1, x[:, 1].max() + 1, 0.005

# 生成点阵
grid_x = np.meshgrid(np.arange(l, r, h),
                     np.arange(b, t, v))

# 点阵中每个点的水平坐标和垂直坐标作为样本的两个特征
# 样本的两个特征合并成一个两列的二维数组
flat_x = np.c_[grid_x[0].ravel(), grid_x[1].ravel()]
flat_y = model.predict(flat_x)


# 将一维数组形式的类别变成点阵形式的二维数组
print(grid_x[0].shape)
grid_y = flat_y.reshape(grid_x[0].shape)
print(type(grid_y))
print(flat_y.shape)
# 将训练集中的输入带入模型预测类别输出
pred_y = model.predict(x)

print((pred_y == y).sum() / pred_y.size)


# 绘制训练样本和分类边界
mp.figure("Gaussian", facecolor='lightgray')
mp.xlabel('x')
mp.ylabel('y')

mp.tick_params(labelsize=20)
mp.pcolormesh(grid_x[0], grid_x[1], grid_y, cmap='gray')
mp.scatter(x[:, 0], x[:, 1], c=y, cmap='brg', s=80)
mp.show()
