import numpy as np
import math as m


def foo(x, y):
    return m.sqrt(x ** 2 + y ** 2)


x, y = 3, 4
print(foo(x, y))
# z = foo(x, y)  错误
x = np.array([3, 4, 5, 6])
y = np.array([4, 5, 6, 7])
# 把foo函数矢量化处理
foo_v = np.vectorize(foo)
print(foo_v(x, y))

# 使用from_pyfunc方法矢量化函数
# foo需要2个参数, 最终将会有1个返回值
foo_f = np.frompyfunc(foo, 2, 1)
print(foo_f(x, y))
