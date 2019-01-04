# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sklearn.cluster as sc
import matplotlib.pyplot as mp
import numpy as np
import sklearn.metrics as sm
x = []
with open('perf.txt', 'r') as f:
    for line in f.readlines():
        data = [float(substr) for substr in line.split(',')]
        x.append(data)
x = np.array(x)
epsilons, scores, models = np.linspace(0.3, 1.2, 10), [], []
for epsilon in epsilons:
   # 带噪声的基于密度的聚类
   # eps---朋友圈的半径
   # min_samples=5--聚类规模最小阈值
    model = sc.DBSCAN(eps=epsilon, min_samples=5)  # eps=epsilon 圆的半径
    model.fit(x)
    score = sm.silhouette_score(
        x, model.labels_, sample_size=len(x), metric='euclidean')
    scores.append(score)
    models.append(model)
best_model = models[np.array(scores).argmax()]
pred_y = best_model.labels_

core_mask = np.zeros(len(x), dtype=bool)
core_mask[model.core_sample_indices_] = True
offset_mask = pred_y == -1
periphery_mask = ~(core_mask | offset_mask)


# # k中心值---聚类中心
mp.figure('Agglom')
mp.title('Agglom')
mp.xlabel('x')
mp.ylabel('y')
mp.tick_params(labelsize=10)
labels = set(pred_y)
print(labels)

# 0,1,2,3,4,5
# B---R----G
# 将色带分为六等份
cs = mp.get_cmap('brg', len(labels))(range(len(labels)))
mp.scatter(x[core_mask][:, 0], x[core_mask][
           :, 1], c=cs[pred_y[core_mask]], s=60)

mp.scatter(x[periphery_mask][:, 0],
           x[periphery_mask][:, 0], c=cs[pred_y[periphery_mask]], marker='o'
           )

mp.scatter(x[offset_mask][:, 0],
           x[offset_mask][:, 0], c=cs[pred_y[offset_mask]], marker='x'
           )

mp.show()
