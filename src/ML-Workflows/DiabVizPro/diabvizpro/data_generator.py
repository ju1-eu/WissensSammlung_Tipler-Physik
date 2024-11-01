"""Modul für die Generierung von Diabetes-Daten."""

import numpy as np
from typing import Optional
from .config import Config


class DataGenerator:
    """Klasse für die Generierung der Diabetes-Daten."""

    def __init__(self, config: Config):
        self.config = config

    def generate_variable_data(
        self, var_name: str, n_samples: int, std_override: Optional[float] = None
    ) -> np.ndarray:
        """Generiert Daten für eine einzelne Variable."""
        var_config = self.config.VARIABLES[var_name]
        std = std_override if std_override is not None else var_config.std

        samples = np.random.normal(var_config.mean, std, int(n_samples))
        values = np.clip(samples, *var_config.range)

        return np.round(values, var_config.decimals)
