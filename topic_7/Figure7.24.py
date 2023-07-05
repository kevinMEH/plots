import sys
import matplotlib.pyplot as plot
import numpy as np

from euler import eulerRecord
import default

default.rcRegular(fontSize=16)
figure, axes = default.getFigureAxes(left=0, right=2.2, top=1.4, bottom=0)

def secondDerivative(y):
    return y - y**2

def derivative(x, y, h, prev):
    return prev + h * secondDerivative(y)

endX = 2
steps = 200

x = np.linspace(0, endX, steps)
axes.plot(x, eulerRecord(0, 1, 1, endX, 100_000, steps, derivative) - 0.5);

axes.set_yticks(np.linspace(0.25, 1.25, 5))
labels = [ str(num) + "" for num in np.linspace(0.75, 1.75, 5) ]
axes.set_yticklabels(labels)

if sys.argv[-1] == "save":
    default.saveFigure(figure)

plot.show()