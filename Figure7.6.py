import sys
import matplotlib.pyplot as plot
import numpy as np

import default

default.rcLatex(fontSize=14)
figure, axes = default.getFigureAxes(left=0, right=1.15, top=3.75, bottom=0)

def equation(x, s):
    return ((s + 2)/4) * np.power(np.e, 2 * x) - ((s - 2)/4) * np.power(np.e, -2 * x)

x = np.linspace(0, 1.1, 100)
axes.plot(x, equation(x, -0.42031))
axes.plot(np.linspace(0, 0.25, 40), np.linspace(0, 0.25, 40) * -0.42031 + 1, linestyle="dashed", dashes=(5, 2), color="k", linewidth=1)
axes.set_xticks(np.linspace(0, 1.0, 6))
axes.plot(np.linspace(1, 1, 100), np.linspace(0, 3.5, 100), color="k", alpha=0.3)
axes.plot(np.linspace(0, 1.07, 100), np.linspace(3, 3, 100), color="k", alpha=0.3)
# axes.set_xticklabels([ "$0$", r"$\frac{\pi}{2}$", r"$\pi$"])

axes.text(0.063, 0.575, "$s=-0.42031$", verticalalignment="center")

if sys.argv[-1] == "save":
    default.saveFigure(figure)

plot.show()