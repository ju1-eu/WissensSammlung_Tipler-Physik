"""Konfigurationsklasse für DiabVizPro."""

from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class VariableConfig:
    mean: float
    std: float
    range: Tuple[float, float]
    decimals: int
    classifications: List[Tuple[float, str]]


class Config:
    """Zentrale Konfiguration für den Diabetes-Visualisierer."""

    # Grundeinstellungen
    DEFAULT_SAMPLES: int = 1000
    PLOT_STYLE: str = "seaborn-v0_8-whitegrid"  # Geändert von 'seaborn' zu 'default'
    FIGURE_SIZE: Tuple[int, int] = (10, 12)
    OUTPUT_DIR: str = "output"

    # Plot-Farben
    COLORS = {
        "background": "#f0f0f0",
        "histogram": "skyblue",
        "line": "red",
        "grid": "#cccccc",
    }

    # Variablen-Konfigurationen
    VARIABLES = {
        "Alter": VariableConfig(
            mean=50, std=15, range=(18, 90), decimals=0, classifications=[]
        ),
        "BMI": VariableConfig(
            mean=28,
            std=5,
            range=(16, 45),
            decimals=1,
            classifications=[
                (18.5, "Untergewicht"),
                (25.0, "Normal"),
                (30.0, "Übergewicht"),
                (35.0, "Adipositas"),
            ],
        ),
        "HbA1c": VariableConfig(
            mean=5.7,
            std=0.8,
            range=(4.0, 9.0),
            decimals=1,
            classifications=[(5.7, "Normal"), (6.5, "Diabetes")],
        ),
    }
