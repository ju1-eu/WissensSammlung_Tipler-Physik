import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
from dataclasses import dataclass
import logging
from pathlib import Path
from datetime import datetime

# Logging konfigurieren
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class KraftstoffKonstanten:
    """Konstanten für die Kraftstoffverbrauchsberechnung"""
    MIN_WIRKUNGSGRAD = 0.25  # 25%
    MAX_WIRKUNGSGRAD = 0.35  # 35%
    DEFAULT_WIRKUNGSGRAD = 0.30  # 30%
    REFERENZ_PUNKTE = {
        0.27: 17.5,  # 27% -> 17.5 l/100km
        0.30: 15.8,  # 30% -> 15.8 l/100km
        0.33: 14.4   # 33% -> 14.4 l/100km
    }

@dataclass
class MotorParameter:
    """
    Parameter für die Kraftstoffverbrauchsberechnung
    
    Attributes:
        P_e: Motorleistung [kW]
        H_u: Heizwert [kJ/kg]
        rho_B: Kraftstoffdichte [kg/l]
        v_ref: Referenzgeschwindigkeit [km/h]
    """
    P_e: float = 75.6           # Motorleistung [kW]
    H_u: float = 42000.0        # Heizwert [kJ/kg]
    rho_B: float = 0.76         # Kraftstoffdichte [kg/l]
    v_ref: float = 180.0        # Referenzgeschwindigkeit [km/h]

