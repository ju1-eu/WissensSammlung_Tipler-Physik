---
title: "Mathe-Kfz-Elektrik"
author: "Jan Unger"
date: "2024-10-19"
---

# Mathe-Kfz-Elektrik

Letzte Aktualisierung: 2024-10-19

## Inhaltsverzeichnis

- [Mathe-Kfz-Elektrik](#mathe-kfz-elektrik)
  - [Inhaltsverzeichnis](#inhaltsverzeichnis)
  - [Arbeit - Leistung - Ohm'sche Gesetz](#arbeit---leistung---ohmsche-gesetz)
  - [Kabelquerschnitt Lüfter berechnen](#kabelquerschnitt-lüfter-berechnen)
  - [Arbeit einer Lampe berechnen](#arbeit-einer-lampe-berechnen)
  - [Stromaufnahme Lüfter berechnen](#stromaufnahme-lüfter-berechnen)
  - [Reihenschaltung](#reihenschaltung)
  - [Parallelschaltung](#parallelschaltung)
  - [Unbelasteter Spannungsteiler](#unbelasteter-spannungsteiler)
  - [Belasteter Spannungsteiler](#belasteter-spannungsteiler)
  - [Ruhestrom berechnen](#ruhestrom-berechnen)
  - [Temperatursensor NTC / PTC](#temperatursensor-ntc--ptc)
  - [PWM - pulsweitenmoduliertes Signal](#pwm---pulsweitenmoduliertes-signal)
    - [Regelfrequenz berechnen](#regelfrequenz-berechnen)
    - [Beispiel einer LED-Helligkeitssteuerung mittels Pulsweitenmodulation](#beispiel-einer-led-helligkeitssteuerung-mittels-pulsweitenmodulation)
  - [FM - frequenzmoduliertes Signal für Drehstrommotoren](#fm---frequenzmoduliertes-signal-für-drehstrommotoren)
  - [Widerstand](#widerstand)
    - [LDR + Widerstand + LED](#ldr--widerstand--led)
    - [Poti + Widerstand + LED](#poti--widerstand--led)
    - [Spannungsteiler belastet](#spannungsteiler-belastet)
    - [Stromteiler](#stromteiler)
    - [Pull-up und Pull-down](#pull-up-und-pull-down)
  - [Kondensator](#kondensator)
    - [Kondensatoren Parallel](#kondensatoren-parallel)
    - [Kondensatoren in Reihe](#kondensatoren-in-reihe)
    - [RC-Glied](#rc-glied)


## Arbeit - Leistung - Ohm'sche Gesetz

1. **W = P x t**:
   - **W** Arbeit in Joule (J) oder Wattstunden (Wh).
   - **P** Leistung in Watt (W).
   - **t** Zeit in Sekunden (s) oder Stunden (h).

2. **P = U x I**:
   - **P** Leistung in Watt.
   - **U** Spannung in Volt (V).
   - **I** Strom in Ampere (A).

3. **U = R x I**:
   - **U** Spannung in Volt.
   - **R** Widerstand in Ohm gemessen.
   - **I** Strom in Ampere.


\newpage
## Kabelquerschnitt Lüfter berechnen

```
# Schaltplan Lüfter: Kabelquerschnitt 0,5 mm^2 und Leitungslänge 20 m
   +----[R_Leitung]----+
   |                   |
 + o                   o 
  [UB]            [R_Lüfter]
 - o                   o 
   |                   |
   +----[R_Leitung]----+
```

**1. Leitungswiderstand $R_{\text{Leitung}}$:**

Gegeben sind:

- Leitungslänge $l$ = 10 m (Hin und Rückweg 20 m)
- Kabelquerschnitt $A = 0,5~mm^2$
- Spezifischer Widerstand von Kupfer $\rho$ = $0,0175 \Omega \times mm^2/m$ 

Die Formel für den Leitungswiderstand ist:

- $R_{\text{Leitung}} = \frac{\rho \times l}{A} = \frac{0,0175 \times 20}{0,5} = 0,7 \, \Omega$

**2. Gesamtwiderstand $R_{\text{ges}}$:**

- $R_{\text{ges}} = R_{\text{Leitung}} + R_{\text{Lüfter}} = 0,7 \, \Omega + 0,48 \, \Omega = 1,18 \, \Omega$

**3. Stromaufnahme $I$:** Die Gesamtspannung $U_{\text{ges}}$ ist 12 V.

- $I = \frac{U_{\text{ges}}}{R_{\text{ges}}} = \frac{12 \, \text{V}}{1,18 \, \Omega} = 10,17 \, \text{A}$

**4. Spannung am Lüfter $U_{\text{Lüfter}}$:**

- $U_{\text{Lüfter}} = R_{\text{Lüfter}} \times I = 0,48 \, \Omega \times 10,17 \, \text{A} = 4,88 \, \text{V}$

**Problem** wenn der Lüfter 12 V und 300 W benötigt, dann sollte der Strom bei 25 A liegen. Die berechnete Spannung am Lüfter sollte ebenfalls nahe an 12 V liegen, und nicht bei 4,88 V.

**Lösung**

```
# Schaltplan Lüfter: Kabelquerschnitt erhöhen und Leitungslänge verkürzen
 +U o-+-------------------
      |     
  [R_Leitung]    
      |
      o     
  [R_Lüfter]
      o  
      |      
GND o-+-------------------
```

1. **Stromaufnahme des Lüfters $I$:** Angenommen $U_{\text{Lüfter}}$ ist ungefähr 12 V (da der maximale Spannungsabfall am Lüfter 0,5 V beträgt, ist die Mindestspannung, die der Lüfter haben sollte, 11,5 V):

- $I = \frac{U_{\text{Lüfter}}}{R_{\text{Lüfter}}} = \frac{11,5 \, \text{V}}{0,48 \, \Omega} = 23,96 \, \text{A}$

2. **Berechnung des Widerstands der Leitung $R_{\text{Leitung}}$ basierend auf dem maximalen Spannungsabfall:** Da der maximale Spannungsabfall 0,5 V beträgt:

- $R_{\text{Leitung}} = \frac{U_{\text{Spannungsabfall}}}{I} = \frac{0,5 \, \text{V}}{23,96 \, \text{A}} \approx 0,0209 \, \Omega$

3. **Erforderlicher Leiterquerschnitt unter Berücksichtigung der halbierten Leitungslänge:** Die Leitungslänge beträgt jetzt $l = 10 \, \text{m}$ (wegen der Verwendung der Karosserie als Masse). 

Die Formel für den Leitungswiderstand lautet: $R_{\text{Leitung}} = \frac{\rho \times l}{A}$

Daraus ergibt sich für $A$:

- $A = \frac{\rho \times l}{R_{\text{Leitung}}} = \frac{0,0175 \times 10}{0,0209} \approx 8,373 \, \text{mm}^2$

Für die gegebene Anwendung sollte daher ein Kabel mit einem Querschnitt von mindestens $8,373~\text{mm}^2$ gewählt werden. Es wäre jedoch ratsam, einen Sicherheitsfaktor einzubeziehen und ein Kabel mit einem etwas größeren Querschnitt zu wählen, z. B. $10~\text{mm}^2$.

\newpage
## Arbeit einer Lampe berechnen

Um die Arbeit die von der Lampe verbraucht wurde, zu berechnen, verwenden wir die Formel:

$W = P \times t$

Dabei ist:

- $W$ die Arbeit in Wattstunden (Wh)
- $P$ die Leistung der Lampe in Watt (W)
- $t$ die Zeit in Stunden

Die Leistung $P$ kann berechnet werden mit:

- $P = U \times I = 12 \, \text{V} \times 0,417 \, \text{A} = 5,004 \, \text{W}$

Die Lampe leuchtet 30 Minuten, was 0,5 Stunden entspricht.

- $W = 5,004 \, \text{W} \times 0,5 \, \text{h} = 2,502 \, \text{Wh}$

Wenn die Lampe 30 Minuten lang leuchtet, hat sie also eine Arbeit von 2,502 Wh verrichtet.

## Stromaufnahme Lüfter berechnen

Um den Strom $I$ zu berechnen, den ein Gerät bei gegebener Spannung $U$ und Leistung $P$ aufnimmt, kann das Ohm'sche Gesetz und die Leistungsformel verwendet werden.

$P = U \times I$

Gegeben: $U = 12 \, \text{V}, P = 300 \, \text{W}$

- $I = \frac{P}{U} = \frac{300 \, \text{W}}{12 \, \text{V}} = 25 \, \text{A}$

Der Lüfter hat also eine Stromaufnahme von 25 Ampere bei einer Spannung von 12 Volt und einer Leistung von 300 Watt.

\newpage
## Reihenschaltung

**Zwei Widerstände $R_1$ und $R_2$ sind in Reihe geschaltet:**

Der Gesamtwiderstand $R_{\text{ges}}$ ist die Summe der einzelnen Widerstände, und der Gesamtstrom $I_{\text{ges}}$ ist derselbe Strom, der durch alle Widerstände fließt.

```
# Schaltplan: Widerstände in Reihe
 +U o-+-------------------
      |     
     [R1]    
      |     
     [R2]    
      |      
GND o-+-------------------
```

**1. Gesamtwiderstand $R_{\text{ges}}$:**

- $R_{\text{ges}} = R_1 + R_2 = 30 \, \Omega + 60 \, \Omega = 90 \, \Omega$

**2. Gesamtstrom $I_{\text{ges}}$ mittels Ohm'schem Gesetz:**

- $I = \frac{U}{R} \to I_{\text{ges}} = \frac{12 \, \text{V}}{90 \, \Omega} = 0,1333 \, \text{A}$ oder $133,3 \, \text{mA}$

**3. Teilspannungen $U_1$ und $U_2$:** Für eine Reihenschaltung gilt, dass die Summe der Teilspannungen gleich der Gesamtspannung ist. Die Teilspannung an einem Widerstand ist das Produkt aus dem Strom, der durch den Widerstand fließt, und dem Widerstandswert:

- $U_1 = I_{\text{ges}} \times R_1 = 0,1333 \, \text{A} \times 30 \, \Omega = 4 \, \text{V}$

- $U_2 = I_{\text{ges}} \times R_2 = 0,1333 \, \text{A} \times 60 \, \Omega = 8 \, \text{V}$

Zusammengefasst:

- $R_{\text{ges}} = 90 \, \Omega$
- $I_{\text{ges}} = 133,3 \, \text{mA}$
- $U_1 = 4 \, \text{V}$
- $U_2 = 8 \, \text{V}$

Die Teilspannungen ergeben zusammen 12 V, was der Gesamtspannung entspricht.

**Drei Widerstände $R_1$, $R_2$ und $R_3$ sind in Reihe geschaltet:**

geg: zusätzlicher Widerstand $R_3$ von 90 Ohm.

```
# Schaltplan: Widerstände in Reihe
 +U o-+-------------------
      |     
     [R1]    
      |     
     [R2]    
      |
     [R3]
      |      
GND o-+-------------------
```

**1. Gesamtwiderstand $R_{\text{ges}}$:**

- $R_{\text{ges}} = R_1 + R_2 + R_3 = 30 \, \Omega + 60 \, \Omega + 90 \, \Omega = 180 \, \Omega$

**2. Gesamtstrom $I_{\text{ges}}$ mittels Ohm'schem Gesetz:**

- $I = \frac{U}{R} \to I_{\text{ges}} = \frac{12 \, \text{V}}{180 \, \Omega} = 0,0667 \, \text{A}$ oder $66,7 \, \text{mA}$

**3. Teilspannungen $U_1$, $U_2$ und $U_3$:**

- $U_1 = I_{\text{ges}} \times R_1 = 0,0667 \, \text{A} \times 30 \, \Omega = 2 \, \text{V}$

- $U_2 = I_{\text{ges}} \times R_2 = 0,0667 \, \text{A} \times 60 \, \Omega = 4 \, \text{V}$

- $U_3 = I_{\text{ges}} \times R_3 = 0,0667 \, \text{A} \times 90 \, \Omega = 6 \, \text{V}$

Zusammengefasst:

- $R_{\text{ges}} = 180 \, \Omega$
- $I_{\text{ges}} = 66,7 \, \text{mA}$
- $U_1 = 2 \, \text{V}$
- $U_2 = 4 \, \text{V}$
- $U_3 = 6 \, \text{V}$

Die Teilspannungen ergeben zusammen 12 V, was der Gesamtspannung entspricht.

\newpage
## Parallelschaltung

**Zwei Widerstände $R_1$ und $R_2$ sind parallel geschaltet:**

```
# Schaltplan: Widerstände parallel
 +U o-+----+-----------
      |    |   
     [R1] [R2]  
      |    |   
GND o-+----+-----------
```

**1. Berechnung des Gesamtwiderstands $R_{\text{ges}}$ einer Parallelschaltung:**

- $\frac{1}{R_{\text{ges}}} = \frac{1}{R_1} + \frac{1}{R_2}$
- $\frac{1}{R_{\text{ges}}} = \frac{1}{30 \, \Omega} + \frac{1}{60 \, \Omega}$
- $\frac{1}{R_{\text{ges}}} = \frac{1 + 0,5}{30}$
- $\frac{1}{R_{\text{ges}}} = \frac{1,5}{30}$
- $\frac{1}{R_{\text{ges}}} = 0,05$ Umkehren: $R_{\text{ges}} = 20 \, \Omega$

**2. Gesamtstrom $I_{\text{ges}}$ mittels Ohm'schem Gesetz:**

- $I = \frac{U}{R} \to I_{\text{ges}} = \frac{12 \, \text{V}}{20 \, \Omega} = 0,6 \, \text{A}$ oder $600 \, \text{mA}$

**3. Teilströme $I_1$ und $I_2$:** Da die Spannung über jedem Widerstand in einer Parallelschaltung gleich ist, können wir das Ohm'sche Gesetz verwenden, um die Ströme zu berechnen:

- $I_1 = \frac{U}{R_1} = \frac{12 \, \text{V}}{30 \, \Omega} = 0,4 \, \text{A}$ oder $400 \, \text{mA}$

- $I_2 = \frac{U}{R_2}  = \frac{12 \, \text{V}}{60 \, \Omega} = 0,2 \, \text{A}$ oder $200 \, \text{mA}$

Zusammengefasst:

- $R_{\text{ges}} = 20 \, \Omega$
- $I_{\text{ges}} = 600 \, \text{mA}$
- $I_1 = 400 \, \text{mA}$
- $I_2 = 200 \, \text{mA}$

Beachte, dass die Summe der Teilströme ($I_1 + I_2$) dem Gesamtstrom $I_{\text{ges}}$ entspricht.

**Drei Widerstände $R_1$, $R_2$ und $R_3$ sind parallel geschaltet:**

geg: zusätzlicher Widerstand $R_3$ von 90 Ohm.

```
# Schaltplan: Widerstände parallel
 +U o-+----+----+--------
      |    |    |
     [R1] [R2] [R3]
      |    |    |
GND o-+----+----+--------
```

**1. Berechnung des Gesamtwiderstands $R_{\text{ges}}$ einer Parallelschaltung:**

- $\frac{1}{R_{\text{ges}}} = \frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3}$
- $\frac{1}{R_{\text{ges}}} = \frac{1}{30 \, \Omega} + \frac{1}{60 \, \Omega} + \frac{1}{90 \, \Omega}$
- $\frac{1}{R_{\text{ges}}} = \frac{1 + 0,5 + 0,33}{30}$
- $\frac{1}{R_{\text{ges}}} = \frac{1,8333}{30}$
- $\frac{1}{R_{\text{ges}}} = 0,06111$ Umkehren: $R_{\text{ges}} \approx 16,36 \, \Omega$

**2. Gesamtstrom $I_{\text{ges}}$ mittels Ohm'schem Gesetz:**

- $I = \frac{U}{R} \to I_{\text{ges}} = \frac{12 \, \text{V}}{16,36 \, \Omega} \approx 0,733 \, \text{A}$ oder $733 \, \text{mA}$

**3. Teilströme $I_1$, $I_2$ und $I_3$:**

- $I_1 = \frac{U}{R_1} = \frac{12 \, \text{V}}{30 \, \Omega} = 0,4 \, \text{A}$ oder $400 \, \text{mA}$

- $I_2 = \frac{U}{R_2} = \frac{12 \, \text{V}}{60 \, \Omega} = 0,2 \, \text{A}$ oder $200 \, \text{mA}$

- $I_3 = \frac{U}{R_3} = \frac{12 \, \text{V}}{90 \, \Omega} \approx 0,133 \, \text{A}$ oder $133 \, \text{mA}$

Zusammengefasst:

- $R_{\text{ges}} \approx 16,36 \, \Omega$
- $I_{\text{ges}} \approx 733 \, \text{mA}$
- $I_1 = 400 \, \text{mA}$
- $I_2 = 200 \, \text{mA}$
- $I_3 \approx 133 \, \text{mA}$

\newpage
## Unbelasteter Spannungsteiler

Ein unbelasteter Spannungsteiler bedeutet, dass kein Verbraucher an seinen Ausgängen angeschlossen ist und der gesamte Stromfluss durch die in Serie geschalteten Widerstände R_1 und R_2 geht.

```
# Schaltplan: unbelasteter Spannungsteiler
 +U o-+--------------------
      |
     [R1]
      |
      +----o U2
      |    
     [R2]    
      |     
GND o-+--------------------
```

**1. Gesamtwiderstand $R_{\text{ges}}$:** Bei einer Reihenschaltung von Widerständen addieren sich die Widerstände einfach:

- $R_{\text{ges}} = R_1 + R_2 = 30 \, \Omega + 60 \, \Omega = 90 \, \Omega$

**2. Gesamtstrom $I_{\text{ges}}$:** Nach dem Ohmschen Gesetz berechnet sich der Strom, der durch eine Schaltung fließt, als:

- $I = \frac{U}{R} \to I_{\text{ges}} = \frac{12 \, \text{V}}{90 \, \Omega} = 0,1333 \, \text{A} = 133,3 \, \text{mA}$

**3. Teilspannungen $U_1$ und $U_2$:** Die Spannung, die an einem Widerstand in einer Reihenschaltung abfällt, ist direkt proportional zu seinem Widerstandswert.

- $U_1 = I_{\text{ges}} \times R_1 = 133,3 \, \text{mA} \times 30 \, \Omega = 4 \, \text{V}$

- $U_2 = I_{\text{ges}} \times R_2  = 133,3 \, \text{mA} \times 60 \, \Omega = 8 \, \text{V}$

**Zusammenfassung:**

- $R_{\text{ges}}$ = $90~\Omega$
- $I_{\text{ges}}$ = 133,3 mA
- $U_1$ = 4 V
- $U_2$ = 8 V

Wie erwartet, summiert sich die Spannung, die über R_1 und R_2 abfällt, zu der gesamten anliegenden Spannung von 12 V.

\newpage
## Belasteter Spannungsteiler

Hier soll ein Spannungsteiler betrachtet werden, bei dem $R_1$ in Serie zu einer Parallelschaltung aus $R_2$ und $R_3$ liegt.

```
# Schaltplan: belasteter Spannungsteiler
  +U o-+---------------------
       |
      [R1]
       |
       +------+--o U2,3
       |      |
       |      o
      [R2]   [R3]
       |      o
       |      |
 GND o-+------+-------------
```

**1. Berechnen des Gesamtwiderstandes $R_{2,3}$ der Parallelschaltung von $R_2$ und $R_3$:**

- $R_{2,3} = \frac{R_2 \times R_3}{R_2 + R_3} = \frac{60 \, \Omega \times 90 \, \Omega}{60 \, \Omega + 90 \, \Omega} = \frac{5400}{150} = 36 \, \Omega$

**2. Gesamtwiderstand $R_{\text{ges}}$ der gesamten Schaltung:**

- $R_{\text{ges}} = R_1 + R_{2,3} = 30 \, \Omega + 36 \, \Omega = 66 \, \Omega$

**3. Gesamtstrom $I_{\text{ges}}$:**

- $I_{\text{ges}} = \frac{U}{R_{\text{ges}}} = \frac{12 \, \text{V}}{66 \, \Omega} = 0,1818 \, \text{A} = 181,8 \, \text{mA}$

**4. Teilspannungen $U_1$ und $U_{2,3}$:**

- $U_1 = I_{\text{ges}} \times R_1 = 181,8 \, \text{mA} \times 30 \, \Omega = 5,4545 \, \text{V}$

- Parallelschaltung: $U_{2,3} = I_{\text{ges}} \times R_{2,3} = 181,8 \, \text{mA} \times 36 \, \Omega = 6,5454 \, \text{V}$

**5. Teilströme $I_1$ und $I_2$ durch $R_1$ bzw. $R_2$ (und $R_3$):**

- Der Strom durch $R_1$ ist der Gesamtstrom:
   - $I_1 = I_{\text{ges}} = 181,8 \, \text{mA}$

- Der Strom $I_2$ durch $R_2$:
   - $I_2 = \frac{U_{2,3}}{R_2} = \frac{6,5454 \, \text{V}}{60 \, \Omega} = 109,1 \, \text{mA}$

- Da $R_2$ und $R_3$ parallel geschaltet sind und die gleiche Spannung $U_{2,3}$ abfällt, ist der Strom durch $R_3$:
   - $I_3 = \frac{U_{2,3}}{R_3} = \frac{6,5454 \, \text{V}}{90 \, \Omega} = 72,7 \, \text{mA}$

**Zusammenfassung:**

- $R_{\text{ges}}$ = $66 \, \Omega$
- $I_{\text{ges}}$ = 181,8 mA
- $U_1$ = 5,45 V
- $U_{2,3}$ = 6,55 V
- $I_1$ = $I_{\text{ges}}$
- $I_2$ = 109,1 mA
- $I_3$ = 72,7 mA

\newpage
## Ruhestrom berechnen

Spannung über Sicherung messen

$I_\text{Teilsystem} = \frac{U_\text{Spannung}}{R_\text{Sicherung}}$

| **Standard-Sicherung** | $R_\text{Sicherung}$  |
| :--------------------: | :-------------------: |
|          5 A           | 15 $\text{m} \Omega$  |
|          10 A          | 7,5 $\text{m} \Omega$ |
|          15 A          | 4,5 $\text{m} \Omega$ |
|          20 A          | 3,3 $\text{m} \Omega$ |
|          25 A          | 2,1 $\text{m} \Omega$ |
|          30 A          | 1,6 $\text{m} \Omega$ |

| **Mini-Sicherung** |  $R_\text{Sicherung}$  |
| :----------------: | :--------------------: |
|        5 A         | 16,7 $\text{m} \Omega$ |
|       7,5 A        |  10 $\text{m} \Omega$  |
|        10 A        |  7 $\text{m} \Omega$   |


**Beispiel:** Teilsystem wird über $20~A$ Standard-Sicherung abgesichert. 

An der Sicherung wird eine Spannung von $5,2~mV$ gemessen. 

- Ruhestrom berechnen: $I_\text{Teilsystem} = \frac{U_\text{Spannung}}{R_\text{Sicherung}} = \frac{5,2~mV}{3,3~m\Omega} = 1,58~A$.

\newpage
## Temperatursensor NTC / PTC

- NTC: Je höher die Temperatur wird, desto niedriger ist ihr Widerstandswert.
- PTC: Je höher die Temperatur wird, desto größer ist ihr Widerstandswert.

Kennlinie des temperaturabhängigen Widerstands bestimmen

```
# Schaltplan: Temperatursensor NTC + SG
+--------------------+
|  -+-o (+5V)        | 
|   |           SG   |
|  [Ri]              |
|   |                |
|   +--[CPU] +----+  |
|   |        |    |  |
+---o--------o----o--+
    |        |    |
  [NTC]      |   GND
    |        | 
    +--------+
```

**Meßwiderstand = Innenwiderstand $R_i$ im SG berechnen:**

Gegeben: $U_\text{o} = 5 \text{ V}$, $I_\text{o} = 2,5 \text{ mA} = 0,0025 \text{ A}$ (Werte messen, Stecker trennen am SG)

- $R_i = \frac{U_\text{o}}{I_\text{o}} = \frac{5 \text{ V}}{0,0025 \text{ A}} = 2000 \Omega = 2 \text{ k}\Omega$

**Widerstandswert des Sensors berechnen:**

**NTC Warm:** $U_{\text{Sensor1}} = 0,5 \text{ V}$ (gemessen im laufenden Betrieb)

- $R_{\text{Sensor1}} = \frac{U_{\text{Sensor1}} \times R_i}{U_\text{o} - U_{\text{Sensor1}}}  = \frac{0,5 \times 2000}{5 - 0,5} = \frac{1000}{4,5} = 222,22~\Omega$

**NTC Kalt:** $U_{\text{Sensor2}} = 4,5 \text{ V}$ (gemessen im laufenden Betrieb)

- $R_{\text{Sensor2}} = \frac{U_{\text{Sensor2}} \times R_i}{U_\text{o} - U_{\text{Sensor2}}} = \frac{4,5 \times 2000}{5 - 4,5} = \frac{9000}{0,5} = 18000~\Omega = 18 \text{ k}\Omega$

Zusammengefasst:

- SG Innenwiderstand: $R_i = 2 \text{ k}\Omega$
- NTC Warm: $R_{\text{Sensor1}} = 222,22~\Omega \to U_{\text{Sensor1}} = 0,5 \text{ V}$
- NTC Kalt: $R_{\text{Sensor2}} = 18 \text{ k}\Omega \to U_{\text{Sensor2}} = 4,5 \text{ V}$

\newpage
## PWM - pulsweitenmoduliertes Signal

PWM-Signal:

- **Frequenz**: Das ist die Anzahl der Pulse pro Sekunde, gemessen in Hertz (Hz). Diese Frequenz bleibt in den meisten PWM-Systemen konstant.

- **Tastverhältnis**: Das ist das Verhältnis der Dauer, in der das Signal eingeschaltet (High) ist, im Vergleich zur gesamten Periodendauer des Signals. Das Tastverhältnis wird oft in Prozent ausgedrückt und zeigt an, welcher Teil der Periode das Signal aktiv ist.
   - **100\% Tastverhältnis**: Das Signal ist ständig eingeschaltet (high).
   - **0\% Tastverhältnis**: Das Signal ist ständig ausgeschaltet (low).
   - **50\% Tastverhältnis**: Das Signal ist genau die Hälfte der Zeit eingeschaltet und die andere Hälfte ausgeschaltet.


1. **Berechnung der Periodendauer $T$**
   - Gegeben: $f = 200 \text{ Hz}$
   - Ansteuerfrequenz: $f = \frac{1}{T}$
   - Umstellen: $T = \frac{1}{f} = \frac{1}{200 \text{ Hz}} = 0,005 \text{ s} = 5 \text{ ms}$

2. **Berechnung der Einschaltzeit $t_{ein}$**
   - Gegeben: $TV_{\%} = 70\%$
   - $TV_{\%} = \frac{t_{ein}}{T} \times 100\% \Rightarrow t_{ein} = TV_{\%} \times T = 0,70 \times 5 \text{ ms} = 3,5 \text{ ms}$

3. **Berechnung der Ausschaltzeit $t_{aus}$**
   - Die gesamte Periode $T$ setzt sich aus der Summe von $t_{ein}$ und $t_{aus}$ zusammen:
   - $T = t_{ein} + t_{aus} \Rightarrow t_{aus} = T - t_{ein} = 5 \text{ ms} - 3,5 \text{ ms} = 1,5 \text{ ms}$

4. **Berechnung des Tastverhältnisses $TV$**
   - $TV = \frac{t_{ein}}{t_{aus}} = \frac{3,5 \text{ ms}}{1,5 \text{ ms}} = 2,33$

Zusammengefasst:

- Periodendauer $T$ = 5 ms
- Einschaltzeit $t_{ein}$ = 3,5 ms
- Ausschaltzeit $t_{aus}$ = 1,5 ms
- Tastverhältnis $TV$ = 2,33

**Hinweis:** Das berechnete Tastverhältnis $TV$ von 2,33 besagt, dass die "Einschaltzeit" 2,3x so lang ist wie die "Ausschaltzeit". Das gegebene $TV_{\%}$ von 70\% gibt den Prozentsatz der Periodendauer an, während der Impuls "ein" ist.


### Regelfrequenz berechnen 

$T$ ist die Periodendauer: $f = \frac{1}{T}$

Um die Periodendauer für eine einzelne Periode zu finden, teilen wir die gegebene Gesamtdauer durch die Anzahl der Perioden:

1. **Oszi (geg: 4x Perioden = 20 s):**
   - Periodendauer: $T_1 = \frac{20 \text{ s}}{4} = 5 \text{ s}$

   - Frequenz: $f_1 = \frac{1}{T_1} = \frac{1}{5 \text{ s}} = 0,2 \text{ Hz}$

2. **Oszi (geg: 5x Perioden = 50 ms):**
   - Periodendauer: $T_2 = \frac{50 \text{ ms}}{5} = 10 \text{ ms} = 0,01 \text{ s}$

   - Frequenz: $f_2 = \frac{1}{T_2} = \frac{1}{0,01 \text{ s}} = 100 \text{ Hz}$

Zusammenfassung:

- Für 4x Perioden = 20 s, $f_1 = 0,2 \text{ Hz}$
- Für 5x Perioden = 50 ms, $f_2 = 100 \text{ Hz}$

### Beispiel einer LED-Helligkeitssteuerung mittels Pulsweitenmodulation

**Angabe:** 
Wir wollen die Helligkeit einer LED mit einer Pulsweitenmodulation (PWM) bei einer konstanten Frequenz von 100 Hz steuern. Das bedeutet, es gibt 100 Pulse pro Sekunde. Die volle Periodendauer eines Pulses beträgt demzufolge:

$T = \frac{1}{f} = \frac{1}{100 \text{ Hz}} = 0,01 \text{ s} = 10 \text{ ms}$

**Ziel:** 
Die LED soll nur zu 40\% ihrer maximalen Helligkeit leuchten.

**Lösung:** 
Um die LED mit 40\% ihrer maximalen Helligkeit zu betreiben, setzen wir das Tastverhältnis auf: $TV = 40\% = 0,4$

Das bedeutet, dass das PWM-Signal für 40\% der gesamten Periodendauer "ein" und für die restlichen 60\% "aus" sein wird.

Berechnen der "Einschaltzeit": $t_{ein} = TV \times T = 0,4 \times 10 \text{ ms} = 4 \text{ ms}$

Die "Ausschaltzeit" ist: $t_{aus} = T - t_{ein} = 10 \text{ ms} - 4 \text{ ms} = 6 \text{ ms}$

**Ergebnis:**
Um die LED mit 40\% ihrer maximalen Helligkeit zu betreiben, sollte das PWM-Signal für 4 ms einer 10 ms Periode "ein" und für die restlichen 6 ms "aus" sein.

\newpage
## FM - frequenzmoduliertes Signal für Drehstrommotoren

**Wie es funktioniert:**
Ein Drehstrommotor dreht sich aufgrund des rotierenden Magnetfelds, das durch die dreiphasige Wechselspannung erzeugt wird. Die Geschwindigkeit des Motors hängt von der Frequenz dieses Magnetfelds ab. Ein Frequenzumrichter steuert die Geschwindigkeit des Motors, indem er die Frequenz der zugeführten Energie verändert.

**Gegeben:**
Ein Drehstrommotor mit einer Nennleistung von 5 kW und einer Nenndrehzahl von 1500 U/min wird für einen Antrieb verwendet. Der Motor ist für eine Netzspannung von 400 V und eine Frequenz von 50 Hz ausgelegt. Die Produktionsanforderung verlangt nun eine Reduzierung der Motorleistung auf 50 \%, d.h. die Drehzahl muss auf die Hälfte reduziert werden.

**Fragestellung:**
Wie muss die Frequenz eingestellt werden, um die gewünschte Drehzahl zu erreichen?

**Lösung:**

Die Geschwindigkeit eines Drehstrommotors ist direkt proportional zur Frequenz. Wenn die Drehzahl halbiert werden soll, muss auch die Frequenz halbiert werden.

- Drehzahlverhältnis: $\text{Verhältnis} = \frac{\text{gewünschte Drehzahl}}{\text{Nenndrehzahl}} = \frac{750 \text{ U/min}}{1500 \text{ U/min}} = 0,5$

- $\text{Neue Frequenz} = \text{Nennfrequenz} \times \text{Verhältnis} = 50 \text{ Hz} \times 0,5 = 25 \text{ Hz}$

**Ergebnis:**
Um die Drehzahl des Motors auf 750 U/min zu reduzieren, sollte die Frequenz des Frequenzumrichters auf 25 Hz eingestellt werden.

\newpage
## Widerstand

**Spannungsteiler unbelastet**

```
# Schaltplan: unbelasteter Spannungsteiler
+Uin o-+--------------------
       |
      [R1]
       |
       +----o Uout
       |    
      [R2]    
       |     
 GND o-+--------------------
```

$U_{out} = \left( \frac{R_2}{R_1 + R_2} \right) \times U_{in}$

nach $R_2$ umzustellen: $R_2 = \frac{U_{out} \times R_1}{U_{in} - U_{out}}$

1. **Berechnung von $R_2$**

gegebene Werte:
$U_{out} = 3.3V$
$U_{in} = 4.982V$
$R_1 = 1 \, \text{k} \Omega$

Formel für $R_2$:
$R_2 = \frac{U_{out} \times R_1}{U_{in} - U_{out}} = \frac{3.3V \times 1 \, \text{k} \Omega}{4.982V - 3.3V} = \frac{3.3 \, \text{k} \Omega}{1.682V} \approx 1.96 \, \text{k} \Omega$

2. **Berechnung von $U_1$ und $U_2$**

$\frac{U_1}{U_2} = \frac{R_1}{R_2}$

Da $U_2 = U_{out} = 3.3V$, können wir $U_1$ berechnen:

$U_1 = U_2 \times \frac{R_1}{R_2} = 3.3V \times \frac{1 \, \text{k} \Omega}{1.96 \, \text{k} \Omega}  \approx 1.683V$

Zur Überprüfung: $U_1 + U_2 = 1.683V + 3.3V = 4.983V$

3. **Überprüfung mit der dritten Formel:**

$\frac{U_{\text{ges}}}{R_{\text{ges}}} = \frac{U_1}{R_1} = \frac{U_2}{R_2} \to I_{\text{ges}} = I_1 = I_2$

$\frac{4.982V}{1 \, \text{k} \Omega + 1.96 \, \text{k} \Omega} = \frac{1.683V}{1 \, \text{k} \Omega} = \frac{3.3V}{1.96 \, \text{k} \Omega}$

Beide Seiten der Gleichung sollten denselben Wert für den Gesamtstrom durch den Teiler liefern, und daher sollte die Gleichung korrekt sein.

Insgesamt haben wir $R_2$ als ungefähr 1.96k und $U_1$ als 1.683V berechnet.

\newpage
### LDR + Widerstand + LED 

**Gegeben ist eine Schaltung mit einer Spannungsquelle von 4.982V, einem Strom von 0.58mA, einem Widerstand von 984 Ohm (1k) und einem LDR (Lichtabhängigen Widerstand) im hellen Zustand mit einem Widerstand von 1,7k Ohm in Reihe.** 

a) **Berechnen Sie die Gesamtleistung der Schaltung.**
b) **Berechnen Sie die Leistung, die am Widerstand von 984 Ohm abfällt.**
c) **Beurteilen Sie, ob ein 1/4 Watt Widerstand für diese Anwendung ausreichend ist.**

```
# Schaltplan: LDR + Widerstand + LED
+Uin o-+--------------------
       |
     [LDR]
       |
      [R]
       |    
     [LED]   
       |     
 GND o-+--------------------
```

**1. Berechnung der Gesamtleistung $P_{\text{ges}}$**

$P_{\text{ges}} = U \times I  = 4.982V \times 0.58mA = 2.88956 \, \text{mW}  \approx 2.89 \, \text{mW}$

**2. Berechnung der Leistung am Widerstand $P_R$**

$P_R = I^2 \times R = (0.58mA)^2 \times 984 \, \Omega = 0.336064 \, \text{mW} \approx 0.34 \, \text{mW}$

**3. Bewertung des 1/4 Watt Widerstands**

Ein 1/4 Watt Widerstand kann 250 mW (0.25W) an Leistung aushalten. Da die Leistung am Widerstand nur ungefähr 0.34 mW beträgt, ist dies weit unter der zulässigen Leistung des Widerstands. Daher ist der 1/4 Watt Widerstand mehr als ausreichend.

\newpage
### Poti + Widerstand + LED  

**Gegeben ist eine Schaltung mit einer Eingangsspannung von 4.982V und einem Gesamtstrom von 1.25mA. Ein Strom von 1.21mA fließt durch einen 1k Widerstand (genau 0.984k), und der Rest des Stroms fließt durch ein 100k Potenziometer, welches aktuell auf 95.3k eingestellt ist. Die beiden Elemente sind in Reihe geschaltet, und der 1k Widerstand ist für 1/4 Watt spezifiziert.**

a) **Berechnen Sie die Leistung, die am 1k Widerstand abfällt.**
b) **Ermitteln Sie die Gesamtleistung der Schaltung.**
c) **Beurteilen Sie, ob der 1/4 Watt Widerstand für diese Schaltung geeignet ist.**

```
# Schaltplan: Poti + Widerstand + LED  
+Uin o-+---------------------
       |
     + o  
    [Poti]o--+ Signal
     - o     |
       |     |
       |    [R1]
       |     |
       |   [LED]
       |     |
 GND o-+-----+--------------
```

**1. Leistung am Widerstand $R_1$ berechnen**

$P_{R_1} = I_1^2 \times R_1 = (1.21mA)^2 \times 0.984 \, \text{k} \Omega = 1.4408324  \, \text{mW}  \approx 1.44  \, \text{mW}$

**2. Gesamtleistung berechnen**

$P_{\text{ges}} = U \times I_{\text{ges}}  = 4.982V \times 1.25mA  = 6.2275  \, \text{mW}  \approx 6.23  \, \text{mW}$

**3. Beurteilung des 1/4 Watt Widerstands**

Ein 1/4 Watt Widerstand kann 250 mW aufnehmen. Die berechnete Leistung am Widerstand $R_1$ beträgt nur 1.44 mW, was weit unter 250 mW liegt. Daher ist der 1/4 Watt Widerstand mehr als ausreichend.

\newpage
### Spannungsteiler belastet

**Ein belasteter Spannungsteiler besteht aus einer Eingangsspannung von 5V und einer Ausgangsspannung von 3,3V. Zwei Widerstände $R_1$ und $R_2$ sind in Reihe geschaltet, wobei $R_2$ parallel zu einem Lastwiderstand $R_{Last}$ liegt. Der Laststrom $I_3$ beträgt 10mA, und der Strom $I_2$ durch $R_2$ soll 10\% von $I_3$ betragen.**

a) **Bestimmen Sie die Widerstandswerte $R_1$ und $R_2$.**
b) **Berechnen Sie die Teilströme $I_1$ und $I_2$.**
c) **Ermitteln Sie die Leistung an $R_1$ und $R_2$ unter Verwendung der Formel $P = U^2/R$.**
d) **Beurteilen Sie, ob ein 1/4-Watt-Widerstand für $R_1$ und $R_2$ ausreichend ist.**

```
# Schaltplan: belasteter Spannungsteiler
+Uin o-+---------------------
       |
      [R1]
       |
       +------+--o Uout
       |      |
       |      o
      [R2] [R_Last]
       |      o
       |      |
 GND o-+------+-------------
```

**1. Berechnung von $R_1$ und $R_2$**

Wenn $U_{out}$ oder $U_2$ gleich 3,3V ist, dann ist $U_1$ (die Spannung über $R_1$):

$U_1 = U_{in} - U_{out} = 5V - 3,3V = 1,7V$

Da $I_2$ 10% von $I_3$ ist: $I_2 = 0,1 \times I_3 = 0,1 \times 10mA = 1mA$

Da $I_2$ der Strom durch $R_2$ ist: $R_2 = \frac{U_2}{I_2} = \frac{3,3V}{1mA} = 3,3 \, \text{k} \Omega$

Für $R_1$ gilt, dass der gesamte Strom $I_{\text{ges}}$ durch $R_1$ fließt:

$I_{\text{ges}} = I_2 + I_3 = 1mA + 10mA = 11mA$

Daraus folgt: $R_1 = \frac{U_1}{I_{\text{ges}}} = \frac{1,7V}{11mA} \approx 154,5 \, \Omega$


**3. Berechnung der Leistung an $R_1$ und $R_2$**

$P_1 = \frac{U_1^2}{R_1} = \frac{(1,7V)^2}{154,5 \, \Omega} \approx 18,63 \, \text{mW}$

$P_2 = \frac{U_2^2}{R_2} = \frac{(3,3V)^2}{3,3 \, \text{k} \Omega} \approx 3,3 \, \text{mW}$

Somit haben wir $R_1 \approx 154,5 \, \Omega$, $R_2 = 3,3 \, \text{k} \Omega$, $P_1 \approx 18,63 \, \text{mW}$ und $P_2 \approx 3,3 \, \text{mW}$.

**Beurteilung des 1/4-Watt-Widerstands:**

Ein 1/4-Watt-Widerstand kann eine Leistung von 250 mW (0.25W) aushalten.

Betrachtet man die Leistung an $R_1$ und $R_2$:

$P_1 \approx 18,63 \, \text{mW}$ - dies liegt deutlich unter der zulässigen Leistung.

$P_2 \approx 3,3 \, \text{mW}$ - dies liegt deutlich unter der zulässigen Leistung.

\newpage
**Ein belasteter Spannungsteiler besteht aus einer Eingangsspannung von 9 V und einer Ausgangsspannung von 5 V. Zwei Widerstände $R_1$ und $R_2$ sind in Reihe geschaltet, wobei $R_2$ parallel zu einem Lastwiderstand $R_{Last}$ liegt. Der Laststrom $I_3$ beträgt 20 mA, und der Strom $I_2$ durch $R_2$ soll 10 \% von $I_3$ betragen.**

a) **Bestimmen Sie die Widerstandswerte $R_1$ und $R_2$.**
b) **Berechnen Sie die Teilströme $I_1$ und $I_2$.**
c) **Ermitteln Sie die Leistung an $R_1$ und $R_2$ unter Verwendung der Formel $P = U^2/R$.**
d) **Beurteilen Sie, ob ein 1/4-Watt-Widerstand für $R_1$ und $R_2$ ausreichend ist.**

```
# Schaltplan: belasteter Spannungsteiler
+Uin o-+---------------------
       |
      [R1]
       |
       +------+--o Uout
       |      |
       |      o
      [R2] [R_Last]
       |      o
       |      |
 GND o-+------+-------------
```

**a) Bestimmung von $R_1$ und $R_2$**

Wenn $U_{out}$ oder $U_2$ gleich 5V ist, dann ist $U_1$ (die Spannung über $R_1$):

$U_1 = U_{in} - U_{out} = 9V - 5V = 4V$

Da $I_2$ 10% von $I_3$ ist:

$I_2 = 0,1 \times I_3 = 0,1 \times 20mA = 2mA$

Da $I_2$ der Strom durch $R_2$ ist:

$R_2 = \frac{U_2}{I_2} = \frac{5V}{2mA} = 2.5 \, \text{k} \Omega$

Für $R_1$ gilt, dass der gesamte Strom $I_{\text{ges}}$ durch $R_1$ fließt:

$I_{\text{ges}} = I_2 + I_3 = 2mA + 20mA = 22mA$

Daraus folgt:

$R_1 = \frac{U_1}{I_{\text{ges}}} = \frac{4V}{22mA} \approx 181.8 \, \Omega$

**b) Berechnung von $I_1$ und $I_2$**

$I_2$ wurde bereits oben berechnet und ist 2mA.

$I_1$ ist gleich $I_{\text{ges}}$, also $I_1 = 22mA$.

**c) Berechnung der Leistung an $R_1$ und $R_2$**

$P_1 = \frac{U_1^2}{R_1} = \frac{(4V)^2}{181.8 \, \Omega} \approx 88.07mW$

$P_2 = \frac{U_2^2}{R_2} = \frac{(5V)^2}{2.5 \, \text{k} \Omega} \approx 10mW$

**d) Beurteilung des 1/4-Watt-Widerstands:**

Ein 1/4-Watt-Widerstand kann eine Leistung von 250mW (0.25W) aushalten.

Für $R_1$, $P_1 \approx 88.07mW$ - dies liegt unter der zulässigen Leistung von 250mW, daher ist der 1/4-Watt-Widerstand für $R_1$ ausreichend.

Für $R_2$, $P_2 \approx 10mW$ - auch dies liegt deutlich unter der zulässigen Leistung von 250mW, daher ist der 1/4-Watt-Widerstand auch für $R_2$ ausreichend.

\newpage
### Stromteiler

Gegeben ist eine Parallelschaltung mit den folgenden Werten:

- $U$ = 5 V
- $R_1$ = 1k = 1000 Ohm
- $R_2$ = 2k = 2000 Ohm

```
# Schaltplan: Stromteiler
U (+5V) 
   |
   +-------+---------+----
           |         |    
        [R1 1k]   [R2 2k]      
           |         |    
   +-------+---------+----
   |
  GND
```

1. **Gesamtwiderstand $R_{\text{ges}}$ der Parallelschaltung**: Da $R_1$ und $R_2$ parallel geschaltet sind, gilt:

$\frac{1}{R_{\text{ges}}} = \frac{1}{R1} + \frac{1}{R2} = \frac{1}{1000~\Omega} + \frac{1}{2000~\Omega} = 0.0015 \approx 666.67~\Omega$

2. **Ströme $I_1$ und $I_2$**: Mit dem Ohmschen Gesetz $I = \frac{U}{R}$:

$I_1 = \frac{U}{R1} = \frac{5 \text{ V}}{1000~\Omega} = 5 \text{ mA}$
$I_2 = \frac{U}{R2} = \frac{5 \text{ V}}{2000~\Omega} = 2.5 \text{ mA}$

3. **Gesamtstrom $I_{\text{ges}}$**: In einer Parallelschaltung addieren sich die Ströme:

$I_{\text{ges}} = I1 + I2 = 5 \text{ mA} + 2.5 \text{ mA} = 7.5 \text{ mA}$

4. **Gesamtleistung $P_{\text{ges}}$**:

$P_{\text{ges}} = U \times I_{\text{ges}} = 5 \text{ V} \times 7.5 \text{ mA} = 37.5 \text{ mW}$

5. **Leistung an Widerstand $R_1$ und $R_2$**:

$P_{\text{R1}} = I1^2 \times R1 = (5 \text{ mA})^2 \times 1000~\Omega = 25 \text{ mW}$
$P_{\text{R2}} = I2^2 \times R2 = (2.5 \text{ mA})^2 \times 2000~\Omega = 12.5 \text{ mW}$

Zusammengefasst:

- $R_{\text{ges}} \approx 666.67~\Omega$
- $I_1 = 5 \text{ mA}$
- $I_2 = 2.5 \text{ mA}$
- $I_{\text{ges}} = 7.5 \text{ mA}$
- $P_{\text{ges}} = 37.5 \text{ mW}$
- $P_{\text{R1}} = 25 \text{ mW}$
- $P_{\text{R2}} = 12.5 \text{ mW}$

\newpage
**Aufgabe:**  
Eine Schaltung besteht aus einem Widerstand $R_1$ und einer Parallelschaltung von $R_2$, $R_3$ und $R_4$. Gegeben sind:

- Gesamtspannung $U = 9$ V
- Widerstand $R_1$ = 450 Ohm
- Widerstand $R_2$ = 1k = 1000 Ohm
- Widerstand $R_3$ = 2k = 2000 Ohm
- Widerstand $R_4$ = 3k = 3000 Ohm

$R_2$, $R_3$ und $R_4$ sind parallel zu $R_1$ geschaltet.

Gesucht:

1. Den Gesamtwiderstand $R_{\text{ges}}$ der Schaltung.
2. Den Gesamtstrom $I_{\text{ges}}$ der durch die Schaltung fließt.
3. Den Spannungsfall $U_1$ über $R_1$ und den Spannungsfall $U_2$ über die Parallelschaltung.
4. Die Ströme $I_1$, $I_2$, $I_3$ und $I_4$, die jeweils durch $R_1$, $R_2$, $R_3$ und $R_4$ fließen.

```
# Schaltplan: Stromteiler
U (+9V) 
   |
   +----[R1 450R]-----+---------+---------+
                      |         |         |
                   [R2 1k]   [R3 2k]   [R3 3k]     
                      |         |         |
   +------------------+---------+---------+
   |
  GND
```

**Lösung:**  

1. **Berechnung von $R_{\text{ges}}$**

Da $R_2$, $R_3$ und $R_4$ parallel geschaltet sind:

$\frac{1}{R_{\text{||}}} = \frac{1}{R_2} + \frac{1}{R_3} + \frac{1}{R_4} \to R_{\text{||}} = \frac{1}{\frac{1}{1000} + \frac{1}{2000} + \frac{1}{3000}} = 545.45~\Omega$ 

Da $R_1$ in Reihe zur Parallelschaltung liegt:

$R_{\text{ges}} = R_1 + R_{\text{||}} = 450~\Omega + 545.45~\Omega = 995.45~\Omega$ 

2. **Berechnung von $I_{\text{ges}}$**

Mit Ohmschem Gesetz: $I = \frac{U}{R} \to I_{\text{ges}} = \frac{9 \text{ V}}{995.45~\Omega} = 0.00903 \text{ A} = 9.03 \text{ mA}$ 

3. **Berechnung von $U_1$ und $U_2$**

$U_1 \text{ (an } R_1\text{)} = I_{\text{ges}} \times R_1 = 9.03 \text{ mA} \times 450~\Omega = 4.06 \text{ V}$ 

Da die Parallelschaltung den gleichen Spannungsfall hat wie $R_1$:

$U_2 \text{ (an Parallelschaltung)} = 9 \text{ V} - 4.06 \text{ V} = 4.94 \text{ V}$ 

4. **Berechnung der Ströme $I_1$, $I_2$, $I_3$ und $I_4$**

$I_1$ = $I_{\text{ges}}$ = 9.03 mA

$I_2$ = $\frac{U_2}{R_2}$ = $\frac{4.94 \text{ V}}{1000~\Omega}$ = 4.94 mA

$I_3$ = $\frac{U_2}{R_3}$ = $\frac{4.94 \text{ V}}{2000~\Omega}$ = 2.47 mA

$I_4$ = $\frac{U_2}{R_4}$ = $\frac{4.94 \text{ V}}{3000~\Omega}$ = 1.65 mA


\newpage
**Aufgabe:**  
Zwei Spannungsquellen $U_1$ und $U_2$ sind parallel geschaltet. An $U_1$ ist ein Widerstand $R_1$ in Reihe geschaltet. Zusätzlich sind die Widerstände $R_2$, $R_3$ und $R_4$ parallel zu $R_1$ und werden von $U_2$ gespeist. Die gegebenen Daten sind:

- $U_1 = 10$ V
- $U_2 = 9$ V
- $R_1 = 450$ Ohm
- $R_2 = 1k$ Ohm (1000 Ohm)
- $R_3 = 2k$ Ohm (2000 Ohm)
- $R_4 = 3k$ Ohm (3000 Ohm)

Berechne die Ströme $I_1$, $I_2$, $I_3$ und $I_4$, die jeweils durch $R_1$, $R_2$, $R_3$ und $R_4$ fließen.

```
# Schaltplan: Stromteiler
U1 (+10V)                                    U2 (+9V) 
   |                                            |
   +----[R1 450R]-----+---------+---------+-----+
                      |         |         |
                   [R2 1k]   [R3 2k]   [R3 3k]     
                      |         |         |
   +------------------+---------+---------+
   |
  GND
```

**Lösung:**  

Die Ströme durch die Widerstände $R_2$, $R_3$ und $R_4$ werden durch $U_2$ bestimmt, während der Strom durch $R_1$ von der Differenz zwischen $U_1$ und $U_2$ abhängt.

1. $I_2 = \frac{U2}{R2} = \frac{9 \text{ V}}{1000~\Omega} = 9 \text{ mA}$

2. $I_3 = \frac{U2}{R3} = \frac{9 \text{ V}}{2000~\Omega} = 4.5 \text{ mA}$

3. $I_4 = \frac{U2}{R4} = \frac{9 \text{ V}}{3000~\Omega} = 3 \text{ mA}$

4. $I_1 = \frac{U1 - U2}{R1}  = \frac{10 \text{ V} - 9 \text{ V}}{450~\Omega} = 2.22 \text{ mA}$

Zusammenfassung:

- $I_1 = 2.22 \text{ mA}$
- $I_2 = 9 \text{ mA}$
- $I_3 = 4.5 \text{ mA}$
- $I_4 = 3 \text{ mA}$

### Pull-up und Pull-down

```
# Schaltplan: Taster + Widerstand + LED + Pull-down Widerstand
+Uin o-+--------------------
       |
       o
   [Taster]
       o---[R2 10k]--+
       |             |
   [R1 3k9]          |
       |             |
     [LED]           |
       |             |
 GND o-+-------------+------
```

## Kondensator

```
# Schaltplan: Taster1 + Kondensator + Taster2 + Widerstand + LED
+Uin o-+--------------------------
       |
       o
   [Taster1]
       o-------[C1 100uF]--+
   [Taster2]               |
       o                   |
       |                   |
   [R1 3k9]                |
       |                   |
     [LED]                 |
       |                   |
 GND o-+-------------------+------
```

\newpage
### Kondensatoren Parallel

**Aufgabe:**
Gegeben sind drei Kondensatoren, die parallel geschaltet sind. Die Spannung U über den Kondensatoren beträgt 5 V. Die Kapazitäten der Kondensatoren sind wie folgt gegeben:

- $C_1 = 470~\mu \text{F}$
- $C_2 = 220~\mu \text{F}$
- $C_3 = 40~\mu \text{F}$

Berechne:

a) Die Gesamtkapazität $C_{\text{ges}}$ der parallelen Schaltung
b) Die Gesamtladung $Q_{\text{ges}}$ in der Schaltung
c) Die Ladungen $Q_1, Q_2,$ und $Q_3$ der einzelnen Kondensatoren
d) Die gespeicherte Energie $W$ in der Schaltung

Energie: $W = \frac{C_{\text{ges}} \times U^2}{2}$

```
# Schaltplan: Kondensatoren parallel
 +U o-+----+----+--------
      |    |    |
     [C1] [C2] [C3]
      |    |    |
GND o-+----+----+--------
```

**Lösung:**

a) Für parallel geschaltete Kondensatoren gilt:

- $C_{\text{ges}} = C_1 + C_2 + C_3 = 470~\mu \text{F} + 220~\mu \text{F} + 40~\mu \text{F} = 730~\mu \text{F}$

b) Die Gesamtladung auf einem Kondensator ist:

- $Q_{\text{ges}} = C_{\text{ges}} \times U = 730~\mu \text{F} \times 5 V = 3650~\mu \text{C}$

c) Die Ladungen der einzelnen Kondensatoren sind:

