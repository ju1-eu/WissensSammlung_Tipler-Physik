"""Tests für die Visualisierungsklasse."""

import pytest
from diabvizpro.config import Config
from diabvizpro.data_generator import DataGenerator
from diabvizpro.plotter import DiabetesPlotter


def test_plotter_initialization():
    """Test der Plotter-Initialisierung."""
    config = Config()
    generator = DataGenerator(config)
    plotter = DiabetesPlotter(config, generator)
