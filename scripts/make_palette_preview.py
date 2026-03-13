import matplotlib.pyplot as plt
import numpy as np

from synosys_styles import WES, WES_HL, use

use()

# ---------------------------------------------------------------------
# Palette preview
# ---------------------------------------------------------------------
ALL = {**WES, **WES_HL}

n = len(ALL)
fig, ax = plt.subplots(figsize=(1.6 * n, 2.4))

for i, (name, color) in enumerate(ALL.items()):
    ax.barh(0, 1, left=i, color=color)

    brightness = sum(color) / 3
    text_color = "black" if brightness > 0.6 else "white"

    ax.text(
        i + 0.5,
        0,
        name,
        ha="center",
        va="center",
        rotation=45,
        fontsize=10,
        color=text_color,
    )

ax.set_xlim(0, n)
ax.set_ylim(-0.7, 0.7)
ax.axis("off")

plt.tight_layout()
plt.savefig("docs/palette_preview.png", dpi=200, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------------
# Colormap preview
# ---------------------------------------------------------------------
cmaps = [
    ("wes", "wes"),
    ("wes_seq", "wes_seq"),
    ("wes_div", "wes_div"),
    ("wes_div_white", "wes_div_white"),
]

x = np.linspace(0, 1, 256)
grad = np.tile(x, (20, 1))

fig, axes = plt.subplots(len(cmaps), 1, figsize=(7, 2.8))

for ax, (label, cmap_name) in zip(axes, cmaps):
    ax.imshow(grad, aspect="auto", cmap=cmap_name)
    ax.text(
        -0.02,
        0.5,
        label,
        transform=ax.transAxes,
        ha="right",
        va="center",
        fontsize=10,
    )
    ax.axis("off")

plt.tight_layout()
plt.savefig("docs/wes_colormaps.png", dpi=200, bbox_inches="tight")
plt.close(fig)