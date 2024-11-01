"""Tests für den Datengenerator."""

import pytest
import numpy as np
from diabvizpro.config import Config
from diabvizpro.data_generator import DataGenerator


def test_data_generation():
    """Test der Datengenerierung."""
    config = Config()
    generator = DataGenerator(config)
    data = generator.generate_variable_data("Alter", 100)
    assert len(data) == 100
