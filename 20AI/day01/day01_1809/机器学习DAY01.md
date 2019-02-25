# 机器学习DAY01

## 机器学习

### 机器学习概述

#### 什么是机器学习

机器学习是一门能够让编程计算机从数据中学习的计算机科学。

一个计算机程序在完成任务T之后，获得经验E，其表现效果为P，如果任务T的性能表现（P），随着E增加而增加，那么这样的计算机程序就被称为机器学习系统。拥有自我完善，自我增进，自我适应的特点。

#### 为什么需要机器学习

* 自动化的升级和维护
* 解决那些算法过于复杂，甚至根本就没有算法的问题
* 在机器学习的过程中协助人类对事物进行深刻理解

#### 机器学习的问题

1. 建模问题

   所谓机器学习，形式上可以这么理解：在数据中通过统计或推理的方法，寻找一个接收特定输入x，并给出预期输出y的功能函数f(x).

2. 评估问题

   针对已知输入，函数给出的输出（预测值）与实际输出（目标值）之间存在一定的误差，因此需要构建一个评估体系，根据误差的大小判定函数的优劣。

3. 优化问题

   学习的核心在于改善自身的性能，通过数据对算法的反复锤炼，不断提升函数预测的准确性，直到获得能够满足实际需求的最优解决方案。

#### 机器学习的种类

**监督学习、无监督学习、半监督学习、强化学习**

1. 监督学习：用已知的输出评估模型的性能，引导模型优化。
2. 无监督学习：在没有已知输出的情况下，仅仅根据输入信息的相关性，进行类别的划分。
3. 半监督学习：先通过无监督学习划分类别，再根据人工标记，通过有监督学习预测输出。
4. 强化学习：通过对不同决策结果的奖励和惩罚，使机器学习系统经过长时间训练以后，越来越倾向于给出接近期望结果的输出。

**批量学习和增量学习**

1. 批量学习：将学习的过程和应用的过程分开，用全部的训练数据训练模型，然后在应用场景中实现预测，当预测结果不够理想时，重新回到学习过程，如此循环。
2. 增量学习：将学习的过程和应用的而过程统一起来，在应用的同时以增量的方式不断学习新的内容，边训练变预测，边预测边训练。

**基于实例的学习和基于模型的学习**

1. 基于实例的学习：以历史数据作为经验，寻找与待预测输入最接近的样本，以其输出作为预测结果。
2. 基于模型的学习：以历史数据作为经验，建立联系输入与输出的某种数学模型，将待预测输入代入该模型，预测结果。

#### 机器学习的一般过程

**数据清理**

1. 数据收集（数据检索、数据挖掘、爬虫）
2. 数据清洗

**机器学习**

1. 选择模型（算法）
2. 训练模型（算法）
3. 评估模型（工具、框架、算法）
4. 测试模型

**业务运维**

1. 应用模型
2. 维护模型

#### 机器学习的典型应用

股价预测、推荐引擎、自然语言识别（NLP）、语音、图像、人脸识别等。

#### 机器学习的基本问题

1. 回归问题：根据已知的输入和输出寻找某种性能最佳的模型，将未知输出的输入代入模型，得到**连续的输出**。
2. 分类问题：根据已知的输入和输出寻找某种性能最佳的模型，将未知输出的输入代入模型，得到**离散的输出**。
3. 聚类问题：根据已知输入的相似程度，将其划分成不同的群落。
4. 升维、降维问题：在性能损失尽可能小的情况下，实现模型业务。

### 数据预处理

**数据样本矩阵格式**

| 年龄 | 学历 | 经验 | 性别 | 月薪  |
| ---- | ---- | ---- | ---- | ----- |
| 27   | 硕士 | 2    | 女   | 12000 |
| 24   | 本科 | 1    | 男   | 8000  |
| ...  | ...  | ...  | ...  | ...   |

一行一样本，一列一特征。

**数据预处理相关库**

```python
# sklearn是解决机器学习问题的科学计算工具包
# preprocessing用于数据预处理操作
import sklearn.preprocessing as sp
```

#### 均值移除(标准化)

由于一个样本的不同特征值差异较大，不利于使用现有机器学习算法进行样本处理。所以可以使用**均值移除**让样本矩阵中每组特征值的平均值为0，标准差为1。

如何使样本矩阵中每组特征平均值为0？

```
年龄： 17  20  23
mean(年龄) = 20
a = -3
b = 0 
c = 3
```

如何使样本矩阵中每组特征标准差为1？

