# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pandas as pd
import matplotlib.pyplot as mp
import numpy as np

#"fixed acidity	""volatile acidity""	""citric acid""	""residual sugar"
#  固定酸度           挥发性酸                柠檬酸            剩余糖分

#""chlorides" """free sulfur dioxide""	""total sulfur dioxide""
# 氯化物              游离二氧化硫             总二氧化硫
#"density""	""pH""	""sulphates""	""alcohol""	"""""quality""""""
#"密度                   硫酸盐          酒精            质量


df = pd.read_csv('wind.csv')
print(df.describe())

print(df.head())
# 研究红酒的质量与那些因素有关
