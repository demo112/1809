# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sklearn.ensemble as se  # 决策树的算法
import sklearn.preprocessing as sp  # 数据预处理
import sklearn.model_selection as ms  # 交叉验证，
import numpy as np


# 验证曲线

data = []
with open('car.txt', 'r') as f:
    for line in f.readlines():
        data.append(line[:-1].split(','))

print(data[:3])
data = np.array(data).T  # 将数据分类
print(data[:7])
encoders, train_x = [], []
for row in range(len(data)):
    encoder = sp.LabelEncoder()
    if row < len(data) - 1:
        train_x.append(encoder.fit_transform(data[row]))
    else:
        train_y = encoder.fit_transform(data[row])
    encoders.append(encoder)

train_x = np.array(train_x).T

print(train_x.shape, train_y.shape)

# 随机森林分类器
model = se.RandomForestClassifier(
    max_depth=8, n_estimators=200, random_state=7)

print(ms.cross_val_score(
    model, train_x, train_y, cv=5, scoring='f1_weighted').mean())


model.fit(train_x, train_y)
data = [
    ['high', 'med', '5more', '4', 'big', 'low'],
    ['high', 'high', '4', '4', 'med', 'med'],
    ['low', 'low', '2', '2', 'small', 'high'],
    ['low', 'med', '4', '4', 'med', 'high']]


data = np.array(data).T
test_x = []
for row in range(len(data)):
    encoder = encoders[row]
    test_x.append(encoder.transform(data[row]))
test_x = np.array(test_x).T
pred_test_y = model.predict(test_x)
print(encoders[-1].inverse_transform(pred_test_y))