```
a = -3
b = 0 
c = 3
s = std(a, b, c)
结果：[a/s, b/s, c/s]
```

sklearn提供了均值移除的相关API：

```python
import sklearn.preprocessing as sp
A = sp.scale(array)
```

案例：

```python
import numpy as np
import sklearn.preprocessing as sp

raw_samples = np.array([
    [17., 100., 4000.],
    [20., 80., 5000.],
    [23., 75., 5500.]])

std_samples = sp.scale(raw_samples)
print(std_samples)
# 输出每一列的均值与标准差
print(std_samples.mean(axis=0))
print(std_samples.std(axis=0))
```

#### 范围缩放

将样本矩阵中的每一列的最小值与最大值设定为相同的区间，统一各列特征值的范围。一般情况下会把特征值缩放至[0,1]区间。

如何使一组特征值的最小值为0呢？

```
原特征： [17, 20, 23]
每个元素减去特征值的最小值： [0, 3, 6]
```

如何使一组特征值的最大值为1呢？

```
[0, 3, 6]
把特征值数组每个元素除以最大值： [0, 0.5, 1]
```

sklearn提供的范围缩放相关API：

```python
# 获取MinMax范围缩放器， 定义缩放范围[0, 1]
mms = sp.MinMaxScaler(feature_range=(0, 1))
# 返回缩放结果
result = mms.fit_transform(原始样本矩阵)
```

案例：

```python
import numpy as np
import sklearn.preprocessing as sp

raw_samples = np.array([
    [17., 100., 4000.],
    [20., 80., 5000.],
    [23., 75., 5500.]])

print(raw_samples)
# 执行范围缩放
mms = sp.MinMaxScaler(feature_range=(0, 1))
result = mms.fit_transform(raw_samples)
print(result)
```

该范围缩放过程也可以这么理解：

当x=17时，y=0； 当x=23时，y=1；问：当x=20时，y=几？
$$
\left[\begin{matrix}
17 & 1 \\
23 & 1 \\
\end{matrix}\right]
\times
\left[\begin{matrix}
k \\
b \\
\end{matrix}\right]
=
\left[\begin{matrix}
0 \\
1 \\
\end{matrix}\right]
$$

```python
# 使用解方程的方式求解k与b，实现线性范围缩放
mms_samples = raw_samples.copy()
for col in mms_samples.T:
    col_min = col.min()
    col_max = col.max()
    a = np.array([[col_min, 1],
                  [col_max, 1]])
    b = np.array([0, 1])
    x = np.linalg.solve(a, b)
    # 计算 kx + b
    col = col * x[0]
    col += x[1]
print(mms_samples)
```

#### 归一化

有些情况每个样本的每个特征值具体是多少并不重要，但是每个样本特征值的占比更加重要。

|      | Python | Java | PHP  |
| ---- | ------ | ---- | ---- |
| 2017 | 10     | 20   | 5    |
| 2018 | 8      | 5    | 0    |
| ...  | ...    | ...  | ...  |

归一化即是用每个样本的每个特征值除以该样本各个特征值绝对值的总和。变换后样本矩阵，每个样本的特征值绝对值之和为1。

sklearn提供的归一化相关API：

```python
# array：原始样本矩阵
# norm：范数
#	l1：l1范数，这组数据每个元素绝对值之和为1
#   l2：l2范数，这组数据每个元素平方之和为1
sp.normalize(array, norm='l1')
```

案例：

```python
import numpy as np
import sklearn.preprocessing as sp

raw_samples = np.array([
    [17., 100., 4000.],
    [20., 80., 5000.],
    [23., 75., 5500.]])

print(raw_samples)
# 归一化处理
nor_samps = sp.normalize(raw_samples, norm='l1')
print(nor_samps)
print(abs(nor_samps).sum(axis=1))

# 自己算：
nor_samps = raw_samples.copy()
for row in nor_samps:
    row /= abs(row).sum()
print(nor_samps)
print(abs(nor_samps).sum(axis=1))
```

#### 二值化

有些业务并不需要分析矩阵的详细完整数据（比如图像边缘识别只需要分析图像边缘即可），可以根据一个事先给定的阈值，用0和1对特征值进行转换，分别表示不高于或高于阈值。二值化后的数组中每个元素非0即1，达到简化数学模型的目的。

sklearn提供二值化相关API：

```python
# 给出阈值，获取二值化器
bin = sp.Binarizer(threshold=阈值)
# 对原始样本矩阵执行二值化预处理操作
result = bin.transform(原始样本矩阵)
```

