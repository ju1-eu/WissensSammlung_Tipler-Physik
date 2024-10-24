---
title: "Mindmap"
author: "Jan Unger"
date: "2024-10-24"
---

# Mindmap

Letzte Aktualisierung: 2024-10-24

Quelle: Basiswissen Verbrennungsmotor, Fragen – rechnen – verstehen – bestehen (Schreiner 2020)

## Zentrales Thema: **Fahrwiderstand und Motorleistung**

---

### 1. **Fahrwiderstände**

#### a) **Rollwiderstand ($F_{\text{roll}}$)**

- **Formel:**
  $$
  F_{\text{roll}} = \mu \cdot m \cdot g
  $$
- **Parameter:**
  - **Rollwiderstandsbeiwert ($\mu$)**
    - Typische Werte: 0,010–0,015
    - Beeinflusst durch Reifentyp, Reifendruck, Straßenbeschaffenheit
  - **Fahrzeugmasse ($m$)**
    - Größere Masse erhöht den Rollwiderstand
  - **Erdbeschleunigung ($g$)**
    - Konstant: $9{,}81~\text{m/s}^2$
- **Eigenschaften:**
  - Unabhängig von der Geschwindigkeit
  - Dominant bei niedrigen Geschwindigkeiten
- **Maßnahmen zur Reduzierung:**
  - Leichtbauweise
  - Energiesparreifen
  - Optimierung des Reifendrucks

#### b) **Luftwiderstand ($F_{\text{cw}}$)**

- **Formel:**
  $$
  F_{\text{cw}} = \frac{1}{2} \cdot \rho \cdot c_{\text{w}} \cdot A \cdot v^2
  $$
- **Parameter:**
  - **Luftdichte ($\rho$)**
    - Typischer Wert: $1{,}2041~\text{kg/m}^3$
  - **Luftwiderstandsbeiwert ($c_{\text{w}}$)**
    - Typische Werte: 0,25–0,35
    - Beeinflusst durch Fahrzeugdesign und Aerodynamik
  - **Stirnfläche ($A$)**
    - Abhängig von Fahrzeuggröße und -form
  - **Geschwindigkeit ($v$)**
    - Quadratischer Einfluss auf $F_{\text{cw}}$
- **Eigenschaften:**
  - Dominant bei hohen Geschwindigkeiten
  - Steigt mit dem Quadrat der Geschwindigkeit
- **Maßnahmen zur Reduzierung:**
  - Aerodynamisches Design
  - Verkleinerung der Stirnfläche
  - Glatte Oberflächen

#### c) **Steigungswiderstand ($F_{\text{steig}}$)**

- **Formel:**
  $$
  F_{\text{steig}} = m \cdot g \cdot \sin \beta
  $$
- **Parameter:**
  - **Steigungswinkel ($\beta$)**
    - Relevant bei Fahrten in hügeligem Gelände
- **Eigenschaften:**
  - Beeinflusst den Leistungsbedarf bei Steigungen
  - Bei ebener Strecke ($\beta = 0^\circ$) vernachlässigbar

---

### 2. **Motorleistung**

#### a) **Radleistung ($P_{\text{Rad}}$)**

- **Formel:**
  $$
  P_{\text{Rad}} = F_{\text{ges}} \cdot v
  $$
- **Gesamtwiderstandskraft ($F_{\text{ges}}$)**
  - Summe aller Fahrwiderstände:
    $$
    F_{\text{ges}} = F_{\text{roll}} + F_{\text{cw}} + F_{\text{steig}}
    $$
- **Einflussfaktoren:**
  - Steigende Geschwindigkeit erhöht $P_{\text{Rad}}$
  - Höhere Fahrwiderstände erhöhen den Leistungsbedarf

#### b) **Getriebewirkungsgrad ($\eta_{\text{Getriebe}}$)**

- **Definition:**
  - Verhältnis von Radleistung zu Motorleistung
- **Typische Werte:**
  - Schaltgetriebe: 0,95–0,97
  - Automatikgetriebe: 0,90–0,92
- **Verluste:**
  - Mechanische Reibung
  - Hydraulische Verluste

#### c) **Motorleistung ($P_{\text{Motor}}$)**

- **Formel:**
  $$
  P_{\text{Motor}} = \frac{P_{\text{Rad}}}{\eta_{\text{Getriebe}}}
  $$
