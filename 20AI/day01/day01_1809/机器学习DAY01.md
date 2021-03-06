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

案例：基于梯度下降理论实现线性回归，求出w<sub>0</sub>  w<sub>1</sub>。

1. 整理训练集数据，自定义梯度下降算法，求出w<sub>0</sub>  w<sub>1</sub>，绘制回归线。

```python
import numpy as np
import matplotlib.pyplot as mp

train_x = np.array([0.5, 0.6, 0.8, 1.1, 1.4])
train_y = np.array([5.0, 5.5, 6.0, 6.8, 7.0])
test_x = np.array([0.45, 0.55, 1.0, 1.3, 1.5])
test_y = np.array([4.8, 5.3, 6.4, 6.9, 7.3])
# 基于梯度下降理论，完成线性回归，求w0与w1
times = 1000  # 梯度下降次数
lrate = 0.01  # 每次梯度下降参数的变化率
epoches = []  # 记录每次梯度下降的索引
w0, w1, losses = [1], [1], []  # 参数
# 做1000次梯度下降
for i in range(1, times + 1):
    epoches.append(i)
    loss = ((w0[-1] + w1[-1] * train_x
             - train_y)**2).sum() / 2
    losses.append(loss)
    # 使用偏导数取出w0与w1梯度下降值
    d0 = ((w0[-1] + w1[-1] * train_x)
          - train_y).sum()
    d1 = ((w0[-1] + w1[-1] * train_x - train_y)
          * train_x).sum()
    print('{: 4} > w0={: .8f}, w1={: .8f}, \
          loss={: .8f}'.format(
        epoches[-1], w0[-1], w1[-1],
        losses[-1]))
    # w0, w1梯度下降：
    w0.append(w0[-1] - lrate * d0)
    w1.append(w1[-1] - lrate * d1)

mp.figure('Linear Regression')
mp.title('Linear Regression', fontsize=18)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.scatter(train_x, train_y, marker='s',
           c='dodgerblue', alpha=0.5, s=80,
           label='Training Points')

# 通过w0与w1，绘制回归线
pred_train_y = w1[-1] * train_x + w0[-1]
mp.plot(train_x, pred_train_y,
        color='orangered', linewidth=2,
        label='Regression Line')

mp.legend()
mp.show()
```

2. 绘制每次梯度下降过程中w<sub>0</sub>  w<sub>1</sub> loss值的变化。

```python
# 绘制每次梯度下降过程中w0 w1 loss值的变化。
mp.figure('Training Progress')
mp.subplot(311)
mp.title('Training Progress', fontsize=16)
mp.ylabel('w0', fontsize=14)
mp.tick_params(labelsize=12)
mp.grid(linestyle=":")
mp.plot(epoches, w0[1:], label='w0')
mp.legend()
mp.subplot(312)
mp.title('Training Progress', fontsize=16)
mp.ylabel('w1', fontsize=14)
mp.tick_params(labelsize=12)
mp.grid(linestyle=":")
mp.plot(epoches, w1[1:], label='w1')
mp.legend()
mp.subplot(313)
mp.title('Training Progress', fontsize=16)
mp.ylabel('loss', fontsize=14)
mp.tick_params(labelsize=12)
mp.grid(linestyle=":")
mp.plot(epoches, losses, label='loss')
mp.legend()
mp.tight_layout()
```

3. 基于三维曲面绘制梯度下降过程中的每一个空间点。

```python
import mpl_toolkits.mplot3d as axes3d

# 绘制空间曲面，观察梯度下降过程
grid_w0, grid_w1 = np.meshgrid(
    np.linspace(0, 9, 500),
    np.linspace(0, 3.5, 500))
# 构建一个数组，结构与grid_w0一致，元素全是0
grid_loss = np.zeros_like(grid_w0)
for x, y in zip(train_x, train_y):
    grid_loss += \
        (grid_w0 + x * grid_w1 - y)**2 / 2
# 绘制曲面
mp.figure("Loss Function")
ax = mp.gca(projection='3d')
mp.title('Loss Function')
ax.set_xlabel('w0', fontsize=12)
ax.set_ylabel('w1', fontsize=12)
ax.set_zlabel('loss', fontsize=12)
ax.plot_surface(
    grid_w0, grid_w1, grid_loss,
    rstride=10, cstride=10, cmap='jet')
ax.plot(w0[:-1], w1[:-1], losses,
        'o-', color='orangered')
```

