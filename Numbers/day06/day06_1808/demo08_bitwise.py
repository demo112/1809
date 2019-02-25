# -*- coding: utf-8 -*-
from __future__ import unicode_literals
'''
位操作
'''
import numpy as np

a = np.array([4, -6, 7, -3, -4, 2])
b = np.array([-2, -8, 2, -5, 3, -4])

print(a)
print(b)
print(a ^ b)
print(np.bitwise_xor(a, b))
# where找到符合条件的元素下标 (异号)
print(np.where((a ^ b) < 0)[0])


print('-' * 40)
d = np.arange(1, 20)
print(d)
e = np.bitwise_and(d, d - 1)
print(e)
print((d & d - 1))
print(d[np.where(((d & d - 1) == 0))[0]])


# # 位或操作
# np.bitwise_or(a, b)
# # 位反操作 (1变0, 0变1)
# np.bitwise_not(a)
# # 移位操作
# np.left_shift(array, 1)		#每个元素左移1位 (乘2)
# np.right_shift(array, 1)	#每个元素右移1位 (除2)