- **Einflussfaktoren:**
  - Getriebeverluste erhöhen den benötigten Motoroutput
  - Effizientes Getriebe reduziert den erforderlichen Motorleistungsbedarf

#### d) **Effektiver Motorwirkungsgrad ($\eta_{\text{e}}$)**

- **Definition:**
  - Anteil der im Kraftstoff enthaltenen Energie, der in mechanische Arbeit umgewandelt wird
- **Typische Werte:**
  - **Ottomotoren:**
    - Volllast: ca. 30 %
    - Teillast: 10–15 %
  - **Dieselmotoren:**
    - Volllast: ca. 35 %
    - Teillast: 15–20 %
- **Einflussfaktoren:**
  - Lastzustand
  - Motortechnologie
  - Betriebsbedingungen

---

### 3. **Kraftstoffverbrauch**

#### a) **Kraftstoffmassenstrom ($\dot{m}_{\text{B}}$)**

- **Formel:**
  $$
  \dot{m}_{\text{B}} = \frac{P_{\text{Motor}}}{\eta_{\text{e}} \cdot H_{\text{U}}}
  $$
- **Parameter:**
  - **Heizwert des Kraftstoffs ($H_{\text{U}}$)**
    - Benzin: ca. $42\,000~\text{kJ/kg}$
    - Diesel: ca. $42\,600~\text{kJ/kg}$
- **Einfluss:**
  - Höherer Wirkungsgrad reduziert den Kraftstoffverbrauch
  - Niedrigere Motorleistung reduziert $\dot{m}_{\text{B}}$

#### b) **Streckenbezogener Kraftstoffverbrauch ($V_{\text{S}}$)**

- **Formel:**
  $$
  V_{\text{S}} = \frac{\dot{m}_{\text{B}}}{\rho_{\text{B}}} \cdot \frac{100~\text{km}}{v}
  $$
- **Parameter:**
  - **Kraftstoffdichte ($\rho_{\text{B}}$)**
    - Benzin: ca. $0{,}76~\text{kg/l}$
    - Diesel: ca. $0{,}84~\text{kg/l}$
- **Einflussfaktoren:**
  - Fahrgeschwindigkeit
  - Fahrwiderstände
  - Motorwirkungsgrad

---

### 4. **Effizienz im Stadtverkehr** (Aufgabe 7)

- **Charakteristika des Stadtverkehrs:**
  - Niedrige Durchschnittsgeschwindigkeit
  - Häufiges Anhalten und Anfahren
  - Hoher Anteil an Leerlaufzeiten
- **Auswirkungen auf die Effizienz:**
  - Motor arbeitet im ineffizienten Teillastbereich
  - Effektiver Wirkungsgrad sinkt auf 10–15 % (Ottomotoren)
- **Verluste:**
  - Drosselverluste bei Ottomotoren
  - Hohe Leerlaufverluste
  - Häufige Beschleunigungs- und Bremsvorgänge
- **Maßnahmen zur Effizienzsteigerung:**
  - Start-Stopp-Systeme
  - Hybridisierung
  - Rekuperation von Bremsenergie
  - Optimierung der Motorsteuerung

---

### 5. **Realisierung eines Verbrauchs von 1 l/100 km** (Aufgabe 6)

- **Anforderungen:**
  - Extrem niedriger Luft- und Rollwiderstand
  - Sehr leichte Fahrzeugmasse
  - Hocheffiziente Antriebstechnologie
- **Technische Maßnahmen:**
  - Verwendung von Leichtbaumaterialien (z. B. CFK)
  - Aerodynamische Optimierung (niedriger $c_{\text{w}}$-Wert)
  - Reduzierung der Stirnfläche
  - Effiziente Motoren oder alternative Antriebe
- **Herausforderungen:**
  - Kompromisse bei Komfort und Sicherheit
  - Hohe Entwicklungskosten
- **Beispiele:**
  - Konzeptfahrzeuge wie der Volkswagen XL1

---

### 6. **Typische Zahlenwerte und Berechnungsbeispiele** (Aufgabe 5)

