import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arrow

# Parameter
m = 0.4  # Masse in kg
F1 = np.array([-2.00, -4.00])  # Kraft 1 in N
F2 = np.array([-2.60, 5.00])   # Kraft 2 in N
F = F1 + F2  # Gesamtkraft in N
a = F / m  # Beschleunigung in m/s^2

# Zeitpunkte
t = np.linspace(0, 2, 100)

# Berechnung der Position
x = 0.5 * a[0] * t**2
y = 0.5 * a[1] * t**2

# Berechnung der Geschwindigkeit
vx = a[0] * t
vy = a[1] * t

# Erstellen der Figur und der Achsen
fig, ax = plt.subplots(figsize=(10, 8))

# Zeichnen der Bahn
ax.plot(x, y, 'b-', label='Bahn des Teilchens')

# Markieren der Position bei t=1.6s
t_mark = 1.6
x_mark = 0.5 * a[0] * t_mark**2
y_mark = 0.5 * a[1] * t_mark**2
ax.plot(x_mark, y_mark, 'ro', markersize=10, label='Position bei t=1.6s')

# Zeichnen des Geschwindigkeitsvektors bei t=1.6s
v_scale = 0.5  # Skalierungsfaktor für die Darstellung des Geschwindigkeitsvektors
vx_mark = a[0] * t_mark
vy_mark = a[1] * t_mark
ax.add_patch(Arrow(x_mark, y_mark, v_scale*vx_mark, v_scale*vy_mark, 
                   width=0.5, color='g', label='Geschwindigkeit bei t=1.6s'))

# Zeichnen der Kraftvektoren am Ursprung
force_scale = 1  # Skalierungsfaktor für die Darstellung der Kraftvektoren
ax.add_patch(Arrow(0, 0, force_scale*F1[0], force_scale*F1[1], width=0.3, color='m', label='Kraft F1'))
ax.add_patch(Arrow(0, 0, force_scale*F2[0], force_scale*F2[1], width=0.3, color='c', label='Kraft F2'))
ax.add_patch(Arrow(0, 0, force_scale*F[0], force_scale*F[1], width=0.3, color='r', label='Gesamtkraft F'))

# Achsenbeschriftungen und Titel
ax.set_xlabel('x-Position (m)')
ax.set_ylabel('y-Position (m)')
ax.set_title('Bewegung eines Teilchens unter Einfluss von zwei Kräften')

# Legende
ax.legend()

# Gleiche Skalierung für beide Achsen
ax.set_aspect('equal')

# Gitternetz hinzufügen
ax.grid(True)

plt.savefig('newtons_bewegungsgleichungen.png', format='png', dpi=300, bbox_inches='tight')
plt.savefig('newtons_bewegungsgleichungen.svg', format='svg', dpi=300, bbox_inches='tight')
print("Abbildung als PNG und SVG gespeichert.")
# Anzeigen der Figur
plt.show()