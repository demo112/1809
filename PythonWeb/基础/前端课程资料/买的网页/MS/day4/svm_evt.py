# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import sklearn.model_selection as ms
import sklearn.preprocessing as sp
import numpy as np
import sklearn.model_selection as ms
import sklearn.svm as svm
import sklearn.metrics as sm
import matplotlib.pyplot as mp


class Dightcoder():

    def fit_transform(self, x):
        return x.astype(int)

    def transform(self, x):
        return x.astype(int)

    def inverse_transform(self, x):
        return x.astype(str)


data = []

with open('events.txt', 'r') as f:
    for line in f.readlines():
        data.append((line[:-1]).split(','))

# 二维列表变成二维数组并转置后删除第1行，日期行删除
print(np.array(data).T)
data = np.delete(np.array(data).T, 1, 0)
print(data)
encoders, x = [], []
for row in range(len(data)):
    print(data[row, 0])
    if data[row, 0].isdigit():
        encoder = Dightcoder()
    else:
        encoder = sp.LabelEncoder()
    encoder.fit_transform(data[row])

    if row < len(data) - 1:
        x.append(encoder.fit_transform(data[row]))
    else:
        y = encoder.fit_transform(data[row])
    encoders.append(encoder)
print(y)
x = np.array(x).T
print(x)

train_x, test_x, train_y, test_y = ms.train_test_split(
    x, y, test_size=0.25, random_state=5)

model = svm.SVC(kernel='rbf', class_weight='balanced', C=600, gamma=0.01)
print(ms.cross_val_score(model, train_x, train_y, cv=5).mean())

model.fit(train_x, train_y)
pred_test_y = model.predict(test_x)
print((pred_test_y == test_y).sum() / pred_test_y.size)
data = [['Tuesday', '12:30:00', '21', '26']]
data = np.array(data).T
x = []
for row in range(len(data)):
    encoder = encoders[row]
    x.append(encoder.transform(data[row]))

x = np.array(x).T

pred_y = model.predict(x)
print(encoders[-1].inverse_transform(pred_y))
