# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sklearn.ensemble as se  # 决策树的算法
import sklearn.preprocessing as sp  # 数据预处理
import sklearn.model_selection as ms  # 交叉验证，
import numpy as np
import matplotlib.pyplot as mp

# ——————————————————验证曲线

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

print(train_x.shape, train_y.shape)

# 关于超参数n_estimators获取验证曲线

# 随机森林分类器
model = se.RandomForestClassifier(
    n_estimators=490, random_state=7)

max_depth = np.arange(1, 11)
_, test_scores2 = ms.validation_curve(
    model, train_x, train_y, 'max_depth', max_depth, cv=5)


n_estimators = np.arange(50, 550, 50)
_, test_scores1 = ms.validation_curve(
    model, train_x, train_y, 'n_estimators', n_estimators, cv=5)

#跨列取均值 ---按行取值
test_mean1 = test_scores1.mean(axis=1)
print(n_estimators[test_mean1.argmax()])
# test_mean.argmax()最大值的下标

test_mean2 = test_scores2.mean(axis=1)
print(test_mean2.argmax())
print(max_depth[test_mean2.argmax()])

mp.figure('test_mean2.argmax')

mp.xlabel('n_estimators')
mp.ylabel("F1 score")
mp.plot(n_estimators, test_mean1, 'o-')
mp.plot(max_depth, test_mean2, c='red')

mp.figure('test_mean3.argmax')

mp.xlabel('ax_depth')
mp.ylabel("F1 score")

mp.plot(max_depth, test_mean2, c='red')


mp.legend()
mp.show()
