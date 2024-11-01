# DiabVizPro

DiabVizPro ist ein professionelles Tool zur interaktiven Visualisierung und Analyse von Diabetes-relevanten Datenverteilungen.

## Features
- 📊 Interaktive Visualisierung von Verteilungen
- 🔄 Dynamische Anpassung der Parameter
- 📏 Automatische Datenvalidierung
- 💾 Export in verschiedene Formate

## Installation
Siehe [Installationsanleitung](docs/installation.md)

1. Virtuelle Umgebung erstellen und aktivieren
```bash
python3 -m venv venv
source venv/bin/activate
```

2. Abhängigkeiten installieren
```bash
#pip install -r requirements.txt
#pip install -e .

vim requirements.in
numpy
matplotlib
seaborn
pytest
black
flake8
mypy
types-seaborn
scikit-learn

pip install pip-tools
pip-compile requirements.in
pip install -r requirements.txt
pip check
```

3. Entwicklungsworkflow 1
```bash
python -m diabvizpro

# Code formatieren
black diabvizpro/

# Linting
#flake8 diabvizpro/
flake8 --max-line-length=100 diabvizpro/

# Typ-Überprüfung: pip install types-seaborn
mypy diabvizpro/

# Tests ausführen
pytest
```

4. Entwicklungsworkflow 2
```bash
# Code formatieren
black diabetes_data_generator.py
black diabetes_analysis.py 
black ml_workflow.py

# Linting
flake8 --max-line-length=100 diabetes_data_generator.py
flake8 --max-line-length=100 diabetes_analysis.py 
flake8 --max-line-length=100 ml_workflow.py

# Typ-Überprüfung
mypy diabetes_data_generator.py
#mypy diabetes_analysis.py 

# Tests ausführen
pytest
```

## Verwendung
Siehe [Benutzerhandbuch](docs/usage.md)

## API-Dokumentation
Siehe [API-Dokumentation](docs/api.md)

## Lizenz
MIT License