4. 以等高线的方式绘制梯度下降的过程。

```python
# 以等高线的方式绘制梯度下降的过程。
mp.figure('Contour')
mp.xlabel('w0', fontsize=14)
mp.ylabel('w1', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.contourf(grid_w0, grid_w1, grid_loss,
            10, cmap='jet')
cntr = mp.contour(grid_w0, grid_w1, grid_loss,
                  10, colors='black',
                  linewidths=0.5)
mp.clabel(cntr, inline_spacing=0.1,
          fmt='%.2f', fontsize=8)
mp.plot(w0, w1, 'o-', c='orangered',
        label='BGD')
mp.legend()
```

#### 线性回归模型

sklearn提供了线性回归相关的API：

```python
import sklearn.linear_model as lm
# 创建线性回归模型
model = lm.LinearRegression()
# 模型训练
# 输入：一个二维数组表示的样本矩阵
# 输出：每个样本最终的结果
model.fit(输入，输出)
# 模型预测  给出与训练时格式相同的输入， 返回预测输出
result = model.predict(测试输入)
```

案例：基于线性回归训练single.txt中的样本，使用模型预测样本。

```python
import numpy as np
import matplotlib.pyplot as mp
import sklearn.linear_model as lm

# 读取数据
x, y = np.loadtxt(
    '../ml_data/single.txt', delimiter=',',
    usecols=(0, 1),  unpack=True)
x = x.reshape(-1, 1)  # x变为n行1列
# 创建模型->训练模型->使用模型
model = lm.LinearRegression()
model.fit(x, y)
pred_y = model.predict(x)
# 把这些点画出来
mp.figure('Linear Regression', facecolor='lightgray')
mp.title('Linear Regression', fontsize=14)
mp.xlabel('x', fontsize=12)
mp.ylabel('y', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=":")
mp.scatter(x, y, c='dodgerblue', alpha=0.5,
           s=60, label='Sample Points')
mp.plot(x, pred_y, c='orangered',
        linewidth=3, label='Regression Line')
mp.legend()
mp.show()
```

#### 评估训练结果的误差

线性回归模型训练完毕后，可以利用测试集评估训练结果误差。sklearn.metrics 提供了计算模型误差的几个常用算法：

```python
import sklearn.metrics as sm

# 平均绝对值误差:  1/m*∑|实际输出-预测输出|
sm.mean_absolute_error(y， pred_y)
# 平均平方误差:  sqrt(1/m*∑(实际输出-预测输出)^2)
sm.mean_squared_error(y, pred_y)
# 中位数绝对值误差: median(|实际输出-预测输出|)
sm.median_absolute_error(y, pred_y)
# R2得分 (0, 1]区间上的分值，分数越高，模型越好, 误差越小
sm.r2_score(y, pred_y)
```

案例：

```python
# 输出误差指标
print(sm.mean_absolute_error(y, pred_y))
print(sm.mean_squared_error(y, pred_y))
print(sm.median_absolute_error(y, pred_y))
print(sm.r2_score(y, pred_y))
```

#### 模型的保存与加载

模型训练是一个耗时的过程，一个优秀的机器学习模型是很宝贵的。可以把模型保存到磁盘中，也可以在需要的时候从磁盘中重新加载模型。不需要重新训练。

模型保存和加载相关的API：

```python
import pickle
pickle.dump(内存对象, 磁盘文件)  # 保存模型
model = pickle.load(磁盘文件) # 加载模型
```

案例：把训练好的模型保存到磁盘中，在合适的时间读取模型对象。

```python
# 保存模型
with open('../ml_data/linear.pkl', 'wb') as f:
    pickle.dump(model, f)

# 加载模型
with open('../ml_data/linear.pkl', 'rb') as f:
    model = pickle.load(f)
pred_y = model.predict(x)
```

### 岭回归

普通线性回归模型使用基于梯度下降的最小二乘法，在损失函数最小化的前提下，寻找最优的模型参数。在此过程中，包括**少数异常样本**在内的全部训练数据会对模型参数造成相当程度的一些影响，而异常样本无法在训练过程中被识别出来。为此，岭回归在模型迭代过程中增加了**正则项**，以限制模型参数对异常样本的匹配程度。进而提高模型对多数正常样本的拟合精度。

