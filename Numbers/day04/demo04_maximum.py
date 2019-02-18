# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
maximum.py
"""
import numpy as np

a = np.arange(1, 10).reshape(3, 3)
b = np.arange(1, 10)[::-1].reshape(3, 3)
print(np.maximum(a, b))
print(np.minimum(a, b))
