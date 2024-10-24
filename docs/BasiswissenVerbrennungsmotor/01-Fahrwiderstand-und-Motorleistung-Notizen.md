---
title: "Fahrwiderstand und Motorleistung"
author: "Jan Unger"
date: "2024-10-24"
---

# Fahrwiderstand und Motorleistung

Letzte Aktualisierung: 2024-10-24

Quelle: Basiswissen Verbrennungsmotor, Fragen – rechnen – verstehen – bestehen (Schreiner 2020)

## Inhaltsverzeichnis

- [Fahrwiderstand und Motorleistung](#fahrwiderstand-und-motorleistung)
  - [Inhaltsverzeichnis](#inhaltsverzeichnis)
- [Zusammenfassung von Kapitel 1: Fahrwiderstand und Motorleistung](#zusammenfassung-von-kapitel-1-fahrwiderstand-und-motorleistung)
  - [Leistungsbedarf eines Fahrzeugs](#leistungsbedarf-eines-fahrzeugs)
  - [Berechnung der erforderlichen Motorleistung](#berechnung-der-erforderlichen-motorleistung)
  - [Beispiel: Berechnung für die A-Klasse bei 180 km/h](#beispiel-berechnung-für-die-a-klasse-bei-180-kmh)
  - [Kraftstoffverbrauch bei hoher Geschwindigkeit](#kraftstoffverbrauch-bei-hoher-geschwindigkeit)
  - [Einfluss der Geschwindigkeit auf den Leistungsbedarf](#einfluss-der-geschwindigkeit-auf-den-leistungsbedarf)
  - [Reduzierung des Kraftstoffverbrauchs: Das 1-Liter-Auto](#reduzierung-des-kraftstoffverbrauchs-das-1-liter-auto)
  - [Wirkungsgrad im Stadtverkehr](#wirkungsgrad-im-stadtverkehr)
- [Liste der 7 Fragen aus Kapitel 1](#liste-der-7-fragen-aus-kapitel-1)
- [Welche Leistung benötigt die A-Klasse bei einer Geschwindigkeit von (180~\\text{km/h})?](#welche-leistung-benötigt-die-a-klasse-bei-einer-geschwindigkeit-von-180textkmh)
  - [Gegebene Werte](#gegebene-werte)
  - [Berechnung der Luftdichte $\\rho$](#berechnung-der-luftdichte-rho)
  - [Berechnung der Luftwiderstandskraft $F\_\\text{cw}$](#berechnung-der-luftwiderstandskraft-f_textcw)
  - [Berechnung der Rollwiderstandskraft $F\_\\text{roll}$](#berechnung-der-rollwiderstandskraft-f_textroll)
  - [Berechnung der gesamten Widerstandskraft $F\_\\text{ges}$](#berechnung-der-gesamten-widerstandskraft-f_textges)
  - [Berechnung der Radleistung $P\_\\text{Rad}$](#berechnung-der-radleistung-p_textrad)
  - [Berücksichtigung des Getriebewirkungsgrads](#berücksichtigung-des-getriebewirkungsgrads)
  - [Ergebnis](#ergebnis)
  - [Zusammenfassung](#zusammenfassung)
- [Erklärung der Aufgabe 1](#erklärung-der-aufgabe-1)
  - [Ziel der Aufgabe](#ziel-der-aufgabe)
  - [Hintergrundinformationen](#hintergrundinformationen)
  - [Gegebene Werte und Parameter](#gegebene-werte-und-parameter)
  - [Vorgehensweise zur Lösung](#vorgehensweise-zur-lösung)
  - [Relevante Formeln](#relevante-formeln)
  - [Ziel der Berechnung](#ziel-der-berechnung)
  - [Bedeutung der Aufgabe](#bedeutung-der-aufgabe)
  - [Zusammenfassung](#zusammenfassung-1)
- [Wie groß ist der Benzinverbrauch in $\\text{l}/(100,\\text{km})$ bei $180~\\text{km/h}$?](#wie-groß-ist-der-benzinverbrauch-intextl100textkm-bei-180textkmh)
  - [Ziel der Aufgabe](#ziel-der-aufgabe-1)
  - [Hintergrundinformationen](#hintergrundinformationen-1)
  - [Vorgehensweise zur Lösung](#vorgehensweise-zur-lösung-1)
  - [Relevante Formeln](#relevante-formeln-1)
  - [Bedeutung der Aufgabe](#bedeutung-der-aufgabe-1)
  - [Ziel der Berechnung](#ziel-der-berechnung-1)
  - [Zusammenfassung](#zusammenfassung-2)
- [Erklärung der Aufgabe 2](#erklärung-der-aufgabe-2)
  - [Ziel der Aufgabe](#ziel-der-aufgabe-2)
  - [Hintergrundinformationen](#hintergrundinformationen-2)
  - [Vorgehensweise zur Lösung](#vorgehensweise-zur-lösung-2)
  - [Relevante Formeln](#relevante-formeln-2)
  - [Bedeutung der Aufgabe](#bedeutung-der-aufgabe-2)
  - [Ziel der Berechnung](#ziel-der-berechnung-2)
  - [Zusammenfassung](#zusammenfassung-3)
- [Welche Leistung wird bei einer Geschwindigkeit von $50~\\text{km/h}$ benötigt? Wie groß ist dann der effektive Motorwirkungsgrad, wenn der Benzinverbrauch $5~\\text{l}/(100~\\text{km})$ beträgt?](#welche-leistung-wird-bei-einer-geschwindigkeit-von-50textkmh-benötigt-wie-groß-ist-dann-der-effektive-motorwirkungsgrad-wenn-der-benzinverbrauch-5textl100textkm-beträgt)
  - [Gegebene Werte](#gegebene-werte-1)
  - [1. Berechnung der Luftwiderstandskraft $F\_{\\text{cw}}$](#1-berechnung-der-luftwiderstandskraft-f_textcw)
  - [2. Berechnung der Rollwiderstandskraft $F\_{\\text{roll}}$](#2-berechnung-der-rollwiderstandskraft-f_textroll)
  - [3. Berechnung der Gesamtwiderstandskraft $F\_{\\text{ges}}$](#3-berechnung-der-gesamtwiderstandskraft-f_textges)
  - [4. Berechnung der Radleistung $P\_{\\text{Rad}}$](#4-berechnung-der-radleistung-p_textrad)
  - [5. Berechnung der erforderlichen Motorleistung $P\_{\\text{Motor}}$](#5-berechnung-der-erforderlichen-motorleistung-p_textmotor)
  - [6. Berechnung des effektiven Motorwirkungsgrades $\\eta\_{\\text{e}}$](#6-berechnung-des-effektiven-motorwirkungsgrades-eta_texte)
    - [a) Berechnung des Kraftstoffvolumenstroms $\\dot{V}\_{\\text{B}}$](#a-berechnung-des-kraftstoffvolumenstroms-dotv_textb)
    - [b) Umrechnung in Kraftstoffmassenstrom $\\dot{m}\_{\\text{B}}$](#b-umrechnung-in-kraftstoffmassenstrom-dotm_textb)
    - [c) Umrechnung des Massenstroms in $\\frac{\\text{kg}}{\\text{s}}$](#c-umrechnung-des-massenstroms-in-fractextkgtexts)
    - [d) Berechnung der zugeführten Brennstoffleistung $\\dot{Q}\_{\\text{B}}$](#d-berechnung-der-zugeführten-brennstoffleistung-dotq_textb)
    - [e) Berechnung des effektiven Motorwirkungsgrades $\\eta\_{\\text{e}}$](#e-berechnung-des-effektiven-motorwirkungsgrades-eta_texte)
  - [Zusammenfassung](#zusammenfassung-4)
- [Erklärung der Aufgabe 3](#erklärung-der-aufgabe-3)
  - [Ziel der Aufgabe](#ziel-der-aufgabe-3)
  - [Hintergrundinformationen](#hintergrundinformationen-3)
    - [Teil 1: Berechnung der Motorleistung bei $50~\\text{km/h}$](#teil-1-berechnung-der-motorleistung-bei-50textkmh)
    - [Teil 2: Bestimmung des effektiven Motorwirkungsgrads](#teil-2-bestimmung-des-effektiven-motorwirkungsgrads)
  - [Gegebene Werte und Parameter](#gegebene-werte-und-parameter-1)
  - [Bedeutung der Aufgabe](#bedeutung-der-aufgabe-3)
  - [Ziel der Berechnung](#ziel-der-berechnung-3)
  - [Relevante Formeln](#relevante-formeln-3)
    - [Rollwiderstandskraft](#rollwiderstandskraft)
    - [Luftwiderstandskraft](#luftwiderstandskraft)
    - [Gesamtwiderstandskraft](#gesamtwiderstandskraft)
    - [Radleistung](#radleistung)
    - [Motorleistung](#motorleistung)
    - [Kraftstoffverbrauch und Wirkungsgrad](#kraftstoffverbrauch-und-wirkungsgrad)
  - [Zusammenfassung](#zusammenfassung-5)
- [Was ist beim Pkw wichtiger: der Rollwiderstand oder der Luftwiderstand?](#was-ist-beim-pkw-wichtiger-der-rollwiderstand-oder-der-luftwiderstand)
  - [Ziel der Aufgabe](#ziel-der-aufgabe-4)
  - [Hintergrundinformationen](#hintergrundinformationen-4)
  - [Vorgehensweise zur Lösung](#vorgehensweise-zur-lösung-3)
  - [Schritt-für-Schritt-Lösung](#schritt-für-schritt-lösung)
    - [1. Gegebene Werte und Annahmen](#1-gegebene-werte-und-annahmen)
    - [2. Berechnung der Rollwiderstandskraft ($F\_{\\text{roll}}$)](#2-berechnung-der-rollwiderstandskraft-f_textroll-1)
    - [3. Berechnung der Luftwiderstandskraft ($F\_{\\text{cw}}$) bei verschiedenen Geschwindigkeiten](#3-berechnung-der-luftwiderstandskraft-f_textcw-bei-verschiedenen-geschwindigkeiten)
      - [Umrechnung der Geschwindigkeit in m/s](#umrechnung-der-geschwindigkeit-in-ms)
      - [Berechnungen](#berechnungen)
    - [4. Vergleich der Kräfte](#4-vergleich-der-kräfte)
    - [5. Analyse der Ergebnisse](#5-analyse-der-ergebnisse)
    - [6. Grafische Darstellung (optional)](#6-grafische-darstellung-optional)
    - [7. Schlussfolgerung](#7-schlussfolgerung)
  - [Antwort auf die Frage](#antwort-auf-die-frage)
  - [Zusammenfassung](#zusammenfassung-6)
- [Erklärung der Aufgabe 4](#erklärung-der-aufgabe-4)
  - [Ziel der Aufgabe](#ziel-der-aufgabe-5)
  - [Hintergrundinformationen](#hintergrundinformationen-5)
    - [Fahrwiderstände beim Pkw](#fahrwiderstände-beim-pkw)
    - [Bedeutung der Widerstände](#bedeutung-der-widerstände)
  - [Relevanz der Frage](#relevanz-der-frage)
  - [Ziel der Untersuchung](#ziel-der-untersuchung)
  - [Vorgehensweise zur Beantwortung der Frage](#vorgehensweise-zur-beantwortung-der-frage)
  - [Relevante Formeln](#relevante-formeln-4)
    - [Rollwiderstandskraft](#rollwiderstandskraft-1)
    - [Luftwiderstandskraft](#luftwiderstandskraft-1)
  - [Interpretation der Formeln](#interpretation-der-formeln)
  - [Praktische Umsetzung](#praktische-umsetzung)
    - [Auswahl typischer Werte](#auswahl-typischer-werte)
    - [Berechnung der Widerstandskräfte](#berechnung-der-widerstandskräfte)
      - [Rollwiderstandskraft](#rollwiderstandskraft-2)
      - [Luftwiderstandskraft bei verschiedenen Geschwindigkeiten](#luftwiderstandskraft-bei-verschiedenen-geschwindigkeiten)
  - [Ergebnisse und Interpretation](#ergebnisse-und-interpretation)
  - [Bedeutung für das Fahrverhalten](#bedeutung-für-das-fahrverhalten)
  - [Maßnahmen zur Reduzierung der Widerstände](#maßnahmen-zur-reduzierung-der-widerstände)
    - [Reduzierung des Rollwiderstands](#reduzierung-des-rollwiderstands)
    - [Reduzierung des Luftwiderstands](#reduzierung-des-luftwiderstands)
  - [Zusammenfassung](#zusammenfassung-7)
  - [Antwort auf die Frage](#antwort-auf-die-frage-1)
- [Was sind typische Zahlenwerte, um den Leistungsbedarf eines Pkw zu berechnen?](#was-sind-typische-zahlenwerte-um-den-leistungsbedarf-eines-pkw-zu-berechnen)
  - [Ziel der Aufgabe](#ziel-der-aufgabe-6)
  - [Hintergrundinformationen](#hintergrundinformationen-6)
  - [Typische Zahlenwerte für Pkw](#typische-zahlenwerte-für-pkw)
    - [1. Luftwiderstandsbeiwert ($c\_{\\text{w}}$)](#1-luftwiderstandsbeiwert-c_textw)
    - [2. Stirnfläche des Fahrzeugs ($A$)](#2-stirnfläche-des-fahrzeugs-a)
    - [3. Rollwiderstandsbeiwert ($\\mu$)](#3-rollwiderstandsbeiwert-mu)
    - [4. Getriebewirkungsgrad ($\\eta\_{\\text{Getriebe}}$)](#4-getriebewirkungsgrad-eta_textgetriebe)
    - [5. Effektiver Motorwirkungsgrad ($\\eta\_{\\text{e}}$)](#5-effektiver-motorwirkungsgrad-eta_texte)
    - [6. Weitere wichtige Größen](#6-weitere-wichtige-größen)
    - [7. Luftdichte ($\\rho$)](#7-luftdichte-rho)
  - [Bedeutung dieser Werte für die Berechnung](#bedeutung-dieser-werte-für-die-berechnung)
  - [Beispielrechnung (optional)](#beispielrechnung-optional)
  - [Zusammenfassung](#zusammenfassung-8)
- [Erklärung der Aufgabe 5](#erklärung-der-aufgabe-5)
  - [Ziel der Aufgabe](#ziel-der-aufgabe-7)
  - [Hintergrundinformationen](#hintergrundinformationen-7)
  - [Bedeutung der typischen Zahlenwerte](#bedeutung-der-typischen-zahlenwerte)
  - [Typische Zahlenwerte für die Berechnung des Leistungsbedarfs](#typische-zahlenwerte-für-die-berechnung-des-leistungsbedarfs)
    - [1. **Luftwiderstandsbeiwert ($c\_{\\text{w}}$)**](#1-luftwiderstandsbeiwert-c_textw-1)
    - [2. **Stirnfläche des Fahrzeugs ($A$)**](#2-stirnfläche-des-fahrzeugs-a-1)
    - [3. **Rollwiderstandsbeiwert ($\\mu$)**](#3-rollwiderstandsbeiwert-mu-1)
    - [4. **Getriebewirkungsgrad ($\\eta\_{\\text{Getriebe}}$)**](#4-getriebewirkungsgrad-eta_textgetriebe-1)
    - [5. **Effektiver Motorwirkungsgrad ($\\eta\_{\\text{e}}$)**](#5-effektiver-motorwirkungsgrad-eta_texte-1)
    - [6. **Luftdichte ($\\rho$)**](#6-luftdichte-rho)
    - [7. **Erdbeschleunigung ($g$)**](#7-erdbeschleunigung-g)
    - [8. **Fahrzeugmasse ($m$)**](#8-fahrzeugmasse-m)
  - [Anwendung dieser Werte in den Berechnungen](#anwendung-dieser-werte-in-den-berechnungen)
    - [**1. Luftwiderstandskraft ($F\_{\\text{cw}}$)**](#1-luftwiderstandskraft-f_textcw)
    - [**2. Rollwiderstandskraft ($F\_{\\text{roll}}$)**](#2-rollwiderstandskraft-f_textroll)
    - [**3. Gesamtwiderstandskraft ($F\_{\\text{ges}}$)**](#3-gesamtwiderstandskraft-f_textges)
    - [**4. Erforderliche Motorleistung ($P\_{\\text{Motor}}$)**](#4-erforderliche-motorleistung-p_textmotor)
    - [**5. Kraftstoffverbrauch und Motorwirkungsgrad**](#5-kraftstoffverbrauch-und-motorwirkungsgrad)
  - [Beispielrechnung](#beispielrechnung)
  - [Zusammenfassung](#zusammenfassung-9)
- [Könnte man mit einem modernen Fahrzeug einen Kraftstoffverbrauch von $1~\\text{l}/(100~\\text{km})$ realisieren?](#könnte-man-mit-einem-modernen-fahrzeug-einen-kraftstoffverbrauch-von-1textl100textkm-realisieren)
  - [Ziel der Aufgabe](#ziel-der-aufgabe-8)
  - [Hintergrundinformationen](#hintergrundinformationen-8)
  - [Vorgehensweise zur Lösung](#vorgehensweise-zur-lösung-4)
  - [Schritt-für-Schritt-Lösung](#schritt-für-schritt-lösung-1)
    - [1. Festlegen der Fahrzeugparameter](#1-festlegen-der-fahrzeugparameter)
    - [2. Berechnung der Fahrwiderstände](#2-berechnung-der-fahrwiderstände)
      - [Umrechnung der Geschwindigkeiten in m/s](#umrechnung-der-geschwindigkeiten-in-ms)
      - [a) Rollwiderstandskraft ($F\_{\\text{roll}}$)](#a-rollwiderstandskraft-f_textroll)
      - [b) Luftwiderstandskraft ($F\_{\\text{cw}}$)](#b-luftwiderstandskraft-f_textcw)
    - [3. Berechnung der erforderlichen Radleistung ($P\_{\\text{Rad}}$)](#3-berechnung-der-erforderlichen-radleistung-p_textrad)
    - [4. Berücksichtigung der Wirkungsgrade](#4-berücksichtigung-der-wirkungsgrade)
    - [5. Berechnung des Kraftstoffverbrauchs](#5-berechnung-des-kraftstoffverbrauchs)
      - [a) Kraftstoffmassenstrom ($\\dot{m}\_{\\text{B}}$)](#a-kraftstoffmassenstrom-dotm_textb)
      - [b) Umrechnung in Verbrauch pro Stunde](#b-umrechnung-in-verbrauch-pro-stunde)
      - [c) Berechnung des streckenbezogenen Kraftstoffverbrauchs ($V\_{\\text{S}}$)](#c-berechnung-des-streckenbezogenen-kraftstoffverbrauchs-v_texts)
    - [6. Analyse der Ergebnisse](#6-analyse-der-ergebnisse)
    - [7. Notwendige technische Maßnahmen](#7-notwendige-technische-maßnahmen)
  - [Antwort auf die Frage](#antwort-auf-die-frage-2)
  - [Fazit](#fazit)
- [Erklärung der Aufgabe 6](#erklärung-der-aufgabe-6)
  - [Ziel der Aufgabe](#ziel-der-aufgabe-9)
  - [Hintergrundinformationen](#hintergrundinformationen-9)
    - [Bedeutung des Kraftstoffverbrauchs](#bedeutung-des-kraftstoffverbrauchs)
    - [Aktuelle Standards und Herausforderungen](#aktuelle-standards-und-herausforderungen)
  - [Faktoren, die den Kraftstoffverbrauch beeinflussen](#faktoren-die-den-kraftstoffverbrauch-beeinflussen)
  - [Theoretische Machbarkeit eines Verbrauchs von 1 l/100 km](#theoretische-machbarkeit-eines-verbrauchs-von-1l100km)
    - [Berechnungsgrundlagen](#berechnungsgrundlagen)
      - [1. **Rollwiderstandskraft ($F\_{\\text{roll}}$)**](#1-rollwiderstandskraft-f_textroll)
      - [2. **Luftwiderstandskraft ($F\_{\\text{cw}}$)**](#2-luftwiderstandskraft-f_textcw)
      - [3. **Gesamtwiderstandskraft ($F\_{\\text{ges}}$)**](#3-gesamtwiderstandskraft-f_textges-1)
      - [4. **Erforderliche Radleistung ($P\_{\\text{Rad}}$)**](#4-erforderliche-radleistung-p_textrad)
      - [5. **Erforderliche Motorleistung ($P\_{\\text{Motor}}$)**](#5-erforderliche-motorleistung-p_textmotor)
      - [6. **Kraftstoffverbrauch**](#6-kraftstoffverbrauch)
    - [Beispielrechnung](#beispielrechnung-1)
    - [Interpretation der Ergebnisse](#interpretation-der-ergebnisse)
  - [Praktische Herausforderungen](#praktische-herausforderungen)
  - [Alternative Ansätze zur Verbrauchsreduzierung](#alternative-ansätze-zur-verbrauchsreduzierung)
  - [Zusammenfassung](#zusammenfassung-10)
  - [Schlussfolgerung](#schlussfolgerung)
- [Wie effizient sind Pkw-Motoren im Stadtverkehr?](#wie-effizient-sind-pkw-motoren-im-stadtverkehr)
  - [Ziel der Aufgabe](#ziel-der-aufgabe-10)
  - [Hintergrundinformationen](#hintergrundinformationen-10)
    - [Motorwirkungsgrad ($\\eta\_{\\text{e}}$)](#motorwirkungsgrad-eta_texte)
    - [Stadtverkehrsbedingungen](#stadtverkehrsbedingungen)
  - [Faktoren, die die Effizienz im Stadtverkehr beeinflussen](#faktoren-die-die-effizienz-im-stadtverkehr-beeinflussen)
  - [Schritt-für-Schritt-Lösung](#schritt-für-schritt-lösung-2)
    - [1. Analyse des Motorwirkungsgrads im Stadtverkehr](#1-analyse-des-motorwirkungsgrads-im-stadtverkehr)
      - [a) Motorbetrieb im Teillastbereich](#a-motorbetrieb-im-teillastbereich)
      - [b) Einfluss der Fahrwiderstände](#b-einfluss-der-fahrwiderstände)
      - [c) Häufiges Anfahren und Bremsen](#c-häufiges-anfahren-und-bremsen)
    - [2. Quantitative Betrachtung](#2-quantitative-betrachtung)
      - [a) Beispielrechnung für einen Ottomotor im Stadtverkehr](#a-beispielrechnung-für-einen-ottomotor-im-stadtverkehr)
      - [b) Berechnung des Kraftstoffverbrauchs](#b-berechnung-des-kraftstoffverbrauchs)
      - [c) Realistischerer Ansatz](#c-realistischerer-ansatz)
    - [3. Schlussfolgerungen](#3-schlussfolgerungen)
  - [Antwort auf die Frage](#antwort-auf-die-frage-3)
  - [Zusammenfassung](#zusammenfassung-11)
- [Erklärung der Aufgabe 7](#erklärung-der-aufgabe-7)
  - [Ziel der Aufgabe](#ziel-der-aufgabe-11)
  - [Hintergrundinformationen](#hintergrundinformationen-11)
    - [Definition der Motoreneffizienz](#definition-der-motoreneffizienz)
    - [Charakteristika des Stadtverkehrs](#charakteristika-des-stadtverkehrs)
  - [Relevanz der Frage](#relevanz-der-frage-1)
  - [Faktoren, die die Motoreneffizienz im Stadtverkehr beeinflussen](#faktoren-die-die-motoreneffizienz-im-stadtverkehr-beeinflussen)
    - [1. Teillastbetrieb des Motors](#1-teillastbetrieb-des-motors)
    - [2. Häufiges Anfahren und Bremsen](#2-häufiges-anfahren-und-bremsen)
    - [3. Leerlaufverluste](#3-leerlaufverluste)
    - [4. Zusatzverbraucher](#4-zusatzverbraucher)
    - [5. Thermische Verluste](#5-thermische-verluste)
  - [Ziel der Untersuchung](#ziel-der-untersuchung-1)
  - [Methodik zur Beantwortung der Frage](#methodik-zur-beantwortung-der-frage)
  - [Detaillierte Betrachtung der Effizienz im Stadtverkehr](#detaillierte-betrachtung-der-effizienz-im-stadtverkehr)
    - [Berechnung der Energiebedarfe](#berechnung-der-energiebedarfe)
      - [Beispielannahmen:](#beispielannahmen)
      - [1. Energie für den Rollwiderstand pro km](#1-energie-für-den-rollwiderstand-pro-km)
      - [2. Energie für Beschleunigungsvorgänge pro km](#2-energie-für-beschleunigungsvorgänge-pro-km)
      - [3. Gesamter Energiebedarf pro km](#3-gesamter-energiebedarf-pro-km)
    - [Berechnung des Kraftstoffverbrauchs](#berechnung-des-kraftstoffverbrauchs)
      - [1. Zugeführte Kraftstoffenergie pro km](#1-zugeführte-kraftstoffenergie-pro-km)
      - [2. Annahme eines realen Verbrauchs](#2-annahme-eines-realen-verbrauchs)
      - [3. Berechnung des effektiven Motorwirkungsgrads](#3-berechnung-des-effektiven-motorwirkungsgrads)
      - [4. Realistischere Schätzung des Wirkungsgrads](#4-realistischere-schätzung-des-wirkungsgrads)
    - [Schlussfolgerungen aus der Berechnung](#schlussfolgerungen-aus-der-berechnung)
  - [Maßnahmen zur Steigerung der Effizienz im Stadtverkehr](#maßnahmen-zur-steigerung-der-effizienz-im-stadtverkehr)
    - [1. Start-Stopp-Systeme](#1-start-stopp-systeme)
    - [2. Hybridisierung](#2-hybridisierung)
    - [3. Rekuperation](#3-rekuperation)
    - [4. Optimierung der Motorsteuerung](#4-optimierung-der-motorsteuerung)
    - [5. Alternative Antriebskonzepte](#5-alternative-antriebskonzepte)
    - [6. Leichtbau und Aerodynamik](#6-leichtbau-und-aerodynamik)
  - [Bedeutung für die Fahrzeugentwicklung](#bedeutung-für-die-fahrzeugentwicklung)
  - [Zusammenfassung](#zusammenfassung-12)
  - [Antwort auf die Frage](#antwort-auf-die-frage-4)

# Zusammenfassung von Kapitel 1: Fahrwiderstand und Motorleistung

In diesem Kapitel wird erläutert, wie der Leistungsbedarf eines Kraftfahrzeugs berechnet wird und welche Kräfte dabei eine Rolle spielen. Verbrennungsmotoren werden in verschiedenen Anwendungen eingesetzt, von Rasenmähern bis zu Schiffen. Die Berechnungsmethoden sind dabei weitgehend identisch.

## Leistungsbedarf eines Fahrzeugs

Ein Fahrzeug, das mit konstanter Geschwindigkeit $v_{\text{Auto}}$ fährt, muss die Fahrwiderstandskräfte überwinden. Diese setzen sich aus der Luftwiderstandskraft $F_{\text{cw}}$, der Rollwiderstandskraft $F_{\text{roll}}$ und gegebenenfalls der Steigungskraft $F_{\text{steig}}$ zusammen:

- **Luftwiderstandskraft:**
  $$
  F_{\text{cw}} = \frac{1}{2} \cdot \rho \cdot v_{\text{Auto}}^2 \cdot c_{\text{w}} \cdot A
  $$
- **Rollwiderstandskraft:**
  $$
  F_{\text{roll}} = \mu \cdot m \cdot g \cdot \cos \beta
  $$
- **Steigungskraft:**
  $$
  F_{\text{steig}} = m \cdot g \cdot \sin \beta
  $$

Dabei sind $\rho$ die Luftdichte, $c_{\text{w}}$ der Luftwiderstandsbeiwert, $A$ die Stirnfläche, $\mu$ der Rollwiderstandsbeiwert, $m$ die Fahrzeugmasse, $g = 9{,}81~\text{m/s}^2$ die Erdbeschleunigung und $\beta$ der Steigungswinkel. Auf ebener Strecke entfällt die Steigungskraft ($\beta = 0^\circ$).

## Berechnung der erforderlichen Motorleistung

Die benötigte Vortriebsleistung $P_{\text{Rad}}$ am Rad ergibt sich aus der Summe der Fahrwiderstandskräfte multipliziert mit der Fahrzeuggeschwindigkeit:

$$
P_{\text{Rad}} = (F_{\text{cw}} + F_{\text{roll}} + F_{\text{steig}}) \cdot v_{\text{Auto}}
$$

Unter Berücksichtigung des Getriebewirkungsgrads $\eta_{\text{Getriebe}}$ wird die erforderliche Motorleistung $P_{\text{Motor}}$ berechnet:

$$
P_{\text{Motor}} = \frac{P_{\text{Rad}}}{\eta_{\text{Getriebe}}}
$$

## Beispiel: Berechnung für die A-Klasse bei 180 km/h

Anhand eines konkreten Beispiels wird die Berechnung der Motorleistung für eine Mercedes A-Klasse durchgeführt:

- **Gegebene Werte:**
  - $c_{\text{w}} = 0{,}31$
  - $A = 2{,}4~\text{m}^2$
  - $m = 1270~\text{kg}$
  - $\mu = 0{,}015$
  - $\eta_{\text{Getriebe}} = 0{,}92$

Die Luftdichte $\rho$ wird aus der idealen Gasgleichung berechnet:

$$
\rho = \frac{p}{R \cdot T}
$$

Mit diesen Werten ergibt sich eine erforderliche Motorleistung von etwa $75{,}6~\text{kW}$ bei einer konstanten Geschwindigkeit von $180~\text{km/h}$.

## Kraftstoffverbrauch bei hoher Geschwindigkeit

Der Kraftstoffverbrauch hängt vom effektiven Wirkungsgrad $\eta_{\text{e}}$ des Motors ab. Für einen Ottomotor bei Nennleistung kann ein Wirkungsgrad von etwa $30~\%$ angenommen werden. Der Kraftstoffmassenstrom $\dot{m}_{\text{B}}$ ergibt sich zu:

$$
\dot{m}_{\text{B}} = \frac{P_{\text{e}}}{\eta_{\text{e}} \cdot H_{\text{U}}}
$$

Dabei ist $H_{\text{U}}$ der Heizwert des Kraftstoffs. Der streckenbezogene Kraftstoffverbrauch $V_{\text{S}}$ bei $180~\text{km/h}$ beträgt somit etwa $15~\text{l}/100~\text{km}$.

## Einfluss der Geschwindigkeit auf den Leistungsbedarf

Der Leistungsbedarf zur Überwindung des Rollwiderstands steigt linear mit der Geschwindigkeit, während der Luftwiderstand in dritter Potenz zur Geschwindigkeit steigt. Bei niedrigen Geschwindigkeiten dominiert der Rollwiderstand, bei höheren Geschwindigkeiten der Luftwiderstand.

## Reduzierung des Kraftstoffverbrauchs: Das 1-Liter-Auto

Um einen Kraftstoffverbrauch von $1~\text{l}/100~\text{km}$ zu erreichen, sind erhebliche Fahrzeugoptimierungen notwendig:

- **Gewichtsreduktion:** Leichtbauweise zur Verringerung der Fahrzeugmasse.
- **Aerodynamik:** Senkung des Luftwiderstandsbeiwerts $c_{\text{w}}$ und der Stirnfläche $A$.
- **Rollwiderstand:** Verwendung von Reifen mit niedrigerem Rollwiderstandsbeiwert $\mu$.
- **Effiziente Antriebe:** Einsatz von Motoren mit höherem Wirkungsgrad $\eta_{\text{e}}$.

## Wirkungsgrad im Stadtverkehr

Im Stadtverkehr ist der Kraftstoffverbrauch trotz geringer Geschwindigkeiten hoch, da der Motor bei niedriger Last einen schlechten Wirkungsgrad aufweist. Zudem führen häufige Stop-and-Go-Situationen zu erhöhtem Verbrauch. Der Leerlaufverbrauch eines Ottomotors liegt bei etwa $1~\text{l}/\text{h}$, was bei niedrigen Geschwindigkeiten zu einem hohen spezifischen Verbrauch führt.

# Liste der 7 Fragen aus Kapitel 1

1. **Welche Leistung benötigt die A-Klasse bei einer Geschwindigkeit von 180 km/h?**
2. **Wie groß ist der Benzinverbrauch in l/(100 km) bei 180 km/h?**
3. **Welche Leistung wird bei einer Geschwindigkeit von 50 km/h benötigt? Wie groß ist dann der effektive Motorwirkungsgrad, wenn der Benzinverbrauch 5 l/(100 km) beträgt?**
4. **Was ist beim Pkw wichtiger: der Rollwiderstand oder der Luftwiderstand?**
5. **Was sind typische Zahlenwerte, um den Leistungsbedarf eines Pkw zu berechnen?**
6. **Könnte man mit einem modernen Fahrzeug einen Kraftstoffverbrauch von 1 l/(100 km) realisieren?**
7. **Wie effizient sind Pkw-Motoren im Stadtverkehr?**

# Welche Leistung benötigt die A-Klasse bei einer Geschwindigkeit von \(180~\text{km/h}\)?

## Gegebene Werte

- Luftwiderstandsbeiwert: $c_\text{w} = 0{,}31$
- Stirnfläche: $A = 2{,}4~\text{m}^2$
- Fahrzeugmasse: $m = 1270~\text{kg}$
- Rollwiderstandsbeiwert: $\mu = 0{,}015$
- Getriebewirkungsgrad: $\eta_\text{Getriebe} = 0{,}92$
- Fahrzeuggeschwindigkeit: $v_\text{Auto} = 180~\text{km/h} = 50~\text{m/s}$

## Berechnung der Luftdichte $\rho$

Die Luftdichte $\rho$ wird mithilfe der idealen Gasgleichung berechnet:

$$
\rho = \frac{p}{R \cdot T}
$$

Dabei sind:

- Luftdruck: $p = 101325~\text{Pa}$
- Gaskonstante für Luft: $R = 287~\frac{\text{J}}{\text{kg}~\text{K}}$
- Temperatur: $T = 288{,}15~\text{K}$ (entspricht \(15^\circ\text{C}\))

**Berechnung:**

$$
\rho = \frac{101325~\text{Pa}}{287~\frac{\text{J}}{\text{kg}~\text{K}} \cdot 288{,}15~\text{K}} = 1{,}225~\frac{\text{kg}}{\text{m}^3}
$$

## Berechnung der Luftwiderstandskraft $F_\text{cw}$

$$
F_\text{cw} = \frac{1}{2} \cdot \rho \cdot v_\text{Auto}^2 \cdot c_\text{w} \cdot A
$$

**Berechnung:**

$$
\begin{align*}
F_\text{cw} &= \frac{1}{2} \cdot 1{,}225~\frac{\text{kg}}{\text{m}^3} \cdot (50~\text{m/s})^2 \cdot 0{,}31 \cdot 2{,}4~\text{m}^2 \\
&= 0{,}5 \cdot 1{,}225 \cdot 2500 \cdot 0{,}31 \cdot 2{,}4 \\
&= 0{,}5 \cdot 1{,}225 \cdot 2500 \cdot 0{,}744 \\
&= 1137{,}75~\text{N}
\end{align*}
$$

## Berechnung der Rollwiderstandskraft $F_\text{roll}$

Da die Straße eben ist ($\beta = 0^\circ$), gilt $\cos 0^\circ = 1$.

$$
F_\text{roll} = \mu \cdot m \cdot g \cdot \cos \beta = \mu \cdot m \cdot g
$$

**Berechnung:**

$$
F_\text{roll} = 0{,}015 \cdot 1270~\text{kg} \cdot 9{,}81~\frac{\text{m}}{\text{s}^2} = 186{,}985~\text{N}
$$

## Berechnung der gesamten Widerstandskraft $F_\text{ges}$

$$
F_\text{ges} = F_\text{cw} + F_\text{roll} = 1137{,}75~\text{N} + 186{,}985~\text{N} = 1324{,}735~\text{N}
$$

## Berechnung der Radleistung $P_\text{Rad}$

$$
P_\text{Rad} = F_\text{ges} \cdot v_\text{Auto}
$$

**Berechnung:**

$$
P_\text{Rad} = 1324{,}735~\text{N} \cdot 50~\text{m/s} = 66\,236{,}75~\text{W} = 66{,}237~\text{kW}
$$

## Berücksichtigung des Getriebewirkungsgrads

$$
P_\text{Motor} = \frac{P_\text{Rad}}{\eta_\text{Getriebe}}
$$

**Berechnung:**

$$
P_\text{Motor} = \frac{66{,}237~\text{kW}}{0{,}92} = 71{,}999~\text{kW} \approx 72{,}0~\text{kW}
$$

## Ergebnis

Die A-Klasse benötigt bei einer Geschwindigkeit von \(180~\text{km/h}\) eine Motorleistung von etwa **72 kW**.

## Zusammenfassung

- **Luftwiderstandskraft:** $F_\text{cw} = 1137{,}75~\text{N}$
- **Rollwiderstandskraft:** $F_\text{roll} = 186{,}985~\text{N}$
- **Gesamtwiderstandskraft:** $F_\text{ges} = 1324{,}735~\text{N}$
- **Radleistung:** $P_\text{Rad} = 66{,}237~\text{kW}$
- **Motorleistung:** $P_\text{Motor} = 72{,}0~\text{kW}$

**Die erforderliche Motorleistung beträgt somit etwa 72 kW.**

# Erklärung der Aufgabe 1

**Frage:** *Welche Leistung benötigt die A-Klasse bei einer Geschwindigkeit von $180~\text{km/h}$?*

## Ziel der Aufgabe

Die Aufgabe besteht darin, die erforderliche Motorleistung zu berechnen, die ein Mercedes A-Klasse Fahrzeug aufbringen muss, um mit einer konstanten Geschwindigkeit von $180~\text{km/h}$ auf ebener Strecke zu fahren. Dabei müssen die verschiedenen Fahrwiderstände berücksichtigt werden, die dem Fahrzeug entgegenwirken und überwunden werden müssen.

## Hintergrundinformationen

Wenn ein Fahrzeug mit konstanter Geschwindigkeit fährt, muss ein Gleichgewicht zwischen den antreibenden und den widerstehenden Kräften bestehen. Die antreibende Kraft wird vom Motor bereitgestellt, während die widerstehenden Kräfte hauptsächlich aus folgenden Komponenten bestehen:

1. **Luftwiderstandskraft ($F_{\text{cw}}$)**: Entsteht durch die Luft, die das Fahrzeug verdrängen muss. Sie hängt von der Geschwindigkeit und der Aerodynamik des Fahrzeugs ab.

2. **Rollwiderstandskraft ($F_{\text{roll}}$)**: Resultiert aus der Verformung der Reifen und dem Rollwiderstand auf der Fahrbahnoberfläche.

3. **Steigungskraft ($F_{\text{steig}}$)**: Tritt auf, wenn das Fahrzeug eine Steigung hinauffährt. Da in dieser Aufgabe von einer ebenen Strecke ausgegangen wird, entfällt dieser Widerstand ($\beta = 0^\circ$).

Die Summe dieser Widerstandskräfte muss durch die Motorkraft kompensiert werden, um eine konstante Geschwindigkeit zu halten.

## Gegebene Werte und Parameter

Für die Berechnung stehen folgende Fahrzeugdaten und physikalische Konstanten zur Verfügung:

- **Fahrzeuggeschwindigkeit ($v_{\text{Auto}}$)**:
  $$
  v_{\text{Auto}} = 180~\text{km/h} = 50~\text{m/s}
  $$
  *(Umrechnung: $1~\text{km/h} = \frac{1}{3{,}6}~\text{m/s}$)*

- **Luftdichte ($\rho$)**: Unter Standardbedingungen (20 °C, 1 bar):
  $$
  \rho = 1{,}2041~\frac{\text{kg}}{\text{m}^3}
  $$

- **Luftwiderstandsbeiwert ($c_{\text{w}}$)**:
  $$
  c_{\text{w}} = 0{,}31
  $$

- **Stirnfläche des Fahrzeugs ($A$)**:
  $$
  A = 2{,}4~\text{m}^2
  $$

- **Fahrzeugmasse ($m$)**:
  $$
  m = 1270~\text{kg}
  $$

- **Rollwiderstandsbeiwert ($\mu$)**:
  $$
  \mu = 0{,}015
  $$

- **Erdbeschleunigung ($g$)**:
  $$
  g = 9{,}81~\frac{\text{m}}{\text{s}^2}
  $$

- **Getriebewirkungsgrad ($\eta_{\text{Getriebe}}$)**:
  $$
  \eta_{\text{Getriebe}} = 0{,}92
  $$

## Vorgehensweise zur Lösung

1. **Berechnung der Luftwiderstandskraft ($F_{\text{cw}}$)**:
   - Bestimmung der Kraft, die benötigt wird, um den Luftwiderstand bei gegebener Geschwindigkeit zu überwinden.

2. **Berechnung der Rollwiderstandskraft ($F_{\text{roll}}$)**:
   - Ermittlung der Kraft, die erforderlich ist, um den Rollwiderstand der Reifen zu überwinden.

3. **Berechnung der Gesamtwiderstandskraft ($F_{\text{ges}}$)**:
   - Addition von $F_{\text{cw}}$ und $F_{\text{roll}}$, da die Steigungskraft entfällt.

4. **Berechnung der Radleistung ($P_{\text{Rad}}$)**:
   - Multiplikation der Gesamtwiderstandskraft mit der Fahrzeuggeschwindigkeit.

5. **Anpassung für den Getriebewirkungsgrad**:
   - Division der Radleistung durch den Getriebewirkungsgrad, um die erforderliche Motorleistung zu erhalten.

## Relevante Formeln

1. **Luftwiderstandskraft**:
   $$
   F_{\text{cw}} = \frac{1}{2} \cdot \rho \cdot c_{\text{w}} \cdot A \cdot v_{\text{Auto}}^2
   $$

2. **Rollwiderstandskraft**:
   $$
   F_{\text{roll}} = \mu \cdot m \cdot g
   $$
   *(Da $\cos 0^\circ = 1$ und $\beta = 0^\circ$)*

3. **Gesamtwiderstandskraft**:
   $$
   F_{\text{ges}} = F_{\text{cw}} + F_{\text{roll}}
   $$

4. **Radleistung**:
   $$
   P_{\text{Rad}} = F_{\text{ges}} \cdot v_{\text{Auto}}
   $$

5. **Motorleistung**:
   $$
   P_{\text{Motor}} = \frac{P_{\text{Rad}}}{\eta_{\text{Getriebe}}}
   $$

## Ziel der Berechnung

- **Bestimmung der erforderlichen Motorleistung ($P_{\text{Motor}}$)**, um die A-Klasse bei $180~\text{km/h}$ konstant auf ebener Strecke zu bewegen.

## Bedeutung der Aufgabe

Die Berechnung ist wichtig, um zu verstehen, wie verschiedene Faktoren wie Aerodynamik, Fahrzeuggewicht und mechanische Verluste die erforderliche Motorleistung beeinflussen. Dies ist entscheidend für die Auslegung von Motoren und Antriebssträngen sowie für die Optimierung des Kraftstoffverbrauchs und der Emissionen.

## Zusammenfassung

Die Aufgabe erfordert eine schrittweise Berechnung unter Berücksichtigung physikalischer Prinzipien und Fahrzeugdaten. Durch das Verständnis der einzelnen Widerstandskräfte und ihrer Abhängigkeiten von Geschwindigkeit und Fahrzeugparametern kann die benötigte Motorleistung genau ermittelt werden.

**Ziel:** Ermittlung der Motorleistung $P_{\text{Motor}}$ für die A-Klasse bei $180~\text{km/h}$.

# Wie groß ist der Benzinverbrauch in $\text{l}/(100\,\text{km})$ bei $180~\text{km/h}$?

## Ziel der Aufgabe

Die Aufgabe besteht darin, den streckenbezogenen Kraftstoffverbrauch eines Fahrzeugs (hier: Mercedes A-Klasse) zu berechnen, wenn es mit einer konstanten Geschwindigkeit von $180~\text{km/h}$ fährt. Der Verbrauch soll in Litern pro 100 Kilometer ($\text{l}/(100~\text{km})$) angegeben werden.

## Hintergrundinformationen

Um den Kraftstoffverbrauch zu ermitteln, müssen wir verstehen, wie der Energiebedarf des Fahrzeugs mit dem Kraftstoffverbrauch zusammenhängt. Der Motor wandelt die chemische Energie des Kraftstoffs in mechanische Arbeit um, um die Fahrwiderstände zu überwinden. Dabei treten folgende wichtige Größen auf:

1. **Erforderliche Motorleistung ($P_{\text{Motor}}$)**: Die Leistung, die der Motor aufbringen muss, um die Fahrwiderstände bei $180~\text{km/h}$ zu überwinden. Diese Leistung wurde in der vorherigen Aufgabe berechnet und beträgt etwa $72{,}0~\text{kW}$.

2. **Effektiver Wirkungsgrad des Motors ($\eta_{\text{e}}$)**: Der Anteil der im Kraftstoff enthaltenen Energie, der tatsächlich in mechanische Arbeit umgewandelt wird. Bei einem Ottomotor kann bei Nennleistung ein Wirkungsgrad von etwa $30\,\%$ angenommen werden.

3. **Heizwert des Kraftstoffs ($H_{\text{U}}$)**: Die spezifische Energie, die bei der Verbrennung eines Kilogramms Kraftstoff freigesetzt wird. Für Ottokraftstoff beträgt der Heizwert $42\,000~\text{kJ}/\text{kg}$.

4. **Kraftstoffdichte ($\rho$)**: Die Dichte des Kraftstoffs, die benötigt wird, um den Massenstrom in einen Volumenstrom umzurechnen. Für Ottokraftstoff beträgt die Dichte $0{,}76~\text{kg}/\text{l}$.

## Vorgehensweise zur Lösung

Die Berechnung erfolgt in mehreren Schritten:

1. **Berechnung des Kraftstoffmassenstroms ($\dot{m}_{\text{B}}$)**:

   - Ermittlung, wie viel Kilogramm Kraftstoff pro Zeiteinheit verbrannt werden müssen, um die erforderliche Motorleistung zu erbringen.

2. **Umrechnung des Massenstroms in Volumenstrom ($\dot{V}_{\text{B}}$)**:

   - Verwendung der Kraftstoffdichte, um den Massenstrom in Liter pro Stunde umzurechnen.

3. **Berechnung des streckenbezogenen Kraftstoffverbrauchs ($V_{\text{S}}$)**:

   - Bestimmung des Kraftstoffverbrauchs pro 100 Kilometer basierend auf der gefahrenen Geschwindigkeit und dem Volumenstrom.

## Relevante Formeln

1. **Kraftstoffmassenstrom**:

   $$
   \dot{m}_{\text{B}} = \frac{P_{\text{Motor}}}{\eta_{\text{e}} \cdot H_{\text{U}}}
   $$

   - $P_{\text{Motor}}$: Motorleistung in Watt ($\text{W}$)
   - $\eta_{\text{e}}$: Effektiver Wirkungsgrad des Motors
   - $H_{\text{U}}$: Heizwert des Kraftstoffs in Joule pro Kilogramm ($\text{J}/\text{kg}$)

2. **Kraftstoffvolumenstrom**:

   $$
   \dot{V}_{\text{B}} = \frac{\dot{m}_{\text{B}}}{\rho}
   $$

   - $\dot{m}_{\text{B}}$: Kraftstoffmassenstrom in Kilogramm pro Stunde ($\text{kg}/\text{h}$)
   - $\rho$: Kraftstoffdichte in Kilogramm pro Liter ($\text{kg}/\text{l}$)

3. **Streckenbezogener Kraftstoffverbrauch**:

   $$
   V_{\text{S}} = \frac{\dot{V}_{\text{B}}}{v_{\text{Auto}}} \times 100~\text{km}
   $$

   - $\dot{V}_{\text{B}}$: Kraftstoffvolumenstrom in Litern pro Stunde ($\text{l}/\text{h}$)
   - $v_{\text{Auto}}$: Fahrzeuggeschwindigkeit in Kilometern pro Stunde ($\text{km}/\text{h}$)

## Bedeutung der Aufgabe

Die Berechnung des Kraftstoffverbrauchs bei hoher Geschwindigkeit ist wichtig für:

- **Energieeffizienz**: Verständnis dafür, wie der Kraftstoffverbrauch mit steigender Geschwindigkeit zunimmt.

- **Umweltaspekte**: Abschätzung der CO₂-Emissionen, die direkt mit dem Kraftstoffverbrauch verknüpft sind.

- **Betriebskosten**: Kalkulation der Kosten für den Fahrer bei hohen Geschwindigkeiten.

## Ziel der Berechnung

- **Ermittlung des Kraftstoffverbrauchs** in $\text{l}/(100~\text{km})$ bei einer konstanten Geschwindigkeit von $180~\text{km/h}$, basierend auf der erforderlichen Motorleistung und den Eigenschaften des Kraftstoffs.

## Zusammenfassung

Die Aufgabe fordert eine detaillierte Berechnung, die folgende Aspekte berücksichtigt:

1. **Energiebedarf des Fahrzeugs**: Bestimmt durch die Fahrwiderstände und die benötigte Motorleistung.

2. **Motorwirkungsgrad**: Beeinflusst, wie viel der zugeführten Energie tatsächlich in Antriebsenergie umgewandelt wird.

3. **Kraftstoffeigenschaften**: Heizwert und Dichte des Kraftstoffs sind entscheidend für die Umrechnung von Energiebedarf zu verbrauchtem Kraftstoffvolumen.

Durch das Verständnis und die Anwendung dieser Faktoren kann der spezifische Kraftstoffverbrauch bei einer gegebenen Fahrbedingung berechnet werden.

# Erklärung der Aufgabe 2

**Frage:** *Wie groß ist der Benzinverbrauch in $\text{l}/(100\,\text{km})$ bei $180~\text{km/h}$?*

## Ziel der Aufgabe

Die Aufgabe besteht darin, den streckenbezogenen Kraftstoffverbrauch eines Fahrzeugs (hier: Mercedes A-Klasse) zu berechnen, wenn es mit einer konstanten Geschwindigkeit von $180~\text{km/h}$ fährt. Der Verbrauch soll in Litern pro 100 Kilometer ($\text{l}/(100~\text{km})$) angegeben werden.

## Hintergrundinformationen

Um den Kraftstoffverbrauch zu ermitteln, müssen wir verstehen, wie der Energiebedarf des Fahrzeugs mit dem Kraftstoffverbrauch zusammenhängt. Der Motor wandelt die chemische Energie des Kraftstoffs in mechanische Arbeit um, um die Fahrwiderstände zu überwinden. Dabei treten folgende wichtige Größen auf:

1. **Erforderliche Motorleistung ($P_{\text{Motor}}$)**: Die Leistung, die der Motor aufbringen muss, um die Fahrwiderstände bei $180~\text{km/h}$ zu überwinden. Diese Leistung wurde in der vorherigen Aufgabe berechnet und beträgt etwa $72{,}0~\text{kW}$.

2. **Effektiver Wirkungsgrad des Motors ($\eta_{\text{e}}$)**: Der Anteil der im Kraftstoff enthaltenen Energie, der tatsächlich in mechanische Arbeit umgewandelt wird. Bei einem Ottomotor kann bei Nennleistung ein Wirkungsgrad von etwa $30\,\%$ angenommen werden.

3. **Heizwert des Kraftstoffs ($H_{\text{U}}$)**: Die spezifische Energie, die bei der Verbrennung eines Kilogramms Kraftstoff freigesetzt wird. Für Ottokraftstoff beträgt der Heizwert $42\,000~\text{kJ}/\text{kg}$.

4. **Kraftstoffdichte ($\rho$)**: Die Dichte des Kraftstoffs, die benötigt wird, um den Massenstrom in einen Volumenstrom umzurechnen. Für Ottokraftstoff beträgt die Dichte $0{,}76~\text{kg}/\text{l}$.

## Vorgehensweise zur Lösung

Die Berechnung erfolgt in mehreren Schritten:

1. **Berechnung des Kraftstoffmassenstroms ($\dot{m}_{\text{B}}$)**:

   - Ermittlung, wie viel Kilogramm Kraftstoff pro Zeiteinheit verbrannt werden müssen, um die erforderliche Motorleistung zu erbringen.

2. **Umrechnung des Massenstroms in Volumenstrom ($\dot{V}_{\text{B}}$)**:

   - Verwendung der Kraftstoffdichte, um den Massenstrom in Liter pro Stunde umzurechnen.

3. **Berechnung des streckenbezogenen Kraftstoffverbrauchs ($V_{\text{S}}$)**:

   - Bestimmung des Kraftstoffverbrauchs pro 100 Kilometer basierend auf der gefahrenen Geschwindigkeit und dem Volumenstrom.

## Relevante Formeln

1. **Kraftstoffmassenstrom**:

   $$
   \dot{m}_{\text{B}} = \frac{P_{\text{Motor}}}{\eta_{\text{e}} \cdot H_{\text{U}}}
   $$

   - $P_{\text{Motor}}$: Motorleistung in Watt ($\text{W}$)
   - $\eta_{\text{e}}$: Effektiver Wirkungsgrad des Motors
   - $H_{\text{U}}$: Heizwert des Kraftstoffs in Joule pro Kilogramm ($\text{J}/\text{kg}$)

2. **Kraftstoffvolumenstrom**:

   $$
   \dot{V}_{\text{B}} = \frac{\dot{m}_{\text{B}}}{\rho}
   $$

   - $\dot{m}_{\text{B}}$: Kraftstoffmassenstrom in Kilogramm pro Stunde ($\text{kg}/\text{h}$)
   - $\rho$: Kraftstoffdichte in Kilogramm pro Liter ($\text{kg}/\text{l}$)

3. **Streckenbezogener Kraftstoffverbrauch**:

   $$
   V_{\text{S}} = \frac{\dot{V}_{\text{B}}}{v_{\text{Auto}}} \times 100~\text{km}
   $$

   - $\dot{V}_{\text{B}}$: Kraftstoffvolumenstrom in Litern pro Stunde ($\text{l}/\text{h}$)
   - $v_{\text{Auto}}$: Fahrzeuggeschwindigkeit in Kilometern pro Stunde ($\text{km}/\text{h}$)

## Bedeutung der Aufgabe

Die Berechnung des Kraftstoffverbrauchs bei hoher Geschwindigkeit ist wichtig für:

- **Energieeffizienz**: Verständnis dafür, wie der Kraftstoffverbrauch mit steigender Geschwindigkeit zunimmt.

- **Umweltaspekte**: Abschätzung der CO₂-Emissionen, die direkt mit dem Kraftstoffverbrauch verknüpft sind.

- **Betriebskosten**: Kalkulation der Kosten für den Fahrer bei hohen Geschwindigkeiten.

## Ziel der Berechnung

- **Ermittlung des Kraftstoffverbrauchs** in $\text{l}/(100~\text{km})$ bei einer konstanten Geschwindigkeit von $180~\text{km/h}$, basierend auf der erforderlichen Motorleistung und den Eigenschaften des Kraftstoffs.

## Zusammenfassung

Die Aufgabe fordert eine detaillierte Berechnung, die folgende Aspekte berücksichtigt:

1. **Energiebedarf des Fahrzeugs**: Bestimmt durch die Fahrwiderstände und die benötigte Motorleistung.

2. **Motorwirkungsgrad**: Beeinflusst, wie viel der zugeführten Energie tatsächlich in Antriebsenergie umgewandelt wird.

3. **Kraftstoffeigenschaften**: Heizwert und Dichte des Kraftstoffs sind entscheidend für die Umrechnung von Energiebedarf zu verbrauchtem Kraftstoffvolumen.

# Welche Leistung wird bei einer Geschwindigkeit von $50~\text{km/h}$ benötigt? Wie groß ist dann der effektive Motorwirkungsgrad, wenn der Benzinverbrauch $5~\text{l}/(100~\text{km})$ beträgt?

## Gegebene Werte

- **Fahrzeuggeschwindigkeit:**  
  $$ v_{\text{Auto}} = 50~\text{km/h} = \frac{50}{3{,}6}~\text{m/s} \approx 13{,}89~\text{m/s} $$
- **Luftwiderstandsbeiwert:**  
  $$ c_{\text{w}} = 0{,}31 $$
- **Stirnfläche:**  
  $$ A = 2{,}4~\text{m}^2 $$
- **Fahrzeugmasse:**  
  $$ m = 1270~\text{kg} $$
- **Rollwiderstandsbeiwert:**  
  $$ \mu = 0{,}015 $$
- **Luftdichte:**  
  $$ \rho = 1{,}2041~\frac{\text{kg}}{\text{m}^3} $$ *(bei Standardbedingungen)*
- **Erdbeschleunigung:**  
  $$ g = 9{,}81~\frac{\text{m}}{\text{s}^2} $$
- **Getriebewirkungsgrad:**  
  $$ \eta_{\text{Getriebe}} = 0{,}92 $$

## 1. Berechnung der Luftwiderstandskraft $F_{\text{cw}}$

Die Luftwiderstandskraft wird berechnet mit:

$$
F_{\text{cw}} = \frac{1}{2} \cdot \rho \cdot v_{\text{Auto}}^2 \cdot c_{\text{w}} \cdot A
$$

Einsetzen der Werte:

$$
\begin{align*}
F_{\text{cw}} &= \frac{1}{2} \cdot 1{,}2041~\frac{\text{kg}}{\text{m}^3} \cdot (13{,}89~\text{m/s})^2 \cdot 0{,}31 \cdot 2{,}4~\text{m}^2 \\
&= 0{,}5 \cdot 1{,}2041 \cdot 193{,}05~\text{m}^2\text{/s}^2 \cdot 0{,}31 \cdot 2{,}4 \\
&= 0{,}5 \cdot 1{,}2041 \cdot 193{,}05 \cdot 0{,}744 \\
&= 0{,}5 \cdot 1{,}2041 \cdot 143{,}605 \\
&= 86{,}469~\text{N}
\end{align*}
$$

## 2. Berechnung der Rollwiderstandskraft $F_{\text{roll}}$

$$
F_{\text{roll}} = \mu \cdot m \cdot g
$$

Einsetzen der Werte:

$$
F_{\text{roll}} = 0{,}015 \cdot 1270~\text{kg} \cdot 9{,}81~\frac{\text{m}}{\text{s}^2} = 186{,}9855~\text{N}
$$

## 3. Berechnung der Gesamtwiderstandskraft $F_{\text{ges}}$

$$
F_{\text{ges}} = F_{\text{cw}} + F_{\text{roll}} = 86{,}469~\text{N} + 186{,}9855~\text{N} = 273{,}4545~\text{N}
$$

## 4. Berechnung der Radleistung $P_{\text{Rad}}$

$$
P_{\text{Rad}} = F_{\text{ges}} \cdot v_{\text{Auto}}
$$

Einsetzen der Werte:

$$
P_{\text{Rad}} = 273{,}4545~\text{N} \cdot 13{,}89~\text{m/s} = 3797{,}5~\text{W} \approx 3{,}8~\text{kW}
$$

## 5. Berechnung der erforderlichen Motorleistung $P_{\text{Motor}}$

$$
P_{\text{Motor}} = \frac{P_{\text{Rad}}}{\eta_{\text{Getriebe}}} = \frac{3797{,}5~\text{W}}{0{,}92} = 4127{,}72~\text{W} \approx 4{,}13~\text{kW}
$$

**Antwort auf den ersten Teil der Frage:** Die benötigte Motorleistung bei $50~\text{km/h}$ beträgt etwa **4{,}13 kW**.

## 6. Berechnung des effektiven Motorwirkungsgrades $\eta_{\text{e}}$

Gegeben ist ein Benzinverbrauch von $V_{\text{S}} = 5~\text{l}/(100~\text{km})$.

### a) Berechnung des Kraftstoffvolumenstroms $\dot{V}_{\text{B}}$

Bei einer Geschwindigkeit von $50~\text{km/h}$ legt das Fahrzeug pro Stunde $50~\text{km}$ zurück.

Der Kraftstoffverbrauch pro Stunde ist:

$$
\dot{V}_{\text{B}} = \frac{V_{\text{S}}}{100~\text{km}} \cdot v_{\text{Auto}} = \frac{5~\text{l}}{100~\text{km}} \cdot 50~\text{km/h} = 2{,}5~\text{l/h}
$$

### b) Umrechnung in Kraftstoffmassenstrom $\dot{m}_{\text{B}}$

Mit der Kraftstoffdichte $\rho_{\text{B}} = 0{,}76~\frac{\text{kg}}{\text{l}}$:

$$
\dot{m}_{\text{B}} = \dot{V}_{\text{B}} \cdot \rho_{\text{B}} = 2{,}5~\text{l/h} \cdot 0{,}76~\frac{\text{kg}}{\text{l}} = 1{,}9~\text{kg/h}
$$

### c) Umrechnung des Massenstroms in $\frac{\text{kg}}{\text{s}}$

$$
\dot{m}_{\text{B}} = \frac{1{,}9~\text{kg/h}}{3600~\text{s/h}} = 5{,}2778 \times 10^{-4}~\frac{\text{kg}}{\text{s}}
$$

### d) Berechnung der zugeführten Brennstoffleistung $\dot{Q}_{\text{B}}$

Mit dem Heizwert von Benzin $H_{\text{U}} = 42{,}000~\frac{\text{kJ}}{\text{kg}} = 42{,}000{,}000~\frac{\text{J}}{\text{kg}}$:

$$
\dot{Q}_{\text{B}} = \dot{m}_{\text{B}} \cdot H_{\text{U}} = 5{,}2778 \times 10^{-4}~\frac{\text{kg}}{\text{s}} \cdot 42{,}000{,}000~\frac{\text{J}}{\text{kg}} = 22{,}166{,}667~\text{W}
$$

### e) Berechnung des effektiven Motorwirkungsgrades $\eta_{\text{e}}$

$$
\eta_{\text{e}} = \frac{P_{\text{Motor}}}{\dot{Q}_{\text{B}}} = \frac{4127{,}72~\text{W}}{22{,}166{,}667~\text{W}} = 0{,}1862 \approx 18{,}62\%
$$

**Antwort auf den zweiten Teil der Frage:** Der effektive Motorwirkungsgrad beträgt etwa **18{,}62 %**.

## Zusammenfassung

- **Benötigte Motorleistung bei 50 km/h:**  
  $P_{\text{Motor}} \approx 4{,}13~\text{kW}$
- **Effektiver Motorwirkungsgrad bei einem Verbrauch von 5 l/(100 km):**  
  $\eta_{\text{e}} \approx 18{,}62\,\%$

# Erklärung der Aufgabe 3

**Frage:** *Welche Leistung wird bei einer Geschwindigkeit von $50~\text{km/h}$ benötigt? Wie groß ist dann der effektive Motorwirkungsgrad, wenn der Benzinverbrauch $5~\text{l}/(100~\text{km})$ beträgt?*

## Ziel der Aufgabe

Die Aufgabe gliedert sich in zwei Teile:

1. **Berechnung der erforderlichen Motorleistung** bei einer konstanten Fahrgeschwindigkeit von $50~\text{km/h}$.
2. **Ermittlung des effektiven Motorwirkungsgrads**, wenn bei dieser Geschwindigkeit ein spezifischer Benzinverbrauch von $5~\text{l}/(100~\text{km})$ gemessen wird.

## Hintergrundinformationen

### Teil 1: Berechnung der Motorleistung bei $50~\text{km/h}$

Wenn ein Fahrzeug mit konstanter Geschwindigkeit auf ebener Strecke fährt, muss es verschiedene Fahrwiderstände überwinden. Die wichtigsten Widerstandskräfte sind:

1. **Rollwiderstandskraft ($F_{\text{roll}}$)**: Entsteht durch die Verformung der Reifen und den Kontakt zwischen Reifen und Fahrbahn.
2. **Luftwiderstandskraft ($F_{\text{cw}}$)**: Resultiert aus dem Luftwiderstand, den das Fahrzeug überwinden muss.
3. **Steigungskraft ($F_{\text{steig}}$)**: Tritt bei Fahrten auf Steigungen auf; auf ebener Strecke entfällt dieser Widerstand ($\beta = 0^\circ$).

Die Gesamtwiderstandskraft ($F_{\text{ges}}$) ist die Summe dieser Kräfte:

$$
F_{\text{ges}} = F_{\text{roll}} + F_{\text{cw}} + F_{\text{steig}}
$$

Da die Steigungskraft auf ebener Strecke entfällt, gilt:

$$
F_{\text{ges}} = F_{\text{roll}} + F_{\text{cw}}
$$

Die **benötigte Radleistung ($P_{\text{Rad}}$)** ergibt sich aus der Multiplikation der Gesamtwiderstandskraft mit der Fahrgeschwindigkeit:

$$
P_{\text{Rad}} = F_{\text{ges}} \cdot v_{\text{Auto}}
$$

Die **erforderliche Motorleistung ($P_{\text{Motor}}$)** berücksichtigt zusätzlich den **Getriebewirkungsgrad ($\eta_{\text{Getriebe}}$)**:

$$
P_{\text{Motor}} = \frac{P_{\text{Rad}}}{\eta_{\text{Getriebe}}}
$$

### Teil 2: Bestimmung des effektiven Motorwirkungsgrads

Der **effektive Motorwirkungsgrad ($\eta_{\text{e}}$)** gibt an, welcher Anteil der im Kraftstoff enthaltenen chemischen Energie in mechanische Arbeit umgewandelt wird.

Der Kraftstoffverbrauch hängt direkt vom Wirkungsgrad ab. Um den Wirkungsgrad zu ermitteln, benötigen wir:

1. **Die zugeführte Brennstoffleistung ($\dot{Q}_{\text{B}}$)**:

$$
\dot{Q}_{\text{B}} = \dot{m}_{\text{B}} \cdot H_{\text{U}}
$$

- $\dot{m}_{\text{B}}$: Kraftstoffmassenstrom
- $H_{\text{U}}$: Heizwert des Kraftstoffs

2. **Den effektiven Wirkungsgrad**:

$$
\eta_{\text{e}} = \frac{P_{\text{Motor}}}{\dot{Q}_{\text{B}}}
$$

Der Kraftstoffmassenstrom kann aus dem bekannten Verbrauch und der Fahrgeschwindigkeit berechnet werden.

## Gegebene Werte und Parameter

- **Fahrzeuggeschwindigkeit:** $v_{\text{Auto}} = 50~\text{km/h}$
- **Luftwiderstandsbeiwert:** $c_{\text{w}} = 0{,}31$
- **Stirnfläche des Fahrzeugs:** $A = 2{,}4~\text{m}^2$
- **Fahrzeugmasse:** $m = 1270~\text{kg}$
- **Rollwiderstandsbeiwert:** $\mu = 0{,}015$
- **Luftdichte:** $\rho = 1{,}2041~\frac{\text{kg}}{\text{m}^3}$ (Standardbedingungen)
- **Erdbeschleunigung:** $g = 9{,}81~\frac{\text{m}}{\text{s}^2}$
- **Getriebewirkungsgrad:** $\eta_{\text{Getriebe}} = 0{,}92$
- **Heizwert von Ottokraftstoff:** $H_{\text{U}} = 42\,000~\frac{\text{kJ}}{\text{kg}}$
- **Kraftstoffdichte:** $\rho_{\text{B}} = 0{,}76~\frac{\text{kg}}{\text{l}}$
- **Spezifischer Kraftstoffverbrauch:** $V_{\text{S}} = 5~\frac{\text{l}}{100~\text{km}}$

## Bedeutung der Aufgabe

Die Aufgabe verdeutlicht:

- **Den Einfluss der Fahrgeschwindigkeit** auf den Leistungsbedarf und den Kraftstoffverbrauch.
- **Die Ineffizienz von Verbrennungsmotoren** bei niedriger Last und geringer Geschwindigkeit, was zu einem höheren spezifischen Verbrauch führt.
- **Die Herausforderungen im Stadtverkehr**, wo häufige Stop-and-go-Situationen und niedrige Geschwindigkeiten zu einem erhöhten Kraftstoffverbrauch beitragen.

## Ziel der Berechnung

1. **Ermittlung der benötigten Motorleistung ($P_{\text{Motor}}$)** bei einer Fahrgeschwindigkeit von $50~\text{km/h}$ auf ebener Strecke.
2. **Berechnung des effektiven Motorwirkungsgrads ($\eta_{\text{e}}$)**, basierend auf dem bekannten spezifischen Kraftstoffverbrauch und der ermittelten Motorleistung.

## Relevante Formeln

### Rollwiderstandskraft

$$
F_{\text{roll}} = \mu \cdot m \cdot g
$$

### Luftwiderstandskraft

$$
F_{\text{cw}} = \frac{1}{2} \cdot \rho \cdot c_{\text{w}} \cdot A \cdot v_{\text{Auto}}^2
$$

### Gesamtwiderstandskraft

$$
F_{\text{ges}} = F_{\text{roll}} + F_{\text{cw}}
$$

### Radleistung

$$
P_{\text{Rad}} = F_{\text{ges}} \cdot v_{\text{Auto}}
$$

### Motorleistung

$$
P_{\text{Motor}} = \frac{P_{\text{Rad}}}{\eta_{\text{Getriebe}}}
$$

### Kraftstoffverbrauch und Wirkungsgrad

- **Kraftstoffvolumenstrom ($\dot{V}_{\text{B}}$)**:

$$
\dot{V}_{\text{B}} = \frac{V_{\text{S}}}{100~\text{km}} \cdot v_{\text{Auto}}
$$

- **Kraftstoffmassenstrom ($\dot{m}_{\text{B}}$)**:

$$
\dot{m}_{\text{B}} = \dot{V}_{\text{B}} \cdot \rho_{\text{B}}
$$

- **Zugeführte Brennstoffleistung ($\dot{Q}_{\text{B}}$)**:

$$
\dot{Q}_{\text{B}} = \dot{m}_{\text{B}} \cdot H_{\text{U}}
$$

- **Effektiver Wirkungsgrad ($\eta_{\text{e}}$)**:

$$
\eta_{\text{e}} = \frac{P_{\text{Motor}}}{\dot{Q}_{\text{B}}}
$$

## Zusammenfassung

Diese Aufgabe zeigt auf, dass bei niedrigen Geschwindigkeiten der Leistungsbedarf eines Fahrzeugs zwar gering ist, der Kraftstoffverbrauch jedoch aufgrund des ineffizienten Motorbetriebs im Teillastbereich relativ hoch sein kann. Durch die Berechnung des effektiven Motorwirkungsgrads wird deutlich, wie die Effizienz des Motors den tatsächlichen Verbrauch beeinflusst.

# Was ist beim Pkw wichtiger: der Rollwiderstand oder der Luftwiderstand?

## Ziel der Aufgabe

Die Aufgabe zielt darauf ab, zu bestimmen, welcher der beiden Hauptfahrwiderstände—Rollwiderstand oder Luftwiderstand—beim Pkw wichtiger ist. Dabei soll untersucht werden, wie sich beide Widerstandskräfte in Abhängigkeit von der Fahrzeuggeschwindigkeit verhalten und welchen Einfluss sie auf den Leistungsbedarf haben.

## Hintergrundinformationen

Beim Fahren wirken auf ein Fahrzeug verschiedene Widerstandskräfte, die überwunden werden müssen, um eine konstante Geschwindigkeit zu halten:

1. **Rollwiderstandskraft ($F_{\text{roll}}$)**: Entsteht durch die Verformung der Reifen und die Reibung zwischen Reifen und Fahrbahn.

2. **Luftwiderstandskraft ($F_{\text{cw}}$)**: Resultiert aus der Luft, die das Fahrzeug verdrängen muss, und hängt von der Aerodynamik ab.

## Vorgehensweise zur Lösung

1. **Formel für die Rollwiderstandskraft:**

   $$
   F_{\text{roll}} = \mu \cdot m \cdot g
   $$

   - $\mu$: Rollwiderstandsbeiwert
   - $m$: Fahrzeugmasse
   - $g$: Erdbeschleunigung

2. **Formel für die Luftwiderstandskraft:**

   $$
   F_{\text{cw}} = \frac{1}{2} \cdot \rho \cdot c_{\text{w}} \cdot A \cdot v^2
   $$

   - $\rho$: Luftdichte
   - $c_{\text{w}}$: Luftwiderstandsbeiwert
   - $A$: Stirnfläche des Fahrzeugs
   - $v$: Fahrzeuggeschwindigkeit

3. **Berechnung der Kräfte bei verschiedenen Geschwindigkeiten:**

   - Wählen Sie typische Werte für $\mu$, $m$, $g$, $\rho$, $c_{\text{w}}$, $A$.
   - Berechnen Sie $F_{\text{roll}}$ und $F_{\text{cw}}$ für verschiedene Geschwindigkeiten.
   - Stellen Sie die Ergebnisse tabellarisch oder grafisch dar.

4. **Analyse der Ergebnisse:**

   - Vergleichen Sie die Werte von $F_{\text{roll}}$ und $F_{\text{cw}}$ bei unterschiedlichen Geschwindigkeiten.
   - Bestimmen Sie, ab welcher Geschwindigkeit der Luftwiderstand den Rollwiderstand überwiegt.

## Schritt-für-Schritt-Lösung

### 1. Gegebene Werte und Annahmen

- **Rollwiderstandsbeiwert ($\mu$)**: 0,015
- **Fahrzeugmasse ($m$)**: 1.500 kg
- **Erdbeschleunigung ($g$)**: 9,81 m/s²
- **Luftdichte ($\rho$)**: 1,2041 kg/m³ (bei 20 °C)
- **Luftwiderstandsbeiwert ($c_{\text{w}}$)**: 0,30
- **Stirnfläche ($A$)**: 2,2 m²
- **Geschwindigkeitsbereich**: 0 bis 200 km/h

### 2. Berechnung der Rollwiderstandskraft ($F_{\text{roll}}$)

Da $F_{\text{roll}}$ unabhängig von der Geschwindigkeit ist (bei konstantem $\mu$):

$$
F_{\text{roll}} = \mu \cdot m \cdot g = 0{,}015 \cdot 1\,500\,\text{kg} \cdot 9{,}81\,\frac{\text{m}}{\text{s}^2} = 220{,}725\,\text{N}
$$

### 3. Berechnung der Luftwiderstandskraft ($F_{\text{cw}}$) bei verschiedenen Geschwindigkeiten

Wir berechnen $F_{\text{cw}}$ für ausgewählte Geschwindigkeiten:

#### Umrechnung der Geschwindigkeit in m/s

$$
v\,(\text{m/s}) = v\,(\text{km/h}) \div 3{,}6
$$

#### Berechnungen

**Für 50 km/h:**

- $v = \frac{50}{3{,}6} = 13{,}89\,\text{m/s}$

$$
F_{\text{cw}} = \frac{1}{2} \cdot 1{,}2041 \cdot 0{,}30 \cdot 2{,}2 \cdot (13{,}89)^2 = 179{,}8\,\text{N}
$$

**Für 100 km/h:**

- $v = \frac{100}{3{,}6} = 27{,}78\,\text{m/s}$

$$
F_{\text{cw}} = \frac{1}{2} \cdot 1{,}2041 \cdot 0{,}30 \cdot 2{,}2 \cdot (27{,}78)^2 = 719{,}3\,\text{N}
$$

**Für 150 km/h:**

- $v = \frac{150}{3{,}6} = 41{,}67\,\text{m/s}$

$$
F_{\text{cw}} = \frac{1}{2} \cdot 1{,}2041 \cdot 0{,}30 \cdot 2{,}2 \cdot (41{,}67)^2 = 1\,618{,}6\,\text{N}
$$

**Für 200 km/h:**

- $v = \frac{200}{3{,}6} = 55{,}56\,\text{m/s}$

$$
F_{\text{cw}} = \frac{1}{2} \cdot 1{,}2041 \cdot 0{,}30 \cdot 2{,}2 \cdot (55{,}56)^2 = 2\,877{,}1\,\text{N}
$$

### 4. Vergleich der Kräfte

| Geschwindigkeit (km/h) | Rollwiderstandskraft $F_{\text{roll}}$ (N) | Luftwiderstandskraft $F_{\text{cw}}$ (N) |
| ---------------------- | ------------------------------------------ | ---------------------------------------- |
| 50                     | 220,7                                      | 179,8                                    |
| 100                    | 220,7                                      | 719,3                                    |
| 150                    | 220,7                                      | 1.618,6                                  |
| 200                    | 220,7                                      | 2.877,1                                  |

### 5. Analyse der Ergebnisse

- **Bei 50 km/h** sind Roll- und Luftwiderstandskraft in derselben Größenordnung.
- **Ab etwa 80 km/h** überwiegt der Luftwiderstand deutlich den Rollwiderstand.
- **Bei höheren Geschwindigkeiten** steigt der Luftwiderstand quadratisch an, während der Rollwiderstand konstant bleibt.

### 6. Grafische Darstellung (optional)

Eine grafische Darstellung der Widerstandskräfte in Abhängigkeit von der Geschwindigkeit verdeutlicht die unterschiedlichen Verläufe:

- **Rollwiderstandskraft:** Horizontale Linie (konstant).
- **Luftwiderstandskraft:** Parabel (quadratische Abhängigkeit von $v$).

### 7. Schlussfolgerung

- **Bei niedrigen Geschwindigkeiten** (unter ca. 50–60 km/h) ist der **Rollwiderstand** wichtiger als der Luftwiderstand.
- **Bei höheren Geschwindigkeiten** dominiert der **Luftwiderstand** und hat den größeren Einfluss auf den Leistungsbedarf.

## Antwort auf die Frage

Beim Pkw ist der Rollwiderstand bei niedrigen Geschwindigkeiten wichtiger, während der Luftwiderstand bei höheren Geschwindigkeiten überwiegt. Ab etwa 80 km/h ist der Luftwiderstand der dominierende Faktor für den Leistungsbedarf des Fahrzeugs.

## Zusammenfassung

- **Rollwiderstand:** Unabhängig von der Geschwindigkeit; wichtig bei niedrigen Geschwindigkeiten.
- **Luftwiderstand:** Steigt mit dem Quadrat der Geschwindigkeit; wird bei höheren Geschwindigkeiten dominierend.
- **Praktische Bedeutung:**
  - **Stadtverkehr:** Rollwiderstand ist relevanter.
  - **Autobahnfahrten:** Luftwiderstand bestimmt den Kraftstoffverbrauch maßgeblich.

# Erklärung der Aufgabe 4

**Frage:** *Was ist beim Pkw wichtiger: der Rollwiderstand oder der Luftwiderstand?*

## Ziel der Aufgabe

Die Aufgabe zielt darauf ab, zu ermitteln, welcher der beiden Hauptfahrwiderstände—Rollwiderstand oder Luftwiderstand—beim Pkw unter verschiedenen Bedingungen wichtiger ist. Es soll untersucht werden, wie sich beide Widerstandskräfte in Abhängigkeit von der Fahrzeuggeschwindigkeit verhalten und welchen Einfluss sie auf den Gesamtwiderstand und den Leistungsbedarf haben.

## Hintergrundinformationen

### Fahrwiderstände beim Pkw

Ein Fahrzeug muss beim Fahren verschiedene Widerstandskräfte überwinden, um sich fortzubewegen. Die beiden wichtigsten sind:

1. **Rollwiderstandskraft ($F_{\text{roll}}$)**

   - **Ursache:** Entsteht durch die Verformung der Reifen und den Kontakt zwischen Reifen und Fahrbahn.
   - **Einflussfaktoren:**
     - **Rollwiderstandsbeiwert ($\mu$)**: Beschreibt den Rollwiderstand der Reifen und ist abhängig von Reifenmaterial, Reifendruck und Fahrbahnoberfläche.
     - **Fahrzeugmasse ($m$)**: Höheres Gewicht führt zu höherem Rollwiderstand.
     - **Erdbeschleunigung ($g$)**: Konstant mit $9{,}81~\text{m/s}^2$.
   - **Charakteristik:** Der Rollwiderstand ist weitgehend unabhängig von der Fahrzeuggeschwindigkeit.

2. **Luftwiderstandskraft ($F_{\text{cw}}$)**

   - **Ursache:** Entsteht durch die Luft, die das Fahrzeug verdrängen muss, während es sich bewegt.
   - **Einflussfaktoren:**
     - **Luftdichte ($\rho$)**: Abhängig von Temperatur, Druck und Luftfeuchtigkeit.
     - **Luftwiderstandsbeiwert ($c_{\text{w}}$)**: Beschreibt die aerodynamische Form des Fahrzeugs.
     - **Stirnfläche ($A$)**: Die projizierte Frontfläche des Fahrzeugs.
     - **Fahrzeuggeschwindigkeit ($v$)**: Die Luftwiderstandskraft steigt quadratisch mit der Geschwindigkeit.
   - **Charakteristik:** Der Luftwiderstand nimmt mit steigender Geschwindigkeit exponentiell zu.

### Bedeutung der Widerstände

- **Rollwiderstand:** Hat einen größeren Einfluss bei niedrigen Geschwindigkeiten, da er unabhängig von der Geschwindigkeit ist. Er beeinflusst den Kraftstoffverbrauch im Stadtverkehr und bei Stop-and-go-Situationen.
  
- **Luftwiderstand:** Wird bei höheren Geschwindigkeiten zum dominierenden Widerstand. Er beeinflusst maßgeblich den Kraftstoffverbrauch auf Autobahnen und Landstraßen.

## Relevanz der Frage

- **Kraftstoffeffizienz:** Verstehen, welcher Widerstand stärker zum Kraftstoffverbrauch beiträgt, um Maßnahmen zur Reduzierung zu ergreifen.
- **Fahrzeugentwicklung:** Optimierung von Reifen und Aerodynamik, um die jeweiligen Widerstände zu minimieren.
- **Umweltaspekte:** Reduzierung von CO₂-Emissionen durch effizientere Fahrzeuge.

## Ziel der Untersuchung

- **Analyse der Abhängigkeiten:** Untersuchen, wie sich Roll- und Luftwiderstandskraft mit der Geschwindigkeit verhalten.
- **Bestimmung des dominierenden Widerstands:** Ermitteln, ab welcher Geschwindigkeit der Luftwiderstand wichtiger wird als der Rollwiderstand.
- **Praktische Implikationen:** Ableiten, welche Faktoren beim Fahrzeugdesign und Fahrverhalten berücksichtigt werden sollten.

## Vorgehensweise zur Beantwortung der Frage

1. **Mathematische Modelle verwenden:**
   - Aufstellen der Formeln für Roll- und Luftwiderstandskraft.
  
2. **Typische Fahrzeugdaten einsetzen:**
   - Verwenden von realistischen Werten für $\mu$, $m$, $g$, $\rho$, $c_{\text{w}}$, $A$.

3. **Berechnungen durchführen:**
   - Berechnung der Widerstandskräfte bei verschiedenen Geschwindigkeiten.

4. **Ergebnisse vergleichen:**
   - Analyse, wie sich die Kräfte mit der Geschwindigkeit verändern.
   - Identifizierung der Geschwindigkeit, ab der der Luftwiderstand dominiert.

## Relevante Formeln

### Rollwiderstandskraft

$$
F_{\text{roll}} = \mu \cdot m \cdot g
$$

- **$\mu$:** Rollwiderstandsbeiwert (dimensionslos)
- **$m$:** Fahrzeugmasse (in kg)
- **$g$:** Erdbeschleunigung ($9{,}81~\text{m/s}^2$)

### Luftwiderstandskraft

$$
F_{\text{cw}} = \frac{1}{2} \cdot \rho \cdot c_{\text{w}} \cdot A \cdot v^2
$$

- **$\rho$:** Luftdichte (ca. $1{,}2041~\text{kg/m}^3$ bei 20 °C)
- **$c_{\text{w}}$:** Luftwiderstandsbeiwert (dimensionslos)
- **$A$:** Stirnfläche (in $\text{m}^2$)
- **$v$:** Fahrzeuggeschwindigkeit (in $\text{m/s}$)

## Interpretation der Formeln

- **Rollwiderstandskraft ($F_{\text{roll}}$)** ist direkt proportional zur Fahrzeugmasse und unabhängig von der Geschwindigkeit.
  
- **Luftwiderstandskraft ($F_{\text{cw}}$)** ist proportional zum Quadrat der Geschwindigkeit. Das bedeutet, dass eine Verdoppelung der Geschwindigkeit zu einer Vervierfachung der Luftwiderstandskraft führt.

## Praktische Umsetzung

### Auswahl typischer Werte

- **Rollwiderstandsbeiwert ($\mu$)**: 0,015
- **Fahrzeugmasse ($m$)**: 1.500 kg
- **Luftdichte ($\rho$)**: 1,2041 kg/m³
- **Luftwiderstandsbeiwert ($c_{\text{w}}$)**: 0,30
- **Stirnfläche ($A$)**: 2,2 m²

### Berechnung der Widerstandskräfte

#### Rollwiderstandskraft

$$
F_{\text{roll}} = 0{,}015 \cdot 1\,500\,\text{kg} \cdot 9{,}81\,\frac{\text{m}}{\text{s}^2} = 220{,}725\,\text{N}
$$

- **Konstant über alle Geschwindigkeiten.**

#### Luftwiderstandskraft bei verschiedenen Geschwindigkeiten

| Geschwindigkeit (km/h) | Geschwindigkeit (m/s) | $F_{\text{cw}}$ (N)       |
| ---------------------- | --------------------- | ------------------------- |
| 30                     | 8,33                  | $F_{\text{cw}}$ berechnen |
| 50                     | 13,89                 | $F_{\text{cw}}$ berechnen |
| 80                     | 22,22                 | $F_{\text{cw}}$ berechnen |
| 100                    | 27,78                 | $F_{\text{cw}}$ berechnen |
| 130                    | 36,11                 | $F_{\text{cw}}$ berechnen |
| 160                    | 44,44                 | $F_{\text{cw}}$ berechnen |

**Beispielrechnung bei 50 km/h:**

$$
\begin{align*}
v &= 50\,\text{km/h} = \frac{50}{3{,}6}\,\text{m/s} = 13{,}89\,\text{m/s} \\
F_{\text{cw}} &= \frac{1}{2} \cdot 1{,}2041\,\frac{\text{kg}}{\text{m}^3} \cdot 0{,}30 \cdot 2{,}2\,\text{m}^2 \cdot (13{,}89\,\text{m/s})^2 \\
&= 86{,}5\,\text{N}
\end{align*}
$$

**Vergleich der Kräfte:**

- **Bei 50 km/h:**
  - **Rollwiderstandskraft:** 220,7 N
  - **Luftwiderstandskraft:** 86,5 N
  - **Der Rollwiderstand ist dominanter.**

- **Bei höheren Geschwindigkeiten steigt $F_{\text{cw}}$ schnell an.**

## Ergebnisse und Interpretation

- **Bis etwa 60 km/h** ist der Rollwiderstand größer als der Luftwiderstand.
  
- **Ab etwa 80 km/h** übersteigt der Luftwiderstand den Rollwiderstand und wird zum dominierenden Faktor.

- **Bei Autobahngeschwindigkeiten (über 100 km/h)** ist der Luftwiderstand deutlich höher und beeinflusst den Kraftstoffverbrauch maßgeblich.

## Bedeutung für das Fahrverhalten

- **Stadtverkehr:**
  - **Rollwiderstand dominiert:**
    - Maßnahmen zur Reduzierung des Rollwiderstands sind effektiver.
    - Richtiger Reifendruck und rollwiderstandsoptimierte Reifen können den Verbrauch senken.

- **Autobahnfahrten:**
  - **Luftwiderstand dominiert:**
    - Aerodynamische Verbesserungen haben größeren Einfluss.
    - Reduzierung der Geschwindigkeit kann den Kraftstoffverbrauch erheblich senken.

## Maßnahmen zur Reduzierung der Widerstände

### Reduzierung des Rollwiderstands

- **Reifendruck optimieren:** Zu niedriger Druck erhöht den Rollwiderstand.
- **Reifenwahl:** Spezielle Energiesparreifen mit niedrigem $\mu$.
- **Gewichtsreduktion:** Leichtere Fahrzeuge haben geringeren Rollwiderstand.

### Reduzierung des Luftwiderstands

- **Aerodynamisches Design:** Optimierung der Fahrzeugform zur Verringerung des $c_{\text{w}}$.
- **Anbauteile reduzieren:** Dachgepäckträger und offene Fenster erhöhen den Luftwiderstand.
- **Fahrzeughöhe anpassen:** Tiefergelegte Fahrzeuge haben oft geringeren Luftwiderstand.

## Zusammenfassung

- **Bei niedrigen Geschwindigkeiten** ist der **Rollwiderstand** wichtiger und hat größeren Einfluss auf den Kraftstoffverbrauch.
  
- **Bei hohen Geschwindigkeiten** wird der **Luftwiderstand** zum dominierenden Widerstand und beeinflusst den Leistungsbedarf sowie den Verbrauch stärker.

- **Praktische Implikationen:**
  - **Für Fahrer:** Anpassung des Fahrverhaltens kann den Kraftstoffverbrauch senken.
  - **Für Hersteller:** Fokus auf entsprechende Fahrzeugoptimierungen je nach Zielgeschwindigkeit.

## Antwort auf die Frage

Beim Pkw ist der **Rollwiderstand** bei niedrigen Geschwindigkeiten (bis ca. 60 km/h) wichtiger. Bei höheren Geschwindigkeiten (ab ca. 80 km/h) wird der **Luftwiderstand** dominierend und hat einen größeren Einfluss auf den Leistungsbedarf und den Kraftstoffverbrauch.

---

**Zusammenfassend** zeigt die Aufgabe, dass der Einfluss der Widerstandskräfte stark von der Fahrgeschwindigkeit abhängt. Ein Verständnis dieser Zusammenhänge ist entscheidend für effizientes Fahren und die Entwicklung sparsamer Fahrzeuge.


# Was sind typische Zahlenwerte, um den Leistungsbedarf eines Pkw zu berechnen?

## Ziel der Aufgabe

Die Aufgabe besteht darin, typische Kenngrößen und Zahlenwerte zu identifizieren, die bei der Berechnung des Leistungsbedarfs eines Pkw verwendet werden. Diese Werte sind essenziell, um genaue Berechnungen durchzuführen und realistische Ergebnisse zu erhalten.

## Hintergrundinformationen

Bei der Berechnung des Leistungsbedarfs eines Pkw werden verschiedene physikalische Größen und Fahrzeugparameter berücksichtigt. Diese beinhalten:

- **Luftwiderstandsbeiwert ($c_{\text{w}}$)**
- **Stirnfläche des Fahrzeugs ($A$)**
- **Rollwiderstandsbeiwert ($\mu$)**
- **Getriebewirkungsgrad ($\eta_{\text{Getriebe}}$)**
- **Effektiver Motorwirkungsgrad ($\eta_{\text{e}}$)**

## Typische Zahlenwerte für Pkw

### 1. Luftwiderstandsbeiwert ($c_{\text{w}}$)

Der Luftwiderstandsbeiwert beschreibt die aerodynamische Güte eines Fahrzeugs.

- **Typische Werte:**
  - **Mittelklasse-Pkw:** $c_{\text{w}} = 0{,}29$ bis $0{,}32$
  - **Aerodynamisch optimierte Fahrzeuge:** $c_{\text{w}} \approx 0{,}25$
  - **SUVs und Geländewagen:** $c_{\text{w}} = 0{,}35$ bis $0{,}40$

### 2. Stirnfläche des Fahrzeugs ($A$)

Die Stirnfläche ist die projizierte Frontfläche und beeinflusst maßgeblich den Luftwiderstand.

- **Typische Werte:**
  - **Kompaktklasse:** $A \approx 2{,}0~\text{m}^2$
  - **Mittelklasse:** $A \approx 2{,}2~\text{m}^2$
  - **Oberklasse und SUVs:** $A = 2{,}5~\text{m}^2$ bis $3{,}0~\text{m}^2$
- **Berechnungshinweis:**
  - Eine Faustformel ist, dass die Stirnfläche etwa **85 %** der Rechteckfläche aus Fahrzeugbreite und -höhe beträgt.

### 3. Rollwiderstandsbeiwert ($\mu$)

Der Rollwiderstandsbeiwert beschreibt den Rollwiderstand der Reifen.

- **Typische Werte:**
  - **Normale Pkw-Reifen:** $\mu = 0{,}015$
  - **Energiesparreifen:** $\mu = 0{,}010$ bis $0{,}012$
  - **Geländereifen:** $\mu = 0{,}020$ oder höher

### 4. Getriebewirkungsgrad ($\eta_{\text{Getriebe}}$)

Der Getriebewirkungsgrad berücksichtigt die Verluste im Antriebsstrang.

- **Typische Werte:**
  - **Manuelles Schaltgetriebe:** $\eta_{\text{Getriebe}} = 0{,}95$ bis $0{,}97$
  - **Automatikgetriebe:** $\eta_{\text{Getriebe}} = 0{,}90$ bis $0{,}92$
  - **Durchschnittswert für Berechnungen:** $\eta_{\text{Getriebe}} = 0{,}90$

### 5. Effektiver Motorwirkungsgrad ($\eta_{\text{e}}$)

Der effektive Wirkungsgrad des Motors variiert je nach Betriebsbedingungen.

- **Bei Nennleistung (Volllast):**
  - **Ottomotor:** $\eta_{\text{e}} \approx 0{,}30$ oder 30 %
  - **Dieselmotor:** $\eta_{\text{e}} \approx 0{,}35$ oder 35 %
- **Im Bestpunkt (hohe Last, mittlere Drehzahl):**
  - **Ottomotor:** $\eta_{\text{e}} \approx 0{,}37$
  - **Dieselmotor:** $\eta_{\text{e}} \approx 0{,}42$
- **Im Stadtverkehr (Teillastbetrieb):**
  - **Sportlicher Ottomotor:** $\eta_{\text{e}} \approx 0{,}10$
  - **Normaler Ottomotor:** $\eta_{\text{e}} \approx 0{,}15$
  - **Kleinwagen mit Dieselmotor:** $\eta_{\text{e}} \approx 0{,}20$
- **Im Leerlauf:**
  - $\eta_{\text{e}} = 0$ (da keine nutzbare Leistung erbracht wird)

### 6. Weitere wichtige Größen

- **Fahrzeugmasse ($m$)**
  - **Kleinwagen:** $m = 1\,000~\text{kg}$ bis $1\,200~\text{kg}$
  - **Mittelklasse:** $m = 1\,400~\text{kg}$ bis $1\,600~\text{kg}$
  - **SUVs/Oberklasse:** $m = 1\,800~\text{kg}$ bis $2\,500~\text{kg}$
- **Erdbeschleunigung ($g$)**
  - $g = 9{,}81~\frac{\text{m}}{\text{s}^2}$ (konstanter Wert)

### 7. Luftdichte ($\rho$)

- **Standardbedingungen (20 °C, 1 bar):**
  - $\rho = 1{,}2041~\frac{\text{kg}}{\text{m}^3}$
- **Einflussfaktoren:**
  - Temperatur, Luftdruck und Luftfeuchtigkeit können die Luftdichte leicht verändern.

## Bedeutung dieser Werte für die Berechnung

Die genannten typischen Zahlenwerte werden in den grundlegenden Formeln zur Berechnung des Leistungsbedarfs eingesetzt:

- **Luftwiderstandskraft ($F_{\text{cw}}$)**
  $$
  F_{\text{cw}} = \frac{1}{2} \cdot \rho \cdot v^2 \cdot c_{\text{w}} \cdot A
  $$
- **Rollwiderstandskraft ($F_{\text{roll}}$)**
  $$
  F_{\text{roll}} = \mu \cdot m \cdot g
  $$
- **Erforderliche Motorleistung ($P_{\text{Motor}}$)**
  $$
  P_{\text{Motor}} = \frac{(F_{\text{cw}} + F_{\text{roll}}) \cdot v}{\eta_{\text{Getriebe}}}
  $$

Durch das Einsetzen der typischen Werte in diese Formeln können Ingenieure und Techniker den Leistungsbedarf eines Fahrzeugs unter verschiedenen Bedingungen abschätzen.

## Beispielrechnung (optional)

Zur Veranschaulichung kann eine beispielhafte Berechnung durchgeführt werden, bei der die typischen Werte eingesetzt werden, um den Leistungsbedarf bei einer bestimmten Geschwindigkeit zu ermitteln.

**Angenommene Werte:**

- $v = 100~\text{km/h} = 27{,}78~\text{m/s}$
- $c_{\text{w}} = 0{,}30$
- $A = 2{,}2~\text{m}^2$
- $\mu = 0{,}015$
- $m = 1\,500~\text{kg}$
- $\eta_{\text{Getriebe}} = 0{,}90$

**Berechnung der Luftwiderstandskraft:**

$$
F_{\text{cw}} = \frac{1}{2} \cdot 1{,}2041~\frac{\text{kg}}{\text{m}^3} \cdot (27{,}78~\text{m/s})^2 \cdot 0{,}30 \cdot 2{,}2~\text{m}^2 = 719{,}3~\text{N}
$$

**Berechnung der Rollwiderstandskraft:**

$$
F_{\text{roll}} = 0{,}015 \cdot 1\,500~\text{kg} \cdot 9{,}81~\frac{\text{m}}{\text{s}^2} = 220{,}7~\text{N}
$$

**Gesamtwiderstandskraft:**

$$
F_{\text{ges}} = F_{\text{cw}} + F_{\text{roll}} = 719{,}3~\text{N} + 220{,}7~\text{N} = 940~\text{N}
$$

**Berechnung der erforderlichen Motorleistung:**

$$
P_{\text{Motor}} = \frac{F_{\text{ges}} \cdot v}{\eta_{\text{Getriebe}}} = \frac{940~\text{N} \cdot 27{,}78~\text{m/s}}{0{,}90} \approx 29\,000~\text{W} = 29~\text{kW}
$$

## Zusammenfassung

Typische Zahlenwerte für die Berechnung des Leistungsbedarfs eines Pkw sind:

- **Luftwiderstandsbeiwert ($c_{\text{w}}$)**: 0,29 bis 0,32
- **Stirnfläche ($A$)**: 2,2 m²
- **Rollwiderstandsbeiwert ($\mu$)**: 0,015
- **Getriebewirkungsgrad ($\eta_{\text{Getriebe}}$)**: 0,90
- **Effektiver Motorwirkungsgrad ($\eta_{\text{e}}$)**: 30 % (Ottomotor bei Nennleistung)

Diese Werte sind essenziell für genaue Berechnungen und helfen dabei, den Leistungsbedarf und den Kraftstoffverbrauch eines Fahrzeugs realistisch einzuschätzen.

# Erklärung der Aufgabe 5

**Frage:** *Was sind typische Zahlenwerte, um den Leistungsbedarf eines Pkw zu berechnen?*

## Ziel der Aufgabe

Die Aufgabe fordert eine Zusammenstellung und Erklärung der typischen physikalischen Größen und Fahrzeugparameter, die bei der Berechnung des Leistungsbedarfs eines Personenkraftwagens (Pkw) verwendet werden. Diese Werte sind essentiell, um realistische und genaue Berechnungen durchführen zu können.

## Hintergrundinformationen

Bei der Berechnung des Leistungsbedarfs eines Pkw müssen verschiedene Widerstandskräfte berücksichtigt werden, die das Fahrzeug während der Fahrt überwinden muss. Die Hauptwiderstände sind:

1. **Luftwiderstandskraft ($F_{\text{cw}}$)**
2. **Rollwiderstandskraft ($F_{\text{roll}}$)**
3. **Steigungskraft ($F_{\text{steig}}$)** (wird auf ebener Strecke vernachlässigt)

Die Gesamtwiderstandskraft ($F_{\text{ges}}$) ist die Summe dieser Kräfte:

$$
F_{\text{ges}} = F_{\text{cw}} + F_{\text{roll}} + F_{\text{steig}}
$$

Auf ebener Strecke vereinfacht sich dies zu:

$$
F_{\text{ges}} = F_{\text{cw}} + F_{\text{roll}}
$$

Um den Leistungsbedarf ($P_{\text{Motor}}$) zu ermitteln, wird die Gesamtwiderstandskraft mit der Geschwindigkeit multipliziert und durch den Getriebewirkungsgrad ($\eta_{\text{Getriebe}}$) dividiert:

$$
P_{\text{Motor}} = \frac{F_{\text{ges}} \cdot v_{\text{Auto}}}{\eta_{\text{Getriebe}}}
$$

## Bedeutung der typischen Zahlenwerte

Typische Zahlenwerte sind notwendig, um die Berechnungen auf realistischen und praxisnahen Daten zu basieren. Sie ermöglichen es, den Leistungsbedarf für verschiedene Fahrzeugtypen und Fahrbedingungen abzuschätzen und zu vergleichen.

## Typische Zahlenwerte für die Berechnung des Leistungsbedarfs

### 1. **Luftwiderstandsbeiwert ($c_{\text{w}}$)**

- **Definition:** Beschreibt die aerodynamische Effizienz des Fahrzeugs. Ein niedrigerer Wert bedeutet geringeren Luftwiderstand.
- **Typische Werte:**
  - **Kompaktwagen:** $c_{\text{w}} = 0{,}29$ bis $0{,}32$
  - **Limousinen:** $c_{\text{w}} = 0{,}25$ bis $0{,}28$
  - **SUVs und Geländewagen:** $c_{\text{w}} = 0{,}35$ bis $0{,}40$

### 2. **Stirnfläche des Fahrzeugs ($A$)**

- **Definition:** Die projizierte Frontfläche des Fahrzeugs in Fahrtrichtung, gemessen in Quadratmetern ($\text{m}^2$).
- **Typische Werte:**
  - **Kleinwagen:** $A = 2{,}0~\text{m}^2$
  - **Mittelklassewagen:** $A = 2{,}2~\text{m}^2$
  - **Oberklassewagen/SUVs:** $A = 2{,}5~\text{m}^2$ bis $3{,}0~\text{m}^2$
- **Berechnungshinweis:** Stirnfläche entspricht etwa 85 % der Rechteckfläche aus Fahrzeugbreite und -höhe.

### 3. **Rollwiderstandsbeiwert ($\mu$)**

- **Definition:** Beschreibt den Rollwiderstand der Reifen auf der Fahrbahn.
- **Typische Werte:**
  - **Standardreifen:** $\mu = 0{,}015$
  - **Energiesparreifen:** $\mu = 0{,}010$ bis $0{,}012$
  - **Geländereifen:** $\mu = 0{,}020$ oder höher

### 4. **Getriebewirkungsgrad ($\eta_{\text{Getriebe}}$)**

- **Definition:** Beschreibt die Effizienz des Antriebsstrangs bei der Übertragung der Motorleistung auf die Räder.
- **Typische Werte:**
  - **Schaltgetriebe:** $\eta_{\text{Getriebe}} = 0{,}95$
  - **Automatikgetriebe:** $\eta_{\text{Getriebe}} = 0{,}90$ bis $0{,}92$

### 5. **Effektiver Motorwirkungsgrad ($\eta_{\text{e}}$)**

- **Definition:** Gibt den Anteil der im Kraftstoff enthaltenen Energie an, der in mechanische Arbeit umgewandelt wird.
- **Typische Werte:**
  - **Ottomotoren bei Nennleistung:** $\eta_{\text{e}} = 0{,}30$ (30 %)
  - **Dieselmotoren bei Nennleistung:** $\eta_{\text{e}} = 0{,}35$ (35 %)
  - **Im Bestpunkt (hohe Last, mittlere Drehzahl):**
    - **Ottomotor:** $\eta_{\text{e}} = 0{,}37$
    - **Dieselmotor:** $\eta_{\text{e}} = 0{,}42$
  - **Im Stadtverkehr (Teillastbetrieb):**
    - **Ottomotor:** $\eta_{\text{e}} = 0{,}10$ bis $0{,}15$
    - **Dieselmotor:** $\eta_{\text{e}} = 0{,}20$
  - **Leerlauf:** $\eta_{\text{e}} = 0$

### 6. **Luftdichte ($\rho$)**

- **Definition:** Masse pro Volumeneinheit der Luft.
- **Typische Werte:**
  - **Standardbedingungen (20 °C, 1 bar):** $\rho = 1{,}2041~\frac{\text{kg}}{\text{m}^3}$

### 7. **Erdbeschleunigung ($g$)**

- **Definition:** Beschleunigung, die auf ein Objekt aufgrund der Erdanziehung wirkt.
- **Wert:** $g = 9{,}81~\frac{\text{m}}{\text{s}^2}$

### 8. **Fahrzeugmasse ($m$)**

- **Definition:** Gesamtmasse des Fahrzeugs inklusive Insassen und Gepäck.
- **Typische Werte:**
  - **Kleinwagen:** $m = 1\,000$ bis $1\,200~\text{kg}$
  - **Mittelklassewagen:** $m = 1\,300$ bis $1\,600~\text{kg}$
  - **Oberklasse/SUVs:** $m = 1\,800$ bis $2\,500~\text{kg}$

## Anwendung dieser Werte in den Berechnungen

### **1. Luftwiderstandskraft ($F_{\text{cw}}$)**

Die Luftwiderstandskraft wird berechnet mit:

$$
F_{\text{cw}} = \frac{1}{2} \cdot \rho \cdot v_{\text{Auto}}^2 \cdot c_{\text{w}} \cdot A
$$

- **Einflussfaktoren:**
  - **Geschwindigkeit ($v_{\text{Auto}}$)**: Quadratischer Einfluss auf $F_{\text{cw}}$
  - **Luftwiderstandsbeiwert ($c_{\text{w}}$)**: Direkter Einfluss; geringerer $c_{\text{w}}$ reduziert $F_{\text{cw}}$
  - **Stirnfläche ($A$)**: Größere Fläche erhöht $F_{\text{cw}}$

### **2. Rollwiderstandskraft ($F_{\text{roll}}$)**

Die Rollwiderstandskraft wird berechnet mit:

$$
F_{\text{roll}} = \mu \cdot m \cdot g
$$

- **Einflussfaktoren:**
  - **Rollwiderstandsbeiwert ($\mu$)**: Direkter Einfluss; geringerer $\mu$ reduziert $F_{\text{roll}}$
  - **Fahrzeugmasse ($m$)**: Höhere Masse erhöht $F_{\text{roll}}$
  - **Erdbeschleunigung ($g$)**: Konstant, aber essentiell für die Berechnung

### **3. Gesamtwiderstandskraft ($F_{\text{ges}}$)**

$$
F_{\text{ges}} = F_{\text{cw}} + F_{\text{roll}}
$$

### **4. Erforderliche Motorleistung ($P_{\text{Motor}}$)**

$$
P_{\text{Motor}} = \frac{F_{\text{ges}} \cdot v_{\text{Auto}}}{\eta_{\text{Getriebe}}}
$$

- **Getriebewirkungsgrad ($\eta_{\text{Getriebe}}$)** berücksichtigt Verluste im Antriebsstrang

### **5. Kraftstoffverbrauch und Motorwirkungsgrad**

Der effektive Motorwirkungsgrad ($\eta_{\text{e}}$) ist entscheidend für die Umrechnung der erforderlichen Motorleistung in den Kraftstoffverbrauch.

$$
\dot{m}_{\text{B}} = \frac{P_{\text{Motor}}}{\eta_{\text{e}} \cdot H_{\text{U}}}
$$

- **$\dot{m}_{\text{B}}$:** Kraftstoffmassenstrom
- **$H_{\text{U}}$:** Heizwert des Kraftstoffs (z. B. $42\,000~\text{kJ/kg}$ für Benzin)

## Beispielrechnung

Angenommen, wir wollen den Leistungsbedarf eines Mittelklasse-Pkw bei einer Geschwindigkeit von $100~\text{km/h}$ berechnen.

**Gegebene Werte:**

- **Geschwindigkeit:** $v_{\text{Auto}} = 100~\text{km/h} = 27{,}78~\text{m/s}$
- **Luftdichte:** $\rho = 1{,}2041~\frac{\text{kg}}{\text{m}^3}$
- **Luftwiderstandsbeiwert:** $c_{\text{w}} = 0{,}30$
- **Stirnfläche:** $A = 2{,}2~\text{m}^2$
- **Rollwiderstandsbeiwert:** $\mu = 0{,}015$
- **Fahrzeugmasse:** $m = 1\,500~\text{kg}$
- **Erdbeschleunigung:** $g = 9{,}81~\frac{\text{m}}{\text{s}^2}$
- **Getriebewirkungsgrad:** $\eta_{\text{Getriebe}} = 0{,}90$
- **Effektiver Motorwirkungsgrad:** $\eta_{\text{e}} = 0{,}30$ (bei Nennleistung)

**Berechnung der Luftwiderstandskraft:**

$$
\begin{align*}
F_{\text{cw}} &= \frac{1}{2} \cdot \rho \cdot v_{\text{Auto}}^2 \cdot c_{\text{w}} \cdot A \\
&= 0{,}5 \cdot 1{,}2041~\frac{\text{kg}}{\text{m}^3} \cdot (27{,}78~\text{m/s})^2 \cdot 0{,}30 \cdot 2{,}2~\text{m}^2 \\
&= 719{,}3~\text{N}
\end{align*}
$$

**Berechnung der Rollwiderstandskraft:**

$$
F_{\text{roll}} = \mu \cdot m \cdot g = 0{,}015 \cdot 1\,500~\text{kg} \cdot 9{,}81~\frac{\text{m}}{\text{s}^2} = 220{,}7~\text{N}
$$

**Gesamtwiderstandskraft:**

$$
F_{\text{ges}} = F_{\text{cw}} + F_{\text{roll}} = 719{,}3~\text{N} + 220{,}7~\text{N} = 940~\text{N}
$$

**Erforderliche Motorleistung:**

$$
P_{\text{Motor}} = \frac{F_{\text{ges}} \cdot v_{\text{Auto}}}{\eta_{\text{Getriebe}}} = \frac{940~\text{N} \cdot 27{,}78~\text{m/s}}{0{,}90} \approx 29\,000~\text{W} = 29~\text{kW}
$$

**Berechnung des Kraftstoffmassenstroms:**

$$
\dot{m}_{\text{B}} = \frac{P_{\text{Motor}}}{\eta_{\text{e}} \cdot H_{\text{U}}} = \frac{29\,000~\text{W}}{0{,}30 \cdot 42\,000\,000~\text{J/kg}} \approx 2{,}30 \times 10^{-3}~\text{kg/s}
$$

**Umrechnung in Liter pro 100 km:**

- **Kraftstoffdichte:** $\rho_{\text{B}} = 0{,}76~\frac{\text{kg}}{\text{l}}$
- **Geschwindigkeit:** $v_{\text{Auto}} = 100~\text{km/h}$

$$
\begin{align*}
\dot{V}_{\text{B}} &= \frac{\dot{m}_{\text{B}}}{\rho_{\text{B}}} = \frac{2{,}30 \times 10^{-3}~\text{kg/s}}{0{,}76~\text{kg/l}} = 3{,}03 \times 10^{-3}~\text{l/s} \\
\text{Verbrauch } V_{\text{S}} &= \dot{V}_{\text{B}} \cdot \frac{3600~\text{s}}{v_{\text{Auto}}} \cdot 100~\text{km} \\
&= 3{,}03 \times 10^{-3}~\text{l/s} \cdot \frac{3600~\text{s}}{100~\text{km}} \cdot 100~\text{km} = 10{,}9~\text{l/100 km}
\end{align*}
$$

## Zusammenfassung

- **Typische Zahlenwerte** sind unerlässlich für realistische Leistungsberechnungen bei Pkw.
- **Luftwiderstandsbeiwert ($c_{\text{w}}$)** und **Stirnfläche ($A$)** beeinflussen maßgeblich den Luftwiderstand.
- **Rollwiderstandsbeiwert ($\mu$)** und **Fahrzeugmasse ($m$)** bestimmen den Rollwiderstand.
- **Getriebewirkungsgrad ($\eta_{\text{Getriebe}}$)** und **Motorwirkungsgrad ($\eta_{\text{e}}$)** sind entscheidend für die tatsächliche Motorleistung und den Kraftstoffverbrauch.
- **Standardwerte** ermöglichen Vergleiche zwischen verschiedenen Fahrzeugen und Fahrbedingungen.

**Praktische Bedeutung:**

- **Fahrzeugentwicklung:** Optimierung dieser Parameter führt zu effizienteren Fahrzeugen.
- **Kraftstoffverbrauch:** Kenntnis der Einflussgrößen hilft Fahrern, den Verbrauch durch angepasstes Fahrverhalten zu reduzieren.
- **Umweltaspekte:** Effizientere Fahrzeuge tragen zur Reduktion von Emissionen bei.

# Könnte man mit einem modernen Fahrzeug einen Kraftstoffverbrauch von $1~\text{l}/(100~\text{km})$ realisieren?

## Ziel der Aufgabe

Die Aufgabe besteht darin zu untersuchen, ob es möglich ist, mit einem modernen Fahrzeug einen Kraftstoffverbrauch von $1~\text{l}/(100~\text{km})$ zu erreichen. Dabei sollen die technischen Anforderungen und Herausforderungen analysiert werden, die notwendig sind, um ein solches Fahrzeug zu realisieren.

## Hintergrundinformationen

Ein Kraftstoffverbrauch von $1~\text{l}/(100~\text{km})$ ist extrem niedrig und stellt eine große Herausforderung dar. Um zu prüfen, ob dies möglich ist, müssen wir die Faktoren betrachten, die den Kraftstoffverbrauch beeinflussen:

1. **Fahrwiderstände:**
   - **Rollwiderstand**
   - **Luftwiderstand**

2. **Fahrzeugparameter:**
   - **Fahrzeugmasse**
   - **Stirnfläche ($A$)**
   - **Luftwiderstandsbeiwert ($c_{\text{w}}$)**
   - **Rollwiderstandsbeiwert ($\mu$)**

3. **Antriebsstrang und Wirkungsgrade:**
   - **Getriebewirkungsgrad ($\eta_{\text{Getriebe}}$)**
   - **Effektiver Motorwirkungsgrad ($\eta_{\text{e}}$)**

4. **Fahrgeschwindigkeit:**
   - Bei welcher Geschwindigkeit kann ein solcher Verbrauch erreicht werden?

## Vorgehensweise zur Lösung

1. **Festlegen der Fahrzeugparameter:**
   - Wählen von realistischen, aber optimierten Werten für die Fahrzeugparameter.

2. **Berechnung der Fahrwiderstände:**
   - Rollwiderstandskraft ($F_{\text{roll}}$)
   - Luftwiderstandskraft ($F_{\text{cw}}$)

3. **Berechnung der erforderlichen Radleistung ($P_{\text{Rad}}$)**

4. **Berücksichtigung der Wirkungsgrade:**
   - Bestimmung der erforderlichen Motorleistung ($P_{\text{Motor}}$)

5. **Berechnung des Kraftstoffverbrauchs:**
   - Ermittlung des Kraftstoffmassenstroms ($\dot{m}_{\text{B}}$)
   - Berechnung des streckenbezogenen Kraftstoffverbrauchs ($V_{\text{S}}$)

6. **Analyse der Ergebnisse:**
   - Beurteilung, ob der Verbrauch von $1~\text{l}/(100~\text{km})$ realisierbar ist.
   - Identifikation der notwendigen technischen Maßnahmen.

## Schritt-für-Schritt-Lösung

### 1. Festlegen der Fahrzeugparameter

Wir verwenden optimierte Werte für ein besonders sparsames Fahrzeug (basierend auf den Angaben aus dem Kapitel):

- **Luftwiderstandsbeiwert ($c_{\text{w}}$)**: 0,25
- **Stirnfläche ($A$)**: 1,8 m² (kleinere Fläche durch schmales Fahrzeugdesign)
- **Rollwiderstandsbeiwert ($\mu$)**: 0,008 (sehr niedriger Wert durch spezielle Reifen)
- **Fahrzeugmasse ($m$)**: 1.000 kg (durch Leichtbau)
- **Getriebewirkungsgrad ($\eta_{\text{Getriebe}}$)**: 0,95
- **Effektiver Motorwirkungsgrad ($\eta_{\text{e}}$)**: 0,42 (hoch effizienter Dieselmotor)
- **Luftdichte ($\rho$)**: 1,2041 kg/m³ (Standardbedingungen)

### 2. Berechnung der Fahrwiderstände

Wir wählen mehrere Geschwindigkeiten, um den Einfluss zu untersuchen, z. B. 30 km/h, 50 km/h, 80 km/h und 100 km/h.

#### Umrechnung der Geschwindigkeiten in m/s

$$
v = \frac{\text{Geschwindigkeit in km/h}}{3{,}6}
$$

- **30 km/h**: $v = \frac{30}{3{,}6} = 8{,}33~\text{m/s}$
- **50 km/h**: $v = \frac{50}{3{,}6} = 13{,}89~\text{m/s}$
- **80 km/h**: $v = \frac{80}{3{,}6} = 22{,}22~\text{m/s}$
- **100 km/h**: $v = \frac{100}{3{,}6} = 27{,}78~\text{m/s}$

#### a) Rollwiderstandskraft ($F_{\text{roll}}$)

$$
F_{\text{roll}} = \mu \cdot m \cdot g
$$

Mit $g = 9{,}81~\text{m/s}^2$:

$$
F_{\text{roll}} = 0{,}008 \cdot 1\,000~\text{kg} \cdot 9{,}81~\text{m/s}^2 = 78{,}48~\text{N}
$$

*Die Rollwiderstandskraft ist konstant, da sie von der Geschwindigkeit unabhängig ist.*

#### b) Luftwiderstandskraft ($F_{\text{cw}}$)

$$
F_{\text{cw}} = \frac{1}{2} \cdot \rho \cdot c_{\text{w}} \cdot A \cdot v^2
$$

Berechnungen für die einzelnen Geschwindigkeiten:

**Bei 30 km/h (8,33 m/s):**

$$
F_{\text{cw}} = 0{,}5 \cdot 1{,}2041 \cdot 0{,}25 \cdot 1{,}8 \cdot (8{,}33)^2 = 18{,}77~\text{N}
$$

**Bei 50 km/h (13,89 m/s):**

$$
F_{\text{cw}} = 0{,}5 \cdot 1{,}2041 \cdot 0{,}25 \cdot 1{,}8 \cdot (13{,}89)^2 = 78{,}21~\text{N}
$$

**Bei 80 km/h (22,22 m/s):**

$$
F_{\text{cw}} = 0{,}5 \cdot 1{,}2041 \cdot 0{,}25 \cdot 1{,}8 \cdot (22{,}22)^2 = 200{,}98~\text{N}
$$

**Bei 100 km/h (27,78 m/s):**

$$
F_{\text{cw}} = 0{,}5 \cdot 1{,}2041 \cdot 0{,}25 \cdot 1{,}8 \cdot (27{,}78)^2 = 314{,}55~\text{N}
$$

### 3. Berechnung der erforderlichen Radleistung ($P_{\text{Rad}}$)

$$
P_{\text{Rad}} = (F_{\text{roll}} + F_{\text{cw}}) \cdot v
$$

**Berechnungen:**

**Bei 30 km/h:**

$$
P_{\text{Rad}} = (78{,}48 + 18{,}77)~\text{N} \cdot 8{,}33~\text{m/s} = 806{,}6~\text{W}
$$

**Bei 50 km/h:**

$$
P_{\text{Rad}} = (78{,}48 + 78{,}21)~\text{N} \cdot 13{,}89~\text{m/s} = 2\,179{,}5~\text{W}
$$

**Bei 80 km/h:**

$$
P_{\text{Rad}} = (78{,}48 + 200{,}98)~\text{N} \cdot 22{,}22~\text{m/s} = 6\,215{,}1~\text{W}
$$

**Bei 100 km/h:**

$$
P_{\text{Rad}} = (78{,}48 + 314{,}55)~\text{N} \cdot 27{,}78~\text{m/s} = 10\,928{,}8~\text{W}
$$

### 4. Berücksichtigung der Wirkungsgrade

**Erforderliche Motorleistung ($P_{\text{Motor}}$)**

$$
P_{\text{Motor}} = \frac{P_{\text{Rad}}}{\eta_{\text{Getriebe}}} = \frac{P_{\text{Rad}}}{0{,}95}
$$

**Berechnungen:**

**Bei 30 km/h:**

$$
P_{\text{Motor}} = \frac{806{,}6}{0{,}95} = 849{,}1~\text{W}
$$

**Bei 50 km/h:**

$$
P_{\text{Motor}} = \frac{2\,179{,}5}{0{,}95} = 2\,294{,}2~\text{W}
$$

**Bei 80 km/h:**

$$
P_{\text{Motor}} = \frac{6\,215{,}1}{0{,}95} = 6\,542{,}2~\text{W}
$$

**Bei 100 km/h:**

$$
P_{\text{Motor}} = \frac{10\,928{,}8}{0{,}95} = 11\,504{,}0~\text{W}
$$

### 5. Berechnung des Kraftstoffverbrauchs

#### a) Kraftstoffmassenstrom ($\dot{m}_{\text{B}}$)

$$
\dot{m}_{\text{B}} = \frac{P_{\text{Motor}}}{\eta_{\text{e}} \cdot H_{\text{U}}}
$$

- **Heizwert von Dieselkraftstoff ($H_{\text{U}}$)**: 42.600 kJ/kg
- **Effektiver Motorwirkungsgrad ($\eta_{\text{e}} = 0{,}42$)**

**Berechnungen:**

**Bei 30 km/h:**

$$
\dot{m}_{\text{B}} = \frac{849{,}1~\text{W}}{0{,}42 \cdot 42\,600\,\text{J/g}} = \frac{849{,}1}{17\,892} \approx 0{,}0475~\text{g/s}
$$

**Bei 50 km/h:**

$$
\dot{m}_{\text{B}} = \frac{2\,294{,}2}{17\,892} \approx 0{,}1282~\text{g/s}
$$

**Bei 80 km/h:**

$$
\dot{m}_{\text{B}} = \frac{6\,542{,}2}{17\,892} \approx 0{,}3655~\text{g/s}
$$

**Bei 100 km/h:**

$$
\dot{m}_{\text{B}} = \frac{11\,504{,}0}{17\,892} \approx 0{,}6431~\text{g/s}
$$

#### b) Umrechnung in Verbrauch pro Stunde

$$
\dot{m}_{\text{B, h}} = \dot{m}_{\text{B}} \cdot 3\,600~\text{s/h}
$$

**Bei 30 km/h:**

$$
\dot{m}_{\text{B, h}} = 0{,}0475~\text{g/s} \cdot 3\,600 = 171~\text{g/h}
$$

**Bei 50 km/h:**

$$
\dot{m}_{\text{B, h}} = 0{,}1282~\text{g/s} \cdot 3\,600 = 461{,}4~\text{g/h}
$$

**Bei 80 km/h:**

$$
\dot{m}_{\text{B, h}} = 0{,}3655~\text{g/s} \cdot 3\,600 = 1\,316~\text{g/h}
$$

**Bei 100 km/h:**

$$
\dot{m}_{\text{B, h}} = 0{,}6431~\text{g/s} \cdot 3\,600 = 2\,315~\text{g/h}
$$

#### c) Berechnung des streckenbezogenen Kraftstoffverbrauchs ($V_{\text{S}}$)

$$
V_{\text{S}} = \frac{\dot{m}_{\text{B, h}}}{\rho_{\text{B}}} \cdot \frac{100~\text{km}}{v_{\text{Auto}} \cdot 1~\text{h}}
$$

- **Dichte von Dieselkraftstoff ($\rho_{\text{B}}$)**: 0,84 kg/l

**Berechnungen:**

**Bei 30 km/h:**

$$
V_{\text{S}} = \frac{0{,}171~\text{kg/h}}{0{,}84~\text{kg/l}} \cdot \frac{100~\text{km}}{30~\text{km}} = 0{,}68~\text{l/100 km}
$$

**Bei 50 km/h:**

$$
V_{\text{S}} = \frac{0{,}4614}{0{,}84} \cdot \frac{100}{50} = 1{,}10~\text{l/100 km}
$$

**Bei 80 km/h:**

$$
V_{\text{S}} = \frac{1{,}316}{0{,}84} \cdot \frac{100}{80} = 1{,}96~\text{l/100 km}
$$

**Bei 100 km/h:**

$$
V_{\text{S}} = \frac{2{,}315}{0{,}84} \cdot \frac{100}{100} = 2{,}75~\text{l/100 km}
$$

### 6. Analyse der Ergebnisse

- **Bei niedrigen Geschwindigkeiten** (30 km/h) ist ein Verbrauch von unter $1~\text{l/100 km}$ erreichbar.
- **Bei 50 km/h** liegt der Verbrauch knapp über $1~\text{l/100 km}$.
- **Bei höheren Geschwindigkeiten** steigt der Verbrauch deutlich an und überschreitet $1~\text{l/100 km}$ erheblich.
- **Gründe dafür:**
  - Der **Luftwiderstand** nimmt mit dem Quadrat der Geschwindigkeit zu und wird zum dominierenden Faktor.
  - Selbst bei optimierten Fahrzeugparametern ist der Verbrauch bei höheren Geschwindigkeiten nicht auf $1~\text{l/100 km}$ zu reduzieren.

### 7. Notwendige technische Maßnahmen

Um einen Verbrauch von $1~\text{l/100 km}$ auch bei höheren Geschwindigkeiten zu erreichen, wären weitere Maßnahmen erforderlich:

- **Gewichtsreduktion:**
  - Einsatz von Leichtbaumaterialien wie CFK (carbonfaserverstärkter Kunststoff).
  - Verzicht auf schwere Komfortausstattungen.
- **Aerodynamik verbessern:**
  - Weitere Reduzierung des $c_{\text{w}}$-Werts.
  - Verkleinerung der Stirnfläche durch schmaleres und niedrigeres Fahrzeugdesign.
- **Reduzierung des Rollwiderstands:**
  - Verwendung von speziellen Reifen mit noch niedrigerem $\mu$.
- **Effizientere Antriebssysteme:**
  - Einsatz von Hybrid- oder Elektroantrieben.
  - Nutzung von Rekuperation (Energierückgewinnung beim Bremsen).
- **Fahrzeugkonzept ändern:**
  - Zwei hintereinanderliegende Sitze anstatt nebeneinander.
  - Kompaktere Fahrzeugabmessungen.

## Antwort auf die Frage

Es ist theoretisch möglich, mit einem modernen Fahrzeug einen Kraftstoffverbrauch von $1~\text{l/100 km}$ zu realisieren, jedoch nur unter bestimmten Bedingungen:

- **Bei niedrigen Geschwindigkeiten** (unter 50 km/h) ist dieser Verbrauch erreichbar, insbesondere bei konstantem Fahren und optimaler Getriebeabstimmung.
- **Bei höheren Geschwindigkeiten** wird es sehr schwierig, diesen Verbrauch zu erreichen, selbst mit optimierten Fahrzeugparametern.
- **Erforderlich sind unkonventionelle Fahrzeugkonzepte**, die erhebliche Änderungen in Design, Gewicht, Aerodynamik und Antrieb erfordern.

**Zusammenfassung:**

Ein Kraftstoffverbrauch von $1~\text{l/100 km}$ kann nur mit neuen Fahrzeugkonzepten realisiert werden, die leichte Materialien, herausragende Aerodynamik und hocheffiziente Antriebssysteme nutzen. Dies erfordert Kompromisse bei Komfort, Größe und möglicherweise Sicherheit.

## Fazit

Die Realisierung eines Kraftstoffverbrauchs von $1~\text{l/100 km}$ mit einem modernen Fahrzeug ist eine große technische Herausforderung. Es erfordert innovative Ansätze in der Fahrzeugentwicklung und möglicherweise eine Neudefinition dessen, was wir von einem Auto erwarten. Projekte wie der Volkswagen XL1 zeigen, dass solche Fahrzeuge technisch möglich sind, jedoch oft mit hohen Kosten und Einschränkungen verbunden sind.

# Erklärung der Aufgabe 6

**Frage:** *Könnte man mit einem modernen Fahrzeug einen Kraftstoffverbrauch von $1~\text{l}/(100~\text{km})$ realisieren?*

## Ziel der Aufgabe

Die Aufgabe zielt darauf ab, zu untersuchen, ob es technisch möglich ist, mit einem modernen Fahrzeug einen extrem niedrigen Kraftstoffverbrauch von **1 Liter pro 100 Kilometer** zu erreichen. Es soll analysiert werden, welche Faktoren den Kraftstoffverbrauch beeinflussen und ob durch technologische Fortschritte und optimierte Fahrzeugkonstruktion ein solch geringer Verbrauch realisierbar ist.

## Hintergrundinformationen

### Bedeutung des Kraftstoffverbrauchs

Der Kraftstoffverbrauch eines Fahrzeugs ist ein entscheidender Faktor für:

- **Betriebskosten**: Ein niedriger Verbrauch reduziert die Kosten für den Fahrer.
- **Umweltverträglichkeit**: Weniger Kraftstoffverbrauch bedeutet geringere CO₂-Emissionen und einen kleineren ökologischen Fußabdruck.
- **Energieeffizienz**: Effiziente Fahrzeuge tragen zur Ressourcenschonung bei und reduzieren die Abhängigkeit von fossilen Brennstoffen.

### Aktuelle Standards und Herausforderungen

- **Durchschnittlicher Verbrauch**: Moderne Pkw verbrauchen typischerweise zwischen 4 l/100 km (für sehr effiziente Dieselfahrzeuge) und 8 l/100 km (für größere Benzinfahrzeuge).
- **Technologische Grenzen**: Die Reduzierung des Verbrauchs auf 1 l/100 km stellt eine erhebliche Herausforderung dar, da sie weit unter dem aktuellen Durchschnitt liegt.
- **Regulatorische Anforderungen**: Gesetzgeber weltweit setzen strengere Emissions- und Verbrauchsstandards, was die Automobilindustrie zu Innovationen antreibt.

## Faktoren, die den Kraftstoffverbrauch beeinflussen

1. **Fahrwiderstände**:

   - **Rollwiderstand ($F_{\text{roll}}$)**:
     - Entsteht durch die Verformung der Reifen und die Reibung zwischen Reifen und Straße.
     - Abhängig von:
       - **Rollwiderstandsbeiwert ($\mu$)**: Kann durch spezielle Reifenmaterialien und -konstruktionen reduziert werden.
       - **Fahrzeugmasse ($m$)**: Leichtere Fahrzeuge haben einen geringeren Rollwiderstand.

   - **Luftwiderstand ($F_{\text{cw}}$)**:
     - Entsteht durch den Widerstand der Luft gegen die Bewegung des Fahrzeugs.
     - Abhängig von:
       - **Luftwiderstandsbeiwert ($c_{\text{w}}$)**: Wird durch die aerodynamische Form des Fahrzeugs bestimmt.
       - **Stirnfläche ($A$)**: Kleinere und flachere Fahrzeuge haben eine geringere Stirnfläche.
       - **Fahrzeuggeschwindigkeit ($v$)**: Der Luftwiderstand steigt quadratisch mit der Geschwindigkeit.

2. **Antriebssystem**:

   - **Effektiver Motorwirkungsgrad ($\eta_{\text{e}}$)**:
     - Gibt an, wie effizient der Motor die im Kraftstoff enthaltene Energie in mechanische Arbeit umwandelt.
     - Kann durch Technologien wie **Hybridisierung**, **Downsizing**, **Turboaufladung** und **Verbesserung der Verbrennung** gesteigert werden.

   - **Getriebewirkungsgrad ($\eta_{\text{Getriebe}}$)**:
     - Verluste im Antriebsstrang können durch optimierte Getriebe und Schmierstoffe minimiert werden.

3. **Gewicht und Größe des Fahrzeugs**:

   - **Leichtbauweise**:
     - Verwendung von Materialien wie Aluminium, Magnesium und kohlenstofffaserverstärktem Kunststoff (CFK) reduziert das Fahrzeuggewicht.
     - Leichtere Fahrzeuge benötigen weniger Energie, um beschleunigt und bewegt zu werden.

4. **Fahrweise und Betriebsbedingungen**:

   - **Konstante Geschwindigkeit**:
     - Konstant gleichmäßiges Fahren verbraucht weniger Kraftstoff als häufiges Beschleunigen und Bremsen.
   - **Niedrige Geschwindigkeiten**:
     - Bei niedrigen Geschwindigkeiten dominiert der Rollwiderstand; der Luftwiderstand ist geringer.

## Theoretische Machbarkeit eines Verbrauchs von 1 l/100 km

### Berechnungsgrundlagen

Um zu beurteilen, ob ein Verbrauch von 1 l/100 km realisierbar ist, müssen wir die **erforderliche Motorleistung** und den **Kraftstoffverbrauch** bei einer bestimmten Fahrgeschwindigkeit berechnen.

#### 1. **Rollwiderstandskraft ($F_{\text{roll}}$)**

$$
F_{\text{roll}} = \mu \cdot m \cdot g
$$

- **$\mu$**: Rollwiderstandsbeiwert (typisch $0{,}008$ für Spezialreifen)
- **$m$**: Fahrzeugmasse (ein sehr leichtes Fahrzeug könnte $500~\text{kg}$ wiegen)
- **$g$**: Erdbeschleunigung ($9{,}81~\text{m/s}^2$)

#### 2. **Luftwiderstandskraft ($F_{\text{cw}}$)**

$$
F_{\text{cw}} = \frac{1}{2} \cdot \rho \cdot c_{\text{w}} \cdot A \cdot v^2
$$

- **$\rho$**: Luftdichte ($1{,}2041~\text{kg/m}^3$)
- **$c_{\text{w}}$**: Sehr niedriger Wert, z. B. $0{,}19$ (für extrem aerodynamische Fahrzeuge)
- **$A$**: Stirnfläche (möglichst klein, z. B. $1{,}0~\text{m}^2$)
- **$v$**: Fahrgeschwindigkeit (niedrige Geschwindigkeit bevorzugt, z. B. $45~\text{km/h}$)

#### 3. **Gesamtwiderstandskraft ($F_{\text{ges}}$)**

$$
F_{\text{ges}} = F_{\text{roll}} + F_{\text{cw}}
$$

#### 4. **Erforderliche Radleistung ($P_{\text{Rad}}$)**

$$
P_{\text{Rad}} = F_{\text{ges}} \cdot v
$$

#### 5. **Erforderliche Motorleistung ($P_{\text{Motor}}$)**

$$
P_{\text{Motor}} = \frac{P_{\text{Rad}}}{\eta_{\text{Getriebe}}}
$$

- **$\eta_{\text{Getriebe}}$**: Hoher Wirkungsgrad, z. B. $0{,}98$

#### 6. **Kraftstoffverbrauch**

$$
\dot{m}_{\text{B}} = \frac{P_{\text{Motor}}}{\eta_{\text{e}} \cdot H_{\text{U}}}
$$

- **$\eta_{\text{e}}$**: Sehr hoher Wirkungsgrad, z. B. $0{,}45$ (für Brennstoffzellen oder sehr effiziente Dieselmotoren)
- **$H_{\text{U}}$**: Heizwert des Kraftstoffs ($42\,600~\text{kJ/kg}$ für Diesel)

### Beispielrechnung

**Annahmen:**

- **$\mu = 0{,}008$**
- **$m = 500~\text{kg}$**
- **$c_{\text{w}} = 0{,}19$**
- **$A = 1{,}0~\text{m}^2$**
- **$v = 45~\text{km/h} = 12{,}5~\text{m/s}$**
- **$\eta_{\text{Getriebe}} = 0{,}98$**
- **$\eta_{\text{e}} = 0{,}45$**
- **$H_{\text{U}} = 42\,600~\text{kJ/kg}$**

**1. Rollwiderstandskraft:**

$$
F_{\text{roll}} = 0{,}008 \cdot 500~\text{kg} \cdot 9{,}81~\text{m/s}^2 = 39{,}24~\text{N}
$$

**2. Luftwiderstandskraft:**

$$
F_{\text{cw}} = 0{,}5 \cdot 1{,}2041~\text{kg/m}^3 \cdot 0{,}19 \cdot 1{,}0~\text{m}^2 \cdot (12{,}5~\text{m/s})^2 = 17{,}86~\text{N}
$$

**3. Gesamtwiderstandskraft:**

$$
F_{\text{ges}} = 39{,}24~\text{N} + 17{,}86~\text{N} = 57{,}1~\text{N}
$$

**4. Radleistung:**

$$
P_{\text{Rad}} = 57{,}1~\text{N} \cdot 12{,}5~\text{m/s} = 713{,}75~\text{W}
$$

**5. Motorleistung:**

$$
P_{\text{Motor}} = \frac{713{,}75~\text{W}}{0{,}98} \approx 728{,}32~\text{W}
$$

**6. Kraftstoffverbrauch pro Stunde:**

$$
\dot{m}_{\text{B}} = \frac{728{,}32~\text{W}}{0{,}45 \cdot 42\,600\,\text{J/g}} = \frac{728{,}32}{19\,170} \approx 0{,}038~\text{g/s}
$$

$$
\dot{m}_{\text{B,h}} = 0{,}038~\text{g/s} \cdot 3\,600~\text{s/h} = 136{,}8~\text{g/h}
$$

**7. Verbrauch pro 100 km:**

Bei $45~\text{km/h}$ legt man in einer Stunde $45~\text{km}$ zurück.

$$
\text{Verbrauch pro 100 km} = \frac{136{,}8~\text{g/h}}{0{,}84~\text{kg/l}} \cdot \frac{100~\text{km}}{45~\text{km}} = 0{,}362~\text{l/100 km}
$$

### Interpretation der Ergebnisse

- **Bei niedriger Geschwindigkeit** und mit **extrem optimierten Fahrzeugparametern** ist ein Verbrauch von deutlich unter 1 l/100 km theoretisch möglich.
- **Praktische Umsetzung**: Solche Fahrzeuge müssten sehr leicht und aerodynamisch sein, was in der Praxis zu Einschränkungen bei Komfort, Sicherheit und Nutzbarkeit führen kann.
- **Beispielprojekte**: Der **Volkswagen XL1** war ein Konzeptfahrzeug, das einen Verbrauch von 0,9 l/100 km erreichte, aber mit erheblichen Kompromissen und hohen Kosten verbunden war.

## Praktische Herausforderungen

1. **Sicherheit**:

   - Leichte Fahrzeuge bieten weniger Schutz bei Unfällen.
   - Gesetzliche Sicherheitsstandards erhöhen das Fahrzeuggewicht (Airbags, Knautschzonen).

2. **Komfort und Funktionalität**:

   - Reduzierte Fahrzeuggröße kann den Innenraum einschränken.
   - Ausstattung und Komfortmerkmale erhöhen das Gewicht und den Energieverbrauch.

3. **Kosten**:

   - Leichtbaumaterialien wie CFK sind teuer.
   - Entwicklung und Produktion solcher Fahrzeuge sind kostspielig.

4. **Akzeptanz beim Verbraucher**:

   - Kunden bevorzugen oft größere und komfortablere Fahrzeuge.
   - Reichweitenangst und Leistungseinbußen können abschreckend wirken.

## Alternative Ansätze zur Verbrauchsreduzierung

- **Hybrid- und Elektrofahrzeuge**:

  - Nutzen elektrische Energie und können den Kraftstoffverbrauch reduzieren oder eliminieren.
  - Rekuperation (Energierückgewinnung beim Bremsen) erhöht die Effizienz.

- **Verbesserung der Verbrennungsmotoren**:

  - Downsizing mit Turboaufladung.
  - Variable Ventilsteuerung und Direkteinspritzung.

- **Aerodynamische Optimierungen**:

  - Aktive Aerodynamik (verstellbare Spoiler).
  - Glattere Unterböden und abgedeckte Radkästen.

- **Intelligente Leichtbauweise**:

  - Kombination von Materialien (Stahl, Aluminium, CFK).
  - Strukturoptimierung ohne Kompromisse bei der Sicherheit.

## Zusammenfassung

- **Theoretische Möglichkeit**: Ein Verbrauch von 1 l/100 km ist unter idealisierten Bedingungen und mit radikalen Fahrzeugkonzepten möglich.
- **Praktische Umsetzbarkeit**: In der breiten Masse sind solche Fahrzeuge aufgrund von Kosten, Komfort- und Sicherheitsanforderungen derzeit nicht realistisch.
- **Zukünftige Entwicklungen**: Technologische Fortschritte könnten den Verbrauch weiter senken, aber ein Verbrauch von 1 l/100 km bleibt eine große Herausforderung.
- **Ganzheitlicher Ansatz**: Kombination von Effizienzsteigerungen im Antrieb, Gewichtsreduktion, aerodynamischer Optimierung und alternativen Antrieben ist der Schlüssel zur Reduzierung des Kraftstoffverbrauchs.

## Schlussfolgerung

Es ist äußerst schwierig, mit einem modernen Fahrzeug im alltäglichen Einsatz einen Kraftstoffverbrauch von 1 l/100 km zu realisieren. Während es technisch möglich ist, erfordert dies erhebliche Kompromisse und Innovationen in Design, Materialien und Technologie. Aktuelle Entwicklungen in der Automobilindustrie zielen darauf ab, den Verbrauch zu senken, jedoch bleibt die Erreichung eines solchen niedrigen Verbrauchs eine ambitionierte Zielsetzung.

# Wie effizient sind Pkw-Motoren im Stadtverkehr?

## Ziel der Aufgabe

Die Aufgabe besteht darin, die Effizienz von Pkw-Motoren im Stadtverkehr zu untersuchen. Dabei sollen die spezifischen Bedingungen des Stadtverkehrs analysiert werden, die die Motoreneffizienz beeinflussen, und es soll quantifiziert werden, wie effizient die Motoren tatsächlich arbeiten.

## Hintergrundinformationen

### Motorwirkungsgrad ($\eta_{\text{e}}$)

- **Definition:** Der effektive Motorwirkungsgrad ($\eta_{\text{e}}$) gibt an, welcher Anteil der im Kraftstoff enthaltenen chemischen Energie in nutzbare mechanische Arbeit umgewandelt wird.
- **Typische Werte:**
  - **Ottomotoren:**
    - **Volllast (Nennleistung):** ca. 30 %
    - **Teillast (Stadtverkehr):** 10–15 %
  - **Dieselmotoren:**
    - **Volllast:** ca. 35 %
    - **Teillast:** bis zu 20 %

### Stadtverkehrsbedingungen

- **Niedrige Geschwindigkeiten:** Typischerweise 0–50 km/h
- **Häufiges Anhalten und Anfahren:** Stop-and-go-Verkehr
- **Geringe Lastzustände:** Motor arbeitet oft im Teillastbereich
- **Idling (Leerlauf):** Motor läuft ohne nützliche Arbeit zu verrichten

## Faktoren, die die Effizienz im Stadtverkehr beeinflussen

1. **Teillastbetrieb des Motors**

   - **Ineffiziente Verbrennung:** Bei geringer Last ist die Verbrennung weniger effizient.
   - **Drosselverluste:** Bei Ottomotoren entsteht ein Unterdruck im Ansaugtrakt, was zu zusätzlichen Verlusten führt.

2. **Häufiges Beschleunigen und Bremsen**

   - **Verluste durch Beschleunigung:** Energie wird benötigt, um das Fahrzeug zu beschleunigen.
   - **Verluste durch Bremsen:** Kinetische Energie wird in Wärme umgewandelt und geht verloren (außer bei Rekuperation in Hybrid- oder Elektrofahrzeugen).

3. **Leerlaufverluste**

   - **Kraftstoffverbrauch im Leerlauf:** Motor verbraucht Kraftstoff, ohne dass Arbeit verrichtet wird.
   - **Effizienz im Leerlauf:** $\eta_{\text{e}} = 0$, da keine nutzbare mechanische Arbeit entsteht.

4. **Zusatzverbraucher**

   - **Klimaanlage, Heizung, Beleuchtung:** Erhöhen den Energiebedarf und senken die Gesamtenergieeffizienz.

## Schritt-für-Schritt-Lösung

### 1. Analyse des Motorwirkungsgrads im Stadtverkehr

#### a) Motorbetrieb im Teillastbereich

- **Problem:** Verbrennungsmotoren sind im Teillastbereich weniger effizient.
- **Ursachen:**
  - **Ottomotoren:**
    - Drosselklappenverluste
    - Schlechtere Verbrennung durch geringere Füllung
  - **Dieselmotoren:**
    - Bessere Teillasteffizienz als Ottomotoren, aber immer noch reduziert

- **Effektiver Wirkungsgrad im Stadtverkehr:**
  - **Ottomotoren:** $\eta_{\text{e}} \approx 10–15\,\%$
  - **Dieselmotoren:** $\eta_{\text{e}} \approx 15–20\,\%$

#### b) Einfluss der Fahrwiderstände

- **Rollwiderstandskraft ($F_{\text{roll}}$)** dominiert bei niedrigen Geschwindigkeiten.
- **Luftwiderstandskraft ($F_{\text{cw}}$)** ist weniger relevant, da sie quadratisch mit der Geschwindigkeit steigt.

#### c) Häufiges Anfahren und Bremsen

- **Zusätzlicher Energiebedarf beim Beschleunigen:**
  - **Kinetische Energie ($E_{\text{kin}}$)**:
    $$
    E_{\text{kin}} = \frac{1}{2} \cdot m \cdot v^2
    $$
  - **Diese Energie muss jedes Mal aufgebracht werden, wenn das Fahrzeug beschleunigt.**

- **Verluste beim Bremsen:**
  - **Ohne Rekuperation** geht die Energie als Wärme verloren.
  - **Hybridfahrzeuge** können hier Vorteile bieten.

### 2. Quantitative Betrachtung

#### a) Beispielrechnung für einen Ottomotor im Stadtverkehr

**Annahmen:**

- **Fahrzeugmasse ($m$)**: 1.500 kg
- **Durchschnittliche Geschwindigkeit ($v_{\text{durch}}$)**: 20 km/h (5,56 m/s)
- **Effektiver Motorwirkungsgrad ($\eta_{\text{e}}$)**: 12 %
- **Fahrwiderstände:**
  - **Rollwiderstandskraft ($F_{\text{roll}}$)**:
    $$
    F_{\text{roll}} = \mu \cdot m \cdot g = 0{,}015 \cdot 1\,500\,\text{kg} \cdot 9{,}81\,\text{m/s}^2 = 220{,}725\,\text{N}
    $$
  - **Luftwiderstandskraft ($F_{\text{cw}}$)** (vernachlässigbar bei 20 km/h)

- **Zusätzlicher Energiebedarf durch Beschleunigung:**
  - **Anzahl der Beschleunigungsvorgänge pro km**: 10 (angenommen)
  - **Endgeschwindigkeit bei jedem Beschleunigen**: 50 km/h (13,89 m/s)
  - **Kinetische Energie pro Beschleunigung:**
    $$
    E_{\text{kin}} = \frac{1}{2} \cdot 1\,500\,\text{kg} \cdot (13{,}89\,\text{m/s})^2 = 144{,}9\,\text{kJ}
    $$

- **Gesamte kinetische Energie pro km:**
  $$
  E_{\text{kin,ges}} = 10 \cdot 144{,}9\,\text{kJ} = 1\,449\,\text{kJ}
  $$

- **Arbeit gegen Rollwiderstand pro km:**
  $$
  W_{\text{roll}} = F_{\text{roll}} \cdot s = 220{,}725\,\text{N} \cdot 1\,000\,\text{m} = 220{,}725\,\text{kJ}
  $$

- **Gesamtarbeit pro km:**
  $$
  W_{\text{ges}} = E_{\text{kin,ges}} + W_{\text{roll}} = 1\,449\,\text{kJ} + 220{,}725\,\text{kJ} = 1\,669{,}725\,\text{kJ}
  $$

#### b) Berechnung des Kraftstoffverbrauchs

- **Energiebedarf pro km:**
  $$
  E_{\text{bedarf}} = W_{\text{ges}}
  $$

- **Kraftstoffenergie pro km (unter Berücksichtigung des Wirkungsgrads):**
  $$
  E_{\text{Kraftstoff}} = \frac{E_{\text{bedarf}}}{\eta_{\text{e}}} = \frac{1\,669{,}725\,\text{kJ}}{0{,}12} = 13\,914\,\text{kJ}
  $$

- **Kraftstoffverbrauch pro km:**
  $$
  m_{\text{B,km}} = \frac{E_{\text{Kraftstoff}}}{H_{\text{U}}} = \frac{13\,914\,\text{kJ}}{42\,000\,\text{kJ/kg}} = 0{,}331\,\text{kg}
  $$

- **Kraftstoffverbrauch pro 100 km:**
  $$
  V_{\text{S}} = \frac{0{,}331\,\text{kg}}{0{,}76\,\text{kg/l}} \cdot 100 = 43{,}55\,\text{l/100 km}
  $$

**Anmerkung:** Dieser Verbrauch erscheint extrem hoch. Dies liegt an den vereinfachten Annahmen und der Vernachlässigung von Faktoren wie Rekuperation, realistische Beschleunigungszyklen und die tatsächliche Anzahl von Stopps.

#### c) Realistischerer Ansatz

- **Typischer Stadtverbrauch für Ottomotoren:** 8–12 l/100 km
- **Effektiver Wirkungsgrad daraus abgeleitet:**

  - **Annahme eines Verbrauchs von 10 l/100 km**
  - **Energiegehalt pro 100 km:**
    $$
    E_{\text{Kraftstoff,100km}} = 10\,\text{l} \cdot 0{,}76\,\text{kg/l} \cdot 42\,000\,\text{kJ/kg} = 319\,200\,\text{kJ}
    $$
  - **Nutzarbeit pro 100 km:**
    $$
    W_{\text{nutz}} = \eta_{\text{e}} \cdot E_{\text{Kraftstoff,100km}} = 0{,}12 \cdot 319\,200\,\text{kJ} = 38\,304\,\text{kJ}
    $$
  - **Durchschnittliche Nutzleistung bei 30 km/h:**
    $$
    P_{\text{nutz}} = \frac{W_{\text{nutz}}}{t} = \frac{38\,304\,\text{kJ}}{3\,600\,\text{s} \cdot \frac{100\,\text{km}}{30\,\text{km/h}}} \approx 3{,}19\,\text{kW}
    $$

**Interpretation:** Im Stadtverkehr wird viel Kraftstoff verbraucht, um relativ geringe mechanische Arbeit zu verrichten. Der effektive Motorwirkungsgrad ist niedrig.

### 3. Schlussfolgerungen

- **Niedriger Wirkungsgrad im Stadtverkehr:**
  - **Hauptursachen:**
    - Teillastbetrieb des Motors
    - Häufiges Anfahren und Bremsen
    - Leerlaufzeiten
  - **Folge:** Der effektive Wirkungsgrad liegt deutlich unter dem möglichen Maximum.

- **Vergleich zu anderen Betriebsbedingungen:**
  - **Landstraße/Autobahn:** Höherer Wirkungsgrad durch konstant höhere Lasten
  - **Bestpunktbetrieb:** Wirkungsgrad von bis zu 35 % (Ottomotor) und 42 % (Dieselmotor) möglich

- **Möglichkeiten zur Effizienzsteigerung:**
  - **Start-Stopp-Systeme:** Abschalten des Motors im Leerlauf reduziert Verbrauch
  - **Hybridisierung:**
    - **Mild-Hybride:** Unterstützung des Motors beim Anfahren
    - **Voll-Hybride:** Elektrisches Fahren bei niedrigen Geschwindigkeiten
    - **Rekuperation:** Rückgewinnung von Bremsenergie
  - **Optimierung der Motorsteuerung:**
    - Variable Ventilsteuerung
    - Abschaltung von Zylindern im Teillastbereich
  - **Leichtbau und Aerodynamik:**
    - Reduzierung der Fahrzeugmasse verringert den Energiebedarf beim Beschleunigen
    - Auch im Stadtverkehr relevant

## Antwort auf die Frage

Pkw-Motoren sind im Stadtverkehr **weniger effizient**. Der effektive Motorwirkungsgrad liegt typischerweise bei **10–15 %** für Ottomotoren und **15–20 %** für Dieselmotoren. Hauptgründe dafür sind:

- **Teillastbetrieb:** Motoren arbeiten weit unter ihrer Nennleistung, was zu ineffizienter Verbrennung führt.
- **Häufiges Anfahren und Bremsen:** Energie geht beim Bremsen verloren, Beschleunigung erfordert zusätzlichen Kraftstoff.
- **Leerlaufverluste:** Im Stillstand verbraucht der Motor Kraftstoff, ohne nützliche Arbeit zu verrichten.
- **Zusatzverbraucher:** Klimaanlage, Heizung und andere Systeme erhöhen den Energiebedarf.

Um die Effizienz im Stadtverkehr zu verbessern, sind Technologien wie **Hybridantriebe**, **Start-Stopp-Systeme** und **Rekuperation** wirksam. Sie helfen, die Energieverluste zu minimieren und den Kraftstoffverbrauch zu senken.

## Zusammenfassung

- **Effizienz im Stadtverkehr ist niedrig** aufgrund spezifischer Betriebsbedingungen.
- **Verbesserungspotenzial** besteht durch den Einsatz moderner Technologien.
- **Fahrzeugentwicklung** sollte den Fokus auf Effizienz im Teillastbereich legen.
- **Umweltrelevanz:** Höherer Verbrauch führt zu höheren Emissionen; Verbesserungen tragen zur Umweltentlastung bei.

# Erklärung der Aufgabe 7

**Frage:** *Wie effizient sind Pkw-Motoren im Stadtverkehr?*

## Ziel der Aufgabe

Die Aufgabe zielt darauf ab, die Effizienz von Personenkraftwagen (Pkw)-Motoren im Stadtverkehr zu untersuchen und zu verstehen. Es soll analysiert werden, welche Faktoren die Motoreneffizienz im urbanen Umfeld beeinflussen, warum die Effizienz typischerweise niedriger ist als unter anderen Fahrbedingungen und welche Maßnahmen ergriffen werden können, um die Effizienz zu steigern.

## Hintergrundinformationen

### Definition der Motoreneffizienz

Die **Motoreneffizienz** oder der **effektive Motorwirkungsgrad ($\eta_{\text{e}}$)** gibt an, welcher Anteil der im Kraftstoff enthaltenen chemischen Energie in mechanische Arbeit umgewandelt wird, die zur Fortbewegung des Fahrzeugs genutzt wird.

- **Effektiver Motorwirkungsgrad ($\eta_{\text{e}}$)**:
  $$
  \eta_{\text{e}} = \frac{\text{Nutzleistung}}{\text{aufgenommene chemische Energie}}
  $$
- **Typische Werte:**
  - **Ottomotoren (Benzinmotoren):**
    - **Bei Volllast (Nennleistung):** bis zu 30 %
    - **Im Teillastbetrieb (Stadtverkehr):** 10–15 %
  - **Dieselmotoren:**
    - **Bei Volllast:** bis zu 35 %
    - **Im Teillastbetrieb:** 15–20 %

### Charakteristika des Stadtverkehrs

- **Niedrige Durchschnittsgeschwindigkeit:** Oft unter 30 km/h.
- **Häufiges Anhalten und Anfahren:** Stop-and-go-Verkehr durch Ampeln, Kreuzungen und Staus.
- **Teillastbetrieb des Motors:** Motor arbeitet selten unter optimalen Bedingungen.
- **Leerlaufphasen:** Motor läuft im Stillstand weiter (ohne Start-Stopp-Systeme).
- **Zusatzverbraucher aktiv:** Klimaanlage, Heizung, Beleuchtung und Unterhaltungssysteme.

## Relevanz der Frage

- **Umweltaspekte:** Geringe Effizienz führt zu höherem Kraftstoffverbrauch und höheren CO₂-Emissionen.
- **Wirtschaftliche Aspekte:** Höherer Kraftstoffverbrauch bedeutet höhere Betriebskosten für den Fahrzeughalter.
- **Technologische Entwicklung:** Verständnis der Effizienz ist wichtig für die Weiterentwicklung von Motoren und Fahrzeugen, um den urbanen Anforderungen gerecht zu werden.
- **Politische Rahmenbedingungen:** Strengere Emissionsvorschriften erfordern effizientere Technologien, insbesondere im Stadtverkehr.

## Faktoren, die die Motoreneffizienz im Stadtverkehr beeinflussen

### 1. Teillastbetrieb des Motors

- **Drosselverluste bei Ottomotoren:**
  - Bei geringer Last ist die Drosselklappe teilweise geschlossen.
  - Dies führt zu einem Unterdruck im Ansaugtrakt und erhöhten Pumpverlusten.
- **Ineffiziente Verbrennung:**
  - Geringere Brennraumfüllung führt zu ungünstigen Verbrennungsbedingungen.
  - Der thermodynamische Wirkungsgrad sinkt.
- **Dieselmotoren haben keine Drosselklappe:**
  - Bessere Effizienz im Teillastbereich als Ottomotoren.
  - Trotzdem sinkt der Wirkungsgrad aufgrund anderer Faktoren (z. B. Reibungsverluste).

### 2. Häufiges Anfahren und Bremsen

- **Beschleunigungsphasen:**
  - Erfordern zusätzlichen Energieaufwand, um die kinetische Energie des Fahrzeugs zu erhöhen.
  - Häufiges Beschleunigen erhöht den durchschnittlichen Energieverbrauch.
- **Bremsphasen:**
  - Kinetische Energie wird in Wärme umgewandelt und geht verloren.
  - Ohne Energierückgewinnung (Rekuperation) ist diese Energie verloren.

### 3. Leerlaufverluste

- **Kraftstoffverbrauch im Stillstand:**
  - Motor verbraucht Kraftstoff, ohne dass das Fahrzeug bewegt wird.
  - Wirkungsgrad im Leerlauf ist faktisch Null.
- **Anteil der Leerlaufzeit:**
  - Im Stadtverkehr kann der Leerlaufanteil erheblich sein (Ampeln, Stau).

### 4. Zusatzverbraucher

- **Elektrische Verbraucher:**
  - Klimaanlage, Heizung, Beleuchtung erhöhen den Energiebedarf.
- **Einfluss auf den Motor:**
  - Motor muss zusätzlich Energie bereitstellen, was den Wirkungsgrad weiter senkt.

### 5. Thermische Verluste

- **Motor erreicht nicht die optimale Betriebstemperatur:**
  - Kurzstreckenfahrten verhindern das Aufwärmen des Motors.
  - Kalter Motor hat höhere innere Verluste und schlechtere Verbrennungsbedingungen.

## Ziel der Untersuchung

- **Analyse der tatsächlichen Effizienz:** Quantifizierung des effektiven Motorwirkungsgrads im Stadtverkehr.
- **Identifikation von Verlustquellen:** Verständnis der Hauptfaktoren, die zur geringen Effizienz beitragen.
- **Bewertung von Verbesserungsmaßnahmen:** Betrachtung von Technologien und Strategien zur Effizienzsteigerung.

## Methodik zur Beantwortung der Frage

1. **Definition der Rahmenbedingungen:**
   - Typisches Fahrzeug (Masse, Motorart).
   - Durchschnittliche Geschwindigkeiten und Stop-and-go-Muster im Stadtverkehr.

2. **Berechnung der Fahrwiderstände:**
   - **Rollwiderstandskraft ($F_{\text{roll}}$)**:
     $$
     F_{\text{roll}} = \mu \cdot m \cdot g
     $$
     - **$\mu$**: Rollwiderstandsbeiwert (typisch 0,015 für Pkw).
     - **$m$**: Fahrzeugmasse.
     - **$g$**: Erdbeschleunigung ($9{,}81~\text{m/s}^2$).

   - **Luftwiderstandskraft ($F_{\text{cw}}$)** (bei niedrigen Geschwindigkeiten weniger relevant):
     $$
     F_{\text{cw}} = \frac{1}{2} \cdot \rho \cdot c_{\text{w}} \cdot A \cdot v^2
     $$
     - **$\rho$**: Luftdichte.
     - **$c_{\text{w}}$**: Luftwiderstandsbeiwert.
     - **$A$**: Stirnfläche.
     - **$v$**: Geschwindigkeit.

3. **Betrachtung der Energieflüsse:**
   - Energiebedarf für Fahrwiderstände.
   - Energiebedarf für Beschleunigungsvorgänge.
   - Verluste durch Bremsen und Leerlauf.

4. **Berechnung des effektiven Motorwirkungsgrads:**
   - Vergleich der zugeführten Kraftstoffenergie mit der tatsächlich genutzten mechanischen Energie.

## Detaillierte Betrachtung der Effizienz im Stadtverkehr

### Berechnung der Energiebedarfe

#### Beispielannahmen:

- **Fahrzeugmasse ($m$)**: 1.500 kg.
- **Durchschnittliche Geschwindigkeit ($v_{\text{durch}}$)**: 20 km/h.
- **Anzahl der Stopps pro Kilometer**: 5.
- **Beschleunigung bis zu einer Geschwindigkeit von**: 50 km/h.
- **Effektiver Motorwirkungsgrad ($\eta_{\text{e}}$)**: Wird ermittelt.

#### 1. Energie für den Rollwiderstand pro km

$$
W_{\text{roll}} = F_{\text{roll}} \cdot s = \mu \cdot m \cdot g \cdot s
$$

- **Berechnung:**
  $$
  W_{\text{roll}} = 0{,}015 \cdot 1\,500\,\text{kg} \cdot 9{,}81\,\text{m/s}^2 \cdot 1\,000\,\text{m} = 220\,725\,\text{J} \approx 220{,}7\,\text{kJ}
  $$

#### 2. Energie für Beschleunigungsvorgänge pro km

- **Kinetische Energie pro Beschleunigung:**
  $$
  E_{\text{kin}} = \frac{1}{2} \cdot m \cdot v_{\text{max}}^2
  $$
  - **$v_{\text{max}}$**: Endgeschwindigkeit in m/s ($50\,\text{km/h} = 13{,}89\,\text{m/s}$).

- **Berechnung:**
  $$
  E_{\text{kin}} = 0{,}5 \cdot 1\,500\,\text{kg} \cdot (13{,}89\,\text{m/s})^2 = 144\,942\,\text{J} \approx 144{,}9\,\text{kJ}
  $$

- **Gesamte kinetische Energie pro km (bei 5 Beschleunigungen):**
  $$
  W_{\text{kin,ges}} = 5 \cdot 144{,}9\,\text{kJ} = 724{,}5\,\text{kJ}
  $$

#### 3. Gesamter Energiebedarf pro km

$$
W_{\text{ges}} = W_{\text{roll}} + W_{\text{kin,ges}} = 220{,}7\,\text{kJ} + 724{,}5\,\text{kJ} = 945{,}2\,\text{kJ}
$$

### Berechnung des Kraftstoffverbrauchs

#### 1. Zugeführte Kraftstoffenergie pro km

$$
E_{\text{Kraftstoff}} = \frac{W_{\text{ges}}}{\eta_{\text{e}}}
$$

Da $\eta_{\text{e}}$ noch unbekannt ist, können wir es umstellen, wenn wir den realen Kraftstoffverbrauch kennen.

#### 2. Annahme eines realen Verbrauchs

- **Annahme:** Verbrauch von 10 l/100 km im Stadtverkehr.
- **Kraftstoffmenge pro km:**
  $$
  V_{\text{B,km}} = \frac{10\,\text{l}}{100\,\text{km}} = 0{,}1\,\text{l/km}
  $$

- **Kraftstoffmasse pro km:**
  $$
  m_{\text{B,km}} = V_{\text{B,km}} \cdot \rho_{\text{B}} = 0{,}1\,\text{l/km} \cdot 0{,}76\,\text{kg/l} = 0{,}076\,\text{kg/km}
  $$

- **Zugeführte Kraftstoffenergie pro km:**
  $$
  E_{\text{Kraftstoff}} = m_{\text{B,km}} \cdot H_{\text{U}} = 0{,}076\,\text{kg/km} \cdot 42\,000\,\text{kJ/kg} = 3\,192\,\text{kJ/km}
  $$

#### 3. Berechnung des effektiven Motorwirkungsgrads

$$
\eta_{\text{e}} = \frac{W_{\text{ges}}}{E_{\text{Kraftstoff}}} = \frac{945{,}2\,\text{kJ}}{3\,192\,\text{kJ}} \approx 0{,}296 \text{ oder } 29{,}6\,\%
$$

Dieser Wirkungsgrad erscheint hoch für den Stadtverkehr. Die Diskrepanz resultiert aus den vereinfachten Annahmen und der Tatsache, dass nicht alle Energieverluste berücksichtigt wurden, insbesondere:

- **Leerlaufverluste wurden nicht einbezogen.**
- **Zusatzverbraucher wurden nicht berücksichtigt.**
- **Verluste durch Bremsen (Energie geht verloren) wurden nicht korrekt abgebildet.**

#### 4. Realistischere Schätzung des Wirkungsgrads

Unter Berücksichtigung der genannten Verluste ist ein effektiver Wirkungsgrad von 10–15 % realistischer für Ottomotoren im Stadtverkehr.

### Schlussfolgerungen aus der Berechnung

- **Niedrige Effizienz im Stadtverkehr:**
  - **Hauptgründe:**
    - **Teillastbetrieb des Motors.**
    - **Verluste durch häufiges Beschleunigen und Bremsen.**
    - **Leerlaufverluste.**
- **Ein großer Teil der zugeführten Energie geht verloren**, ohne zur Vorwärtsbewegung beizutragen.

## Maßnahmen zur Steigerung der Effizienz im Stadtverkehr

### 1. Start-Stopp-Systeme

- **Automatisches Abschalten des Motors im Stillstand.**
- **Reduzierung von Leerlaufverlusten.**
- **Senkung des Kraftstoffverbrauchs um bis zu 10 % im Stadtverkehr.**

### 2. Hybridisierung

- **Mild-Hybride:**
  - Elektrischer Startergenerator unterstützt den Motor beim Anfahren.
  - Rekuperation von Bremsenergie.

- **Voll-Hybride:**
  - Elektrischer Antrieb bei niedrigen Geschwindigkeiten.
  - Verbrennungsmotor schaltet sich bei Bedarf zu.

- **Plug-in-Hybride:**
  - Größere Batteriekapazität.
  - Möglichkeit, kurze Strecken rein elektrisch zu fahren.

### 3. Rekuperation

- **Energierückgewinnung beim Bremsen.**
- **Speicherung der zurückgewonnenen Energie in einer Batterie oder einem Kondensator.**
- **Nutzung der Energie für Beschleunigungsvorgänge.**

### 4. Optimierung der Motorsteuerung

- **Variable Ventilsteuerung:**
  - Anpassung der Ventilöffnungszeiten an den Lastzustand.
- **Downsizing:**
  - Reduzierung des Hubraums bei gleichzeitiger Aufladung (Turbo, Kompressor).
- **Zylinderabschaltung:**
  - Abschaltung einzelner Zylinder bei geringer Last.

### 5. Alternative Antriebskonzepte

- **Elektrofahrzeuge:**
  - Höhere Effizienz des elektrischen Antriebs.
  - Keine lokalen Emissionen.
- **Brennstoffzellenfahrzeuge:**
  - Nutzung von Wasserstoff als Energieträger.
  - Abgabe von Wasserdampf als Emission.

### 6. Leichtbau und Aerodynamik

- **Reduzierung der Fahrzeugmasse:**
  - Verringerung des Energiebedarfs beim Beschleunigen.
- **Verbesserte Aerodynamik:**
  - Im Stadtverkehr weniger relevant, aber dennoch förderlich.

## Bedeutung für die Fahrzeugentwicklung

- **Fokus auf Effizienz im Teillastbereich:**
  - Entwicklung von Motoren, die auch bei geringer Last effizient arbeiten.
- **Integration von Energiespeichersystemen:**
  - Batterien oder Superkondensatoren für die Speicherung von Bremsenergie.
- **Anpassung an urbanen Verkehr:**
  - Fahrzeuge, die speziell für den Stadtverkehr optimiert sind (z. B. kompakte Elektrofahrzeuge).

## Zusammenfassung

- **Pkw-Motoren sind im Stadtverkehr weniger effizient**, da sie häufig im ineffizienten Teillastbereich betrieben werden und Energie durch häufiges Anfahren, Bremsen und Leerlauf verlieren.
- **Der effektive Motorwirkungsgrad liegt typischerweise bei 10–15 %** für Ottomotoren und 15–20 % für Dieselmotoren im Stadtverkehr.
- **Maßnahmen zur Effizienzsteigerung** umfassen Start-Stopp-Systeme, Hybridisierung, Rekuperation, Motoroptimierung und alternative Antriebe.
- **Technologische Innovationen sind notwendig**, um die Effizienz im Stadtverkehr zu erhöhen und den Kraftstoffverbrauch sowie die Emissionen zu reduzieren.

## Antwort auf die Frage

**Pkw-Motoren sind im Stadtverkehr aufgrund der spezifischen Fahrbedingungen weniger effizient.** Der effektive Motorwirkungsgrad liegt für Ottomotoren typischerweise bei **10–15 %** und für Dieselmotoren bei **15–20 %**. Hauptursachen für die geringe Effizienz sind:

- **Teillastbetrieb des Motors**, bei dem die Verbrennung weniger effizient ist.
- **Häufiges Anhalten und Anfahren**, was zu erhöhtem Energieverbrauch führt.
- **Leerlaufverluste**, da der Motor im Stillstand weiterläuft und Kraftstoff verbraucht, ohne Arbeit zu verrichten.
- **Verluste durch Bremsen**, bei denen kinetische Energie nicht genutzt, sondern als Wärme abgegeben wird.

**Um die Effizienz zu verbessern**, werden Technologien wie **Start-Stopp-Systeme**, **Hybridantriebe** und **Rekuperation** eingesetzt. Diese helfen, Energieverluste zu minimieren und den Kraftstoffverbrauch zu senken, was sowohl wirtschaftliche als auch ökologische Vorteile bietet.

---

**Zusätzliche Hinweise:**

- **Fahrer können zur Effizienz beitragen**, indem sie vorausschauend fahren, starke Beschleunigungen und unnötiges Anhalten vermeiden.
- **Politische Maßnahmen** wie Umweltzonen und Förderungen für effiziente Fahrzeuge können die Entwicklung und Verbreitung effizienterer Technologien unterstützen.
- **Zukünftige Entwicklungen** in der Elektromobilität und bei alternativen Kraftstoffen werden die Effizienz im Stadtverkehr weiter verbessern.

