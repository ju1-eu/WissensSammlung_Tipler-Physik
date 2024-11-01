# reifenabrieb_berechnung.py

from decimal import Decimal, getcontext

# Setze die Präzision für Decimal
getcontext().prec = 15

# Eingabe der Werte
A = Decimal("1e-2")  # Abrieb in Meter
s = Decimal("60e3")  # Fahrstrecke in Kilometer

# Berechnung des Reifenabriebs pro Kilometer
reifenabrieb = A / s

print(f"Reifenabrieb (wissenschaftliche Notation): {reifenabrieb:.2e}")


# Funktion zur Ausgabe mit bestimmter Anzahl signifikanter Stellen
def vpa(zahl, stellen):
    return f"{zahl:.{stellen}e}"


# Ausgabe mit zwei signifikanten Stellen
ergebnis = vpa(reifenabrieb, 2)
print(f"Reifenabrieb (2 signifikante Stellen): {ergebnis}")

# Formatierte Ausgabe des Endergebnisses
print("\nFür den Abrieb A eines Autoreifens erhalten wir das Ergebnis:")
print(f"A = {ergebnis} m Abrieb pro km Fahrt")

# Plausibilitätsprüfung
gesamtabrieb = reifenabrieb * s
print("\nPlausibilitätsprüfung:")
print(f"Gesamtabrieb über {s:.0f} km: {gesamtabrieb:.2e} m")

# Weiterführende Betrachtung
atom_durchmesser = Decimal("2e-10")  # Meter
atomlagen_pro_km = reifenabrieb / atom_durchmesser
print("\nWeiterführende Betrachtung:")
print(f"Anzahl der Atomlagen pro km: {atomlagen_pro_km:.0f}")
