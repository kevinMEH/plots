import sys
import matplotlib.pyplot as plot
import numpy as np

import default
from euler import eulerRecord

default.rcLatex(fontSize=14)
figure, axes = default.getFigureAxes(left=0, right=1.5, top=36, bottom=-13, bottomArrow=False)

def derivative(x, y, stepSize, previousDerivative):
    return previousDerivative + stepSize * ((3/2) * y * y)

endX = 1.5
x = np.linspace(0, endX, 100)
axes.plot(x, eulerRecord(0, 4, -35.9, endX, 1_000000, 100, derivative))
axes.scatter([1], [1], facecolors="k", edgecolors="k", zorder=10)
axes.plot(np.linspace(0, 1.45, 2), np.linspace(1, 1, 2), zorder=-10, alpha=0.2, color="k")
axes.plot(np.linspace(1, 1, 50), np.linspace(-13, 36, 50), zorder=-10, alpha=0.2, color="k")
axes.set_xticks(np.linspace(0.2, 1.4, 7))
axes.set_yticks(np.linspace(-10, 30, 5))

if sys.argv[-1] == "save":
    default.saveFigure(figure)

plot.show()