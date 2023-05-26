import matplotlib.pyplot as plot
import matplotlib as matplotlib
from mpl_toolkits.axisartist.axislines import SubplotZero
import numpy as np

plot.rcParams.update({
    "mathtext.fontset": "stix",
    "font.size": "14",
    "xtick.major.pad": "10",
    "ytick.major.pad": "10",
    "text.usetex": True,
    "text.latex.preamble": r"\usepackage{{amsmath}}",
});

figure = plot.figure(figsize = (10/1.2, 10/1.2));
axes = SubplotZero(figure, 111)
figure.add_subplot(axes)

for direction in ["xzero", "yzero"]:
    # axes.axis[direction].set_axisline_style("-|>")
    axes.axis[direction].set_visible(True)
for direction in ["left", "right", "bottom", "top"]:
    axes.axis[direction].set_visible(False)

ten = np.linspace(-10, 10, 50)
axes.plot([ 2 for i in ten ], ten, color="k", alpha=0.1)
axes.plot([ -2 for i in ten ], ten, color="k", alpha=0.1)
axes.plot([ 4 for i in ten ], ten, color="k", alpha=0.1)
axes.plot([ -4 for i in ten ], ten, color="k", alpha=0.1)
axes.plot(ten, [ 2 for i in ten ], color="k", alpha=0.1)
axes.plot(ten, [ -2 for i in ten ], color="k", alpha=0.1)
axes.plot(ten, [ 4 for i in ten ], color="k", alpha=0.1)
axes.plot(ten, [ -4 for i in ten ], color="k", alpha=0.1)

axes.quiver([-1], [2], color="r", scale_units="xy", scale=1, zorder=5)
axes.quiver([1], [1], color="r", scale_units="xy", scale=1, zorder=5)

axes.quiver([1], [3], color="k", scale_units="xy", scale=1, width=0.004, alpha=0.4)
axes.quiver([-2], [-4], color="k", scale_units="xy", scale=1, width=0.004, alpha=0.4)
axes.quiver([3.5], [1.5], color="k", scale_units="xy", scale=1, width=0.004, alpha=0.4)
axes.quiver([1.2], [-3.5 * 1.2], color="k", scale_units="xy", scale=1, width=0.004, alpha=0.4)
axes.quiver([3], [-3], color="k", scale_units="xy", scale=1, width=0.004, alpha=0.4)
axes.quiver([-4], [-2], color="k", scale_units="xy", scale=1, width=0.004, alpha=0.4)
axes.quiver([-4], [2], color="k", scale_units="xy", scale=1, width=0.004, alpha=0.4)

axes.text(-1.9, 2.5, r"$\begin{bmatrix} 2 \\ -1 \end{bmatrix}$");
axes.text(1.3, 1.5, r"$\begin{bmatrix} 1 \\ 1 \end{bmatrix}$");

# No arrows on negatives
axes.set_xlim(left=-5, right=5)
axes.set_ylim(bottom=-5, top=5)

axes.quiver([0], [5], scale_units="xy", scale=1, width=0.0055)
axes.quiver([0], [-5], scale_units="xy", scale=1, width=0.0055)
axes.quiver([5], [0], scale_units="xy", scale=1, width=0.0055)
axes.quiver([-5], [0], scale_units="xy", scale=1, width=0.0055)

axes.set_xticks(np.delete(np.linspace(-4, 4, 5), 2))
axes.set_yticks(np.delete(np.linspace(-4, 4, 5), 2))





matrix = np.array([2, 0.5, 1, 1.5]).reshape(2, 2);
print(matrix);

def mvMultiply(xList, yList):
    resultX = []
    resultY = []
    for x, y in zip(xList, yList):
        rx, ry = matrix.dot([x, y])
        resultX.append(rx)
        resultY.append(ry)
    return resultX, resultY

transformed = plot.figure(figsize = (10/1.2, 10/1.2))
transformed_axes = SubplotZero(transformed, 111)
transformed.add_subplot(transformed_axes)

for direction in ["xzero", "yzero"]:
    # transformed_axes.axis[direction].set_axisline_style("-|>")
    transformed_axes.axis[direction].set_visible(True)
for direction in ["left", "right", "bottom", "top"]:
    transformed_axes.axis[direction].set_visible(False)

