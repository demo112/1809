# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import cv2 as cv

#_________________________________________
original = cv.imread('table.jpg')
cv.imshow('Original', original)
#-----角点检测---先变成灰度图
gray = cv.cvtColor(original, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# star特征点检测器
star = cv.xfeatures2d.StarDetector_create()
keypoints = star.detect(gray)
mixture = original.copy()
cv.drawKeypoints(original, keypoints, mixture,
                 flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv.imshow('Mixture', mixture)
cv.waitKey()
