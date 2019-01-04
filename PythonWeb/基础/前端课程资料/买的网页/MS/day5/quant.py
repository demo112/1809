# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import scipy.misc as sm
import sklearn.cluster as sc
import matplotlib.pyplot as mp
image1 = sm.imread('lily.jpg', True).astype(np.uint8)  # 加True后变成灰度图
print(image1.shape, image1.dtype)
x = image1.reshape(-1, 1)  # 若按行，1列
model = sc.KMeans(n_clusters=2)
model.fit(x)
y = model.labels_
print(y)
centers = model.cluster_centers_.squeeze()  # squeeze()用于去除多余的维度
print(centers.ravel())  # 降维
print(image1.shape)
image2 = centers[y].reshape(image1.shape)

image3 = centers[y].reshape(image1.shape)
mp.figure('Image_Quantization')
mp.subplot(221)
mp.title('Orange')
mp.axis('off')
mp.imshow(image1, cmap='gray')
mp.tight_layout()
mp.subplot(222)
mp.title('quant')
mp.axis('off')
mp.imshow(image2, cmap='gray')
mp.tight_layout()
mp.subplot(223)
mp.title('quant')
mp.axis('off')
mp.imshow(image3, cmap='gray')
mp.tight_layout()
mp.show()
