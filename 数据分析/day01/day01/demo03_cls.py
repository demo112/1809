# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
demo03_cls.py
测试ndarray的自定义复合类型
"""
import numpy as np

data = [
    ('zs', [90, 85, 80], 16),
    ('ls', [91, 81, 81], 17),
    ('ww', [92, 82, 82], 18)]

# 第一种设置dtype的方式
# 3个Unicode字符,3个32位整型组成的列表,整数
a = np.array(data, dtype='U3, 3int32, int32')
print(a)
# 获取a数组中第一个元素的第一个字段的值
print(a[0]['f0'])
print(a[-1]['f1'])

# 第二种设置dtype的方式
b = np.array(data, dtype={
    'names': ['name', 'scores', 'age'],
    'formats': ['U3', '3int32', 'int32']})
print(b)
print(b[0]['scores'])

# 第三种设置dtype的方式
c = np.array(data, dtype=[
    ('name', 'str_', 2),
    ('scores', 'int32', 3),
    ('age', 'int32', 1)])
print(c)
print(c[2]['name'])

# 第四种设置dtype的方式
# 存储数据时，
# name字段占用8字节，从0字节的位置开始输出
# scores字段占用12字节，从16字节的位置开始输出
# 虽然name字段没有把前16个字节充分利用，但是
# 在内存中字段的位置偏移量是一致的，访问
# 效率将会得到提高。
d = np.array(data, dtype={
    'name': ('U2', 0),
    'scores': ('3int32', 16),
    'age': ('int32', 28)})
print(d)
print(d[0]['name'])

# 测试日期类型数组
e = np.array(['2011', '2012-01-01',
              '2013-01-01 01:01:01',
              '2012-02-01'])
f = e.astype('M8[D]')
print(f.dtype, f)
print(f[2] + 1)
