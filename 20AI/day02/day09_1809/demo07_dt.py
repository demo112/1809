# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
demo07_dt.py 决策树预测房屋价格
"""
import sklearn.datasets as sd
import sklearn.utils as su
import sklearn.tree as st
import sklearn.metrics as sm
import sklearn.ensemble as se
import sklearn.linear_model as lm


boston = sd.load_boston()
print(boston.data.shape)  # 数据量
print(boston.target.shape)
print(boston.feature_names)  # 13个特征名

# 打乱原始输入、输出数据集
x, y = su.shuffle(
    boston.data, boston.target, random_state=7)
# 划分测试集、训练集
train_size = int(len(x) * 0.8)
train_x, train_y, test_x, test_y = \
    x[:train_size], y[:train_size], \
    x[train_size:], y[train_size:]

# 创建模型， 使用训练集数据进行训练
model = st.DecisionTreeRegressor(max_depth=4)
model.fit(train_x, train_y)
# 测试集数据预测
pred_test_y = model.predict(test_x)
# 输出R2得分
print(sm.r2_score(test_y, pred_test_y))

model = se.AdaBoostRegressor(
    model, 	# 基础模型
    n_estimators=400,  # 决策树的数量
    random_state=7  # 随机种子
)
model.fit(train_x, train_y)
pred_test_y = model.predict(test_x)
# 输出R2得分
print(sm.r2_score(test_y, pred_test_y))
