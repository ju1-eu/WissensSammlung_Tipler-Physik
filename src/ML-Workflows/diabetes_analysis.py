from ml_workflow import MLWorkflow

# ML Workflow initialisieren
ml_workflow = MLWorkflow()

# Daten laden und vorbereiten
ml_workflow.load_data("diabetes_daten.csv")

# Wichtige Features auswählen
selected_features = [
    "Alter",
    "BMI",
    "Blutdruck_Systolisch",
    "Blutzucker_Nuechtern",
    "HbA1c",
    "Cholesterin_Gesamt",
    "Taillenumfang",
    "Familien_Diabetes",
    "Bluthochdruck",
    "Herz_Kreislauf_Erkrankung",
]

# Daten mit ausgewählten Features vorbereiten
ml_workflow.prepare_data("Diabetes", features=selected_features)

# Modell mit Grid Search trainieren
param_grid = {
    "classifier__n_estimators": [100, 200],
    "classifier__max_depth": [10, 20, None],
    "classifier__min_samples_split": [2, 5],
}

ml_workflow.train_model(perform_gridsearch=True, param_grid=param_grid)

# Modell evaluieren
ml_workflow.evaluate_model()

# Kreuzvalidierung durchführen
ml_workflow.cross_validate()
