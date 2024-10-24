---
title: "KAWA"
author: "Jan Unger"
date: "2024-10-24"
---

# KAWA

Letzte Aktualisierung: 2024-10-24

Quelle: Basiswissen Verbrennungsmotor, Fragen – rechnen – verstehen – bestehen (Schreiner 2020)

## Hauptthema: Fahrwiderstand und Motorleistung

---

### Wissensbausteine:

1. **Fahrwiderstände**

   - **Rollwiderstand ($F_{\text{roll}}$)**

     - **Formel:**
       $$
       F_{\text{roll}} = \mu \cdot m \cdot g
       $$
     - **Parameter:**
       - **Rollwiderstandsbeiwert ($\mu$)**
         - Typische Werte: 0,010–0,015
         - Abhängig von Reifentyp, Reifendruck, Straßenbeschaffenheit
       - **Fahrzeugmasse ($m$)**
         - Größere Masse erhöht $F_{\text{roll}}$
       - **Erdbeschleunigung ($g$)**
         - Konstant: $9{,}81~\text{m/s}^2$
     - **Eigenschaften:**
       - Unabhängig von der Geschwindigkeit
       - Dominant bei niedrigen Geschwindigkeiten
     - **Maßnahmen zur Reduzierung:**
       - Verwendung von Energiesparreifen
       - Optimierung des Reifendrucks
       - Gewichtsreduktion durch Leichtbau

   - **Luftwiderstand ($F_{\text{cw}}$)**

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

   - **Steigungswiderstand ($F_{\text{steig}}$)**

     - **Formel:**
       $$
       F_{\text{steig}} = m \cdot g \cdot \sin \beta
       $$
     - **Parameter:**
       - **Steigungswinkel ($\beta$)**
         - Relevant bei Fahrten in hügeligem Gelände
     - **Eigenschaften:**
       - Beeinflusst den Leistungsbedarf bei Steigungen
       - Nicht relevant auf ebener Strecke ($\beta = 0^\circ$)

2. **Motorleistung und Leistungsbedarf**

   - **Radleistung ($P_{\text{Rad}}$)**

     - **Formel:**
       $$
       P_{\text{Rad}} = F_{\text{ges}} \cdot v
       $$
     - **Gesamtwiderstandskraft ($F_{\text{ges}}$)**
       - Summe der einzelnen Widerstände:
         $$
         F_{\text{ges}} = F_{\text{roll}} + F_{\text{cw}} + F_{\text{steig}}
         $$

   - **Motorleistung ($P_{\text{Motor}}$)**

     - **Formel:**
       $$
       P_{\text{Motor}} = \frac{P_{\text{Rad}}}{\eta_{\text{Getriebe}}}
       $$
     - **Getriebewirkungsgrad ($\eta_{\text{Getriebe}}$)**
       - Berücksichtigt Verluste im Antriebsstrang
       - Typische Werte: 0,90–0,95

3. **Effektiver Motorwirkungsgrad ($\eta_{\text{e}}$)**

   - **Definition:**
     - Anteil der im Kraftstoff enthaltenen Energie, der in mechanische Arbeit umgewandelt wird
   - **Typische Werte:**
     - **Ottomotoren:**
       - Volllast: ca. 30%
       - Teillast: 10–15%
     - **Dieselmotoren:**
       - Volllast: ca. 35%
       - Teillast: 15–20%
   - **Einflussfaktoren:**
     - Lastzustand des Motors
     - Motortechnologie
     - Betriebsbedingungen

4. **Kraftstoffverbrauch**

   - **Kraftstoffmassenstrom ($\dot{m}_{\text{B}}$)**

     - **Formel:**
       $$
       \dot{m}_{\text{B}} = \frac{P_{\text{Motor}}}{\eta_{\text{e}} \cdot H_{\text{U}}}
       $$
     - **Heizwert des Kraftstoffs ($H_{\text{U}}$)**
       - Benzin: ca. $42\,000~\text{kJ/kg}$
       - Diesel: ca. $42\,600~\text{kJ/kg}$

   - **Streckenbezogener Verbrauch ($V_{\text{S}}$)**

     - **Berechnung:**
       - Umrechnung des Kraftstoffmassenstroms in Volumenverbrauch
       - Berücksichtigung der Kraftstoffdichte
       - Angabe in Litern pro 100 km

