import sys
import matplotlib.lines as lines
import matplotlib.pyplot as plot
import numpy as np

import default
from euler import eulerRecord

default.rcLatex(fontSize=14)
figure, axes = default.getFigureAxes(left=0, right=1.2, top=8, bottom=-12)

def derivative(x, y, stepSize, previousDerivative):
    return previousDerivative + stepSize * ((3/2) * y * y)

endX = 1.1
x = np.linspace(0, endX, 100)
axes.plot(x, eulerRecord(0, 4, -7, endX, 1_000000, 100, derivative))
axes.plot(x, eulerRecord(0, 4, -8, endX, 1_000000, 100, derivative))
axes.plot(x, eulerRecord(0, 4, -10, endX, 1_000000, 100, derivative))
axes.plot(x, eulerRecord(0, 4, -36, endX, 1_000000, 100, derivative))
axes.plot(x, eulerRecord(0, 4, -40, endX, 1_000000, 100, derivative))
axes.scatter([1], [1], facecolors="k", edgecolors="k", zorder=10)
axes.set_xticks(np.linspace(0.2, 1.0, 5))
axes.set_yticks(np.linspace(-10, 6, 9))

# axes.legend(["$s=-7$", "$s=-8$", "$s=-10$", "$s=-36$", "$s=-40$"])
axes.legend(handles=[
    lines.Line2D([], [], label="$s=-7$", color="tab:blue"),
    lines.Line2D([], [], label="$s=-8$", color="tab:orange"),
    lines.Line2D([], [], label="$s=-10$", color="tab:green"),
    lines.Line2D([], [], label="$s=-36$", color="tab:red"),
    lines.Line2D([], [], label="$s=-40$", color="tab:purple"),
])

if sys.argv[-1] == "save":
    default.saveFigure(figure)

plot.show()