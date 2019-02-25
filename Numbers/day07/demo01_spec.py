import numpy as np

A = np.array([[1, 6, 5], [9, 7, 3], [1, 5, 6]])
# 已知n阶方阵A, 求特征值与特征向量
# eigvals: 找到的所有特征值数组
# eigvecs: 找到的与特征值对应的特征向量数组
eigvals, eigvecs = np.linalg.eig(A)
print('特征值数组', '\n', eigvals, '\n',
      '特征向量数组', '\n', eigvecs)
eigvals[2:] = 0
S = np.mat(eigvecs) * np.mat(np.diag(eigvals)) * \
    np.mat(eigvecs).I
S = S.real
# 已知特征值与特征向量,逆向求原方阵
print(A)
print(S)
