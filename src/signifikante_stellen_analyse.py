import numpy as np
import matplotlib.pyplot as plt

print("Dieses Skript heißt signifikante_stellen_analyse.py")

# Eingabe der Punktzahlen
P = np.array([25, 22, 22, 20, 20, 20, 18, 18, 18, 18, 18, 15, 15, 15, 10])

# Berechnung des Mittelwerts
s_mean = np.mean(P)

# Berechnung des quadratisch gemittelten Ergebnisses
s_rms = np.sqrt(np.mean(P**2))

print(f"Mittleres Ergebnis: {s_mean:.1f} Punkte")
print(f"Quadratisch gemitteltes Ergebnis: {s_rms:.1f} Punkte")

# Histogramm erstellen
plt.figure(figsize=(10, 6))
plt.hist(P, bins=range(min(P), max(P)+2, 1), align='left', rwidth=0.8)
plt.xlabel('Punktzahl')
plt.ylabel('Häufigkeit')
plt.title('Verteilung der Punktzahlen')
plt.grid(True, alpha=0.3)
plt.show()