---
title: "Vektorrechnung_Kap_Koordinatendarstellung"
author: "Jan Unger"
date: "2024-10-19"
---

# Vektorrechnung - Koordinatendarstellung

Letzte Aktualisierung: 2024-10-20

Quelle: Rießinger, Thomas. Mathematik für Ingenieure: Eine anschauliche Einführung für das praxisorientierte Studium. 9. Auflage, Springer Vieweg, 2013.

## Inhaltsverzeichnis

- [Vektorrechnung - Koordinatendarstellung](#vektorrechnung---koordinatendarstellung)
  - [Inhaltsverzeichnis](#inhaltsverzeichnis)
  - [Prompt](#prompt)
  - [Koordinatendarstellung von Vektoren](#koordinatendarstellung-von-vektoren)
  - [Vektoroperationen in Koordinatendarstellung](#vektoroperationen-in-koordinatendarstellung)
  - [Definitionen](#definitionen)
  - [Sätze](#sätze)
  - [Einheitsvektoren](#einheitsvektoren)
  - [Beispiele](#beispiele)
    - [Beispiel 1: Berechnung des Betrags eines zweidimensionalen Vektors](#beispiel-1-berechnung-des-betrags-eines-zweidimensionalen-vektors)
    - [Beispiel 2: Berechnung des Betrags eines dreidimensionalen Vektors](#beispiel-2-berechnung-des-betrags-eines-dreidimensionalen-vektors)
    - [Beispiel 3: Bestimmung der Koordinaten und des Winkels eines Vektors](#beispiel-3-bestimmung-der-koordinaten-und-des-winkels-eines-vektors)
    - [Beispiel 4: Vektoraddition und -subtraktion](#beispiel-4-vektoraddition-und--subtraktion)
    - [Beispiel 5: Skalare Multiplikation](#beispiel-5-skalare-multiplikation)
    - [Beispiel 6: Kraftvektorberechnung](#beispiel-6-kraftvektorberechnung)
    - [Beispiel 7: Berechnung der resultierenden Kräfte](#beispiel-7-berechnung-der-resultierenden-kräfte)
    - [Beispiel 8: Berechnung der fehlenden Kraft](#beispiel-8-berechnung-der-fehlenden-kraft)
    - [Beispiele 9](#beispiele-9)

## Prompt

- Thema: Vektorrechnung / Kap. Koordinatendarstellung

- Aufgabe: Kernpunkte zusammenfassen und das Konzept etwas vertiefen
  - Ausgabe: Markdown mit LaTeX-Mathematik, beachte Sprachstil-Richtlinien
Thema: Vektorrechnung / Kap. Koordinatendarstellung

- Aufgabe: fasse alle Definitionen und Sätze zusammen

- Aufgabe: Berechne schritt-für-schritt die Lösung. Fange mit Punkt 1. an. Vergleiche Ergebnis mit der PDF.

- Visualisieren mit Python
  - interaktiv, speichern in PNG und SVG

---

## Koordinatendarstellung von Vektoren

- Vektoren können durch Koordinaten dargestellt werden:
  - 2D: 
  $$
  \mathbf{a} = \begin{pmatrix} a_1 \\ a_2 \end{pmatrix}
  $$
  - 3D: 
  $$
  \mathbf{a} = \begin{pmatrix} a_1 \\ a_2 \\ a_3 \end{pmatrix}
  $$

- Der Betrag eines Vektors berechnet sich durch:
  - 2D: 
  $$
  |\mathbf{a}| = \sqrt{a_1^2 + a_2^2}
  $$
  - 3D: 
  $$
  |\mathbf{a}| = \sqrt{a_1^2 + a_2^2 + a_3^2}
  $$

- Winkel und Koordinaten hängen zusammen:
  $$
  a_1 = |\mathbf{a}| \cdot \cos\varphi \quad \text{und} \quad a_2 = |\mathbf{a}| \cdot \sin\varphi
  $$

## Vektoroperationen in Koordinatendarstellung

- Addition/Subtraktion:
  $$
  \begin{pmatrix} a_1 \\ a_2 \end{pmatrix} \pm \begin{pmatrix} b_1 \\ b_2 \end{pmatrix} = \begin{pmatrix} a_1 \pm b_1 \\ a_2 \pm b_2 \end{pmatrix}
  $$

- Skalare Multiplikation:
  $$
  \lambda \cdot \begin{pmatrix} a_1 \\ a_2 \end{pmatrix} = \begin{pmatrix} \lambda a_1 \\ \lambda a_2 \end{pmatrix}
  $$




## Definitionen

1. **Koordinatendarstellung eines Vektors**:
   - 2D: 
   $$
   \mathbf{a} = \begin{pmatrix} a_1 \\ a_2 \end{pmatrix}
   $$
   - 3D: 
   $$
   \mathbf{a} = \begin{pmatrix} a_1 \\ a_2 \\ a_3 \end{pmatrix}
   $$

2. **Betrag eines Vektors**:
   - 2D: 
   $$
   |\mathbf{a}| = \sqrt{a_1^2 + a_2^2}
   $$
   - 3D: 
   $$
   |\mathbf{a}| = \sqrt{a_1^2 + a_2^2 + a_3^2}
   $$

3. **Rechtssystem**: Drei Vektoren $\mathbf{x}$, $\mathbf{y}$, $\mathbf{z}$ bilden ein Rechtssystem, wenn die rechte Hand so gehalten werden kann, dass Daumen, Zeigefinger und Mittelfinger in dieser Reihenfolge in die Richtung von $\mathbf{x}$, $\mathbf{y}$ bzw. $\mathbf{z}$ zeigen.

4. **Linkssystem**: Analog zum Rechtssystem, aber mit der linken Hand.

## Sätze

1. **Zusammenhang zwischen Winkel und Koordinaten** (2D):
   Für einen Vektor $\mathbf{a}$ mit Winkel $\varphi$ zur x-Achse gilt:
   $$
   a_1 = |\mathbf{a}| \cdot \cos\varphi \quad \text{und} \quad a_2 = |\mathbf{a}| \cdot \sin\varphi
   $$

2. **Vektoraddition und -subtraktion**:
   - 2D: 
   $$
   (a_1, a_2) \pm (b_1, b_2) = (a_1 \pm b_1, a_2 \pm b_2)
   $$
   - 3D: 
   $$
   \begin{pmatrix} a_1 \\ a_2 \\ a_3 \end{pmatrix} \pm \begin{pmatrix} b_1 \\ b_2 \\ b_3 \end{pmatrix} = \begin{pmatrix} a_1 \pm b_1 \\ a_2 \pm b_2 \\ a_3 \pm b_3 \end{pmatrix}
   $$

3. **Skalare Multiplikation**:
   - 2D: 
   $$
   \lambda \cdot (a_1, a_2) = (\lambda a_1, \lambda a_2)
   $$
   - 3D: 
   $$
   \lambda \cdot \begin{pmatrix} a_1 \\ a_2 \\ a_3 \end{pmatrix} = \begin{pmatrix} \lambda a_1 \\ \lambda a_2 \\ \lambda a_3 \end{pmatrix}
   $$

4. **Koordinaten eines Vektors zwischen zwei Punkten**:
   Für einen Vektor $\mathbf{a}$ von Punkt $P_1(a_1, a_2)$ zu $P_2(b_1, b_2)$ gilt:
   $$
   \mathbf{a} = (b_1 - a_1, b_2 - a_2)
   $$


## Einheitsvektoren

1. **Definition**:
   Einheitsvektoren sind Vektoren mit einer Länge von 1 Längeneinheit.

2. **Standardeinheitsvektoren**:
   - In 2D:
     $$
     \mathbf{e}_1 = \begin{pmatrix} 1 \\ 0 \end{pmatrix} \quad \text{und} \quad \mathbf{e}_2 = \begin{pmatrix} 0 \\ 1 \end{pmatrix}
     $$
   - In 3D:
     $$
     \mathbf{e}_1 = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}, \quad \mathbf{e}_2 = \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix} \quad \text{und} \quad \mathbf{e}_3 = \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}
     $$

3. **Eigenschaften**:
   - Einheitsvektoren stehen senkrecht aufeinander.
   - Sie bilden die Basis des Koordinatensystems.
   - In 3D bilden sie ein Rechtssystem.

4. **Darstellung beliebiger Vektoren**:
   Jeder Vektor lässt sich als Linearkombination der Einheitsvektoren darstellen:
   - In 2D: 
   $$
   \mathbf{a} = a_1 \mathbf{e}_1 + a_2 \mathbf{e}_2 = \begin{pmatrix} a_1 \\ a_2 \end{pmatrix}
   $$
   - In 3D: 
   $$
   \mathbf{a} = a_1 \mathbf{e}_1 + a_2 \mathbf{e}_2 + a_3 \mathbf{e}_3 = \begin{pmatrix} a_1 \\ a_2 \\ a_3 \end{pmatrix}
   $$

5. **Verwendung**:
   - Einheitsvektoren vereinfachen die Darstellung und Berechnung von Vektoren.
   - Sie dienen als Referenz für die Richtungen im Koordinatensystem.
   - In der Physik werden sie oft zur Beschreibung von Richtungen verwendet, z.B. bei Kräften oder Geschwindigkeiten.

6. **Normierung**:
   Jeder Vektor $\mathbf{a} \neq \mathbf{0}$ kann zu einem Einheitsvektor normiert werden:
   $$
   \mathbf{e}_a = \frac{\mathbf{a}}{|\mathbf{a}|}
   $$

## Beispiele

### Beispiel 1: Berechnung des Betrags eines zweidimensionalen Vektors

Gegeben ist der Vektor $\mathbf{a} = \begin{pmatrix} 3 \\ 4 \end{pmatrix}$. Berechnen Sie den Betrag $|\mathbf{a}|$.

**Lösung:**

1. Wir verwenden die Formel für den Betrag eines zweidimensionalen Vektors:
   $$
   |\mathbf{a}| = \sqrt{a_1^2 + a_2^2}
   $$
2. Setzen wir die Werte ein:
   $$
   |\mathbf{a}| = \sqrt{3^2 + 4^2}
   $$
3. Berechnen wir die Quadrate:
   $$
   |\mathbf{a}| = \sqrt{9 + 16}
   $$
4. Addieren wir unter der Wurzel:
   $$
   |\mathbf{a}| = \sqrt{25}
   $$
5. Ziehen wir die Wurzel:
   $$
   |\mathbf{a}| = 5
   $$

**Ergebnis:** Der Betrag des Vektors $\mathbf{a} = (3, 4)$ beträgt 5 Längeneinheiten.

### Beispiel 2: Berechnung des Betrags eines dreidimensionalen Vektors

Gegeben ist der Vektor:

$$
\mathbf{b} = \begin{pmatrix} 1 \\ -2 \\ 4 \end{pmatrix}
$$

**Lösung:**

1. Wir verwenden die Formel für den Betrag eines dreidimensionalen Vektors:
   $$
   |\mathbf{b}| = \sqrt{b_1^2 + b_2^2 + b_3^2}
   $$

2. Setzen wir die Werte ein:
   $$
   |\mathbf{b}| = \sqrt{1^2 + (-2)^2 + 4^2}
   $$

3. Berechnen wir die Quadrate:
   $$
   |\mathbf{b}| = \sqrt{1 + 4 + 16}
   $$

4. Addieren wir unter der Wurzel:
   $$
   |\mathbf{b}| = \sqrt{21}
   $$

5. $\sqrt{21} \approx 4{,}583$

**Ergebnis:** Der Betrag des Vektors $\mathbf{b} = \begin{pmatrix} 1 \\ -2 \\ 4 \end{pmatrix}$ ist $\sqrt{21}$ Längeneinheiten, was ungefähr 4,583 entspricht.

### Beispiel 3: Bestimmung der Koordinaten und des Winkels eines Vektors

Ein Vektor hat einen Betrag von 5 Einheiten und bildet mit der positiven x-Achse einen Winkel von $30^\circ$. Bestimmen Sie seine Koordinaten.

**Lösung:**

1. Wir verwenden die Formeln aus Satz 2.2.7:
   $$
   a_1 = |\mathbf{a}| \cdot \cos \varphi \quad \text{und} \quad a_2 = |\mathbf{a}| \cdot \sin \varphi
   $$

2. Gegeben sind:
   $$
   |\mathbf{a}| = 5 \quad \text{und} \quad \varphi = 30^\circ
   $$

3. Berechnung von $a_1$:
   $$
   a_1 = 5 \cdot \cos 30^\circ
   $$
   $$
   a_1 = 5 \cdot \frac{\sqrt{3}}{2} = \frac{5\sqrt{3}}{2}
   $$

4. Berechnung von $a_2$:
   $$
   a_2 = 5 \cdot \sin 30^\circ
   $$
   $$
   a_2 = 5 \cdot \frac{1}{2} = \frac{5}{2}
   $$

5. Der Vektor in Koordinatendarstellung lautet somit:
   $$
   \mathbf{a} = \left(\frac{5\sqrt{3}}{2}, \frac{5}{2}\right)
   $$

**Ergebnis:** Die Koordinaten des Vektors sind $\left(\frac{5\sqrt{3}}{2}, \frac{5}{2}\right)$.

- $\frac{5\sqrt{3}}{2} \approx 4{,}33$
- $\frac{5}{2} = 2{,}5$

Somit kann der Vektor auch als $\mathbf{a} \approx (4{,}33, 2{,}5)$ dargestellt werden.

### Beispiel 4: Vektoraddition und -subtraktion

Gegeben sind die Vektoren $\mathbf{a} = \begin{pmatrix} 2 \\ 1 \end{pmatrix}$ und $\mathbf{b} = \begin{pmatrix} -1 \\ 3 \end{pmatrix}$. Berechnen Sie $\mathbf{a} + \mathbf{b}$ und $\mathbf{a} - \mathbf{b}$.

**Lösung:**

1. **Vektoraddition $\mathbf{a} + \mathbf{b}$:**

   Wir addieren die entsprechenden Komponenten:
   $$
   \mathbf{a} + \mathbf{b} = \begin{pmatrix} a_1 + b_1 \\ a_2 + b_2 \end{pmatrix}
   $$
   $$
   \mathbf{a} + \mathbf{b} = \begin{pmatrix} 2 + (-1) \\ 1 + 3 \end{pmatrix}
   $$
   $$
   \mathbf{a} + \mathbf{b} = \begin{pmatrix} 1 \\ 4 \end{pmatrix}
   $$

2. **Vektorsubtraktion $\mathbf{a} - \mathbf{b}$:**

   Wir subtrahieren die entsprechenden Komponenten:
   $$
   \mathbf{a} - \mathbf{b} = \begin{pmatrix} a_1 - b_1 \\ a_2 - b_2 \end{pmatrix}
   $$
   $$
   \mathbf{a} - \mathbf{b} = \begin{pmatrix} 2 - (-1) \\ 1 - 3 \end{pmatrix}
   $$
   $$
   \mathbf{a} - \mathbf{b} = \begin{pmatrix} 2 + 1 \\ 1 - 3 \end{pmatrix}
   $$
   $$
   \mathbf{a} - \mathbf{b} = \begin{pmatrix} 3 \\ -2 \end{pmatrix}
   $$

**Ergebnis:**
$$
\mathbf{a} + \mathbf{b} = \begin{pmatrix} 1 \\ 4 \end{pmatrix}
$$
$$
\mathbf{a} - \mathbf{b} = \begin{pmatrix} 3 \\ -2 \end{pmatrix}
$$

### Beispiel 5: Skalare Multiplikation

Multiplizieren Sie den Vektor $\mathbf{c} = \begin{pmatrix} 2 \\ -1 \\ 3 \end{pmatrix}$ mit dem Skalar $\lambda = 4$.

**Lösung:**

1. Wir verwenden die Formel für die skalare Multiplikation aus Satz
   $$
   \lambda \cdot \mathbf{c} = \begin{pmatrix} \lambda c_1 \\ \lambda c_2 \\ \lambda c_3 \end{pmatrix}
   $$

2. Setzen wir die Werte ein:
   $$
   4 \cdot \begin{pmatrix} 2 \\ -1 \\ 3 \end{pmatrix}
   $$

3. Multiplizieren wir jede Komponente mit 4:
   $$
   4 \cdot \begin{pmatrix} 2 \\ -1 \\ 3 \end{pmatrix} = \begin{pmatrix} 4 \cdot 2 \\ 4 \cdot (-1) \\ 4 \cdot 3 \end{pmatrix}
   $$

4. Berechnen wir die einzelnen Komponenten:
   $$
   4 \cdot \begin{pmatrix} 2 \\ -1 \\ 3 \end{pmatrix} = \begin{pmatrix} 8 \\ -4 \\ 12 \end{pmatrix}
   $$

**Ergebnis:** 
$$
4 \cdot \mathbf{c} = \begin{pmatrix} 8 \\ -4 \\ 12 \end{pmatrix}
$$


### Beispiel 6: Kraftvektorberechnung

An einem Massenpunkt greifen zwei Kräfte an: $\mathbf{F}_1$ hat den Betrag von 2 Newton unter einem Winkel von $30^\circ$, während $\mathbf{F}_2$ den Betrag von 2 Newton unter einem Winkel von $90^\circ$ hat. Gesucht sind die Koordinatendarstellungen der Kräfte $\mathbf{F}_1$ und $\mathbf{F}_2$ sowie der resultierenden Kraft $\mathbf{F} = \mathbf{F}_1 + \mathbf{F}_2$.

**Lösung:**

1. **Berechnung von $\mathbf{F}_1$:**
   $$
   |\mathbf{F}_1| = 2, \quad \varphi_1 = 30^\circ
   $$
   Nach Satz 2.2.7 gilt:
   $$
   a_1 = |\mathbf{F}_1| \cdot \cos 30^\circ = 2 \cdot \frac{\sqrt{3}}{2} = \sqrt{3}
   $$
   $$
   b_1 = |\mathbf{F}_1| \cdot \sin 30^\circ = 2 \cdot \frac{1}{2} = 1
   $$
   Damit ist:
   $$
   \mathbf{F}_1 = \begin{pmatrix} \sqrt{3} \\ 1 \end{pmatrix}
   $$

2. **Berechnung von $\mathbf{F}_2$:**
   $$
   |\mathbf{F}_2| = 2, \quad \varphi_2 = 90^\circ
   $$
   Nach Satz 2.2.7 gilt:
   $$
   a_2 = |\mathbf{F}_2| \cdot \cos 90^\circ = 2 \cdot 0 = 0
   $$
   $$
   b_2 = |\mathbf{F}_2| \cdot \sin 90^\circ = 2 \cdot 1 = 2
   $$
   Damit ist:
   $$
   \mathbf{F}_2 = \begin{pmatrix} 0 \\ 2 \end{pmatrix}
   $$

3. **Berechnung der resultierenden Kraft $\mathbf{F}$:**
   $$
   \mathbf{F} = \mathbf{F}_1 + \mathbf{F}_2
   $$
   $$
   \mathbf{F} = \begin{pmatrix} \sqrt{3} \\ 1 \end{pmatrix} + \begin{pmatrix} 0 \\ 2 \end{pmatrix} = \begin{pmatrix} \sqrt{3} \\ 3 \end{pmatrix}
   $$

**Ergebnis:**
$$
\mathbf{F}_1 = \begin{pmatrix} \sqrt{3} \\ 1 \end{pmatrix}, \quad \mathbf{F}_2 = \begin{pmatrix} 0 \\ 2 \end{pmatrix}
$$
$$
\mathbf{F} = \begin{pmatrix} \sqrt{3} \\ 3 \end{pmatrix}
$$

### Beispiel 7: Berechnung der resultierenden Kräfte

Es sind drei Kräfte $\mathbf{F}_1$, $\mathbf{F}_2$ und $\mathbf{F}_3$ gegeben mit den Beträgen:

$$
|\mathbf{F}_1| = 2, \quad |\mathbf{F}_2| = 3, \quad |\mathbf{F}_3| = 1
$$

Die Angriffswinkel betragen $0^\circ$, $30^\circ$ und $135^\circ$.

Um die resultierende Kraft $\mathbf{F}$ zu berechnen, bestimmen wir zunächst die Koordinatendarstellungen der drei Kraftvektoren und addieren sie.

**Berechnung der Komponenten:**

1. **$\mathbf{F}_1$:**
   $$
   a_1 = |\mathbf{F}_1| \cdot \cos 0^\circ = 2 \cdot 1 = 2
   $$
   $$
   a_2 = |\mathbf{F}_1| \cdot \sin 0^\circ = 2 \cdot 0 = 0
   $$
   $$
   \mathbf{F}_1 = \begin{pmatrix} 2 \\ 0 \end{pmatrix}
   $$

2. **$\mathbf{F}_2$:**
   $$
   b_1 = |\mathbf{F}_2| \cdot \cos 30^\circ = 3 \cdot \frac{\sqrt{3}}{2} = \frac{3\sqrt{3}}{2}
   $$
   $$
   b_2 = |\mathbf{F}_2| \cdot \sin 30^\circ = 3 \cdot \frac{1}{2} = \frac{3}{2}
   $$
   $$
   \mathbf{F}_2 = \begin{pmatrix} \frac{3\sqrt{3}}{2} \\ \frac{3}{2} \end{pmatrix}
   $$

3. **$\mathbf{F}_3$:**
   $$
   c_1 = |\mathbf{F}_3| \cdot \cos 135^\circ = 1 \cdot \left( -\frac{\sqrt{2}}{2} \right) = -\frac{\sqrt{2}}{2}
   $$
   $$
   c_2 = |\mathbf{F}_3| \cdot \sin 135^\circ = 1 \cdot \frac{\sqrt{2}}{2} = \frac{\sqrt{2}}{2}
   $$
   $$
   \mathbf{F}_3 = \begin{pmatrix} -\frac{\sqrt{2}}{2} \\ \frac{\sqrt{2}}{2} \end{pmatrix}
   $$

**Summieren der Kräfte:**

$$
\mathbf{F} = \mathbf{F}_1 + \mathbf{F}_2 + \mathbf{F}_3
$$

Addieren der x-Komponenten:

$$
F_x = 2 + \frac{3\sqrt{3}}{2} - \frac{\sqrt{2}}{2}
$$

Addieren der y-Komponenten:

$$
F_y = 0 + \frac{3}{2} + \frac{\sqrt{2}}{2}
$$

**Numerische Berechnung:**

Verwenden der Näherungswerte $\sqrt{3} \approx 1{,}732$ und $\sqrt{2} \approx 1{,}414$:

$$
F_x \approx 2 + \frac{3 \cdot 1{,}732}{2} - \frac{1{,}414}{2} = 2 + 2{,}598 - 0{,}707 = 3{,}891
$$
$$
F_y \approx 0 + \frac{3}{2} + \frac{1{,}414}{2} = 1{,}5 + 0{,}707 = 2{,}207
$$

**Betrag der resultierenden Kraft:**

$$
|\mathbf{F}| = \sqrt{F_x^2 + F_y^2} = \sqrt{(3{,}891)^2 + (2{,}207)^2} = \sqrt{20{,}011} \approx 4{,}473
$$

**Winkel der resultierenden Kraft:**

$$
\cos \varphi = \frac{F_x}{|\mathbf{F}|} = \frac{3{,}891}{4{,}473} \approx 0{,}87
$$
$$
\sin \varphi = \frac{F_y}{|\mathbf{F}|} = \frac{2{,}207}{4{,}473} \approx 0{,}493
$$

Da sich die resultierende Kraft im ersten Quadranten befindet, ist der Winkel:

$$
\varphi \approx \arctan\left(\frac{2{,}207}{3{,}891}\right) \approx 29{,}54^\circ
$$

**Ergebnis:**

Die resultierende Kraft $\mathbf{F}$ hat einen Betrag von etwa 4{,}473 Newton und greift unter einem Winkel von $29{,}54^\circ$ an.

### Beispiel 8: Berechnung der fehlenden Kraft

Es greifen zwei Kräfte $\mathbf{F}_1$ und $\mathbf{F}_2$ an einem Massenpunkt an und ergeben die resultierende Kraft $\mathbf{F}$. $\mathbf{F}_1$ hat einen Betrag von 2 Newton und einen Winkel von $45^\circ$, während $\mathbf{F}$ einen Betrag von 1 Newton und einen Winkel von $180^\circ$ hat. Gesucht ist die Kraft $\mathbf{F}_2$.

Wir setzen:

$$
\mathbf{F}_1 = \begin{pmatrix} a_1 \\ a_2 \end{pmatrix}, \quad \mathbf{F}_2 = \begin{pmatrix} b_1 \\ b_2 \end{pmatrix}, \quad \mathbf{F} = \begin{pmatrix} c_1 \\ c_2 \end{pmatrix}
$$

**Berechnung der Komponenten:**

1. **$\mathbf{F}_1$:**
   $$
   a_1 = |\mathbf{F}_1| \cdot \cos 45^\circ = 2 \cdot \frac{\sqrt{2}}{2} = \sqrt{2}
   $$
   $$
   a_2 = |\mathbf{F}_1| \cdot \sin 45^\circ = 2 \cdot \frac{\sqrt{2}}{2} = \sqrt{2}
   $$
   $$
   \mathbf{F}_1 = \begin{pmatrix} \sqrt{2} \\ \sqrt{2} \end{pmatrix}
   $$

2. **$\mathbf{F}$:**
   $$
   c_1 = |\mathbf{F}| \cdot \cos 180^\circ = 1 \cdot (-1) = -1
   $$
   $$
   c_2 = |\mathbf{F}| \cdot \sin 180^\circ = 1 \cdot 0 = 0
   $$
   $$
   \mathbf{F} = \begin{pmatrix} -1 \\ 0 \end{pmatrix}
   $$

3. **Berechnung von $\mathbf{F}_2$:**
   $$
   \mathbf{F}_2 = \mathbf{F} - \mathbf{F}_1
   $$
   $$
   \mathbf{F}_2 = \begin{pmatrix} -1 \\ 0 \end{pmatrix} - \begin{pmatrix} \sqrt{2} \\ \sqrt{2} \end{pmatrix} = \begin{pmatrix} -1 - \sqrt{2} \\ 0 - \sqrt{2} \end{pmatrix}
   $$
   $$
   \mathbf{F}_2 = \begin{pmatrix} -1 - \sqrt{2} \\ -\sqrt{2} \end{pmatrix}
   $$
   Verwenden wir die Näherung $\sqrt{2} \approx 1{,}414$:
   $$
   \mathbf{F}_2 = \begin{pmatrix} -1 - 1{,}414 \\ -1{,}414 \end{pmatrix} = \begin{pmatrix} -2{,}414 \\ -1{,}414 \end{pmatrix}
   $$

**Betrag der Kraft $\mathbf{F}_2$:**
$$
|\mathbf{F}_2| = \sqrt{(-2{,}414)^2 + (-1{,}414)^2} = \sqrt{5{,}828 + 2{,}000} = \sqrt{7{,}828} \approx 2{,}798
$$

**Winkel der Kraft $\mathbf{F}_2$:**
$$
\cos \varphi = \frac{-2{,}414}{2{,}798} \approx -0{,}863, \quad \sin \varphi = \frac{-1{,}414}{2{,}798} \approx -0{,}505
$$

Der Cosinus liefert einen Winkel von $149{,}66^\circ$ und der Sinus von $-30{,}33^\circ$. Da sich die Kraft im dritten Quadranten befindet, müssen wir den Winkel korrekt anpassen:

$$
\varphi = 180^\circ + 30{,}34^\circ = 210{,}34^\circ
$$

**Ergebnis:**
$$
\mathbf{F}_2 = \begin{pmatrix} -2{,}414 \\ -1{,}414 \end{pmatrix}, \quad |\mathbf{F}_2| \approx 2{,}798, \quad \varphi \approx 210{,}34^\circ
$$



### Beispiele 9

(i) Wir nehmen wieder den Vektor $\mathbf{a} = \begin{pmatrix} 3 \\ 4 \end{pmatrix}$. Dann ist der Betrag:

$$
|\mathbf{a}| = \sqrt{3^2 + 4^2} = \sqrt{25} = 5
$$

Nach Satz 2.2.7 gilt:

$$
a_1 = |\mathbf{a}| \cdot \cos \varphi = 5 \cdot \cos \varphi
$$
und
$$
a_2 = |\mathbf{a}| \cdot \sin \varphi = 5 \cdot \sin \varphi
$$

Aus $a_1 = 3$ und $a_2 = 4$ folgt:

$$
\cos \varphi = \frac{3}{5} = 0{,}6 \quad \text{und} \quad \sin \varphi = \frac{4}{5} = 0{,}8
$$

Mit Hilfe eines Taschenrechners oder – etwas altmodischer – einer Sinustabelle kann leicht der Winkel $\varphi$ bestimmt werden, und man erhält:

$$
\varphi = 53{,}13^\circ
$$

(ii) Etwas anders sieht es bei $\mathbf{b} = \begin{pmatrix} -1 \\ 2 \end{pmatrix}$ aus. Es gilt:

$$
|\mathbf{b}| = \sqrt{(-1)^2 + 2^2} = \sqrt{5} \approx 2{,}236
$$

Für den Winkel $\varphi$ erhält man:

$$
-1 = \sqrt{5} \cdot \cos \varphi \quad \text{und} \quad 2 = \sqrt{5} \cdot \sin \varphi
$$

Also gilt:

$$
\cos \varphi = \frac{-1}{\sqrt{5}} \quad \text{und} \quad \sin \varphi = \frac{2}{\sqrt{5}}
$$

Wenn man nun für beide Gleichungen die entsprechenden inversen Funktionstasten (auch Arcus-Funktionen genannt) des Taschenrechners verwendet, wird man feststellen, dass aus der Cosinus-Gleichung folgt:

$$
\varphi = 116{,}57^\circ
$$

und aus der Sinus-Gleichung:

$$
\varphi = 63{,}43^\circ
$$

Es gibt jedoch nur einen richtigen Winkel $\varphi$. Dieses Phänomen tritt auf, weil es mehrere Winkel mit dem gleichen Sinus-Wert gibt, und der Taschenrechner üblicherweise einen passenden Wert zwischen $-90^\circ$ und $90^\circ$ auswählt. Anders gesagt: Natürlich ist:

$$
\sin 63{,}43^\circ = \frac{2}{\sqrt{5}}
$$

aber:

$$
\sin 116{,}57^\circ = \frac{2}{\sqrt{5}}
$$

stimmt ebenfalls. Beim Cosinus hingegen liegt die Bandbreite der Winkel, die der Taschenrechner auswählt, zwischen $0^\circ$ und $180^\circ$, und deshalb erhält man den richtigen Winkel $\varphi = 116{,}57^\circ$ in diesem Beispiel über den Cosinus.



