import numpy as np

import matplotlib.pyplot as mp

t = np.linspace(0, 4 * np.pi, 1000)
r  = 0.8 * t


mp.figure('polar')
mp.gca(projection='polar')
mp.xlabel('x')
mp.xlabel('y')
mp.grid(linestyle=':')
mp.plot(t, r, label='xxxx')
# mp.plot(x, ct, label='xxxx')

x = np.linspace(0, 6 * np.pi, 1000)
y = 3 * np.sin(6 * x)

mp.grid(linestyle='-')
mp.plot(x, y, label='xxxx')

mp.legend()
mp.show()