- $Q_1 = C_1 \times U = 470~\mu \text{F} \times 5 V = 2350~\mu \text{C}$
- $Q_2 = C_2 \times U = 220~\mu \text{F} \times 5 V = 1100~\mu \text{C}$
- $Q_3 = C_3 \times U = 40~\mu \text{F} \times 5 V = 200~\mu \text{C}$

d) Mit der gegebenen Formel ergibt sich die Energie:

- $W = \frac{730~\mu \text{F} \times (5 V)^2}{2} = 9125~\mu \text{J} = 9.125 mJ$

Die Kondensatoren sind parallel geschaltet, daher haben alle Kondensatoren die gleiche Spannung von 5 V.




\newpage
### Kondensatoren in Reihe

**Aufgabe:**

Drei Kondensatoren sind in Reihe geschaltet. Gegeben sind ihre Kapazitäten:

- $C_1 = 470~\mu \text{F}$
- $C_2 = 220~\mu \text{F}$
- $C_3 = 40~\mu \text{F}$

Die Spannung über die gesamte Schaltung beträgt $U = 5 V$.

Berechnen Sie:

1. Die Gesamtkapazität $C_{\text{ges}}$ der in Reihe geschalteten Kondensatoren.
2. Die gespeicherte Ladung $Q$ in der Schaltung.
3. Die gespeicherte Energie $W$ in der Schaltung.


