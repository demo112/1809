# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sklearn.cluster as sc
import matplotlib.pyplot as mp
import numpy as np
import sklearn.metrics as sm
x = []
with open('multiple3.txt', 'r') as f:
    for line in f.readlines():
        data = [float(substr) for substr in line.split(',')]
        x.append(data)
x = np.array(x)
clstrs, scores, models = np.arange(2, 11), [], []
for clstr in clstrs:
    # 凝聚层次算法----相对距离
    model = sc.AgglomerativeClustering(n_clusters=clstr)  # 4--K(聚类数)=4
    model.fit(x)
    score = sm.silhouette_score(
        x, model.labels_, sample_size=len(x), metric='euclidean')
    scores.append(score)
    models.append(model)
pred_y = models[np.array(scores).argmax()].labels_
print(pred_y)

# k中心值---聚类中心
mp.figure('Agglom')
mp.title('Agglom')
mp.xlabel('x')
mp.ylabel('y')
mp.tick_params(labelsize=10)

mp.scatter(x[:, 0], x[:, 1], c=pred_y, cmap='brg', s=60)

mp.show()
