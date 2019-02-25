import numpy as np
import matplotlib.pyplot as mp
# 测试素组的裁剪
a = np.arange(1, 10)
b = a.clip(min=3, max=7)
print(a, b)

# 测试数组的压缩
# c = a.compress((a > 5) & (a < 8))
c = a.compress(np.all([a > 5, a < 8], axis=0))
print(a, c)

# 测试数组的累乘
d = a.prod()
print(a, d)
e = a.cumprod()
print(e)

mp.figure('AAPL', facecolor='lightgray')
mp.title('AAPL', fontsize=18)
mp.xlabel('Date', fontsize=14)
mp.ylabel('Price', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')

# 计算两只股票收盘价的相关程度(协方差)
# 两组样本的均值
ave_a = a.mean()
ave_b = b.mean()
# 两组样本的离差
dev_a = a - ave_a
dev_b = b - ave_b
# 两组样本的协方差
cov_ab = np.mean(dev_a * dev_b)
print(cov_ab)

print(':', (cov_ab / (
            a.std() *
            b.std())))

about = cov_ab / (a.std() * b.std())

mp.plot(a, a)
mp.plot(b, a)
mp.hlines(about * 10, a[0], a[-1], label=about)
mp.legend()
mp.show()
np.roots()