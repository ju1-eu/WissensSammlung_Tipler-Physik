import numpy as np
import pandas as pd


def generate_diabetes_dataset(n_samples=1000):
    np.random.seed(42)

    # Demografische Daten
    alter = np.random.normal(50, 15, n_samples).clip(18, 90)
    geschlecht = np.random.choice(["M", "W"], n_samples)
    ethnische_zugehoerigkeit = np.random.choice(
        ["Europäisch", "Afrikanisch", "Asiatisch", "Hispanisch"],
        n_samples,
        p=[0.7, 0.1, 0.1, 0.1],
    )

    # Klinische Messungen
    bmi = np.random.normal(28, 5, n_samples).clip(16, 45)
    blutdruck_systolisch = np.random.normal(130, 15, n_samples).clip(90, 180)
    blutdruck_diastolisch = np.random.normal(80, 10, n_samples).clip(60, 110)

    # Blutwerte
    blutzucker_nuechtern = np.random.normal(100, 20, n_samples).clip(70, 180)
    hba1c = np.random.normal(5.7, 0.8, n_samples).clip(4.0, 9.0)
    cholesterin_gesamt = np.random.normal(200, 35, n_samples).clip(120, 300)
    hdl = np.random.normal(50, 15, n_samples).clip(20, 90)
    ldl = np.random.normal(130, 30, n_samples).clip(50, 220)
    triglyzeride = np.random.normal(150, 50, n_samples).clip(50, 400)

    # Körpermaße
    taillenumfang = np.random.normal(95, 15, n_samples).clip(60, 150)
    hueftumfang = np.random.normal(105, 15, n_samples).clip(70, 160)

    # Lebensstilfaktoren
    raucher = np.random.choice([0, 1], n_samples, p=[0.8, 0.2])
    alkohol_pro_woche = np.random.choice(
        ["Kein", "Gelegentlich", "Regelmäßig", "Häufig"],
        n_samples,
        p=[0.3, 0.4, 0.2, 0.1],
    )
    bewegung_pro_woche = np.random.choice(
        ["Keine", "1-2 Mal", "3-4 Mal", "5+ Mal"], n_samples, p=[0.2, 0.3, 0.3, 0.2]
    )

    # Medizinische Vorgeschichte
    familien_diabetes = np.random.choice([0, 1], n_samples, p=[0.7, 0.3])
    bluthochdruck = np.random.choice([0, 1], n_samples, p=[0.75, 0.25])
    herz_kreislauf = np.random.choice([0, 1], n_samples, p=[0.85, 0.15])

    # Zusätzliche Faktoren
    schlafstunden = np.random.normal(7, 1, n_samples).clip(4, 10)
    stress_level = np.random.choice(["Niedrig", "Mittel", "Hoch"], n_samples)

    # Diabetes-Diagnose basierend auf Risikofaktoren
    # Komplexe Berechnung des Diabetes-Risikos
    risiko_score = (
        (bmi > 30) * 2
        + (blutdruck_systolisch > 140) * 1.5
        + (blutzucker_nuechtern > 100) * 2
        + (hba1c > 5.7) * 2.5
        + (familien_diabetes) * 1.5
        + (alter > 45) * 1
        + (bewegung_pro_woche == "Keine") * 1
        + (raucher) * 1
    )

    diabetes = (risiko_score > 5) | (np.random.random(n_samples) < 0.1)

    # Erstellen des DataFrames
    data = pd.DataFrame(
        {
            "Alter": alter.astype(int),
            "Geschlecht": geschlecht,
            "Ethnische_Zugehoerigkeit": ethnische_zugehoerigkeit,
            "BMI": bmi.round(1),
            "Blutdruck_Systolisch": blutdruck_systolisch.astype(int),
            "Blutdruck_Diastolisch": blutdruck_diastolisch.astype(int),
            "Blutzucker_Nuechtern": blutzucker_nuechtern.astype(int),
            "HbA1c": hba1c.round(1),
            "Cholesterin_Gesamt": cholesterin_gesamt.astype(int),
            "HDL": hdl.astype(int),
            "LDL": ldl.astype(int),
            "Triglyzeride": triglyzeride.astype(int),
            "Taillenumfang": taillenumfang.astype(int),
            "Hueftumfang": hueftumfang.astype(int),
            "Raucher": raucher.astype(int),
            "Alkohol_Konsum": alkohol_pro_woche,
            "Bewegung_pro_Woche": bewegung_pro_woche,
            "Familien_Diabetes": familien_diabetes.astype(int),
            "Bluthochdruck": bluthochdruck.astype(int),
            "Herz_Kreislauf_Erkrankung": herz_kreislauf.astype(int),
            "Schlafstunden": schlafstunden.round(1),
            "Stress_Level": stress_level,
            "Diabetes": diabetes.astype(int),
        }
    )

    return data


# Datensatz generieren
diabetes_data = generate_diabetes_dataset(1000)

# Speichern als CSV
diabetes_data.to_csv("diabetes_daten.csv", index=False)

# Informationen über den Datensatz anzeigen
print("\nInformationen zum generierten Datensatz:")
print(f"Anzahl der Datensätze: {len(diabetes_data)}")
print(f"Anzahl der Merkmale: {len(diabetes_data.columns)}")
print("\nVerteilung der Diabetes-Diagnosen:")
print(
    diabetes_data["Diabetes"].value_counts(normalize=True).round(3) * 100, "% der Fälle"
)

# Beispieldatensätze anzeigen
print("\nBeispieldatensätze:")
print(diabetes_data.head())
