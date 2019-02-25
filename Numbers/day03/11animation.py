import matplotlib.animation as ma
import matplotlib.pyplot as mp
import numpy as np

mp.figure('Animation')

n = 100
balls = np.zeros(n, dtype=[
    ('position', float, 2),
    ('size', float, 1),
    ('growth', float, 1),
    ('color', float, 4),
])
balls['position'] = np.random.uniform(0, 1, (n, 2))
balls['size'] = np.random.uniform(15, 50, 1)
balls['growth'] = np.random.uniform(2, 5, 1)
balls['color'] = np.random.uniform(0, 1, (n, 4))

sc = mp.scatter(balls['position'][:, 0],
                balls['position'][:, 1],
                s=balls['size'],
                facecolor=balls['color'],
                alpha=0.5
                )


def update(number):
    balls['size'] += balls['growth']
    boom_ind = number % n
    balls[boom_ind]['size'] = np.random.uniform(20, 50, 1)
    balls[boom_ind]['position'] = np.random.uniform(0, 1, (1, 2))
    print(sc.get_sizes())
    sc.set_sizes(balls['size'])
    sc.set_offsets(balls['position'])


# def update(number):
#     """根据大小"""
#     balls['size'] += balls['growth']
#     i = 0
#     for size in sc.get_sizes():
#         i += 1
#         if size >= 70:
#             balls[i]['size'] = np.random.uniform(20, 50, 1)
#             balls[i]['position'] = np.random.uniform(0, 1, (1, 2))
#             sc.set_sizes(balls['size'])
#             sc.set_offsets(balls['position'])


anim = ma.FuncAnimation(mp.gcf(), update, interval=100)

mp.show()
