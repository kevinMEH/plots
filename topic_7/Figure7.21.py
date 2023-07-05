import sys
import matplotlib.pyplot as plot
import numpy as np

import default

default.rcRegular(fontSize=16)
figure, axes = default.getFigureAxes(left=0, right=13.5, top=16, bottom=0)

def equation(x):
    lx = x
    return (-4 * lx)/(abs(lx) + 1) + (1/42) * lx**3 + 8 - 18**(x/10)

x = np.linspace(1, 12, 200)
axes.plot(x, equation(x))
x = np.asarray([1, 2.4, 3.8, 9.2, 10.6, 12])
y = equation(x)
axes.scatter(x, y)

for sx, sy, label in zip(x, y, ["$y_a$", "$y_1$", "$y_2$", "$y_{n-2}$", "$y_{n-1}$", "$y_b$"]):
    plot.text(sx + (0 if sx < 4 else 0.4), sy - (1.5 if sx < 4 else 1.6), label, ha="center")

for sx, sy, label in zip(x, y, ["$y_a$", "$w_1$", "$w_2$", "$w_{n-2}$", "$w_{n-1}$", "$y_b$"]):
    if sx == 1 or sx == 12: continue
    plot.text(sx - (0 if sx < 4 else 0.5), sy + (1.3 if sx < 4 else 1.25), label, ha="center")

axes.set_xticks([1, 2.4, 3.8, 9.2, 10.6, 12])
axes.set_xticklabels(["$t_0$", "$t_1$", "$t_2$", "$t_{n-2}$", "$t_{n-1}$", "$t_n$"])
axes.set_yticks([])

if sys.argv[-1] == "save":
    default.saveFigure(figure)
    
plot.show()