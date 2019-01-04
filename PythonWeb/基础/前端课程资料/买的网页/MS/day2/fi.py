# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# 决策树的回归问题
import sklearn.datasets as sd
import sklearn.utils as su  # 打乱顺序
import sklearn.tree as st
import sklearn.ensemble as se  # 三种决策树的集成算法
import sklearn.metrics as sm
import matplotlib.pyplot as mp
import numpy as np
boston = sd.load_boston()
fn = boston.feature_names
print(boston.data)
# 打乱数据,random_state=7 是随机种子
x, y = su.shuffle(boston.data, boston.target, random_state=7)
train_size = int(len(x) * 0.8)
train_x, test_x, train_y, test_y = \
    x[:train_size], x[train_size:],\
    y[:train_size], y[train_size:]

# 创建决策树回归
model = st.DecisionTreeRegressor(max_depth=4)
# 训练模型
model.fit(train_x, train_y)
# 测试模型
pre_test_y = model.predict(test_x)
print(sm.r2_score(test_y, pre_test_y))


# 基于决策树的正向激励模型
model = se.AdaBoostRegressor(
    st.DecisionTreeRegressor(max_depth=4), n_estimators=400, random_state=7)
# 训练模型
model.fit(train_x, train_y)
# 测试模型
pre_test_y = model.predict(test_x)
# print(sm.r2_score(test_y, pre_test_y))
# 获取特征重要性
fi = model.feature_importances_
mp.figure("feature_importances", facecolor='lightgray')
mp.title('feature_importances', fontsize=14)
mp.xlabel('feature')
mp.ylabel('importace')

mp.grid(axis='y')
sorted_indices = fi.argsort()[::-1]
pos = np.arange(sorted_indices.size)
mp.bar(pos, fi[sorted_indices], facecolor='blue')
mp.xticks(pos, fn, rotation=30)
mp.show()
