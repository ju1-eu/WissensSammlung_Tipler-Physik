"""Modul für die Visualisierung von Diabetes-Daten."""

import seaborn as sns
import matplotlib.pyplot as plt

# print(plt.style.available) # debug
from matplotlib.widgets import Slider, Button
from pathlib import Path
from datetime import datetime
import numpy as np
from typing import Optional

sns.set()


class DiabetesPlotter:
    """Klasse für die Visualisierung der Diabetes-Daten."""

    def __init__(self, config, data_generator):
        """Initialisiert den DiabetesPlotter."""
        self.config = config
        self.data_generator = data_generator
        self.n_samples = config.DEFAULT_SAMPLES
        self._setup_plot()
        self._setup_controls()
        self.update(None)  # Initiales Update

    def _setup_plot(self):
        """Initialisiert die Plot-Umgebung."""
        plt.style.use(self.config.PLOT_STYLE)
        self.fig, self.axes = plt.subplots(3, 1, figsize=self.config.FIGURE_SIZE)
        # Mehr Platz für die Slider am unteren Rand
        plt.subplots_adjust(left=0.1, bottom=0.3, right=0.9, top=0.95, hspace=0.4)

        # Konfiguriere Achsen
        for ax, (var_name, var_config) in zip(self.axes, self.config.VARIABLES.items()):
            ax.set_title(f"{var_name}-Verteilung")
            ax.set_xlabel(var_name)
            ax.set_ylabel("Häufigkeit")

            # Füge Klassifikationslinien hinzu
            for value, label in var_config.classifications:
                ax.axvline(x=value, color="r", linestyle="--", alpha=0.3)
                ax.text(
                    value,
                    ax.get_ylim()[1] * 0.95,
                    label,
                    rotation=90,
                    va="top",
                    ha="right",
                )

    def _setup_controls(self):
        """Initialisiert die Steuerelemente."""
        # Konstanten für das Layout
        slider_height = 0.02
        spacing = 0.035  # Erhöhter Abstand zwischen den Slidern
        bottom_margin = 0.05  # Abstand vom unteren Rand
        slider_width = 0.65
        slider_left = 0.1

        # Slider für Stichprobengröße (oberster Slider)
        slider_bottom = bottom_margin
        ax_samples = plt.axes([slider_left, slider_bottom, slider_width, slider_height])
        self.slider_n = Slider(
            ax_samples,
            "Stichprobengröße",
            100,
            5000,
            valinit=self.n_samples,
            valstep=100,
        )
        self.slider_n.on_changed(self.update)

        # Slider für Standardabweichungen
        self.std_sliders = {}
        for i, (var_name, var_config) in enumerate(self.config.VARIABLES.items()):
            slider_bottom = bottom_margin + (i + 1) * spacing
            ax = plt.axes([slider_left, slider_bottom, slider_width, slider_height])
            self.std_sliders[var_name] = Slider(
                ax, f"{var_name} σ", 0.1, var_config.std * 2, valinit=var_config.std
            )
            self.std_sliders[var_name].on_changed(self.update)

        # Reset-Button (rechts neben dem untersten Slider)
        button_width = 0.1
        button_height = slider_height
        button_left = slider_left + slider_width + 0.05
        button_bottom = bottom_margin
        ax_reset = plt.axes([button_left, button_bottom, button_width, button_height])
        self.reset_button = Button(ax_reset, "Reset")
        self.reset_button.on_clicked(self.reset_parameters)

    def update(self, _):
        """Aktualisiert die Plots."""
        # Generiere neue Daten
        data = {}
        for var_name, var_config in self.config.VARIABLES.items():
            data[var_name] = self.data_generator.generate_variable_data(
                var_name, int(self.slider_n.val), self.std_sliders[var_name].val
            )

        # Aktualisiere Plots
        for ax, (var_name, values) in zip(self.axes, data.items()):
            ax.clear()
            var_config = self.config.VARIABLES[var_name]

            # Histogram
            counts, bins, _ = ax.hist(
                values,
                bins=30,
                density=True,
                alpha=0.7,
                color="skyblue",
                edgecolor="black",
            )

            # Theoretische Verteilung
            x = np.linspace(*var_config.range, 100)
            y = np.exp(
                -((x - var_config.mean) ** 2)
                / (2 * self.std_sliders[var_name].val ** 2)
            )
            y = y / (self.std_sliders[var_name].val * np.sqrt(2 * np.pi))
            ax.plot(x, y, "r--", lw=2, alpha=0.7, label="Theoretische Verteilung")

            # Labels und Titel
            ax.set_title(f"{var_name}-Verteilung")
            ax.set_xlabel(var_name)
            ax.set_ylabel("Häufigkeit")

            # Klassifikationslinien
            max_height = max(counts) if len(counts) > 0 else 1
            for value, label in var_config.classifications:
                ax.axvline(x=value, color="r", linestyle="--", alpha=0.3)
                ax.text(
                    value, max_height * 0.95, label, rotation=90, va="top", ha="right"
                )

            ax.legend()
            ax.grid(True, alpha=0.3)

        self.fig.canvas.draw_idle()

    def reset_parameters(self, _):
        """Setzt alle Parameter auf ihre Standardwerte zurück."""
        self.slider_n.set_val(self.config.DEFAULT_SAMPLES)
        for var_name, slider in self.std_sliders.items():
            slider.set_val(self.config.VARIABLES[var_name].std)

    def show(self):
        """Zeigt die interaktive Visualisierung an."""
        plt.show()

    def save(self, filename: Optional[str] = None):
        """Speichert die aktuelle Visualisierung."""
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"diabetes_dist_{timestamp}"

        output_dir = Path(self.config.OUTPUT_DIR)
        output_dir.mkdir(exist_ok=True)

        # Speichere in verschiedenen Formaten
        for fmt in ["png", "svg", "pdf"]:
            self.fig.savefig(
                output_dir / f"{filename}.{fmt}", bbox_inches="tight", dpi=300
            )
            print(f"Plot gespeichert als: {output_dir / f'{filename}.{fmt}'}")
