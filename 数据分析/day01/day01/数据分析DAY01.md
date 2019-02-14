# 数据分析DAY01

## 徐铭 

xuming@tedu.cn  15201603213

## 什么是数据分析？

数据分析是指用适当的统计分析方法对收集来的大量数据进行分析，提取有用的信息形成结论而对结论加以详细研究、概括、总结的过程。

**使用python做数据分析的常用库**

1. numpy		基础数值算法
2. scipy                科学计算
3. matplotlib      数据可视化
4. pandas           序列高级函数

## numpy概述

1. Numerical Python, 数值的python，补充了Python语言所欠缺的数值计算能力。
2. Numpy是其他数据分析及机器学习库的底层库。
3. Numpy完全标准C语言实现，效率充分优化。
4. Numpy开源免费。

### numpy的历史

1. 1995年， Numeric发布（numpy的前身）。  
2. 2001年，Scipy->Numarray，提供多维数组运算。

3. 2005年，Numeric+Numarray -> Numpy
4. 2006年，Numpy脱离Scipy称为独立项目。

### numpy的核心：多维数组

```python
import numpy as np
array = np.array([1,2,3,4,5])
a = array + 10
```

## numpy基础

### ndarray数组

#### 内存中的ndarray对象

**元数据（metadata）**

存储对目标数组的描述信息，如：dim count, dimensions, dtype, data等等。

**实际数据**

完整的数组内容

将实际数据与元数据分开存放，一方面提高了内存空间的使用效率， 另一方面减少对实际数据的访问频率， 提高效率。

Numpy数组是**同质数组**，所有元素的数据类型必须相同。

#### ndarray对象的创建

np.array(任何可以被解释为Numpy数组的逻辑结构)

```python
import numpy as np
array = np.array([1,2,3,4,5])
```

np.arange(起始值(0)， 终止值， 步长(1))	

```python
print(np.arange(0, 10, 1))
print(np.arange(0, 10))
print(np.arange(10))
```

np.zeros(数组元素个数, dtype='类型')

np.ones(数组元素格式, dtype='类型')  

```python
a = np.zeros(10, dtype='int32')
print(a.dtype, a)
a = np.ones(10, dtype='float32')
print(a.dtype, a)
a = np.ones(5, dtype='bool')
print(a.dtype, a)
```

#### ndarray对象属性的基本操作

**数组的维度：**array.shape

```python
a = np.arange(1, 9)
print(a.shape, a)

# 修改数组对象的维度
a.shape = (2, 4)
print(a.shape, a, sep='\n')
a.shape = (2, 2, 2)
print(a.shape, a, sep='\n')
```

**元素的类型：**array.dtype

```python
# 测试元素的类型相关操作
b = np.arange(10)
print(b.dtype, b)
# 把b中的每个元素当做float来看
# 返回新类型的数组
c = b.astype('float32')
print(b.dtype, b)
print(c.dtype, c)
```

**数组元素个数：**array.size

```python
# 测试数组元素的个数
a = np.arange(8).reshape(2, 4)
print(a)
print(a.size)
print(len(a))
```

**数组元素索引（下标）**

```python
# 测试数组索引操作
c = np.arange(1, 28).reshape(3, 3, 3)
print(c)
print(c[0])  # 0页
print(c[0][0])  # 0页 0行
print(c[0][0][0])  # 0页 0行 0列
print(c[0, 0, 0])  # 0页 0行 0列

for i in range(c.shape[0]):
    for j in range(c.shape[1]):
        for k in range(c.shape[2]):
            print(c[i, j, k], end=' ')

```

#### ndarray对象属性操作详解

**Numpy的内部基本数据类型**

| 类型名       | 类型表示符                       |
| ------------ | -------------------------------- |
| 布尔型       | bool_                            |
| 有符号整数型 | int8(-128~127)/int16/int32/int64 |
| 无符号整型   | uint8/uint16/uint32/uint64       |
| 浮点型       | float16/float32/float64          |
| 复数型       | complex64/complex128             |
| 字符串型     | str_ (每个字符32位Unicode编码)   |

**自定义复合类型**

```python
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
```

类型字符码

