import sys
import matplotlib.pyplot as plot
import numpy as np

import default

default.rcRegular(fontSize=14)
figure, axes = default.getFigureAxes(leftLim=-0.5, left=0, right=9.5, top=130, bottom=0, bottomLim=-10)

def equation(x, v0):
    return 30 + (v0 * x) - (1/2) * (9.81) * x**2

x = np.linspace(0, 8.84, 100)
axes.plot(x, equation(x, 40))
axes.plot(np.linspace(0, 1, 50), 30 + 40 * np.linspace(0, 1, 50), linestyle="dashed", dashes=(5, 2), color="k", linewidth=1)
axes.set_xticks(np.linspace(2, 8, 4))
axes.set_yticks(np.linspace(0, 120, 7))

axes.text(0.3, 80, "$v_0=40$")

if sys.argv[-1] == "save":
    default.saveFigure(figure);

plot.show()