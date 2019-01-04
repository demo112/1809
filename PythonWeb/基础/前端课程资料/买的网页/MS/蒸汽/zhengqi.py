# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sklearn.ensemble as se  # 决策树的算法
import sklearn.preprocessing as sp  # 数据预处理
import sklearn.model_selection as ms  # 交叉验证，
import numpy as np


data = []
with open('zhengqi_train.txt') as f:
    for line in f.readlines():
        data.append(line[:-1].split('\t'))
data = np.array(data).T  # 将数据分类
print(data[-3:])

train_x = []
for row in range(len(data)):
    if row < len(data) - 1:
        train_x.append(data[row])
    else:
        train_y = data[row]

train_x = np.array(train_x).T

print(train_x)

model.fit(train_x, train_y)
print(model.best_params_, model.best_score_)
