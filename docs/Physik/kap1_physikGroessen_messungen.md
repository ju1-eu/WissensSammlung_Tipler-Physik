---
title: "Physikalische Größen und Messungen"
author: "Jan Unger"
date: "2024-10-19"
---

# Physikalische Größen und Messungen

Letzte Aktualisierung: 2024-10-19

Quelle: Tipler/Mosca Physik. 9. Aufl., 2024

## Inhaltsverzeichnis

- [Physikalische Größen und Messungen](#physikalische-größen-und-messungen)
  - [Inhaltsverzeichnis](#inhaltsverzeichnis)
- [Zusammenfassung: Physikalische Größen und Messungen](#zusammenfassung-physikalische-größen-und-messungen)
- [Erklärungen zu Tabellen und Diagrammen](#erklärungen-zu-tabellen-und-diagrammen)
  - [Maßeinheiten](#maßeinheiten)
  - [Dimensionen physikalischer Größen](#dimensionen-physikalischer-größen)
  - [Signifikante Stellen und Größenordnungen](#signifikante-stellen-und-größenordnungen)
    - [Größenordnungen im Universum](#größenordnungen-im-universum)
  - [internationale Einheitensystem (SI)](#internationale-einheitensystem-si)
    - [SI-Grundeinheiten:](#si-grundeinheiten)
    - [Änderungen im Jahr 2018:](#änderungen-im-jahr-2018)
    - [Historische Entwicklung der Definitionen:](#historische-entwicklung-der-definitionen)
    - [Konstanten](#konstanten)
  - [Messgenauigkeit und Messfehler](#messgenauigkeit-und-messfehler)
    - [Abbildung 1.5: Verteilung von Klausurergebnissen](#abbildung-15-verteilung-von-klausurergebnissen)
    - [Abbildung 1.7: Gauß-Verteilung](#abbildung-17-gauß-verteilung)
- [Fachwörter](#fachwörter)
- [Visualisierung der Zusammenhänge](#visualisierung-der-zusammenhänge)
- [Notizen: Physikalische Größen und Messungen](#notizen-physikalische-größen-und-messungen)
  - [Vom Wesen der Physik](#vom-wesen-der-physik)
    - [Lernziel](#lernziel)
    - [Notizen](#notizen)
    - [Beispiele](#beispiele)
  - [Maßeinheiten](#maßeinheiten-1)
    - [Lernziel](#lernziel-1)
    - [Notizen](#notizen-1)
    - [Beispiele](#beispiele-1)
  - [Dimensionen physikalischer Größen](#dimensionen-physikalischer-größen-1)
    - [Lernziel](#lernziel-2)
    - [Notizen](#notizen-2)
  - [Signifikante Stellen und Größenordnungen](#signifikante-stellen-und-größenordnungen-1)
    - [Lernziel](#lernziel-3)
    - [Notizen](#notizen-3)
  - [Messgenauigkeit und Messfehler](#messgenauigkeit-und-messfehler-1)
    - [Lernziel](#lernziel-4)
    - [Notizen](#notizen-4)
    - [Rechenbeispielen](#rechenbeispielen)
- [Regeln für Berechnungen in Exponentialschreibweise](#regeln-für-berechnungen-in-exponentialschreibweise)
- [Zusammenfassung](#zusammenfassung)


# Zusammenfassung: Physikalische Größen und Messungen

1. Maßeinheiten
   - Physikalische Größen sind durch Messungen erhaltene Zahlenwerte
   - Wert einer physikalischen Größe = Maßzahl × Maßeinheit

2. Grundeinheiten des SI-Systems
   - Meter (m), Sekunde (s), Kilogramm (kg), Kelvin (K), Ampere (A), Mol (mol), Candela (cd)
   - Alle physikalischen Größen lassen sich durch diese Grundeinheiten ausdrücken

3. Gleichungen
   - Einheiten in Gleichungen werden wie algebraische Größen behandelt
   - Dimensionen auf beiden Seiten einer Gleichung müssen übereinstimmen

4. Signifikante Stellen
   - Bei Multiplikation/Division: Ergebnis hat nie mehr signifikante Stellen als der Faktor mit den wenigsten
   - Bei Addition/Subtraktion: Ergebnis hat so viele Dezimalstellen wie der Term mit den wenigsten

5. Umrechnung
   - Umrechnungsfaktoren haben stets den Wert 1
   - Ermöglichen einfache Umrechnung zwischen Einheiten

6. Exponentialschreibweise
   - Für sehr kleine/große Zahlen: Darstellung als Produkt einer Zahl und einer Zehnerpotenz

7. Exponenten
   - Multiplikation: Exponenten werden addiert
   - Division: Exponenten werden subtrahiert
   - Potenzierung: Exponenten werden multipliziert

8. Größenordnungen
   - Rundung auf nächstgelegene Zehnerpotenz
   - Ermöglicht schnelle Abschätzungen und einfache Berechnungen

9. Messfehler
   - Gauß'sche Verteilungsfunktion: $$f(x) = \frac{1}{\sqrt{2\pi\sigma}}e^{-(x-\langle x\rangle)^2/(2\sigma^2)}$$
   - Mittelwert (Schätzwert für wahren Messwert): $$\langle x\rangle = \frac{1}{n}\sum_{i=1}^n x_i$$
   - Standardabweichung einer Einzelmessung: $$\sigma = \sqrt{\langle x^2\rangle - \langle x\rangle^2} = \sqrt{\frac{1}{n-1}\sum_{i=1}^n (x_i - \langle x\rangle)^2}$$
   - Standardabweichung des Mittelwerts: $$\Delta x = \frac{\sigma}{\sqrt{n}} = \sqrt{\frac{1}{n(n-1)}\sum_{i=1}^n (x_i - \langle x\rangle)^2}$$


# Erklärungen zu Tabellen und Diagrammen

## Maßeinheiten

Tabelle: Vorsätze für Zehnerpotenzen

| Vielfaches | Vorsatz | Abkürzung |
| ---------- | ------- | --------- |
| $10^{18}$  | Exa     | E         |
| $10^{15}$  | Peta    | P         |
| $10^{12}$  | Tera    | T         |
| $10^9$     | Giga    | G         |
| $10^6$     | Mega    | M         |
| $10^3$     | Kilo    | k         |
| $10^2$     | Hekto   | h         |
| $10^1$     | Deka    | da        |
| $10^{-1}$  | Dezi    | d         |
| $10^{-2}$  | Zenti   | c         |
| $10^{-3}$  | Milli   | m         |
| $10^{-6}$  | Mikro   | $\mu$     |
| $10^{-9}$  | Nano    | n         |
| $10^{-12}$ | Piko    | p         |
| $10^{-15}$ | Femto   | f         |
| $10^{-18}$ | Atto    | a         |

> Hinweis: Die Vorsätze Hekto (h), Deka (da) und Dezi (d) sind keine Potenzen von $10^3$ oder $10^{-3}$ und werden selten verwendet. Eine Ausnahme bildet Zenti (c), das bei der Längeneinheit (1 cm = $10^{-2}$ m) üblich ist. Beachte, dass die Abkürzungen für Vorsätze ab $10^6$ großgeschrieben werden, alle anderen hingegen kleingeschrieben.

## Dimensionen physikalischer Größen

Tabelle: Dimensionen und SI-Einheiten einiger physikalischer Größen aus der Mechanik


| Größe               | Dimension               | SI-Einheit                              |
| ------------------- | ----------------------- | --------------------------------------- |
| Flächeninhalt $A$   | $L^2$                   | $\text{m}^2$                            |
| Volumen $V$         | $L^3$                   | $\text{m}^3$                            |
| Geschwindigkeit $v$ | $L/T$                   | $\text{m/s}$                            |
| Beschleunigung $a$  | $L/T^2$                 | $\text{m/s}^2$                          |
| Kraft $F$           | $M \cdot L/T^2$         | $\text{kg} \cdot \text{m/s}^2$          |
| Druck $p$           | $F/A = M/(L \cdot T^2)$ | $\text{kg}/(\text{m} \cdot \text{s}^2)$ |
| Dichte $\rho$       | $m/V = M/L^3$           | $\text{kg/m}^3$                         |
| Energie $E$         | $M \cdot L^2/T^2$       | $\text{kg} \cdot \text{m}^2/\text{s}^2$ |


## Signifikante Stellen und Größenordnungen

### Größenordnungen im Universum

Typische Größenordnungen für Längen, Massen und Zeitintervalle im Universum. Beispiele:

Tabelle: Größenordnungen im Universum

| Länge oder Größe (m)       | Wert       |
| -------------------------- | ---------- |
| Protonradius               | $10^{-15}$ |
| Atomradius                 | $10^{-10}$ |
| Virus                      | $10^{-7}$  |
| Riesenamöbe                | $10^{-4}$  |
| Walnuss                    | $10^{-2}$  |
| Mensch                     | $10^{0}$   |
| Höchster Berg              | $10^{4}$   |
| Erde                       | $10^{7}$   |
| Sonne                      | $10^{9}$   |
| Abstand Erde–Sonne         | $10^{11}$  |
| Sonnensystem               | $10^{13}$  |
| Abstand zum nächsten Stern | $10^{16}$  |
| Milchstraße/Galaxis        | $10^{21}$  |
| Sichtbares Universum       | $10^{26}$  |


| Masse (kg)          | Wert       |
| ------------------- | ---------- |
| Elektron            | $10^{-30}$ |
| Proton              | $10^{-27}$ |
| Aminosäure          | $10^{-25}$ |
| Hämoglobin          | $10^{-22}$ |
| Grippevirus         | $10^{-19}$ |
| Riesenamöbe         | $10^{-8}$  |
| Regentropfen        | $10^{-6}$  |
| Ameise              | $10^{-2}$  |
| Mensch              | $10^{2}$   |
| Saturn-V-Rakete     | $10^{6}$   |
| Pyramide            | $10^{10}$  |
| Erde                | $10^{24}$  |
| Sonne               | $10^{30}$  |
| Milchstraße/Galaxis | $10^{41}$  |
| Universum           | $10^{52}$  |


| Zeitintervall (s)                                  | Wert       |
| -------------------------------------------------- | ---------- |
| Licht durchquert den Atomkern                      | $10^{-23}$ |
| Schwingungsperiode des sichtbaren Lichts           | $10^{-15}$ |
| Schwingungsperiode von Mikrowellenstrahlung        | $10^{-10}$ |
| Halbwertszeit eines Myons                          | $10^{-6}$  |
| Schwingungsperiode der höchsten noch hörbaren Töne | $10^{-4}$  |
| Periode des menschlichen Herzschlags               | $10^{0}$   |
| Halbwertszeit freier Neutronen                     | $10^{3}$   |
| Umdrehungszeit der Erdrotation                     | $10^{5}$   |
| Umlaufzeit der Erde um die Sonne                   | $10^{7}$   |
| Lebensdauer eines Menschen                         | $10^{9}$   |
| Halbwertszeit von Plutonium-239                    | $10^{12}$  |
| Lebenszeit eines Gebirges                          | $10^{15}$  |
| Alter der Erde                                     | $10^{17}$  |
| Alter des Universums                               | $10^{18}$  |



## internationale Einheitensystem (SI)

Das internationale Einheitensystem (SI) ist ein unverzichtbarer Standard in der Physik, um Messungen weltweit einheitlich zu machen.

### SI-Grundeinheiten:

- **Länge (Meter, m):** Heute definiert als die Strecke, die Licht im Vakuum in $1/299,792,458$ Sekunden zurücklegt.
- **Masse (Kilogramm, kg):** Früher durch das Urkilogramm, heute über die Planck-Konstante $h = 6.62607015 \times 10^{-34}$ J s definiert.
- **Zeit (Sekunde, s):** Basierend auf der Schwingungsdauer eines Energieübergangs im Cäsium-133-Atom.
- **Elektrischer Strom (Ampere, A):** Definiert über die elementare Ladung $e = 1.602176634 \times 10^{-19}$ C.
- **Temperatur (Kelvin, K):** Bezogen auf die Boltzmann-Konstante $k = 1.380649 \times 10^{-23}$ J/K.
- **Stoffmenge (Mol, mol):** Definiert über die Avogadro-Konstante $N_A = 6.02214076 \times 10^{23}$ mol⁻¹.
- **Lichtstärke (Candela, cd):** Festgelegt über das photometrische Strahlungsäquivalent $K_{cd} = 683$ lm/W.

### Änderungen im Jahr 2018:

Die Neudefinition der SI-Einheiten basiert auf sieben Naturkonstanten, was zu noch präziseren Standards geführt hat. Die Änderungen betreffen vor allem das Kilogramm, das nun nicht mehr auf einem physischen Objekt (dem Urkilogramm) basiert, sondern auf der Planck-Konstante.

Die Masse wird nun unter anderem mit Verfahren wie der **Wattwaage** oder den **Siliciumkugeln** (Avogadro-Projekt) ermittelt.

### Historische Entwicklung der Definitionen:

- **Länge:** Vom Meridianabschnitt durch Paris über einen Platin-Iridium-Stab hin zur aktuellen Definition über die Lichtgeschwindigkeit.
- **Masse:** Vom Wasser-Liter hin zum Urkilogramm und schließlich zur heutigen Planck-Konstanten-Definition.
- **Zeit:** Von der Rotation der Erde hin zur heutigen Definition über die Cäsium-Atom-Uhr.

Diese neuen Definitionen stellen sicher, dass Messungen weltweit konsistent und unabhängig von physischen Prototypen sind.

### Konstanten

Tab. Festgelegte Werte der ausgewählten Konstanten

| Konstante                                                       | Symbol   | Wert                                                                                                                                                                |
| --------------------------------------------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Frequenz des Hyper. des Grundzustands im $^{133}\text{Cs}$-Atom | $D$      | $9\,192\,631\,770 \, \text{s}^{-1}$                                                                                                                                 |
| Lichtgeschwindigkeit im Vakuum                                  | $c$      | $299\,792\,458 \, \text{m/s}$                                                                                                                                       |
| Planck’sches Wirkungsquantum                                    | $h$      | $6.626\,070\,15 \times 10^{-34} \, \text{J} \cdot \text{s} \, (\text{J} \cdot \text{s} = \text{kg} \cdot \text{m}^2 \cdot \text{s}^{-1})$                           |
| Elementarladung                                                 | $e$      | $1.602\,176\,634 \times 10^{-19} \, \text{C} \, (\text{C} = \text{A} \cdot \text{s})$                                                                               |
| Boltzmann-Konstante                                             | $k$      | $1.380\,649 \times 10^{-23} \, \text{J} \cdot \text{K}^{-1} \, (\text{J} \cdot \text{K}^{-1} = \text{kg} \cdot \text{m}^2 \cdot \text{s}^{-2} \cdot \text{K}^{-1})$ |
| Avogadro-Konstante                                              | $N_A$    | $6.022\,140\,76 \times 10^{23} \, \text{mol}^{-1}$                                                                                                                  |
| Photometrisches Strahlungsäquivalent                            | $K_{cd}$ | $683 \, \text{lm/W} \, \text{(Strahlung der Frequenz } 540 \times 10^{12} \, \text{Hz)}$                                                                            |



## Messgenauigkeit und Messfehler

### Abbildung 1.5: Verteilung von Klausurergebnissen

Dieses Diagramm zeigt:

- X-Achse: Erzielte Punkte in einer Klausur (0-25)
- Y-Achse links: Anzahl der Studierenden $n_i$ mit dem jeweiligen Ergebnis
- Y-Achse rechts: Anteil $f_i$ der Studierenden mit dem jeweiligen Ergebnis

Wichtige Kennwerte:

- Mittelwert: $\langle s \rangle = 14,2$
- Quadratisch gemitteltes Ergebnis: $s_{rms} = \sqrt{\langle s^2 \rangle} = 14,9$

Diese Darstellung veranschaulicht die statistische Verteilung von Messwerten und wichtige statistische Größen.

### Abbildung 1.7: Gauß-Verteilung

Diese Abbildung zeigt die charakteristische Glockenkurve der Gauß-Verteilung:

$$f(h) = \frac{1}{\sigma\sqrt{2\pi}} e^{-(h-\langle h \rangle)^2/(2\sigma^2)}$$

- X-Achse: Abweichung vom Mittelwert $(h - \langle h \rangle)$
- Y-Achse: Wahrscheinlichkeitsdichte $f(h)$

Die Gauß-Verteilung ist fundamental für die Beschreibung zufälliger Messfehler und statistischer Schwankungen in der Physik.

# Fachwörter

1. Physikalische Größe:
   Eine messbare Eigenschaft eines physikalischen Systems, die durch einen Zahlenwert und eine Einheit ausgedrückt wird.

2. SI-Einheiten (Système International d'Unités):
   Das international vereinbarte Einheitensystem, das sieben Basiseinheiten definiert.

3. Dimension:
   Die qualitative Beschreibung einer physikalischen Größe, unabhängig von spezifischen Einheiten (z.B. Länge, Zeit, Masse).

4. Signifikante Stellen:
   Die Anzahl der Ziffern in einem Messwert, die als zuverlässig betrachtet werden.

5. Exponentialschreibweise:
   Eine Darstellungsform für sehr große oder kleine Zahlen als Produkt einer Zahl zwischen 1 und 10 und einer Zehnerpotenz.

6. Größenordnung:
   Eine ungefähre Angabe der Größe eines Wertes, meist als nächstgelegene Zehnerpotenz.

7. Systematischer Fehler:
   Ein konstanter oder proportionaler Fehler, der bei wiederholten Messungen in gleicher Weise auftritt.

8. Zufälliger Fehler:
   Statistische Schwankungen in Messwerten, die auf unkontrollierbare Einflüsse zurückzuführen sind.

9. Gauß'sche Verteilung:
   Eine symmetrische, glockenförmige Wahrscheinlichkeitsverteilung, die häufig zur Beschreibung von Messfehlern verwendet wird.

10. Mittelwert:
    Der Durchschnittswert einer Reihe von Messungen, berechnet durch die Summe aller Werte geteilt durch ihre Anzahl.

11. Standardabweichung:
    Ein Maß für die Streuung der Messwerte um den Mittelwert.

12. Fehlerfortpflanzung:
    Die Berechnung des Gesamtfehlers eines Ergebnisses, das aus mehreren fehlerbehafteten Messgrößen berechnet wird.

13. Dimensionsanalyse:
    Eine Methode zur Überprüfung der Konsistenz von Gleichungen durch Vergleich der Dimensionen auf beiden Seiten.

14. Operationale Definition:
    Eine Definition, die eine physikalische Größe durch die Beschreibung ihrer Messmethode charakterisiert.

15. Signifikanz:
    Die statistische Bedeutsamkeit eines Messergebnisses, oft im Zusammenhang mit der Abweichung vom Erwartungswert.

Diese Fachbegriffe bilden das Grundvokabular für das Verständnis und die Diskussion von physikalischen Messungen und deren Analyse.

# Visualisierung der Zusammenhänge

```mermaid
graph TD
    A[Physikalische Größe] --> B[Messung]
    A --> C[Einheiten]
    C --> D[SI-Einheiten]
    C --> E[Dimension]
    
    B --> F[Messwert]
    F --> G[Signifikante Stellen]
    F --> H[Exponentialschreibweise]
    F --> I[Größenordnung]
    
    B --> J[Messfehler]
    J --> K[Systematischer Fehler]
    J --> L[Zufälliger Fehler]
    
    L --> M[Statistische Analyse]
    M --> N[Gauß'sche Verteilung]
    M --> O[Mittelwert]
    M --> P[Standardabweichung]
    
    Q[Fehlerfortpflanzung] --> J
    Q --> R[Dimensionsanalyse]
    
    S[Operationale Definition] --> A
    
    T[Signifikanz] --> M
```

![Visualisierung](images/visualisierung.png)


Diese Visualisierung zeigt:

1. Physikalische Größen sind der Ausgangspunkt, definiert durch Messungen und ausgedrückt in Einheiten.
2. Einheiten werden durch SI-Einheiten standardisiert und haben Dimensionen.
3. Messwerte werden durch signifikante Stellen, Exponentialschreibweise und Größenordnungen charakterisiert.
4. Messfehler unterteilen sich in systematische und zufällige Fehler.
5. Zufällige Fehler werden durch statistische Analyse behandelt, einschließlich Gauß'scher Verteilung, Mittelwert und Standardabweichung.
6. Fehlerfortpflanzung und Dimensionsanalyse sind wichtige Werkzeuge zur Fehlerbehandlung und Konsistenzprüfung.
7. Operationale Definitionen sind grundlegend für die Definition physikalischer Größen.
8. Signifikanz ist ein wichtiges Konzept in der statistischen Analyse von Messergebnissen.

Diese Darstellung verdeutlicht die Vernetzung der verschiedenen Konzepte in der Messtechnik und Datenanalyse in der Physik.

# Notizen: Physikalische Größen und Messungen

## Vom Wesen der Physik

### Lernziel

Verstehen der grundlegenden Herangehensweise der Physik zur Beschreibung und Erklärung der Realität.

### Notizen

- Physik: Wissenschaftliche Beschreibung und Erklärung der Grundgesetze des Universums
- Methodik: Beobachtung, Hypothesenbildung, Experimente, Theorieentwicklung
- Klassische Physik: Mechanik, Licht, Wärme, Schall, Elektrizität, Magnetismus
- Moderne Physik: Relativitätstheorie, Quantenmechanik
- Bedeutung von Computern in der modernen Physik

### Beispiele

1. **Klassische Mechanik: Fallbewegung**

   Galileo Galilei untersuchte die Fallbewegung und entdeckte, dass alle Körper unabhängig von ihrer Masse gleich schnell fallen (im Vakuum).

   Fallgesetz: $s = \frac{1}{2}gt^2$

   wobei:
   $s$: zurückgelegte Strecke
   $g$: Erdbeschleunigung ($\approx 9.81 \text{ m/s}^2$)
   $t$: Zeit

2. **Elektromagnetismus: Maxwell-Gleichungen**

   James Clerk Maxwell vereinheitlichte Elektrizität und Magnetismus in seinen berühmten Gleichungen:

   $\nabla \cdot \mathbf{E} = \frac{\rho}{\epsilon_0}$ (Gaußsches Gesetz)
   $\nabla \cdot \mathbf{B} = 0$ (Gaußsches Gesetz für Magnetismus)
   $\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}$ (Faradaysches Induktionsgesetz)
   $\nabla \times \mathbf{B} = \mu_0\mathbf{J} + \mu_0\epsilon_0\frac{\partial \mathbf{E}}{\partial t}$ (Ampère-Maxwell-Gesetz)

3. **Spezielle Relativitätstheorie: Zeitdilatation**

   Einstein zeigte, dass Zeit relativ ist und sich bei hohen Geschwindigkeiten verlangsamt:

   $\Delta t' = \frac{\Delta t}{\sqrt{1-\frac{v^2}{c^2}}}$

   wobei:
   $\Delta t'$: Zeit im bewegten System
   $\Delta t$: Zeit im ruhenden System
   $v$: Relativgeschwindigkeit
   $c$: Lichtgeschwindigkeit

4. **Quantenmechanik: Schrödinger-Gleichung**

   Die Schrödinger-Gleichung beschreibt das Verhalten von Quantensystemen:

   $i\hbar\frac{\partial}{\partial t}\Psi(\mathbf{r},t) = \left[-\frac{\hbar^2}{2m}\nabla^2 + V(\mathbf{r},t)\right]\Psi(\mathbf{r},t)$

   wobei:
   $\Psi$: Wellenfunktion
   $\hbar$: reduziertes Plancksches Wirkungsquantum
   $m$: Masse des Teilchens
   $V$: Potenzial

5. **Computergestützte Physik: Monte-Carlo-Simulation**

   Moderne physikalische Forschung nutzt oft Computersimulationen, z.B. die Monte-Carlo-Methode zur Berechnung komplexer Integrale:

   $\int_a^b f(x) dx \approx \frac{b-a}{N} \sum_{i=1}^N f(x_i)$

   wobei:
   $N$: Anzahl der zufällig gewählten Punkte
   $x_i$: zufällig gewählte Punkte im Intervall $[a,b]$

Diese Beispiele zeigen die Entwicklung der Physik von klassischen Konzepten bis hin zu modernen Theorien und Methoden, wobei die zunehmende mathematische Komplexität und die Bedeutung von Computern in der modernen Physik deutlich werden.

## Maßeinheiten

### Lernziel

Erfassen der Bedeutung von Maßeinheiten und Kennenlernen des Internationalen Einheitensystems (SI).

### Notizen

- Physikalische Größen: Produkt aus Zahlenwert und Einheit
- SI-Basiseinheiten:
  - Sekunde (s): Zeit
  - Meter (m): Länge
  - Kilogramm (kg): Masse
  - Kelvin (K): Temperatur
  - Ampere (A): Elektrischer Strom
  - Mol (mol): Stoffmenge
  - Candela (cd): Lichtstärke
- Vorsätze für Zehnerpotenzen: z.B. Kilo (k) für $10^3$, Milli (m) für $10^{-3}$
- Umrechnung zwischen Einheiten mittels Umrechnungsfaktoren

### Beispiele

1. **Längenumrechnung**

   1 km = 1000 m
   
   Beispiel: 5,4 km in m umrechnen
   
   $5,4 \text{ km} = 5,4 \times 1000 \text{ m} = 5400 \text{ m}$

2. **Geschwindigkeitsumrechnung**

   1 m/s = 3,6 km/h
   
   Beispiel: 20 m/s in km/h umrechnen
   
   $20 \text{ m/s} = 20 \times 3,6 \text{ km/h} = 72 \text{ km/h}$

3. **Verwendung von SI-Vorsätzen**

   1 MHz = $10^6$ Hz
   1 μm = $10^{-6}$ m
   
   Beispiel: 2,5 GHz in Hz ausdrücken
   
   $2,5 \text{ GHz} = 2,5 \times 10^9 \text{ Hz}$

4. **Flächenberechnung mit SI-Einheiten**

   Fläche eines Rechtecks: $A = l \times b$
   
   Beispiel: $l = 2 \text{ m}$, $b = 50 \text{ cm}$
   
   $A = 2 \text{ m} \times 0,5 \text{ m} = 1 \text{ m}^2$

5. **Dichte-Berechnung**

   Dichte: $\rho = \frac{m}{V}$
   
   Beispiel: $m = 500 \text{ g}$, $V = 200 \text{ cm}^3$
   
   $\rho = \frac{500 \text{ g}}{200 \text{ cm}^3} = 2,5 \text{ g/cm}^3$
   
   In SI-Einheiten:
   $\rho = \frac{0,5 \text{ kg}}{0,0002 \text{ m}^3} = 2500 \text{ kg/m}^3$

6. **Temperaturumrechnung**

   Celsius zu Kelvin: $T(K) = T(°C) + 273,15$
   
   Beispiel: 25°C in Kelvin
   
   $T = 25°C + 273,15 = 298,15 \text{ K}$

7. **Elektrische Leistung**

   Leistung: $P = U \times I$
   
   Beispiel: $U = 230 \text{ V}$, $I = 2 \text{ A}$
   
   $P = 230 \text{ V} \times 2 \text{ A} = 460 \text{ W} = 0,46 \text{ kW}$

Diese Beispiele demonstrieren die Anwendung von SI-Einheiten, Umrechnungen zwischen verschiedenen Einheiten und die Verwendung von SI-Vorsätzen in praktischen Berechnungen.

## Dimensionen physikalischer Größen

### Lernziel

Verstehen des Konzepts der Dimensionen und ihrer Anwendung in der Dimensionsanalyse.

### Notizen
- Dimension: Qualitative Beschreibung einer Größe
- Grunddimensionen: Länge [L], Zeit [T], Masse [M]
- Dimensionsanalyse: Überprüfung der Konsistenz von Gleichungen
- Beispiel: Geschwindigkeit hat die Dimension [L]/[T]

## Signifikante Stellen und Größenordnungen

### Lernziel
Korrekter Umgang mit Messwerten in Bezug auf signifikante Stellen und Größenordnungen.

### Notizen
- Signifikante Stellen: Zuverlässig bekannte Ziffern eines Messwerts
- Regeln für Berechnungen mit signifikanten Stellen
- Exponentialschreibweise: $a \cdot 10^n$ für große/kleine Zahlen
- Größenordnung: Gerundeter Wert auf nächste Zehnerpotenz

## Messgenauigkeit und Messfehler

### Lernziel
Verstehen der Konzepte der Messgenauigkeit, verschiedener Arten von Messfehlern und der Grundlagen der Fehlerrechnung.

### Notizen

- Systematische Fehler: Konstante Abweichungen
- Statistische Fehler: Zufällige Schwankungen
- Gauß'sche Normalverteilung: $f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-(x-\langle x \rangle)^2/(2\sigma^2)}$
- Mittelwert: $\langle x \rangle = \frac{1}{n}\sum_{i=1}^n x_i$
- Standardabweichung: $\sigma = \sqrt{\frac{1}{n-1}\sum_{i=1}^n (x_i - \langle x \rangle)^2}$
- Fehlerfortpflanzung: $\Delta Y = \sqrt{\sum_{j=1}^m (\frac{\partial Y}{\partial X_j}\Delta X_j)^2}$

### Rechenbeispielen

1. **Systematischer Fehler:**

   **Beispiel:** Ein Thermometer zeigt stets 1.5°C zu viel an.

   **Korrektur:**

   Gemessene Temperatur: $T_{\text{gemessen}} = 25.3^\circ \text{C}$  
   Korrektur: $T_{\text{korrigiert}} = T_{\text{gemessen}} - 1.5^\circ \text{C} = 25.3^\circ \text{C} - 1.5^\circ \text{C} = 23.8^\circ \text{C}$



2. Mittelwertberechnung:
   **Beispiel:** Fünf Messungen der Fallzeit eines Balls: 2.1s, 2.3s, 2.0s, 2.2s, 2.1s

   **Berechnung:**

   $\langle t \rangle = \frac{1}{n} \sum_{i=1}^n t_i = \frac{1}{5}(2.1 + 2.3 + 2.0 + 2.2 + 2.1)$
   $= \frac{1}{5}(10.7) = 2.14\text{ s}$


3. Standardabweichung:
   **Beispiel:** Nutzen wir die Daten aus dem vorherigen Beispiel.

   **Berechnung:**

   $\sigma = \sqrt{\frac{1}{n-1} \sum_{i=1}^n (t_i - \langle t \rangle)^2}$
   
   $= \sqrt{\frac{1}{4}[(2.1-2.14)^2 + (2.3-2.14)^2 + (2.0-2.14)^2 + (2.2-2.14)^2 + (2.1-2.14)^2]}$
   
   $= \sqrt{\frac{1}{4}[(-0.04)^2 + (0.16)^2 + (-0.14)^2 + (0.06)^2 + (-0.04)^2]}$
   
   $= \sqrt{\frac{1}{4}[0.0016 + 0.0256 + 0.0196 + 0.0036 + 0.0016]}$
   
   $= \sqrt{\frac{0.052}{4}} = \sqrt{0.013} \approx 0.114\text{ s}$


4. Fehlerfortpflanzung:
   **Beispiel:** Berechnung des Fehlers bei der Bestimmung der Fläche eines Rechtecks.
   
   Länge: $l = 5.0 \pm 0.1\text{ m}$, Breite: $b = 3.0 \pm 0.1\text{ m}$

   **Berechnung:**

   Fläche: $A = l \cdot b$
   
   $\Delta A = \sqrt{(\frac{\partial A}{\partial l}\Delta l)^2 + (\frac{\partial A}{\partial b}\Delta b)^2}$
   
   $= \sqrt{(b\Delta l)^2 + (l\Delta b)^2}$
   
   $= \sqrt{(3.0 \cdot 0.1)^2 + (5.0 \cdot 0.1)^2}$
   
   $= \sqrt{0.09 + 0.25} = \sqrt{0.34} \approx 0.58\text{ m}^2$
   
   Also: $A = 5.0 \text{ m} \cdot 3.0 \text{ m} \pm 0.58 \text{ m}^2 = 15.0 \pm 0.6 \text{ m}^2$


5. Gauß'sche Normalverteilung:
   **Beispiel:** Berechnung der Wahrscheinlichkeitsdichte für einen Messwert.
   
   Mittelwert $\langle x \rangle = 10$, Standardabweichung $\sigma = 2$, für $x = 11$

   **Berechnung:**

   $f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x-\langle x \rangle)^2}{2\sigma^2}}$
   
   $= \frac{1}{2\sqrt{2\pi}} e^{-\frac{(11-10)^2}{2(2)^2}}$
   
   $= \frac{1}{2\sqrt{2\pi}} e^{-\frac{1}{8}} \approx 0.176$


# Regeln für Berechnungen in Exponentialschreibweise

1. **Multiplikation und Division**:
   - Bei Multiplikation: Exponenten addieren
   - Bei Division: Exponenten subtrahieren

   Beispiele:
   - Multiplikation: $10^2 \cdot 10^3 = 100 \cdot 1000 = 100\,000 = 10^5$
   - Division: $\frac{10^2}{10^3} = \frac{100}{1000} = \frac{1}{10} = 10^{-1}$

2. **Nullte Potenz**:
   $10^0 = 1$ (per Definition)

   Beispiel: $\frac{1000}{1000} = \frac{10^3}{10^3} = 10^{3-3} = 10^0 = 1$

3. **Addition und Subtraktion**:
   Bei unterschiedlichen Exponenten vorsichtig sein:

   Beispiel: $(1,200 \cdot 10^2) + (8 \cdot 10^{-1}) = 120,0 + 0,8 = 120,8$

4. **Anpassung der Exponenten**:
   Für einfachere Addition/Subtraktion, Exponenten angleichen:

   Beispiel: $(1200 \cdot 10^{-1}) + (8 \cdot 10^{-1}) = 1208 \cdot 10^{-1} = 120,8$

5. **Potenzieren von Zehnerpotenzen**:
   Exponenten multiplizieren

   Beispiel: $(10^2)^4 = 10^2 \cdot 10^2 \cdot 10^2 \cdot 10^2 = 10^8$

6. **Negative Exponenten**:
   Bei Ergebnissen kleiner als 1 ist der Exponent negativ.

7. **Vorsicht bei Exponentenberechnungen**:
   Fehler bei Addition, Subtraktion oder Multiplikation von Exponenten können zu großen Abweichungen führen.

8. **Zwischenergebnisse**:
   Nutzen Sie den Rechnerspeicher für Zwischenergebnisse, um Rundungsfehler zu minimieren.

Beachten Sie diese Regeln sorgfältig, um präzise Ergebnisse bei Berechnungen mit Exponentialschreibweise zu erzielen.

# Zusammenfassung

Die Physik strebt nach einer präzisen Beschreibung und Erklärung der Naturgesetze. Sie verwendet dazu eine systematische Methodik aus Beobachtung, Hypothesenbildung und experimenteller Überprüfung. Physikalische Größen werden durch Zahlenwerte und Einheiten ausgedrückt, wobei das Internationale Einheitensystem (SI) sieben Basiseinheiten definiert. 

Die Dimensionsanalyse dient der Überprüfung der Konsistenz physikalischer Gleichungen. Bei der Angabe von Messwerten sind signifikante Stellen und Größenordnungen zu beachten. Die Exponentialschreibweise erleichtert den Umgang mit sehr großen oder kleinen Zahlen.

Messungen unterliegen stets Unsicherheiten. Man unterscheidet zwischen systematischen Fehlern, die konstante Abweichungen verursachen, und statistischen Fehlern, die zu zufälligen Schwankungen führen. Die Gauß'sche Normalverteilung beschreibt häufig die Verteilung von Messwerten. Zentrale statistische Größen sind der Mittelwert und die Standardabweichung. Die Fehlerfortpflanzung ermöglicht die Berechnung der Gesamtunsicherheit bei kombinierten Messgrößen.

Diese Konzepte bilden die Grundlage für präzise Messungen und zuverlässige Datenanalysen in der Physik. Sie ermöglichen ein tieferes Verständnis der natürlichen Welt und die Entwicklung neuer Technologien.
