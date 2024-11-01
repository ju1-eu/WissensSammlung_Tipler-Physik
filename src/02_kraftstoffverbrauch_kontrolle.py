import numpy as np
import matplotlib.pyplot as plt
from typing import Dict, Optional
from dataclasses import dataclass
import logging
from pathlib import Path
from datetime import datetime

# Logging konfigurieren
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class VerbrauchsKonstanten:
    """Konstanten für die Verbrauchsberechnung"""

    MIN_WIRKUNGSGRAD = 0.27
    MAX_WIRKUNGSGRAD = 0.33
    STANDARD_WIRKUNGSGRAD = 0.30
    RUNDUNG_NACHKOMMASTELLEN = 1

    # Referenzwerte für die Validierung
    REFERENZ_PUNKTE = {
        0.27: 17.5,  # 27% -> 17.5 l/100km
        0.30: 15.8,  # 30% -> 15.8 l/100km
        0.33: 14.4,  # 33% -> 14.4 l/100km
    }


@dataclass
class VerbrauchsParameter:
    """
    Parameter für die Kraftstoffverbrauchsberechnung

    Attributes:
        v_kmh: Geschwindigkeit [km/h]
        P_e: Effektive Motorleistung [kW]
        eta_e: Effektiver Wirkungsgrad [-]
        H_u: Unterer Heizwert [kJ/kg]
        rho_B: Kraftstoffdichte [kg/l]
    """

    v_kmh: float  # Geschwindigkeit [km/h]
    P_e: float  # Effektive Motorleistung [kW]
    eta_e: float  # Effektiver Wirkungsgrad [-]
    H_u: float  # Unterer Heizwert [kJ/kg]
    rho_B: float  # Kraftstoffdichte [kg/l]


