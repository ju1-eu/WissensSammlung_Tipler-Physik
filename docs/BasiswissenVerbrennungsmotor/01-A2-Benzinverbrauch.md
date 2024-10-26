---
title: "Benzinverbrauch"
author: "Jan Unger"
date: "2024-10-24"
---

# Wie groß ist der Benzinverbrauch in l/100 km bei 180 km/h?

Letzte Aktualisierung: 2024-10-26

**Quelle**: K. Schreiner, *Basiswissen Verbrennungsmotor: Fragen – rechnen – verstehen – bestehen*, 3., erweiterte und aktualisierte Auflage. Wiesbaden: Springer Fachmedien Wiesbaden, 2020. Verfügbar: https://doi.org/10.1007/978-3-658-29226-3

- [Wie groß ist der Benzinverbrauch in l/100 km bei 180 km/h?](#wie-groß-ist-der-benzinverbrauch-in-l100-km-bei-180-kmh)
- [Zusammenfassung](#zusammenfassung)
  - [Ausgangssituation und bekannte Größen](#ausgangssituation-und-bekannte-größen)
    - [Gegebene Werte](#gegebene-werte)
    - [Physikalische Grundlagen](#physikalische-grundlagen)
  - [Berechnungsschritte](#berechnungsschritte)
    - [Berechnung des Kraftstoffmassenstroms](#berechnung-des-kraftstoffmassenstroms)
    - [Berechnung des Volumenstroms](#berechnung-des-volumenstroms)
    - [Berechnung des streckenbezogenen Verbrauchs](#berechnung-des-streckenbezogenen-verbrauchs)
  - [Sensitivitätsanalyse](#sensitivitätsanalyse)
    - [Einfluss des Wirkungsgrads](#einfluss-des-wirkungsgrads)
    - [Einflussfaktoren auf den Verbrauch](#einflussfaktoren-auf-den-verbrauch)
  - [Fazit und Praxisbezug](#fazit-und-praxisbezug)
- [Schritt-für-Schritt-Berechnung: Kraftstoffverbrauch bei 180 km/h](#schritt-für-schritt-berechnung-kraftstoffverbrauch-bei-180-kmh)
  - [Schritt 1: Aufgabenanalyse](#schritt-1-aufgabenanalyse)
    - [Gegeben:](#gegeben)
    - [Gesucht:](#gesucht)
  - [Schritt 2: Berechnung des Kraftstoffmassenstroms](#schritt-2-berechnung-des-kraftstoffmassenstroms)
    - [a) Grundgleichung:](#a-grundgleichung)
    - [b) Umstellung nach Massenstrom:](#b-umstellung-nach-massenstrom)
    - [c) Einsetzen der Werte:](#c-einsetzen-der-werte)
  - [Schritt 3: Berechnung des Volumenstroms](#schritt-3-berechnung-des-volumenstroms)
    - [a) Umrechnung von Massen- in Volumenstrom:](#a-umrechnung-von-massen--in-volumenstrom)
    - [b) Einsetzen und Berechnung:](#b-einsetzen-und-berechnung)
  - [Schritt 4: Berechnung des streckenbezogenen Verbrauchs](#schritt-4-berechnung-des-streckenbezogenen-verbrauchs)
    - [a) Normierung auf 100 km:](#a-normierung-auf-100-km)
    - [b) Einsetzen und Berechnung:](#b-einsetzen-und-berechnung-1)
  - [Schritt 5: Sensitivitätsanalyse](#schritt-5-sensitivitätsanalyse)
    - [a) Berechnung für 27%:](#a-berechnung-für-27)
    - [b) Berechnung für 33%:](#b-berechnung-für-33)
  - [Validierung der Ergebnisse:](#validierung-der-ergebnisse)
  - [Schlussfolgerungen:](#schlussfolgerungen)
- [Formeln und Berechnungen zum Kraftstoffverbrauch](#formeln-und-berechnungen-zum-kraftstoffverbrauch)
  - [Grundlegende Formeln](#grundlegende-formeln)
    - [Effektive Motorleistung](#effektive-motorleistung)
    - [Kraftstoffmassenstrom](#kraftstoffmassenstrom)
    - [Volumenstrom](#volumenstrom)
    - [Streckenbezogener Verbrauch](#streckenbezogener-verbrauch)
  - [Verwendete Symbole und Fachbegriffe](#verwendete-symbole-und-fachbegriffe)
    - [Griechische Buchstaben](#griechische-buchstaben)
    - [Lateinische Symbole](#lateinische-symbole)
    - [Fachbegriffe](#fachbegriffe)
- [Benzinverbrauch bei 180 km/h - Umfassende Analyse](#benzinverbrauch-bei-180-kmh---umfassende-analyse)
  - [ABC-Liste nach Birkenbihl](#abc-liste-nach-birkenbihl)
  - [KAWA-Analyse für "KRAFTSTOFF"](#kawa-analyse-für-kraftstoff)
  - [Mindmap: Benzinverbrauch bei 180 km/h](#mindmap-benzinverbrauch-bei-180-kmh)
  - [Kategorische Wissensanalyse](#kategorische-wissensanalyse)


# Zusammenfassung

**Lernziele**:

- Luftwiderstandskraft
- Rollwiderstandskraft
- mechanischer Wirkungsgrad des Antriebsstrangs
- thermische Zustandsgleichung
- Luftdichte

## Ausgangssituation und bekannte Größen

### Gegebene Werte

- Geschwindigkeit: $v = 180~\text{km/h}$
- Motorleistung: $P_\text{e} = 75{,}6~\text{kW}$ (aus vorheriger Berechnung)
- Heizwert Ottokraftstoff: $H_\text{U} = 42.000~\text{kJ/kg}$
- Kraftstoffdichte: $\rho_\text{B} = 0{,}76~\text{kg/l}$
- Effektiver Wirkungsgrad: $\eta_\text{e} \approx 30\%$ (Ottomotor bei Nennleistung)

### Physikalische Grundlagen

- Der Kraftstoffverbrauch ergibt sich aus der erforderlichen Motorleistung und dem Wirkungsgrad
- Die Umrechnung von Massenstrom in Volumenstrom erfolgt über die Kraftstoffdichte
- Der streckenbezogene Verbrauch wird auf 100 km normiert

## Berechnungsschritte

### Berechnung des Kraftstoffmassenstroms

Die Grundgleichung für die effektive Motorleistung lautet:

$$P_\text{e} = \eta_\text{e} \cdot \dot{m}_\text{B} \cdot H_\text{U}$$

Umgestellt nach dem Kraftstoffmassenstrom:

$$\dot{m}_\text{B} = \frac{P_\text{e}}{\eta_\text{e} \cdot H_\text{U}}$$

Einsetzen der Werte:

$$\dot{m}_\text{B} = \frac{75{,}6~\text{kW}}{0{,}30 \cdot 42.000~\text{kJ/kg}} = 0{,}006~\text{kg/s}$$

### Berechnung des Volumenstroms

Umrechnung des Massenstroms in Volumenstrom:

$$\dot{V}_\text{B} = \frac{\dot{m}_\text{B}}{\rho_\text{B}}$$

Einsetzen der Werte:

$$\dot{V}_\text{B} = \frac{0{,}006~\text{kg/s}}{0{,}76~\text{kg/l}} = 0{,}00789~\text{l/s} = 28{,}42~\text{l/h}$$

### Berechnung des streckenbezogenen Verbrauchs

Umrechnung auf Verbrauch pro 100 km:

$$B_{100} = \frac{\dot{V}_\text{B}}{v} \cdot 100~\text{km}$$

Einsetzen der Werte:

$$B_{100} = \frac{28{,}42~\text{l/h}}{180~\text{km/h}} \cdot 100~\text{km} = 15{,}8~\text{l/100km}$$

## Sensitivitätsanalyse

### Einfluss des Wirkungsgrads

- Bei $\eta_\text{e} = 27\%$: $B_{100} = 17{,}5~\text{l/100km}$
- Bei $\eta_\text{e} = 33\%$: $B_{100} = 14{,}4~\text{l/100km}$

### Einflussfaktoren auf den Verbrauch

1. **Direkte Faktoren:**
   - Motorwirkungsgrad
   - Heizwert des Kraftstoffs
   - Fahrgeschwindigkeit
   - Erforderliche Motorleistung

2. **Indirekte Faktoren:**
   - Luftwiderstand
   - Rollwiderstand
   - Fahrbahnsteigung
   - Fahrzeugmasse

## Fazit und Praxisbezug

- Der berechnete Verbrauch von $15{,}8~\text{l/100km}$ liegt im typischen Bereich für Fahrzeuge der A-Klasse bei 180 km/h
- Die Spanne von 14,4 bis 17,5 l/100km zeigt den erheblichen Einfluss des Motorwirkungsgrads
- Der hohe Verbrauch bei dieser Geschwindigkeit resultiert hauptsächlich aus dem überproportional ansteigenden Luftwiderstand
- Die Berechnung verdeutlicht den Zusammenhang zwischen Fahrwiderständen, Motorleistung und Kraftstoffverbrauch

# Schritt-für-Schritt-Berechnung: Kraftstoffverbrauch bei 180 km/h

## Schritt 1: Aufgabenanalyse

### Gegeben:

- Geschwindigkeit: $v = 180~\text{km/h}$
- Motorleistung: $P_\text{e} = 75{,}6~\text{kW}$
- Heizwert Ottokraftstoff: $H_\text{U} = 42.000~\text{kJ/kg}$
- Kraftstoffdichte: $\rho_\text{B} = 0{,}76~\text{kg/l}$
- Effektiver Wirkungsgrad: $\eta_\text{e} = 30\% = 0{,}30$

### Gesucht:

- Kraftstoffverbrauch in $\text{l/100km}$

## Schritt 2: Berechnung des Kraftstoffmassenstroms

### a) Grundgleichung:

Die effektive Motorleistung $P_\text{e}$ ergibt sich aus:

$$P_\text{e} = \eta_\text{e} \cdot \dot{m}_\text{B} \cdot H_\text{U}$$

### b) Umstellung nach Massenstrom:

Umformen nach $\dot{m}_\text{B}$:

$$\dot{m}_\text{B} = \frac{P_\text{e}}{\eta_\text{e} \cdot H_\text{U}}$$

### c) Einsetzen der Werte:

Umrechnung der Einheiten:

- $P_\text{e} = 75{,}6~\text{kW} = 75.600~\text{W}$
- $H_\text{U} = 42.000~\text{kJ/kg} = 42.000.000~\text{J/kg}$

Berechnung:

$$\dot{m}_\text{B} = \frac{75.600~\text{W}}{0{,}30 \cdot 42.000.000~\text{J/kg}} = 0{,}006~\text{kg/s}$$

## Schritt 3: Berechnung des Volumenstroms

### a) Umrechnung von Massen- in Volumenstrom:

$$\dot{V}_\text{B} = \frac{\dot{m}_\text{B}}{\rho_\text{B}}$$

### b) Einsetzen und Berechnung:

$$\dot{V}_\text{B} = \frac{0{,}006~\text{kg/s}}{0{,}76~\text{kg/l}} = 0{,}00789~\text{l/s}$$

Umrechnung in Liter pro Stunde:

$$\dot{V}_\text{B} = 0{,}00789~\text{l/s} \cdot 3600~\text{s/h} = 28{,}42~\text{l/h}$$

## Schritt 4: Berechnung des streckenbezogenen Verbrauchs

### a) Normierung auf 100 km:

$$B_{100} = \frac{\dot{V}_\text{B}}{v} \cdot 100~\text{km}$$

### b) Einsetzen und Berechnung:

$$B_{100} = \frac{28{,}42~\text{l/h}}{180~\text{km/h}} \cdot 100~\text{km} = 15{,}8~\text{l/100km}$$

## Schritt 5: Sensitivitätsanalyse

### a) Berechnung für 27%:

$$\dot{m}_\text{B} = \frac{75.600~\text{W}}{0{,}27 \cdot 42.000.000~\text{J/kg}} = 0{,}0067~\text{kg/s}$$

$$\dot{V}_\text{B} = \frac{0{,}0067~\text{kg/s}}{0{,}76~\text{kg/l}} \cdot 3600~\text{s/h} = 31{,}58~\text{l/h}$$

$$B_{100} = \frac{31{,}58~\text{l/h}}{180~\text{km/h}} \cdot 100~\text{km} = 17{,}5~\text{l/100km}$$

### b) Berechnung für 33%:

$$\dot{m}_\text{B} = \frac{75.600~\text{W}}{0{,}33 \cdot 42.000.000~\text{J/kg}} = 0{,}0055~\text{kg/s}$$

$$\dot{V}_\text{B} = \frac{0{,}0055~\text{kg/s}}{0{,}76~\text{kg/l}} \cdot 3600~\text{s/h} = 25{,}83~\text{l/h}$$

$$B_{100} = \frac{25{,}83~\text{l/h}}{180~\text{km/h}} \cdot 100~\text{km} = 14{,}4~\text{l/100km}$$

## Validierung der Ergebnisse:

1. **Plausibilitätsprüfung**:
   - Verbrauch bei $\eta_\text{e} = 27\%$: $17{,}5~\text{l/100km}$
   - Verbrauch bei $\eta_\text{e} = 30\%$: $15{,}8~\text{l/100km}$
   - Verbrauch bei $\eta_\text{e} = 33\%$: $14{,}4~\text{l/100km}$

2. **Einheitenkonsistenz**:
   - Leistung: $\text{kW} \rightarrow \text{W}$
   - Heizwert: $\text{kJ/kg} \rightarrow \text{J/kg}$
   - Volumenstrom: $\text{l/s} \rightarrow \text{l/h}$
   - Endverbrauch: $\text{l/100km}$

## Schlussfolgerungen:

1. **Physikalische Zusammenhänge**:
   - Der Verbrauch ist umgekehrt proportional zum Wirkungsgrad
   - Die hohe Geschwindigkeit ($180~\text{km/h}$) führt zu hohem Leistungsbedarf
   - Der Verbrauch wird maßgeblich durch den Wirkungsgrad beeinflusst

2. **Praktische Bedeutung**:
   - Der Verbrauch von $15{,}8~\text{l/100km}$ ist realistisch für $180~\text{km/h}$
   - Eine Wirkungsgradverbesserung um 6 Prozentpunkte spart etwa $3{,}1~\text{l/100km}$
   - Der Dieselmotor hat durch höheren Wirkungsgrad ($\approx 35\%$) Verbrauchsvorteile

# Formeln und Berechnungen zum Kraftstoffverbrauch

## Grundlegende Formeln

### Effektive Motorleistung

$$P_\text{e} = \eta_\text{e} \cdot \dot{m}_\text{B} \cdot H_\text{U}$$

### Kraftstoffmassenstrom

$$\dot{m}_\text{B} = \frac{P_\text{e}}{\eta_\text{e} \cdot H_\text{U}}$$

### Volumenstrom

$$\dot{V}_\text{B} = \frac{\dot{m}_\text{B}}{\rho_\text{B}}$$

### Streckenbezogener Verbrauch

$$B_{100} = \frac{\dot{V}_\text{B}}{v} \cdot 100~\text{km}$$

## Verwendete Symbole und Fachbegriffe

### Griechische Buchstaben

- $\eta_\text{e}$ (eta): Effektiver Wirkungsgrad des Motors
- $\rho_\text{B}$ (rho): Dichte des Kraftstoffs

### Lateinische Symbole

- $P_\text{e}$: Effektive Motorleistung [kW]
- $\dot{m}_\text{B}$: Kraftstoffmassenstrom [kg/s]
- $H_\text{U}$: Unterer Heizwert des Kraftstoffs [kJ/kg]
- $\dot{V}_\text{B}$: Kraftstoffvolumenstrom [l/s]
- $B_{100}$: Streckenbezogener Verbrauch [l/100km]
- $v$: Fahrzeuggeschwindigkeit [km/h]

### Fachbegriffe

- **Effektiver Wirkungsgrad**: Verhältnis von nutzbarer mechanischer Leistung zu zugeführter Kraftstoffleistung
- **Heizwert**: Energieinhalt pro Masse Kraftstoff
- **Massenstrom**: Kraftstoffdurchsatz pro Zeiteinheit
- **Volumenstrom**: Kraftstoffvolumen pro Zeiteinheit
- **Streckenbezogener Verbrauch**: Kraftstoffverbrauch bezogen auf 100 km Fahrstrecke

# Benzinverbrauch bei 180 km/h - Umfassende Analyse

## ABC-Liste nach Birkenbihl

| Buchstabe | Begriff                 | Erklärung                                            |
| --------- | ----------------------- | ---------------------------------------------------- |
| A         | Antriebsstrang          | Mechanische Komponenten zur Kraftübertragung         |
| B         | Benzinverbrauch         | Kraftstoffverbrauch in l/(100 km)                    |
| D         | Dieselmotor             | Verbrennungsmotor mit höherem Wirkungsgrad (≈35%)    |
| E         | Effektiver Wirkungsgrad | Verhältnis von nutzbarer zu zugeführter Energie      |
| F         | Fahrwiderstand          | Kräfte, die der Fahrzeugbewegung entgegenwirken      |
| G         | Geschwindigkeit         | Hier: 180 km/h                                       |
| H         | Heizwert                | Energiegehalt pro kg Kraftstoff (HU)                 |
| K         | Kraftstoffdichte        | Masse pro Volumen (ρ = 0,76 kg/l für Ottokraftstoff) |
| L         | Luftdichte              | Masse der Luft pro Volumen                           |
| M         | Massenstrom             | Kraftstoffdurchsatz pro Zeit                         |
| N         | Nennleistung            | Maximale Dauerleistung des Motors                    |
| O         | Ottomotor               | Verbrennungsmotor mit ca. 30% Wirkungsgrad           |
| P         | Pe (Leistung)           | Effektive Motorleistung                              |
| R         | Rollwiderstand          | Widerstandskraft durch Reifenverformung              |
| S         | Streckenbezogen         | Verbrauch pro 100 km Fahrstrecke                     |
| T         | Thermodynamik           | Lehre von Energieumwandlungen                        |
| V         | Volumenstrom            | Kraftstoffdurchsatz in l/h                           |
| W         | Widerstandskraft        | Summe aller bremsenden Kräfte                        |

## KAWA-Analyse für "KRAFTSTOFF"

- **K**raft, **K**inematik, **K**onstanten
- **R**ollwiderstand, **R**eibung
- **A**ntriebsenergie, **A**ußentemperatur
- **F**ahrwiderstand, **F**ahrzeugmasse
- **T**hermodynamik, **T**reibstoff
- **S**trömung, **S**trecke
- **T**emperatur, **T**reibstoff
- **O**ttomotor, **O**berflächenreibung
- **F**lüssigkeit, **F**ahrzeug
- **F**ließrate, **F**örderung

## Mindmap: Benzinverbrauch bei 180 km/h

1. Fahrzeugspezifische Faktoren
   - Motortyp (Ottomotor)
   - Effektiver Wirkungsgrad (≈30%)
   - Antriebsstrang
   - Fahrzeuggeometrie

2. Energetische Faktoren
   - Heizwert (HU = 42.000 kJ/kg)
   - Kraftstoffdichte (ρ = 0,76 kg/l)
   - Leistungsbedarf (75,6 kW)
   - Energieumwandlung

3. Fahrwiderstände
   - Luftwiderstand
   - Rollwiderstand
   - Steigungswiderstand
   - Beschleunigungswiderstand

4. Verbrauchsberechnung
   - Kraftstoffmassenstrom
   - Volumenstrom
   - Streckenbezogener Verbrauch
   - Verbrauchsspanne (14,4-17,5 l/100km)

## Kategorische Wissensanalyse

1. **Physikalische Grundgrößen**
   - Geschwindigkeit (180 km/h)
   - Leistung (75,6 kW)
   - Masse
   - Dichte

2. **Energetische Kenngrößen**
   - Heizwert (42.000 kJ/kg)
   - Effektiver Wirkungsgrad (27-33%)
   - Kraftstoffdichte (0,76 kg/l)
   - Energieumwandlung

3. **Verbrauchskenngrößen**
   - Kraftstoffmassenstrom
   - Volumenstrom
   - Streckenbezogener Verbrauch
   - Verbrauchsbereich (14,4-17,5 l/100km)

4. **Technische Systeme**
   - Ottomotor
   - Antriebsstrang
   - Kraftstoffanlage
   - Fahrzeugaufbau

5. **Einflussfaktoren**
   - Motorwirkungsgrad
   - Fahrwiderstände
   - Umgebungsbedingungen
   - Fahrzeugparameter

6. **Berechnungsmethoden**
   - Leistungsberechnung
   - Massenstromberechnung
   - Volumenstromberechnung
   - Verbrauchsberechnung