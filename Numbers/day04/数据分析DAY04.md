# 数据分析DAY04

### 加载文件

案例：绘制AAPL的K线图.

```python
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
```

### 算数平均数

算数平均数表示对真值的无偏估计。

```
A = [a1, a2, a3, ... an]
mean = (a1 + a2 + a3 + ... + an) / n
```

numpy提供了方法求一组数据的均值：

```python
# 1.
m = np.mean(array)
# 2.
m = array.mean()
```

案例：

```python
# 绘制收盘价的均值水平线
mean = np.mean(closing_prices)
mp.hlines(mean, dates[0], dates[-1],
          color='orangered', linewidth=2,
          label='average(closing_prices)')
```

### 加权平均值

```
S = [s1, s2, s3, .. sn]
W = [w1, w2, w3, .. wn]
# 加权均值：
aw = (s1w1 + s2w2 + ... sn*wn)/(w1+w2+...wn)
```

相关API：

```python
# a: 原始样本数组
# b: 与原始样本数组相对应的权重数组
np.average(a, weights=b)
```

VWAP - 交易量加权平均价格（成交量体现了市场对于当前交易价格的认可度， 成交量加权平均价格将会更接近这只股票的价值）

案例：

```pythoon
# VWAP 交易量加权平均价格
vwap = np.average(closing_prices,
                  weights=volumns)
mp.hlines(vwap, dates[0], dates[-1],
          color='limegreen', linewidth=2,
          label='VWAP')

```

TWAP-时间加权平均价格

```python
# TWAP 时间加权平均价格
times = np.arange(1, 31)
times = np.linspace(1, 10, 30)
twap = np.average(closing_prices,weights=times)
mp.hlines(twap, dates[0], dates[-1],
          color='gold', linewidth=2,
          label='TWAP')
```

### 最值

```python
np.max(a)	# 返回一组数据的最大值
np.min(a)	# 返回一组数据的最小值
np.ptp(a)	# 返回一组数据的极差 (max-min)
```

```python
np.argmax(a)	# 返回一组数据最大值的下标
np.argmin(a) 	# 返回一组数据最小值的下标
```

案例：

```python
# 求最值
max_highest = np.max(highest_prices)
min_lowest = np.min(lowest_prices)
print(max_highest - min_lowest)

# 求最高点、最低点的日期
print(dates[np.argmax(highest_prices)])
print(dates[np.argmin(lowest_prices)])
```



```python
# 将两个同维数组中对应位置的元素进行比较，把最大的保留。返回新数组
np.maximum(a, b)
# 将两个同维数组中对应位置的元素进行比较，把最小的保留。返回新数组
np.minimum(a, b)
```

案例：

```python
a = np.arange(1, 10).reshape(3, 3)
b = np.arange(1, 10)[::-1].reshape(3, 3)
print(np.maximum(a, b))
print(np.minimum(a, b))
```

### 中位数

将多个样本按照大小排序，取中间位置的元素。

如果样本个数为奇数，则为中间的数字。如果样本个数为偶数，则求两个中间数字的均值即可。

```python
a = [..排序过的数组..]
median = (a[(a.size-1)/2] + a[a.size/2]) / 2

# 对数组排序
sc = np.msort(closing_prices)
m2 = (sc[int((sc.size - 1) / 2)] +
      sc[int(sc.size / 2)]) / 2
print(median, m2)

# 求a数组的中位数
np.median(a)
```

### 标准差

一组数据的标准差可以衡量这组数据的离散程度。标准差越大代表这组样本越散。反之，则代表这组样本越集中。

样本：S = [s1, s2, s3 ...,  sn]

均值：m = (s1 + s2 + ... + sn) / n

离差：D = [s1-m, s2-m, s3-m .... , sn-m]

离差方： D<sup>2</sup>  -> [q1, q2, q3 .... qn]    每个元素求平方

总体方差：(q1+q2+...qn) / **n**  离差方数组的均值

