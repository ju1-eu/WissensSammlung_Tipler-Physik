"""Grundlegende Verwendung von DiabVizPro."""

from diabvizpro.config import Config
from diabvizpro.data_generator import DataGenerator
from diabvizpro.plotter import DiabetesPlotter


def main():
    # Konfiguration erstellen
    config = Config()

    # Datengenerator initialisieren
    generator = DataGenerator(config)

    # Plotter erstellen und anzeigen
    plotter = DiabetesPlotter(config, generator)
    plotter.show()


if __name__ == "__main__":
    main()