class KraftstoffRechner:
    """Klasse zur Berechnung und Visualisierung des Kraftstoffverbrauchs"""

    def __init__(self, rundung: int = 1):
        """
        Initialisiert den Kraftstoffrechner

        Args:
            rundung: Anzahl der Nachkommastellen für Rundungen
        """
        self.konstanten = VerbrauchsKonstanten()
        self.rundung = rundung
        logger.info("KraftstoffRechner initialisiert")

    def validiere_parameter(self, params: VerbrauchsParameter) -> None:
        """
        Überprüft die Gültigkeit der Eingabeparameter

        Args:
            params: VerbrauchsParameter-Objekt

        Raises:
            ValueError: Wenn Parameter ungültig sind
        """
        if params.v_kmh <= 0:
            raise ValueError("Geschwindigkeit muss positiv sein")
        if params.P_e <= 0:
            raise ValueError("Motorleistung muss positiv sein")
        if not 0 < params.eta_e < 1:
            raise ValueError("Wirkungsgrad muss zwischen 0 und 1 liegen")
        if params.H_u <= 0:
            raise ValueError("Heizwert muss positiv sein")
        if params.rho_B <= 0:
            raise ValueError("Kraftstoffdichte muss positiv sein")

    def berechne_kraftstoffverbrauch(
        self, params: VerbrauchsParameter
    ) -> Dict[str, float]:
        """
        Berechnet den Kraftstoffverbrauch eines Fahrzeugs

        Args:
            params: VerbrauchsParameter-Objekt

        Returns:
            Dict mit Berechnungsergebnissen
        """
        self.validiere_parameter(params)

        # Berechnung des Massenstroms [kg/s]
        m_dot_B = (params.P_e * 1000) / (params.eta_e * params.H_u * 1000)

        # Berechnung des Volumenstroms [l/s, l/h]
        V_dot_B = m_dot_B / params.rho_B
        V_dot_B_h = V_dot_B * 3600

        # Berechnung des streckenbezogenen Verbrauchs [l/100km]
        B_100 = (V_dot_B_h / params.v_kmh) * 100

        return {
            "Massenstrom [kg/s]": round(m_dot_B, self.rundung),
            "Volumenstrom [l/s]": round(V_dot_B, self.rundung),
            "Volumenstrom [l/h]": round(V_dot_B_h, self.rundung),
            "Verbrauch [l/100km]": round(B_100, self.rundung),
        }

    def sensitivitaetsanalyse(
        self, params: VerbrauchsParameter, eta_bereich: Optional[list] = None
    ) -> Dict[float, float]:
        """
        Führt eine Sensitivitätsanalyse für verschiedene Wirkungsgrade durch

        Args:
            params: Basis-Parameter
            eta_bereich: Liste der zu testenden Wirkungsgrade

        Returns:
            Dict mit Wirkungsgraden und zugehörigen Verbräuchen
        """
        if eta_bereich is None:
            eta_bereich = [0.27, 0.30, 0.33]

        ergebnisse = {}
        for eta in eta_bereich:
            test_params = VerbrauchsParameter(
                v_kmh=params.v_kmh,
                P_e=params.P_e,
                eta_e=eta,
                H_u=params.H_u,
                rho_B=params.rho_B,
            )
            verbrauch = self.berechne_kraftstoffverbrauch(test_params)[
                "Verbrauch [l/100km]"
            ]
            ergebnisse[eta] = verbrauch

        return ergebnisse

    def erstelle_plot(self, params: VerbrauchsParameter) -> plt.Figure:
        """
        Erstellt einen Plot der Verbrauchskurve

        Args:
            params: Parameter für die Berechnung

        Returns:
            matplotlib Figure-Objekt
        """
        fig, ax = plt.subplots(figsize=(10, 6))

        # Wirkungsgrade für die Kurve
        eta_range = np.linspace(
            self.konstanten.MIN_WIRKUNGSGRAD, self.konstanten.MAX_WIRKUNGSGRAD, 100
        )

        # Verbrauchskurve berechnen
        verbrauch_range = []
        for eta in eta_range:
            test_params = VerbrauchsParameter(
                v_kmh=params.v_kmh,
                P_e=params.P_e,
                eta_e=eta,
                H_u=params.H_u,
                rho_B=params.rho_B,
            )
            verbrauch = self.berechne_kraftstoffverbrauch(test_params)[
                "Verbrauch [l/100km]"
            ]
            verbrauch_range.append(verbrauch)

        # Plot erstellen
        ax.plot(eta_range * 100, verbrauch_range, "b-", label="Verbrauchskurve")

        # Referenzpunkte markieren
        for eta, verbrauch in self.konstanten.REFERENZ_PUNKTE.items():
            ax.plot(eta * 100, verbrauch, "ro")
            ax.annotate(
                f"{verbrauch:.1f} l/100km",
                xy=(eta * 100, verbrauch),
                xytext=(5, 5),
                textcoords="offset points",
            )

        # Layout
        ax.set_xlabel("Motorwirkungsgrad η [%]")
        ax.set_ylabel("Kraftstoffverbrauch [l/100km]")
        ax.set_title(
            "Kraftstoffverbrauch bei 180 km/h\nAbhängigkeit vom Motorwirkungsgrad"
        )
        ax.grid(True)
        ax.legend()

        return fig

    def speichere_plot(self, fig: plt.Figure, prefix: str = "verbrauch") -> None:
        """
        Speichert den Plot als PNG und SVG

        Args:
            fig: matplotlib Figure-Objekt
            prefix: Präfix für den Dateinamen
        """
        # Erstelle Ausgabeordner
        output_dir = Path("output")
        output_dir.mkdir(exist_ok=True)

        # Zeitstempel für eindeutige Dateinamen
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        # Speichere als PNG und SVG
        for format in ["png", "svg"]:
            filename = f"{prefix}_{timestamp}.{format}"
            filepath = output_dir / filename
            fig.savefig(filepath, format=format, dpi=300, bbox_inches="tight")
            logger.info(f"Plot gespeichert als {filepath}")


def main():
    """Hauptfunktion mit Beispielberechnungen und Plot"""
    # Eingabewerte
    params = VerbrauchsParameter(
        v_kmh=180.0,  # Geschwindigkeit in km/h
        P_e=75.6,  # Motorleistung in kW
        eta_e=0.30,  # Wirkungsgrad 30%
        H_u=42000.0,  # Heizwert in kJ/kg
        rho_B=0.76,  # Kraftstoffdichte in kg/l
    )

    # Rechner initialisieren
    rechner = KraftstoffRechner()

    try:
        # Standardberechnung durchführen
        print("\nBerechnungsergebnisse:")
        print("-" * 50)
        ergebnis = rechner.berechne_kraftstoffverbrauch(params)
        for key, value in ergebnis.items():
            print(f"{key:<20}: {value:.1f}")

        # Sensitivitätsanalyse durchführen
        print("\nSensitivitätsanalyse - Wirkungsgrad:")
        print("-" * 50)
        sensitivitaet = rechner.sensitivitaetsanalyse(params)
        for eta, verbrauch in sensitivitaet.items():
            print(f"Wirkungsgrad {eta*100:>2.0f}%: {verbrauch:.1f} l/100km")

        # Plot erstellen und speichern
        fig = rechner.erstelle_plot(params)
        rechner.speichere_plot(fig)
        plt.show()

    except Exception as e:
        logger.error(f"Fehler bei der Berechnung: {e}")


if __name__ == "__main__":
    main()
