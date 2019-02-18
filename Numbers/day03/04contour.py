
import numpy as np
import matplotlib.pyplot as mp

mp.figure('Contour', facecolor='gray')
mp.title('contour', fontsize=19)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=12)
mp.grid(linestyle=':')

n = 10000

x, y = np.meshgrid(
    np.linspace(-3, 3, n),
    np.linspace(-3, 3, n),
)

# 通过x与y编坐标高度

z = (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2  - y ** 2)

cntr = mp.contour(x, y, z, 8, colors='black',
                  linewidths=0.8, linestyles='-', zorder=8)


mp.clabel(cntr, inline_spacing=1, fmt='%.1f', fontsize=10)
mp.contourf(x, y, z, 8, cmap='jet', alpha=0.7, zorder=8)
# 热成像图
# mp.imshow(z, cmap='jet', origin='lower')
mp.tight_layout()
mp.show()
