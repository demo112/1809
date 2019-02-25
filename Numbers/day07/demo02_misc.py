import numpy as np
import matplotlib.pyplot as mp
import scipy.misc as sm
import matplotlib.animation as ma

# 使用sm的方法读取一张图片 得到图片像素矩阵
# True  黑白亮度矩阵
# False 完整图像

img = sm.imread('lily.jpg', True)
# 提取图片的特征值与特征向量
eigvals, eigvecs = np.linalg.eig(img)
print(eigvals, eigvecs)
print(eigvals.shape, eigvecs.shape)

# todo 以此结合动画实现图像渐渐清晰


# mp.figure('Lily', facecolor='lightgray')
# mp.subplot(1, 2, 1)
# mp.xticks([])
# mp.yticks([])
# mp.imshow(img, cmap='gray')
# mp.tight_layout()

m = 0
mp.subplot(1, 2, 2)
mp.xticks([])
mp.yticks([])
mp.tight_layout()

def generator():
    global m
    eigvals[m:] = 0
    print(m)
    # print(eigvals.size)
    nimg = np.mat(eigvecs) * \
           np.mat(np.diag(eigvals)) * \
           np.mat(eigvecs).I
    # 只取实部
    nimg = nimg.real
    if m >= 512:
        yield nimg
    else:
        yield nimg
        m += 10


def update(data):
    mp.imshow(data, cmap='gray')


anim = ma.FuncAnimation(mp.gcf(), update, generator, interval=500)
mp.show()