5. **Geschwindigkeitsabhängigkeit der Widerstände**

   - **Rollwiderstand ($F_{\text{roll}}$)**
     - Konstant über die Geschwindigkeit
     - Relevanter bei niedrigen Geschwindigkeiten
   - **Luftwiderstand ($F_{\text{cw}}$)**
     - Steigt quadratisch mit der Geschwindigkeit
     - Dominant bei hohen Geschwindigkeiten
   - **Grafische Darstellung:**
     - Diagramm mit Widerstandskräften in Abhängigkeit von der Geschwindigkeit

6. **Effizienz im Stadtverkehr (Aufgabe 7)**

   - **Herausforderungen:**
     - Häufiges Anfahren und Bremsen
     - Teillastbetrieb des Motors
     - Leerlaufverluste
     - Zusätzliche Verbraucher (Klimaanlage, Heizung)
   - **Auswirkungen:**
     - Niedriger effektiver Motorwirkungsgrad (10–15% bei Ottomotoren)
     - Erhöhter Kraftstoffverbrauch
   - **Maßnahmen zur Verbesserung:**
     - Start-Stopp-Systeme
     - Hybridisierung (Rekuperation von Bremsenergie)
     - Effiziente Motorsteuerung
     - Leichtbauweise zur Reduzierung der Fahrzeugmasse

7. **Realisierung eines Verbrauchs von 1 l/100 km (Aufgabe 6)**

   - **Anforderungen:**
     - Extrem niedriger Luft- und Rollwiderstand
     - Sehr geringer Fahrzeugmasse
     - Hocheffiziente Antriebe (z. B. Elektroantrieb)
   - **Technische Maßnahmen:**
     - Verwendung von Leichtbaumaterialien (CFK, Aluminium)
     - Aerodynamische Optimierung (niedriger $c_{\text{w}}$-Wert)
     - Einsatz von Hybrid- oder Elektroantrieben mit hoher Effizienz
   - **Praktische Beispiele:**
     - Konzeptfahrzeuge wie der Volkswagen XL1

8. **Typische Zahlenwerte für Berechnungen (Aufgabe 5)**

   - **Luftwiderstandsbeiwert ($c_{\text{w}}$)**: 0,25–0,35
   - **Stirnfläche ($A$)**: 2,0–2,5 m²
   - **Rollwiderstandsbeiwert ($\mu$)**: 0,010–0,015
   - **Getriebewirkungsgrad ($\eta_{\text{Getriebe}}$)**: 0,90–0,95
   - **Effektiver Motorwirkungsgrad ($\eta_{\text{e}}$)**:
     - Ottomotor: ca. 30% bei Volllast
     - Dieselmotor: ca. 35% bei Volllast

9. **Berechnungsbeispiele**

   - **Aufgabe 1: Motorleistung bei 180 km/h**
     - Hoher Luftwiderstand dominiert
     - Erforderliche Motorleistung steigt stark an
   - **Aufgabe 2: Kraftstoffverbrauch bei 180 km/h**
     - Hoher Verbrauch aufgrund des hohen Leistungsbedarfs
     - Effektiver Wirkungsgrad spielt wichtige Rolle
   - **Aufgabe 3: Motorleistung und Wirkungsgrad bei 50 km/h**
     - Rollwiderstand relevanter als Luftwiderstand
     - Niedriger Wirkungsgrad im Teillastbereich

10. **Optimierungsmöglichkeiten**

    - **Reduzierung des Luftwiderstands**
      - Aerodynamische Fahrzeugform
      - Reduzierung der Stirnfläche
      - Verwendung von Spoilern und Luftleitelementen
    - **Reduzierung des Rollwiderstands**
      - Energiesparreifen mit niedrigem $\mu$
      - Regelmäßige Kontrolle des Reifendrucks
      - Leichtbau zur Gewichtsreduktion
    - **Verbesserung des Motorwirkungsgrads**
      - Moderne Verbrennungstechnologien
      - Elektrifizierung des Antriebsstrangs
      - Hybridisierung und Nutzung von Rekuperation
