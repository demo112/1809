# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
demo01_K.py 绘制K线图
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

mp.plot(dates, closing_prices, alpha=0.5,
        color='dodgerblue', linestyle='--',
        linewidth=2, label='Closing Prices')

# 绘制每一天的蜡烛图：
rise = closing_prices >= opening_prices
# 整理所有的填充色
color = np.array(
    [('white' if x else 'limegreen')
     for x in rise])
# 整理所有的边缘色
edgecolor = np.array(
    [('red' if x else 'limegreen')
     for x in rise])

# 绘制影线
mp.bar(dates, highest_prices - lowest_prices,
       0.1, lowest_prices, color=edgecolor)

# 绘制实体
mp.bar(dates, closing_prices - opening_prices,
       0.8, opening_prices, color=color,
       edgecolor=edgecolor)

mp.legend()
mp.tight_layout()
mp.gcf().autofmt_xdate()
mp.show()
