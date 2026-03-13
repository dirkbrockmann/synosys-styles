from .colors import WES, WES_HL, register_colors
from .colormaps import (
    wes_colormap,
    wes_seq_colormap,
    wes_div_colormap,
    wes_div_white_colormap,
    register_colormaps,
)
from .style import use

__all__ = [
    "WES",
    "WES_HL",
    "register_colors",
    "wes_colormap",
    "wes_seq_colormap",
    "wes_div_colormap",
    "wes_div_white_colormap",
    "register_colormaps",
    "use",
]