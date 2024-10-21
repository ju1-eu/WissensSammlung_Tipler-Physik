---
title: "Vektorrechnung_Einführung"
author: "Jan Unger"
date: "2024-10-19"
---

# Vektorrechnung - Einführung

Letzte Aktualisierung: 2024-10-20

Quelle: Rießinger, Thomas. Mathematik für Ingenieure: Eine anschauliche Einführung für das praxisorientierte Studium. 9. Auflage, Springer Vieweg, 2013.

## Inhaltsverzeichnis

- [Vektorrechnung - Einführung](#vektorrechnung---einführung)
  - [Inhaltsverzeichnis](#inhaltsverzeichnis)
  - [Prompt](#prompt)

## Prompt

- Thema: Vektorrechnung / Kap. Koordinatendarstellung

- Aufgabe: Kernpunkte zusammenfassen und das Konzept etwas vertiefen
  - Ausgabe: Markdown mit LaTeX-Mathematik, beachte Sprachstil-Richtlinien

- Aufgabe: fasse alle Definitionen und Sätze zusammen

- Aufgabe: Berechne schritt-für-schritt die Lösung. Fange mit Punkt 1. an. Vergleiche Ergebnis mit der PDF.

- Visualisieren mit Python
  - Skript soll genau die Berechnungen durchführen, die in der Aufgabenstellung beschrieben sind
  - interaktiv, speichern in PNG und SVG
  - Maßstab des Plots anpassen
  - Vektorendarstellung, Koordinatenursprung (0,0,0), Pfeile und Längen
  - rechtshändiges Koordinatensystem
  - sinnvoller Name für das Python-Skript

---


1. **Definition eines Vektors**  
   Ein Vektor $\vec{AB}$ ist eine gerichtete Strecke mit dem Anfangspunkt $A$ und dem Endpunkt $B$.

2. **Definition: Gleiche Vektoren**  
   Zwei Vektoren sind gleich, wenn sie dieselbe Richtung und Länge haben. Ein Vektor wird durch seine Richtung und Länge eindeutig bestimmt.

3. **Beispiel: Kräfte als Vektoren**  
   Die auf einen Massenpunkt wirkende Kraft kann durch einen Vektor beschrieben werden, wobei der Betrag der Kraft der Länge des Vektors und die Richtung der Kraft der Richtung des Vektors entspricht.

4. **Definition der Vektoraddition**  
   Gegeben seien zwei Vektoren $a$ und $b$. Die Vektoraddition $a + b$ ergibt den Vektor, dessen Anfangspunkt dem Anfangspunkt von $a$ und dessen Endpunkt dem Endpunkt von $b$ entspricht.

5. **Bemerkung: Parallelogramm**  
   Vektoren $a$ und $b$, die denselben Anfangspunkt haben, bilden ein Parallelogramm. Die Diagonale dieses Parallelogramms entspricht der Summe $a + b$.

6. **Satz: Rechenregeln der Vektoraddition**  
   Für Vektoren $a$, $b$, $c$ gelten:
   - $a + b = b + a$ (Kommutativgesetz)
   - $(a + b) + c = a + (b + c)$ (Assoziativgesetz)

7. **Definition des Nullvektors und inversen Vektors**  
   - Der Nullvektor ist der Vektor mit demselben Anfangs- und Endpunkt: $ \vec{0} = \vec{AA} $.
   - Der inverse Vektor zu $a = \vec{AB}$ ist der Vektor $ -a = \vec{BA} $, welcher dieselbe Länge wie $a$, aber die entgegengesetzte Richtung hat.

8. **Definition der Vektorsubtraktion**  
   Die Differenz $a - b$ von zwei Vektoren wird definiert als $a - b = a + (-b)$.

9. **Definition der Multiplikation eines Vektors mit einem Skalar**  
   Für einen Vektor $a$ und einen Skalar $\lambda \in \mathbb{R}$ ist $\lambda \cdot a$ der Vektor mit:
   - Der Länge $\lambda \cdot \text{Länge}(a)$.
   - $\lambda \cdot a$ hat dieselbe Richtung wie $a$ für $\lambda > 0$, und die entgegengesetzte Richtung für $\lambda < 0$. Falls $\lambda = 0$, ist $\lambda \cdot a = \vec{0}$.

10. **Satz: Rechenregeln für die Multiplikation eines Vektors mit einem Skalar**  
    Für Vektoren $a$, $b$ und Skalare $\lambda$, $\mu \in \mathbb{R}$ gelten:
   - $(\lambda + \mu) \cdot a = \lambda \cdot a + \mu \cdot a$
   - $(\lambda \cdot \mu) \cdot a = \lambda \cdot (\mu \cdot a)$
   - $\lambda \cdot (a + b) = \lambda \cdot a + \lambda \cdot b$
