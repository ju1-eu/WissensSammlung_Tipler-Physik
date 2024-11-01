#!/bin/bash

# create_project.sh
echo "🚀 Erstelle DiabVizPro Projektstruktur..."

# Hauptverzeichnisse erstellen
mkdir -p DiabVizPro/{docs,tests,diabvizpro/utils,examples,output}

# Leere __init__.py Dateien erstellen
touch DiabVizPro/tests/__init__.py
touch DiabVizPro/diabvizpro/__init__.py
touch DiabVizPro/diabvizpro/utils/__init__.py

# Hauptpaket-Dateien erstellen
cat > DiabVizPro/diabvizpro/config.py << 'EOL'
"""Konfigurationsklasse für DiabVizPro."""
from dataclasses import dataclass
from typing import Dict, List, Tuple, Optional

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
    PLOT_STYLE: str = 'seaborn'
    FIGURE_SIZE: Tuple[int, int] = (10, 12)
    OUTPUT_DIR: str = 'output'
    
    # Variablen-Konfigurationen
    VARIABLES = {
        'Alter': VariableConfig(
            mean=50, std=15, range=(18, 90), decimals=0,
            classifications=[]
        ),
        'BMI': VariableConfig(
            mean=28, std=5, range=(16, 45), decimals=1,
            classifications=[
                (18.5, 'Untergewicht'),
                (25.0, 'Normal'),
                (30.0, 'Übergewicht'),
                (35.0, 'Adipositas')
            ]
        ),
        'HbA1c': VariableConfig(
            mean=5.7, std=0.8, range=(4.0, 9.0), decimals=1,
            classifications=[
                (5.7, 'Normal'),
                (6.5, 'Diabetes')
            ]
        )
    }
EOL

cat > DiabVizPro/diabvizpro/data_generator.py << 'EOL'
"""Modul für die Generierung von Diabetes-Daten."""
import numpy as np
from typing import Dict, Optional
from .config import Config

class DataGenerator:
    """Klasse für die Generierung der Diabetes-Daten."""
    
    def __init__(self, config: Config):
        self.config = config
    
    def generate_variable_data(self, 
                             var_name: str, 
                             n_samples: int, 
                             std_override: Optional[float] = None) -> np.ndarray:
        """Generiert Daten für eine einzelne Variable."""
        var_config = self.config.VARIABLES[var_name]
        std = std_override if std_override is not None else var_config.std
        
        samples = np.random.normal(var_config.mean, std, int(n_samples))
        values = np.clip(samples, *var_config.range)
        
        return np.round(values, var_config.decimals)
EOL

cat > DiabVizPro/diabvizpro/plotter.py << 'EOL'
"""Modul für die Visualisierung von Diabetes-Daten."""
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
from pathlib import Path
from datetime import datetime
from .config import Config
from .data_generator import DataGenerator

class DiabetesPlotter:
    """Klasse für die Visualisierung der Diabetes-Daten."""
    
    def __init__(self, config: Config, data_generator: DataGenerator):
        self.config = config
        self.data_generator = data_generator
        self._setup_plot()
EOL

cat > DiabVizPro/diabvizpro/utils/validators.py << 'EOL'
"""Validierungsfunktionen für DiabVizPro."""
import numpy as np
from typing import Dict, Any

def validate_data_ranges(data: Dict[str, np.ndarray], 
                        ranges: Dict[str, Dict[str, Any]]) -> Dict[str, Dict[str, bool]]:
    """Validiert die generierten Daten auf Plausibilität."""
    validation_results = {}
    
    for var_name, values in data.items():
        range_config = ranges.get(var_name, {})
        validation_results[var_name] = {
            'in_range': True,  # Implementierung folgt
            'mean_ok': True,   # Implementierung folgt
            'std_ok': True     # Implementierung folgt
        }
    
    return validation_results
EOL

cat > DiabVizPro/diabvizpro/utils/helpers.py << 'EOL'
"""Hilfsfunktionen für DiabVizPro."""
from typing import Dict, Any
from pathlib import Path
import json

def save_configuration(config: Dict[str, Any], filepath: Path) -> None:
    """Speichert die Konfiguration in einer JSON-Datei."""
    with open(filepath, 'w') as f:
        json.dump(config, f, indent=4)

def load_configuration(filepath: Path) -> Dict[str, Any]:
    """Lädt die Konfiguration aus einer JSON-Datei."""
    with open(filepath) as f:
        return json.load(f)
EOL

# Test-Dateien erstellen
cat > DiabVizPro/tests/test_config.py << 'EOL'
"""Tests für die Konfigurationsklasse."""
import pytest
from diabvizpro.config import Config, VariableConfig

