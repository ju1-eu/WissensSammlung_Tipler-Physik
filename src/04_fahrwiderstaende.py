"""
Fahrwiderstandsanalyse für PKW
=============================

Visualisierung und Analyse der Bedeutung von Roll- und Luftwiderstand
bei verschiedenen Geschwindigkeiten.

Kernfrage: Was ist beim PKW wichtiger - Rollwiderstand oder Luftwiderstand?

Lernziele:
- Methode der linearen Interpolation
- Größenordnung der Fahrwiderstandskräfte
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import os
from dataclasses import dataclass
from typing import Tuple

# Farbschema gemäß Anforderungen
COLORS = {
    "roll": "#EE9A00",  # orange2
    "ges": "#B22222",  # firebrick
    "diff": "#000000",  # Schwarz für Differenzmarkierung
}


@dataclass
class InterpolationPoints:
    """Stützstellen für die lineare Interpolation des Rollwiderstands."""

    v1: float = 50.0  # Geschwindigkeit Punkt 1 [km/h]
    v2: float = 150.0  # Geschwindigkeit Punkt 2 [km/h]
    f1: float = 0.008  # Rollwiderstandskoeff. bei v1
    f2: float = 0.015  # Rollwiderstandskoeff. bei v2


class FahrwiderstandAnalyse:
    """Analyse und Visualisierung der Fahrwiderstände."""

    def __init__(self):
        self.points = InterpolationPoints()
        self.setup_visualization()

    def linear_interpolation(self, v: np.ndarray) -> np.ndarray:
        """
        Berechnet den Rollwiderstandskoeffizienten durch lineare Interpolation.

        Formel: y = (y2-y1)/(x2-x1) * (x-x1) + y1
        """
        p = self.points
        f_roll = np.where(
            v <= p.v1,
            p.f1,
            np.where(
                v >= p.v2, p.f2, p.f1 + (p.f2 - p.f1) * (v - p.v1) / (p.v2 - p.v1)
            ),
        )
        return f_roll

    def calculate_power(self, v: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        """Berechnet Roll- und Gesamtwiderstandsleistung."""
        # Geschwindigkeit in m/s
        v_ms = v / 3.6

        # Rollwiderstand
        f_roll = self.linear_interpolation(v)
        P_roll = 1500 * 9.81 * f_roll * v_ms / 1000  # [kW]

        # Luftwiderstand (cw*A = 0.6, rho = 1.225)
        P_air = 0.5 * 1.225 * 0.6 * v_ms**3 / 1000  # [kW]

        return P_roll, P_roll + P_air

    def setup_visualization(self):
        """Initialisiert die Visualisierung mit zwei Plots."""
        self.fig, (self.ax1, self.ax2) = plt.subplots(2, 1, figsize=(10, 12))
        plt.subplots_adjust(bottom=0.1, hspace=0.3)

        for ax in [self.ax1, self.ax2]:
            ax.grid(True, linestyle="--", alpha=0.7)
            ax.set_xlabel("Geschwindigkeit v in km/h")
            ax.set_ylabel("Leistung P in kW")

        # Slider für interaktive Analyse
        ax_slider = plt.axes([0.2, 0.02, 0.6, 0.03])
        self.v_slider = Slider(
            ax=ax_slider,
            label="Analysegeschwindigkeit (km/h)",
            valmin=0,
            valmax=200,
            valinit=50,
            color=COLORS["diff"],
        )
        self.v_slider.on_changed(self.update_analysis)

        # Initiale Darstellung
        self.update_analysis(50)

    def update_analysis(self, v_analyse: float):
        """Aktualisiert die Analyse für eine bestimmte Geschwindigkeit."""
        self.ax1.clear()
        self.ax2.clear()

        # Geschwindigkeitsbereiche
        v_full = np.linspace(0, 200, 1000)
        v_detail = np.linspace(0, 50, 500)

        # Leistungen berechnen
        P_roll_full, P_ges_full = self.calculate_power(v_full)
        P_roll_detail, P_ges_detail = self.calculate_power(v_detail)

        # Gesamtbereich Plot (0-200 km/h)
        self.ax1.plot(
            v_full,
            P_roll_full,
            "-",
            color=COLORS["roll"],
            label="Rollwiderstand",
            linewidth=2,
        )
        self.ax1.plot(
            v_full,
            P_ges_full,
            "-",
            color=COLORS["ges"],
            label="Gesamtwiderstand",
            linewidth=2,
        )
        self.ax1.set_ylim(0, 100)
        self.ax1.set_title("Leistungsbedarf (0-200 km/h)")

        # Detailbereich Plot (0-50 km/h)
        self.ax2.plot(
            v_detail,
            P_roll_detail,
            "-",
            color=COLORS["roll"],
            label="Rollwiderstand",
            linewidth=2,
        )
        self.ax2.plot(
            v_detail,
            P_ges_detail,
            "-",
            color=COLORS["ges"],
            label="Gesamtwiderstand",
            linewidth=2,
        )
        self.ax2.set_ylim(0, 3)
        self.ax2.set_title("Detailansicht Stadtverkehr (0-50 km/h)")

        # Analyse-Markierung
        if v_analyse <= 200:
            P_roll, P_ges = self.calculate_power(np.array([v_analyse]))
            P_diff = P_ges[0] - P_roll[0]
            print(
                f"Differenz zwischen Gesamt- und Rollwiderstand bei {v_analyse:.0f} km/h: "
                f"{P_diff:.2f} kW"
            )

            # Markierung im Hauptplot
            self.ax1.vlines(
                v_analyse,
                P_roll[0],
                P_ges[0],
                color=COLORS["diff"],
                linestyles="--",
                label=f"Luftwiderstand bei {v_analyse:.0f} km/h",
            )

            # Markierung im Detailplot wenn v <= 50
            if v_analyse <= 50:
                self.ax2.vlines(
                    v_analyse,
                    P_roll[0],
                    P_ges[0],
                    color=COLORS["diff"],
                    linestyles="--",
                )

        for ax in [self.ax1, self.ax2]:
            ax.grid(True)
            ax.legend()

        plt.draw()

    def save_analysis(
        self, output_dir: str = "output", filename: str = "fahrwiderstand_analyse"
    ):
        """
        Speichert die aktuelle Analyse in verschiedenen Formaten.

        Args:
            output_dir: Zielverzeichnis für die Ausgabedateien
            filename: Basis-Dateiname ohne Erweiterung
        """
        # Ausgabeverzeichnis erstellen
        os.makedirs(output_dir, exist_ok=True)
        base_path = os.path.join(output_dir, filename)

        try:
            # PNG speichern (Rastergrafik)
            self.fig.savefig(f"{base_path}.png", dpi=300, bbox_inches="tight")
            print(f"PNG gespeichert: {base_path}.png")

            # SVG speichern (Vektorgrafik)
            # SVG unterstützt nur bestimmte Metadaten-Keys
            svg_metadata = {
                "Creator": "Fahrwiderstandsanalyse-Skript",
                "Title": "Fahrwiderstandsanalyse PKW",
                "Description": "Analyse von Roll- und Luftwiderstand",
            }

            self.fig.savefig(
                f"{base_path}.svg", metadata=svg_metadata, bbox_inches="tight"
            )
            print(f"SVG gespeichert: {base_path}.svg")

            # PDF speichern (Vektorgrafik)
            pdf_metadata = {
                "Title": "Fahrwiderstandsanalyse PKW",
                "Author": "Automatisch generiert",
                "Subject": "Roll- und Luftwiderstand",
                "Keywords": "Fahrwiderstand, PKW, Analyse",
                "Creator": "Fahrwiderstandsanalyse-Skript",
            }

            self.fig.savefig(
                f"{base_path}.pdf", metadata=pdf_metadata, bbox_inches="tight"
            )
            print(f"PDF gespeichert: {base_path}.pdf")

        except Exception as e:
            print(f"Fehler beim Speichern: {str(e)}")
            raise

    def show(self):
        """Zeigt die interaktive Analyse."""
        plt.show()


def main():
    """Hauptfunktion zur Durchführung der Analyse."""
    analyse = FahrwiderstandAnalyse()
    analyse.show()
    analyse.save_analysis()


if __name__ == "__main__":
    main()
