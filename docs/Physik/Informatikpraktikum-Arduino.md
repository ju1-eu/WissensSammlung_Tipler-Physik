---
title: "Informatikpraktikum 1"
author: "Jan Unger"
date: "2024-10-19"
---

# Informatikpraktikum 1

Letzte Aktualisierung: 2024-10-19

Informatikpraktikum 1 <https://wiki.hshl.de/wiki/index.php/Informatikpraktikum_MTR#AlphaBot_SoSe24>

## Inhaltsverzeichnis

- [Informatikpraktikum 1](#informatikpraktikum-1)
  - [Inhaltsverzeichnis](#inhaltsverzeichnis)
  - [Prompt](#prompt)
- [Einführungsveranstaltung Informatikpraktikum 1](#einführungsveranstaltung-informatikpraktikum-1)
  - [Modulbeschreibung](#modulbeschreibung)
  - [Qualifikationsziele der Lehrveranstaltung](#qualifikationsziele-der-lehrveranstaltung)
  - [Inhalte](#inhalte)
  - [Lehrform des Informatikpraktikum 1](#lehrform-des-informatikpraktikum-1)
  - [Prüfungsform des Informatikpraktikum 1](#prüfungsform-des-informatikpraktikum-1)
    - [Bewertung](#bewertung)
  - [Workload des Informatikpraktikum 1](#workload-des-informatikpraktikum-1)
    - [Versionsverwaltung Git](#versionsverwaltung-git)
- [Einarbeitung in Git](#einarbeitung-in-git)
  - [Fragestellungen und Konzepte](#fragestellungen-und-konzepte)
  - [Lernziele](#lernziele)
  - [Vorbereitung](#vorbereitung)
  - [Versuchsdurchführung](#versuchsdurchführung)
    - [Aufgabe 1.1: Lernzielkontrolle](#aufgabe-11-lernzielkontrolle)
    - [Aufgabe 1.2: Arduino Uno Spezifikationen](#aufgabe-12-arduino-uno-spezifikationen)
    - [Aufgabe 1.3: Erstes Arduino-Programm](#aufgabe-13-erstes-arduino-programm)
    - [Aufgabe 1.4: LED-Blinken](#aufgabe-14-led-blinken)
    - [Aufgabe 1.5: Nachhaltige Dokumentation](#aufgabe-15-nachhaltige-dokumentation)
  - [Zusatzaufgabe: Python-Integration](#zusatzaufgabe-python-integration)
  - [Lernzielkontrolle](#lernzielkontrolle)
- [Arduino UNO R3 und Steckplatine](#arduino-uno-r3-und-steckplatine)
  - [1. Technische Daten des Arduino UNO R3](#1-technische-daten-des-arduino-uno-r3)
  - [2. Erläuterung der Fachbegriffe](#2-erläuterung-der-fachbegriffe)
  - [3. Aufbau einer Steckplatine](#3-aufbau-einer-steckplatine)
- [Einstieg in die Welt des Arduino](#einstieg-in-die-welt-des-arduino)
  - [Inhalt](#inhalt)
  - [Lernziele](#lernziele-1)
  - [Lernzielkontrolle](#lernzielkontrolle-1)
  - [Versuchsvorbereitung](#versuchsvorbereitung)
  - [Versuchsdurchführung](#versuchsdurchführung-1)
    - [Aufgabe 2.1: Lernzielkontrolle](#aufgabe-21-lernzielkontrolle)
    - [Aufgabe 2.2: Wechselblinker](#aufgabe-22-wechselblinker)
    - [Aufgabe 2.3: Pulsierende LED](#aufgabe-23-pulsierende-led)
    - [Aufgabe 2.4: Licht und Tonsignal](#aufgabe-24-licht-und-tonsignal)
    - [Aufgabe 2.5: Nachhaltige Dokumentation](#aufgabe-25-nachhaltige-dokumentation)
- [Arduino: Taster auswerten und LEDs ansteuern](#arduino-taster-auswerten-und-leds-ansteuern)
  - [Inhalt](#inhalt-1)
  - [Lernziele](#lernziele-2)
  - [Lernzielkontrolle](#lernzielkontrolle-2)
  - [Versuchsvorbereitung](#versuchsvorbereitung-1)
  - [Versuchsdurchführung](#versuchsdurchführung-2)
    - [Aufgabe 3.1: Lernzielkontrolle](#aufgabe-31-lernzielkontrolle)
    - [Aufgabe 3.2: Eine LED per Tastendruck aktivieren](#aufgabe-32-eine-led-per-tastendruck-aktivieren)
    - [Aufgabe 3.3: Auf Knopfdruck dimmen](#aufgabe-33-auf-knopfdruck-dimmen)
    - [Aufgabe 3.4: Ansteuerung einer farbigen LED](#aufgabe-34-ansteuerung-einer-farbigen-led)
    - [Aufgabe 3.5: Nachhaltige Dokumentation](#aufgabe-35-nachhaltige-dokumentation)
- [Arduino: Sensoren einlesen](#arduino-sensoren-einlesen)
  - [Inhalt](#inhalt-2)
  - [Lernziele](#lernziele-3)
  - [Lernzielkontrolle](#lernzielkontrolle-3)
  - [Versuchsvorbereitung](#versuchsvorbereitung-2)
  - [Versuchsdurchführung](#versuchsdurchführung-3)
    - [Aufgabe 4.1: Lernzielkontrolle](#aufgabe-41-lernzielkontrolle)
    - [Aufgabe 4.2: Der Bewegungsmelder HC-SR501](#aufgabe-42-der-bewegungsmelder-hc-sr501)
    - [Aufgabe 4.3: Fotowiderstand (LDR) am Arduino auslesen](#aufgabe-43-fotowiderstand-ldr-am-arduino-auslesen)
    - [Aufgabe 4.4: Drehregler - Drehpotentiometer](#aufgabe-44-drehregler---drehpotentiometer)
    - [Aufgabe 4.5: Nachhaltige Dokumentation](#aufgabe-45-nachhaltige-dokumentation)
- [Arduino: Infrarotsensor einlesen](#arduino-infrarotsensor-einlesen)
  - [Inhalt](#inhalt-3)
  - [Lernziele](#lernziele-4)
  - [Lernzielkontrolle](#lernzielkontrolle-4)
  - [Versuchsvorbereitung](#versuchsvorbereitung-3)
  - [Versuchsdurchführung](#versuchsdurchführung-4)
    - [Aufgabe 5.1: Lernzielkontrolle](#aufgabe-51-lernzielkontrolle)
    - [Aufgabe 5.2: Der Abstandssensor Sharp GP2Y0A21YK0F](#aufgabe-52-der-abstandssensor-sharp-gp2y0a21yk0f)
    - [Aufgabe 5.3: Sensorkennlinie](#aufgabe-53-sensorkennlinie)
    - [Aufgabe 5.4: Charakterisierung des Sharp Abstandssensors](#aufgabe-54-charakterisierung-des-sharp-abstandssensors)
    - [Aufgabe 5.5: Nachhaltige Dokumentation](#aufgabe-55-nachhaltige-dokumentation)
- [Arduino: Infrarotsensor entstören](#arduino-infrarotsensor-entstören)
  - [Inhalt](#inhalt-4)
  - [Lernziele](#lernziele-5)
  - [Lernzielkontrolle](#lernzielkontrolle-5)
  - [Vorbereitung](#vorbereitung-1)
  - [Versuchsdurchführung](#versuchsdurchführung-5)
    - [Aufgabe 6.1: Lernzielkontrolle](#aufgabe-61-lernzielkontrolle)
    - [Aufgabe 6.2: Messwertanalyse](#aufgabe-62-messwertanalyse)
    - [Aufgabe 6.3: IR Sensorcharakterisierung](#aufgabe-63-ir-sensorcharakterisierung)
    - [Aufgabe 6.4: Median-Filter](#aufgabe-64-median-filter)
    - [Aufgabe 6.5: Ergebnisbewertung und nachhaltige Dokumentation](#aufgabe-65-ergebnisbewertung-und-nachhaltige-dokumentation)
- [Arduino: IR-Theremin](#arduino-ir-theremin)
  - [Fragestellungen und Konzepte](#fragestellungen-und-konzepte-1)
  - [Vorausgesetzte Kenntnisse](#vorausgesetzte-kenntnisse)
  - [Lernziele](#lernziele-6)
  - [Lernzielkontrolle](#lernzielkontrolle-6)
  - [Vorbereitung](#vorbereitung-2)
  - [Versuchsdurchführung](#versuchsdurchführung-6)
    - [Aufgabe 8.1: Lernzielkontrolle](#aufgabe-81-lernzielkontrolle)
    - [Aufgabe 8.2: Debugging](#aufgabe-82-debugging)
    - [Aufgabe 8.3: Töne erzeugen](#aufgabe-83-töne-erzeugen)
    - [Aufgabe 8.4: IR-Theremin](#aufgabe-84-ir-theremin)
    - [Aufgabe 8.5: Nachhaltige Dokumentation](#aufgabe-85-nachhaltige-dokumentation)
- [Arduino: Aktoren](#arduino-aktoren)
  - [Fragestellungen und Konzepte](#fragestellungen-und-konzepte-2)
  - [Vorausgesetzte Kenntnisse](#vorausgesetzte-kenntnisse-1)
  - [Lernziele](#lernziele-7)
  - [Lernzielkontrolle](#lernzielkontrolle-7)
  - [Vorbereitung](#vorbereitung-3)
  - [Versuchsdurchführung](#versuchsdurchführung-7)
    - [Aufgabe 9.1: Lernzielkontrolle](#aufgabe-91-lernzielkontrolle)
    - [Aufgabe 9.2: Servo ansteuern](#aufgabe-92-servo-ansteuern)
    - [Aufgabe 9.3: Schrittmotor 28BYJ-48 ansteuern](#aufgabe-93-schrittmotor-28byj-48-ansteuern)
    - [Aufgabe 9.4: Motorbewegung unterbrechen](#aufgabe-94-motorbewegung-unterbrechen)
    - [Aufgabe 9.5: Nachhaltige Dokumentation](#aufgabe-95-nachhaltige-dokumentation)
- [Arduino: LCD Display mit I2C Schnittstelle](#arduino-lcd-display-mit-i2c-schnittstelle)
  - [Fragestellungen und Konzepte](#fragestellungen-und-konzepte-3)
  - [Vorausgesetzte Kenntnisse](#vorausgesetzte-kenntnisse-2)
  - [Lernziele](#lernziele-8)
  - [Lernzielkontrolle](#lernzielkontrolle-8)
  - [Vorbereitung](#vorbereitung-4)
  - [Versuchsdurchführung](#versuchsdurchführung-8)
    - [Aufgabe 10.1: Lernzielkontrolle](#aufgabe-101-lernzielkontrolle)
    - [Aufgabe 10.2: LCD-Display-Ansteuerung](#aufgabe-102-lcd-display-ansteuerung)
    - [Aufgabe 10.3: Sensordaten auf LCD ausgeben](#aufgabe-103-sensordaten-auf-lcd-ausgeben)
    - [Aufgabe 10.4: Anzeige via Taster umschalten](#aufgabe-104-anzeige-via-taster-umschalten)
    - [Aufgabe 10.5: Nachhaltige Dokumentation](#aufgabe-105-nachhaltige-dokumentation)
- [Arduino: Ultraschall Entfernungsmessung](#arduino-ultraschall-entfernungsmessung)
  - [Lernziele](#lernziele-9)
  - [Lernzielkontrolle](#lernzielkontrolle-9)
  - [Vorbereitung](#vorbereitung-5)
  - [Versuchsdurchführung](#versuchsdurchführung-9)
    - [Aufgabe 11.1: Lernzielkontrolle](#aufgabe-111-lernzielkontrolle)
    - [Aufgabe 11.2: Ultraschall-Entfernungsmessung](#aufgabe-112-ultraschall-entfernungsmessung)
    - [Aufgabe 11.3: Sensordaten auf LCD ausgeben](#aufgabe-113-sensordaten-auf-lcd-ausgeben)
    - [Aufgabe 11.4: Charakterisierung der Ultraschall-Messwerte](#aufgabe-114-charakterisierung-der-ultraschall-messwerte)
    - [Aufgabe 11.5: Nachhaltige Dokumentation](#aufgabe-115-nachhaltige-dokumentation)
  - [Hinweis zur Python-Nutzung](#hinweis-zur-python-nutzung)
    - [Aufgabe 11.6: Python-basierte Datenanalyse](#aufgabe-116-python-basierte-datenanalyse)
- [Arduino: Ultraschallsensor entstören](#arduino-ultraschallsensor-entstören)
  - [Inhalt](#inhalt-5)
  - [Lernziele](#lernziele-10)
  - [Lernzielkontrolle](#lernzielkontrolle-10)
  - [Vorbereitung](#vorbereitung-6)
  - [Versuchsdurchführung](#versuchsdurchführung-10)
    - [Aufgabe 12.1: Charakterisierung des Ultraschallsensors](#aufgabe-121-charakterisierung-des-ultraschallsensors)
    - [Aufgabe 12.2: Statische Messunsicherheit](#aufgabe-122-statische-messunsicherheit)
    - [Aufgabe 12.3: Gleitendes Mittelwertfilter](#aufgabe-123-gleitendes-mittelwertfilter)
    - [Aufgabe 12.4: Rekursives Tiefpassfilter](#aufgabe-124-rekursives-tiefpassfilter)
    - [Aufgabe 12.5: Dynamische Messunsicherheit](#aufgabe-125-dynamische-messunsicherheit)
  - [Abschließende Überprüfung](#abschließende-überprüfung)
- [Arduino: Temperaturmessung mit NTC und PTC](#arduino-temperaturmessung-mit-ntc-und-ptc)
  - [Inhalt](#inhalt-6)
  - [Lernziele](#lernziele-11)
  - [Lernzielkontrolle](#lernzielkontrolle-11)
  - [Vorbereitung](#vorbereitung-7)
  - [Versuchsdurchführung](#versuchsdurchführung-11)
    - [Aufgabe 13.1: Lernzielkontrolle](#aufgabe-131-lernzielkontrolle)
    - [Aufgabe 13.2: Temperaturmessung mit einem NTC](#aufgabe-132-temperaturmessung-mit-einem-ntc)
    - [Aufgabe 13.3: Temperaturmessung mit einem PTC](#aufgabe-133-temperaturmessung-mit-einem-ptc)
    - [Aufgabe 13.4: Datensicherung im EEPROM](#aufgabe-134-datensicherung-im-eeprom)
    - [Aufgabe 13.5: Nachhaltige Dokumentation](#aufgabe-135-nachhaltige-dokumentation)
- [Software Versionsverwaltung mit Git](#software-versionsverwaltung-mit-git)
  - [Einleitung](#einleitung)
  - [Warum sollten Sie Git nutzen?](#warum-sollten-sie-git-nutzen)
  - [Git Schnellstart](#git-schnellstart)
  - [Grundregeln im Umgang mit Git](#grundregeln-im-umgang-mit-git)
  - [Umgang mit binären Dateien](#umgang-mit-binären-dateien)
  - [Python-Integration](#python-integration)
- [Header-Beispiels für c](#header-beispiels-für-c)
- [Programmierrichtlinie für C](#programmierrichtlinie-für-c)
  - [Modul- und Funktionsköpfe](#modul--und-funktionsköpfe)
  - [Namenskonventionen](#namenskonventionen)
    - [Funktionen](#funktionen)
    - [Konstanten](#konstanten)
    - [Benutzerdefinierte Datentypen](#benutzerdefinierte-datentypen)
    - [Variablen](#variablen)
  - [Sonderregeln](#sonderregeln)
    - [Schleifeninkrement](#schleifeninkrement)
  - [Wortwahl](#wortwahl)
  - [Git-spezifische Ergänzungen](#git-spezifische-ergänzungen)
  - [Python-Integration](#python-integration-1)
- [Software-Plagiat](#software-plagiat)
  - [Definition](#definition)
  - [Konsequenzen](#konsequenzen)
  - [Vermeidung von Plagiaten](#vermeidung-von-plagiaten)
- [Arduino Programmier-Challenge I WS 23/24](#arduino-programmier-challenge-i-ws-2324)
  - [Inhalt](#inhalt-7)
  - [Vorbereitung](#vorbereitung-8)
  - [Einleitung](#einleitung-1)
  - [Anforderungen](#anforderungen)
  - [Durchführung](#durchführung)
    - [Aufgabe 7.1: Softwareplanung (PAP)](#aufgabe-71-softwareplanung-pap)
    - [Aufgabe 7.2: Implementierung](#aufgabe-72-implementierung)
    - [Aufgabe 7.3: Testing](#aufgabe-73-testing)
    - [Aufgabe 7.4: Dokumentation](#aufgabe-74-dokumentation)
  - [Hinweise](#hinweise)
  - [Bewertung](#bewertung-1)
  - [FAQ](#faq)
- [Arduino Programmier-Challenge II WS 23/24](#arduino-programmier-challenge-ii-ws-2324)
  - [Inhalt](#inhalt-8)
  - [Vorbereitung](#vorbereitung-9)
  - [Einleitung](#einleitung-2)
  - [Anforderungen](#anforderungen-1)
  - [Durchführung](#durchführung-1)
    - [Aufgabe 14.1: Softwareplanung (PAP)](#aufgabe-141-softwareplanung-pap)
    - [Aufgabe 14.2: Implementierung](#aufgabe-142-implementierung)
    - [Aufgabe 14.3: Testing](#aufgabe-143-testing)
    - [Aufgabe 14.4: Dokumentation](#aufgabe-144-dokumentation)
  - [Hinweise](#hinweise-1)
  - [Bewertung](#bewertung-2)
  - [FAQ](#faq-1)
  - [Zusätzliche Git- und Python-spezifische Empfehlungen:](#zusätzliche-git--und-python-spezifische-empfehlungen)

## Prompt

Ausgabe: Markdown mit LaTeX-Mathematik
beachte Sprachstil-Richtlinien und Git und Python anstatt SVN und MATLAB 


# Einführungsveranstaltung Informatikpraktikum 1

## Modulbeschreibung

Die Lehrveranstaltung Informatikpraktikum 1.

## Qualifikationsziele der Lehrveranstaltung

Die Studierenden können das an der Hochschule erworbene Wissen in der beruflichen Praxis bzw. in vergleichbaren Aufgabenstellungen anwenden und verfügen daher über eine verbesserte instrumentale Kompetenz. Sie können praxisorientierte Aufgaben analysieren und geeignete Problemlösungsmethoden im Kontext der Ingenieurdisziplinen anwenden.

Die Studierenden können:

- Aufgaben in Kleingruppen bearbeiten
- Strukturiert Software planen
- Mit einem SW-Versionierungstool (Git) umgehen
- Aufgaben der Informatik systematisch lösen
- Mit einem SW-Entwicklungstool umgehen
- Ergebnisse zu einem Abgabetermin hin erstellen (Projekt- und Zeitmanagement)
- Ergebnisse anschaulich und verständlich präsentieren sowie nachhaltig dokumentieren
- Ein mechatronisches System mit der Mikrokontrollerplattform Arduino in der Sprache C programmieren

## Inhalte

**Pflichtfach:** Informatikpraktikum 1: Die Studierenden können

- Strukturiert Software planen
- Mit einem SW-Versionierungstool (Git) umgehen
- Aufgaben der Informatik systematisch lösen
- Mit einem SW-Entwicklungstool umgehen
- Ergebnisse anschaulich und verständlich präsentieren
- Ergebnisse nachhaltig dokumentieren
- Mit dem Simulationstool Python umgehen

## Lehrform des Informatikpraktikum 1

2 SWS Praktikum (2 SWS)

## Prüfungsform des Informatikpraktikum 1

- Anwesenheitspflicht an allen Praktikumsterminen (Anwesenheitskontrolle)
- Vorbereitung des Praktikumstags und Überprüfung in Form von mündlichen Antestaten
- Durchführung im Praktikum
- Nachbereitung in Form von Versuchsberichten bzw. Protokollen (Hausarbeit)

### Bewertung

- Zwischen- und Abschlussprüfung
- Bewertung der Abgaben anhand der Bewertungskriterien für Software
- Plagiate (ähnliche Lösungen) werden mit der Note 6.0 bewertet
- Bei unentschuldigtem Fehlen ist die Teilnahme am Praktikum in diesem Semester nicht möglich
- Aufgaben sind im Team zu bearbeiten und Lösungen in Git zu sichern
- Regelmäßige Teilnahme erforderlich

**Hinweis**: Das Praktikum ist ein Submodul. Bei Bestehen bleibt der Status auch bei Nichtbestehen des Gesamtmoduls erhalten.

## Workload des Informatikpraktikum 1

| ECTS | Workload gesamt | Präsenz | Selbststudium |
| ---- | --------------- | ------- | ------------- |
| 2,5  | 75 h            | 30 h    | 45 h (3 h/w)  |


### Versionsverwaltung Git
- Gruppenordner
- Softwareablageort
- Versionsverwaltung
- Kollaboratives Arbeiten
- Datensicherung


# Einarbeitung in Git

Einführung in Versionskontrolle und Arduino-Programmierung

## Fragestellungen und Konzepte
- Funktion und praktischer Umgang mit Versionskontrolle
- Datentransfer und kollaboratives Arbeiten mit Git
- Grundlagen der Arduino-Programmierung

## Lernziele

Nach Abschluss dieser Lektion können die Studierenden:

1. Eine Verbindung zu GitHub herstellen
2. Auf Daten zugreifen und diese versioniert auf dem Server sichern
3. Kollaborativ im Team auf GitHub arbeiten
4. Dateikonflikte effektiv lösen
5. Sicher mit der Versionsverwaltung Git umgehen
6. Mit der Arduino IDE:
   - Programme anlegen
   - Globale Variablen definieren
   - Den Arduino programmieren
   - Text im seriellen Monitor ausgeben
   - Eine LED ansteuern

## Vorbereitung

1. Studium des Artikels: "Einführung in die Versionskontrolle mit Git"
2. Einrichtung eines lokalen Git-Repositories
3. Durchführung grundlegender Git-Operationen:
   - Checkout (git clone)
   - Commit
   - Push
   - Pull
   - Branching
   - Merging
4. Erstellung einer Textdatei und Versionierung mit Git
5. Simulation von Konflikten und deren Lösung
6. Erstellung von Tags und Wiederherstellung alter Versionsstände
7. Dokumentation der Git-Begriffe in `Git_Dokumentation.md`

## Versuchsdurchführung

### Aufgabe 1.1: Lernzielkontrolle
Präsentation der Ergebnisse der Vorbereitung

**Arbeitsergebnisse in Git**: 
- `Test.txt` mit Versionshistorie
- `Git_Dokumentation.md`

### Aufgabe 1.2: Arduino Uno Spezifikationen
Recherche und Dokumentation der technischen Daten des Arduino Uno R3

**Arbeitsergebnis in Git**: `ArduinoUnoSpec.md`

### Aufgabe 1.3: Erstes Arduino-Programm
Implementierung eines "Hallo Welt"-Programms mit der Arduino IDE

**Arbeitsergebnis in Git**: `HalloWelt.ino`

### Aufgabe 1.4: LED-Blinken
Erweiterung des Programms um eine blinkende LED

**Arbeitsergebnis in Git**: `blinkendeLED.ino`

### Aufgabe 1.5: Nachhaltige Dokumentation
Sicherung aller Ergebnisse in Git mit aussagekräftigen Commit-Messages

**Arbeitsergebnis in Git**: Git Log

## Zusatzaufgabe: Python-Integration

Entwickeln Sie ein Python-Skript, das die seriellen Ausgaben des Arduino ausliest und visualisiert.

**Arbeitsergebnis in Git**: `arduino_monitor.py`

## Lernzielkontrolle

1. Erklärung der Git-Konzepte:
   - Repository, Commit, Push, Pull, Branch, Merge
2. Demonstration der Konfliktlösung in Git
3. Erläuterung der Arduino Uno R3 Spezifikationen
4. Erklärung der Funktion einer Steckplatine (Breadboard)
5. Vorführung des "Hallo Welt"-Programms auf dem Arduino
6. Demonstration des LED-Blink-Programms
7. Präsentation des Python-Skripts zur Datenvisualisierung (falls implementiert)


# Arduino UNO R3 und Steckplatine

## 1. Technische Daten des Arduino UNO R3

1. **Mikrocontroller**: ATmega328P
2. **Spannungsversorgung**: 7-12V
3. **Betriebsspannung**: 5V
4. **Digitale I/O**: 14 Pins (davon 6 mit PWM)
5. **Analoge I/O**: 6 Pins
6. **Strom pro digitalem Pin**: 20 mA
7. **Flash Memory**: 32 KB (0,5 KB für Bootloader)
8. **SRAM**: 2 KB
9. **EEPROM**: 1 KB
10. **Taktfrequenz**: 16 MHz
11. **Programmierschnittstelle**: USB
12. **ICSP-Schnittstelle**: Vorhanden

## 2. Erläuterung der Fachbegriffe

1. **Mikrocontroller**: Integrierter Schaltkreis, der als Minicomputer fungiert und spezifische Aufgaben in einem eingebetteten System steuert.

2. **Spannungsversorgung**: Bereich der Eingangsspannung, die dem Board zugeführt werden kann, um es mit Energie zu versorgen.

3. **Betriebsspannung**: Spannung, mit der die internen Komponenten des Arduino arbeiten.

4. **Digitale I/O**: Pins für digitale Ein- und Ausgaben, die entweder HIGH (5V) oder LOW (0V) sein können. PWM steht für Pulsweitenmodulation, eine Technik zur Simulation analoger Ausgaben.

5. **Analoge I/O**: Pins, die analoge Spannungen zwischen 0V und 5V messen oder ausgeben können.

6. **Strom pro digitalem Pin**: Maximale Stromstärke, die ein einzelner digitaler Pin liefern oder aufnehmen kann.

7. **Flash Memory**: Nichtflüchtiger Speicher für das Programm (Sketch).

8. **SRAM**: Flüchtiger Arbeitsspeicher für Variablen während der Programmausführung.

9. **EEPROM**: Nichtflüchtiger Speicher für langfristige Datenspeicherung.

10. **Taktfrequenz**: Geschwindigkeit, mit der der Mikrocontroller Befehle ausführt, gemessen in Hertz (Hz).

11. **Programmierschnittstelle**: Methode zum Übertragen des Programms auf den Arduino.

12. **ICSP-Schnittstelle**: In-Circuit Serial Programming, ermöglicht das Programmieren des Mikrocontrollers direkt auf der Platine.

## 3. Aufbau einer Steckplatine

Eine Steckplatine, auch Breadboard genannt, ist ein wiederverwendbares Hilfsmittel zum schnellen Aufbau und Testen elektronischer Schaltungen ohne Löten. Ihr Aufbau lässt sich wie folgt beschreiben:

1. **Grundstruktur**: Rechteckige Platte mit Löchern in einem regelmäßigen Raster.

2. **Stromschienen**: Vertikale Reihen an den äußeren Rändern, meist rot (+) und blau (-) markiert, für die Stromversorgung.

3. **Komponenten-Bereich**: Horizontale Reihen in der Mitte für elektronische Bauteile.

4. **Verbindungen**:
   - Stromschienen: Vertikal verbunden
   - Komponenten-Bereich: Horizontal verbunden in Gruppen von meist 5 Löchern

5. **Mittlere Trennlinie**: Teilt die Steckplatine in zwei unabhängige Hälften.

6. **Material**: Meist aus Kunststoff gefertigt mit leitfähigen Metallclips unter den Löchern.

7. **Größe**: Verschiedene Standardgrößen verfügbar, z.B. Mini-Breadboards oder größere Versionen mit mehreren hundert Kontakten.


# Einstieg in die Welt des Arduino

Einführung in die Arduino-Programmierung

## Inhalt
- Einstieg in die Arduino-Welt
- Programmcode (Datentypen, Grundstruktur)
- if-Verzweigung
- LED, aktiver und passiver Lautsprecher
- Arduino IDE, Serieller Monitor, Code Debugging
- Digitale und analoge Ein- und Ausgänge

## Lernziele

Nach Abschluss dieser Lektion können die Studierenden:

1. Mit dem Arduino und der Arduino IDE umgehen
2. Programme schreiben, kompilieren und auf den Arduino übertragen
3. Variablen aller Datentypen deklarieren
4. Elektrische LED-Schaltungen aufbauen und in Betrieb nehmen
5. Eine LED über Pulsweitenmodulation ansteuern
6. Eine if-Verzweigung programmieren

## Lernzielkontrolle

1. Auflistung der Arduino-Datentypen mit ihrer Länge
2. Anwendungsfälle für verschiedene Datentypen
3. Deklaration lokaler und globaler Variablen
4. Definition und Zweck eines Makros
5. Anwendung der Befehle `define`, `static`, `const`
6. Programmierung einer if-Verzweigung
7. Ansteuerung einer LED (inkl. Schaltskizze und Widerstandsfunktion)
8. Unterschied zwischen aktiven und passiven Lautsprechern
9. Verwendung des PAPDesigners und Erstellung von PAPs für Programme 2.2 bis 2.4

## Versuchsvorbereitung

1. Studium der bereitgestellten Tutorials
2. Beantwortung der Lernzielkontrollfragen
3. Erstellung von PAPs für die Software
4. Sicherung der Unterlagen in Git

**Arbeitsergebnisse in Git**: `Lernzielkontrolle_Termin_02.pdf`

## Versuchsdurchführung

### Aufgabe 2.1: Lernzielkontrolle
Präsentation der Lernzielkontrolle-Ergebnisse

**Arbeitsergebnisse in Git**: `Lernzielkontrolle_Termin_02.pdf`

### Aufgabe 2.2: Wechselblinker
Implementierung eines abwechselnden Blinkens zweier LEDs

**Arbeitsergebnisse in Git**: `Wechselblinker.ino`

### Aufgabe 2.3: Pulsierende LED
Implementierung einer pulsierenden LED mit Helligkeitsänderung

**Arbeitsergebnisse in Git**: `PulsierendeLED.ino`

### Aufgabe 2.4: Licht und Tonsignal
Implementierung eines kontinuierlichen Blink- und Piep-Signals mit LED und Piezo-Lautsprecher

**Arbeitsergebnisse in Git**: `LichtundTon.ino`

### Aufgabe 2.5: Nachhaltige Dokumentation
1. Sicherung aller Ergebnisse in Git mit aussagekräftigen Commit-Messages
2. Überprüfung:
   - Einhaltung der Git-Nutzungsregeln
   - Nachhaltige Dokumentation
   - Vorhandensein von Programm-Headern
   - Umfangreiche Quelltext-Kommentierung
   - Erstellung und Übereinstimmung der PAPs mit den Programmen

**Arbeitsergebnis in Git**: Git Log


# Arduino: Taster auswerten und LEDs ansteuern

Tastereinbindung, LED-Ansteuerung und Programmierrichtlinien

## Inhalt
- Programmierrichtlinien
- Tasterauslesen und -entprellung mit Arduino
- Zählerimplementierung
- switch..case-Verzweigung
- Ansteuerung einer RGB-LED

## Lernziele

Nach Abschluss dieser Lektion können die Studierenden:

1. Quelltext entsprechend der Programmierrichtlinien schreiben
2. Einen Taster über eine Interrupt-Leitung einlesen und entprellen
3. Mittels Taster und switch..case-Verzweigung eine LED in verschiedenen Helligkeiten ansteuern
4. Eine RGB-LED in verschiedenen Farben ansteuern

## Lernzielkontrolle

1. Erfolgreiche Implementierung des Tastereinlesens und der Entprellung
2. Erklärung der Funktion eines Pull-Up/Pull-Down-Widerstands
3. Bewertung der Quelltext-Dokumentation (Header und Kommentare)
4. Aufzählung der Möglichkeiten zur Zähler-In-/Dekrementierung
5. Überprüfung der Verwendung von switch...case in Aufgabe 3.3
6. Identifikation der verwendeten RGB-LED-Version (gemeinsame Anode oder Kathode)
7. Überprüfung der PAP-Erstellung für jedes Programm
8. Vermeidung von `magic numbers`
9. Einhaltung der Programmierrichtlinie

## Versuchsvorbereitung

1. Einbindung der HSHL-Bibliothek
2. Studium des Artikels "Interrupt Service Routine" und des Demos DemoInterrupt.ino
3. Studium der bereitgestellten Tutorials
4. Studium der Programmierrichtlinie
5. Erstellung von PAPs für die Software
6. Beantwortung der Lernzielkontrollfragen
7. Sicherung der Unterlagen in Git

**Arbeitsergebnisse in Git**: `Lernzielkontrolle_Termin_03.pdf`

## Versuchsdurchführung

### Aufgabe 3.1: Lernzielkontrolle
Präsentation der Lernzielkontrolle-Ergebnisse

**Arbeitsergebnisse in Git**: `Lernzielkontrolle_Termin_03.pdf`

### Aufgabe 3.2: Eine LED per Tastendruck aktivieren
1. Implementierung einer Interrupt-Service-Routine für den Taster
2. Auswertung des Tasterstatus im `void loop()`
3. Serielle Ausgabe des Tasterstatus
4. LED-Steuerung (5 Sekunden an nach Tastendruck)

**Arbeitsergebnisse in Git**: `TasterSchaltetLED.ino`

### Aufgabe 3.3: Auf Knopfdruck dimmen
Implementierung einer LED-Dimmfunktion mit drei Zuständen (100%, 50%, 0%)

**Arbeitsergebnisse in Git**: `dimmeLED.ino`

### Aufgabe 3.4: Ansteuerung einer farbigen LED
Implementierung verschiedener Farbmodi für eine RGB-LED, gesteuert durch Tastendruck

**Arbeitsergebnisse in Git**: `steureFarbigeLED.ino`

### Aufgabe 3.5: Nachhaltige Dokumentation
1. Sicherung aller Ergebnisse in Git mit aussagekräftigen Commit-Messages
2. Überprüfung:
   - Einhaltung der Git-Nutzungsregeln
   - Einhaltung der Programmierrichtlinien
   - Nachhaltige Dokumentation
   - Vorhandensein von Programm-Headern
   - Umfangreiche Quelltext-Kommentierung
   - Erstellung und Übereinstimmung der PAPs mit den Programmen

**Arbeitsergebnis in Git**: Git Log



# Arduino: Sensoren einlesen

Einbindung und Auswertung digitaler und analoger Sensoren

## Inhalt
- Einbindung von PIR-Bewegungssensor (HC-SR501)
- Einbindung von Fotowiderstand (LDR)
- Einbindung von Drehpotentiometer (Poti)
- Visualisierung von Messwerten im seriellen Plotter

## Lernziele

Nach Abschluss dieser Lektion können die Studierenden:

1. Die Funktionsweise der 3 Sensoren (PIR-Bewegungssensor, Fotowiderstand, Drehpotentiometer) erläutern
2. Die Sensoren korrekt elektrisch anschließen
3. Die Sensordaten im Seriellen Plotter anzeigen und auswerten

## Lernzielkontrolle

1. Technische Funktionsweise des PIR-Bewegungssensors, seine Strahlungsempfindlichkeit und Einstellmöglichkeiten
2. Technische Funktionsweise des Fotowiderstands und Zweck der zusätzlichen Widerstände
3. Technische Funktionsweise des Drehpotentiometers und seine Kalibrierungsmethode
4. Methode zur Ausgabe mehrerer Signale im Seriellen Plotter
5. Bewertung der Quelltext-Dokumentation
6. Überprüfung der PAP-Erstellung für jedes Programm
7. Vermeidung von `magic numbers`
8. Einhaltung der Programmierrichtlinien

## Versuchsvorbereitung

1. Studium des Tutorials "Using the Serial Plotter Tool" und Nutzung von DemoSerialPlotter.ino
2. Recherche zur Funktion der Sensoren (PIR, LDR, Drehpoti)
3. Aufbau der Schaltungen zur Sensorauswertung
4. Erstellung von PAPs für die Software
5. Beantwortung der Lernzielkontrollfragen
6. Sicherung der Unterlagen in Git

**Arbeitsergebnisse in Git**: `Lernzielkontrolle_Termin_04.pdf`

## Versuchsdurchführung

### Aufgabe 4.1: Lernzielkontrolle
Präsentation der Lernzielkontrolle-Ergebnisse

**Arbeitsergebnisse in Git**: `Lernzielkontrolle_Termin_04.pdf`

### Aufgabe 4.2: Der Bewegungsmelder HC-SR501
Implementierung eines Piezo-Lautsprechers, der bei Bewegungserkennung piept

**Arbeitsergebnisse in Git**: `BewegungsmelderMitPiezo.ino`

### Aufgabe 4.3: Fotowiderstand (LDR) am Arduino auslesen
Steuerung einer LED basierend auf der Helligkeit (LDR-Wert)

**Arbeitsergebnisse in Git**: `LDRSteuertLED.ino`

### Aufgabe 4.4: Drehregler - Drehpotentiometer
Implementierung einer blinkenden LED mit Drehregler-gesteuerter Blinkgeschwindigkeit

**Arbeitsergebnisse in Git**: `PotiSteuertLED.ino`

### Aufgabe 4.5: Nachhaltige Dokumentation
1. Sicherung aller Ergebnisse in Git mit aussagekräftigen Commit-Messages
2. Überprüfung:
   - Einhaltung der Git-Nutzungsregeln
   - Einhaltung der Programmierrichtlinien
   - Nachhaltige Dokumentation
   - Vorhandensein von Programm-Headern
   - Umfangreiche Quelltext-Kommentierung
   - Erstellung und Übereinstimmung der PAPs mit den Programmen

**Arbeitsergebnis in Git**: Git Log


# Arduino: Infrarotsensor einlesen


Arrays, Funktionen und Sharp Entfernungssensor

## Inhalt
- Deklaration und Verwendung von Arrays
- Kapselung von Teilaufgaben in Funktionen
- Funktion des Sharp Entfernungssensors GP2Y0A41SK0F
- Einlesen und Verarbeitung von Sensordaten mit Arduino
- Kennlinienkalibrierung

## Lernziele

Nach Abschluss dieser Lektion können die Studierenden:

1. Den IR-Sensor korrekt elektrisch anschließen
2. Messwerte mit dem Serial Plotter der Arduino IDE anzeigen
3. Arrays anlegen und auf Array-Elemente zugreifen
4. Funktional programmieren
5. Sensordaten in gemessene Entfernungen umrechnen
6. Messwerte charakterisieren

## Lernzielkontrolle

1. Identifikation des Primärsensors im Sharp GP2Y0A21YK0F
2. Technische Funktionsweise des Sensors GP2Y0A41SK0F
3. Messgröße und Ausgangsgröße U1 des Sensors GP2Y0A41SK0F
4. Digitalisierung der Ausgangsgröße U1 zu D1
5. Methoden zur Umrechnung von D1 in die Distanz d
6. Bewertung der Quelltext-Dokumentation
7. Überprüfung der PAP-Erstellung für jedes Programm
8. Vermeidung von `magic numbers`
9. Einhaltung der Programmierrichtlinien

## Versuchsvorbereitung

1. Studium der Tutorials und Demos
2. Nutzung des Serial Plotter Tools mit DemoSharpIR.ino
3. Recherche zur Sensorfunktion (Fachliteratur, Datenblatt, Wiki)
4. Aufbau der Sensorauswertungsschaltungen
5. Erstellung einer Spannung/Distanz-Tabelle
6. Vertrautmachung mit analogen Eingängen und Spannungsmessung
7. Erweiterung der Tabelle um Digitalwerte D1
8. Erstellung von PAPs für die Software
9. Beantwortung der Lernzielkontrollfragen
10. Sicherung der Unterlagen in Git

**Arbeitsergebnisse in Git**: `Lernzielkontrolle_Termin_05.pdf`

## Versuchsdurchführung

### Aufgabe 5.1: Lernzielkontrolle
Präsentation der Lernzielkontrolle-Ergebnisse

**Arbeitsergebnisse in Git**: `Lernzielkontrolle_Termin_05.pdf`

### Aufgabe 5.2: Der Abstandssensor Sharp GP2Y0A21YK0F
1. Implementierung der geplanten Software
2. Darstellung der Messwerte D1 im Seriellen Monitor und Plotter

**Arbeitsergebnisse in Git**: `leseSharpIR.ino`

### Aufgabe 5.3: Sensorkennlinie
1. Erweiterung von `leseSharpIR.ino` zur Umrechnung von D1 in Messdistanz d
2. Darstellung der Distanz d im Seriellen Monitor und Plotter
3. Verifizierung mit einem Gliedermaßstab
4. Analyse der Messwerte

**Arbeitsergebnisse in Git**: `leseSharpIR.ino`

### Aufgabe 5.4: Charakterisierung des Sharp Abstandssensors
Bestimmung folgender Werte:
1. Messbereich in cm
2. Auflösung (Zeit, Distanz)
3. Empfindlichkeit

**Arbeitsergebnisse in Git**: `Sensorcharakterisierung.pdf`

### Aufgabe 5.5: Nachhaltige Dokumentation
1. Sicherung aller Ergebnisse in Git mit aussagekräftigen Commit-Messages
2. Überprüfung:
   - Einhaltung der Git-Nutzungsregeln
   - Einhaltung der Programmierrichtlinien
   - Nachhaltige Dokumentation
   - Vorhandensein von Programm-Headern
   - Umfangreiche Quelltext-Kommentierung
   - Erstellung und Übereinstimmung der PAPs mit den Programmen

**Arbeitsergebnis in Git**: Git Log


# Arduino: Infrarotsensor entstören

Kennlinienuntersuchung, Filterung und Bibliotheksnutzung

## Inhalt
- Kennlinienuntersuchung und Filterung
- Installation und Nutzung einer Bibliothek
- Programmierung und Anwendung eines Median-Filters

## Lernziele

Nach Abschluss dieser Lektion können die Studierenden:

1. Systematische Sensorfehler erkennen und behandeln
2. Eine Bibliothek installieren und nutzen
3. Messwerte vergleichend anzeigen und bewerten
4. Messwerte charakterisieren
5. Ein Median-Filter erläutern und anwenden

## Lernzielkontrolle

1. Methode zur Bestimmung der Größe eines Arrays
2. Installation einer neuen Bibliothek in der Arduino IDE
3. Nutzung der Bibliothek ArduinoSort zum Ausgeben und Sortieren eines Arrays
4. Definition und Berechnung eines Median-Filters
5. Konzept und Verwendung von Zeigern in C
6. Bewertung der Quelltext-Dokumentation
7. Überprüfung der PAP-Erstellung für jedes Programm
8. Vermeidung von `magic numbers`
9. Einhaltung der Programmierrichtlinien

## Vorbereitung

1. Studium der bereitgestellten Tutorials und Demos
2. Implementierung eines Arrays und Bestimmung seiner Größe
3. Installation der Bibliothek ArduinoSort-master.zip
4. Vertrautmachung mit DemoSortiereArray
5. Ausgabe eines Arrays im seriellen Monitor und Verständnis von Zeigern in C
6. Recherche zu "call by value" und "call by reference"
7. Sortierung eines Arrays mit Zufallszahlen
8. Studium der Median-Filter-Videos und des DemoMedianFilter
9. Erstellung von PAPs für die Software
10. Beantwortung der Lernzielkontrollfragen
11. Sicherung der Unterlagen in Git

**Arbeitsergebnisse in Git**: `Lernzielkontrolle_Termin_06.pdf`

## Versuchsdurchführung

### Aufgabe 6.1: Lernzielkontrolle
Präsentation der Lernzielkontrolle-Ergebnisse

**Arbeitsergebnisse in Git**: `Lernzielkontrolle_Termin_06.pdf`

### Aufgabe 6.2: Messwertanalyse
1. Zeitmessung mit `millis()`
2. Serielle Ausgabe von Zeit und Messdaten
3. Analyse und Diskussion der Messdaten
4. Entwicklung von Fehlerbehebungsstrategien

**Arbeitsergebnisse in Git**: `zeigeIRMesswerte.ino`

### Aufgabe 6.3: IR Sensorcharakterisierung
1. Aufzeichnung der gemessenen Entfernung im Verhältnis zur Referenz
2. Bestimmung des Messbereichs
3. Analyse der Entfernungsschritte und Auflösung
4. Berechnung der Sensorempfindlichkeit

**Arbeitsergebnisse in Git**: `IR_Sensorcharakterisierung.pdf`

### Aufgabe 6.4: Median-Filter
1. Implementierung der Funktion `int MedianFilter(int Messwert_s16)`
2. Erstellung eines 5-Werte-Ringspeichers (FIFO)
3. Sortierung der Werte
4. Rückgabe des Medianwerts
5. Test der Funktion mit Zufallszahlen

**Arbeitsergebnisse in Git**: `testeMedianFilter.ino`

### Aufgabe 6.5: Ergebnisbewertung und nachhaltige Dokumentation
1. Visualisierung des ungefilterten und Median-gefilterten Signals im seriellen Plotter
2. Bewertung der Messfehlerentfernung
3. Sicherung aller Ergebnisse in Git mit aussagekräftigen Commit-Messages
4. Überprüfung:
   - Einhaltung der Git-Nutzungsregeln
   - Einhaltung der Programmierrichtlinien
   - Nachhaltige Dokumentation
   - Vorhandensein von Programm-Headern
   - Umfangreiche Quelltext-Kommentierung
   - Erstellung und Übereinstimmung der PAPs mit den Programmen

**Arbeitsergebnisse in Git**: Git Log, `IRMedianFilter.ino`, `Ergebnisbewertung.pdf`


# Arduino: IR-Theremin

Datenexport, Python-Visualisierung und Arduino-Musikprojekte

## Fragestellungen und Konzepte
- Anwendung des kalibrierten Sharp IR Abstandssensors als Musikinstrument
- Datenexport in Textdateien und Visualisierung mit Python
- Erzeugung von Melodien mit Arduino und passivem Lautsprecher
- Entwicklung eines IR-Theremins

## Vorausgesetzte Kenntnisse
- Messung der Entfernung mit einem IR-Sensor
- Ansteuerung des Piezo-Lautsprechers

## Lernziele

Nach Abschluss dieser Lektion können die Studierenden:

1. Daten in eine Textdatei exportieren und mit Python visualisieren
2. Eine Melodie mit dem Arduino abspielen
3. Ein IR-Theremin bauen und entfernungsabhängig Töne erzeugen

## Lernzielkontrolle

1. Serielle Datenausgabe mit 115200 Baud
2. Datenspeicherung mit Putty in eine Textdatei
3. Datenvisualisierung mit Python
4. Bewertung der Quelltext-Dokumentation
5. Überprüfung der PAP-Erstellung für jedes Programm
6. Vermeidung von `magic numbers`
7. Einhaltung der Programmierrichtlinien

## Vorbereitung

1. Installation und Vertrautmachung mit Putty
2. Entwicklung eines Arduino-Programms zur seriellen Ausgabe von Zeit und Distanz
3. Python-Skript zur Visualisierung der Distanz über der Zeit
4. Erstellung von PAPs für die Software
5. Beantwortung der Lernzielkontrollfragen
6. Sicherung der Unterlagen in Git

**Arbeitsergebnisse in Git**: `Lernzielkontrolle_Termin_07.pdf`

## Versuchsdurchführung

### Aufgabe 8.1: Lernzielkontrolle
Präsentation der Lernzielkontrolle-Ergebnisse

**Arbeitsergebnisse in Git**: `Lernzielkontrolle_Termin_08.pdf`

### Aufgabe 8.2: Debugging
Arduino-Aufgabe:
1. Zeitmessung mit `millis()`
2. Entfernungsmessung mit und ohne Median-Filter
3. Serielle Ausgabe der Daten
4. Datenspeicherung mit Putty in `Debug.txt`

Python-Aufgabe:
1. Dateneinlesen aus `Debug.txt`
2. Visualisierung der Entfernung mit und ohne Median-Filter
3. Ergänzung von Legende und Achsenbeschriftungen

**Arbeitsergebnisse in Git**: `schreibeDebugDatei.ino`, `Debug.txt`, `visualisiere_daten.py`

### Aufgabe 8.3: Töne erzeugen
Implementierung verschiedener Töne und einer Melodie mit passivem Lautsprecher

**Arbeitsergebnisse in Git**: `spieleMelodie.ino`

### Aufgabe 8.4: IR-Theremin
1. Implementierung eines Theremins mit IR-Sensor
2. Kalibrierung der Entfernung-Frequenz-Zuordnung
3. Melodieerzeugung

**Arbeitsergebnisse in Git**: `IR_Theremin.ino`

### Aufgabe 8.5: Nachhaltige Dokumentation
1. Sicherung aller Ergebnisse in Git mit aussagekräftigen Commit-Messages
2. Überprüfung:
   - Einhaltung der Git-Nutzungsregeln
   - Einhaltung der Programmierrichtlinien
   - Nachhaltige Dokumentation
   - Vorhandensein von Programm-Headern
   - Umfangreiche Quelltext-Kommentierung
   - Erstellung und Übereinstimmung der PAPs mit den Programmen

**Arbeitsergebnis in Git**: Git Log

Diese aktualisierte Struktur berücksichtigt die Verwendung von Python für die Datenanalyse und -visualisierung anstelle von MATLAB. Die grundlegenden Lernziele und Aufgaben bleiben bestehen, aber die spezifischen Implementierungen werden an Python angepasst.

Für die Python-Visualisierung könnten folgende Bibliotheken verwendet werden:
- `pandas` für das Einlesen und Verarbeiten der Daten
- `matplotlib` für die Erstellung der Plots

Ein Beispiel für den Python-Code zur Datenvisualisierung könnte wie folgt aussehen:

```python
import pandas as pd
import matplotlib.pyplot as plt

# Daten einlesen
data = pd.read_csv('Debug.txt', delimiter=';', names=['Zeit', 'Distanz', 'Median'])

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(data['Zeit'], data['Distanz'], 'r.-', label='Messwerte')
plt.plot(data['Zeit'], data['Median'], 'b-', label='Median-Filter')
plt.xlabel('Zeit (ms)')
plt.ylabel('Entfernung (cm)')
plt.title('Entfernungsmessung mit IR-Sensor')
plt.legend()
plt.grid(True)
plt.show()
```




# Arduino: Aktoren

Ansteuerung von Aktoren: Servomotor und Schrittmotor

## Fragestellungen und Konzepte
- Ansteuerung von Servomotoren und Schrittmotoren mit Arduino
- Einführung in die Funktionsweise und Anwendungsfelder beider Motortypen

## Vorausgesetzte Kenntnisse
- Nutzung der digitalen IO-Pins
- Interrupts

## Lernziele

Nach Abschluss dieser Lektion können die Studierenden:

1. Die Funktion eines Servomotors und Schrittmotors erläutern
2. Unterschiede und Anwendungsfelder der Motoren beschreiben
3. Beide Motoren gezielt ansteuern
4. Das Hauptprogramm mit einem Interrupt unterbrechen

## Lernzielkontrolle

1. Funktionsweise und Arbeitsbereich eines Servomotors
2. Pulsweitenmodulation (PWM) und Servoansteuerung
3. Vorsichtsmaßnahmen beim Umgang mit Servomotoren
4. Methode zur Ansteuerung eines Servomotors
5. Funktionsweise und Arbeitsbereich eines Schrittmotors
6. Vorsichtsmaßnahmen beim Umgang mit Schrittmotoren
7. Methode zur Ansteuerung eines Schrittmotors
8. Anzahl der Schritte des verwendeten Schrittmotors
9. Vergleich beider Motortypen anhand fachlicher Kriterien
10. Bewertung der Quelltext-Dokumentation
11. Überprüfung der PAP-Erstellung für jedes Programm
12. Vermeidung von `magic numbers`
13. Einhaltung der Programmierrichtlinien

## Vorbereitung

1. Studium der Materialien zum Servomotor TowerPro SG90
2. Studium der Materialien zum Schrittmotor 28BYJ-48
3. Recherche zu Arduino-Interrupts
4. Erstellung von PAPs für die Software
5. Beantwortung der Lernzielkontrollfragen
6. Sicherung der Unterlagen in Git

**Arbeitsergebnisse in Git**: `Lernzielkontrolle_Termin_08.pdf`

## Versuchsdurchführung

### Aufgabe 9.1: Lernzielkontrolle
Präsentation der Lernzielkontrolle-Ergebnisse

**Arbeitsergebnisse in Git**: `Lernzielkontrolle_Termin_09.pdf`

### Aufgabe 9.2: Servo ansteuern
Implementierung der Servoansteuerung mit drei Positionen und Wartezeiten

**Nützliche Befehle**: `#include`, `Servo`, `attach`, `write`

**Arbeitsergebnisse in Git**: `steureServo.ino`

### Aufgabe 9.3: Schrittmotor 28BYJ-48 ansteuern
Implementierung einer vollständigen Umdrehung vor- und rückwärts

**Nützliche Befehle**: `#include<Stepper.h>`, `Stepper`, `step()`, `setSpeed()`

**Arbeitsergebnisse in Git**: `steureSchrittmotor.ino`

### Aufgabe 9.4: Motorbewegung unterbrechen
1. Implementierung eines Sekundenzeigers mit dem Schrittmotor
2. Einlesen eines Tasters als "Notaus" über Interrupt
3. Implementierung einer Interrupt-Service-Routine zum sofortigen Motorstopp

**Nützliche Befehle**: `attachInterrupt()`

**Arbeitsergebnisse in Git**: `StepperUhrNotaus.ino`

### Aufgabe 9.5: Nachhaltige Dokumentation
1. Sicherung aller Ergebnisse in Git mit aussagekräftigen Commit-Messages
2. Überprüfung:
   - Einhaltung der Git-Nutzungsregeln
   - Einhaltung der Programmierrichtlinien
   - Nachhaltige Dokumentation
   - Vorhandensein von Programm-Headern
   - Umfangreiche Quelltext-Kommentierung
   - Erstellung und Übereinstimmung der PAPs mit den Programmen

**Arbeitsergebnis in Git**: Git Log




# Arduino: LCD Display mit I2C Schnittstelle

## Fragestellungen und Konzepte
- Ansteuerung eines LCD-Displays über I2C-Bus
- Einführung in I2C-Bus und LCD-Display-Ansteuerung

## Vorausgesetzte Kenntnisse
- Nutzung der digitalen IO-Pins

## Lernziele

Nach Abschluss dieser Lektion können die Studierenden:

1. Die Funktion eines I2C-Busses erläutern
2. Ein LCD-Display ansteuern
3. Daten auf dem LCD-Display anzeigen
4. Die Anzeige via Taster umschalten

## Lernzielkontrolle

1. Definition und Funktionsweise des I2C-Busses
2. Kommunikationsprinzip des I2C-Busses
3. Methode zur Ansteuerung eines LCD-Displays
4. Auslesen des Temperatursensors TMP36
5. Implementierung der Modusumschaltung im Display
6. Bewertung der Quelltext-Dokumentation (Header und Kommentare)
7. Überprüfung der PAP-Erstellung für jedes Programm
8. Vermeidung von `magic numbers`
9. Einhaltung der Programmierrichtlinien

## Vorbereitung

1. Recherche zur Funktion des I2C-Busses
2. Recherche zur Funktion des TMP36
3. Implementierung des Beispiels "Temperaturen mit einem TMP36 am Arduino messen"
4. Implementierung des Beispiels "Ein LCD Display per Arduino ansteuern"
5. Implementierung der Anzeigenumschaltung im Display
6. Erstellung von PAPs für die Software
7. Beantwortung der Lernzielkontrollfragen
8. Sicherung der Unterlagen in Git

**Arbeitsergebnisse in Git**: `Lernzielkontrolle_Termin_09.pdf`

## Versuchsdurchführung

### Aufgabe 10.1: Lernzielkontrolle
Präsentation der Lernzielkontrolle-Ergebnisse

**Arbeitsergebnisse in Git**: `Lernzielkontrolle_Termin_10.pdf`

### Aufgabe 10.2: LCD-Display-Ansteuerung
Ansteuerung eines LCD-Displays mit vorgegebenem Text

**Nützliche Befehle**: `#include`, `init`, `backlight`, `setCursor`, `print`

**Arbeitsergebnisse in Git**: `AusgabeTextAufLCD.ino`

### Aufgabe 10.3: Sensordaten auf LCD ausgeben
Auslesen und Anzeige der Temperatur vom TMP36-Sensor auf dem LCD

**Nützliche Befehle**: `analogRead()`, `map()`

**Arbeitsergebnisse in Git**: `messeTemperatur.ino`

### Aufgabe 10.4: Anzeige via Taster umschalten
1. Implementierung eines Taster-Interrupts
2. Umschaltung zwischen 4 Modi:
   - Modus 1: Text aus Aufgabe 10.2
   - Modus 2: Sensorwert aus Aufgabe 10.3
   - Modus 3: Text "Modus 3"
   - Modus 4: Text "Modus 4"
3. Zyklische Umschaltung (nach Modus 4 zurück zu Modus 1)

**Nützliche Befehle**: `switch .. case`

**Arbeitsergebnisse in Git**: `schalteAnzeige.ino`

### Aufgabe 10.5: Nachhaltige Dokumentation
1. Sicherung aller Ergebnisse in Git mit aussagekräftigen Commit-Messages
2. Überprüfung:
   - Einhaltung der Git-Nutzungsregeln
   - Einhaltung der Programmierrichtlinien
   - Nachhaltige Dokumentation
   - Vorhandensein von Programm-Headern
   - Umfangreiche Quelltext-Kommentierung
   - Erstellung und Übereinstimmung der PAPs mit den Programmen

**Arbeitsergebnis in Git**: Git Log


# Arduino: Ultraschall Entfernungsmessung

## Lernziele

Nach Abschluss dieser Lektion können die Studierenden:

1. Die Funktion eines Ultraschallsensors erläutern
2. Vor- und Nachteile der Entfernungsmessung mit Ultraschall erklären
3. Einen Ultraschallsensor ansteuern
4. Messdaten charakterisieren und auf einem LCD-Display anzeigen

## Lernzielkontrolle

1. Frequenzbereich des menschlichen Gehörs
2. Hörbarkeit von Ultraschall
3. Typische Frequenz von Ultraschall
4. Ultraschallgeschwindigkeit bei 20°C
5. Einflussfaktoren auf die Ultraschallgeschwindigkeit
6. Formel für Entfernungsmessung mit Ultraschall
7. Vor- und Nachteile von Ultraschallsensoren
8. Zehn Anwendungsgebiete für Ultraschallsensoren
9. Bewertung der Quelltext-Dokumentation (Header und Kommentare)
10. Überprüfung der PAP-Erstellung für jedes Programm
11. Vermeidung von `magic numbers`
12. Einhaltung der Programmierrichtlinien

## Vorbereitung

1. Recherche zur Funktionsweise des HC-SR04 Ultraschallsensors
2. Implementierung des Beispiels "Entfernungsmessung mit HC-SR04 und Arduino"
3. Umsetzung der LCD-Display-Ansteuerung via Arduino
4. Anzeige der Messwerte auf dem LCD-Display
5. Softwareplanung mittels PAP
6. Beantwortung der Lernzielkontrollfragen
7. Sicherung der Unterlagen in Git

**Arbeitsergebnisse** in Git: `Lernzielkontrolle_Termin_10.pdf`

## Versuchsdurchführung

### Aufgabe 11.1: Lernzielkontrolle
Präsentation der Lernzielkontrolle-Ergebnisse

**Arbeitsergebnisse** in Git: `Lernzielkontrolle_Termin_11.pdf`

### Aufgabe 11.2: Ultraschall-Entfernungsmessung
Implementierung der Entfernungsmessung mit HC-SR04 und Arduino

**Nützliche Befehle**: `pinMode`, `digitalWrite`, `delay`, `pulseIn`

**Arbeitsergebnisse** in Git: `messeUltraschallEntfernung.ino`

### Aufgabe 11.3: Sensordaten auf LCD ausgeben
Anzeige der Entfernungsmessung auf LCD als Messwert und Balkenanzeige

**Nützliche Befehle**: `#include`, `init`, `backlight`, `setCursor`, `print`

**Arbeitsergebnisse** in Git: `zeigeUltraschallEntfernung.ino`

### Aufgabe 11.4: Charakterisierung der Ultraschall-Messwerte
Analyse der Sensorfunktion anhand der Messwerte:
1. Messbereich
2. Werteauflösung
3. Maximale Abtastrate
4. Empfindlichster Bereich
5. Messunsicherheit (1 σ) für glatte Flächen

**Arbeitsergebnisse** in Git: `UltraschallSensorcharakterisierung.pdf`

### Aufgabe 11.5: Nachhaltige Dokumentation
Sicherung aller Ergebnisse in Git mit beschreibenden Commit-Messages

Überprüfung:
- Einhaltung der Git-Nutzungsregeln
- Einhaltung der Programmierrichtlinien
- Nachhaltige Dokumentation
- Vorhandensein von Programm-Headern
- Umfangreiche Quelltext-Kommentierung
- Erstellung und Übereinstimmung der PAPs mit den Programmen

**Arbeitsergebnis** in Git: `Git Log`

## Hinweis zur Python-Nutzung

Für die Datenvisualisierung und -analyse können die Studierenden Python-Skripte entwickeln, um die vom Arduino gesammelten Daten zu verarbeiten und grafisch darzustellen. Dies könnte eine zusätzliche Aufgabe sein:

### Aufgabe 11.6: Python-basierte Datenanalyse
Entwickeln Sie ein Python-Skript zur Visualisierung und statistischen Analyse der Ultraschall-Messdaten.

**Arbeitsergebnisse** in Git: `ultraschall_analyse.py`


# Arduino: Ultraschallsensor entstören

Statische und Dynamische Messung, Kennlinienuntersuchung und Filterung

## Inhalt
- Statische und dynamische Messung
- Kennlinienuntersuchung und Filterung
- Programmierung und Anwendung eines gleitenden Mittelwertfilters
- Programmierung und Anwendung eines gleitenden Tiefpassfilters

## Lernziele

Nach Abschluss dieser Lektion können die Studierenden:

1. Zufällige Sensorfehler erkennen und behandeln
2. Messwerte vergleichend anzeigen und bewerten
3. Messwerte charakterisieren
4. Ein gleitendes Mittelwertfilter erläutern und anwenden
5. Ein Tiefpassfilter erläutern und anwenden

## Lernzielkontrolle

1. Messbereich des verwendeten Ultraschallsensors
2. Auflösung (t, s) des Sensors
3. Empfindlichkeit des Sensors
4. Messunsicherheit bei Entfernungen: 10 cm, 20 cm, 50 cm, 1 m, 2 m, 3 m und 4 m
5. Definition und Berechnung eines gleitenden Mittelwertfilters
6. Definition und Berechnung eines rekursiven Tiefpassfilters
7. Bewertung der Quelltext-Dokumentation (Header und Kommentare)
8. Überprüfung der PAP-Erstellung für jedes Programm
9. Vermeidung von `magic numbers`
10. Einhaltung der Programmierrichtlinien

## Vorbereitung

1. Vorbereitung von Aufgabe 11.1 anhand der Tutorials und Demos
2. Implementierung und Test der Funktion `GleitendesMittelwertFilter()`
3. Implementierung und Test der Funktion `TiefpasstFilter()`
4. Erstellung von PAPs für alle Programme

**Arbeitsergebnisse in Git**: PAP, charakterisiereUltraschaschallsensor.ino, USMessung.txt, charakterisiereUltraschallSensor.py, Lernzielkontrolle_Termin_11.pdf, GleitendesMittelwertFilter(), TiefpasstFilter()

## Versuchsdurchführung

### Aufgabe 12.1: Charakterisierung des Ultraschallsensors
1. Implementierung der Funktion `float messeUltraschallAbstand()`
2. Aufzeichnung von Zeitstempel, Signallaufzeit und berechneter Entfernung in `Ultraschallmessung.txt`
3. Datenvisualisierung mit Python
4. Graphische Darstellung: Entfernung s über Laufzeit t
5. Bestimmung von Empfindlichkeit E, Auflösung von t und s
6. Dokumentation der Ergebnisse in `Lernzielkontrolle_Termin_12.pdf`

**Arbeitsergebnisse in Git**: charakterisiereUltraschaschallsensor.ino, USMessung.txt, charakterisiereUltraschallSensor.py, Lernzielkontrolle_Termin_11.pdf

### Aufgabe 12.2: Statische Messunsicherheit
1. Implementierung von `statische_messunsicherheit.ino`
2. Datenerfassung für verschiedene Entfernungen
3. Datenvisualisierung und -analyse mit Python
4. Berechnung und Darstellung von Mittelwert und Standardabweichung

**Arbeitsergebnisse in Git**: statische_messunsicherheit.ino, Ultraschallmessung.txt, zeigeUltraschallMessung.py

### Aufgabe 12.3: Gleitendes Mittelwertfilter
1. Implementierung der Funktion `GleitendesMittelwertFilter()`
2. Test mit statischen und dynamischen Zielen
3. Visualisierung im seriellen Plotter
4. Wahl und Diskussion des Parameters k

**Arbeitsergebnisse in Git**: testeGleitendesMittelwert.ino

### Aufgabe 12.4: Rekursives Tiefpassfilter
1. Implementierung der Funktion `TiefpassFilter()`
2. Test mit statischen und dynamischen Zielen
3. Visualisierung im seriellen Plotter
4. Wahl und Diskussion des Parameters α

**Arbeitsergebnisse in Git**: testeTiefpassFilter.ino

### Aufgabe 12.5: Dynamische Messunsicherheit
1. Vergleich von ungefiltertem und Tiefpass-gefiltertem Signal mit Python
2. Bewertung der Signalglättung
3. Sicherung aller Ergebnisse in Git mit aussagekräftigen Commit-Messages

**Arbeitsergebnis in Git**: USTiefpassFilter.ino, Ergebnisbewertung.pdf

## Abschließende Überprüfung
- Einhaltung der Git-Nutzungsregeln
- Einhaltung der Programmierrichtlinien
- Nachhaltige Dokumentation
- Vorhandensein von Programm-Headern
- Umfangreiche Quelltext-Kommentierung
- Erstellung und Übereinstimmung der PAPs mit den Programmen


# Arduino: Temperaturmessung mit NTC und PTC

Temperaturmessung und EEPROM-Datenspeicherung

## Inhalt
- Temperaturkennlinie von NTC und PTC
- Temperaturmessung mit NTC und PTC
- Datenspeicherung im EEPROM

## Lernziele

Nach Abschluss dieser Lektion können die Studierenden:

1. Mittels NTC und PTC Temperaturen messen
2. Die Funktion und die Kennlinien eines NTC und PTC beschreiben
3. Messwerte im EEPROM ablegen und auswerten

## Lernzielkontrolle

1. NTC: Funktionsweise und Prinzip
2. Schaltung zur Temperaturmessung mit NTC
3. Mathematischer Zusammenhang T = f(R_NTC)
4. Implementierung der NTC-Formel in C und Test mit Datenblatt-Werten
5. PTC: Funktionsweise und Prinzip
6. Schaltung zur Temperaturmessung mit PTC
7. Mathematischer Zusammenhang T = f(R_PTC)
8. Implementierung der PTC-Formel in C und Test mit Datenblatt-Werten
9. Anwendungsbereiche für NTC und PTC
10. EEPROM: Definition und Eigenschaften
11. EEPROM-Größe und Position auf dem Arduino Uno R3
12. EEPROM-Schreibzyklen
13. Geeignete Daten für EEPROM-Speicherung
14. Methoden der EEPROM.h-Klasse (crc, get, put, read, update, write)
15. Bewertung der Quelltext-Dokumentation
16. Überprüfung der PAP-Erstellung für jedes Programm
17. Vermeidung von `magic numbers`
18. Einhaltung der Programmierrichtlinien

## Vorbereitung

1. Studium der bereitgestellten Tutorials und Demos
2. Erstellung von PAPs für alle Programme
3. Beantwortung der Lernzielkontrollfragen
4. Nachhaltige Arbeit in Git

**Arbeitsergebnisse in Git**: Lernzielkontrolle_Termin_12.pdf

## Versuchsdurchführung

### Aufgabe 13.1: Lernzielkontrolle
Präsentation der Lernzielkontrolle-Ergebnisse

**Arbeitsergebnisse in Git**: Lernzielkontrolle_Termin_13.pdf

### Aufgabe 13.2: Temperaturmessung mit einem NTC
1. Aufbau der NTC-Grundschaltung
2. Einlesen der Spannung am Analogpin A0
3. Berechnung des Widerstands R(T) in Ω
4. Umformung der Formel R(T) nach T
5. Berechnung der Temperatur in °C
6. Visualisierung im seriellen Plotter

**Arbeitsergebnisse in Git**: messeNTCTemperatur.ino

### Aufgabe 13.3: Temperaturmessung mit einem PTC
1. Aufbau der PTC-Grundschaltung
2. Einlesen der Spannung am Analogpin A0
3. Berechnung des Widerstands R(T) in Ω
4. Umformung der Formel R(T) nach T
5. Berechnung der Temperatur in °C
6. Visualisierung im seriellen Plotter

**Arbeitsergebnisse in Git**: messePTCTemperatur.ino

### Aufgabe 13.4: Datensicherung im EEPROM
1. Betrieb des Arduino mit 9V Batterieblock
2. Implementierung eines entprellten Tasters
3. EEPROM-Speicherung bei Tastendruck:
   - Namen der Teammitglieder (string)
   - Anzahl der Teammitglieder (byte)
   - Baudrate (int)
   - Zeit mit millis() (long)
   - Gemessene Temperatur in °C (float)
4. Messung bei ca. 20°C und ca. 0°C
5. Kurzzeitige Trennung der Spannungsversorgung
6. Auslesen und Visualisierung der EEPROM-Daten im seriellen Monitor

**Arbeitsergebnisse in Git**: speichereDatenimEEPROM.ino, leseDatenausEEPROM.ino

### Aufgabe 13.5: Nachhaltige Dokumentation
1. Sicherung aller Ergebnisse in Git mit aussagekräftigen Commit-Messages
2. Überprüfung:
   - Einhaltung der Git-Nutzungsregeln
   - Einhaltung der Programmierrichtlinien
   - Nachhaltige Dokumentation
   - Vorhandensein von Programm-Headern
   - Umfangreiche Quelltext-Kommentierung
   - Erstellung und Übereinstimmung der PAPs mit den Programmen

**Arbeitsergebnis in Git**: Git Log

# Software Versionsverwaltung mit Git

## Einleitung

Als Software-Versionsverwaltung nutzen wir an der HSHL Git. Git ist ein freies, verteiltes Versionskontrollsystem, das die Verwaltung von Dateien und Verzeichnissen sowie deren Änderungen über die Zeit ermöglicht. Dies erlaubt Ihnen, alte Versionen Ihrer Daten wiederherzustellen oder die Historie der Änderungen nachzuverfolgen.

Git kann netzwerkübergreifend arbeiten, was die Zusammenarbeit von Personen an verschiedenen Computern ermöglicht. Die Fähigkeit, dass unterschiedliche Personen dieselben Daten bearbeiten und verwalten können, fördert die Kollaboration und beschleunigt den Fortschritt.

## Warum sollten Sie Git nutzen?

- Ihre Daten sind auf einem Server (z.B. GitHub) sicher und weltweit für Sie zugänglich.
- Teammitglieder können auf Arbeitsergebnisse zugreifen, auch wenn Sie verhindert sind.
- Commit-Nachrichten ermöglichen die schnelle Identifizierung von Änderungen.
- Änderungen sind personenbezogen - Sie können in der Historie nachverfolgen, wer was programmiert hat.
- Dateien liegen nur in einer Version vor - der aktuellen. Die Historie ist jederzeit rückverfolgbar und wiederherstellbar.
- Fertige Softwarestände können mit Tags versehen und später schnell wiederhergestellt werden.
- Versionsverwaltung ist Industriestandard, und die Übung im Studium wird Ihnen später helfen, sich zurechtzufinden.

## Git Schnellstart

1. Erstellen Sie einen GitHub-Account und ändern Sie Ihr Passwort.
2. Prüfen Sie, ob Sie Zugang zum passenden Repository haben.
3. Installieren Sie Git für Ihr Betriebssystem.
4. Konfigurieren Sie Git mit Ihrem Namen und Ihrer E-Mail-Adresse:

   ```
   git config --global user.name "Ihr Name"
   git config --global user.email "ihre.email@example.com"
   ```

5. Klonen Sie das Repository:

   ```
   git clone https://github.com/username/repository.git
   ```

6. Machen Sie sich mit den grundlegenden Git-Befehlen vertraut.

## Grundregeln im Umgang mit Git

1. Committen Sie Ihre Änderungen regelmäßig, idealerweise nach jeder wichtigen Änderung.
2. Überlassen Sie Git die Versionierung. Vermeiden Sie manuelle Versionierung in Dateinamen.
3. Sichern Sie nur wichtige Dateien in Git. Ignorieren Sie Kompilate, Backups und temporäre Dateien.
4. Vermeiden Sie das Committen von großen Binärdateien.
5. Testen Sie Ihren Code sorgfältig vor dem Commit.
6. Führen Sie vor jedem Commit ein `git pull` durch, um Ihre lokale Kopie zu aktualisieren.
7. Lösen Sie Konflikte sorgfältig und testen Sie erneut vor dem Commit.
8. Committen Sie nur getesteten Code mit ausreichenden Kommentaren und Headern.
9. Nutzen Sie aussagekräftige Commit-Nachrichten, die Ihre Änderungen erläutern.
10. Verwenden Sie Branches für neue Features oder Experimente.
11. Nutzen Sie Pull Requests für Code-Reviews und Diskussionen.
12. Halten Sie sich an die vereinbarten Coding-Standards Ihres Teams.

## Umgang mit binären Dateien

Git ist optimiert für textbasierte Dateien. Für binäre Dateien wie Bilder oder Dokumente:

1. Überlegen Sie, ob die Datei wirklich versioniert werden muss.
2. Nutzen Sie Git LFS (Large File Storage) für große Binärdateien.
3. Beachten Sie, dass Merges bei Binärdateien oft nicht automatisch möglich sind.

## Python-Integration

Für die Datenvisualisierung und -analyse können Sie Python-Skripte entwickeln:

```python
import matplotlib.pyplot as plt
import numpy as np

# Daten aus Git-Repository laden und visualisieren
data = np.loadtxt('data.txt')
plt.plot(data)
plt.title('Datenvisualisierung')
plt.show()
```

Speichern Sie solche Skripte im Git-Repository, um die Datenanalyse reproduzierbar zu machen.

# Header-Beispiels für c

```c
/******************************************************************************
 * Modul           : DemoGitPython.c                                          *
 *                                                                            *
 * Datum           : 19.10.2024                                               *
 *                                                                            *
 * Funktion        : Demonstration der Git-Integration und Python-Analyse     *
 *                                                                            *
 * Implementation  : GCC 11.2.0                                               *
 *                                                                            *
 * Hardware        : Beliebiger PC mit Git und Python-Installation            *
 *                                                                            *
 * Author          : (c) 2024, Max Mustermann                                 *
 *                                                                            *
 * Letzte Änderung : 19.10.2024                                               *
 *                                                                            *
 * Git-Repository  : https://github.com/username/repository                   *
 *                                                                            *
 * Python-Version  : 3.9.0                                                    *
 *                                                                            *
 ******************************************************************************/
/* Hinweis: Dieses Programm demonstriert die Integration von C-Code mit       *
 *          Git-Versionskontrolle und Python-basierter Datenanalyse.          *
 *          Stellen Sie sicher, dass Git installiert und konfiguriert ist     *
 *          und dass Python mit den benötigten Bibliotheken verfügbar ist.    *
 ******************************************************************************/
```

Dieser Header enthält die folgenden wichtigen Informationen:

1. Modulname
2. Erstellungsdatum
3. Funktionsbeschreibung
4. Verwendete Entwicklungsumgebung (GCC in diesem Fall)
5. Benötigte Hardware
6. Autor und Copyright-Information
7. Datum der letzten Änderung
8. Git-Repository-URL
9. Verwendete Python-Version
10. Zusätzliche Hinweise zur Git- und Python-Integration

Der Header ist so gestaltet, dass er leicht lesbar ist und alle wichtigen Informationen für Entwickler enthält, die mit dem Projekt arbeiten. Er berücksichtigt die Verwendung von Git für die Versionskontrolle und Python für mögliche Datenanalysen, was den aktualisierten Anforderungen entspricht.


# Programmierrichtlinie für C

## Modul- und Funktionsköpfe

Jedes Modul und jede Funktion sollte einen Kopf mit folgenden Informationen haben:

- Modulname/Funktionsname
- Datum der Erstellung
- Beschreibung/Zweck
- Implementierungsumgebung
- Autor
- Bemerkungen
- Datum der letzten Änderung
- Git-Repository-URL (für Module)
- Übergabeparameter und Rückgabewerte (für Funktionen)

## Namenskonventionen

### Funktionen

- CamelCase-Schreibweise
- Modulkürzel für globale Funktionen
- Beispiel: `void MD_MisalignmentDetection(void);`

### Konstanten

- Großbuchstaben mit Unterstrichen
- Typ als Suffix
- Beispiel: `#define MD_MAX_RAWCHANNEL_TRANSITIONS_u8 ((u8)20)`

### Benutzerdefinierte Datentypen

- Enden mit `_t`
- CamelCase-Schreibweise
- Beispiel: `typedef struct { ... } ResultValueStruct_t;`

### Variablen

- CamelCase-Schreibweise
- Typ als Suffix
- Modulpräfix für globale Variablen
- Beispiele:
  - `u16 MD_StdAlignmentAngle_u16;` (global)
  - `bool channelTransValid_bit;` (lokal)

## Sonderregeln

### Schleifeninkrement

- Einfache Zählvariablen in kurzen Schleifen erlaubt
- Sprechende Namen in komplexen Schleifen
- Beispiel: `for (index_u8=1; index_u8<3; index_u8++)`

## Wortwahl

- Deutsche Wörter für Variablennamen
- Lesbarkeit vor Kürze
- Vermeidung von Unterstrichen (außer bei Konstanten und Typsuffixen)
- Keine Bindestriche oder Sonderzeichen
- Vermeidung von Konflikten mit Sprachschlüsselwörtern

## Git-spezifische Ergänzungen

- Commit-Nachrichten sollten kurz und aussagekräftig sein
- Verwenden Sie aussagekräftige Branch-Namen für Features oder Bugfixes

## Python-Integration

Für Python-Skripte zur Datenanalyse:

- Verwenden Sie PEP 8 als Stilrichtlinie
- Dokumentieren Sie Funktionen mit Docstrings
- Nutzen Sie aussagekräftige Variablennamen, die mit der C-Codebase konsistent sind

Diese Richtlinien kombinieren die ursprünglichen C-Konventionen mit Best Practices für Git und berücksichtigen die mögliche Integration von Python für Datenanalyse.

# Software-Plagiat

## Definition
Ein Plagiat ist die unerlaubte Aneignung fremder geistiger Leistungen. Dies kann sich auf Code, Texte, Ideen oder andere kreative Werke beziehen.

## Konsequenzen
- An Hochschulen kann ein Plagiat zu schwerwiegenden Konsequenzen bis hin zur Exmatrikulation führen.
- Es schadet der akademischen Integrität und der eigenen Reputation.

## Vermeidung von Plagiaten

1. **Quellen zitieren**: 
   - Verwenden Sie Kommentare im Code, um Quellen zu kennzeichnen.
   - In Git-Commits können Sie Referenzen zu genutzten Quellen angeben.

2. **Lizenzprüfung**:
   - Überprüfen Sie stets die Lizenzbedingungen von fremdem Code.
   - Respektieren Sie die Bedingungen der Lizenzen.

3. **Verstehen statt Kopieren**:
   - Analysieren Sie fremden Code und erstellen Sie ein eigenes Konzept (z.B. PAP).
   - Implementieren Sie basierend auf Ihrem Verständnis.

4. **Dokumentation in Git**:
   - Nutzen Sie aussagekräftige Commit-Nachrichten, die Ihre Denkprozesse und Quellen reflektieren.
   - Verwenden Sie separate Branches für experimentelle Implementierungen.

5. **Integration von Python**:
   - Wenn Sie Python-Bibliotheken oder -Code verwenden, dokumentieren Sie dies klar.
   - Beispiel für einen Python-Kommentar:

     ```python
     # Verwendet numpy für numerische Berechnungen
     # Quelle: https://numpy.org/, BSD-3-Clause Lizenz
     import numpy as np
     ```

6. **Lizenzen in Git-Repository**:
   - Fügen Sie eine LICENSE-Datei zu Ihrem Repository hinzu, die klar die Bedingungen für die Nutzung Ihres Codes festlegt.
   - Erwähnen Sie in der README.md-Datei alle verwendeten externen Ressourcen und deren Lizenzen.

7. **Beispiel für Quellenverweis im Code**:

   ```python
   def some_function():
       """
       Diese Funktion basiert auf der Arbeit von [Autor] aus [Quelle].
       Lizenz: [Lizenztyp]
       Angepasst für [Ihr Projekt] von [Ihr Name] am [Datum].
       """
       # Implementierung
   ```

8. **Verwendung von .gitignore**:
   - Stellen Sie sicher, dass keine urheberrechtlich geschützten Materialien versehentlich in Ihr Git-Repository gelangen.

Durch sorgfältige Dokumentation, klare Quellenangaben und Respekt für Urheberrechte können Sie Plagiate vermeiden und gleichzeitig die Vorteile von Git und Python für Ihre Softwareentwicklung nutzen.

# Arduino Programmier-Challenge I WS 23/24

## Inhalt
Diese Challenge dient als Lernzielkontrolle und semesterbegleitende Abschlussprüfung. Sie umfasst Inhalte der Lektionen 1-6.

## Vorbereitung
- Wiederholen Sie Lektionen 1-6
- Üben Sie Softwareplanung mit dem PAP-Designer
- Bereiten Sie ein Arduino-Programmierungstemplate vor
- Machen Sie sich mit der Ansteuerung des Ampelmoduls vertraut

## Einleitung
Entwickeln Sie ein Frühwarnsystem für Eisberge für die RMS Titanic mit Ihrem Arduino-Baukasten.

## Anforderungen
1. Akustischer Alarm bei Eisberg <20 cm
2. Verwendung eines Sharp IR Entfernungssensors
3. Alarmstummschaltung via entprelltem Taster (Interrupt)
4. Filterung der Sensorwerte zur Vermeidung von Fehlalarmen
5. Ampelsignalisierung: Grün >45 cm
6. Gelb 20-45 cm
7. Rot <20 cm

## Durchführung

### Aufgabe 7.1: Softwareplanung (PAP)
- Erstellen Sie einen Programmablaufplan
- Speichern Sie als `EisbergWarnsystem.pdf` in Git

### Aufgabe 7.2: Implementierung
- Setzen Sie den Plan mit der Arduino IDE um
- Speichern Sie als `EisbergWarnsystem.ino` in Git

### Aufgabe 7.3: Testing
- Testen Sie die Erfüllung aller Anforderungen
- Dokumentieren Sie in einem Testprotokoll

### Aufgabe 7.4: Dokumentation
- Dokumentieren Sie nachhaltig in Git
- Befolgen Sie die C-Programmierrichtlinien
- Fügen Sie Headers und Kommentare hinzu

## Hinweise
- Eigenleistung ist erforderlich; Plagiate führen zu 0 Punkten
- Gehen Sie systematisch vor: Planung → Umsetzung → Test → Dokumentation

## Bewertung
Insgesamt 10 Punkte, aufgeteilt auf Planung, Umsetzung, Test und Dokumentation

## FAQ
- Anwesenheit ist Pflicht
- Bauteile werden im Labor bereitgestellt
- Verwendung von KI (z.B. ChatGPT) ist nicht erlaubt

Beachten Sie:
- Verwenden Sie Git für die Versionskontrolle anstelle von SVN
- Für etwaige Datenanalysen oder Visualisierungen können Sie Python-Skripte entwickeln und im Git-Repository speichern


# Arduino Programmier-Challenge II WS 23/24

## Inhalt
Diese Challenge dient als Lernzielkontrolle und semesterbegleitende Abschlussprüfung, basierend auf Lektionen 1-13.

## Vorbereitung
- Wiederholen Sie Lektionen 1-13
- Üben Sie Softwareplanung mit dem PAP-Designer
- Bereiten Sie ein Arduino-Programmierungstemplate vor

## Einleitung
Entwickeln Sie eine Einparkhilfe für Toyota (1980) mit Ihrem Arduino-Baukasten.

## Anforderungen
1. Akustischer Alarm bei Hindernis <1 m
2. Verwendung eines Ultraschallsensors HC-SR04
3. Alarmstummschaltung via entprelltem Taster (Interrupt)
4. Filterung der Sensorwerte zur Vermeidung von Fehlalarmen
5. Kein Alarm bei >1 m
6. Lineare Alarmfrequenzänderung 20 Hz - 1 Hz bei 20 cm - 1 m
7. Dauerton bei <20 cm

## Durchführung

### Aufgabe 14.1: Softwareplanung (PAP)
- Erstellen Sie einen Programmablaufplan
- Speichern Sie als `Einparkhilfe.pdf` in Git

### Aufgabe 14.2: Implementierung
- Setzen Sie den Plan mit der Arduino IDE um
- Speichern Sie als `Einparkhilfe.ino` in Git

### Aufgabe 14.3: Testing
- Testen Sie die Erfüllung aller Anforderungen
- Dokumentieren Sie in einem Testprotokoll

### Aufgabe 14.4: Dokumentation
- Dokumentieren Sie nachhaltig in Git
- Befolgen Sie die C-Programmierrichtlinien
- Fügen Sie Headers und Kommentare hinzu

## Hinweise
- Eigenleistung ist erforderlich; Plagiate führen zu 0 Punkten
- Gehen Sie systematisch vor: Planung → Umsetzung → Test → Dokumentation

## Bewertung
Insgesamt 10 Punkte + 5 Bonuspunkte, aufgeteilt auf Planung, Umsetzung, Test und Dokumentation

## FAQ
- Anwesenheit ist Pflicht
- Bauteile werden im Labor bereitgestellt
- Verwendung von KI (z.B. ChatGPT) ist nicht erlaubt

## Zusätzliche Git- und Python-spezifische Empfehlungen:

1. Verwenden Sie aussagekräftige Commit-Nachrichten in Git.
2. Erstellen Sie einen Feature-Branch für die Entwicklung und mergen Sie ihn nach Fertigstellung in den Hauptbranch.
3. Nutzen Sie `.gitignore`, um generierte Dateien und IDE-spezifische Dateien auszuschließen.
4. Für die Datenanalyse oder Visualisierung können Sie ein Python-Skript erstellen:

   ```python
   import matplotlib.pyplot as plt
   import numpy as np

   # Funktion zur Berechnung der Alarmfrequenz
   def alarm_frequency(distance):
       if distance > 100:
           return 0
       elif distance < 20:
           return 20
       else:
           return 20 - (distance - 20) * 19 / 80

   distances = np.linspace(0, 120, 200)
   frequencies = [alarm_frequency(d) for d in distances]

   plt.plot(distances, frequencies)
   plt.xlabel('Entfernung (cm)')
   plt.ylabel('Alarmfrequenz (Hz)')
   plt.title('Alarmfrequenz vs. Entfernung')
   plt.savefig('alarm_frequency_chart.png')
   plt.show()
   ```

   Speichern Sie dieses Skript als `visualize_alarm.py` in Ihrem Git-Repository.

5. Fügen Sie eine `README.md`-Datei hinzu, die das Projekt, seine Funktionen und die Einrichtungsschritte beschreibt.
