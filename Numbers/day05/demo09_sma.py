# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
demo09_sma.py 移动平均线
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
    return t

dates, opening_prices, highest_prices, \
    lowest_prices, closing_prices = \
    np.loadtxt('aapl.csv',
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

mp.plot(dates, closing_prices, alpha=0.6,
        color='dodgerblue', linestyle='-',
        linewidth=2, label='Closing Prices')

# 使用卷积 实现5日均线
core = np.ones(5) / 5
sma52 = np.convolve(closing_prices, core,
                    'valid')
mp.plot(dates[4:], sma52, color='orangered',
        linewidth=7, alpha=0.3,
        linestyle='-', label='SMA-52')

# 实现加权5日均线
weights = np.exp(np.linspace(-1, 0, 5))
weights = weights[::-1]
# 处理卷积核数组，使得卷积核中元素之和为1
weights /= weights.sum()
sma53 = np.convolve(closing_prices,
                    weights, 'valid')
mp.plot(dates[4:], sma53,
        linewidth=2, alpha=0.8,
        linestyle='-', label='SMA-53')

stds = np.zeros(sma53.size)
for i in range(stds.size):
    stds[i] = closing_prices[i:i + 5].std()
# 计算上轨和下轨
# 计算中轨
lowers = sma53 - 2 * stds
uppers = sma53 + 2 * stds

mp.plot(dates[4:], lowers, color='gold',
        linewidth=1, label='Lower Line')
mp.plot(dates[4:], uppers, color='gold',
        linewidth=1, label='upper Line')


mp.fill_between(dates[4:], lowers, uppers, uppers>lowers,
                color='gold', zorder=1, alpha=0.5)

mp.legend()
mp.tight_layout()
mp.gcf().autofmt_xdate()
mp.show()
