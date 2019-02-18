import numpy as np
import matplotlib.pyplot as mp
from mpl_toolkits.mplot3d import axes3d

n = 1000

x = np.random.normal(0, 1, n)
y = np.random.normal(0, 1, n)
z = np.random.normal(0, 1, n)

# d = x ** 2 + y ** 2 + z**2
d = (1 - x / 2 + x ** 5 + y ** 3 + z ** 2) * np.exp(-x ** 2 - y ** 2 - z ** 2)

mp.figure('scatter3d', facecolor='gray')

ax = mp.gca(projection='3d')

ax.scatter(x, y, z, s = 60, alpha=0.5, c=d, cmap='jet_r')

mp.tight_layout()
mp.show()