def test_config_initialization():
    """Test der Konfigurationsinitialisierung."""
    config = Config()
    assert config.DEFAULT_SAMPLES == 1000
    assert config.PLOT_STYLE == 'seaborn'
EOL

cat > DiabVizPro/tests/test_data_generator.py << 'EOL'
"""Tests für den Datengenerator."""
import pytest
import numpy as np
from diabvizpro.config import Config
from diabvizpro.data_generator import DataGenerator

def test_data_generation():
    """Test der Datengenerierung."""
    config = Config()
    generator = DataGenerator(config)
    data = generator.generate_variable_data('Alter', 100)
    assert len(data) == 100
EOL

cat > DiabVizPro/tests/test_plotter.py << 'EOL'
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
EOL

# Beispiel-Dateien erstellen
cat > DiabVizPro/examples/basic_usage.py << 'EOL'
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
EOL

cat > DiabVizPro/examples/advanced_usage.py << 'EOL'
"""Fortgeschrittene Verwendung von DiabVizPro."""
from diabvizpro.config import Config
from diabvizpro.data_generator import DataGenerator
from diabvizpro.plotter import DiabetesPlotter
from diabvizpro.utils.helpers import save_configuration, load_configuration
from pathlib import Path

def main():
    # Erweiterte Beispiele folgen
    pass

if __name__ == "__main__":
    main()
EOL

# Dokumentation erstellen
cat > DiabVizPro/docs/installation.md << 'EOL'
# Installation von DiabVizPro

## Voraussetzungen
- Python 3.8 oder höher
- pip (Python Package Installer)

## Installation
1. Repository klonen
```bash
git clone https://github.com/username/diabvizpro.git
cd diabvizpro
```

2. Virtuelle Umgebung erstellen und aktivieren
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Abhängigkeiten installieren
```bash
pip install -r requirements.txt
```

4. Paket installieren
```bash
pip install -e .
```
EOL

cat > DiabVizPro/docs/usage.md << 'EOL'
# DiabVizPro Benutzerhandbuch

## Grundlegende Verwendung
```python
from diabvizpro import DiabetesVisualizer
viz = DiabetesVisualizer()
viz.show()
```

## Funktionen
- Interaktive Visualisierung von Verteilungen
- Dynamische Anpassung der Parameter
- Automatische Datenvalidierung
- Export in verschiedene Formate
EOL

cat > DiabVizPro/docs/api.md << 'EOL'
# DiabVizPro API-Dokumentation

## Hauptklassen

### Config
Zentrale Konfigurationsklasse für alle Parameter und Einstellungen.

### DataGenerator
Klasse zur Generierung von Testdaten mit konfigurierbaren Verteilungen.

### DiabetesPlotter
Visualisierungsklasse für die interaktive Darstellung der Daten.
EOL

# Konfigurationsdateien erstellen
cat > DiabVizPro/requirements.txt << 'EOL'
numpy
matplotlib
pytest
black
flake8
mypy
EOL

cat > DiabVizPro/setup.py << 'EOL'
from setuptools import setup, find_packages

setup(
    name="diabvizpro",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        'numpy',
        'matplotlib',
    ],
    author="Ihr Name",
    author_email="ihre.email@domain.com",
    description="DiabVizPro - Diabetes Data Visualization Tool",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
EOL

cat > DiabVizPro/.gitignore << 'EOL'
# Python
__pycache__/
*.py[cod]
*$py.class
*.so

# Virtuelle Umgebungen
.env
.venv
env/
venv/
ENV/

# Distribution / Packaging
dist/
build/
*.egg-info/

# Test Cache
.coverage
.pytest_cache/
.mypy_cache/

# Output Dateien
output/*.png
output/*.svg
output/*.pdf

# MacOS
.DS_Store
EOL

cat > DiabVizPro/README.md << 'EOL'
# DiabVizPro

DiabVizPro ist ein professionelles Tool zur interaktiven Visualisierung und Analyse von Diabetes-relevanten Datenverteilungen.

## Features
- 📊 Interaktive Visualisierung von Verteilungen
- 🔄 Dynamische Anpassung der Parameter
- 📏 Automatische Datenvalidierung
- 💾 Export in verschiedene Formate

## Installation
Siehe [Installationsanleitung](docs/installation.md)

## Verwendung
Siehe [Benutzerhandbuch](docs/usage.md)

## API-Dokumentation
Siehe [API-Dokumentation](docs/api.md)

## Lizenz
MIT License
EOL

# Output-Verzeichnis mit .gitkeep
touch DiabVizPro/output/.gitkeep

echo "✅ Projektstruktur wurde erstellt!"
echo "📂 Wechseln Sie in das Projektverzeichnis:"
echo "cd DiabVizPro"