总体标准差：np.sqrt(总体方差)   

样本方差： (q1+q2+...qn) / **n-1**  离差方数组的均值

样本标准差：np.sqrt(样本方差)   

```python
# 求array数组的总体标准差
np.std(array)
# 求array数组的样本标准差，分母的修正值：n-1
np.std(array, ddof=1)
```

案例：

```python
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

```

### 案例应用

#### 案例：轴向统计

统一每个周一、周二、.. 周五的收盘价的平均值，并放入一个数组。

```python
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

ave_closing_prices = np.zeros(5)
for wday in range(ave_closing_prices.size):
    ave_closing_prices[wday] = \
        np.mean(closing_prices[wdays == wday])

print(ave_closing_prices)
```

案例：统一每个周一、周二、.. 周五的收盘价的平均值，最大值，最小值，并放入一个数组。

numpy提供了一个方法可以方便的实现**二维数据的轴向汇总**。

```python
def func(data):
    pass
# 根据轴向的设定，把每一行（列）依次传递给func函数实现统计业务
# func： 处理函数
# axis： 轴向  0  1
# array： 原二维数组
np.apply_along_axis(func, axis, array)
```

案例：

```python
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

```

#### 案例：移动平均线

收盘价5日平均线：从第五天开始，每天计算最近5天的收盘价的平均值所构成的一条线。

移动均线的算法：

```
(a + b + c + d + e) / 5	 均线的第1个点
(b + c + d + e + f) / 5	 均线的第2个点
....
```

案例：绘制5日均线图

```python
# 求5日均线
sma5 = np.zeros(closing_prices.size - 4)
for i in range(sma5.size):
    sma5[i] = closing_prices[i:i + 5].mean()

mp.plot(dates[4:], sma5, color='orangered',
        linewidth=2,
        linestyle='-', label='SMA-5')
```

#### 卷积运算

a = [1, 2, 3, 4, 5] 	原数组

b = [8, 7, 6]		卷积核数组

使用b数组作为卷积核对a数组执行卷积运算的过程如下：

```
				44	65	86			- 有效卷积(valid)
			23	44	65	86	59		- 同维卷积(same)
		8	23	44	65	86	59	30	- 完全卷积(full)
0	0	1	2	3	4	5	0	0
6	7	8
	6	7	8
		6	7	8
			6	7	8
				6	7	8
					6	7	8
						6	7	8
```

卷积运算相关API：

```python
# a: 原数组
# b: 卷积核数组
# 卷积类型： 
# 	'valid'	有效卷积
# 	'same'	同维卷积
# 	'full'	完全卷积
np.convole(a, b, 卷积类型)
```

```
a b c d e f g h i j k l ....
b = [1/5, 1/5, 1/5, 1/5, 1/5] 
```

案例： 使用卷积实现5日均线

```python
# 使用卷积 实现5日均线
core = np.ones(5) / 5
sma52 = np.convolve(closing_prices, core,
                    'valid')
mp.plot(dates[4:], sma52, color='orangered',
        linewidth=7, alpha=0.3,
        linestyle='-', label='SMA-52')

# 使用卷积 实现10日均线
core = np.ones(10) / 10
sma510 = np.convolve(closing_prices, core,
                     'valid')
mp.plot(dates[9:], sma510, color='limegreen',
        linewidth=2, alpha=0.8,
        linestyle='-', label='SMA-10')
```

**加权卷积**

5日均线中计算的平均值为算数平均值，但是每个样本应该有不同的权重。按照时间加权均值的算法，时间越晚权重越高。所以可以选出一组卷积核，使得在卷积运算中实现加权卷积。

```python
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
```

#### 布林带

布林带由三条线组成：

中轨：移动均线

上轨：中轨 + 2*5日标准差

下轨：中轨 -  2*5日标准差

布林带收窄代表股价趋于稳定，布林带张开代表有较大的波动空间。













