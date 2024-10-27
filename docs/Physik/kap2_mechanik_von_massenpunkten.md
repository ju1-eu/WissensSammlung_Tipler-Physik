---
title: "Mechanik von Massenpunkten"
author: "Jan Unger"
date: "2024-10-19"
---

# Mechanik von Massenpunkten - Zusammenfassung

Letzte Aktualisierung: 2024-10-27

Quelle: P. A. Tipler und G. Mosca, *Tipler Physik für Studierende der Naturwissenschaften und Technik*, 9., vollständig überarbeitete und ergänzte Auflage, P. Kersten, Hrsg. Heidelberg, Deutschland: Springer Spektrum, 2024. Verfügbar: https://doi.org/10.1007/978-3-662-67936-4

**Lernziel**: In diesem Kapitel wollen wir uns mit der Kinematik
einfacher Bewegungen beschäftigen. In diesem Zusammenhang
werden wir die exakten Definitionen von Begriffen
wie Verschiebung, Geschwindigkeit, Geschwindigkeitsbetrag
und Beschleunigung einführen, die umgangssprachlich
zur Beschreibung von Bewegungen herangezogen
werden. Insbesondere werden wir den wichtigen
Spezialfall der gleichförmig beschleunigten Bewegung
betrachten und als Anwendungen den schrägen Wurf und
die Kreisbewegung näher untersuchen.

