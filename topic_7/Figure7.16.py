import sys
import matplotlib.pyplot as plot
import numpy as np

import default
from euler import eulerRecord

default.rcLatex(fontSize=14)
figure, axes = default.getFigureAxes(left=0, right=2.2, top=1.1, bottom=0)

def secondDerivative(x, y):
    return -x * y

def derivative(x, y, h, prev):
    return prev + h * secondDerivative(x, y)

endX = 2.0
steps = 100
x = np.linspace(0, endX, steps)
axes.plot(x, eulerRecord(0, 0.888, 0, endX, 100_000, steps, derivative))
axes.scatter([2], [-0.0133008], ec="tab:blue", fc="tab:blue", s=25)
axes.text(1.9, 0.16, r"$y(2)\approx0.0133$", ha="left")

if sys.argv[-1] == "save":
    default.saveFigure(figure)

plot.show()