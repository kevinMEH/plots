import sys
import matplotlib.pyplot as plot
import numpy as np

from euler import eulerRecord
import default

default.rcRegular(fontSize=16)
figure, axes = default.getFigureAxes(left=0, right=1.3, top=4.7, bottom=0)

def secondDerivative(y):
    return y - y**2

def derivative(x, y, h, prev):
    return prev + h * secondDerivative(y)

endX = 1.3
steps = 200

x = np.linspace(0, endX, steps)
axes.plot(x, eulerRecord(0, 1, 5.74221, endX, 100_000, steps, derivative));
axes.scatter([1], [4], fc="tab:blue", ec="tab:blue")
axes.plot([0, 1.3], [4, 4], color="k", alpha=0.3)
axes.plot([1, 1], [0, 5], color="k", alpha=0.3)

if sys.argv[-1] == "save":
    default.saveFigure(figure)

plot.show()