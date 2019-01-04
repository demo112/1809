# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sklearn.datasets as sd
import sklearn.utils as su  # 打乱顺序
import sklearn.ensemble as se  # 三种决策树的集成算法
import sklearn.metrics as sm
import matplotlib.pyplot as mp
import numpy as np
import csv
# 读取bikeday.csv
with open('bike_hour.csv', 'r') as f:
    reader = csv.reader(f)
    x, y = [], []
    for row in reader:
        x.append(row[2:13])
        y.append(row[-1])

fn_dy = np.array(x[0])
x = np.array(x[1:], dtype=float)
y = np.array(y[1:], dtype=float)
x, y = su.shuffle(x, y, random_state=7)
train_size = int(len(x) * 0.9)
train_x, test_x, train_y, test_y = \
    x[:train_size], x[train_size:],\
    y[:train_size], y[train_size:]
# 训练模型
model = se.RandomForestRegressor(
    max_depth=10, n_estimators=1000, min_samples_split=2)
model.fit(train_x, train_y)
fi = model.feature_importances_
pre_test_y = model.predict(test_x)
print(sm.r2_score(test_y, pre_test_y))
mp.figure("111feature_importances", facecolor='lightgray')
mp.title('feature_importances', fontsize=14)

mp.xlabel('feature')
mp.ylabel('importace')

mp.grid(axis='y')
sorted_indices = fi.argsort()[::-1]
pos = np.arange(sorted_indices.size)
mp.bar(pos, fn_dy[sorted_indices], facecolor='blue')
mp.xticks(pos, fn_dy, rotation=30)
mp.show()
