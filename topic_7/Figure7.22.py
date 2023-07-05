import sys
import matplotlib.pyplot as plot
import numpy as np

import default

default.rcRegular(fontSize=16)
figure, axes = default.getFigureAxes(left=-0.2, right=1.2, top=4.5, bottom=0)

def equation(x):
    return (np.e**(-2 * x) * (-1 * np.e**(4*x) + 3 * np.e**(4*x+2) - 3 * np.e**2 + np.e**4)) / (np.e**4 - 1)

x = np.linspace(-0.2, 1.2, 200)
axes.plot(x, equation(x))
axes.scatter([1], [equation(1)])

axes.axvline(1, c="k", alpha=0.2, zorder=-20)
axes.axhline(equation(1), c="k", alpha=0.2, zorder=-20)

axes.set_yticks(np.arange(1, 5))
axes.set_xticks(np.linspace(0, 1, 5))

if sys.argv[-1] == "save":
    default.saveFigure(figure)

plot.show()