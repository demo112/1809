import numpy as np
import datetime as dt
import matplotlib.pyplot as mp
import matplotlib.dates as md


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
        '../day01/素材/da_data/vale.csv',
        delimiter=',',
        usecols=(1, 3, 4, 5, 6),
        unpack=True,
        dtype='M8[D], f8, f8, f8, f8',
        converters={1: dmy2ymd})

bhp_dates, bhp_opening_prices, bhp_highest_prices, \
bhp_lowest_prices, bhp_closing_prices = \
    np.loadtxt(
        '../day01/素材/da_data/bhp.csv',
        delimiter=',',
        usecols=(1, 3, 4, 5, 6),
        unpack=True,
        dtype='M8[D], f8, f8, f8, f8',
        converters={1: dmy2ymd})

mp.figure('COV', facecolor='lightgray')
mp.title('COV', fontsize=18)
mp.xlabel('Date', fontsize=14)
mp.ylabel('Price', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')

ax = mp.gca()
# x轴主刻度为每周一
ax.xaxis.set_major_locator(
    md.WeekdayLocator(byweekday=md.MO))
ax.xaxis.set_major_formatter(
    md.DateFormatter('%Y-%m-%d'))
# x轴次刻度为每天
ax.xaxis.set_minor_locator(
    md.DayLocator())

print(dates)
mp.plot(dates, closing_prices, label='APPLE', linewidth=2)
mp.plot(dates, bhp_closing_prices, label='BHP', linewidth=2)

# 计算两只股票收盘价的相关程度(协方差)
# 两组样本的均值
ave_a = closing_prices.mean()
ave_b = bhp_closing_prices.mean()
# 两组样本的离差
dev_a = closing_prices - ave_a
dev_b = bhp_closing_prices - ave_b
# 两组样本的协方差
cov_ab = np.mean(dev_a * dev_b)
print(cov_ab)
mp.hlines(cov_ab, dates[0], dates[-1], label=cov_ab)
print(':', (cov_ab / (
        closing_prices.std() *
        bhp_closing_prices.std())))

about = cov_ab / (closing_prices.std() * bhp_closing_prices.std())

mp.hlines(about * 10, dates[0], dates[-1], label=about)
covm = np.corrcoef(closing_prices, bhp_closing_prices)
print(covm)
mp.tight_layout()
mp.legend()
mp.show()
