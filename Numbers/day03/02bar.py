import numpy as np
import matplotlib.pyplot as mp
import matplotlib.dates as md


apples  = [79, 36, 58, 92, 37, 85, 72, 63, 54, 72, 40, 95]
orange  = [67, 26, 48, 91, 68, 34, 17, 51, 24, 48, 79, 69]

mp.figure('Bar', facecolor='gray')
mp.title('bar', fontsize=18)
mp.xlabel('Date', fontsize=14)
mp.ylabel('Price', fontsize=14)
mp.tick_params(labelsize=12)
mp.grid(linestyle='-.')

x = np.arange(len(apples))

mp.bar(x - 0.2, apples, 0.4, color='red', label='Apple')
mp.bar(x + 0.2, orange, 0.4, color='orange', label='Orange')

mp.xticks(x, ['Jan', 'Feb', 'Mar', 'Apr', 'May',
              'Jun', 'Jul', "Aug", 'Sep', 'Oct', 'Nov', 'Dec'])
mp.legend()
mp.show()
