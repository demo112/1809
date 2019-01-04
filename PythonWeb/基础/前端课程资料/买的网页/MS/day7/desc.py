# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import cv2 as cv
import matplotlib.pyplot as mp
#_________________________________________
original = cv.imread('table.jpg')
cv.imshow('Original', original)
#-----角点检测---先变成灰度图
gray = cv.cvtColor(original, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# star特征点检测器
star = cv.xfeatures2d.StarDetector_create()
keypoints = star.detect(gray)
# 特征点描述器
sift = cv.xfeatures2d.SIFT_create()
_, desc = sift.compute(gray, keypoints)


mp.matshow(desc, cmap='gray', fignum="MFCC")
mp.title('desc')
mp.xlabel('Feature')
mp.ylabel('Sample')

mp.tick_params(which='both', top='False', labeltop='False',
               labelbottom='True', labelsize=10)

mp.show()
cv.waitKey()
