import numpy as np

a = np.array([[1, -2, 1], [0, 2, -8], [-4, 5, 9]])
c = np.array([[0], [8], [-9]])

b = np.linalg.lstsq(a, c)[0]
print(b)
