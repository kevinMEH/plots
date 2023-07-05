import sys
import matplotlib.lines as lines
import matplotlib.pyplot as plot
import numpy as np

import default

default.rcRegular(fontSize=16)
figure, axes = default.getFigureAxes(left=0, right=1.06, top=3.3, bottom=0)

def equation(x):
    return 0.605078 * np.e**(-2*x) + 0.394923 * np.e**(2*x)

def equation2(x):
    return 1 + 2 * x

def equation4(x):
    return 1 - 0.1886 * x + 1.0273 * x**2 + 1.1613 * x**3

x = np.linspace(0, 1, 200)
line1 = axes.plot(x, equation(x));
line2 = axes.plot(x, equation2(x));
line3 = axes.plot(x, equation4(x));

axes.legend(handles=[
    lines.Line2D([], [], label="$exact$", color="tab:blue"),
    lines.Line2D([], [], label="$n=2$", color="tab:orange"),
    lines.Line2D([], [], label="$n=4$", color="tab:green"),
], loc="lower right", bbox_to_anchor=(0.95, 0.05))

if sys.argv[-1] == "save":
    default.saveFigure(figure)

plot.show()