```
# Schaltplan: Kondensatoren in Reihe
 +U o-+-------------------
      |     
     [C1]    
      |     
     [C2]    
      |
     [C3]
      |      
GND o-+-------------------
```

**Berechnung:**

1. Gesamtkapazität $C_{\text{ges}}$ bei in Reihe geschalteten Kondensatoren:

- $\frac{1}{C_{\text{ges}}} = \frac{1}{C_1} + \frac{1}{C_2} + \frac{1}{C_3}$

2. Die Ladung $Q$ eines Kondensators berechnet sich als:

- $Q = C_{\text{ges}} \times U$

3. Die gespeicherte Energie $W$ in einem Kondensator ist:

- $W = \frac{1}{2} \times C_{\text{ges}} \times U^2$

**Lösung:**

1. Gesamtkapazität: $\frac{1}{C_{\text{ges}}} = \frac{1}{470} + \frac{1}{220} + \frac{1}{40} \approx 0.0316731141$
$C_{\text{ges}} \approx 31.56~\mu \text{F}$

2. Ladung: $Q = 31.56~\mu \text{F} \times 5 V  \approx 157.8~\mu \text{C}$

3. Energie: $W = \frac{1}{2} \times 31.56~\mu \text{F} \times (5 V)^2 \approx 394.5~\mu \text{J}$

