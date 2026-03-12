import numpy as np
import matplotlib.pyplot as plt

import synosys_styles as ss


# activate SynoSys style
ss.use()


# data
x = np.linspace(0, 10, 500)

frequencies = [0.6, 0.8, 1.0, 1.2, 1.4]

colors = [
    "wes_mint",
    "wes_teal",
    "wes_sand",
    "wes_rust",
    "wes_plum",
]


fig, ax = plt.subplots(figsize=(7, 4))


# plot sine waves
for f, c in zip(frequencies, colors):
    y = np.sin(f * x)
    ax.plot(x, y, color=c, linewidth=2, label=rf"$\omega={f}$")


# highlighted reference curve
y_ref = np.sin(1.0 * x)
ax.plot(x, y_ref, color="wes_hl_crimson", linewidth=3, label="reference")


ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$\sin(\omega x)$")

ax.legend()

plt.tight_layout()

# save example figure for README
plt.savefig("docs/example_plot.png", dpi=200, bbox_inches="tight")

plt.show()