# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# 演示ndarray对象的掩码操作

import numpy as np

a = np.array([1, 2, 3, 4, 5, 6, 7, 8])
f = np.array([True, False, True, False,
              True, False, True, False])
print(a[f])
b = a >= 5
print(b)
print(a[b])
print(a[a > 3])

# 把1~100中3的倍数或7的倍数都打印出来
a = np.arange(1, 100)
flag_a = a % 3 == 0
flag_b = a % 7 == 0
# 3且7的倍数
with_37 = flag_a & flag_b
# 3或7的倍数
or_37 = flag_a | flag_b

print(flag_a)
print(flag_b)

print('3且7的倍数', a[with_37])
print('3或7的倍数', a[or_37])


flag = np.any([flag_a, flag_b], axis=0)
print(a[flag])
