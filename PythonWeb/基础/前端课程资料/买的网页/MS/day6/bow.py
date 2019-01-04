# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import nltk.tokenize as tk
import sklearn.feature_extraction.text as ft
import sklearn.preprocessing as sp


doc = 'The brown dog is running. ' \
      'The black dog is in the black room. ' \
      'Running in the room is forbidden.'

ss = tk.word_tokenize(doc)
print(ss)
sentences = tk.sent_tokenize(doc)
# 计数矢量化器
cv = ft.CountVectorizer()
# 词袋矩阵
bow = cv.fit_transform(sentences).toarray()
print(bow)
words = cv.get_feature_names()
print(words)
tf = sp.normalize(bow, norm='l1')
print(tf)
print('----------------')
# 词频逆文档频率
# 词频逆文档频率转换器
tt = ft.TfidfTransformer()
# toarray(),将稀疏矩阵转换为正常矩阵
tifd = tt.fit_transform(bow).toarray()
print(tifd)
