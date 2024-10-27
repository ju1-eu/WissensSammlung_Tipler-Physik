"""
Vektorberechnungen für physikalische Aufgaben

Dieses Modul implementiert Berechnungen für:
1. Bär-Verschiebung (Vektoraddition)
2. Schiffsposition (Trigonometrie)

Beispielverwendung:
    rechner = VektorBerechnung()
    ergebnis = rechner.berechne_baer_verschiebung(12, 45, 12, 0)
    print(f"Gesamtverschiebung: {ergebnis['betrag']} m")

Autor: [Name]
Datum: 2024-10-27
Version: 1.0
"""

import numpy as np
from typing import Dict, Union, List
import unittest

class BerechnungsFehler(Exception):
    """Basisklasse für Berechnungsfehler"""
    pass

class EingabeFehler(BerechnungsFehler):
    """Fehler bei ungültigen Eingabewerten"""
    pass

class VektorBerechnung:
    """Klasse für physikalische Vektorberechnungen"""
    
    def __init__(self):
        """Initialisierung der Klasse für Vektorberechnungen"""
        self.setup_constants()
        
    def setup_constants(self):
        """Definition von Konstanten"""
        self.DEG_TO_RAD = np.pi / 180
        self.RAD_TO_DEG = 180 / np.pi
        
    def _validiere_winkel(self, winkel: float) -> None:
        """
        Überprüft, ob ein Winkel im gültigen Bereich liegt
        
        Args:
            winkel: Winkel in Grad
            
        Raises:
            EingabeFehler: Wenn der Winkel ungültig ist
        """
        if not (0 <= winkel <= 360):
            raise EingabeFehler(f"Winkel {winkel} muss zwischen 0 und 360 Grad liegen")
            
    def _validiere_betrag(self, betrag: float, name: str) -> None:
        """
        Überprüft, ob ein Betrag positiv ist
        
        Args:
            betrag: Zu prüfender Betrag
            name: Name der Größe für Fehlermeldung
            
        Raises:
            EingabeFehler: Wenn der Betrag negativ ist
        """
        if betrag < 0:
            raise EingabeFehler(f"{name} muss positiv sein")
            
    def _pruefe_plausibilitaet(self, ergebnis: Dict[str, float]) -> None:
        """
        Prüft die Plausibilität der Ergebnisse
        
        Args:
            ergebnis: Dictionary mit Berechnungsergebnissen
            
        Raises:
            BerechnungsFehler: Bei unplausiblen Ergebnissen
        """
        if ergebnis.get('betrag', 0) < 0:
            raise BerechnungsFehler("Negativer Betrag berechnet")
            
    def berechne_baer_verschiebung(self, 
                                  r1_betrag: float, 
                                  r1_winkel: float, 
                                  r2_betrag: float, 
                                  r2_winkel: float) -> Dict[str, float]:
        """
        Berechnet die Gesamtverschiebung und den Rückweg für den Bären
        
        Args:
            r1_betrag: Länge der ersten Verschiebung [m]
            r1_winkel: Winkel der ersten Verschiebung [grad]
            r2_betrag: Länge der zweiten Verschiebung [m]
            r2_winkel: Winkel der zweiten Verschiebung [grad]
            
        Returns:
            Dictionary mit Berechnungsergebnissen
            
        Raises:
            EingabeFehler: Bei ungültigen Eingabewerten
            BerechnungsFehler: Bei Berechnungsproblemen
        """
        # Eingabevalidierung
        self._validiere_betrag(r1_betrag, "Erste Verschiebung")
        self._validiere_betrag(r2_betrag, "Zweite Verschiebung")
        self._validiere_winkel(r1_winkel)
        self._validiere_winkel(r2_winkel)
        
        try:
            # Vektorzerlegung der ersten Verschiebung
            dx1 = r1_betrag * np.cos(r1_winkel * self.DEG_TO_RAD)
            dy1 = r1_betrag * np.sin(r1_winkel * self.DEG_TO_RAD)
            
            # Vektorzerlegung der zweiten Verschiebung
            dx2 = r2_betrag * np.cos(r2_winkel * self.DEG_TO_RAD)
            dy2 = r2_betrag * np.sin(r2_winkel * self.DEG_TO_RAD)
            
            # Gesamtverschiebung
            dx_ges = dx1 + dx2
            dy_ges = dy1 + dy2
            
            # Rückweg berechnen
            betrag = np.sqrt(dx_ges**2 + dy_ges**2)
            winkel = np.arctan2(dy_ges, dx_ges) * self.RAD_TO_DEG
            
            # Winkel in [0, 360] umrechnen
            if winkel < 0:
                winkel += 360
                
            ergebnis = {
                'dx_ges': dx_ges,
                'dy_ges': dy_ges,
                'betrag': betrag,
                'winkel': winkel
            }
            
            # Plausibilitätsprüfung
            self._pruefe_plausibilitaet(ergebnis)
            
            return ergebnis
            
        except Exception as e:
            raise BerechnungsFehler(f"Fehler bei Bär-Verschiebung: {str(e)}")
            
    def berechne_schiffsposition(self, 
                               abstand_sender: float, 
                               winkel_a: float) -> Dict[str, float]:
        """
        Berechnet die Position des Schiffs
        
        Args:
            abstand_sender: Abstand zwischen Sender A und B [km]
            winkel_a: Winkel des Signals von Sender A [grad]
            
        Returns:
            Dictionary mit Berechnungsergebnissen
            
        Raises:
            EingabeFehler: Bei ungültigen Eingabewerten
            BerechnungsFehler: Bei Berechnungsproblemen
        """
        # Eingabevalidierung
        self._validiere_betrag(abstand_sender, "Senderabstand")
        self._validiere_winkel(winkel_a)
        
        try:
            # Berechnung der x-Position
            x_schiff = abstand_sender / np.tan(winkel_a * self.DEG_TO_RAD)
            
            # y-Position ist 0 (Schiff liegt auf x-Achse)
            y_schiff = 0
            
            # Entfernung zu Sender B berechnen
            entfernung = np.sqrt(x_schiff**2 + y_schiff**2)
            
            ergebnis = {
                'x_position': x_schiff,
                'y_position': y_schiff,
                'entfernung': entfernung
            }
            
            return ergebnis
            
        except Exception as e:
            raise BerechnungsFehler(f"Fehler bei Schiffsposition: {str(e)}")
            
    def formatiere_ergebnis(self, 
                           wert: float, 
                           einheit: str, 
                           nachkommastellen: int = 2) -> str:
        """
        Formatiert einen Zahlenwert mit Einheit
        
        Args:
            wert: Zu formatierender Zahlenwert
            einheit: Einheit als String
            nachkommastellen: Anzahl der Nachkommastellen
            
        Returns:
            Formatierter String mit Wert und Einheit
        """
        return f"{wert:.{nachkommastellen}f} {einheit}"
        
    def _formatiere_ausgabe(self, ergebnis: Dict[str, float]) -> str:
        """
        Erstellt formatierte Ausgabe der Ergebnisse
        
        Args:
            ergebnis: Dictionary mit Berechnungsergebnissen
            
        Returns:
            Formatierte Ausgabe als String
        """
        ausgabe = []
        for key, value in ergebnis.items():
            if 'winkel' in key:
                ausgabe.append(f"{key}: {self.formatiere_ergebnis(value, '°', 1)}")
            else:
                ausgabe.append(f"{key}: {self.formatiere_ergebnis(value, 'm')}")
        return "\n".join(ausgabe)

