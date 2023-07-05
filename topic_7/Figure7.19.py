import sys
import matplotlib.pyplot as plot
import numpy as np

import default
from euler import eulerRecord

default.rcLatex(fontSize=14)
figure, axes = default.getFigureAxes(left=0, right=3.2, top=1.1, bottom=-2.1, bottomArrow=False)

def equation(x):
    return 0.89918 * x - 1.9013

x = [ 0, 1, 2, 3 ]
y = np.asarray([ -1.9013008, -1.002121, -0.10394, 0.79624 ])
axes.plot(np.linspace(0, 3.2, 100), equation(np.linspace(0, 3.2, 100)), c="tab:blue")
axes.scatter(x, y, fc="tab:blue", ec="tab:blue", s=25, zorder=10)
axes.set_xticks(np.linspace(0.5, 3.0, 6))

if sys.argv[-1] == "save":
    default.saveFigure(figure)

plot.show()