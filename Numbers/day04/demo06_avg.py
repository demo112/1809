# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
demo06_avg.py  统计周一、..周五的收盘价的均值。
"""
import numpy as np
import datetime as dt


def dmy2day(dmy):
    # 日月年字符串转成星期
    dmy = str(dmy, encoding='utf-8')
    date = dt.datetime.strptime(
        dmy, '%d-%m-%Y').date()
    wday = date.weekday()
    return wday

wdays, closing_prices = np.loadtxt(
    '../da_data/aapl.csv',
    delimiter=',', usecols=(1, 6),
    unpack=True, converters={1: dmy2day})

print(wdays)

ave_closing_prices = np.zeros(5)
for wday in range(ave_closing_prices.size):
    ave_closing_prices[wday] = \
        np.mean(closing_prices[wdays == wday])

print(ave_closing_prices)
