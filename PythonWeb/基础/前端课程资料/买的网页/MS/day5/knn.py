# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sklearn.neighbors as sn
import numpy as np
import matplotlib.pyplot as mp

train_x, train_y = [], []
with open('knn.txt', 'r') as f:
    for line in f:
        data = [float(substr) for substr in line.split(',')]

        train_x.append(data[:-1])

        train_y.append(data[-1])
x = np.array(train_x)

y = np.array(train_y, dtype=int)
# KNN分类器模型
model = sn.KNeighborsClassifier(n_neighbors=10, weights='distance')
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

test_x = np.array([
    [2.2, 6.2],
    [3.6, 1.8],
    [4.5, 3.6]])


pred_test_y = model.predict(test_x)

knn_distance, nn_indices = model.kneighbors(test_x)
print(knn_distance)
print(nn_indices)
# 将训练集中的输入带入模型预测类别输出
pred_y = model.predict(flat_x)

# 绘制训练样本和分类边界
mp.figure("KNN", facecolor='lightgray')
mp.xlabel('x')
mp.ylabel('y')
mp.tick_params(labelsize=20)
mp.pcolormesh(grid_x[0], grid_x[1], grid_y, cmap='gray')
mp.scatter(x[:, 0], x[:, 1], c=y, cmap='brg', s=80)
mp.scatter(test_x[:, 0], test_x[:, 1], c=pred_test_y,
           cmap='brg', s=80, marker='D')
mp.scatter(x[nn_indices[0], 0], x[nn_indices[0], 1],
           marker='D', edgecolor='r', facecolor='none', s=180)
mp.scatter(x[nn_indices[1], 0], x[nn_indices[1], 1],
           marker='D', edgecolor='g', facecolor='none', s=180)
mp.scatter(x[nn_indices[2], 0], x[nn_indices[2], 1],
           marker='D', edgecolor='g', facecolor='none', s=180)

mp.show()