岭回归相关API：

```python
import sklearn.linear_model as lm
# 正则强度: 该数字越大，越忽略异常样本
# fit_intercept: 是否训练截距 
# max_iter: 最大迭代次数
m = lm.Ridge(正则强度, fit_intercept=True, max_iter=1000)
# 训练模型
m.fit(输入， 输出)
# 使用模型
pred_y = m.predict(test_x)
```

案例：加载abnormal.txt 

```python
# 使用岭回归
model = lm.Ridge(150, fit_intercept=True,
                 max_iter=10000)
model.fit(x, y)
pred_y = model.predict(x)
print(sm.r2_score(y, pred_y))
mp.plot(x, pred_y, c='limegreen',
        linewidth=3, label='Ridge Regression')
```

### 多项式回归

若希望回归模型更好的拟合训练样本的数据，可以用多项式回归器。

**一元多项式回归**
$$
y = w_0  + w_1x + w_2x^2 + w_3x^3 + ... + w_dx^d
$$
将高次项看做对1次项的扩展:
$$
y = w_0  + w_1x_1 + w_2x_2 + w_3x_3 + ... + w_dx_d
$$
那么一元多项式回归即可以看做为多元线性回归。可以直接使用LinearRegression模型对样本数据进行模型训练。

所以一元多项式回归的实现需要两个步骤：

1. 将一元多项式回归问题转换为多元线性回归问题（只需给出高次数）
2. 将1步骤得到的多项式结果中w<sub>1</sub> w<sub>2</sub> .. 当做样本特征，交给线性回归器训练多元线性模型。

使用sklearn提供的**数据管线**实现两个步骤的顺序执行：

```python
import sklearn.pipeline as pl
import sklearn.preprocessing as sp
import sklearn.linear_model as lm
# 该管线将会组织两个步骤，首先使用多项式特征扩展器扩展出多项式，
# 而后把数据交给线性回归器训练多元线性模型。
model = pl.make_pipeline(
	sp.PolynomialFeatures(5), # 多项式特征扩展器
    lm.LinearRegression()	  # 线性回归器	
)
```

案例：

```python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
demo06_poly.py 多项式回归 single.txt
"""
import numpy as np
import matplotlib.pyplot as mp
import sklearn.linear_model as lm
import sklearn.preprocessing as sp
import sklearn.metrics as sm
import sklearn.pipeline as pl

# 读取数据
x, y = np.loadtxt(
    '../ml_data/single.txt', delimiter=',',
    usecols=(0, 1),  unpack=True)
x = x.reshape(-1, 1)  # x变为n行1列

# 创建管线
model = pl.make_pipeline(
    sp.PolynomialFeatures(6),  # 多项式特征扩展
    lm.LinearRegression()  # 线性回归器
)
model.fit(x, y)
pred_y = model.predict(x)
print(sm.r2_score(y, pred_y))

# 把这些点画出来
mp.figure('Linear Regression', facecolor='lightgray')
mp.title('Linear Regression', fontsize=14)
mp.xlabel('x', fontsize=12)
mp.ylabel('y', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=":")
mp.scatter(x, y, c='dodgerblue', alpha=0.5,
           s=60, label='Sample Points')
# 绘制多项式曲线
x = np.linspace(x.min(), x.max(), 1000)
x = x.reshape(-1, 1)
y = model.predict(x)
mp.plot(x, y, color='orangered',
        linewidth=2, label='PolyFit Line')
mp.legend()
mp.show()
```

过于简单的模型，无论对于训练数据还是测试数据都无法给出足够高的预测精度，这种现象叫做欠拟合。

过于复杂的模型，对于训练数据可以得到较高的预测精度，但是对于预测数据通常精度较低。这种现象叫做过拟合。

一个性能可以接收的学习模型，应该对训练数据和测试数据都有接近的预测精度，而且精度不能太低。

### 决策树

**基本算法原理**

核心思想：相似的输入必会产生相似的输出。比如预测薪资：

年龄：1-青年， 2-中年， 3 -老年

学历：1-本科， 2-硕士，3-博士

