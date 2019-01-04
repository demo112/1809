# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import cv2 as cv

#_________________________________________
original = cv.imread('chair.jpg')
cv.imshow('Original', original)

canny = cv.Canny(original, 50, 240)  # 亮度梯度，把外轮廓线显示出来
cv.imshow('Canny', canny)

cv.waitKey()
