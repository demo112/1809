# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp
import datetime as dt
import matplotlib.dates as md


# 定义函数,转换日期格式


def dmy2ymd(dmy):
    """转换日期的格式"""
    dmy = str(dmy, encoding='utf-8')
    date = dt.datetime.strptime(
        dmy, '%d-%m-%Y').date()
    s = date.strftime("%Y-%m-%d")
    return s

# 加载文件
dates, opening_prices, highest_prices, \
lowest_prices, closing_prices = \
    np.loadtxt(
        'aapl.csv',
        delimiter=',',
        usecols=(1, 3, 4, 5, 6),
        unpack=True,
        dtype='M8[D], f8, f8, f8, f8',
        converters={1: dmy2ymd})

# 将收盘价转换为折线图
mp.figure("APPLE", facecolor='gray')
mp.title(label='apple')
mp.xlabel('Date')
mp.xlabel('Prices')
mp.tick_params(labelsize=12)
mp.grid(linestyle=":")

ax = mp.gca()
ax.xaxis.set_major_locator(md.WeekdayLocator(byweekday=md.MO))
ax.xaxis.set_major_formatter(md.DateFormatter('%d %b %y'))
ax.xaxis.set_minor_locator(md.DayLocator())
# 修改dates数据类型
dates = dates.astype(md.datetime.datetime)
mp.plot(dates, closing_prices, color='gray',
        linestyle='--', linewidth=3, label='Closing Prices')
mp.tight_layout()
mp.gcf().autofmt_xdate()
mp.legend()
mp.show()