- [Mechanik von Massenpunkten - Zusammenfassung](#mechanik-von-massenpunkten---zusammenfassung)
  - [Grundlagen der Bewegungsbeschreibung](#grundlagen-der-bewegungsbeschreibung)
    - [Verschiebung](#verschiebung)
  - [Geschwindigkeiten](#geschwindigkeiten)
    - [Momentangeschwindigkeit](#momentangeschwindigkeit)
    - [Mittlere Geschwindigkeit](#mittlere-geschwindigkeit)
  - [Beschleunigung](#beschleunigung)
    - [Momentanbeschleunigung](#momentanbeschleunigung)
    - [Mittlere Beschleunigung](#mittlere-beschleunigung)
  - [Spezielle Bewegungsformen](#spezielle-bewegungsformen)
    - [Gleichförmig beschleunigte Bewegung](#gleichförmig-beschleunigte-bewegung)
    - [Schräger Wurf](#schräger-wurf)
    - [Kreisbewegung](#kreisbewegung)
    - [Krummlinige Bewegung](#krummlinige-bewegung)
- [Erklärung der Fachbegriffe - Orts- und Verschiebungsvektoren](#erklärung-der-fachbegriffe---orts--und-verschiebungsvektoren)
  - [Vektoren und Notation](#vektoren-und-notation)
  - [Mathematische Notation](#mathematische-notation)
  - [Wichtige Konzepte](#wichtige-konzepte)

## Grundlagen der Bewegungsbeschreibung

### Verschiebung

Die eindimensionale Verschiebung eines Massenpunktes wird durch die Differenz der Positionen definiert:
$$\Delta x = x_2 - x_1$$

Der Ortsvektor $$\mathbf{r}$$ beschreibt die Position des Teilchens relativ zum Ursprung des Koordinatensystems. Der Verschiebungsvektor ergibt sich aus:
$$\Delta \mathbf{r} = \mathbf{r}_2 - \mathbf{r}_1 = \Delta x~\hat{\mathbf{x}} + \Delta y~\hat{\mathbf{y}}$$

## Geschwindigkeiten

### Momentangeschwindigkeit

Die Momentangeschwindigkeit beschreibt die augenblickliche Bewegungsrate und ist definiert als:
$$v_x(t) = \lim_{\Delta t \to 0} \frac{\Delta x}{\Delta t} = \frac{\text{d}x}{\text{d}t} = \dot{x}(t)$$

### Mittlere Geschwindigkeit

Die mittlere Geschwindigkeit über ein Zeitintervall berechnet sich durch:
$$\langle v_x \rangle = \frac{\Delta x}{\Delta t} = \frac{1}{\Delta t} \int_{t_1}^{t_2} v_x~\text{d}t$$

Der Geschwindigkeitsvektor $$\mathbf{v}$$ zeigt in Bewegungsrichtung und sein Betrag entspricht der Geschwindigkeit:
$$\mathbf{v}(t) = \lim_{\Delta t \to 0} \frac{\Delta \mathbf{r}}{\Delta t} = \frac{\text{d}\mathbf{r}}{\text{d}t} = \dot{\mathbf{r}}(t)$$

## Beschleunigung

### Momentanbeschleunigung

Die Momentanbeschleunigung ist die zeitliche Änderung der Geschwindigkeit:
$$a_x(t) = \frac{\text{d}v_x}{\text{d}t} = \frac{\text{d}^2x}{\text{d}t^2} = \ddot{x}(t)$$

### Mittlere Beschleunigung

$$\langle a_x \rangle = \frac{\Delta v_x}{\Delta t}$$

Der Beschleunigungsvektor ist gegeben durch:
$$\mathbf{a}(t) = \lim_{\Delta t \to 0} \frac{\Delta \mathbf{v}}{\Delta t} = \frac{\text{d}\mathbf{v}}{\text{d}t} = \dot{\mathbf{v}}(t) = \ddot{\mathbf{r}}(t)$$

## Spezielle Bewegungsformen

### Gleichförmig beschleunigte Bewegung

Für eine eindimensionale gleichförmig beschleunigte Bewegung gelten:

- Geschwindigkeit: $$v_x = v_{0,x} + a_x t$$
- Verschiebung: $$\Delta x = v_{0,x}t + \frac{1}{2}a_x t^2$$
- Geschwindigkeits-Weg-Beziehung: $$v_x^2 = v_{0,x}^2 + 2a_x \Delta x$$

### Schräger Wurf

Beim schrägen Wurf ohne Luftwiderstand gilt:

- Horizontale Bewegung: $$a_x = 0$$
- Vertikale Bewegung: $$a_y = -g$$
- Bewegungsgleichungen:
  $$x(t) = x_0 + v_{0,x}t$$
  $$y(t) = y_0 + v_{0,y}t - \frac{1}{2}gt^2$$
- Anfangsgeschwindigkeiten:
  $$v_{x,0} = |\mathbf{v}_0| \cos \theta_0$$
  $$v_{y,0} = |\mathbf{v}_0| \sin \theta_0$$

### Kreisbewegung

Bei der gleichförmigen Kreisbewegung tritt die Zentripetalbeschleunigung auf:
$$a_\text{ZP} = -\frac{v^2}{r}\hat{\mathbf{r}}$$

Die Periode der Kreisbewegung beträgt:
$$T = \frac{2\pi r}{v}$$

### Krummlinige Bewegung

Bei krummlinigen Bewegungen unterscheidet man:

- Tangentialbeschleunigung: $$a_\text{t} = \frac{v^2}{r}\hat{\mathbf{t}}$$
- Normalbeschleunigung: $$a_\text{n} = \frac{\text{d}v}{\text{d}t}\hat{\mathbf{n}}$$

wobei $$\hat{\mathbf{t}}$$ der Einheitsvektor der Tangente und $$\hat{\mathbf{n}}$$ der Einheitsvektor zum Krümmungsmittelpunkt ist.

# Erklärung der Fachbegriffe - Orts- und Verschiebungsvektoren

## Vektoren und Notation

1. **Ortsvektor** $$\vec{r}$$
   - Beschreibt die Position eines Punktes relativ zum Koordinatenursprung
   - Besteht aus Betrag (Länge) und Richtung
   - Notation: Pfeil über dem Symbol $$\vec{r}$$ kennzeichnet einen Vektor

2. **Verschiebungsvektor** $$\Delta\vec{r}$$
   - Beschreibt die Änderung der Position zwischen zwei Punkten
   - $$\Delta$$ (Delta) steht für die Differenz/Änderung
   - Berechnung: $$\Delta\vec{r} = \vec{r}_\text{Ende} - \vec{r}_\text{Start}$$

3. **Einheitsvektoren** $$\hat{x}$$ und $$\hat{y}$$
   - Vektoren der Länge 1 in Koordinatenrichtungen
   - Dach-Symbol (^) kennzeichnet Einheitsvektoren
   - Dienen zur Zerlegung von Vektoren in Komponenten

## Mathematische Notation

1. **Vektorkomponenten**
   - $$x$$-Komponente: horizontale Richtung
   - $$y$$-Komponente: vertikale Richtung
   - Beispiel: $$\vec{r} = x\hat{x} + y\hat{y}$$

2. **Betrag eines Vektors** $$|\vec{r}|$$
   - Länge des Vektors
   - Berechnung: $$|\vec{r}| = \sqrt{x^2 + y^2}$$

3. **Winkel** $$\theta$$ (Theta)
   - Griechischer Buchstabe für Winkelangaben
   - Gemessen gegen die positive $$x$$-Achse
   - Einheit: Grad ($$^\circ$$)

## Wichtige Konzepte

1. **Koordinatensystem**
   - Rechtshändiges kartesisches System
   - $$x$$-Achse: horizontal (Ost-West)
   - $$y$$-Achse: vertikal (Nord-Süd)
   - Ursprung: Bezugspunkt (0,0)

2. **Trigonometrische Funktionen**
   - $$\sin\theta$$: Verhältnis Gegenkathete zu Hypotenuse
   - $$\cos\theta$$: Verhältnis Ankathete zu Hypotenuse
   - $$\tan\theta$$: Verhältnis Gegenkathete zu Ankathete
   - $$\arctan$$: Umkehrfunktion des Tangens

3. **Vektorzerlegung**
   - Aufspaltung eines Vektors in Komponenten
   - $$x$$-Komponente: $$|\vec{r}|\cos\theta$$
   - $$y$$-Komponente: $$|\vec{r}|\sin\theta$$

Diese Konzepte bilden die Grundlage für die Beschreibung und Berechnung von Bewegungen in der Mechanik.