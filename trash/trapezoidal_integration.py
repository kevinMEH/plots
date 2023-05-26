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

x = np.linspace(-1, 7, 100);
y = 3 \
    + 15.95833 * x \
    - 24.27917 * (x ** 2) \
    + 11.9875 * (x ** 3) \
    - 2.320833 * (x ** 4) \
    + 0.1541667 * (x ** 5)

x1 = np.linspace(0, 1, 25);
y1 = 1.5 * x1 + 3
x2 = np.linspace(1, 2, 25);
y2 = -3 * x2 + 7.5
x3 = np.linspace(2, 3, 25);
y3 = 4 * x3 - 6.5
x4 = np.linspace(3, 4, 25);
y4 = 3.8 * x4 - 5.9
x5 = np.linspace(4, 5, 25);
y5 = -3.8 * x5 + 24.5
x6 = np.linspace(5, 6, 25);
y6 = -0.5 * x6 + 8

figure = plot.figure(figsize = (10/1.2, 6/1.2));
axes = SubplotZero(figure, 111)
figure.add_subplot(axes)

for direction in ["xzero", "yzero"]:
    axes.axis[direction].set_axisline_style("-|>")
    axes.axis[direction].set_visible(True)
for direction in ["left", "right", "bottom", "top"]:
    axes.axis[direction].set_visible(False)

plot.plot(x + 0.5, y, color="r", zorder=10, linewidth=2)
# plot.plot(x1, y1, color="tab:green")
# plot.plot(x2, y2, color="tab:green")
# plot.plot(x3, y3, color="tab:green")
# plot.plot(x4, y4, color="tab:green")
# plot.plot(x5, y5, color="tab:green")
# plot.plot(x6, y6, color="tab:green")
plot.fill_between(x1 + 0.5, y1, linewidth=1.5, edgecolor="#606060", facecolor="#c1efc0")
plot.fill_between(x2 + 0.5, y2, linewidth=1.5, edgecolor="#606060", facecolor="#c1efc0")
plot.fill_between(x3 + 0.5, y3, linewidth=1.5, edgecolor="#606060", facecolor="#c1efc0")
plot.fill_between(x4 + 0.5, y4, linewidth=1.5, edgecolor="#606060", facecolor="#c1efc0")
plot.fill_between(x5 + 0.5, y5, linewidth=1.5, edgecolor="#606060", facecolor="#c1efc0")
plot.fill_between(x6 + 0.5, y6, linewidth=1.5, edgecolor="#606060", facecolor="#c1efc0")

axes.set_xticks(np.asarray([1, 2, 3, 4, 5, 6, 7]) - 0.5)
axes.set_xticklabels(["$x_0$", "$x_1$", "$x_2$", "$x_3$", "$x_4$", "$x_5$", "$x_6$"])
axes.set_yticks([])

# No arrows on negatives
axes.set_xlim(left=0, right=7)
axes.set_ylim(bottom=0, top=10)

plot.show()