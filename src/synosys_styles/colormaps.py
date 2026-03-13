# src/synosys_styles/colormaps.py
import matplotlib as mpl
from matplotlib.colors import LinearSegmentedColormap

from .colors import WES


def _make_cmap(name, colors, N=256):
    return LinearSegmentedColormap.from_list(name, colors, N=N)


def wes_colormap():
    return _make_cmap(
        "wes",
        [
            WES["wes_plum"],
            WES["wes_mauvegray"],
            WES["wes_teal"],
            WES["wes_mint"],
            WES["wes_sand"],
            WES["wes_ochre"],
            WES["wes_crimson"],
        ],
    )


def wes_seq_colormap():
    return _make_cmap(
        "wes_seq",
        [
            WES["wes_mauvegray"],
            WES["wes_teal"],
            WES["wes_mint"],
            WES["wes_sand"],
            WES["wes_ochre"],
        ],
    )


def wes_div_colormap():
    return _make_cmap(
        "wes_div",
        [
            WES["wes_teal"],
            WES["wes_taupe"],
            WES["wes_rosewood"],
        ],
    )


def wes_div_white_colormap():
    return _make_cmap(
        "wes_div_white",
        [
            WES["wes_teal"],
            WES["wes_mint"],
            (1.0, 1.0, 1.0),
            WES["wes_sand"],
            WES["wes_crimson"],
        ],
    )


def register_colormaps():
    cmaps = [
        wes_colormap(),
        wes_seq_colormap(),
        wes_div_colormap(),
        wes_div_white_colormap(),
    ]

    for cmap in cmaps:
        try:
            mpl.colormaps.register(cmap)
        except ValueError:
            pass