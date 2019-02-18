# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
max.py 最值相关API
"""
import numpy as np
import matplotlib.pyplot as mp
import datetime as dt
import matplotlib.dates as md


def dmy2ymd(dmy):
    # 28-10-2011  -> 2011-10-28
    # 把字符串转成日期对象，在按照需要的
    # 格式把日期对象转成字符串
    dmy = str(dmy, encoding='utf-8')
    time = dt.datetime.strptime(
        dmy, '%d-%m-%Y').date()
    t = time.strftime('%Y-%m-%d')
    print(t)
    return t

dates, opening_prices, highest_prices, \
    lowest_prices, closing_prices = \
    np.loadtxt('../da_data/aapl.csv',
               delimiter=',',
               usecols=(1, 3, 4, 5, 6),
               unpack=True,
               dtype='M8[D], f8, f8, f8, f8',
               converters={1: dmy2ymd})

# 把收盘价绘制为折线图
mp.figure('APPL', facecolor='lightgray')
mp.title('APPL', fontsize=18)
mp.xlabel('Dates', fontsize=14)
mp.ylabel('Prices', fontsize=14)
mp.tick_params(labelsize=12)
mp.grid(linestyle=':')
# 为了x轴显示日期，设置刻度定位器
ax = mp.gca()
ax.xaxis.set_major_locator(
    md.WeekdayLocator(byweekday=md.MO))
ax.xaxis.set_major_formatter(
    md.DateFormatter('%d %b %Y'))
ax.xaxis.set_minor_locator(md.DayLocator())

# 修改dates的数据类型 从M8[D] ->
dates = dates.astype(md.datetime.datetime)

mp.plot(dates, closing_prices,
        linewidth=2, label='Closing Prices')
mp.plot(dates, highest_prices,
        linewidth=2, label='Highest Prices')
mp.plot(dates, lowest_prices,
        linewidth=2, label='Lowest Prices')

# 求最值
max_highest = np.max(highest_prices)
min_lowest = np.min(lowest_prices)
print(max_highest - min_lowest)

# 求最高点、最低点的日期
print(dates[np.argmax(highest_prices)])
print(dates[np.argmin(lowest_prices)])

mp.legend()
mp.tight_layout()
mp.gcf().autofmt_xdate()
mp.show()