Zusammenfassend:

- $C_{\text{ges}} \approx 31.56~\mu \text{F}$
- $Q \approx 157.8~\mu \text{C}$
- $W \approx 394.5~\mu \text{J}$

\newpage
### RC-Glied

**Aufgabe:**
**Ein RC-Glied (Widerstand-Kondensator-Schaltung) mit einer Spannung von $U = 5 V$ ist gegeben.** 

*Beim Aufladen*: Ein Schalter wird geschlossen. Ein Widerstand $R_1 = 1~\text{k} \Omega$ und ein Kondensator $C_1 = 470~\mu \text{F}$ sind in Reihe geschaltet, während ein weiterer Widerstand $R_2$ parallel dazu liegt.

*Beim Entladen*: Der Schalter wird geöffnet, sodass $R_2 = 10~\text{k} \Omega$, $R_1 = 1~\text{k} \Omega$ und $C_1 = 470~\mu \text{F}$ in Reihe liegen.

**Bestimmen Sie die Zeitkonstante** ($\tau$):

1. Beim Aufladen.
2. Beim Entladen.

**Berechnen Sie dann die benötigte Zeit sowohl beim Aufladen als auch beim Entladen:**

a) Erreichen von 63,2% der Spannung $U$
b) Erreichen von 86,5% der Spannung $U$
c) Erreichen von 95% der Spannung $U$

