import matplotlib as mpl
from cycler import cycler

from .colors import WES, register_colors


def use():
    """
    Apply SynoSys matplotlib defaults.
    """

    register_colors()

    mpl.rcParams["font.family"] = "Arial"
    mpl.rcParams["mathtext.fontset"] = "stix"
    mpl.rcParams["text.usetex"] = False

    mpl.rcParams["axes.prop_cycle"] = cycler(color=list(WES.values()))

    mpl.rcParams["legend.frameon"] = True
    mpl.rcParams["legend.facecolor"] = "white"
    mpl.rcParams["legend.edgecolor"] = "black"
    mpl.rcParams["legend.framealpha"] = 1.0