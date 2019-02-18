import matplotlib.pyplot as mp
from mpl_toolkits.mplot3d import axes3d
# """:type mp: matplotlib.pyplot"""
mp.figure(
    'test windows',
    figsize=(10, 10),
    facecolor='gray'
)
mp.title('TEST')
mp.grid(linestyle='-.')
mp.tight_layout()

class ChildFigure(object):
    """绘制子图"""
    def juzhen(self):
        mp.subplot(331)

    def wange(self):
        space = mp.GridSpec(3, 3)
        mp.subplot(space[0, :2])

    def free(self):
        mp.axes([0.1, 0.1, 0.3, 0.3], facecolor='gray')
        mp.axes([0.4, 0.4, 0.2, 0.2], facecolor='gray')
        mp.axes([0.6, 0.6, 0.3, 0.3], facecolor='gray')


class Axess(object):
    def dicar(self):
        self.ax = mp.gca()
        axl = self.ax.spines('left')
        axr = self.ax.spines('right')
        axt = self.ax.spines('top')
        axb = self.ax.spines('bottom')

    def polar(self):
        mp.gca(pojection='polar')

    def three_d(self):
        mp.figure(projection='3d')



if __name__ == '__main__':
    child = ChildFigure()
    child.free()
    mp.show()
