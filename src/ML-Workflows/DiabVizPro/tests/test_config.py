"""Tests für die Konfigurationsklasse."""

import pytest
from diabvizpro.config import Config, VariableConfig


def test_config_initialization():
    """Test der Konfigurationsinitialisierung."""
    config = Config()
    assert config.DEFAULT_SAMPLES == 1000
    assert (
        config.PLOT_STYLE == "seaborn-v0_8-whitegrid"
    )  # Geändert von 'seaborn' zu 'default'
