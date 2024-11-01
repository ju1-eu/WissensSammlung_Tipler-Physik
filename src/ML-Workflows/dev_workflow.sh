#!/bin/bash

echo "Starte Entwicklungsworkflow..."

# Code formatieren
echo "1. Code formatieren mit black..."
black diabetes_data_generator.py
black diabetes_analysis.py 
black ml_workflow.py

# Linting
echo "2. Linting mit flake8..."
flake8 --max-line-length=100 diabetes_data_generator.py
flake8 --max-line-length=100 diabetes_analysis.py 
flake8 --max-line-length=100 ml_workflow.py

# Typ-Überprüfung
echo "3. Typ-Überprüfung mit mypy..."
mypy diabetes_data_generator.py
#mypy diabetes_analysis.py 

# Tests ausführen
echo "4. Tests ausführen mit pytest..."
pytest

echo "Entwicklungsworkflow abgeschlossen!"

