"""
Verbessertes Kraft- und Drehmoment-Visualisierungsskript

Dieses Skript visualisiert die Beziehung zwischen Kraft und Drehmoment in einem
dreidimensionalen Raum mit verbesserter Lesbarkeit und Genauigkeit.

Funktionen:
- Präzise Berechnung und Visualisierung von Kraft und Drehmoment
- Interaktive Anpassung der Parameter mit Slidern
- Verbesserte Fehlerbehandlung und Eingabevalidierung
- Konsistente Einheitenverwendung und -anzeige
- Dynamische, gut lesbare erklärende Textfelder
- Option zur Darstellung von Vektoren als Pfeile oder Linien
- Speichern der Visualisierung als PNG und SVG

Autor: [Ihr Name]
Datum: [Aktuelles Datum]
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.widgets import Slider, Button, RadioButtons
from matplotlib.patches import FancyBboxPatch

# Konstanten und Einheiten
MASS_UNIT = "kg"
ACCELERATION_UNIT = "m/s²"
FORCE_UNIT = "N"
LENGTH_UNIT = "m"
TORQUE_UNIT = "N·m"

def calculate_vectors(m, a, r):
    """
    Berechnet Kraft- und Drehmoment-Vektoren mit erhöhter Präzision.
    """
    if m <= 0:
        raise ValueError("Masse muss positiv sein")
    if not all(isinstance(x, (int, float)) for x in a) or not all(isinstance(x, (int, float)) for x in r):
        raise ValueError("Beschleunigungs- und Ortsvektoren müssen numerische Werte enthalten")
    
    F = m * a
    M = np.cross(r, F)
    return F, M

def plot_vector(ax, vector, origin=[0, 0, 0], color='b', label='', arrow_length_ratio=0.1, as_arrow=True):
    if as_arrow:
        ax.quiver(origin[0], origin[1], origin[2], vector[0], vector[1], vector[2], 
                  color=color, arrow_length_ratio=arrow_length_ratio)
    else:
        ax.plot([origin[0], origin[0]+vector[0]], 
                [origin[1], origin[1]+vector[1]], 
                [origin[2], origin[2]+vector[2]], 
                color=color)
    
    text_pos = origin + vector + 0.3 * vector / np.linalg.norm(vector)
    ax.text(text_pos[0], text_pos[1], text_pos[2], 
            f'{label}: ({vector[0]:.2f}, {vector[1]:.2f}, {vector[2]:.2f})', 
            color=color, fontsize=10)

def create_textbox(fig, x, y, width, height, text):
    box = FancyBboxPatch((x, y), width, height, boxstyle="round,pad=0.1", 
                         fc="white", ec="gray", alpha=0.9)
    fig.patches.append(box)
    fig.text(x+0.01, y+height-0.02, text, fontsize=10, va="top", ha="left")

def update(val):
    global text_boxes
    ax.clear()
    m = mass_slider.val
    a = np.array([ax_slider.val, ay_slider.val, az_slider.val])
    r = np.array([rx_slider.val, ry_slider.val, rz_slider.val])
    
    try:
        F, M = calculate_vectors(m, a, r)
    except ValueError as e:
        print(f"Fehler: {e}")
        return
    
    M_scale = 0.3
    M_scaled = M * M_scale

    as_arrow = vector_style_radio.value_selected == "Pfeile"
    plot_vector(ax, a, color='y', label='a', as_arrow=as_arrow)
    plot_vector(ax, F, color='r', label='F', as_arrow=as_arrow)
    plot_vector(ax, r, color='g', label='r', as_arrow=as_arrow)
    plot_vector(ax, M_scaled, color='b', label=f'M (skaliert um {M_scale})', as_arrow=as_arrow)

    ax.text(0, 0, 0, f"m = {m:.3f} {MASS_UNIT}", color='k', fontsize=10)

    ax.set_xlabel(f'X [{LENGTH_UNIT}]', fontsize=12)
    ax.set_ylabel(f'Y [{LENGTH_UNIT}]', fontsize=12)
    ax.set_zlabel(f'Z [{LENGTH_UNIT}]', fontsize=12)

    ax.set_title(f'Kraft $\\mathbf{{F}} = m \\cdot \\mathbf{{a}}$ [{FORCE_UNIT}] und\nDrehmoment $\\mathbf{{M}} = \\mathbf{{r}} \\times \\mathbf{{F}}$ [{TORQUE_UNIT}]', fontsize=14)

    ax.set_xlim([-5, 10])
    ax.set_ylim([-5, 10])
    ax.set_zlim([-5, 5])

    ax.grid(True)
    ax.legend(['a (Beschleunigung)', 'F (Kraft)', 'r (Hebelarm)', 'M (Drehmoment)'], loc='upper left', fontsize=10)

    # Aktualisiere erklärende Textfelder mit erhöhter Präzision
    for box in text_boxes:
        box.remove()
    text_boxes.clear()
    
    F_mag = np.linalg.norm(F)
    M_mag = np.linalg.norm(M)
    a_mag = np.linalg.norm(a)
    
    create_textbox(fig, 0.1, 0.25, 0.4, 0.15, 
                   f"Masse m = {m:.3f} {MASS_UNIT}\n"
                   f"|a| = {a_mag:.3f} {ACCELERATION_UNIT}\n"
                   f"Kraft |F| = m * |a| = {F_mag:.3f} {FORCE_UNIT}\n"
                   f"Drehmoment |M| = |r × F| = {M_mag:.3f} {TORQUE_UNIT}")

    plt.draw()

def save_figure(event):
    plt.savefig('kraft_und_drehmoment_visualisierung.png', format='png', dpi=300, bbox_inches='tight')
    plt.savefig('kraft_und_drehmoment_visualisierung.svg', format='svg', dpi=300, bbox_inches='tight')
    print("Abbildung als PNG und SVG gespeichert.")

# Hauptprogramm
fig = plt.figure(figsize=(15, 10))
ax = fig.add_subplot(111, projection='3d')

# Slider für interaktive Anpassung
slider_color = 'lightgoldenrodyellow'
mass_slider_ax = plt.axes([0.1, 0.02, 0.3, 0.03], facecolor=slider_color)
ax_slider_ax = plt.axes([0.1, 0.07, 0.3, 0.03], facecolor=slider_color)
ay_slider_ax = plt.axes([0.1, 0.12, 0.3, 0.03], facecolor=slider_color)
az_slider_ax = plt.axes([0.1, 0.17, 0.3, 0.03], facecolor=slider_color)
rx_slider_ax = plt.axes([0.6, 0.07, 0.3, 0.03], facecolor=slider_color)
ry_slider_ax = plt.axes([0.6, 0.12, 0.3, 0.03], facecolor=slider_color)
rz_slider_ax = plt.axes([0.6, 0.17, 0.3, 0.03], facecolor=slider_color)

mass_slider = Slider(mass_slider_ax, f'Masse [{MASS_UNIT}]', 0.1, 10.0, valinit=2.5)
ax_slider = Slider(ax_slider_ax, f'a_x [{ACCELERATION_UNIT}]', -5.0, 5.0, valinit=3.0)
ay_slider = Slider(ay_slider_ax, f'a_y [{ACCELERATION_UNIT}]', -5.0, 5.0, valinit=4.0)
az_slider = Slider(az_slider_ax, f'a_z [{ACCELERATION_UNIT}]', -5.0, 5.0, valinit=0.0)
rx_slider = Slider(rx_slider_ax, f'r_x [{LENGTH_UNIT}]', -2.0, 2.0, valinit=0.5)
ry_slider = Slider(ry_slider_ax, f'r_y [{LENGTH_UNIT}]', -2.0, 2.0, valinit=0.0)
rz_slider = Slider(rz_slider_ax, f'r_z [{LENGTH_UNIT}]', -2.0, 2.0, valinit=1.2)

# Radio Buttons für Vektorstil
vector_style_ax = plt.axes([0.02, 0.5, 0.1, 0.1], facecolor=slider_color)
vector_style_radio = RadioButtons(vector_style_ax, ('Pfeile', 'Linien'), active=0)

# Speichern-Button
save_button_ax = plt.axes([0.8, 0.02, 0.1, 0.04])
save_button = Button(save_button_ax, 'Speichern')
save_button.on_clicked(save_figure)

# Event Handlers
mass_slider.on_changed(update)
ax_slider.on_changed(update)
ay_slider.on_changed(update)
az_slider.on_changed(update)
rx_slider.on_changed(update)
ry_slider.on_changed(update)
rz_slider.on_changed(update)
vector_style_radio.on_clicked(update)

# Globale Variable für Textfelder
text_boxes = []

# Initial plot
update(None)

plt.tight_layout()
plt.subplots_adjust(left=0.1, bottom=0.25, right=0.9, top=0.9)
plt.show()