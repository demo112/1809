# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import cv2 as cv
import numpy as np
#_________________________________________
original = cv.imread('forest.jpg')
cv.imshow('Original', original)

#__________________________________________
blue = np.zeros_like(original)
blue[..., 0] = original[..., 0]  # 0,1,2 蓝绿红
cv.imshow('blue', blue)


green = np.zeros_like(original)
green[..., 1] = original[..., 1]  # 0,1,2 蓝绿红
cv.imshow('green ', green)


red = np.zeros_like(original)
red[..., 2] = original[..., 2]  # 0,1,2 蓝绿红
cv.imshow('red ', red)

h, w = original.shape[:2]
l, t = int(w / 4), int(h / 4)
r, b = int(w * 3 / 4), int(h * 3 / 4)

cropped = original[t:b, l:r]
cv.imshow('Cropped', cropped)

# 缩放
# scaled = cv.resize(original, (int(w / 2), int(h / 2)))
scaled = cv.resize(original, None, fx=0.5, fy=0.5)
cv.imshow('scaled', scaled)

cv.imwrite('blue.jpg', blue)
cv.imwrite('Cropped.jpg', cropped)
cv.imwrite('scaled.jpg', scaled)
cv.waitKey()
