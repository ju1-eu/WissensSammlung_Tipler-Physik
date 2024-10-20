---
title: "Mathe-Formelsammlung-Elektrik"
author: "Jan Unger"
date: "2024-10-19"
---

# Mathe Formelsammlung

Letzte Aktualisierung: 2024-10-19

- [Mathe Formelsammlung](#mathe-formelsammlung)
  - [Größenordnungen und Einheiten](#größenordnungen-und-einheiten)
  - [Elektrotechnik](#elektrotechnik)

## Größenordnungen und Einheiten

**Eingabe Rechner**

z. B. $20~\text{mV} = 20 \times 10^{-3}~\text{V} \quad \curvearrowright$ Rechner: $20 \text{ EE} -3 = 0{,}02$

$10^3 = 1.000 = 1 \times 10^3$

$10^{-3} = \frac{1}{1.000} = 0{,}001 = 1 \times 10^{-3}$

$10^6 = 1.000.000 = 1 \times 10^6$

$10^{-6} = \frac{1}{1.000.000} = 0{,}000001 = 1 \times 10^{-6}$

$\boxed{K \times m = 1 \quad 10^3 \times 10^{-3} = 1 \quad 1.000 \times \frac{1}{1.000} = 1}$

**Größenpräfixe**

$\boxed{K = 10^3 \quad M = 10^6 \quad G = 10^9 \quad T = 10^{12}}$

$\boxed{m = 10^{-3} \quad \mu = 10^{-6} \quad n = 10^{-9} \quad p = 10^{-12}}$

**Einheiten** 

Faktor: Länge 10, Fläche 100, Volumen 1000

$\boxed{\mu\text{m} \quad \text{mm} \quad \text{cm} \quad \text{dm} \quad \text{m} \quad \text{km}}$

$1~\text{l} = 1~\text{dm}^3 \quad 10~\text{ml} = 1~\text{cl} = 0{,}01~\text{l}$

$\frac{\text{g}}{\text{cm}^3} \quad \frac{\text{kg}}{\text{dm}^3} \quad \frac{\text{t}}{\text{m}^3}$

**Prozent** $10~\% = \frac{10}{100} = 0{,}1$

**km/h in m/s** $\Rightarrow \frac{\text{km/h}}{3{,}6} \quad \frac{\text{km}}{\text{h}} \Rightarrow \frac{\text{m}}{\text{s}} \Rightarrow \frac{1000}{3600}$ 

**Stunden:Min:Sek in Dezimalstunden** $\Rightarrow \text{h} + \frac{\text{Min}}{60} + \frac{\text{Sek}}{60 \cdot 60}$ 

**Zoll in mm** $1~\text{Zoll} = 25{,}4~\text{mm}$

**Kreisfläche** $\boxed{A = \frac{d^2 \cdot \pi}{4}} \quad \text{Hinweis: }\frac{\pi}{4} \approx 0{,}785$

**Masse** $\boxed{m = V \cdot \rho}$ Dichte bleibt immer gleich $\to$ Volumen ändert sich

**Volumen** $\boxed{V = A \cdot h}$

**Umfang** $\boxed{U = d \cdot \pi}$

**Drehmoment** $\boxed{\mathbf{M} = \mathbf{F} \times \mathbf{r}}$

Dabei gilt: $\mathbf{M}~[\text{N} \cdot \text{m}] = \mathbf{F}~[\text{N}] \times \mathbf{r}~[\text{m}]$

$\mathbf{M}$: Drehmomentvektor $[\text{N} \cdot \text{m}]$
$\mathbf{F}$: Kraftvektor $[\text{N}]$
$\mathbf{r}$: Ortsvektor (Hebelarm) $[\text{m}]$

**Kraft** $\boxed{\mathbf{F} = m \cdot \mathbf{a}}$

Dabei gilt: $\mathbf{F}~[\text{N}] = m~[\text{kg}] \cdot \mathbf{a}~[\text{m/s}^2]$

$\mathbf{F}$: Kraftvektor in Newton $[\text{N}]$
$m$: Masse (Skalar) in Kilogramm $[\text{kg}]$
$\mathbf{a}$: Beschleunigungsvektor in Meter pro Sekunde zum Quadrat $[\text{m/s}^2]$

## Elektrotechnik
 
**SPANNUNG** $U~\text{Volt}~[\text{V}]$

**STROM** $I~\text{Ampere}~[\text{A}]$

**WIDERSTAND** $R~\text{Ohm}~[\Omega]$

**Reihe**

1. Strombegrenzung
2. Spannungsteilung

**Parallel**

1. Stromflusserhöhung
2. Leistungsteilung $\boxed{R_{\text{ges}} = \frac{R_{\text{Teil}}}{n}}$

**OHMSCHES GESETZ**

$\boxed{I = \frac{U}{R}} \quad \bigl[\frac{\text{V}}{\Omega}\bigr] = \text{A} \quad
 \boxed{R = \frac{U}{I}} \quad \bigl[\frac{\text{V}}{\text{A}}\bigr] = \Omega \quad
 \boxed{U = R \cdot I} \quad [\Omega \cdot \text{A}] = \text{V}$

**STROMDICHTE**

$\boxed{J = \frac{I}{A}} \quad \bigl[\frac{\text{A}}{\text{mm}^2}\bigr] \quad
 \boxed{I = J \cdot A} \quad \bigl[\frac{\text{A} \cdot \text{mm}^2}{\text{mm}^2}\bigr] = \text{A} \quad
 \boxed{A = \frac{I}{J}} \quad \bigl[\frac{\text{A} \cdot \text{mm}^2}{\text{A}}\bigr] = \text{mm}^2$

**LEITWERT** $G$ Siemens $[\text{S}]$

$\boxed{G = \frac{1}{R}} \quad \bigl[\frac{1}{\Omega}\bigr] = \text{S} \quad \boxed{R = \frac{1}{G}} \quad \bigl[\frac{1}{\text{S}}\bigr] = \Omega$

**LEITERWIDERSTAND** 

$\boxed{R_\text{l} = \frac{\rho \cdot l}{A}} \quad  \bigl[\frac{\Omega \cdot \text{mm}^2 \cdot \text{m}}{\text{m} \cdot \text{mm}^2}\bigr] = \Omega \quad 
\boxed{A = \frac{\rho \cdot l}{R_\text{l}}} \quad  \bigl[\frac{\Omega \cdot \text{mm}^2 \cdot \text{m}}{\text{m} \cdot \Omega}\bigr] = \text{mm}^2$

$\boxed{l = \frac{R_\text{l} \cdot A}{\rho}} \quad  \bigl[\frac{\Omega \cdot \text{mm}^2 \cdot \text{m}}{\Omega \cdot \text{mm}^2}\bigr] = \text{m}$

**SPEZIFISCHER WIDERSTAND** $\rho$ (rho)

$\rho \quad \bigl[\frac{\Omega \cdot \text{mm}^2}{\text{m}}\bigr] \quad \rho_{\text{Cu}} = 0{,}0178~\frac{\Omega \cdot \text{mm}^2}{\text{m}}$

**ELEKTRISCHE LEITFÄHIGKEIT** $\kappa$ (Kappa)

$\boxed{\kappa = \frac{1}{\rho}} \quad \bigl[\frac{\text{m}}{\Omega \cdot \text{mm}^2}\bigr] \quad \kappa_{\text{Cu}} = 56~\frac{\text{m}}{\Omega \cdot \text{mm}^2}$

**REIHENSCHALTUNG**

$\boxed{U_{\text{ges}} = U_{R_1} + U_{R_2} + U_{R_3} + \dots + U_{R_n}} \quad [\text{V} + \text{V} + \text{V}] = \text{V}$ 

$\boxed{U_{\text{teil}} = \frac{U_{\text{ges}}}{n}} \quad \bigl[\frac{\text{V}}{1}\bigr] = \text{V}$

$\boxed{I_{\text{ges}} = I_{R_1} = I_{R_2} = I_{R_3} = \dots = I_{R_n}} \quad [\text{A} = \text{A} = \text{A}] = \text{A}$ 

$\boxed{R_{\text{ges}} = R_1 + R_2 + R_3 + \dots + R_n} \quad [\Omega + \Omega + \Omega] = \Omega$ 

**SPANNUNGSVERLUST** (Spannungsfall)

$U_{\text{ges}} = U_\text{v} + U_\text{k};\quad U_\text{k} = U_{\text{ges}} - U_\text{v};\quad U_\text{v} = U_{\text{ges}} - U_\text{k}$

$U_\text{v} = R_\text{l} \cdot I;\quad R_\text{l} = \frac{\rho \cdot l}{A} \quad \bigl[\frac{\Omega \cdot \text{mm}^2 \cdot \text{m}}{\text{m} \cdot \text{mm}^2}\bigr] = \Omega$

$U_\text{k} = U_{\text{ges}} - R_\text{l} \cdot I$

$\boxed{U_\text{v} = \frac{\rho \cdot l \cdot I}{A}} \quad \bigl[\frac{\Omega \cdot \text{mm}^2 \cdot \text{m} \cdot \text{A}}{\text{m} \cdot \text{mm}^2}\bigr] = \text{V} \quad \rho_{\text{Cu}} = 0{,}0178~\frac{\Omega \cdot \text{mm}^2}{\text{m}}$

$U_{v_{~\%}} = \frac{U_\text{v} \cdot 100}{U_{\text{ges}}} \quad \bigl[\frac{\text{V} \cdot ~\%}{\text{V}}\bigr] = ~\%$

$\boxed{U_{v_{\text{max}}} = 0{,}5~\text{V}}$

$\boxed{\text{max. Leiterwiderstand} = 1~\Omega}$ (außer Starterhauptleitung)

**INNENWIDERSTAND** (von Spannungsquellen)

$U_\text{q} = U_\text{k} + U_\text{i} \quad [\text{V} + \text{V}] = \text{V}$

$U_\text{k} = U_\text{q} - U_\text{i} \quad [\text{V} - \text{V}] = \text{V}$

$U_\text{i} = U_\text{q} - U_\text{k} \quad [\text{V} - \text{V}] = \text{V}$

$U_\text{i} = I \cdot R_\text{i} \quad [\text{A} \cdot \Omega] = \text{V}$

$U_\text{k} = I \cdot R_a \quad [\text{A} \cdot \Omega] = \text{V}$

$I = \frac{U_\text{i}}{R_\text{i}} \quad \bigl[\frac{\text{V}}{\Omega}\bigr] = \text{A}$

$I = \frac{U_\text{k}}{R_a} \quad \bigl[\frac{\text{V}}{\Omega}\bigr] = \text{A}$

$I = \frac{U_\text{q}}{R_{\text{ges}}} \quad \bigl[\frac{\text{V}}{\Omega}\bigr] = \text{A}$

$I = \frac{U_\text{q}}{R_\text{i} + R_a} \quad \bigl[\frac{\text{V}}{\Omega + \Omega}\bigr] = \text{A}$

$\boxed{U_\text{k} = U_\text{q} - I \cdot R_\text{i}} \quad [\text{V} - \text{A} \cdot \Omega \to \text{V} - \text{V}] = \text{V}$

$\boxed{R_\text{i} = \frac{U_\text{i}}{I}} \quad \bigl[\frac{\text{V}}{\text{A}}\bigr] = \Omega$

$\boxed{U_\text{k} = U_\text{q} - U_\text{i} - U_\text{v}} \quad \boxed{R_{\text{ges}} = R_\text{i} + R_\text{l} + R_{\text{ü}} + R_{\text{La}}}$

*Herleitung*

$U_\text{k} = U_\text{q} - I \cdot R_\text{i}$  $\quad | +I \cdot R_\text{i}$

$U_\text{k} + I \cdot R_\text{i} = U_\text{q} - I \cdot R_\text{i} + I \cdot R_\text{i}$ $\quad |  -U_\text{k}$

$-U_\text{k} + U_\text{k} + I \cdot R_\text{i} = U_\text{q} - U_\text{k}$  $\quad | :I$

$\frac{I \cdot R_\text{i}}{I} = \frac{U_\text{q} - U_\text{k}}{I}$ $\quad \bigl[\frac{\text{V} - \text{V}}{\text{A}} \to \frac{\text{V}}{\text{A}}\bigr] = \Omega$

$R_\text{i} = \frac{U_\text{i}}{I}$

**PARALLELSCHALTUNG**

$\boxed{I_{\text{ges}} = I_{R_1} + I_{R_2} + I_{R_3} + \dots + I_{R_n}}\quad [\text{A} + \text{A} + \text{A}] = \text{A}$

$\boxed{U_{\text{ges}} = U_{R_1} = U_{R_2} = U_{R_3} = \dots = U_{R_n}}\quad [\text{V} = \text{V} = \text{V}] = \text{V}$

$\boxed{R_{\text{ges}} = \frac{1}{\frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3} + \dots + \frac{1}{R_n}}} \quad \bigl[\frac{1}{\frac{1}{\Omega} + \frac{1}{\Omega} + \frac{1}{\Omega}} = \frac{1}{\frac{1}{\Omega}} = \frac{1}{\text{S}}\bigr] = \Omega$

Ersatzwiderstand $\boxed{R_{\text{ges}} = \frac{R_{\text{Teil}}}{n}} \quad \bigl[\frac{\Omega}{1}\bigr] = \Omega \quad \to \text{Anzahl } n = \frac{R_{\text{Teil}}}{R_{\text{ges}}} \quad \bigl[\frac{\Omega}{\Omega}\bigr] = 1$ 

n = Anzahl der Widerstände (gleich große Widerstände)

$\boxed{R_{\text{ges}} = \frac{R_1 \cdot R_2}{R_1 + R_2}}$

$R_{\text{ges}} = \frac{1}{\frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3}}$

$\to R_{1} = \frac{1}{\frac{1}{R_{\text{ges}}} - \frac{1}{R_2} - \frac{1}{R_3}} \quad \to R_{2} \to R_{2} = \frac{1}{\frac{1}{R_{\text{ges}}} - \frac{1}{R_1} - \frac{1}{R_3}} \quad \to R_{3} = \frac{1}{\frac{1}{R_{\text{ges}}} - \frac{1}{R_1} - \frac{1}{R_2}}$

**LEISTUNG** $P$ (Power) Watt, $[\text{W}], [\text{kW}]$

$\boxed{P = U \cdot I} \quad [\text{V} \cdot \text{A}] = \text{W}$

$\boxed{U = \frac{P}{I}} \quad \bigl[\frac{\text{W}}{\text{A}} \to \frac{\text{V} \cdot \text{A}}{\text{A}}\bigr] = \text{V}$

$\boxed{I = \frac{P}{U}} \quad \bigl[\frac{\text{W}}{\text{V}} \to \frac{\text{V} \cdot \text{A}}{\text{V}}\bigr] = \text{A}$

**wenn $I$ fehlt** (Einsetzverfahren)

$P = U \cdot I \quad [\text{V} \cdot \text{A}] = \text{W}, \quad I = \frac{U}{R} \quad \bigl[\frac{\text{V}}{\Omega}\bigr] = \text{A}$

$P = U \cdot \frac{U}{R} \to \boxed{P = \frac{U^2}{R}} \quad \bigl[\frac{\text{V} \cdot \text{V}}{\Omega} \to \text{A} \cdot \text{V}\bigr] = \text{W}$

**wenn $U$ fehlt** (Einsetzverfahren)

$P = U \cdot I \quad [\text{V} \cdot \text{A}] = \text{W}, \quad U = R \cdot I \quad [\Omega \cdot \text{A}] = \text{V}$

$P = R \cdot I \cdot I \to \boxed{P = R \cdot I^2} \quad [\Omega \cdot \text{A} \cdot \text{A} \to \text{V} \cdot \text{A}] = \text{W}$

**Lampe** $12~\text{V}/55~\text{W}$ 

1. $R_{\text{La}} = \frac{U^2}{P}$
2. $I_{\text{tat}} = \frac{U_\text{k}}{R_{\text{La}}} = \frac{U_{\text{ges}} - U_\text{v}}{R_{\text{La}}}$
3. $P_{\text{tat}} = U_\text{k} \cdot I_{\text{tat}}$
