import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
from matplotlib.widgets import Slider, RadioButtons
import os
from datetime import datetime

class VektorVisualisierung:
    def __init__(self):
        """Initialisierung der Visualisierung"""
        plt.style.use('default')  # Sauberer Stil
        self.setup_plot()
        self.setup_sliders()
        self.setup_radio()
        self.setup_save_directory()
        
    def setup_plot(self):
        """Erstellt das Hauptfenster und die Plots"""
        self.fig = plt.figure(figsize=(12, 8))
        self.gs = self.fig.add_gridspec(2, 1, height_ratios=[3, 1], hspace=0.3)
        
        # Hauptplot für Vektoren
        self.ax_main = self.fig.add_subplot(self.gs[0])
        self.ax_main.set_aspect('equal', adjustable='box')
        
        # Slider-Bereich
        self.ax_slider = self.fig.add_subplot(self.gs[1])
        self.ax_slider.set_visible(False)
        
        # Initiale Plot-Einstellungen
        self.ax_main.grid(True, linestyle='--', alpha=0.7)
        self.ax_main.set_title('Vektorberechnungen', pad=20)
        
        # Speicher-Button hinzufügen
        self.button_ax = plt.axes([0.8, 0.85, 0.1, 0.075])
        self.button = plt.Button(self.button_ax, 'Speichern')
        self.button.on_clicked(lambda x: self.auto_save())
        
    def setup_sliders(self):
        """Erstellt die Slider für die Parameter"""
        # Positionen für Slider
        slider_width = 0.3
        slider_height = 0.03
        x_left = 0.1
        x_right = 0.55
        
        # Bär-Verschiebung Slider
        self.ax_r1_betrag = plt.axes([x_left, 0.2, slider_width, slider_height])
        self.ax_r1_winkel = plt.axes([x_left, 0.15, slider_width, slider_height])
        self.ax_r2_betrag = plt.axes([x_left, 0.1, slider_width, slider_height])
        self.ax_r2_winkel = plt.axes([x_left, 0.05, slider_width, slider_height])
        
        # Schiffsposition Slider
        self.ax_abstand = plt.axes([x_right, 0.2, slider_width, slider_height])
        self.ax_winkel = plt.axes([x_right, 0.15, slider_width, slider_height])
        
        # Slider-Objekte mit angepassten Wertebereichen
        self.slider_r1_betrag = Slider(self.ax_r1_betrag, 'R1 Betrag', 0, 20, valinit=12)
        self.slider_r1_winkel = Slider(self.ax_r1_winkel, 'R1 Winkel', 0, 360, valinit=43.5)
        self.slider_r2_betrag = Slider(self.ax_r2_betrag, 'R2 Betrag', 0, 20, valinit=11.92)
        self.slider_r2_winkel = Slider(self.ax_r2_winkel, 'R2 Winkel', 0, 360, valinit=89)
        
        self.slider_abstand = Slider(self.ax_abstand, 'Abstand', 0, 200, valinit=170.8)
        self.slider_winkel = Slider(self.ax_winkel, 'Winkel A', 0, 90, valinit=20.5)
        
        # Event-Handler
        for slider in [self.slider_r1_betrag, self.slider_r1_winkel,
                      self.slider_r2_betrag, self.slider_r2_winkel,
                      self.slider_abstand, self.slider_winkel]:
            slider.on_changed(self.update)
            
    def draw_vector(self, start, end, color='blue', label=None):
        """Zeichnet einen Vektor"""
        arrow = FancyArrowPatch(
            start, end,
            arrowstyle='-|>',
            color=color,
            mutation_scale=15,
            linewidth=2,
            label=label
        )
        self.ax_main.add_patch(arrow)
        
    def update_baer(self):
        """Aktualisiert die Bär-Verschiebung"""
        self.ax_main.clear()
        self.setup_grid()
        
        # Parameter holen
        r1_betrag = self.slider_r1_betrag.val
        r1_winkel = np.radians(self.slider_r1_winkel.val)
        r2_betrag = self.slider_r2_betrag.val
        r2_winkel = np.radians(self.slider_r2_winkel.val)
        
        # Vektoren berechnen
        r1_x = r1_betrag * np.cos(r1_winkel)
        r1_y = r1_betrag * np.sin(r1_winkel)
        r2_x = r2_betrag * np.cos(r2_winkel)
        r2_y = r2_betrag * np.sin(r2_winkel)
        
        # Vektoren zeichnen mit korrekter Skalierung
        scale = 1.0  # Skalierungsfaktor
        self.draw_vector((0, 0), (r1_x * scale, r1_y * scale), 'blue', 'R1')
        self.draw_vector((r1_x * scale, r1_y * scale),
                        ((r1_x + r2_x) * scale, (r1_y + r2_y) * scale), 'red', 'R2')
        self.draw_vector((0, 0), ((r1_x + r2_x) * scale, (r1_y + r2_y) * scale),
                        'green', 'Rges')
        
        # Plot-Grenzen dynamisch anpassen
        max_val = max(abs(r1_x + r2_x), abs(r1_y + r2_y)) * scale
        margin = max_val * 0.2  # 20% Rand
        self.ax_main.set_xlim(-margin, max_val + margin)
        self.ax_main.set_ylim(-margin, max_val + margin)
        
        # Ergebnis berechnen
        r_ges = np.sqrt((r1_x + r2_x)**2 + (r1_y + r2_y)**2)
        winkel_ges = np.degrees(np.arctan2(r1_y + r2_y, r1_x + r2_x))
        if winkel_ges < 0:
            winkel_ges += 360
            
        self.ax_main.set_title(
            f'Gesamtverschiebung: {r_ges:.2f}m, Winkel: {winkel_ges:.1f}°'
        )
        self.ax_main.legend()
        self.ax_main.grid(True)
        
    def update_schiff(self):
        """Aktualisiert die Schiffsposition"""
        self.ax_main.clear()
        self.setup_grid()
        
        abstand = self.slider_abstand.val
        winkel = np.radians(self.slider_winkel.val)
        
        # Berechnung der Schiffsposition
        x_schiff = abstand / np.tan(winkel)
        
        # Plot-Grenzen anpassen
        max_x = max(x_schiff * 1.2, 1000)
        max_y = max(abstand * 1.2, 200)
        
        self.ax_main.set_xlim(-100, max_x)
        self.ax_main.set_ylim(-max_y, max_y/5)
        
        # Sender zeichnen
        self.ax_main.plot(0, 0, 'ro', label='Sender B', markersize=10)
        self.ax_main.plot(0, -abstand, 'bo', label='Sender A', markersize=10)
        self.ax_main.plot(x_schiff, 0, 'go', label='Schiff', markersize=10)
        
        # Verbindungslinien
        self.ax_main.plot([0, x_schiff], [0, 0], 'g--', alpha=0.5)
        self.ax_main.plot([0, x_schiff], [-abstand, 0], 'b--', alpha=0.5)
        
        # Beschriftungen
        entfernung = np.sqrt(x_schiff**2)
        self.ax_main.set_title(f'Entfernung zu Sender B: {entfernung:.2f}km')
        self.ax_main.legend()
        
    def setup_grid(self):
        """Richtet das Koordinatensystem ein"""
        self.ax_main.grid(True, linestyle='--', alpha=0.7)
        self.ax_main.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
        self.ax_main.axvline(x=0, color='k', linestyle='-', linewidth=0.5)
        
    def update(self, val):
        """Aktualisiert die Visualisierung"""
        if self.radio.value_selected == 'Bär-Verschiebung':
            self.update_baer()
        else:
            self.update_schiff()
    
    # Automatisches Speichern
    def auto_save(self):
        """Speichert die Plots mit einfachen Dateinamen"""
        try:
            # Erstelle output-Verzeichnis falls nicht vorhanden
            if not os.path.exists(self.output_dir):
                os.makedirs(self.output_dir)
            
            # Einfache Dateinamen
            mode = 'baer_verschiebung' if self.radio.value_selected == 'Bär-Verschiebung' else 'schiffsposition'
            base_filename = f'vektor_{mode}'
            png_path = os.path.join(self.output_dir, f'{base_filename}.png')
            svg_path = os.path.join(self.output_dir, f'{base_filename}.svg')
            
            # Speichern mit hoher Qualität
            self.fig.savefig(png_path, dpi=300, bbox_inches='tight')
            self.fig.savefig(svg_path, format='svg', bbox_inches='tight')
            
            print(f"\nPlots gespeichert als:")
            print(f"PNG: {os.path.basename(png_path)}")
            print(f"SVG: {os.path.basename(svg_path)}")
            
            # Plot aktiv halten
            plt.draw()
            
        except Exception as e:
            print(f"Fehler beim Speichern: {str(e)}")
            
    def setup_radio(self):
        """Erstellt die Radio-Buttons"""
        self.ax_radio = plt.axes([0.02, 0.85, 0.15, 0.1])
        self.radio = RadioButtons(self.ax_radio, ('Bär-Verschiebung', 'Schiffsposition'))
        self.radio.on_clicked(self.update)
        
    def setup_save_directory(self):
        """Erstellt das Ausgabeverzeichnis"""
        self.output_dir = 'output'
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
            
    def save_plot(self):
        """Speichert den aktuellen Plot"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        mode = self.radio.value_selected.lower().replace('-', '_')
        
        # PNG speichern
        png_path = os.path.join(self.output_dir, f'vektor_{mode}_{timestamp}.png')
        self.fig.savefig(png_path, dpi=300, bbox_inches='tight')
        
        # SVG speichern
        svg_path = os.path.join(self.output_dir, f'vektor_{mode}_{timestamp}.svg')
        self.fig.savefig(svg_path, format='svg', bbox_inches='tight')
        
        print(f"Plots gespeichert als {png_path} und {svg_path}")
        
    def show(self):
        """Zeigt die Visualisierung an"""
        self.update(None)
        plt.show()

if __name__ == "__main__":
    viz = VektorVisualisierung()
    viz.show()