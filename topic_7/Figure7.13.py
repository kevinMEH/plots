import sys
import matplotlib.pyplot as plot
import numpy as np

import default
from euler import eulerRecord

default.rcLatex(fontSize=14)
figure, axes = default.getFigureAxes(left=-45, right=5.5, top=13, bottom=-7, bottomArrow=False, flipY=True)

x = [ -5, -10, -20, -30, -35, -40 ]
y = np.asarray([ 12.0577, -2.40083, -4.83701, -1.46678, 0.625988, 2.86098 ]) - 1
axes.plot(x, y, c="tab:blue")
axes.scatter(x, y, fc="tab:blue", ec="tab:blue", s=25, zorder=10)
# axes.plot(np.linspace(0, 1.45, 2), np.linspace(1, 1, 2), zorder=-10, alpha=0.2, color="k")
# axes.plot(np.linspace(1, 1, 50), np.linspace(-13, 36, 50), zorder=-10, alpha=0.2, color="k")
axes.set_xticks(np.linspace(-40, -10, 4))
# axes.set_yticks(np.linspace(-10, 30, 5))

if sys.argv[-1] == "save":
    default.saveFigure(figure)

plot.show()