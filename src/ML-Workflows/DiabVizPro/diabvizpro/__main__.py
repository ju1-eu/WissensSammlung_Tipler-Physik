# diabvizpro/__main__.py
"""Haupteinstiegspunkt für DiabVizPro."""

from .config import Config
from .data_generator import DataGenerator
from .plotter import DiabetesPlotter


def main():
    """Hauptfunktion zum Starten der Anwendung."""
    try:
        # Konfiguration erstellen
        config = Config()

        # Datengenerator initialisieren
        generator = DataGenerator(config)

        # Plotter erstellen und anzeigen
        plotter = DiabetesPlotter(config, generator)
        plotter.show()  # Diese Methode müssen wir noch in der DiabetesPlotter-Klasse implementieren

    except Exception as e:
        print(f"❌ Fehler beim Starten der Anwendung: {e}")
        raise


if __name__ == "__main__":
    main()
