---
title: "Fahrwiderstand und Motorleistung"
author: "Jan Unger"
date: "2024-10-24"
---

# Welche Leistung benötigt die A-Klasse bei einer Geschwindigkeit von 180 km/h?

Letzte Aktualisierung: 2024-10-24

Quelle: Basiswissen Verbrennungsmotor, Fragen – rechnen – verstehen – bestehen (Schreiner 2020)

## Inhaltsverzeichnis

- [Welche Leistung benötigt die A-Klasse bei einer Geschwindigkeit von 180 km/h?](#welche-leistung-benötigt-die-a-klasse-bei-einer-geschwindigkeit-von-180-kmh)
  - [Inhaltsverzeichnis](#inhaltsverzeichnis)
- [Prompt](#prompt)
- [Formeln zur Leistungsberechnung der A-Klasse](#formeln-zur-leistungsberechnung-der-a-klasse)
  - [Grundlegende Gleichungen](#grundlegende-gleichungen)
    - [Luftdichte aus thermischer Zustandsgleichung](#luftdichte-aus-thermischer-zustandsgleichung)
    - [Widerstandskräfte](#widerstandskräfte)
    - [Leistungen](#leistungen)
  - [2. Parameter](#2-parameter)
    - [Fahrzeugspezifische Größen](#fahrzeugspezifische-größen)
    - [Betriebsbedingungen](#betriebsbedingungen)
    - [Variante 0](#variante-0)
    - [Variante 2](#variante-2)
  - [3. Ergebnisse](#3-ergebnisse)
    - [Variante 0](#variante-0-1)
    - [Variante 2](#variante-2-1)
- [Leistungsberechnung A-Klasse bei 180 km/h - Vergleich zweier Varianten](#leistungsberechnung-a-klasse-bei-180-kmh---vergleich-zweier-varianten)
  - [1. Gegebene Werte der A-Klasse](#1-gegebene-werte-der-a-klasse)
    - [Gemeinsame Parameter:](#gemeinsame-parameter)
    - [Variantenspezifische Parameter:](#variantenspezifische-parameter)
  - [2. Berechnung der Widerstandskräfte](#2-berechnung-der-widerstandskräfte)
    - [a) Luftwiderstandskraft (identisch für beide Varianten)](#a-luftwiderstandskraft-identisch-für-beide-varianten)
    - [b) Rollwiderstandskraft](#b-rollwiderstandskraft)
    - [c) Gesamtwiderstandskraft](#c-gesamtwiderstandskraft)
  - [3. Berechnung der Leistungen](#3-berechnung-der-leistungen)
    - [a) Radleistung](#a-radleistung)
    - [b) Motorleistung](#b-motorleistung)
  - [4. Vergleichende Analyse](#4-vergleichende-analyse)
  - [5. Auswirkungen der Parameteränderungen](#5-auswirkungen-der-parameteränderungen)

# Prompt

erstelle eine Zusammenfassung aller Formeln 

# Formeln zur Leistungsberechnung der A-Klasse

## Grundlegende Gleichungen

### Luftdichte aus thermischer Zustandsgleichung

$$\rho = \frac{p}{R \cdot T}$$
mit:

- Luftdruck: $$p = 100.000~\text{Pa}$$
- Gaskonstante von Luft: $$R = 287~\text{J}/(\text{kg}\cdot\text{K})$$
- Temperatur: $$T = 293{,}15~\text{K}$$

Ergibt: $$\rho = 1{,}189~\text{kg}/\text{m}^3$$

### Widerstandskräfte

1. Luftwiderstandskraft:
$$\mathbf{F}_\text{cw} = \frac{1}{2} \cdot \rho \cdot v_\text{Auto}^2 \cdot c_\text{w} \cdot A$$
2. Rollwiderstandskraft:
$$\mathbf{F}_\text{roll} = \mu \cdot m \cdot g \cdot \cos(\beta)$$
3. Steigungskraft:
$$\mathbf{F}_\text{steig} = m \cdot g \cdot \sin(\beta)$$
4. Gesamtwiderstandskraft:
$$\mathbf{F}_\text{gesamt} = \mathbf{F}_\text{cw} + \mathbf{F}_\text{roll} + \mathbf{F}_\text{steig}$$

### Leistungen

1. Radleistung:
$$P_\text{Rad} = \mathbf{F}_\text{gesamt} \cdot v_\text{Auto}$$
2. Motorleistung:
$$P_\text{Motor} = \frac{P_\text{Rad}}{\eta_\text{Getriebe}}$$

## 2. Parameter

### Fahrzeugspezifische Größen

- Luftwiderstandsbeiwert: $$c_\text{w} = 0{,}31$$
- Stirnfläche: $$A = 2{,}4~\text{m}^2$$
- Fahrzeugmasse: $$m = 1270~\text{kg}$$

### Betriebsbedingungen

- Geschwindigkeit: $$v_\text{Auto} = 180~\text{km}/\text{h} = 50~\text{m}/\text{s}$$
- Steigungswinkel: $$\beta = 0^\circ$$
- Erdbeschleunigung: $$g = 9{,}81~\text{m}/\text{s}^2$$

### Variante 0

- Getriebewirkungsgrad: $$\eta_\text{Getriebe} = 0{,}92$$
- Rollwiderstandsbeiwert: $$\mu = 0{,}0150$$

### Variante 2

- Getriebewirkungsgrad: $$\eta_\text{Getriebe} = 0{,}90$$
- Rollwiderstandsbeiwert: $$\mu = 0{,}0205$$

## 3. Ergebnisse

### Variante 0

1. $$\mathbf{F}_\text{cw} = 1105{,}77~\text{N}$$
2. $$\mathbf{F}_\text{roll} = 186{,}88~\text{N}$$
3. $$\mathbf{F}_\text{gesamt} = 1292{,}65~\text{N}$$
4. $$P_\text{Rad} = 64{,}63~\text{kW}$$
5. $$P_\text{Motor} = 70{,}25~\text{kW}$$

### Variante 2

1. $$\mathbf{F}_\text{cw} = 1105{,}77~\text{N}$$
2. $$\mathbf{F}_\text{roll} = 255{,}40~\text{N}$$
3. $$\mathbf{F}_\text{gesamt} = 1361{,}17~\text{N}$$
4. $$P_\text{Rad} = 68{,}06~\text{kW}$$
5. $$P_\text{Motor} = 75{,}62~\text{kW}$$


# Leistungsberechnung A-Klasse bei 180 km/h - Vergleich zweier Varianten

## 1. Gegebene Werte der A-Klasse

### Gemeinsame Parameter:

- Luftwiderstandsbeiwert: $$c_\text{w} = 0{,}31$$
- Stirnfläche: $$A = 2{,}4~\text{m}^2$$
- Fahrzeugmasse: $$m = 1270~\text{kg}$$
- Geschwindigkeit: $$v_\text{Auto} = 180~\text{km}/\text{h} = 50~\text{m}/\text{s}$$
- Erdbeschleunigung: $$g = 9{,}81~\text{m}/\text{s}^2$$
- Steigungswinkel: $$\beta = 0^\circ$$
- Luftdichte: $$\rho = 1{,}189~\text{kg}/\text{m}^3$$

### Variantenspezifische Parameter:

| Parameter                | Variante 0   | Variante 2   |
| ------------------------ | ------------ | ------------ |
| $$\eta_\text{Getriebe}$$ | $$0{,}92$$   | $$0{,}90$$   |
| $$\mu$$                  | $$0{,}0150$$ | $$0{,}0205$$ |

## 2. Berechnung der Widerstandskräfte

### a) Luftwiderstandskraft (identisch für beide Varianten)

$$\mathbf{F}_\text{cw} = \frac{1}{2} \cdot \rho \cdot v_\text{Auto}^2 \cdot c_\text{w} \cdot A = 1105{,}77~\text{N}$$

### b) Rollwiderstandskraft

$$\mathbf{F}_\text{roll} = \mu \cdot m \cdot g \cdot \cos(\beta)$$

**Variante 0:**
$$\mathbf{F}_\text{roll} = 0{,}0150 \cdot 1270~\text{kg} \cdot 9{,}81~\text{m}/\text{s}^2 \cdot \cos(0^\circ) = 186{,}88~\text{N}$$
**Variante 2:**
$$\mathbf{F}_\text{roll} = 0{,}0205 \cdot 1270~\text{kg} \cdot 9{,}81~\text{m}/\text{s}^2 \cdot \cos(0^\circ) = 255{,}40~\text{N}$$

### c) Gesamtwiderstandskraft

**Variante 0:**
$$\mathbf{F}_\text{gesamt} = 1105{,}77~\text{N} + 186{,}88~\text{N} = 1292{,}65~\text{N}$$

**Variante 2:**
$$\mathbf{F}_\text{gesamt} = 1105{,}77~\text{N} + 255{,}40~\text{N} = 1361{,}17~\text{N}$$

## 3. Berechnung der Leistungen

### a) Radleistung

$$P_\text{Rad} = \mathbf{F}_\text{gesamt} \cdot v_\text{Auto}$$

**Variante 0:**
$$P_\text{Rad} = 1292{,}65~\text{N} \cdot 50~\text{m}/\text{s} = 64{,}63~\text{kW}$$

**Variante 2:**
$$P_\text{Rad} = 1361{,}17~\text{N} \cdot 50~\text{m}/\text{s} = 68{,}06~\text{kW}$$

### b) Motorleistung

$$P_\text{Motor} = \frac{P_\text{Rad}}{\eta_\text{Getriebe}}$$

**Variante 0:**
$$P_\text{Motor} = \frac{64{,}63~\text{kW}}{0{,}92} = 70{,}25~\text{kW}$$
**Variante 2:**
$$P_\text{Motor} = \frac{68{,}06~\text{kW}}{0{,}90} = 75{,}62~\text{kW}$$

## 4. Vergleichende Analyse

| Parameter                    | Variante 0             | Variante 2             | Differenz             |
| ---------------------------- | ---------------------- | ---------------------- | --------------------- |
| $$\eta_\text{Getriebe}$$     | $$0{,}92$$             | $$0{,}90$$             | $$-0{,}02$$           |
| $$\mu$$                      | $$0{,}0150$$           | $$0{,}0205$$           | $$+0{,}0055$$         |
| $$\mathbf{F}_\text{cw}$$     | $$1105{,}77~\text{N}$$ | $$1105{,}77~\text{N}$$ | $$0~\text{N}$$        |
| $$\mathbf{F}_\text{roll}$$   | $$186{,}88~\text{N}$$  | $$255{,}40~\text{N}$$  | $$+68{,}52~\text{N}$$ |
| $$\mathbf{F}_\text{gesamt}$$ | $$1292{,}65~\text{N}$$ | $$1361{,}17~\text{N}$$ | $$+68{,}52~\text{N}$$ |
| $$P_\text{Rad}$$             | $$64{,}63~\text{kW}$$  | $$68{,}06~\text{kW}$$  | $$+3{,}43~\text{kW}$$ |
| $$P_\text{Motor}$$           | $$70{,}25~\text{kW}$$  | $$75{,}62~\text{kW}$$  | $$+5{,}37~\text{kW}$$ |

## 5. Auswirkungen der Parameteränderungen

1. Der erhöhte Rollwiderstandsbeiwert ($$+36{,}7\%$$) führt zu:
   - Höherer Rollwiderstandskraft
   - Gesteigerter Gesamtwiderstandskraft
   - Erhöhter Radleistung
2. Der reduzierte Getriebewirkungsgrad ($$-2{,}2\%$$) bewirkt:
   - Zusätzliche Steigerung der erforderlichen Motorleistung

Die Kombination beider Effekte führt zu einer Erhöhung der erforderlichen Motorleistung um $$7{,}6\%$$.