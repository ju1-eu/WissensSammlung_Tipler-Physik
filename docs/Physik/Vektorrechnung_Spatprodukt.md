---
title: "Vektorrechnung_Spatprodukt"
author: "Jan Unger"
date: "2024-10-19"
---

# Vektorrechnung - Spatprodukt

Letzte Aktualisierung: 2024-10-21

Quelle: Rießinger, Thomas. Mathematik für Ingenieure: Eine anschauliche Einführung für das praxisorientierte Studium. 9. Auflage, Springer Vieweg, 2013.

## Inhaltsverzeichnis

- [Vektorrechnung - Spatprodukt](#vektorrechnung---spatprodukt)
  - [Inhaltsverzeichnis](#inhaltsverzeichnis)
  - [Prompt](#prompt)
  - [Definition](#definition)
  - [Bemerkung](#bemerkung)
  - [Definition: Spatprodukt](#definition-spatprodukt)
  - [Satz: Volumen eines Spats](#satz-volumen-eines-spats)
  - [Bemerkung: Rechtssystem und Komplanarität](#bemerkung-rechtssystem-und-komplanarität)
  - [Bemerkung: Determinantenformel für das Spatprodukt](#bemerkung-determinantenformel-für-das-spatprodukt)
  - [Berechnungen](#berechnungen)
    - [Beispiel 1](#beispiel-1)
      - [1. Berechnung des Vektorprodukts](#1-berechnung-des-vektorprodukts)
      - [2. Berechnung des Spatprodukts](#2-berechnung-des-spatprodukts)
    - [Beispiel 2](#beispiel-2)
      - [1. Berechnung des Vektorprodukts](#1-berechnung-des-vektorprodukts-1)
      - [2. Berechnung des Spatprodukts](#2-berechnung-des-spatprodukts-1)
    - [Beispiel 3](#beispiel-3)
      - [1. Berechnung der Differenzvektoren](#1-berechnung-der-differenzvektoren)
      - [2. Berechnung des Vektorprodukts](#2-berechnung-des-vektorprodukts)
      - [3. Berechnung des Spatprodukts](#3-berechnung-des-spatprodukts)


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

## Definition

Das von drei Vektoren im Raum aufgespannte Gebilde heißt **Parallelepiped** oder auch **Spat**.

## Bemerkung

Gegeben seien drei Vektoren $\vec{a}, \vec{b}, \vec{c}$ im Raum. Das Volumen des aufgespannten Spats wird durch eine Kombination aus Skalarprodukt und Vektorprodukt bestimmt. Es gilt:
$$
V = \left|\vec{a} \cdot (\vec{b} \times \vec{c})\right|
$$
Das Skalarprodukt von $\vec{a}$ und dem Vektorprodukt $\vec{b} \times \vec{c}$ ergibt das Volumen des Spats.

## Definition: Spatprodukt

Das **Spatprodukt** von drei Raumvektoren $\vec{a}, \vec{b}, \vec{c}$ ist definiert als:
$$
[abc] = \vec{a} \cdot (\vec{b} \times \vec{c})
$$
Dabei ist das Spatprodukt das Skalarprodukt von $\vec{a}$ und dem Vektorprodukt von $\vec{b}$ und $\vec{c}$.

## Satz: Volumen eines Spats

Seien $\vec{a}, \vec{b}, \vec{c}$ Vektoren im Raum und $V$ das Volumen des von ihnen aufgespannten Spats. Dann gilt:

$$
V = |[abc]|
$$
Bilden $\vec{a}, \vec{b}, \vec{c}$ in dieser Reihenfolge ein Rechtssystem, so gilt:
$$
V = [abc]
$$
Andernfalls gilt:
$$
V = -[abc]
$$

## Bemerkung: Rechtssystem und Komplanarität

1. Drei Vektoren $\vec{a}, \vec{b}, \vec{c}$ bilden genau dann ein Rechtssystem, wenn:
   $$
   [abc] > 0
   $$
2. Drei Vektoren $\vec{a}, \vec{b}, \vec{c}$ liegen genau dann in einer Ebene (sie sind komplanar), wenn:
   $$
   [abc] = 0
   $$

## Bemerkung: Determinantenformel für das Spatprodukt

Das Spatprodukt lässt sich als Determinante einer $3 \times 3$-Matrix berechnen:

$$
[abc] = \det \begin{pmatrix} a_1 & a_2 & a_3 \\ b_1 & b_2 & b_3 \\ c_1 & c_2 & c_3 \end{pmatrix}
$$
Dabei sind $\vec{a} = \begin{pmatrix} a_1 \\ a_2 \\ a_3 \end{pmatrix}, \vec{b} = \begin{pmatrix} b_1 \\ b_2 \\ b_3 \end{pmatrix}, \vec{c} = \begin{pmatrix} c_1 \\ c_2 \\ c_3 \end{pmatrix}$.

## Berechnungen

### Beispiel 1

Gegeben sind die Vektoren:

$$
\vec{a} = \begin{pmatrix} 4 \\ -2 \\ 2 \end{pmatrix}, \quad \vec{b} = \begin{pmatrix} 2 \\ 2 \\ -1 \end{pmatrix}, \quad \vec{c} = \begin{pmatrix} 1 \\ 6 \\ -3 \end{pmatrix}
$$

#### 1. Berechnung des Vektorprodukts 

$\vec{b} \times \vec{c}$

Das Vektorprodukt $\vec{b} \times \vec{c}$ wird mit der Determinantenregel berechnet:

$$
\vec{b} \times \vec{c} = \begin{vmatrix} \vec{i} & \vec{j} & \vec{k} \\ 2 & 2 & -1 \\ 1 & 6 & -3 \end{vmatrix}
$$

Die Berechnung erfolgt, indem man die Determinante nach der Regel von Sarrus löst:

$$
\vec{b} \times \vec{c} = \vec{i} \cdot (2 \cdot (-3) - (-1) \cdot 6) - \vec{j} \cdot (2 \cdot (-3) - (-1) \cdot 1) + \vec{k} \cdot (2 \cdot 6 - 2 \cdot 1)
$$
$$
\vec{b} \times \vec{c} = \vec{i} \cdot (-6 + 6) - \vec{j} \cdot (-6 + 1) + \vec{k} \cdot (12 - 2)
$$
$$
\vec{b} \times \vec{c} = \vec{i} \cdot 0 - \vec{j} \cdot (-5) + \vec{k} \cdot 10
$$
$$
\vec{b} \times \vec{c} = \begin{pmatrix} 0 \\ 5 \\ 10 \end{pmatrix}
$$

#### 2. Berechnung des Spatprodukts 

$[abc]$

Nun berechnen wir das Skalarprodukt von $\vec{a}$ und $\vec{b} \times \vec{c}$:

$$
[abc] = \vec{a} \cdot (\vec{b} \times \vec{c}) = \begin{pmatrix} 4 \\ -2 \\ 2 \end{pmatrix} \cdot \begin{pmatrix} 0 \\ 5 \\ 10 \end{pmatrix}
$$
$$
[abc] = 4 \cdot 0 + (-2) \cdot 5 + 2 \cdot 10
$$
$$
[abc] = 0 - 10 + 20 = 10
$$

Das Spatprodukt beträgt $10$. Da es positiv ist, bilden die Vektoren ein Rechtssystem.


### Beispiel 2

Gegeben sind die Vektoren:

$$
\vec{a} = \begin{pmatrix} 2 \\ 0 \\ 0 \end{pmatrix}, \quad \vec{b} = \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}, \quad \vec{c} = \begin{pmatrix} 0 \\ 0 \\ 3 \end{pmatrix}
$$

#### 1. Berechnung des Vektorprodukts 

$\vec{b} \times \vec{c}$

Das Vektorprodukt $\vec{b} \times \vec{c}$ wird mit der Determinantenregel berechnet:

$$
\vec{b} \times \vec{c} = \begin{vmatrix} \vec{i} & \vec{j} & \vec{k} \\ 0 & 1 & 0 \\ 0 & 0 & 3 \end{vmatrix}
$$

Die Berechnung erfolgt:

$$
\vec{b} \times \vec{c} = \vec{i} \cdot (1 \cdot 3 - 0 \cdot 0) - \vec{j} \cdot (0 \cdot 3 - 0 \cdot 0) + \vec{k} \cdot (0 \cdot 0 - 1 \cdot 0)
$$
$$
\vec{b} \times \vec{c} = \vec{i} \cdot 3 + \vec{j} \cdot 0 + \vec{k} \cdot 0
$$
$$
\vec{b} \times \vec{c} = \begin{pmatrix} 3 \\ 0 \\ 0 \end{pmatrix}
$$

#### 2. Berechnung des Spatprodukts 

$[abc]$

Nun berechnen wir das Skalarprodukt von $\vec{a}$ und $\vec{b} \times \vec{c}$:

$$
[abc] = \vec{a} \cdot (\vec{b} \times \vec{c}) = \begin{pmatrix} 2 \\ 0 \\ 0 \end{pmatrix} \cdot \begin{pmatrix} 3 \\ 0 \\ 0 \end{pmatrix}
$$
$$
[abc] = 2 \cdot 3 + 0 \cdot 0 + 0 \cdot 0
$$
$$
[abc] = 6
$$

Das Spatprodukt beträgt $6$, was dem Volumen des aufgespannten Quaders entspricht. Da es positiv ist, bilden die Vektoren ebenfalls ein Rechtssystem.

### Beispiel 3

Gegeben sind die Punkte:

$$
A = (1, 2, 3), \quad B = (2, -1, 0), \quad C = (0, -3, 4)
$$

Die Ortsvektoren lauten:
$$
\vec{a} = \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix}, \quad \vec{b} = \begin{pmatrix} 2 \\ -1 \\ 0 \end{pmatrix}, \quad \vec{c} = \begin{pmatrix} 0 \\ -3 \\ 4 \end{pmatrix}
$$

#### 1. Berechnung der Differenzvektoren

Zunächst berechnen wir die Differenzvektoren:

$$
\vec{b} - \vec{a} = \begin{pmatrix} 2 \\ -1 \\ 0 \end{pmatrix} - \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix} = \begin{pmatrix} 1 \\ -3 \\ -3 \end{pmatrix}
$$
$$
\vec{c} - \vec{a} = \begin{pmatrix} 0 \\ -3 \\ 4 \end{pmatrix} - \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix} = \begin{pmatrix} -1 \\ -5 \\ 1 \end{pmatrix}
$$

#### 2. Berechnung des Vektorprodukts 

$(\vec{b} - \vec{a}) \times (\vec{c} - \vec{a})$

Das Vektorprodukt $(\vec{b} - \vec{a}) \times (\vec{c} - \vec{a})$ wird mit der Determinantenregel berechnet:

$$
(\vec{b} - \vec{a}) \times (\vec{c} - \vec{a}) = \begin{vmatrix} \vec{i} & \vec{j} & \vec{k} \\ 1 & -3 & -3 \\ -1 & -5 & 1 \end{vmatrix}
$$

Die Berechnung erfolgt wie folgt:

$$
(\vec{b} - \vec{a}) \times (\vec{c} - \vec{a}) = \vec{i} \cdot (-3 \cdot 1 - (-3) \cdot (-5)) - \vec{j} \cdot (1 \cdot 1 - (-3) \cdot (-1)) + \vec{k} \cdot (1 \cdot (-5) - (-3) \cdot (-1))
$$
$$
= \vec{i} \cdot (-3 - 15) - \vec{j} \cdot (1 - 3) + \vec{k} \cdot (-5 - 3)
$$
$$
= \vec{i} \cdot (-18) - \vec{j} \cdot (-2) + \vec{k} \cdot (-8)
$$
$$
= \begin{pmatrix} -18 \\ 2 \\ -8 \end{pmatrix}
$$

#### 3. Berechnung des Spatprodukts 

$[abc]$

Nun berechnen wir das Skalarprodukt von $\vec{a}$ und $(\vec{b} - \vec{a}) \times (\vec{c} - \vec{a})$:

$$
[abc] = (\vec{a} - \vec{A}) \cdot \left( (\vec{b} - \vec{a}) \times (\vec{c} - \vec{a}) \right) = \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix} \cdot \begin{pmatrix} -18 \\ 2 \\ -8 \end{pmatrix}
$$
$$
[abc] = 1 \cdot (-18) + 2 \cdot 2 + 3 \cdot (-8)
$$
$$
[abc] = -18 + 4 - 24 = -38
$$

Das Spatprodukt beträgt $-38$, was bedeutet, dass die drei Vektoren ein Linkssystem bilden.