ten = np.linspace(-10, 10, 50)

rx, ry = mvMultiply([0 for i in ten ], ten)
transformed_axes.plot(rx, ry, color="k", alpha=0.1)
rx, ry = mvMultiply([2 for i in ten ], ten)
transformed_axes.plot(rx, ry, color="k", alpha=0.1)
rx, ry = mvMultiply([4 for i in ten ], ten)
transformed_axes.plot(rx, ry, color="k", alpha=0.1)
rx, ry = mvMultiply([-2 for i in ten ], ten)
transformed_axes.plot(rx, ry, color="k", alpha=0.1)
rx, ry = mvMultiply([-4 for i in ten ], ten)
transformed_axes.plot(rx, ry, color="k", alpha=0.1)

rx, ry = mvMultiply(ten, [0 for i in ten ])
transformed_axes.plot(rx, ry, color="k", alpha=0.1)
rx, ry = mvMultiply(ten, [2 for i in ten ])
transformed_axes.plot(rx, ry, color="k", alpha=0.1)
rx, ry = mvMultiply(ten, [4 for i in ten ])
transformed_axes.plot(rx, ry, color="k", alpha=0.1)
rx, ry = mvMultiply(ten, [-2 for i in ten ])
transformed_axes.plot(rx, ry, color="k", alpha=0.1)
rx, ry = mvMultiply(ten, [-4 for i in ten ])
transformed_axes.plot(rx, ry, color="k", alpha=0.1)

rx, ry = mvMultiply([-1], [2])
transformed_axes.quiver(rx, ry, color="r", scale_units="xy", scale=1, zorder=10)
rx, ry = mvMultiply([1], [1])
transformed_axes.quiver(rx, ry, color="r", scale_units="xy", scale=1, zorder=10)

rx, ry = mvMultiply([1], [3])
transformed_axes.quiver(rx, ry, color="k", scale_units="xy", scale=1, width=0.004, alpha=0.4)
rx, ry = mvMultiply([-2], [-4])
transformed_axes.quiver(rx, ry, color="k", scale_units="xy", scale=1, width=0.004, alpha=0.4)
rx, ry = mvMultiply([3.5], [1.5])
transformed_axes.quiver(rx, ry, color="k", scale_units="xy", scale=1, width=0.004, alpha=0.4)
rx, ry = mvMultiply([1.2], [-3.5 * 1.2])
transformed_axes.quiver(rx, ry, color="k", scale_units="xy", scale=1, width=0.004, alpha=0.4)
rx, ry = mvMultiply([3], [-3])
transformed_axes.quiver(rx, ry, color="k", scale_units="xy", scale=1, width=0.004, alpha=0.4)
rx, ry = mvMultiply([-4], [-2])
transformed_axes.quiver(rx, ry, color="k", scale_units="xy", scale=1, width=0.004, alpha=0.4)
rx, ry = mvMultiply([-4], [2])
transformed_axes.quiver(rx, ry, color="k", scale_units="xy", scale=1, width=0.004, alpha=0.4)

transformed_axes.text(-9, 8, r"$\begin{bmatrix} 2 & 0.5 \\ 1 & 1.5 \end{bmatrix}$");
transformed_axes.text(-2.5, 2.5, r"$\begin{bmatrix} 2 \\ -1 \end{bmatrix}$");
transformed_axes.text(2.8, 3, r"$\begin{bmatrix} 2.5 \\ 2.5 \end{bmatrix}$");

# No arrows on negatives
transformed_axes.set_xlim(left=-10, right=10)
transformed_axes.set_ylim(bottom=-10, top=10)

transformed_axes.set_xticks(np.delete(np.linspace(-8, 8, 9), 4))
transformed_axes.set_yticks(np.delete(np.linspace(-8, 8, 9), 4))

transformed_axes.quiver([0], [10], scale_units="xy", scale=1, width=0.0055)
transformed_axes.quiver([0], [-10], scale_units="xy", scale=1, width=0.0055)
transformed_axes.quiver([10], [0], scale_units="xy", scale=1, width=0.0055)
transformed_axes.quiver([-10], [0], scale_units="xy", scale=1, width=0.0055)

plot.show()