```
# Schaltplan: Taster + R1 + Kondensator + R2
+Uin o-+--------------------------
       |
       o
   [Taster1]
       o-------------------+
       |                   |
   [R2 10k]             [R1 1k]
       |                   |
       |               [C1 100uF]
       |                   |
 GND o-+-------------------+------
```

**Lösung:**

1. Zeitkonstante ($\tau$):
Die Zeitkonstante einer RC-Schaltung ist definiert als $\tau = R \times C$.

Beim *Aufladen*: Da $R_2$ parallel zu $R_1$ und $C_1$ liegt und keinen Einfluss auf den Aufladevorgang hat (der Strom fließt durch den Pfad mit dem geringsten Widerstand), beträgt der effektive Widerstand $R = R_1$:

- $\tau_{\text{aufladen}} = R_1 \times C_1 = 1~\text{k} \Omega \times 470~\mu \text{F} = 470 ms$

Beim *Entladen*: Hier sind $R_1$ und $R_2$ in Reihe:

- $\tau_{\text{entladen}} = (R_1 + R_2) \times C_1 = 11~\text{k} \Omega \times 470~\mu \text{F} = 5.17 s$

2. Zeit zum Erreichen eines bestimmten Prozentsatzes der Spannung:
Die Spannung an einem Kondensator während des Ladevorgangs kann mit der folgenden Formel beschrieben werden:

