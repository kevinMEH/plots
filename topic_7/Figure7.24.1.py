import sys
import matplotlib.pyplot as plot
import numpy as np

import default

default.rcRegular(fontSize=16)
figure, axes = default.getFigureAxes(left=0, right=10.5, top=5.5, bottom=0)

def equation(x):
    return 1 + 0.841187306 * x + -0.069934253 * x**2 + 0.002937344 * x**3 - 0.000070397 * x**4

x = np.linspace(0, 10, 200)
axes.plot(x, equation(x))
axes.scatter([0, 1, 2, 5, 10], equation(np.array([0, 1, 2, 5, 10])), fc="tab:blue", ec="tab:blue")
axes.plot([0, 10], [4, 4], color="k", alpha=0.3)
axes.plot([5.74221, 5.74221], [0, 5.5], color="k", alpha=0.3)
axes.scatter([5.74221], [4], fc="k", ec="k", zorder=25, alpha=1, s=25)

if sys.argv[-1] == "save":
    default.saveFigure(figure)

plot.show()