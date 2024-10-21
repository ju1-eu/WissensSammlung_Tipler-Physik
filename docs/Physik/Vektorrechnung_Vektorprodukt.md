---
title: "Vektorrechnung_Vektorprodukt"
author: "Jan Unger"
date: "2024-10-19"
---

# Vektorrechnung - Vektorprodukt

Letzte Aktualisierung: 2024-10-21

Quelle: Rießinger, Thomas. Mathematik für Ingenieure: Eine anschauliche Einführung für das praxisorientierte Studium. 9. Auflage, Springer Vieweg, 2013.

## Inhaltsverzeichnis

- [Vektorrechnung - Vektorprodukt](#vektorrechnung---vektorprodukt)
  - [Inhaltsverzeichnis](#inhaltsverzeichnis)
  - [Prompt](#prompt)
  - [Lemma: Fläche eines Parallelogramms](#lemma-fläche-eines-parallelogramms)
  - [Lemma: Orthogonalität](#lemma-orthogonalität)
  - [Definition: Vektorprodukt](#definition-vektorprodukt)
  - [Satz: Rechenregeln für das Vektorprodukt](#satz-rechenregeln-für-das-vektorprodukt)
  - [Satz: Formel für das Vektorprodukt](#satz-formel-für-das-vektorprodukt)
  - [Bemerkung: Determinantenformel für das Vektorprodukt](#bemerkung-determinantenformel-für-das-vektorprodukt)
  - [Berechnungen](#berechnungen)
    - [Beispiel 1](#beispiel-1)
      - [Schritt 1: Berechnung des Vektorprodukts](#schritt-1-berechnung-des-vektorprodukts)
      - [Schritt 2: Ergebnis](#schritt-2-ergebnis)
    - [Beispiel 2](#beispiel-2)
      - [Schritt 1: Berechnung der Vektoren](#schritt-1-berechnung-der-vektoren)
      - [Schritt 2: Berechnung des Vektorprodukts](#schritt-2-berechnung-des-vektorprodukts)
      - [Schritt 3: Berechnung der Länge](#schritt-3-berechnung-der-länge)
      - [Schritt 4: Ergebnis](#schritt-4-ergebnis)
    - [Beispiele 3 mit der Sarrus-Regel](#beispiele-3-mit-der-sarrus-regel)
      - [Schritt 1: Aufstellen der Determinante](#schritt-1-aufstellen-der-determinante)
      - [Schritt 2: Anwendung der Sarrus-Regel](#schritt-2-anwendung-der-sarrus-regel)
      - [Schritt 3: Berechnung des Ergebnisses](#schritt-3-berechnung-des-ergebnisses)
    - [Beispiel 4](#beispiel-4)


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

## Lemma: Fläche eines Parallelogramms

Die Fläche des von zwei Vektoren $\vec{a}$ und $\vec{b}$ gebildeten Parallelogramms beträgt:
$$
|\vec{a}| \cdot |\vec{b}| \cdot \sin(\varphi)
$$
wobei $\varphi$ der Winkel zwischen $\vec{a}$ und $\vec{b}$ ist, mit $0^\circ \leq \varphi \leq 180^\circ$.

## Lemma: Orthogonalität

Zwei Vektoren $\vec{x}$ und $\vec{y}$ stehen genau dann senkrecht aufeinander, wenn:
$$
\vec{x} \cdot \vec{y} = 0
$$

## Definition: Vektorprodukt

Das Vektorprodukt $\vec{c} = \vec{a} \times \vec{b}$ zweier Vektoren $\vec{a}$ und $\vec{b}$ ist der Vektor, der folgende Eigenschaften erfüllt:

1. Die Länge von $\vec{c}$ entspricht der Fläche des von $\vec{a}$ und $\vec{b}$ gebildeten Parallelogramms:
   $$
   |\vec{c}| = |\vec{a}| \cdot |\vec{b}| \cdot \sin(\varphi)
   $$
2. $\vec{c}$ steht senkrecht auf $\vec{a}$ und $\vec{b}$, d. h.:
   $$
   \vec{c} \cdot \vec{a} = 0, \quad \vec{c} \cdot \vec{b} = 0
   $$
3. Die Vektoren $\vec{a}, \vec{b}, \vec{c}$ bilden in dieser Reihenfolge ein Rechtssystem.

## Satz: Rechenregeln für das Vektorprodukt

Für die Vektoren $\vec{a}, \vec{b}, \vec{c}$ gelten die folgenden Regeln:

1. $\vec{a} \times \vec{b} = -(\vec{b} \times \vec{a})$
2. $(\lambda \cdot \vec{a}) \times \vec{b} = \lambda \cdot (\vec{a} \times \vec{b}) = \vec{a} \times (\lambda \cdot \vec{b}) \quad \text{für} \quad \lambda \in \mathbb{R}$
3. $(\vec{a} + \vec{b}) \times \vec{c} = \vec{a} \times \vec{c} + \vec{b} \times \vec{c}$
4. $\vec{c} \times (\vec{a} + \vec{b}) = \vec{c} \times \vec{a} + \vec{c} \times \vec{b}$
5. $\vec{a} \times \vec{b} = 0$ genau dann, wenn $\vec{a} \parallel \vec{b}$ (kollinear).

## Satz: Formel für das Vektorprodukt

Für die Vektoren $\vec{a} = \begin{pmatrix} a_1 \\ a_2 \\ a_3 \end{pmatrix}$ und $\vec{b} = \begin{pmatrix} b_1 \\ b_2 \\ b_3 \end{pmatrix}$ lautet das Vektorprodukt:
$$
\vec{a} \times \vec{b} = \begin{pmatrix} a_2 \cdot b_3 - a_3 \cdot b_2 \\ a_3 \cdot b_1 - a_1 \cdot b_3 \\ a_1 \cdot b_2 - a_2 \cdot b_1 \end{pmatrix}
$$

## Bemerkung: Determinantenformel für das Vektorprodukt

Das Vektorprodukt $\vec{a} \times \vec{b}$ lässt sich auch als Determinante einer $3 \times 3$-Matrix schreiben:

$$
\vec{a} \times \vec{b} = \det \begin{pmatrix} \vec{i} & \vec{j} & \vec{k} \\ a_1 & a_2 & a_3 \\ b_1 & b_2 & b_3 \end{pmatrix}
$$

## Berechnungen

### Beispiel 1

Gegeben sind die Vektoren:

$$
\vec{a} = \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix}, \quad \vec{b} = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}
$$

#### Schritt 1: Berechnung des Vektorprodukts

Das Vektorprodukt $\vec{a} \times \vec{b}$ kann mit der folgenden Formel berechnet werden:
$$
\vec{a} \times \vec{b} = \begin{pmatrix} a_2 \cdot b_3 - a_3 \cdot b_2 \\ a_3 \cdot b_1 - a_1 \cdot b_3 \\ a_1 \cdot b_2 - a_2 \cdot b_1 \end{pmatrix}
$$
Hier sind die Komponenten von $\vec{a}$ und $\vec{b}$:
$$
\vec{a} = \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix}, \quad \vec{b} = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}
$$
Setzen wir diese Komponenten in die Formel ein:

1. **Erste Komponente**:
   $$
   a_2 \cdot b_3 - a_3 \cdot b_2 = 1 \cdot 0 - 0 \cdot 0 = 0
   $$

2. **Zweite Komponente**:
   $$
   a_3 \cdot b_1 - a_1 \cdot b_3 = 0 \cdot 1 - 1 \cdot 0 = 0
   $$

3. **Dritte Komponente**:
   $$
   a_1 \cdot b_2 - a_2 \cdot b_1 = 1 \cdot 0 - 1 \cdot 1 = -1
   $$

Damit ergibt sich das Vektorprodukt:
$$
\vec{a} \times \vec{b} = \begin{pmatrix} 0 \\ 0 \\ -1 \end{pmatrix}
$$

#### Schritt 2: Ergebnis

Das Vektorprodukt von $\vec{a}$ und $\vec{b}$ ist:
$$
\vec{a} \times \vec{b} = \begin{pmatrix} 0 \\ 0 \\ -1 \end{pmatrix}
$$

### Beispiel 2

Gegeben sind die Punkte:
$$
A = (0, 1, 2), \quad B = (2, 3, 1), \quad C = (1, 7, -1)
$$

#### Schritt 1: Berechnung der Vektoren 

$\vec{a} = \overrightarrow{AB}$ und $\vec{b} = \overrightarrow{AC}$

Zuerst berechnen wir die Vektoren $\vec{a}$ und $\vec{b}$, die von den Punkten $A$ zu $B$ bzw. $A$ zu $C$ verlaufen.

$$
\vec{a} = \overrightarrow{AB} = B - A = \begin{pmatrix} 2 \\ 3 \\ 1 \end{pmatrix} - \begin{pmatrix} 0 \\ 1 \\ 2 \end{pmatrix} = \begin{pmatrix} 2 \\ 2 \\ -1 \end{pmatrix}
$$
$$
\vec{b} = \overrightarrow{AC} = C - A = \begin{pmatrix} 1 \\ 7 \\ -1 \end{pmatrix} - \begin{pmatrix} 0 \\ 1 \\ 2 \end{pmatrix} = \begin{pmatrix} 1 \\ 6 \\ -3 \end{pmatrix}
$$

#### Schritt 2: Berechnung des Vektorprodukts 

$\vec{a} \times \vec{b}$

Das Vektorprodukt $\vec{a} \times \vec{b}$ wird mit der Formel berechnet:
$$
\vec{a} \times \vec{b} = \begin{pmatrix} a_2 \cdot b_3 - a_3 \cdot b_2 \\ a_3 \cdot b_1 - a_1 \cdot b_3 \\ a_1 \cdot b_2 - a_2 \cdot b_1 \end{pmatrix}
$$
Setzen wir die Komponenten von $\vec{a} = \begin{pmatrix} 2 \\ 2 \\ -1 \end{pmatrix}$ und $\vec{b} = \begin{pmatrix} 1 \\ 6 \\ -3 \end{pmatrix}$ in die Formel ein:

1. **Erste Komponente**:
   $$
   a_2 \cdot b_3 - a_3 \cdot b_2 = 2 \cdot (-3) - (-1) \cdot 6 = -6 + 6 = 0
   $$

2. **Zweite Komponente**:
   $$
   a_3 \cdot b_1 - a_1 \cdot b_3 = (-1) \cdot 1 - 2 \cdot (-3) = -1 + 6 = 5
   $$

3. **Dritte Komponente**:
   $$
   a_1 \cdot b_2 - a_2 \cdot b_1 = 2 \cdot 6 - 2 \cdot 1 = 12 - 2 = 10
   $$

Damit ergibt sich das Vektorprodukt:
$$
\vec{a} \times \vec{b} = \begin{pmatrix} 0 \\ 5 \\ 10 \end{pmatrix}
$$

#### Schritt 3: Berechnung der Länge 

von $\vec{a} \times \vec{b}$

Die Länge des Vektors $\vec{a} \times \vec{b}$ entspricht der Fläche des aufgespannten Parallelogramms:
$$
|\vec{a} \times \vec{b}| = \sqrt{0^2 + 5^2 + 10^2} = \sqrt{0 + 25 + 100} = \sqrt{125} = 11,18
$$

#### Schritt 4: Ergebnis

Die Fläche des von $A$, $B$ und $C$ aufgespannten Parallelogramms beträgt:
$$
|\vec{a} \times \vec{b}| = 11,18
$$

### Beispiele 3 mit der Sarrus-Regel

Gegeben sind die Vektoren:
$$
\vec{a} = \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix}, \quad \vec{b} = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}
$$

Wir berechnen das Vektorprodukt $\vec{a} \times \vec{b}$ mithilfe der **Sarrus-Regel**.

#### Schritt 1: Aufstellen der Determinante

Das Vektorprodukt lässt sich als Determinante einer $3 \times 3$-Matrix darstellen:
$$
\vec{a} \times \vec{b} = \det \begin{pmatrix} \vec{i} & \vec{j} & \vec{k} \\ 1 & 1 & 0 \\ 1 & 0 & 0 \end{pmatrix}
$$

#### Schritt 2: Anwendung der Sarrus-Regel

Für die Sarrus-Regel werden die ersten beiden Spalten der Matrix wiederholt:
$$
\begin{pmatrix} \vec{i} & \vec{j} & \vec{k} & \vec{i} & \vec{j} \\ 1 & 1 & 0 & 1 & 1 \\ 1 & 0 & 0 & 1 & 0 \end{pmatrix}
$$
Nun multiplizieren wir die Diagonalen:

- Positive Diagonalen:
  $$
  \vec{i} \cdot 1 \cdot 0 = 0, \quad \vec{j} \cdot 0 \cdot 1 = 0, \quad \vec{k} \cdot 1 \cdot 1 = \vec{k}
  $$

- Negative Diagonalen:
  $$
  \vec{k} \cdot 1 \cdot 1 = \vec{k}, \quad \vec{j} \cdot 1 \cdot 0 = 0, \quad \vec{i} \cdot 0 \cdot 1 = 0
  $$

#### Schritt 3: Berechnung des Ergebnisses

Nun addieren und subtrahieren wir die Ergebnisse der Diagonalen:
$$
\vec{a} \times \vec{b} = 0 + 0 + \vec{k} - \vec{k} - 0 - 0 = -\vec{k}
$$

Das Vektorprodukt lautet somit:
$$
\vec{a} \times \vec{b} = \begin{pmatrix} 0 \\ 0 \\ -1 \end{pmatrix}
$$

### Beispiel 4

Gegeben sind die Vektoren:
$$
\vec{a} = \begin{pmatrix} 2 \\ 2 \\ -1 \end{pmatrix}, \quad \vec{b} = \begin{pmatrix} 1 \\ 6 \\ -3 \end{pmatrix}
$$

Wir berechnen das Vektorprodukt $\vec{a} \times \vec{b}$ mithilfe der **Sarrus-Regel**.

Nach Überprüfung der im Bild gezeigten Berechnung ergibt sich für das Vektorprodukt:

$$
\vec{a} = \begin{pmatrix} 2 \\ 2 \\ -1 \end{pmatrix}, \quad \vec{b} = \begin{pmatrix} 1 \\ 6 \\ -3 \end{pmatrix}
$$

Das Vektorprodukt $\vec{a} \times \vec{b}$ wird durch die Determinante berechnet:

$$
\vec{a} \times \vec{b} = \det \begin{pmatrix} \vec{e_1} & \vec{e_2} & \vec{e_3} \\ 2 & 2 & -1 \\ 1 & 6 & -3 \end{pmatrix}
$$

Durch Anwendung der Sarrus-Regel ergibt sich das Schema:

$$
\begin{pmatrix} \vec{e_1} & \vec{e_2} & \vec{e_3} & \vec{e_1} & \vec{e_2} \\ 2 & 2 & -1 & 2 & 2 \\ 1 & 6 & -3 & 1 & 6 \end{pmatrix}
$$

Die Berechnung erfolgt wie folgt:

- **Positive Diagonalen**:
  $$
  2 \cdot (-3) \cdot \vec{e_1} = -6 \vec{e_1}, \quad (-1) \cdot 1 \cdot \vec{e_2} = \vec{e_2}, \quad 2 \cdot 6 \cdot \vec{e_3} = 12 \vec{e_3}
  $$

- **Negative Diagonalen**:
  $$
  1 \cdot 2 \cdot \vec{e_3} = 2 \vec{e_3}, \quad (-3) \cdot 2 \cdot \vec{e_2} = 6 \vec{e_2}, \quad (-1) \cdot 6 \cdot \vec{e_1} = 6 \vec{e_1}
  $$

Nun subtrahieren wir die negativen Diagonalen von den positiven:

$$
\vec{a} \times \vec{b} = (-6 \vec{e_1} + \vec{e_2} + 12 \vec{e_3}) - (2 \vec{e_3} + 6 \vec{e_2} + 6 \vec{e_1})
$$
$$
= (-6 \vec{e_1} - 6 \vec{e_1}) + (\vec{e_2} - 6 \vec{e_2}) + (12 \vec{e_3} - 2 \vec{e_3})
$$
$$
= 0 \vec{e_1} + 5 \vec{e_2} + 10 \vec{e_3}
$$

Das Vektorprodukt lautet somit:
$$
\vec{a} \times \vec{b} = \begin{pmatrix} 0 \\ 5 \\ 10 \end{pmatrix}
$$
