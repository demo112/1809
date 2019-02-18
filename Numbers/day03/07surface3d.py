
import numpy as np
import matplotlib.pyplot as mp
from mpl_toolkits.mplot3d import axes3d

n = 2000

x, y = np.meshgrid(
    np.linspace(-3, 3, n),
    np.linspace(-3, 3, n),
)
# 通过x与y编坐标高度
z = (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2  - y ** 2)

mp.figure('surface', facecolor='gray')
mp.title('wireframe', fontsize=19)
ax = mp.gca(projection='3d')
ax.set_xlabel('x', fontsize=14)
ax.set_ylabel('y', fontsize=14)
ax.set_zlabel('z', fontsize=14)
ax.plot_surface(x, y, z, rstride=10, cstride=10, cmap='jet')

mp.tight_layout()
mp.show()