案例：

```python
import numpy as np
import sklearn.preprocessing as sp

raw_samples = np.array([
    [17., 100., 4000.],
    [20., 80., 5000.],
    [23., 75., 5500.]])

print(raw_samples)
# 二值化处理
bin = sp.Binarizer(threshold=80)
bin_samples = bin.transform(raw_samples)
print(bin_samples)
# 自己做：
bin_samples = raw_samples.copy()
bin_samples[bin_samples <= 80] = 0
bin_samples[bin_samples > 80] = 1
print(bin_samples)
```

#### 独热编码

为样本特征的每个值建立一个由一个1与若干个0组成的序列，用该序列对所有的特征值进行编码。

```
2个数	  3个数	4个数
1		3		2
7		5		4
1		8		6
7		3		9
为每一个数组进行编码：
1-10    3-100	2-1000
7-01	5-010	4-0100
		8-001	6-0010
				9-0001
编码完毕后得到的最终样本矩阵：
101001000
010100100
100010010
011000001
```

独热编码相关的API：

```python
# 创建独热编码器对象
# sparse：是否采用紧缩格式
# dtype:数据类型
ohe=sp.OneHotEncoder(sparse=是否采用紧缩格式，dtype=数据类型)
# 对原始样本矩阵进行处理，返回度热编码后的样本矩阵
result=ohe.fit_transform(原始样本矩阵)
```

```python
# 获取ohe的编码字典
ohe_dict = ohe.fit(raw_samples)
ohe_samples = ohe_dict.transform(raw_samples)
print(ohe_samples)
```

案例：

```python
import numpy as np
import sklearn.preprocessing as sp

raw_samples = np.array([
    [17., 100., 4000.],
    [20., 80., 5000.],
    [23., 75., 5500.]])

print(raw_samples)
# 独热编码
ohe = sp.OneHotEncoder(sparse=False, dtype=int)
ohe_samples = ohe.fit_transform(raw_samples)
print(ohe_samples)
# 获取ohe的编码字典
ohe_dict = ohe.fit(raw_samples)
ohe_samples = ohe_dict.transform(raw_samples)
print(ohe_samples)
```

#### 标签编码

根据字符串形式的特征值在特征序列中的位置，为其制定一个数字标签，用于提供给基于数值算法的学习模型。

标签编码相关的API：

```python
# 获取标签编码器
lbe = sp.LabelEncoder()
# 对原始样本矩阵执行标签编码，返回编码完毕后的结果
result = lbe.fit_transform(原始样本矩阵)
# 给出编码矩阵，反向逆推出原始样本矩阵
samples = lbe.inverse_transform(result)
```

案例：

```python
import numpy as np
import sklearn.preprocessing as sp

raw_samples = np.array([
    'audi', 'ford', 'audi', 'toyota',
    'ford', 'bmw', 'toyota', 'byd',
    'audi'])
# 执行标签编码
lbe = sp.LabelEncoder()
lbe_samples = lbe.fit_transform(raw_samples)
print(lbe_samples)

inv_sampls = lbe.inverse_transform(lbe_samples)
print(inv_sampls)
```

### 线性回归

线性回归的本质为针对符合线性数学模型的一组数据，可以找到一个线性方程拟合样本数据。从而当给出自变量后，通过线性方程实现预测输出的目的。

```
输入	   输出
0.5		5.0
0.6		5.5
0.8		6.0
1.1		6.8
1.4		7.0
....
y = kx + b
```

预测函数： y = w<sub>0</sub> + w<sub>1</sub>x

x： 输入   

y： 输出

 w<sub>0</sub>  w<sub>1</sub>: 模型参数

**所谓模型的训练，就是根据已知的x与y，找到最佳的模型参数 w<sub>0</sub>  w<sub>1</sub>，使得尽可能的精确描述所有输出和输出的关系（误差最小）。**

**单样本误差：**

根据预测函数求出输入为x时的预测值： y' = w<sub>0</sub> + w<sub>1</sub>x。

单样本误差则为：1/2  (y' - y)<sup>2</sup>

**总样本误差：** 

把所有单样本误差相加即是总样本误差： 1/2 &Sigma; (y' - y)<sup>2</sup>

**损失函数：**

loss =  1/2 &Sigma; (w<sub>0</sub> + w<sub>1</sub>x - y)<sup>2</sup>

所以最终的结果即是需要找到一组w<sub>0</sub>  w<sub>1</sub>使得loss函数值最小。















