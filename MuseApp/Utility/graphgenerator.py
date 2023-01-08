import matplotlib as mpl
import matplotlib.pyplot as plt
from kivy.metrics import dp

#optimized draw on Agg backend
mpl.rcParams['path.simplify'] = True
mpl.rcParams['path.simplify_threshold'] = 1.0
mpl.rcParams['agg.path.chunksize'] = 1000

#define some matplotlib figure parameters
mpl.rcParams['axes.spines.top'] = False
mpl.rcParams['axes.spines.right'] = False
mpl.rcParams['axes.linewidth'] = 1.0

font_size_axis_title=dp(13)
font_size_axis_tick=dp(12)

class GraphGenerator(object):

    def __init__(self, plotdata):
        super().__init__()

        self.fig, self.ax1 = plt.subplots(1, 1)

        self.line1, = self.ax1.plot(range(0, plotdata.shape[0]), plotdata[:,0],label='delta')
        self.line2, = self.ax1.plot(range(0, plotdata.shape[0]), plotdata[:,1],label='theta')
        self.line3, = self.ax1.plot(range(0, plotdata.shape[0]), plotdata[:,2],label='alpha')
        self.line4, = self.ax1.plot(range(0, plotdata.shape[0]), plotdata[:,3],label='beta')

        self.xmin,self.xmax = self.ax1.get_xlim()
        self.ymin,self.ymax = self.ax1.get_ylim()

        self.ax1.set_xlim(self.xmin, self.xmax)
        self.ax1.set_ylim(self.ymin, self.ymax)   
        self.ax1.set_xlabel("time in seconds",fontsize=font_size_axis_title)
        self.ax1.set_ylabel("psd",fontsize=font_size_axis_title)

