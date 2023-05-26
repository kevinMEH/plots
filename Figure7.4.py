import sys
import matplotlib.pyplot as plot
import numpy as np

import default

default.rcLatex(fontSize=14)
figure, axes = default.getFigureAxes(left=0, right=np.pi + 0.25, top=2.2, bottom=0)

def equation(x):
    return x * np.sin(x)

x = np.linspace(0, np.pi, 100)
axes.plot(x, equation(x))
axes.set_xticks(np.linspace(0, np.pi, 3))
axes.set_xticklabels([ "$0$", r"$\frac{\pi}{2}$", r"$\pi$"])

axes.text(0.5, 1.75, "$y(t) = t \sin(t)$")

if sys.argv[-1] == "save":
    default.saveFigure(figure)

plot.show()