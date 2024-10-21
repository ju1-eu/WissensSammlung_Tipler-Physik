---
title: "Vektorrechnung_Skalarprodukt"
author: "Jan Unger"
date: "2024-10-19"
---

# Vektorrechnung - Skalarprodukt

Letzte Aktualisierung: 2024-10-21

Quelle: Rießinger, Thomas. Mathematik für Ingenieure: Eine anschauliche Einführung für das praxisorientierte Studium. 9. Auflage, Springer Vieweg, 2013.

## Inhaltsverzeichnis

- [Vektorrechnung - Skalarprodukt](#vektorrechnung---skalarprodukt)
  - [Inhaltsverzeichnis](#inhaltsverzeichnis)
  - [Prompt](#prompt)
  - [Definition – Skalarprodukt](#definition--skalarprodukt)
  - [Lemma – Projektion](#lemma--projektion)
  - [Satz – Rechenregeln des Skalarprodukts](#satz--rechenregeln-des-skalarprodukts)
  - [Satz – Skalarprodukt in Koordinatendarstellung](#satz--skalarprodukt-in-koordinatendarstellung)
  - [Bemerkung – Winkelbestimmung über das Skalarprodukt](#bemerkung--winkelbestimmung-über-das-skalarprodukt)
  - [Bemerkung – Quadrat eines Vektors](#bemerkung--quadrat-eines-vektors)
  - [Bemerkung – Richtungswinkel eines Vektors](#bemerkung--richtungswinkel-eines-vektors)
  - [Berechnungen](#berechnungen)
    - [Beispiel 1](#beispiel-1)
      - [Schritt 1: Bestimme das Skalarprodukt](#schritt-1-bestimme-das-skalarprodukt)
      - [Schritt 2: Berechne den Winkel](#schritt-2-berechne-den-winkel)
      - [Schritt 3: Berechne den Winkel](#schritt-3-berechne-den-winkel)
      - [Ergebnis](#ergebnis)
    - [Beispiel 2](#beispiel-2)
      - [Schritt 1: Bestimme den Verschiebungsvektor](#schritt-1-bestimme-den-verschiebungsvektor)
      - [Schritt 2: Berechne die Arbeit](#schritt-2-berechne-die-arbeit)
      - [Ergebnis:](#ergebnis-1)
    - [Beispiel 3](#beispiel-3)
      - [Schritt 1: Bestimme das Skalarprodukt](#schritt-1-bestimme-das-skalarprodukt-1)
      - [Schritt 2: Berechne die Beträge der Vektoren](#schritt-2-berechne-die-beträge-der-vektoren)
      - [Schritt 3: Bestimme den Winkel](#schritt-3-bestimme-den-winkel)
      - [Schritt 4: Berechne den Winkel](#schritt-4-berechne-den-winkel)
      - [Ergebnis:](#ergebnis-2)
    - [Beispiel 4](#beispiel-4)
      - [Schritt 1: Bestimme den Richtungsvektor](#schritt-1-bestimme-den-richtungsvektor)
      - [Schritt 2: Bestimme einen Normalenvektor](#schritt-2-bestimme-einen-normalenvektor)
      - [Schritt 3: Bestimme die Geradengleichung](#schritt-3-bestimme-die-geradengleichung)
    - [Beispiel 5](#beispiel-5)
      - [Schritt 1: Bestimme den Richtungsvektor](#schritt-1-bestimme-den-richtungsvektor-1)
      - [Schritt 2: Bestimme einen Normalenvektor](#schritt-2-bestimme-einen-normalenvektor-1)
      - [Schritt 3: Bestimme die Geradengleichung](#schritt-3-bestimme-die-geradengleichung-1)
      - [Ergebnis:](#ergebnis-3)
    - [Beispiel 6](#beispiel-6)
      - [Schritt 1: Bestimmung der Koordinaten](#schritt-1-bestimmung-der-koordinaten)
      - [Schritt 2: Berechnung der Komponenten](#schritt-2-berechnung-der-komponenten)
      - [Schritt 3: Ergebnis](#schritt-3-ergebnis)


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

## Definition – Skalarprodukt

Seien $\vec{a}$ und $\vec{b}$ Vektoren in der Ebene oder im Raum. Das Skalarprodukt $\vec{a} \cdot \vec{b}$ ist definiert als:

$$
\vec{a} \cdot \vec{b} = |\vec{a}| \cdot |\vec{b}| \cdot \cos(\varphi)
$$

wobei $\varphi$ der Winkel zwischen den Vektoren $\vec{a}$ und $\vec{b}$ ist.

---

## Lemma – Projektion

Das Skalarprodukt von $\vec{a}$ und $\vec{b}$ ist das Produkt der Länge von $\vec{a}$ und der senkrechten Projektion $\vec{b}_{\vec{a}}$ von $\vec{b}$ auf $\vec{a}$.

- $\vec{a} \cdot \vec{b} = |\vec{a}| \cdot |\vec{b}_{\vec{a}}|$, falls $\vec{b}_{\vec{a}} \uparrow \uparrow \vec{a}$
- $\vec{a} \cdot \vec{b} = -|\vec{a}| \cdot |\vec{b}_{\vec{a}}|$, falls $\vec{b}_{\vec{a}} \uparrow \downarrow \vec{a}$

---

## Satz – Rechenregeln des Skalarprodukts

Für Vektoren $\vec{a}, \vec{b}, \vec{c}$ und $\lambda \in \mathbb{R}$ gelten folgende Regeln:

- (i) $(\lambda \cdot \vec{a}) \cdot \vec{b} = \lambda \cdot (\vec{a} \cdot \vec{b})$
- (ii) $\vec{a} \cdot \vec{b} = \vec{b} \cdot \vec{a}$ (Kommutativgesetz)
- (iii) $\vec{a} \cdot (\vec{b} + \vec{c}) = \vec{a} \cdot \vec{b} + \vec{a} \cdot \vec{c}$ (Distributivgesetz)

---

## Satz – Skalarprodukt in Koordinatendarstellung

(i) Für $\vec{a} = (a_1, a_2)$ und $\vec{b} = (b_1, b_2)$ gilt:

$$
\vec{a} \cdot \vec{b} = a_1 \cdot b_1 + a_2 \cdot b_2
$$

(ii) Für $\vec{a} = \begin{pmatrix} a_1 \\ a_2 \\ a_3 \end{pmatrix}$ und $\vec{b} = \begin{pmatrix} b_1 \\ b_2 \\ b_3 \end{pmatrix}$ gilt:

$$
\vec{a} \cdot \vec{b} = a_1 \cdot b_1 + a_2 \cdot b_2 + a_3 \cdot b_3
$$

---

## Bemerkung – Winkelbestimmung über das Skalarprodukt

Für zwei Vektoren $\vec{a}, \vec{b}$ und ihren eingeschlossenen Winkel $\varphi$ gilt:

$$
\cos(\varphi) = \frac{\vec{a} \cdot \vec{b}}{|\vec{a}| \cdot |\vec{b}|}
$$

Sind die Koordinaten von $\vec{a}$ und $\vec{b}$ bekannt, kann man das Skalarprodukt und die Beträge berechnen, um den eingeschlossenen Winkel $\varphi$ zu bestimmen.

---

## Bemerkung – Quadrat eines Vektors

(i) Es gilt:

$$
\vec{a}^2 = |\vec{a}|^2
$$

Das Quadrat eines Vektors entspricht dem Quadrat seiner Länge.

(ii) Die Regeln über das Skalarprodukt ermöglichen eine schnelle Herleitung des Cosinussatzes:

$$
|\vec{c}|^2 = |\vec{a}|^2 - 2 \cdot |\vec{a}| \cdot |\vec{b}| \cdot \cos(\varphi) + |\vec{b}|^2
$$

---

## Bemerkung – Richtungswinkel eines Vektors

Die Richtung eines Vektors $\vec{a} = \begin{pmatrix} a_1 \\ a_2 \\ a_3 \end{pmatrix}$ im Raum wird durch die Winkel $\varphi_1, \varphi_2, \varphi_3$ mit den Einheitsvektoren $\vec{e_1}, \vec{e_2}, \vec{e_3}$ festgelegt:

$$
\cos(\varphi_1) = \frac{a_1}{|\vec{a}|}, \quad \cos(\varphi_2) = \frac{a_2}{|\vec{a}|}, \quad \cos(\varphi_3) = \frac{a_3}{|\vec{a}|}
$$

## Berechnungen

### Beispiel 1

Gegeben sind die Vektoren $\vec{a} = \begin{pmatrix} \sqrt{3} \\ 1 \end{pmatrix}$ und $\vec{b} = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$.

#### Schritt 1: Bestimme das Skalarprodukt

Das Skalarprodukt zweier Vektoren in der Ebene lautet:

$$
\vec{a} \cdot \vec{b} = a_1 \cdot b_1 + a_2 \cdot b_2
$$

Setze die Komponenten der Vektoren $\vec{a}$ und $\vec{b}$ ein:

$$
\vec{a} \cdot \vec{b} = \sqrt{3} \cdot 0 + 1 \cdot 1 = 0 + 1 = 1
$$

#### Schritt 2: Berechne den Winkel 

zwischen $\vec{a}$ und $\vec{b}$

Das Skalarprodukt ist auch gegeben durch:

$$
\vec{a} \cdot \vec{b} = |\vec{a}| \cdot |\vec{b}| \cdot \cos(\varphi)
$$

Um den Winkel $\varphi$ zu bestimmen, müssen wir zunächst die Beträge der Vektoren berechnen:

- Betrag von $\vec{a}$:

$$
|\vec{a}| = \sqrt{(\sqrt{3})^2 + 1^2} = \sqrt{3 + 1} = \sqrt{4} = 2
$$

- Betrag von $\vec{b}$:

$$
|\vec{b}| = \sqrt{0^2 + 1^2} = \sqrt{1} = 1
$$

Nun setzen wir in die Gleichung für das Skalarprodukt ein:

$$
1 = 2 \cdot 1 \cdot \cos(\varphi)
$$

Daraus folgt:

$$
\cos(\varphi) = \frac{1}{2}
$$

#### Schritt 3: Berechne den Winkel 

$\varphi$

Der Winkel $\varphi$ ist:

$$
\varphi = \cos^{-1}\left( \frac{1}{2} \right) = 60^\circ
$$

#### Ergebnis
Das Skalarprodukt beträgt 1, und der Winkel zwischen den Vektoren $\vec{a}$ und $\vec{b}$ ist $60^\circ$.

### Beispiel 2

Gegeben ist eine konstante Kraft $\vec{F} = \begin{pmatrix} 1 \, \text{N} \\ 2 \, \text{N} \\ 3 \, \text{N} \end{pmatrix}$, die einen Massenpunkt vom Punkt $P_1 = \begin{pmatrix} -2 \, \text{m} \\ 1 \, \text{m} \\ 3 \, \text{m} \end{pmatrix}$ zum Punkt $P_2 = \begin{pmatrix} -1 \, \text{m} \\ 2 \, \text{m} \\ 5 \, \text{m} \end{pmatrix}$ verschiebt.

#### Schritt 1: Bestimme den Verschiebungsvektor 

$\vec{s}$

Der Verschiebungsvektor $\vec{s}$ ist die Differenz zwischen den Ortsvektoren der Punkte $P_2$ und $P_1$:

$$
\vec{s} = \vec{P_2} - \vec{P_1} = \begin{pmatrix} -1 \\ 2 \\ 5 \end{pmatrix} - \begin{pmatrix} -2 \\ 1 \\ 3 \end{pmatrix} = \begin{pmatrix} -1 + 2 \\ 2 - 1 \\ 5 - 3 \end{pmatrix} = \begin{pmatrix} 1 \, \text{m} \\ 1 \, \text{m} \\ 2 \, \text{m} \end{pmatrix}
$$

#### Schritt 2: Berechne die Arbeit 

$A$

Die Arbeit wird durch das Skalarprodukt von Kraft $\vec{F}$ und Weg $\vec{s}$ berechnet:

$$
A = \vec{F} \cdot \vec{s} = F_1 \cdot s_1 + F_2 \cdot s_2 + F_3 \cdot s_3
$$

Setze die Werte ein:

$$
A = 1 \cdot 1 + 2 \cdot 1 + 3 \cdot 2 = 1 + 2 + 6 = 9 \, \text{Nm}
$$

#### Ergebnis:
Die verrichtete Arbeit beträgt 9 Joule.

---

### Beispiel 3

Gegeben sind die Vektoren $\vec{a} = \begin{pmatrix} -1 \\ 0 \\ 2 \end{pmatrix}$ und $\vec{b} = \begin{pmatrix} 3 \\ 1 \\ 4 \end{pmatrix}$. Der Winkel $\varphi$ zwischen den Vektoren soll berechnet werden.

#### Schritt 1: Bestimme das Skalarprodukt 

$\vec{a} \cdot \vec{b}$

Das Skalarprodukt zweier Vektoren im Raum lautet:

$$
\vec{a} \cdot \vec{b} = a_1 \cdot b_1 + a_2 \cdot b_2 + a_3 \cdot b_3
$$

Setze die Komponenten der Vektoren ein:

$$
\vec{a} \cdot \vec{b} = (-1) \cdot 3 + 0 \cdot 1 + 2 \cdot 4 = -3 + 0 + 8 = 5
$$

#### Schritt 2: Berechne die Beträge der Vektoren 

$\vec{a}$ und $\vec{b}$

- Betrag von $\vec{a}$:

$$
|\vec{a}| = \sqrt{(-1)^2 + 0^2 + 2^2} = \sqrt{1 + 0 + 4} = \sqrt{5}
$$

- Betrag von $\vec{b}$:

$$
|\vec{b}| = \sqrt{3^2 + 1^2 + 4^2} = \sqrt{9 + 1 + 16} = \sqrt{26}
$$

#### Schritt 3: Bestimme den Winkel 

$\varphi$

Das Skalarprodukt ist auch gegeben durch:

$$
\vec{a} \cdot \vec{b} = |\vec{a}| \cdot |\vec{b}| \cdot \cos(\varphi)
$$

Setze die bekannten Werte ein:

$$
5 = \sqrt{5} \cdot \sqrt{26} \cdot \cos(\varphi)
$$

Daraus folgt:

$$
\cos(\varphi) = \frac{5}{\sqrt{5} \cdot \sqrt{26}} = \frac{5}{\sqrt{130}}
$$

Berechne den Wert von $\cos(\varphi)$:

$$
\cos(\varphi) \approx \frac{5}{11.401} \approx 0.439
$$

#### Schritt 4: Berechne den Winkel 

$\varphi$

Der Winkel $\varphi$ ist:

$$
\varphi = \cos^{-1}(0.439) \approx 63.99^\circ
$$

#### Ergebnis:
Der Winkel zwischen den Vektoren $\vec{a}$ und $\vec{b}$ beträgt ungefähr $63.99^\circ$.


### Beispiel 4

Gesucht ist die Gleichung einer Geraden in der Ebene, die durch zwei Punkte $A$ und $B$ verläuft.

#### Schritt 1: Bestimme den Richtungsvektor

Die Geradengleichung kann mit Hilfe eines Richtungsvektors, der durch zwei Punkte $A$ und $B$ bestimmt wird, beschrieben werden. Sei $a$ der Ortsvektor von Punkt $A$ und $b$ der Ortsvektor von Punkt $B$. Der Richtungsvektor $\vec{AB}$ ergibt sich aus der Differenz der Ortsvektoren:

$$
\vec{AB} = b - a
$$

#### Schritt 2: Bestimme einen Normalenvektor

Ein Normalenvektor $m$, der senkrecht auf der Geraden steht, kann bestimmt werden, indem die Komponenten des Richtungsvektors $\vec{AB}$ so vertauscht werden, dass das Skalarprodukt von $m$ und $\vec{AB}$ gleich null ist. Sei $\vec{AB} = \begin{pmatrix} b_1 - a_1 \\ b_2 - a_2 \end{pmatrix}$, dann ist ein möglicher Normalenvektor:

$$
m = \begin{pmatrix} -(b_2 - a_2) \\ b_1 - a_1 \end{pmatrix}
$$

#### Schritt 3: Bestimme die Geradengleichung

Die allgemeine Gleichung einer Geraden in der Ebene lautet:

$$
m \cdot (z - a) = 0
$$

Dabei ist $z = \begin{pmatrix} x \\ y \end{pmatrix}$ ein beliebiger Punkt auf der Geraden und $m$ der Normalenvektor. Setze $m$ und $a$ in die Gleichung ein:

$$
m_1 \cdot (x - a_1) + m_2 \cdot (y - a_2) = 0
$$

Diese Gleichung stellt die gesuchte Geradengleichung in impliziter Form dar.

---

### Beispiel 5

Gesucht ist die Gleichung der Geraden, die durch die Punkte $A = (1, 1)$ und $B = (2, 3)$ verläuft.

#### Schritt 1: Bestimme den Richtungsvektor

Der Richtungsvektor $\vec{AB}$ ergibt sich aus der Differenz der Koordinaten von $B$ und $A$:

$$
\vec{AB} = \begin{pmatrix} 2 - 1 \\ 3 - 1 \end{pmatrix} = \begin{pmatrix} 1 \\ 2 \end{pmatrix}
$$

#### Schritt 2: Bestimme einen Normalenvektor

Ein Normalenvektor $m$, der senkrecht auf $\vec{AB}$ steht, ist:

$$
m = \begin{pmatrix} -2 \\ 1 \end{pmatrix}
$$

#### Schritt 3: Bestimme die Geradengleichung

Die Geradengleichung lautet:

$$
m_1 \cdot (x - a_1) + m_2 \cdot (y - a_2) = 0
$$

Setze $m = \begin{pmatrix} -2 \\ 1 \end{pmatrix}$ und $a = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$ ein:

$$
-2 \cdot (x - 1) + 1 \cdot (y - 1) = 0
$$

Multipliziere die Terme aus:

$$
-2x + 2 + y - 1 = 0
$$

$$
-2x + y + 1 = 0
$$

Bringe die Gleichung in die Form $y = mx + b$:

$$
y = 2x - 1
$$

#### Ergebnis:
Die Gleichung der Geraden, die durch die Punkte $A(1, 1)$ und $B(2, 3)$ verläuft, lautet:

$$
y = 2x - 1
$$

### Beispiel 6

Gesucht ist der Vektor $\vec{a}$, der mit der x-Achse einen Winkel von $60^\circ$, mit der y-Achse einen Winkel von $45^\circ$ und mit der z-Achse ebenfalls einen Winkel von $60^\circ$ bildet. Der Betrag des Vektors $\vec{a}$ beträgt $|a| = 4$.

#### Schritt 1: Bestimmung der Koordinaten

Die Koordinaten des Vektors $\vec{a}$ lassen sich berechnen, indem man die Länge des Vektors mit den Cosinuswerten der Richtungswinkel multipliziert. Die Richtungswinkel sind $\varphi_1 = 60^\circ$ zur x-Achse, $\varphi_2 = 45^\circ$ zur y-Achse und $\varphi_3 = 60^\circ$ zur z-Achse.

Die Komponenten des Vektors sind wie folgt definiert:

- $a_1 = |a| \cdot \cos(\varphi_1)$
- $a_2 = |a| \cdot \cos(\varphi_2)$
- $a_3 = |a| \cdot \cos(\varphi_3)$

#### Schritt 2: Berechnung der Komponenten

1. Berechnung von $a_1$:

$$
a_1 = 4 \cdot \cos(60^\circ) = 4 \cdot \frac{1}{2} = 2
$$

2. Berechnung von $a_2$:

$$
a_2 = 4 \cdot \cos(45^\circ) = 4 \cdot \frac{\sqrt{2}}{2} = 2\sqrt{2}
$$

3. Berechnung von $a_3$:

$$
a_3 = 4 \cdot \cos(60^\circ) = 4 \cdot \frac{1}{2} = 2
$$

#### Schritt 3: Ergebnis

Der Vektor $\vec{a}$ hat also die Koordinaten:

$$
\vec{a} = \begin{pmatrix} 2 \\ 2\sqrt{2} \\ 2 \end{pmatrix}
$$