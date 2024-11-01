import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.pipeline import Pipeline
import matplotlib.pyplot as plt
import seaborn as sns


class MLWorkflow:
    def __init__(self, random_state=42):
        """Initialisiert den ML Workflow."""
        self.random_state = random_state
        self.scaler = StandardScaler()
        self.model = None
        self.data = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None

    def load_data(self, file_path):
        """Lädt die Daten aus einer CSV-Datei."""
        try:
            self.data = pd.read_csv(file_path)
            print("\nDatenübersicht:")
            print(f"Anzahl Datensätze: {len(self.data)}")
            print(f"Anzahl Features: {len(self.data.columns)}")
            print("\nFeatures:")
            print(self.data.columns.tolist())
            print("\nFehlende Werte:")
            print(self.data.isnull().sum())

            # Datentypen anzeigen
            print("\nDatentypen:")
            print(self.data.dtypes)

        except Exception as e:
            print(f"Fehler beim Laden der Daten: {str(e)}")
            raise

    def prepare_data(self, target_column, features=None):
        """Bereitet die Daten für das Training vor."""
        try:
            if features is None:
                features = [col for col in self.data.columns if col != target_column]

            print(f"\nVerwendete Features: {features}")
            print(f"Zielvariable: {target_column}")

            X = self.data[features]
            y = self.data[target_column]

            # Daten aufteilen
            self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
                X, y, test_size=0.2, random_state=self.random_state
            )

            print(f"\nTrainingsdaten Shape: {self.X_train.shape}")
            print(f"Testdaten Shape: {self.X_test.shape}")

            # Verteilung der Zielvariable anzeigen
            print("\nVerteilung der Zielvariable:")
            print("Training:", pd.Series(self.y_train).value_counts(normalize=True))
            print("Test:", pd.Series(self.y_test).value_counts(normalize=True))

        except Exception as e:
            print(f"Fehler bei der Datenvorbereitung: {str(e)}")
            raise

    def train_model(self, model=None, perform_gridsearch=False, param_grid=None):
        """Trainiert das Modell mit optionalem Grid Search."""
        try:
            if model is None:
                model = RandomForestClassifier(random_state=self.random_state)

            if perform_gridsearch and param_grid:
                print("\nFühre Grid Search durch...")
                pipeline = Pipeline([("scaler", self.scaler), ("classifier", model)])

                grid_search = GridSearchCV(
                    pipeline, param_grid, cv=5, scoring="accuracy", n_jobs=-1
                )
                grid_search.fit(self.X_train, self.y_train)

                print("\nBeste Parameter:", grid_search.best_params_)
                print("Beste CV-Genauigkeit:", grid_search.best_score_)
                self.model = grid_search.best_estimator_

            else:
                print("\nTrainiere Modell ohne Grid Search...")
                pipeline = Pipeline([("scaler", self.scaler), ("classifier", model)])
                self.model = pipeline.fit(self.X_train, self.y_train)

        except Exception as e:
            print(f"Fehler beim Modelltraining: {str(e)}")
            raise

    def evaluate_model(self):
        """Evaluiert das trainierte Modell und speichert Visualisierungen."""
        try:
            # Vorhersagen machen
            y_pred = self.model.predict(self.X_test)

            # Genauigkeit berechnen
            accuracy = accuracy_score(self.y_test, y_pred)
            print(f"\nTest-Genauigkeit: {accuracy:.4f}")

            # Klassifikationsbericht
            print("\nKlassifikationsbericht:")
            print(classification_report(self.y_test, y_pred))

            # Confusion Matrix visualisieren und speichern
            plt.figure(figsize=(8, 6))
            cm = confusion_matrix(self.y_test, y_pred)
            sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
            plt.title("Confusion Matrix")
            plt.ylabel("Wahre Labels")
            plt.xlabel("Vorhergesagte Labels")

            # Speichern in verschiedenen Formaten
            plt.savefig(
                "docs/images/confusion_matrix.png", dpi=300, bbox_inches="tight"
            )
            plt.savefig(
                "docs/images/confusion_matrix.pdf", format="pdf", bbox_inches="tight"
            )
            plt.savefig(
                "docs/images/confusion_matrix.svg", format="svg", bbox_inches="tight"
            )
            plt.show()

            # Feature Importance für Random Forest
            if isinstance(self.model.named_steps["classifier"], RandomForestClassifier):
                feature_importance = pd.DataFrame(
                    {
                        "feature": self.X_train.columns,
                        "importance": self.model.named_steps[
                            "classifier"
                        ].feature_importances_,
                    }
                )
                feature_importance = feature_importance.sort_values(
                    "importance", ascending=False
                )

                plt.figure(figsize=(10, 6))
                sns.barplot(x="importance", y="feature", data=feature_importance)
                plt.title("Feature Importance")

                # Speichern in verschiedenen Formaten
                plt.savefig(
                    "docs/images/feature_importance.png", dpi=300, bbox_inches="tight"
                )
                plt.savefig(
                    "docs/images/feature_importance.pdf",
                    format="pdf",
                    bbox_inches="tight",
                )
                plt.savefig(
                    "docs/images/feature_importance.svg",
                    format="svg",
                    bbox_inches="tight",
                )
                plt.show()

                # Speichern der Feature Importance Daten als CSV
                feature_importance.to_csv(
                    "docs/images/feature_importance.csv", index=False
                )

            print("\nVisualisierungen wurden gespeichert als:")
            print("- docs/images/confusion_matrix.png/pdf/svg")
            print("- docs/images/feature_importance.png/pdf/svg")
            print("- docs/images/feature_importance.csv")

        except Exception as e:
            print(f"Fehler bei der Modellevaluation: {str(e)}")
            raise

    def cross_validate(self, cv=5):
        """Führt eine Kreuzvalidierung durch."""
        try:
            print(f"\nFühre {cv}-fold Kreuzvalidierung durch...")
            scores = cross_val_score(
                self.model,
                self.X_train,
                self.y_train,
                cv=cv,
                scoring="accuracy",
                n_jobs=-1,
            )

            print("Kreuzvalidierungs-Scores:", scores)
            print(
                f"Mittlere CV-Genauigkeit: {scores.mean():.4f} (+/- {scores.std() * 2:.4f})"
            )

        except Exception as e:
            print(f"Fehler bei der Kreuzvalidierung: {str(e)}")
            raise
