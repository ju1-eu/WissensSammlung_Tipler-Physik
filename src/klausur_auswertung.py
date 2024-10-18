# klausur_auswertung.py

import numpy as np
import matplotlib.pyplot as plt

# Eingabe der Klausurergebnisse in einen Vektor
P = np.array([25, 22, 22, 20, 20, 20, 18, 18, 18, 18, 18, 15, 15, 15, 10])

# Berechnung des Mittelwerts
s = np.mean(P)

# Berechnung des quadratischen Mittelwerts (RMS)
srms = np.sqrt(np.mean(P**2))

# Ausgabe der Ergebnisse
print(f"Mittleres Ergebnis <s>: {s:.1f} Punkte")
print(f"Quadratisch gemitteltes Ergebnis s_rms: {srms:.1f} Punkte")

# Berechnung der Differenz und des prozentualen Unterschieds
diff = srms - s
prozent_diff = (diff / s) * 100

print(f"Differenz (s_rms - <s>): {diff:.2f} Punkte")
print(f"Prozentualer Unterschied: {prozent_diff:.2f}%")

# Erstellen eines Histogramms
plt.figure(figsize=(10, 6))
plt.hist(P, bins=range(min(P), max(P)+2, 1), edgecolor='black', align='left')
plt.title('Verteilung der Klausurergebnisse')
plt.xlabel('Punktzahl')
plt.ylabel('Häufigkeit')
plt.xticks(range(min(P), max(P)+1, 1))
plt.grid(True, alpha=0.3)

# Hinzufügen von Mittelwert und RMS als vertikale Linien
plt.axvline(s, color='r', linestyle='dashed', linewidth=2, label=f'Mittelwert ({s:.1f})')
plt.axvline(srms, color='g', linestyle='dashed', linewidth=2, label=f'RMS ({srms:.1f})')

plt.legend()
plt.savefig('klausur_histogramm.png')
plt.show()

# Berechnung zusätzlicher statistischer Kennzahlen
median = np.median(P)
std_dev = np.std(P)
min_val = np.min(P)
max_val = np.max(P)

print(f"\nZusätzliche statistische Kennzahlen:")
print(f"Median: {median:.1f} Punkte")
print(f"Standardabweichung: {std_dev:.2f} Punkte")
print(f"Minimum: {min_val} Punkte")
print(f"Maximum: {max_val} Punkte")