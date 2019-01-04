# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import operator
s = {1, 2, 3}
s.add(4)
print(s)
print(s.update())

L = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def isodd(x):
    return x % 2 == 1


for x in filter(isodd, L):
    print(x)  # 1,3,5,7,9

D = [{"name": '12', "age": 30}, {"name": '12', "age": 25}]
print(id(D))
D.sort(key=lambda x: x["age"], reverse=False)
print(id(D))
print(D)
t = (10, 20, 30, 30, 30, 5)
print(t.count(30))
# 2. s = "Python"，请依次写出语句完成如下输出：
# (1) 生成列表s2 = ['P','y','t','h','o','n']
s = "Python"
s2 = []
for i in s:
    s2.append(i)
print(s2)

s3 = [i for i in s]
print(s3)
# (2) 在s2列表尾部追加元素 "!"
s2.append("!")
print(s2)
# (3) 返回列表s2的长度
print(len(s))
# (4) 删除s2中的元素'!'
s2.pop(-1)  # 索引下标
# s2.remove('!')
print(s2)
# (5) 清空s2列表中的所有元素

del s2[:2]
print(s2)
F = lambda x: x**2
print(F(4))


v = 100


def fun1():
    v = 200
    print("fun1, v=", v)

    def fun2():
        v = 300
        print('fun2.v=', v)
    fun2()
fun1()
print("v is ", v)


def mynum(x):
    if x > 0:
        print(x, "is zheng")
        return x
    else:
        return x
        print(x, "is fu")
# （1）、请写出 print(mynum(1)) 的输出结果
#      1 是整数
print(mynum(1))
# （2）、请写出print(myfun(-1)) 	的输出结果
#      1
# （3）、请简单阐述原因


def myfn():
    def myfn2():
        print('My Python')
    return myfn2()


print(myfn())

print('L=', "*".join(str(i) for i in L))

# 4. 写一个函数myfn(n)，要求： 每隔1秒在屏幕打印"hello world"，共打印n次（要求用递归方法实现）


def myfn(n):
    while True:
        if n == 0:
            break
        print('hello world')
        import time
        time.sleep(1)
        return myfn(n - 1)

myfn(5)

import random
# 码为（大写字母，数字，或者下划线）


def get_pass(num):
    L = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'G', 'K', 'L',
         'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 1, 2, 3, 4, 5]
    return random.sample(L, num)

print(get_pass(8))   # 会生成一个8位的随机密码
print(get_pass(6))

L = [1, 2, 3]
s = [L1, 4, 5]
o = s
r = o.copy()
print(L[1]=10)
print(o[1]=40)
print(r[2]=50)
