# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sklearn.datasets as sd
import sklearn.utils as su  # 打乱
import sklearn.tree as st
import sklearn.ensemble as se
import sklearn.metrics as sm

# 获取并展示数据结构
boston = sd.load_boston()
print(boston.data.shape)
print(boston.target.shape)
print(boston.feature_names)

# 打乱原始输入，输出数据集， 划分测试训练集
x, y = su.shuffle(boston.data, boston.target, random_state=7)  # 随机种子，是几无所谓，每次种子一样，随机结果一样

# 选取训练集
train_size = int(len(x) * 0.8)
train_x, test_x, train_y, test_y = x[:train_size], x[train_size:], y[:train_size], y[train_size:]

# 创建模型，使用训练集数据进行训练
model = st.DecisionTreeRegressor(max_depth=5)
model.fit(train_x, train_y)
pred_test_y = model.predict(test_x)
print(sm.r2_score(test_y, pred_test_y))

model = se.AdaBoostRegressor(
    st.DecisionTreeRegressor(max_depth=7),
    n_estimators=400, random_state=7)
model.fit(train_x, train_y)
pred_test_y = model.predict(test_x)
print(sm.r2_score(test_y, pred_test_y))
