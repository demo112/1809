# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
mean.py 求均值
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
    lowest_prices, closing_prices,\
    volumns = \
    np.loadtxt('../da_data/aapl.csv',
               delimiter=',',
               usecols=(1, 3, 4, 5, 6, 7),
               unpack=True,
               dtype='M8[D], f8, f8, f8, f8, f8',
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
        color='dodgerblue', linestyle='--',
        linewidth=2, label='Closing Prices')

# 绘制收盘价的均值水平线
mean = np.mean(closing_prices)
mp.hlines(mean, dates[0], dates[-1],
          color='orangered', linewidth=2,
          label='average(closing_prices)')

# VWAP 交易量加权平均价格
vwap = np.average(closing_prices,
                  weights=volumns)
mp.hlines(vwap, dates[0], dates[-1],
          color='limegreen', linewidth=2,
          label='VWAP')

# TWAP 时间加权平均价格
times = np.arange(1, 31)
times = np.linspace(1, 10, 30)
twap = np.average(closing_prices,
                  weights=times)
mp.hlines(twap, dates[0], dates[-1],
          color='gold', linewidth=2,
          label='TWAP')

# 求出收盘价的中位数
median = np.median(closing_prices)
sc = np.msort(closing_prices)

m2 = (sc[int((sc.size - 1) / 2)] +
      sc[int(sc.size / 2)]) / 2
print(median, m2)

mp.hlines(twap, dates[0], dates[-1],
          color='red', linewidth=2,
          label='Median')


mp.legend()
mp.tight_layout()
mp.gcf().autofmt_xdate()
mp.show()
