import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.gridspec import GridSpec

def berechne_leistung(v_kmh, eta_getriebe, mu):
    # Konstanten
    rho = 1.189  # kg/m³
    cw = 0.31
    A = 2.4  # m²
    m = 1270  # kg
    g = 9.81  # m/s²
    beta = 0  # Grad
    
    # Geschwindigkeit in m/s
    v = v_kmh / 3.6
    
    # Widerstandskräfte
    F_cw = 0.5 * rho * v**2 * cw * A
    F_roll = mu * m * g * np.cos(np.radians(beta))
    F_steig = m * g * np.sin(np.radians(beta))
    F_gesamt = F_cw + F_roll + F_steig
    
    # Leistungen
    P_rad = F_gesamt * v
    P_motor = P_rad / eta_getriebe
    
    return {
        'F_cw': F_cw,
        'F_roll': F_roll,
        'F_gesamt': F_gesamt,
        'P_rad': P_rad/1000,  # kW
        'P_motor': P_motor/1000  # kW
    }

def erstelle_sankey_diagramm(varianten):
    # Seaborn Style
    sns.set_style("whitegrid")
    sns.set_context("notebook", font_scale=1.0)
    
    # Farbpalette
    colors = sns.color_palette("deep")
    
    # B5-Querformat (250 x 176 mm)
    mm_to_inch = 1/25.4
    fig = plt.figure(figsize=(250*mm_to_inch, 176*mm_to_inch), dpi=300)
    
    # Erstelle 1x2 Subplot-Grid
    gs = GridSpec(1, 2, figure=fig)
    
    # Farbschema für die verschiedenen Komponenten
    color_dict = {
        'luft': colors[0],     # Blau
        'roll': colors[3],     # Rot
        'rad': colors[2],      # Grün
        'verlust': colors[7]   # Grau
    }
    
    # Für beide Varianten
    for idx, (variant_name, data) in enumerate(varianten.items()):
        ax = fig.add_subplot(gs[0, idx])
        
        # Berechne Verlustleistung
        P_verlust = data['P_motor'] - data['P_rad']
        
        # Positionen für die Balken
        positions = np.array([0, 1, 2])
        
        # Kraftanteile (Luft- und Rollwiderstand)
        F_anteile = [
            data['F_cw'] / data['F_gesamt'] * data['P_motor'],
            data['F_roll'] / data['F_gesamt'] * data['P_motor'],
        ]
        
        # Balkenbreiten
        balken_breiten = [0.8, 0.6, 0.8]
        
        # Kraftanteile
        ax.bar(positions[0], F_anteile[0], width=balken_breiten[0], 
               color=color_dict['luft'], label='Luftwiderstand')
        ax.bar(positions[0], F_anteile[1], width=balken_breiten[0], 
               bottom=F_anteile[0], color=color_dict['roll'], label='Rollwiderstand')
        
        # Radleistung
        ax.bar(positions[1], data['P_rad'], width=balken_breiten[1], 
               color=color_dict['rad'], label='Radleistung')
        
        # Motorleistung mit Verlust
        ax.bar(positions[2], data['P_rad'], width=balken_breiten[2], 
               color=color_dict['rad'])
        ax.bar(positions[2], P_verlust, width=balken_breiten[2], 
               bottom=data['P_rad'], color=color_dict['verlust'], label='Verlustleistung')
        
        # Beschriftungen
        ax.set_title(f'{variant_name}\n(η = {data["eta_getriebe"]:.2f}, μ = {data["mu"]:.4f})',
                    pad=20)
        ax.set_ylabel('Leistung [kW]')
        ax.set_xticks(positions)
        ax.set_xticklabels(['Widerstandskräfte\n(Leistungsanteile)', 
                           'Radleistung\n{:.2f} kW'.format(data['P_rad']),
                           'Motorleistung\n{:.2f} kW'.format(data['P_motor'])],
                           rotation=0)
        
        # Legende nur beim ersten Plot
        if idx == 0:
            ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        
        # Y-Achsen-Limits vereinheitlichen
        ax.set_ylim(0, max(v0_ergebnisse['P_motor'], v2_ergebnisse['P_motor']) * 1.1)
        
        # Werte in die Balken schreiben
        def autolabel(rects, values, offset=0):
            for rect, val in zip(rects, values):
                height = rect.get_height()
                ax.text(rect.get_x() + rect.get_width()/2., height/2. + offset,
                       f'{val:.2f}\nkW', 
                       ha='center', 
                       va='center',
                       color='black',
                       fontweight='bold')
        
        # Beschrifte Balken
        autolabel([ax.patches[0]], [F_anteile[0]])
        autolabel([ax.patches[1]], [F_anteile[1]], offset=F_anteile[0])
        autolabel([ax.patches[2]], [data['P_rad']])
        autolabel([ax.patches[3]], [data['P_rad']])
        autolabel([ax.patches[4]], [P_verlust], offset=data['P_rad'])
    
    # Haupttitel
    fig.suptitle('Leistungsbedarf der A-Klasse bei 180 km/h', 
                 fontsize=12, 
                 fontweight='bold',
                 y=0.95)
    
    # Layout optimieren
    plt.tight_layout()
    
    # Speichern
    plt.savefig('Leistungsberechnung_Sankey.png', dpi=300, bbox_inches='tight')
    plt.savefig('Leistungsberechnung_Sankey.svg', bbox_inches='tight')
    
    return fig

# Hauptprogramm
if __name__ == "__main__":
    # Variante 0
    v0_ergebnisse = berechne_leistung(
        v_kmh=180,
        eta_getriebe=0.92,
        mu=0.0150  # Angepasst auf 0.0150
    )
    v0_ergebnisse['eta_getriebe'] = 0.92
    v0_ergebnisse['mu'] = 0.0150  # Angepasst auf 0.0150
    
    # Variante 2
    v2_ergebnisse = berechne_leistung(
        v_kmh=180,
        eta_getriebe=0.90,
        mu=0.0205
    )
    v2_ergebnisse['eta_getriebe'] = 0.90
    v2_ergebnisse['mu'] = 0.0205
    
    # Dictionary mit beiden Varianten
    varianten = {
        'Variante 0': v0_ergebnisse,
        'Variante 2': v2_ergebnisse
    }
    
    # Erstelle Visualisierung
    fig = erstelle_sankey_diagramm(varianten)
    plt.show()