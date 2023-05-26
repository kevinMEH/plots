import sys
import matplotlib.pyplot as plot
import numpy as np

import default

default.rcLatex(fontSize=14)
figure, axes = default.getFigureAxes(left=0, right=1.15, top=9, bottom=0)

def equation(x, s):
    return ((s + 2)/4) * np.power(np.e, 2 * x) - ((s - 2)/4) * np.power(np.e, -2 * x)

x = np.linspace(0, 1.1, 100)
axes.plot(x, equation(x, -0.42031))
axes.plot(x, equation(x, 0))
axes.plot(x, equation(x, 1))
axes.plot(x, equation(x, 2))
axes.plot(x, equation(x, -1))
axes.set_xticks(np.linspace(0, 1.0, 6))
axes.plot(np.linspace(1, 1, 100), np.linspace(0, 9, 100), color="k", alpha=0.3)
axes.plot(np.linspace(0, 1.1, 100), np.linspace(3, 3, 100), color="k", alpha=0.3)

axes.text(0.8, 5.8, "$s=2$", verticalalignment="center", rotation=45)
axes.text(0.83, 4.8, "$s=1$", verticalalignment="center", rotation=39)
axes.text(0.86, 3.5, "$s=0$", verticalalignment="center", rotation=30)
axes.text(0.87, 2.05, "$s=-1$", verticalalignment="center", rotation=15)

if sys.argv[-1] == "save":
    default.saveFigure(figure)

plot.show()