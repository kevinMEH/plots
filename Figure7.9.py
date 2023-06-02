import sys
import matplotlib.pyplot as plot
import numpy as np

import default
from euler import euler

default.rcLatex(fontSize=14)
figure, axes = default.getFigureAxes(left=-75, right=8, rightLim=10, top=25, bottom=-8, flipY=True, leftArrow=False, bottomArrow=False)

def derivative(x, y, stepSize, previousDerivative):
    return previousDerivative + stepSize * ((3/2) * y * y)

x = np.linspace(-80, 0, 81)
y = [ euler(0, 4, startDerivative, 1, 100_000, derivative) for startDerivative in x ]
axes.plot(x, y)
axes.plot(np.linspace(-74, 7, 50), np.linspace(1, 1, 50), zorder=-10, alpha=0.5, color="k")
axes.set_xticks(np.linspace(-70, -10, 7))
axes.set_yticks(np.linspace(-5, 20, 6))
axes.yaxis.tick_right()

if sys.argv[-1] == "save":
    default.saveFigure(figure)

plot.show()