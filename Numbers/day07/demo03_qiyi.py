# -*- coding: utf-8 -*-
from __future__ import unicode_literals
'''
qiyi.py 奇异值分解
'''
import numpy as np
import matplotlib.pyplot as mp
import scipy.misc as sm

# 使用sm的方法读取一张图片 得到图片像素矩阵
# True  黑白亮度矩阵
# False 完整图像
img = sm.imread('lily.jpg', True)
# 设置图像精度
n = 50
# 提取图片的特征值与特征向量
eigvals, eigvecs = np.linalg.eig(img)
#print(eigvals.shape, eigvecs.shape)
eigvals[n:] = 0
img2 = np.mat(eigvecs) *  \
    np.mat(np.diag(eigvals)) * \
    np.mat(eigvecs).I
img2 = img2.real

# 奇异值分解
# todo 正交矩阵怎么来的
print(img.dtype)
U, sv, V = np.linalg.svd(img, full_matrices=False)
sv[n - 25:] = 0
img3 = U * np.mat(np.diag(sv)) * V
print(U)
print(V)

mp.figure('Lily', facecolor='lightgray')
mp.subplot(2, 2, 1)
mp.xticks([])
mp.yticks([])
mp.imshow(img, cmap='gray')
mp.tight_layout()

mp.subplot(2, 2, 2)
mp.xticks([])
mp.yticks([])
mp.imshow(img2, cmap='gray')
mp.tight_layout()

mp.subplot(2, 2, 3)
mp.xticks([])
mp.yticks([])
mp.imshow(img3, cmap='gray')
mp.tight_layout()

mp.show()
