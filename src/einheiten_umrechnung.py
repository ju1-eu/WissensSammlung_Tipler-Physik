import numpy as np

print("Dieses Skript heißt einheiten_umrechnung.py")

# Umrechnung von Minuten in Stunden
t_min = 180
t_h = t_min / 60

print(f"{t_min} Minuten = {t_h} Stunden")

# Reifenabrieb berechnen
A = 1e-2  # 1 cm in Meter
s = 60e3  # 60000 km in Meter
Reifenabrieb = A / s

print(f"Reifenabrieb: {Reifenabrieb:.2e} m/km")