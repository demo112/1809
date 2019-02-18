import numpy as np
import matplotlib.pyplot as mp

mp.figure('Pie', facecolor='gray')
mp.title('pie', fontsize=18)

values = [26, 17, 21, 29, 11]
spaces = [0.05, 0.01, 0.01, 0.01, 0.01]
labels = ['Python', 'JS', 'C++', 'Java', 'PHP']
color = ['dodgerblue', 'orangered', 'limegreen', 'violet', 'gold']

mp.pie(values, spaces, labels, color, '%.f%%',
       shadow=True,
       pctdistance=0.618,
       labeldistance=1.2,
       startangle=90,
       radius=2)
mp.show()