| 类型              | 字符码                    |
| ----------------- | ------------------------- |
| np.bool_          | ?                         |
| np.int8/16/32/64  | i1/i2/i4/i8               |
| np.uint8/16/32/64 | u1/u2/u4/u8               |
| np.float16/32/64  | f2/f4/f8                  |
| np.complex64/128  | c8/c16                    |
| np.str_           | U<字符数>                 |
| np.datetime64     | M8[Y / M / D / h / m / s] |

**ndarray数组对象维度操作**

**视图变维(数据共享):** reshape()  ravel()

```python
a = np.arange(1, 9)
print(a)
a = a.reshape(2, 4)
print(a)
b = a.reshape(2, 2, 2)
print(b)
a[0, 0] = 999
print(a)
print(b)
b = b.ravel()
print(b)
```

**复制变维(数据独立):** flatten()

```python
# 复制变维 数据独立
c = a.flatten()
print(a)
print(c)
c[0] = 1000
print(a)
print(c)
```

**就地变维:** 使用shape属性直接改变原数组对象的维度，不返回新数组。 resize(2, 2)

```python
# 就地变维
c.shape = (2, 4)
print(c)
c.resize(2, 2, 2)
print(c)
```

**ndarray数组对象的切片操作**

```python
# 数组切片的参数与列表切片基本一致
# step+（步长+）：默认从头向后切
# step-（步长-）：默认从后向前切
array[start:end:step, ...]
```

```python
import numpy as np
a = np.arange(1, 10)
print(a)
print(a[:3])
print(a[3:6])
print(a[6:])
print(a[::-1])
print(a[:-4:-1])
print(a[-4:-7:-1])
print(a[-7::-1])
print(a[::])
print(a[::3])
print(a[1::3])
print(a[2::3])
```

**多维数组的切片操作**

```python
a = a.reshape(3, 3)
print(a)
print(a[:2, :2])
print(a[:, 2])  # 所有行的最后一列
```

**ndarray数组的掩码操作**

```python
import numpy as np

a = np.array([43, 70, 34, 76, 34, 57, 23, 45])
print(a)
b = a >= 60
print(b)
print(a[b])
indices = [1, 7, 6, 5, 4, 3, 2, 0]
print(a[indices])

# 输出100以内3与7的倍数
b = np.arange(100)
mask = (b % 3 == 0) & (b % 7 == 0)
print(b[mask])
```

**多维数组的组合与拆分**

垂直方向的操作：

```python
# 在垂直方向a与b摞起来
np.vstack((a, b))
# 把c数组在垂直方向拆成2个
np.vsplit(c, 2)
```

水平方向的操作：

```python
# 在水平方向a与b并起来
np.hstack((a, b))
# 把c数组在水平方向拆成2个
np.hsplit(c, 2)
```

深度方向的操作：

```python
# 在深度方向a与b并起来
np.dstack((a, b))
# 把c数组在深度方向拆成2个
np.dsplit(c, 2)
```

多维数组组合与拆分的通用方法：

```python
# 实现a与b数组的组合操作
# axis：轴向
# 如果待组合数组都是二维数组
# axis：0 垂直方向组合
# axis：1 水平方向组合
# 如果待组合数组都是三维数组
# axis：0 垂直方向组合
# axis：1 水平方向组合
# axis：2 深度方向组合
np.concatenate((a, b), axis=0)
# 把c数组拆成2分  axis为轴向
np.split(c, 2, axis=0)
```

长度不等的数组的组合：

```python
# 长度不等的数组的组合
a = np.array([1, 2, 3, 4, 5])
b = np.array([6, 7, 8, 9])
# 把b补成5个元素, 头部补0个，尾部补1个，
# 新增元素的默认值为-1
b = np.pad(
    b, pad_width=(3, 1), mode='constant',
    constant_values=-1)
print(b)
```

简单的一维数组的组合方案

```python
# 把a与b两个一维数组摞在一起成两行
np.row_stack((a, b))
# 把a与b两个一维数组组合在一起成两列
np.column_stack((a, b))
```

ndarray对象的其他常用属性

1. ndim		维数（n维数组的n）
2. itemsize         元素所占用字节数
3. nbytes            数组所占用的总字节数
4. real                 复数的实部
5. imag               复数的虚部
6. T                      二维数组的转置数组
7. flat                  多维数组的扁平迭代器













