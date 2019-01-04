# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sklearn.cluster as sc
import matplotlib.pyplot as mp
import numpy as np

x = []
with open('multiple3.txt', 'r') as f:
    for line in f.readlines():
        data = [float(substr) for substr in line.split(',')]
        x.append(data)
x = np.array(x)
bw = sc.estimate_bandwidth(x, n_samples=len(x), quantile=0.1)  # 量化带宽

# 基于欧式距离
model = sc.MeanShift(bandwidth=bw, bin_seeding=True)

model.fit(x)
pred_y = model.labels_
print(pred_y)

centers = model.cluster_centers_

l, r, h = x[:, 0].min() - 1, x[:, 0].max() + 1, 0.005
b, t, v = x[:, 1].min() - 1, x[:, 1].max() + 1, 0.005
grid_x = np.meshgrid(np.arange(l, r, h), np.arange(b, t, v))

flat_x = np.c_[grid_x[0].ravel(), grid_x[1].ravel()]
flat_y = model.predict(flat_x)
grid_y = flat_y.reshape(grid_x[0].shape)

mp.figure('Shift-means')
mp.title('Shift-means')
mp.xlabel('x')
mp.ylabel('y')
mp.tick_params(labelsize=10)
mp.pcolormesh(grid_x[0], grid_x[1], grid_y)
mp.scatter(x[:, 0], x[:, 1], c=pred_y, cmap='brg', s=60)
mp.scatter(centers[:, 0], centers[:, 1], marker='+',
           c='red', s=1000, linewidth=10)
mp.show()
