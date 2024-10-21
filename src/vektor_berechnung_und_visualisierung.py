# Dateiname: vektor_berechnung_und_visualisierung.py

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_vector(ax, vector, color, label):
    ax.quiver(0, 0, 0, vector[0], vector[1], vector[2], color=color, arrow_length_ratio=0.1, label=label)
    # Endpunkt des Vektors
    endpoint = vector
    # Text mit Koordinaten und Länge am Endpunkt des Vektors
    ax.text(endpoint[0], endpoint[1], endpoint[2], 
            f'{label}\n({vector[0]:.1f}, {vector[1]:.1f}, {vector[2]:.1f})\nLänge: {np.linalg.norm(vector):.2f}', 
            color=color)

def set_axes_equal(ax, vectors):
    max_range = np.array([abs(vec).max() for vec in vectors]).max()
    ax.set_xlim3d([-max_range, max_range])
    ax.set_ylim3d([-max_range, max_range])
    ax.set_zlim3d([-max_range, max_range])

# Gegebene Vektoren definieren
a = np.array([-2, 3, 1])
b = np.array([0, -1, 4])
c = np.array([6, -1, 2])

# Vektoren x, y und z berechnen
x = -2*a + 3*b + 5*c
y = 5*(b - 3*a) - 2*c
z = 3*(a + b) - 5*(b - c) + a

# 3D-Plot erstellen
fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='3d')

# Vektoren x, y und z zeichnen
plot_vector(ax, x, 'r', 'x')
plot_vector(ax, y, 'g', 'y')
plot_vector(ax, z, 'b', 'z')

# Ursprung markieren
ax.scatter(0, 0, 0, color='k', s=100, label='Ursprung (0,0,0)')

# Achsen beschriften
ax.set_xlabel('X-Achse')
ax.set_ylabel('Y-Achse')
ax.set_zlabel('Z-Achse')

# Legende hinzufügen
ax.legend()

# Titel hinzufügen
plt.title('Visualisierung der Vektoren x, y und z')

# Achsen gleichmäßig skalieren
set_axes_equal(ax, [x, y, z])

# Ansicht anpassen
ax.view_init(elev=20, azim=45)

# Als PNG speichern
plt.savefig('vektoren_visualisierung.png', dpi=300, bbox_inches='tight')

# Als SVG speichern
plt.savefig('vektoren_visualisierung.svg', format='svg', bbox_inches='tight')

print("Visualisierung wurde als PNG und SVG gespeichert.")

# Plot anzeigen (optional, wenn Sie das Ergebnis direkt sehen möchten)
plt.show()