- Ladevorgang: $U(t) = U_{\text{max}}(1 - e^{-t/\tau})$ 
- Entladevorgang: $U(t) = U_{\text{max}} e^{-t/\tau}$

a) 63,2\% von $U$ entspricht einer Zeit von $\tau$:

- Aufladen: $t = \tau_{\text{aufladen}} = 470 ms$
- Entladen: $t = \tau_{\text{entladen}} = 5.17 s$

b) Für 86,5\% von $U$ setzen wir $U(t) = 0.865 \times U_{\text{max}}$ in die Ladeformel ein und lösen nach $t$ auf. Dies entspricht in etwa $2\tau$.

- Aufladen: $t \approx 2 \times 470 ms = 940 ms$
- Entladen: $t \approx 2 \times 5.17 s = 10.34 s$

c) Für 95\% von $U$ setzen wir $U(t) = 0.95 \times U_{\text{max}}$ in die Ladeformel ein und lösen nach $t$ auf. Dies entspricht in etwa $3\tau$.

- Aufladen: $t \approx 3 \times 470 ms = 1.41 s$
- Entladen: $t \approx 3 \times 5.17 s = 15.51 s$

**Zusammenfassung:**

Beim Aufladen:

- a) 470 ms
- b) 940 ms
- c) 1.41 s

Beim Entladen:

- a) 5.17 s
- b) 10.34 s
- c) 15.51 s