class TestVektorBerechnung(unittest.TestCase):
    """Testklasse für VektorBerechnung"""
    
    def setUp(self):
        """Test-Setup"""
        self.rechner = VektorBerechnung()
        
    def test_baer_verschiebung(self):
        """Test der Bär-Verschiebung mit bekannten Werten"""
        ergebnis = self.rechner.berechne_baer_verschiebung(12, 45, 12, 0)
        self.assertAlmostEqual(ergebnis['betrag'], 22.14, places=2)
        
    def test_schiffsposition(self):
        """Test der Schiffsposition mit bekannten Werten"""
        ergebnis = self.rechner.berechne_schiffsposition(100, 30)
        self.assertAlmostEqual(ergebnis['entfernung'], 173.21, places=2)
        
    def test_ungueltige_eingabe(self):
        """Test der Fehlerbehandlung bei ungültigen Eingaben"""
        with self.assertRaises(EingabeFehler):
            self.rechner.berechne_baer_verschiebung(-1, 45, 12, 0)

def main():
    """Hauptprogramm mit Benutzerinteraktion"""
    rechner = VektorBerechnung()
    
    print("\nVektorberechnungen")
    print("-----------------")
    print("1. Bär-Verschiebung")
    print("2. Schiffsposition")
    
    try:
        wahl = input("\nBitte wählen (1/2): ")
        
        if wahl == "1":
            # Bär-Verschiebung Eingaben
            r1_betrag = float(input("Erste Verschiebung (m): "))
            r1_winkel = float(input("Erster Winkel (Grad): "))
            r2_betrag = float(input("Zweite Verschiebung (m): "))
            r2_winkel = float(input("Zweiter Winkel (Grad): "))
            
            ergebnis = rechner.berechne_baer_verschiebung(r1_betrag, r1_winkel, 
                                                         r2_betrag, r2_winkel)
            print("\nErgebnis:")
            print(rechner._formatiere_ausgabe(ergebnis))
            
        elif wahl == "2":
            # Schiffsposition Eingaben
            abstand = float(input("Abstand der Sender (km): "))
            winkel = float(input("Winkel von Sender A (Grad): "))
            
            ergebnis = rechner.berechne_schiffsposition(abstand, winkel)
            print("\nErgebnis:")
            print(rechner._formatiere_ausgabe(ergebnis))
            
        else:
            print("Ungültige Eingabe!")
            
    except ValueError as e:
        print(f"Eingabefehler: {str(e)}")
    except BerechnungsFehler as e:
        print(f"Berechnungsfehler: {str(e)}")
    except Exception as e:
        print(f"Unerwarteter Fehler: {str(e)}")

if __name__ == "__main__":
    main()