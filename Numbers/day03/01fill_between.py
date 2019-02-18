import numpy as np
import matplotlib.pyplot as mp

n = 1000

x = np.linspace(0, 8*np.pi, n)

sinx = np.sin(x)
cosx = np.cos(x / 2) / 2

mp.figure('Fill', facecolor='gray')
mp.title('Fill', fontsize=18)
mp.xlabel('x', fontsize=18)
mp.ylabel('y', fontsize=18)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(x, sinx, c='b', label=r'$y=sin(x)$')
mp.plot(x, cosx, c='red', label=r'$y=\frac{1}{2}cos(\frac{x}{2})$')

mp.fill_between(x, sinx, cosx, sinx < cosx, color='orange', alpha=0.5)
mp.fill_between(x, sinx, cosx, sinx > cosx, color='orangered', alpha=0.5)

mp.legend()
mp.show()
