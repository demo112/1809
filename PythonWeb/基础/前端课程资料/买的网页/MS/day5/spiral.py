# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sklearn.cluster as sc
import matplotlib.pyplot as mp
import numpy as np
import sklearn.neighbors as nb  # 方向变化最小的近邻

n_sample = 500
t = 2.5 * np.pi * (1 + 2 * np.random.rand(n_sample, 1))
# 阿基米德圈
x = 0.05 * t * np.cos(t)
y = 0.05 * t * np.sin(t)
n = 0.05 * np.random.rand(n_sample, 2)
x = np.hstack((x, y)) + n
model = sc.AgglomerativeClustering(linkage='average', n_clusters=3)

pred_y1 = model.fit_predict(x)
# 寻找连续性 近邻方法connectivity=nb.kneighbors_graph(x,10,include_self=False)
model = sc.AgglomerativeClustering(
    linkage='average', n_clusters=3, connectivity=nb.kneighbors_graph(x, 10, include_self=False))

pred_y2 = model.fit_predict(x)

# # 凝聚层次算法----相对距离
# model = sc.AgglomerativeClustering(n_clusters=4)  # 4--K(聚类数)=4

# model.fit(x)
# pred_y = model.labels_
# print(pred_y)

# k中心值---聚类中心
mp.figure('Agglom1')
mp.title('Agglom1')
mp.xlabel('x')
mp.ylabel('y')
mp.tick_params(labelsize=10)

mp.scatter(x[:, 0], x[:, 1], c=pred_y1, s=30, alpha=0.75)
mp.figure('Agglom2')
mp.title('Agglom2')
mp.xlabel('x')
mp.ylabel('y')
mp.tick_params(labelsize=10)

mp.scatter(x[:, 0], x[:, 1], c=pred_y2, s=30, alpha=0.75)
mp.show()
