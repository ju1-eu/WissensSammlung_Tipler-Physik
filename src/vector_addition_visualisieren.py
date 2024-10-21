import matplotlib.pyplot as plt
import numpy as np

def plot_vector(ax, vector, origin=[0, 0], color='r', label=''):
    return ax.quiver(origin[0], origin[1], vector[0], vector[1],
                     angles='xy', scale_units='xy', scale=1, color=color, label=label)

def calculate_vectors():
    F1 = np.array([1.41, 1.41])
    F2 = np.array([2.60, 1.50])
    F_res = F1 + F2
    return F1, F2, F_res

def annotate_vector(ax, vector, label, offset):
    ax.annotate(f'{label}: ({vector[0]:.2f}, {vector[1]:.2f})',
                xy=(vector[0], vector[1]), xytext=offset,
                textcoords='offset points', ha='center', va='bottom',
                bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5),
                arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))

# B5 Querformat in Zoll (250 x 176 mm)
width_in, height_in = 9.84, 6.93

# Vektoren definieren und Plot erstellen
F1, F2, F_res = calculate_vectors()
fig, ax = plt.subplots(figsize=(width_in, height_in))

# Vektoren zeichnen
plot_vector(ax, F1, color='r', label='F1')
plot_vector(ax, F2, color='g', label='F2')
plot_vector(ax, F_res, color='b', label='F_res')

# Gestrichelte Linien für Vektoraddition
ax.plot([0, F1[0], F_res[0]], [0, F1[1], F_res[1]], 'k--', linewidth=1)

# Annotationen hinzufügen
annotate_vector(ax, F1, 'F1', (10, 10))
annotate_vector(ax, F2, 'F2', (10, -10))
annotate_vector(ax, F_res, 'F_res', (-10, 10))

# Achsen konfigurieren
ax.set_xlim(-0.5, 5)
ax.set_ylim(-0.5, 5)
ax.set_aspect('equal', adjustable='box')
ax.grid(True)
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')

# Beschriftungen und Titel
ax.set_xlabel('x-Komponente [N]')
ax.set_ylabel('y-Komponente [N]')
ax.set_title('Vektoraddition: F_res = F1 + F2')
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

plt.tight_layout()
plt.savefig('vector_addition.png', dpi=300, bbox_inches='tight')
plt.savefig('vector_addition.svg', bbox_inches='tight')
plt.show()