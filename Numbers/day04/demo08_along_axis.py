# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
demo08_axis.py  轴向统计
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

# 第一个周一的下标， 最后一个周五的下标
# np.where方法返回一个元组，数据存储在[0]中
first_mon = np.where(wdays == 0)[0][0]
last_fri = np.where(wdays == 4)[0][-1]
wdays = wdays[first_mon: last_fri + 1]

indices = np.arange(first_mon, last_fri + 1)
# 整理这些数据为一个二维数组
mon_inds = indices[wdays == 0]
tue_inds = indices[wdays == 1]
wen_inds = indices[wdays == 2]
thu_inds = indices[wdays == 3]
fri_inds = indices[wdays == 4]

# 把不足6个元素的数组补齐
mon_inds = np.pad(
    mon_inds, pad_width=(0, 1),
    mode='constant', constant_values=-1)

# 把这些数据在垂直方向摞在一起，执行轴向汇总
data = np.vstack(
    (mon_inds, tue_inds, wen_inds,
     thu_inds, fri_inds))

print(data)


def func(row):
    row = row[row != -1]
    return np.max(closing_prices[row]), \
        np.min(closing_prices[row]),	\
        np.mean(closing_prices[row])

r = np.apply_along_axis(func, 1, data)
print(r)
