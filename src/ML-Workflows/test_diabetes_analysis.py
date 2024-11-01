import pytest
from sklearn.metrics import confusion_matrix
import numpy as np


def test_confusion_matrix():
    # Beispielhafte Vorhersagen und wahre Werte
    y_true = [0, 1, 0, 1, 0, 1, 0, 1, 1, 0]
    y_pred = [0, 1, 0, 1, 0, 1, 1, 0, 1, 0]

    # Berechnung der Confusion Matrix
    cm = confusion_matrix(y_true, y_pred)

    # Überprüfen, ob die Confusion Matrix die richtige Form hat
    assert cm.shape == (2, 2), "Die Confusion Matrix sollte die Form (2, 2) haben."

    # Überprüfen, ob die Werte in der Confusion Matrix korrekt sind
    expected_cm = np.array([[4, 1], [1, 4]])
    assert np.array_equal(
        cm, expected_cm
    ), "Die berechnete Confusion Matrix ist nicht korrekt."
