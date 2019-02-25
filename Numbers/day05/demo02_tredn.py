# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp
import datetime as dt
import matplotlib.dates as md
import pandas as pd

'''
demo02_predict: 线性预测
假设股价符合某种线性方程, 预测下一天的股价
'''


def dmy2ymd(dmy):
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

# 绘制收盘价的折线图
mp.figure('AAPL', facecolor='lightgray')
mp.title('AAPL', fontsize=18)
mp.xlabel('Date', fontsize=14)
mp.ylabel('Price', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
# 设置刻度定位器, x轴需要显示时间信息
ax = mp.gca()
# x轴主刻度为每周一
ax.xaxis.set_major_locator(
    md.WeekdayLocator(byweekday=md.MO))
ax.xaxis.set_major_formatter(
    md.DateFormatter('%Y-%m-%d'))
# x轴次刻度为每天
ax.xaxis.set_minor_locator(
    md.DayLocator())
# 把日期数组元素类型改为md可识别的类型
dates = dates.astype(md.datetime.datetime)

trend_points = (highest_prices + lowest_prices + closing_prices) / 3
mp.plot(dates, trend_points, color='red',
        linewidth=2, linestyle=':',
        label='Trendpoints')
days = dates.astype('M8[D]').astype(int)
a = np.column_stack((days, np.ones(days.size)))
b = trend_points
# 绘制趋势线

x = np.linalg.lstsq(a, b)[0]
y = x[0] * days + x[1]
mp.plot(dates, y,
        color='dodgerblue', linewidth=3,
        label='Trend Line')

print(a)
print(b)

spreads = highest_prices - lowest_prices
# 绘制顶部压力线 (trend+(highest-lowest))
resistance_points = y + spreads
mp.plot(dates, resistance_points,
           color='orangered', alpha=0.8,
           zorder=4)

# 绘制底部支撑线 (trend-(highest-lowest))
support_points = y - spreads
mp.plot(dates, support_points,
           color='limegreen', alpha=0.8,
           zorder=4)




mp.legend()
# 自动格式化日期显示方式
mp.gcf().autofmt_xdate()
mp.show()
