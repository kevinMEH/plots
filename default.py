import sys
import matplotlib.pyplot as plot
from mpl_toolkits.axisartist.axislines import SubplotZero

# Non serious maths
def rcRegular(fontSize = 16, flipY = False):
    plot.rcParams.update({
        "mathtext.fontset": "stix",
        "font.family": "Times New Roman",
        "font.size": fontSize,
        "xtick.major.pad": "10",
        "ytick.major.pad": "10",
        "axes.linewidth": 0,
    })

# Matrix and other maths
def rcLatex(fontSize = 16, flipY = False):
    plot.rcParams.update({
        "mathtext.fontset": "stix",
        "font.size": fontSize,
        "xtick.major.pad": "10",
        "ytick.major.pad": "10",
        "axes.linewidth": 0,
        "text.usetex": True,
        "text.latex.preamble": r"\usepackage{{amsmath}}",
    })

def getFigureAxes(figsize = (8, 5), left = -10, right = 10, top = 10, bottom = -10,
leftLim = None, rightLim = None, topLim = None, bottomLim = None,
leftArrow = True, rightArrow = True, topArrow = True, bottomArrow = True,
yLabel = "y", xLabel = "x", xPosition = "right", flipY = False):

    if flipY:
        plot.rcParams.update({
            "ytick.major.pad": -40,
        })

    if leftLim == None:
        if left == 0: leftLim = (right - left) * -0.05;
        else: leftLim = left
    if rightLim == None: rightLim = right * 1.05;
    if topLim == None: topLim = top * 1.05;
    if bottomLim == None:
        if bottom == 0: bottomLim = (top - bottom) * -0.03
        else: bottomLim = bottom;

    figure = plot.figure(figsize=figsize)
    axes = SubplotZero(figure, 111)
    figure.add_subplot(axes)

    for direction in ["xzero", "yzero"]:
        axes.axis[direction].set_visible(True)
    for direction in ["left", "right", "bottom", "top"]:
        axes.axis[direction].set_visible(False)

    if flipY:
        axes.axis["yzero"].major_ticklabels.set_ha("left")

    if right != 0: axes.quiver([right], [0], scale_units="xy", scale=1, width=0.0025, headwidth=5 if rightArrow else 0)
    if left != 0: axes.quiver([left], [0], scale_units="xy", scale=1, width=0.0025, headwidth=5 if leftArrow else 0)
    if top != 0: axes.quiver([0], [top], scale_units="xy", scale=1, width=0.0025, headwidth=5 if topArrow else 0)
    if bottom != 0: axes.quiver([0], [bottom], scale_units="xy", scale=1, width=0.0025, headwidth=5 if bottomArrow else 0)
    axes.set_xlim(left=leftLim, right=rightLim)
    axes.set_ylim(bottom=bottomLim, top=topLim)
    
    axes.text(rightLim if xPosition == "right" else leftLim * 1.03, (top - bottom) * 0.005, "$" + xLabel + "$" if xLabel != "" else "", fontsize=16, horizontalalignment="center", verticalalignment="center");
    axes.text(0, top + (topLim - bottomLim) * 0.05, "$" + yLabel + "$" if yLabel != "" else "", fontsize=16, horizontalalignment="center", verticalalignment="center");

    return figure, axes

def saveFigure(figure):
    selfName = sys.argv[0][0 : -3] + ".jpeg"
    figure.savefig("./Images/" + selfName, dpi=400)
    print("Saved plot as " + selfName)