经验：1-出道，2-一般，3-老手， 4-骨灰

性别：1-男性，2-女性

| 年龄 | 学历 | 工作经验 | 性别 | ==>  | 薪资  |
| ---- | ---- | -------- | ---- | ---- | ----- |
| 1    | 1    | 1        | 1    | ==>  | 6000  |
| 2    | 1    | 3        | 1    | ==>  | 10000 |
| 3    | 3    | 4        | 1    | ==>  | 50000 |
| ...  | ...  | ...      | ...  | ...  | ...   |
| 1    | 2    | 2        | 1    | ==>  | ?     |

为了提高搜索效率，使用树形数据结构处理样本数据：
$$
年龄1\left\{
\begin{aligned}
学历1 \\
学历2 \\
学历3 \\
\end{aligned}
\right.
\quad\quad
年龄2\left\{
\begin{aligned}
学历1 \\
学历2 \\
学历3 \\
\end{aligned}
\right.
\quad\quad
年龄3\left\{
\begin{aligned}
学历1 \\
学历2 \\
学历3 \\
\end{aligned}
\right.
$$
首先从训练样本矩阵中选择第一个特征正进行子表划分，使每个子表中该特征的值全部相同。然后在每个子表中选择下一个特征按照同样的规则继续划分更小的子表，不断重复，直到所有的特征全部使用完为止。

此时便得到了叶级子表，其中所有样本的特征值全部相同。对于待预测样本，根据其每一个特征的值，选择对应的子表，逐一匹配，直到找到域值完全匹配的叶级子表，利用该子表中样本的输出，通过平均（回归问题）或投票（分类问题）为待预测样本提供预测输出。

随着子表的划分，信息熵（信息的混乱度）将会越来越小，信息越来越纯，数据越来越精准。

决策树回归器模型相关API：

```python
import sklearn.tree as st
# 创建决策树回归器模型
# max_depth: 树的最大深度
model = st.DecisionTreeRegressor(max_depth=4)
# 训练模型
model.fit(train_x, train_y)
# 使用模型
pred_y=model.predict(test_x)
```

案例：预测波士顿地区房屋价格。

```python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
demo07_dt.py 决策树预测房屋价格
"""
import sklearn.datasets as sd
import sklearn.utils as su
import sklearn.tree as st
import sklearn.metrics as sm

boston = sd.load_boston()
print(boston.data.shape)  # 数据量
print(boston.target.shape)
print(boston.feature_names)  # 13个特征名

# 打乱原始输入、输出数据集
x, y = su.shuffle(
    boston.data, boston.target, random_state=7)
# 划分测试集、训练集
train_size = int(len(x) * 0.8)
train_x, train_y, test_x, test_y = \
    x[:train_size], y[:train_size], \
    x[train_size:], y[train_size:]

# 创建模型， 使用训练集数据进行训练
model = st.DecisionTreeRegressor(max_depth=10)
model.fit(train_x, train_y)
# 测试集数据预测
pred_test_y = model.predict(test_x)
# 输出R2得分
print(sm.r2_score(test_y, pred_test_y))
```

#### 集合算法

根据多个不同模型给出的预测结果，利用平均（回归问题）或者投票（分类问题）的方法，得出最终预测的结果。

基于决策树的集合算法，就是按照某种规则构建多颗彼此不同的决策树模型，分别给出针对未知样本的预测结果，最后通过平均或投票的方式得到相对综合的结论。

**正向激励**

首先为样本矩阵中的每行样本随机分配初始权重，由此构建一棵带有权重的决策树。在使用该决策树提供预测输出时，通过加权平均或加权投票的方式产生预测值。将训练样本代入模型，预测输出，对那些预测失败的样本，提高其权重，由此形成第二棵树。重复以上过程，构建出不同权重的n棵树。

正向激励相关API：

```python
import sklearn.tree as st
import sklearn.ensemble as se
# 普通决策树模型
model = st.DecisionTreeRegressor(max_depth=4)
# 使用正向激励集合算法构建400棵树
model = se.AdaBoostRegressor(
    model, 	# 基础模型
    n_estimators=400,  # 决策树的数量
	random_state=7	# 随机种子
)
model.fit(train_x, train_y)
test_y = model.predict(test_x)
```

案例：

































