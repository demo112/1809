# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import cv2 as cv

#_________________________________________
original = cv.imread('sunrise.jpg')
cv.imshow('Original', original)
#-----先变成灰度图
gray = cv.cvtColor(original, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)
equalized_gray = cv.equalizeHist(gray)
cv.imshow('equalized_gray', equalized_gray)

#——-------彩色图加强亮度
yuv = cv.cvtColor(original, cv.COLOR_BGR2YUV)
yuv[..., 0] = cv.equalizeHist(yuv[..., 0])
equalized_color = cv.cvtColor(yuv, cv.COLOR_YUV2BGR)
cv.imshow('equalized_color', equalized_color)

cv.waitKey()
