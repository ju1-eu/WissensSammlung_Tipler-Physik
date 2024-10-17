import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("Dieses Skript heißt messgenauigkeit_analyse.py")

# Generieren von Beispieldaten
np.random.seed(42)
n_measurements = 10
true_value = 2.00
noise = 0.05

measurements = np.random.normal(true_value, noise, n_measurements)
measurements = np.round(measurements, 2)

# Erstellen eines DataFrames
df = pd.DataFrame({'Messung': range(1, n_measurements + 1), 'Wert': measurements})

# Berechnung des Mittelwerts
mean_value = np.mean(measurements)

# Berechnung der Standardabweichung
std_dev = np.std(measurements, ddof=1)  # ddof=1 für Stichproben-Standardabweichung

print(f"Mittelwert: {mean_value:.2f}")
print(f"Standardabweichung: {std_dev:.2f}")

# Streudiagramm erstellen
plt.figure(figsize=(10, 6))
plt.scatter(df['Messung'], df['Wert'], color='blue')
plt.axhline(y=mean_value, color='red', linestyle='--', label=f'Mittelwert: {mean_value:.2f}')
plt.fill_between(df['Messung'], mean_value - std_dev, mean_value + std_dev, 
                 color='gray', alpha=0.2, label=f'Standardabweichung: ±{std_dev:.2f}')
plt.xlabel('Messung')
plt.ylabel('Wert')
plt.title('Streudiagramm der Messungen')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()