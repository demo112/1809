import pandas as pd
import numpy as np

# 创建一组Series数据
# 1.创建Series
s1 = pd.Series([90, 86, 70], index=['leo', 'kate', 'john'])
print(s1)
print('-' * 40)
dict = {'leo': 90, 'kate': 86, 'john': 70}
s1 = pd.Series(dict)

print(s1)
print('-' * 40)

# 绝对位置查找
print(s1[0])
print('-' * 40)

# 标签查找
print(s1['kate'])
print('-' * 40)

# 列表查找
print(s1[['john', 'kate']])
print('-' * 40)

# 表达式查找
a = s1 > 80
print(s1[a])
print('-' * 40)

# 2.numpy中的ndarray：
s2 = pd.Series(np.random.randn(5), index=list('ABCDE'))
print(s2)
print('-' * 40)

# 3.数字创建
s3 = pd.Series(6)
print(s3)
print('数字创建', '-' * 40)

# 4.创建一组DataFrame数据-date_range创建时间
date = pd.date_range('20100101', periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=date, columns=list('abcd'))
print('-' * 40)

print(df)
print(df.index)
print(df.values)

# 读取单列。多列
print(df.a)
print(df['a'])
print(df[['a', 'b']])

# 读取多行，单行
print(df[0:4])
print(df.head(3))
print(df.tail(3))

print(df.loc['2010-01-01':'2010-01-04', ['a', 'b']])
print(df.iloc[:4, [0, 1]])
print(df.ix[:4, ['a', 'b']])
print(df.loc[df.index < '20100104', ['a', 'b']])
