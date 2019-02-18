# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
demo05_std.py  标准差示例
"""
import numpy as np

closing_prices = np.loadtxt(
    '../da_data/aapl.csv', delimiter=',',
    usecols=(6,), unpack=True)
# 求这组数据的标准差
m = np.mean(closing_prices)
s = np.mean((closing_prices - m) ** 2)
std = np.sqrt(s)
print(std)

std = np.std(closing_prices)
print(std)

std = np.std(closing_prices, ddof=1)
print(std)
