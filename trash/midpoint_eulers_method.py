import matplotlib.pyplot as plot
import matplotlib as matplotlib
from mpl_toolkits.axisartist.axislines import SubplotZero
import numpy as np

plot.rcParams.update({
    "mathtext.fontset": "stix",
    "font.size": "20",
    "xtick.major.pad": "10",
    "ytick.major.pad": "10"
});

x = np.linspace(0, 2, 100);
y = ((x - 2) ** 2) * -1 + 4

df = 2 * x + 1
dfw = 2 * x + 0.75

figure = plot.figure(figsize = (10/1.2, 6/1.2));
axes = SubplotZero(figure, 111)
figure.add_subplot(axes)

for direction in ["xzero", "yzero"]:
    axes.axis[direction].set_axisline_style("-|>")
    axes.axis[direction].set_visible(True)
for direction in ["left", "right", "bottom", "top"]:
    axes.axis[direction].set_visible(False)

plot.plot(x, y, color="b")
plot.plot(x, df, color="tab:red", alpha=0.4)
plot.plot(x, dfw, color="r")

xn_horizontal_y = np.linspace(1.75, 1.75, 50);
xn_horizontal_x = np.linspace(0, 0.5, 50);
xn_vertical_x = np.linspace(0.5, 0.5, 50);
xn_vertical_y = np.linspace(0, 1.75, 50);
xn1_vertical_x = np.linspace(1.5, 1.5, 50);
xn1_vertical_y = np.linspace(0, 3.75, 50);

plot.plot(xn_horizontal_x, xn_horizontal_y, "m--", linewidth=1);
plot.plot(xn_vertical_x, xn_vertical_y, "m--", linewidth=1);
plot.plot(xn1_vertical_x, xn1_vertical_y, "m--", linewidth=1);

plot.scatter([0.5], [1.75], facecolors="w", edgecolors="k", zorder=10)
plot.scatter([1], [3], facecolors="k", edgecolors="k", zorder=10)
plot.scatter([1.5], [3.75], facecolors="k", edgecolors="k", zorder=10)

axes.set_xticks([0.5, 1, 1.5])
axes.set_xticklabels(["$x_n$", r"$x_{n+\frac{1}{2}}$", "$x_{n+1}$"])
axes.set_yticks([1.75])
axes.set_yticklabels(["$y_n$"])

plot.text(1.22, 0.25, r"$\frac{h}{2}$")
plot.text(0.72, 0.25, r"$\frac{h}{2}$")
plot.text(2.02, 3.93, r"$\mathrm{Exact}$", color="b", fontsize=16)

# No arrows on negatives
axes.set_xlim(left=0, right=2)
axes.set_ylim(bottom=0)

plot.show()