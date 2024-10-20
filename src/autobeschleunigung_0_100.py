import numpy as np
import matplotlib.pyplot as plt

# Parameter
m = 1200  # Masse in kg
t = np.linspace(0, 7, 100)  # Zeitpunkte
v_end = 27.78  # Endgeschwindigkeit in m/s (100 km/h)

# Berechnung der Geschwindigkeit und Position
a = v_end / 7  # Durchschnittliche Beschleunigung
v = a * t  # Geschwindigkeit
s = 0.5 * a * t**2  # Zurückgelegte Strecke

# Kräfte berechnen (vereinfacht)
F_antrieb = m * a * np.ones_like(t)  # Antriebskraft (konstant angenommen)
F_luft = 0.5 * 1.225 * 0.3 * 2 * v**2  # Luftwiderstand (geschätzte Parameter)
F_roll = 0.015 * m * 9.81 * np.ones_like(t)  # Rollwiderstand (geschätzt)

# Plotting
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 15))
fig.suptitle('Analyse der Autobeschleunigung: 0-100 km/h in 7s', fontsize=16)

# Geschwindigkeit und Strecke
ax1.plot(t, v * 3.6, 'b-', label='Geschwindigkeit')
ax1.set_ylabel('Geschwindigkeit (km/h)')
ax1.legend(loc='lower right')
ax1.grid(True)

ax1_twin = ax1.twinx()
ax1_twin.plot(t, s, 'r-', label='Strecke')
ax1_twin.set_ylabel('Zurückgelegte Strecke (m)')
ax1_twin.legend(loc='upper left')

ax1.set_title('Geschwindigkeit und zurückgelegte Strecke')

# Kräfte
ax2.plot(t, F_antrieb, 'g-', label='Antriebskraft')
ax2.plot(t, F_luft, 'r-', label='Luftwiderstand')
ax2.plot(t, F_roll, 'b-', label='Rollwiderstand')
ax2.set_xlabel('Zeit (s)')
ax2.set_ylabel('Kraft (N)')
ax2.legend()
ax2.grid(True)
ax2.set_title('Wirkende Kräfte')

# Beschleunigung
ax3.plot(t, a * np.ones_like(t), 'k-', label='Durchschnittliche Beschleunigung')
ax3.set_xlabel('Zeit (s)')
ax3.set_ylabel('Beschleunigung (m/s²)')
ax3.legend()
ax3.grid(True)
ax3.set_title('Beschleunigung')

plt.tight_layout()
plt.savefig('autobeschleunigung_0_100.png', format='png', dpi=300, bbox_inches='tight')
plt.savefig('autobeschleunigung_0_100.svg', format='svg', dpi=300, bbox_inches='tight')
print("Abbildung als PNG und SVG gespeichert.")
plt.show()