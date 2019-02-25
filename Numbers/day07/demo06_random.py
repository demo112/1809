# -*- coding: utf-8 -*-
from __future__ import unicode_literals

'''
random  测试随机数模块
'''
import numpy as np

# 某人投篮命中率0.3, 投10次,
# 进5个的概率大概多少?
n = 10
p = 0.3
s = np.random.binomial(n, p, 10000000)
print(s)
print(sum(s == 10) / 10000000)

# 某人打电话, 接通率0.6, 打三次都不通的概率:
print(sum(
    np.random.binomial(3, 0.6, 10000) == 0)
      / 10000)

print('-' * 40)
a = np.random.hypergeometric(9, 1, 3, 10)
print(a)

# 产生size个随机数, 每个随机数为在样本中随机抽取samples
# 个样本后好样本的个数.
# 其中总样本由ngood个好样本 和 nbad个坏样本组成.
# s = np.random.hypergeometric(ngood, nbad, samples, size)
print('-' * 40)
a = np.random.hypergeometric(9, 1, 3, 10)
print(a)
