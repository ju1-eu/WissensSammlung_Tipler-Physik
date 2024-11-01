# schwingungsdauer_analyse.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Schwingungsdauer-Werte direkt im Skript definieren
T = np.array([2.05, 1.99, 2.06, 1.97, 2.01, 2.00, 2.03, 1.97, 2.02, 1.96])

print("Schwingungsdauer-Werte:")
print(T)

# Berechnung der statistischen Kenngrößen
T_mittel = np.mean(T)
T_std = np.std(T, ddof=1)
T_std_mittelwert = T_std / np.sqrt(len(T))

print(f"\nMittlere Schwingungsdauer <T>: {T_mittel:.3f} s")
print(f"Standardabweichung σ_T: {T_std:.3f} s")
print(f"Standardabweichung des Mittelwerts σ_<T>: {T_std_mittelwert:.3f} s")

# Histogramm erstellen
plt.figure(figsize=(10, 6))
plt.hist(T, bins="auto", edgecolor="black")
plt.title("Verteilung der Schwingungsdauer-Messungen")
plt.xlabel("Schwingungsdauer (s)")
plt.ylabel("Häufigkeit")
plt.axvline(
    T_mittel,
    color="r",
    linestyle="dashed",
    linewidth=2,
    label=f"Mittelwert: {T_mittel:.3f} s",
)
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig("schwingungsdauer_histogramm.png")
plt.show()

# Optional: Daten in Excel-Datei speichern
df = pd.DataFrame({"Messung": range(1, len(T) + 1), "Schwingungsdauer (s)": T})
df.to_excel("schwingungsdauer_messungen.xlsx", index=False)
print("\nDaten wurden in 'schwingungsdauer_messungen.xlsx' gespeichert.")
