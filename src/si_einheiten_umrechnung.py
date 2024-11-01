# si_einheiten_umrechnung.py
import sys

print(f"Python Version: {sys.version}")
print(f"Version Info: {sys.version_info}")
print(f"Python Executable: {sys.executable}")


class SymbolicUnitsCollection:
    def __init__(self):
        self.units = {
            "A": "ampere",
            "K": "kelvin",
            "kg": "kilogram",
            "m": "meter",
            "mol": "mole",
            "s": "second",
            "cd": "candela",
            "min": "minute",
            "h": "hour",
        }

    def __getattr__(self, unit):
        if unit in self.units:
            return unit
        raise AttributeError(f"Unit '{unit}' not found")

    def show_all_units(self):
        for symbol, name in self.units.items():
            print(f"{name}: [{symbol}]")


class SI_Unit:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def __str__(self):
        return f"{self.value}*[{self.unit}]"


def unitConvert(time, new_unit):
    conversions = {
        ("min", "h"): lambda x: x / 60,
        ("h", "min"): lambda x: x * 60,
    }
    if (time.unit, new_unit) in conversions:
        new_value = conversions[(time.unit, new_unit)](time.value)
        return SI_Unit(new_value, new_unit)
    else:
        raise ValueError(f"Conversion from {time.unit} to {new_unit} not supported")


# Erstellen der Einheitensammlung
u = SymbolicUnitsCollection()
print("symbolicUnitsCollection with units:")
u.show_all_units()

# Definition der Zeit in Minuten
t = SI_Unit(180, u.min)
print(f"\nUrsprüngliche Zeit: {t}")

# Umrechnung der Zeit in Stunden
t = unitConvert(t, u.h)
print(f"Zeit in Stunden: {t}")

# Trennen der Einheit vom Wert (äquivalent zu separateUnits)
wert = t.value
einheit = t.unit

print(f"\nGetrennter Wert: {wert}")
print(f"Getrennte Einheit: [{einheit}]")
