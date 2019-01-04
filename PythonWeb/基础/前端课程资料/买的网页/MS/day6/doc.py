# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sklearn.datasets as sd
import sklearn.feature_extraction.text as ft
import sklearn.naive_bayes as nb

# 多项分布朴素贝叶斯分类器

train = sd.load_files('20news', encoding='latin1',
                      shuffle=True, random_state=7)

train_data = train.data
# 训练集主题类别
train_y = train.target
print(train_y)
# 训练集主题条目
categories = train.target_names

# 计数矢量化器
cv = ft.CountVectorizer()
print('-->', cv)
# 训练集词袋矩阵
train_bow = cv.fit_transform(train_data)

# 词频-逆文档频率转换器
tt = ft.TfidfTransformer()
# 训练集的词频逆文档频率矩阵
train_x = tt.fit_transform(train_bow)

# 多项分布朴素贝叶斯分类器
model = nb.MultinomialNB()
# 训练集多项分布朴素贝叶斯分类
model.fit(train_x, train_y)

test_data = [
    'The curveballs of right handed pitchers tend to curve to the left',
    'Caesar cipher is an ancient form of encryption',
    'This two-wheeler is really good on slippery roads']

test_bow = cv.transform(test_data)

test_x = tt.fit_transform(test_bow)

pred_test_y = model.predict(test_x)
print(pred_test_y)
# 打印预测结果--转换为主题目录
for sentence, index in zip(test_data, pred_test_y):
    print(sentence, '->', categories[index])
