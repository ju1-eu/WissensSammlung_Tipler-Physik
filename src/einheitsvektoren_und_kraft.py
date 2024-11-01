import matplotlib.pyplot as plt
import numpy as np

# Definieren der Kräfte
F1 = np.array([3, -2])
F2 = np.array([-1, 4])
F_res = F1 + F2

# Erstellen der Figur und der Achsen
fig, ax = plt.subplots(figsize=(10, 10))

# Zeichnen der Einheitsvektoren
ax.quiver(
    0,
    0,
    1,
    0,
    angles="xy",
    scale_units="xy",
    scale=1,
    color="gray",
    label="Einheitsvektor x",
)
ax.quiver(
    0,
    0,
    0,
    1,
    angles="xy",
    scale_units="xy",
    scale=1,
    color="gray",
    label="Einheitsvektor y",
)

# Zeichnen der Kräfte
ax.quiver(
    0, 0, F1[0], F1[1], angles="xy", scale_units="xy", scale=1, color="r", label="F1"
)
ax.quiver(
    0, 0, F2[0], F2[1], angles="xy", scale_units="xy", scale=1, color="b", label="F2"
)
ax.quiver(
    0,
    0,
    F_res[0],
    F_res[1],
    angles="xy",
    scale_units="xy",
    scale=1,
    color="g",
    label="F_res",
)

# Beschriftungen und Titel
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Vektordarstellung der Kräfte und resultierenden Kraft")

# Grenzen der Achsen setzen
ax.set_xlim(-3, 4)
ax.set_ylim(-3, 5)

# Gitter hinzufügen
ax.grid(True)

# Ursprung markieren
ax.plot(0, 0, "ko", markersize=10)

# Legende hinzufügen
ax.legend()

# Gleiche Skalierung für beide Achsen
ax.set_aspect("equal")
plt.savefig(
    "einheitsvektoren_und_kraft.png", format="png", dpi=300, bbox_inches="tight"
)
plt.savefig(
    "einheitsvektoren_und_kraft.svg", format="svg", dpi=300, bbox_inches="tight"
)
print("Abbildung als PNG und SVG gespeichert.")
# Anzeigen des Plots
plt.show()
