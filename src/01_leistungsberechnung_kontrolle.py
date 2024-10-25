import numpy as np
import pandas as pd
from dataclasses import dataclass
from typing import Dict

@dataclass
class Fahrzeugparameter:
    """Klasse für die Fahrzeugparameter der A-Klasse"""
    cw: float = 0.31          # Luftwiderstandsbeiwert
    A: float = 2.4           # Stirnfläche in m²
    m: float = 1270.0        # Fahrzeugmasse in kg
    v_kmh: float = 180.0     # Geschwindigkeit in km/h
    g: float = 9.81          # Erdbeschleunigung in m/s²
    beta: float = 0.0        # Steigungswinkel in Grad
    rho: float = 1.189       # Luftdichte in kg/m³

@dataclass
class Variante:
    """Klasse für die variantenspezifischen Parameter"""
    eta_getriebe: float      # Getriebewirkungsgrad
    mu: float               # Rollwiderstandsbeiwert

class LeistungsBerechnung:
    def __init__(self, parameter: Fahrzeugparameter):
        self.parameter = parameter
        self.v_ms = parameter.v_kmh / 3.6  # Geschwindigkeit in m/s
    
    def berechne_luftwiderstandskraft(self) -> float:
        """Berechnet die Luftwiderstandskraft"""
        F_cw = (0.5 * self.parameter.rho * self.v_ms**2 * 
                self.parameter.cw * self.parameter.A)
        return round(F_cw, 2)
    
    def berechne_rollwiderstandskraft(self, mu: float) -> float:
        """Berechnet die Rollwiderstandskraft"""
        F_roll = (mu * self.parameter.m * self.parameter.g * 
                 np.cos(np.radians(self.parameter.beta)))
        return round(F_roll, 2)
    
    def berechne_steigungskraft(self) -> float:
        """Berechnet die Steigungskraft"""
        F_steig = (self.parameter.m * self.parameter.g * 
                  np.sin(np.radians(self.parameter.beta)))
        return round(F_steig, 2)
    
    def berechne_variante(self, variante: Variante) -> Dict[str, float]:
        """Berechnet alle Werte für eine Variante"""
        # Kräfte
        F_cw = self.berechne_luftwiderstandskraft()
        F_roll = self.berechne_rollwiderstandskraft(variante.mu)
        F_steig = self.berechne_steigungskraft()
        F_gesamt = F_cw + F_roll + F_steig
        
        # Leistungen
        P_rad = F_gesamt * self.v_ms / 1000  # Umrechnung in kW
        P_motor = P_rad / variante.eta_getriebe
        
        return {
            'F_cw': F_cw,
            'F_roll': F_roll,
            'F_steig': F_steig,
            'F_gesamt': F_gesamt,
            'P_rad': round(P_rad, 2),
            'P_motor': round(P_motor, 2)
        }

def main():
    # Parameter initialisieren
    parameter = Fahrzeugparameter()
    
    # Varianten definieren
    variante0 = Variante(eta_getriebe=0.92, mu=0.015)
    variante2 = Variante(eta_getriebe=0.90, mu=0.0205)
    
    # Berechnung durchführen
    berechnung = LeistungsBerechnung(parameter)
    ergebnis_v0 = berechnung.berechne_variante(variante0)
    ergebnis_v2 = berechnung.berechne_variante(variante2)
    
    # Ergebnisse in DataFrame für Vergleich
    df_ergebnisse = pd.DataFrame({
        'Variante 0': ergebnis_v0,
        'Variante 2': ergebnis_v2
    })
    
    # Differenzen berechnen
    df_ergebnisse['Differenz'] = (df_ergebnisse['Variante 2'] - 
                                 df_ergebnisse['Variante 0'])
    
    # Parameter-Tabelle erstellen
    parameter_dict = {
        'η_Getriebe': [variante0.eta_getriebe, variante2.eta_getriebe],
        'μ': [variante0.mu, variante2.mu]
    }
    df_parameter = pd.DataFrame(parameter_dict, 
                              index=['Variante 0', 'Variante 2'])
    
    # Prozentuale Änderungen berechnen
    proz_aenderung = {
        'η_Getriebe': ((variante2.eta_getriebe - variante0.eta_getriebe) / 
                      variante0.eta_getriebe * 100),
        'μ': ((variante2.mu - variante0.mu) / variante0.mu * 100),
        'Motorleistung': ((ergebnis_v2['P_motor'] - ergebnis_v0['P_motor']) / 
                         ergebnis_v0['P_motor'] * 100)
    }
    
    # Ausgabe
    print("A-Klasse Leistungsberechnung bei 180 km/h\n")
    
    print("1. Fahrzeugparameter:")
    for key, value in vars(parameter).items():
        print(f"{key:12} = {value}")
    print()
    
    print("2. Variantenparameter:")
    print(df_parameter)
    print()
    
    print("3. Berechnete Werte:")
    print(df_ergebnisse.round(2))
    print()
    
    print("4. Prozentuale Änderungen:")
    for key, value in proz_aenderung.items():
        print(f"{key:15} = {value:6.1f}%")

if __name__ == "__main__":
    main()