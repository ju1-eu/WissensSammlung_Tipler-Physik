import pytest
from diabetes_data_generator import generate_diabetes_dataset
import pandas as pd


def test_generate_diabetes_dataset():
    # Erzeuge einen Testdatensatz
    df = generate_diabetes_dataset(n_samples=100)

    # Prüfe, ob die Rückgabe ein Pandas DataFrame ist
    assert isinstance(
        df, pd.DataFrame
    ), "Die Rückgabe sollte ein Pandas DataFrame sein."

    # Prüfe, ob der DataFrame die erwartete Anzahl an Datensätzen enthält
    assert len(df) == 100, "Der DataFrame sollte 100 Datensätze enthalten."

    # Prüfe, ob alle erwarteten Spalten vorhanden sind
    expected_columns = [
        "Alter",
        "Geschlecht",
        "Ethnische_Zugehoerigkeit",
        "BMI",
        "Blutdruck_Systolisch",
        "Blutdruck_Diastolisch",
        "Blutzucker_Nuechtern",
        "HbA1c",
        "Cholesterin_Gesamt",
        "HDL",
        "LDL",
        "Triglyzeride",
        "Taillenumfang",
        "Hueftumfang",
        "Raucher",
        "Alkohol_Konsum",
        "Bewegung_pro_Woche",
        "Familien_Diabetes",
        "Bluthochdruck",
        "Herz_Kreislauf_Erkrankung",
        "Schlafstunden",
        "Stress_Level",
        "Diabetes",
    ]
    for column in expected_columns:
        assert column in df.columns, f"Spalte '{column}' fehlt im DataFrame."

    # Überprüfe, ob keine NaN-Werte vorhanden sind
    assert (
        df.isnull().sum().sum() == 0
    ), "Der DataFrame sollte keine fehlenden Werte enthalten."