class KraftstoffVisualisierung:
    """Interaktive Visualisierung des Kraftstoffverbrauchs"""
    
    def __init__(self):
        """Initialisiert die Visualisierung"""
        self.params = MotorParameter()
        self.konstanten = KraftstoffKonstanten()
        self.setup_plot()
        logger.info("Kraftstoffvisualisierung initialisiert")
    
    def berechne_verbrauch(self, eta_e: float) -> float:
        """
        Berechnet den Kraftstoffverbrauch für einen gegebenen Wirkungsgrad
        
        Args:
            eta_e: Effektiver Wirkungsgrad (0 bis 1)
            
        Returns:
            float: Kraftstoffverbrauch in l/100km
            
        Raises:
            ValueError: Wenn der Wirkungsgrad außerhalb des gültigen Bereichs liegt
        """
        if not self.konstanten.MIN_WIRKUNGSGRAD <= eta_e <= self.konstanten.MAX_WIRKUNGSGRAD:
            raise ValueError(f"Wirkungsgrad muss zwischen {self.konstanten.MIN_WIRKUNGSGRAD*100}% "
                           f"und {self.konstanten.MAX_WIRKUNGSGRAD*100}% liegen")
            
        # Berechnung des Massenstroms [kg/s]
        m_dot_B = (self.params.P_e * 1000) / (eta_e * self.params.H_u * 1000)
        
        # Berechnung des Volumenstroms [l/h]
        V_dot_B = m_dot_B / self.params.rho_B * 3600
        
        # Berechnung des streckenbezogenen Verbrauchs [l/100km]
        verbrauch = (V_dot_B / self.params.v_ref) * 100
        
        return round(verbrauch, 1)
    
    def update(self, _):
        """Aktualisiert die Visualisierung bei Änderung des Sliders"""
        try:
            eta_e = self.eta_slider.val / 100
            verbrauch = self.berechne_verbrauch(eta_e)
            
            # Aktualisiere Verbrauchspunkt
            self.verbrauch_point.set_offsets([[self.eta_slider.val, verbrauch]])
            
            # Aktualisiere Textanzeige
            self.verbrauch_text.set_text(
                f'Verbrauch bei η = {self.eta_slider.val:.1f}%:\n{verbrauch:.1f} l/100km'
            )
            
            self.fig.canvas.draw_idle()
        except Exception as e:
            logger.error(f"Fehler bei der Aktualisierung: {e}")
    
    def save_plot(self, _):
        """Speichert den Plot als PNG und SVG"""
        try:
            # Erstelle Ausgabeordner, falls nicht vorhanden
            output_dir = Path("output")
            output_dir.mkdir(exist_ok=True)
            
            # Generiere Zeitstempel für eindeutige Dateinamen
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            base_filename = f"kraftstoffverbrauch_{timestamp}"
            
            # Speichere als PNG
            png_path = output_dir / f"{base_filename}.png"
            self.fig.savefig(png_path, dpi=300, bbox_inches='tight')
            logger.info(f"Plot als PNG gespeichert: {png_path}")
            
            # Speichere als SVG
            svg_path = output_dir / f"{base_filename}.svg"
            self.fig.savefig(svg_path, format='svg', bbox_inches='tight')
            logger.info(f"Plot als SVG gespeichert: {svg_path}")
            
        except Exception as e:
            logger.error(f"Fehler beim Speichern: {e}")
    
    def setup_plot(self):
        """Erstellt den interaktiven Plot"""
        # Figure erstellen
        self.fig = plt.figure(figsize=(12, 8))
        
        # Subplot mit Abstand für Slider und Buttons
        self.ax = self.fig.add_subplot(111)
        plt.subplots_adjust(left=0.1, bottom=0.28, right=0.9, top=0.9)
        
        # Wirkungsgrade für die Kurve
        eta_range = np.linspace(
            self.konstanten.MIN_WIRKUNGSGRAD * 100,
            self.konstanten.MAX_WIRKUNGSGRAD * 100,
            100
        )
        verbrauch_range = [self.berechne_verbrauch(eta/100) for eta in eta_range]
        
        # Hauptkurve
        self.ax.plot(eta_range, verbrauch_range, 'b-', label='Verbrauch bei 180 km/h')
        
        # Referenzpunkte mit Beschriftungen
        for eta, verbrauch in self.konstanten.REFERENZ_PUNKTE.items():
            self.ax.plot(eta * 100, verbrauch, 'ro')
            self.ax.annotate(
                f'{verbrauch:.1f} l/100km',
                xy=(eta * 100, verbrauch),
                xytext=(5, 5),
                textcoords='offset points'
            )
        
        # Aktueller Verbrauchspunkt
        self.verbrauch_point = self.ax.scatter([], [], color='red', s=100, zorder=5)
        
        # Layout und Beschriftungen
        self.ax.set_xlabel('Motorwirkungsgrad η [%]')
        self.ax.set_ylabel('Kraftstoffverbrauch [l/100km]')
        self.ax.set_title('Kraftstoffverbrauch bei 180 km/h\nAbhängigkeit vom Motorwirkungsgrad')
        self.ax.grid(True)
        
        # Achsenbereiche
        self.ax.set_xlim(25, 35)
        self.ax.set_ylim(13, 19)
        
        # Slider erstellen
        slider_ax = plt.axes([0.15, 0.12, 0.65, 0.03])
        self.eta_slider = Slider(
            slider_ax,
            'Wirkungsgrad η [%]',
            valmin=self.konstanten.MIN_WIRKUNGSGRAD * 100,
            valmax=self.konstanten.MAX_WIRKUNGSGRAD * 100,
            valinit=self.konstanten.DEFAULT_WIRKUNGSGRAD * 100,
            valfmt='%.1f%%'
        )
        self.eta_slider.on_changed(self.update)
        
        # Speicher-Button erstellen
        button_ax = plt.axes([0.8, 0.02, 0.1, 0.04])
        self.save_button = Button(button_ax, 'Speichern')
        self.save_button.on_clicked(self.save_plot)
        
        # Textfeld für aktuellen Verbrauch
        self.verbrauch_text = self.ax.text(
            0.02, 0.98,
            '',
            transform=self.ax.transAxes,
            verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.8)
        )
        
        # Zusatzinformationen
        info_text = (
            'Motorleistung: 75.6 kW\n'
            'Ottomotor-Wirkungsgrad: ~30%\n'
            'Dieselmotor-Wirkungsgrad: ~35%'
        )
        self.ax.text(
            0.98, 0.98,
            info_text,
            transform=self.ax.transAxes,
            verticalalignment='top',
            horizontalalignment='right',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.8)
        )
        
        # Initialer Update
        self.update(None)
        logger.info("Plot-Setup abgeschlossen")

def main():
    """Hauptfunktion zum Starten der Visualisierung"""
    try:
        visualisierung = KraftstoffVisualisierung()
        plt.show()
        logger.info("Visualisierung erfolgreich beendet")
    except Exception as e:
        logger.error(f"Fehler beim Erstellen der Visualisierung: {e}")

if __name__ == '__main__':
    main()