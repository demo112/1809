# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np

a = np.arange(1, 10).reshape(3, 3)
print(a)


def func(data):
    print(data, '-----------', sep='\n')

np.apply_along_axis(func, 1, a)
