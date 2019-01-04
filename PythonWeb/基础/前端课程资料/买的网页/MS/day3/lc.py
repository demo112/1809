# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sklearn.ensemble as se  # 决策树的算法
import sklearn.preprocessing as sp  # 数据预处理
import sklearn.model_selection as ms  # 交叉验证，
import numpy as np
import matplotlib.pyplot as mp

# ——————————————————学习曲线

data = []
with open('car.txt', 'r') as f:
    for line in f.readlines():
        data.append(line[:-1].split(','))


data = np.array(data).T  # 将数据分类

encoders, train_x = [], []
for row in range(len(data)):
    encoder = sp.LabelEncoder()
    if row < len(data) - 1:
        train_x.append(encoder.fit_transform(data[row]))
    else:
        train_y = encoder.fit_transform(data[row])
    encoders.append(encoder)

train_x = np.array(train_x).T
#-------------------------------------划分训练集大小


print(train_x.shape, train_y.shape)

# 关于超参数n_estimators获取验证曲线

# 随机森林分类器
model = se.RandomForestClassifier(max_depth=9,
                                  n_estimators=490, random_state=7)
train_sizes = np.linspace(0.1, 1, 10)
train_sizes, train_scores, test_scores = ms.learning_curve(
    model, train_x, train_y, train_sizes=train_sizes, cv=5)

print(train_sizes)
test_means = test_scores.mean(axis=1)
train_means = train_scores.mean(axis=1)

mp.figure('train_means')
mp.xlabel("train Size")

mp.plot(train_sizes, train_means, c='red')
mp.plot(train_sizes, test_means, c='blue')
mp.legend()
mp.show()
