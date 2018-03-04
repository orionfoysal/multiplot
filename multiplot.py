import sys
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from math import floor
from mplcursors import cursor

# fileName = sys.argv[1]
# step = int(sys.argv[-1])

# if 'xls' in fileName:
#     df = pd.read_excel(fileName)
# elif 'csv' in fileName:
#     df = pd.read_csv(fileName)

def make_patch_spines_invisible(ax):
    ax.set_frame_on(True)
    ax.patch.set_visible(False)
    for sp in ax.spines.values():
        sp.set_visible(False)

# x = df[sys.argv[2]]
# x = pd.to_datetime(x) 

# y = []
# for i in sys.argv[3:-1]:
#     y.append(df[i])

# for j,item in enumerate(y):
#     temp = 0
#     for i in range(len(item)):
#         if(i+1) < len(item):
#             s1 = item[i+1] - item[i]
#             if temp < s1:
#                 temp = s1 

#     print('Max difference between consecutive '+ y[j].name + ' :'+ str(temp))

def multiplot(x,step,y1,y2=None,y3=None,y4=None):
    x = x 
    y = [y1, y2, y3, y4]
    fig, ax = plt.subplots()
    plt.subplots_adjust(bottom=0.25)
    fig.subplots_adjust(right=0.75)

    lines = []
    lines.append(ax.plot(x, y[0])[0])
    ax.axis([x[0], x[step], min(y[0]), max(y[0])])
    ax.set_ylabel(y[0].name)
    ax.set_xlabel(x.name)
    axpos = plt.axes([0.2, 0.1, 0.65, 0.03], facecolor='white')
    slider_max = len(x) - step - 1
    spos = Slider(axpos, 'Pos', 0, slider_max)

    if y[1] != None:
        ax2 = ax.twinx()
        lines.append(ax2.plot(x,y[1],color='tab:red')[0])
        ax2.axis([x[0], x[step], min(y[1]), max(y[1])])
        ax2.set_ylabel(y[1].name)

    if y[2] != None:    
        ax3 = ax.twinx()
        ax3.spines["right"].set_position(("axes", 1.1))
        # Having been created by twinx, par2 has its frame off, so the line of its
        # detached spine is invisible.  First, activate the frame but make the patch
        # and spines invisible.
        make_patch_spines_invisible(ax3)
        # Second, show the right spine.
        ax3.spines["right"].set_visible(True)
        lines.append(ax3.plot(x,y[2],color='tab:green')[0])
        ax3.axis([x[0], x[step], min(y[2]), max(y[2])])
        ax3.set_ylabel(y[2].name)

    if y[3] != None:
        ax4 = ax.twinx()
        ax4.spines["right"].set_position(("axes", 1.2))
        # Having been created by twinx, par2 has its frame off, so the line of its
        # detached spine is invisible.  First, activate the frame but make the patch
        # and spines invisible.
        make_patch_spines_invisible(ax4)
        # Second, show the right spine.
        ax4.spines["right"].set_visible(True)
        lines.append(ax4.plot(x,y[3],color='tab:red')[0])
        ax4.axis([x[0], x[step], min(y[3]), max(y[3])])
        ax4.set_ylabel(y[3].name)

    ax.legend(lines, [l.get_label() for l in lines])

    def update(val):
        pos = spos.val
        ax.axis([x[floor(pos)], x[floor(pos)+step], min(y[0]), max(y[0])])
        fig.canvas.draw_idle()

    spos.on_changed(update)
    cursor()
    plt.show()