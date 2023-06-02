import sys
import matplotlib.pyplot as plot
import numpy as np

import default
from euler import eulerRecord

default.rcLatex(fontSize=14)
figure, axes = default.getFigureAxes(left=-45, right=5.5, top=13, bottom=-9, bottomArrow=False, flipY=True)

def equation(x):
    return 43.0205 + 8.76262 * x + 0.536311 * x**2 + 0.0135212 * x ** 3 + 0.000123702 * x ** 4

x = [ -5, -10, -20, -30, -35, -40 ]
y = np.asarray([ 12.0577, -2.40083, -4.83701, -1.46678, 0.625988, 2.86098 ]) - 1
axes.plot(np.linspace(-45, 0, 100), equation(np.linspace(-45, 0, 100)), c="tab:blue")
axes.scatter(x, y, fc="tab:blue", ec="tab:blue", s=25, zorder=10)
axes.set_xticks(np.linspace(-40, -10, 4))

if sys.argv[-1] == "save":
    default.saveFigure(figure)

plot.show()