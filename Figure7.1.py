import sys
import matplotlib.pyplot as plot
import numpy as np

import default

default.rcRegular(fontSize=14)
figure, axes = default.getFigureAxes(leftLim=-0.5, left=0, right=7, top=130, bottom=0, bottomLim=-10)

def equation(x, v0):
    return -40 + (v0 * x) - (1/2) * (20) * x**2

x = np.linspace(1, 6, 100)
axes.plot(x, equation(x, 80))
axes.plot(np.linspace(1, 1.8, 50), -30 + 60 * np.linspace(1, 1.8, 50), linestyle="dashed", dashes=(5, 2), color="k", linewidth=1)
axes.scatter([6], [80], fc="k", ec="k")
axes.scatter([1], [30], fc="k", ec="k")

axes.set_xticks([1, 6])
axes.set_xticklabels(["$a$", "$b$"])
axes.set_yticks([30, 80])
axes.set_yticklabels(["$y_a$", "$y_b$"])

axes.plot(np.linspace(0, 1, 2), np.linspace(30, 30, 2), "k--", alpha=0.25)
axes.plot(np.linspace(1, 1, 2), np.linspace(0, 30, 2), "k--", alpha=0.25)
axes.plot(np.linspace(0, 6, 2), np.linspace(80, 80, 2), "k--", alpha=0.25)
axes.plot(np.linspace(6, 6, 2), np.linspace(0, 80, 2), "k--", alpha=0.25)

axes.text(1.2, 23, "$s_a=?$", ha="left")

if sys.argv[-1] == "save":
    default.saveFigure(figure);

plot.show()