- **Luftwiderstandsbeiwert ($c_{\text{w}}$)**: 0,25–0,35
- **Stirnfläche ($A$)**: 2,0–2,5 m²
- **Rollwiderstandsbeiwert ($\mu$)**: 0,010–0,015
- **Getriebewirkungsgrad ($\eta_{\text{Getriebe}}$)**: 0,90–0,95
- **Effektiver Motorwirkungsgrad ($\eta_{\text{e}}$)**:
  - Ottomotor: ca. 30 % bei Volllast
  - Dieselmotor: ca. 35 % bei Volllast
- **Anwendung in Berechnungen:**
  - **Aufgabe 1** und **2**: Berechnung der Motorleistung und des Verbrauchs bei 180 km/h
  - **Aufgabe 3**: Berechnung bei 50 km/h
  - **Aufgabe 4**: Vergleich der Bedeutung von Roll- und Luftwiderstand

---

### 7. **Optimierungsmöglichkeiten**

#### a) **Reduzierung des Luftwiderstands**

- **Maßnahmen:**
  - Aerodynamisches Fahrzeugdesign
  - Glatte Oberflächen
  - Abdeckungen für Räder
- **Effekte:**
  - Senkung des $c_{\text{w}}$-Werts
  - Reduzierung des Leistungsbedarfs bei hohen Geschwindigkeiten

#### b) **Reduzierung des Rollwiderstands**

- **Maßnahmen:**
  - Verwendung von Niedrigrollwiderstandsreifen
  - Richtiger Reifendruck
  - Leichtbauweise
- **Effekte:**
  - Geringerer Kraftstoffverbrauch bei allen Geschwindigkeiten
  - Besonders effektiv im Stadtverkehr

#### c) **Verbesserung des Motorwirkungsgrads**

- **Technologien:**
  - Effizientere Verbrennungsmotoren
  - Hybridantriebe
  - Elektrifizierung
- **Effekte:**
  - Reduzierung des Kraftstoffverbrauchs
  - Senkung der Emissionen

---

### 8. **Zusammenhänge und Schlussfolgerungen**

- **Geschwindigkeitsabhängigkeit:**
  - Luftwiderstand steigt quadratisch mit der Geschwindigkeit
  - Rollwiderstand bleibt konstant
- **Einfluss auf den Verbrauch:**
  - Hohe Geschwindigkeiten führen zu höherem Verbrauch
  - Effizientes Fahren kann den Verbrauch senken
- **Bedeutung der Fahrwiderstände:**
  - Entscheidend für die Dimensionierung des Antriebs
  - Wichtig für die Fahrzeugentwicklung und -optimierung

---

### 9. **Anwendung in den Aufgaben**

- **Aufgabe 1:** Berechnung der Motorleistung bei 180 km/h
- **Aufgabe 2:** Berechnung des Kraftstoffverbrauchs bei 180 km/h
- **Aufgabe 3:** Bestimmung der Motorleistung und des Wirkungsgrads bei 50 km/h
- **Aufgabe 4:** Analyse der Bedeutung von Roll- und Luftwiderstand
- **Aufgabe 5:** Bereitstellung typischer Zahlenwerte für Berechnungen
- **Aufgabe 6:** Diskussion der Realisierbarkeit eines Verbrauchs von 1 l/100 km
- **Aufgabe 7:** Untersuchung der Effizienz von Pkw-Motoren im Stadtverkehr

---

### 10. **Fachbegriffe und Symbole**

- **$F_{\text{roll}}$**: Rollwiderstandskraft
- **$F_{\text{cw}}$**: Luftwiderstandskraft
- **$F_{\text{steig}}$**: Steigungswiderstandskraft
- **$P_{\text{Rad}}$**: Radleistung
- **$P_{\text{Motor}}$**: Motorleistung
- **$\mu$ (Mu)**: Rollwiderstandsbeiwert
- **$c_{\text{w}}$**: Luftwiderstandsbeiwert
- **$\eta_{\text{Getriebe}}$ (Eta)**: Getriebewirkungsgrad
- **$\eta_{\text{e}}$ (Eta)**: Effektiver Motorwirkungsgrad
- **$H_{\text{U}}$**: Heizwert des Kraftstoffs
- **$\rho$ (Rho)**: Luftdichte
- **$A$**: Stirnfläche
- **$v$**: Geschwindigkeit
- **$m$**: Fahrzeugmasse
- **$g$**: Erdbeschleunigung
- **$\beta$ (Beta)**: Steigungswinkel
