import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
from matplotlib.gridspec import GridSpec
import os

class SturzSimulation:
    def __init__(self):
        self.g = 9.81
        self.setup_plot()
        self.update(None)
        
        os.makedirs('output', exist_ok=True)
        self.save_plots()
        
        plt.show()

    def setup_plot(self):
        """Initialisiert das Layout mit korrigierter Legende-Position."""
        plt.style.use('seaborn-v0_8-whitegrid')
        self.fig = plt.figure(figsize=(12, 10))
        
        # Verwende GridSpec für bessere Kontrolle über das Layout
        gs = GridSpec(4, 1, height_ratios=[3, 3, 0.5, 0.5], hspace=0.4)
        
        # Positions-Plot
        self.ax1 = self.fig.add_subplot(gs[0])
        self.position_line, = self.ax1.plot([], [], 'b-', label='Position', linewidth=2)
        self.ax1.set_xlabel('Zeit (s)')
        self.ax1.set_ylabel('Position (m)')
        self.ax1.grid(True)
        # Legende in die obere rechte Ecke mit Padding
        self.ax1.legend(loc='upper right', bbox_to_anchor=(0.98, 0.98))
        
        # Geschwindigkeits-Plot
        self.ax2 = self.fig.add_subplot(gs[1])
        self.velocity_line, = self.ax2.plot([], [], 'g-', label='Geschwindigkeit', linewidth=2)
        self.ax2.set_xlabel('Zeit (s)')
        self.ax2.set_ylabel('Geschwindigkeit (m/s)')
        self.ax2.grid(True)
        # Legende in die obere rechte Ecke mit Padding
        self.ax2.legend(loc='upper right', bbox_to_anchor=(0.98, 0.98))
        
        # Slider für Höhe
        slider_ax_h = plt.axes([0.15, 0.2, 0.7, 0.03])
        self.slider_h = Slider(
            slider_ax_h, 'Fallhöhe (m)',
            10, 300, valinit=150,
            color='royalblue'
        )
        
        # Slider für Eindringtiefe
        slider_ax_dy = plt.axes([0.15, 0.1, 0.7, 0.03])
        self.slider_dy = Slider(
            slider_ax_dy, 'Eindringtiefe (m)',
            0.2, 3, valinit=1.2,
            color='forestgreen'
        )
        
        self.slider_h.on_changed(self.update)
        self.slider_dy.on_changed(self.update)
        
        # Textbox für Ergebnisse - Position angepasst
        self.text_box = self.fig.text(0.15, 0.02, '', transform=self.fig.transFigure,
                                    bbox=dict(facecolor='white', alpha=0.8))
        
        # Angepasste Ränder
        plt.subplots_adjust(left=0.1, right=0.95, bottom=0.25, top=0.95)

    def update(self, _):
        """Aktualisiert die Plots bei Slider-Änderungen."""
        h = self.slider_h.val
        dy = self.slider_dy.val
        
        t, y, v, ergebnisse = self.generiere_zeitdaten(h, dy)
        
        # Aktualisiere Position-Plot mit festen Grenzen
        self.position_line.set_data(t, y)
        self.ax1.set_xlim(0, max(t) * 1.05)
        self.ax1.set_ylim(-dy * 1.2, h * 1.05)
        
        # Aktualisiere Geschwindigkeit-Plot mit festen Grenzen
        self.velocity_line.set_data(t, v)
        self.ax2.set_xlim(0, max(t) * 1.05)
        self.ax2.set_ylim(-5, max(v) * 1.05)
        
        # Aktualisiere Ergebnistext
        self.text_box.set_text(
            f"Auftreffgeschwindigkeit: {ergebnisse['v1']:.2f} m/s\n"
            f"Bremsbeschleunigung: {ergebnisse['a_h']:.0f} m/s²\n"
            f"Fallzeit: {ergebnisse['t_fall']:.2f} s\n"
            f"Bremszeit: {ergebnisse['t_brems']:.3f} s\n"
            f"G-Belastung: {ergebnisse['g_vielfaches']:.0f}-fach"
        )
        
        self.fig.canvas.draw_idle()

    # Die anderen Methoden bleiben unverändert
    def berechne_bewegung(self, h, dy):
        """Berechnet die Bewegungsgrößen für beide Phasen."""
        v1 = np.sqrt(2 * self.g * h)
        t_fall = np.sqrt(2 * h / self.g)
        a_h = -(v1 * v1) / (2 * dy)
        t_brems = -v1 / a_h
        
        return {
            'v1': v1,
            'a_h': a_h,
            't_fall': t_fall,
            't_brems': t_brems,
            'g_vielfaches': abs(a_h / self.g)
        }

    def generiere_zeitdaten(self, h, dy):
        """Generiert Zeitreihen für Position und Geschwindigkeit."""
        ergebnisse = self.berechne_bewegung(h, dy)
        
        t1 = np.linspace(0, ergebnisse['t_fall'], 100)
        y1 = h - 0.5 * self.g * t1 * t1
        v1 = self.g * t1
        
        t2 = np.linspace(ergebnisse['t_fall'], 
                        ergebnisse['t_fall'] + ergebnisse['t_brems'], 
                        25)
        dt = t2 - ergebnisse['t_fall']
        y2 = -(ergebnisse['a_h'] * dt * dt) / 2 + ergebnisse['v1'] * dt
        v2 = ergebnisse['v1'] + ergebnisse['a_h'] * dt
        
        return np.concatenate([t1, t2]), np.concatenate([y1, y2]), np.concatenate([v1, v2]), ergebnisse

    def save_plots(self):
        """Speichert die Plots als PNG und SVG."""
        self.fig.savefig('output/sturz_simulation.png', dpi=300, bbox_inches='tight')
        self.fig.savefig('output/sturz_simulation.svg', bbox_inches='tight')

if __name__ == "__main__":
    simulation = SturzSimulation()