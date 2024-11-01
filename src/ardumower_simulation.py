import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Rectangle
from matplotlib.collections import PatchCollection


# Fahrzeugmodell-Klasse
class VehicleModel:
    def __init__(
        self, wheelbase, track_width, sensor_distance, vehicle_width, vehicle_length
    ):
        """
        Initialisiert das Fahrzeugmodell.

        Args:
            wheelbase (float): Radstand des Fahrzeugs.
            track_width (float): Spurweite des Fahrzeugs.
            sensor_distance (float): Abstand des Sensors vom Schwerpunkt.
            vehicle_width (float): Breite des Fahrzeugs.
            vehicle_length (float): Länge des Fahrzeugs.
        """
        self.wheelbase = wheelbase
        self.track_width = track_width
        self.sensor_distance = sensor_distance
        self.vehicle_width = vehicle_width
        self.vehicle_length = vehicle_length

    def dynamics(self, state, t, control_inputs):
        """
        Berechnet die Fahrzeugdynamik.

        Args:
            state (list): Zustand des Fahrzeugs [x, y, theta, x_d, y_d].
            t (float): Aktuelle Zeit.
            control_inputs (function): Funktion zur Berechnung der Radgeschwindigkeiten.

        Returns:
            list: Ableitungen des Zustands.
        """
        x, y, theta, x_d, y_d = state
        v_right, v_left = control_inputs(t, x, y, theta)

        v = (v_right + v_left) / 2
        omega = (v_right - v_left) / self.track_width

        dx = v * np.cos(theta)
        dy = v * np.sin(theta)
        dtheta = omega

        dx_d = dx + self.sensor_distance * (-np.sin(theta) * omega)
        dy_d = dy + self.sensor_distance * (np.cos(theta) * omega)

        return [dx, dy, dtheta, dx_d, dy_d]

    def simulate(self, t, control_inputs, initial_state):
        """
        Führt die Simulation durch.

        Args:
            t (array): Zeitvektor.
            control_inputs (function): Funktion zur Berechnung der Radgeschwindigkeiten.
            initial_state (list): Anfangszustand des Fahrzeugs.

        Returns:
            array: Lösung der Differentialgleichungen.
        """
        try:
            solution = odeint(self.dynamics, initial_state, t, args=(control_inputs,))
            return solution
        except Exception as e:
            print(f"Fehler während der Simulation: {e}")
            return None


# Hindernisse definieren
obstacles = [
    Rectangle((1, 1), 0.5, 0.5),
    Rectangle((-1, -1), 0.5, 0.5),
    Rectangle((2, -1), 0.5, 0.5),
]


# Funktion zur erweiterten Kollisionserkennung
def check_collision(vehicle_rect):
    """
    Prüft, ob das Fahrzeug mit einem Hindernis kollidiert.

    Args:
        vehicle_rect (matplotlib.patches.Rectangle): Rechteck, das das Fahrzeug darstellt.

        Returns:
            bool: True, wenn eine Kollision vorliegt, sonst False.
    """
    vehicle_path = vehicle_rect.get_path().transformed(vehicle_rect.get_transform())
    for obstacle in obstacles:
        obstacle_path = obstacle.get_path().transformed(obstacle.get_transform())
        if vehicle_path.intersects_path(obstacle_path):
            return True
    return False


# Animation initialisieren
fig, ax = plt.subplots(figsize=(10, 10))
ax.set_xlim(-2, 3)
ax.set_ylim(-2, 3)
ax.set_aspect("equal")
ax.grid(True)


# Potentialfeld zur Hindernisvermeidung mit Begrenzungen
def potential_field(x, y):
    """
    Berechnet das Potentialfeld an der Position (x, y),
    einschließlich repulsiver Kräfte von Hindernissen und Begrenzungen.

    Args:
        x (float): X-Position.
        y (float): Y-Position.

    Returns:
        tuple: Anpassungen der Geschwindigkeit in x- und y-Richtung.
    """
    force_x, force_y = 0, 0

    # Repulsive Kräfte von Hindernissen
    for obstacle in obstacles:
        ox, oy = obstacle.get_xy()
        ow, oh = obstacle.get_width(), obstacle.get_height()
        center_x, center_y = ox + ow / 2, oy + oh / 2
        dx = x - center_x
        dy = y - center_y
        distance = np.hypot(dx, dy)
        if distance < 0.1:
            distance = 0.1  # Vermeidung von extrem hohen Kräften
        repulsive_force = 0.5 / distance**2
        force_x += repulsive_force * (dx / distance)
        force_y += repulsive_force * (dy / distance)

    # Repulsive Kräfte von den Begrenzungen
    boundary_margin = 0.5  # Abstand zur Grenze, ab dem die Kraft wirkt
    boundary_force = 1.0  # Stärke der Kraft

    # Linke Grenze
    if x < ax.get_xlim()[0] + boundary_margin:
        dist = x - ax.get_xlim()[0]
        if dist < 0.1:
            dist = 0.1
        force_x += boundary_force / dist**2

    # Rechte Grenze
    if x > ax.get_xlim()[1] - boundary_margin:
        dist = ax.get_xlim()[1] - x
        if dist < 0.1:
            dist = 0.1
        force_x -= boundary_force / dist**2

    # Untere Grenze
    if y < ax.get_ylim()[0] + boundary_margin:
        dist = y - ax.get_ylim()[0]
        if dist < 0.1:
            dist = 0.1
        force_y += boundary_force / dist**2

    # Obere Grenze
    if y > ax.get_ylim()[1] - boundary_margin:
        dist = ax.get_ylim()[1] - y
        if dist < 0.1:
            dist = 0.1
        force_y -= boundary_force / dist**2

    return force_x, force_y


# Angepasste Steuerungsfunktion mit Hindernisvermeidung
def control_inputs(t, x, y, theta):
    """
    Berechnet die Radgeschwindigkeiten unter Berücksichtigung der Hindernisse.

    Args:
        t (float): Aktuelle Zeit.
        x (float): X-Position des Fahrzeugs.
        y (float): Y-Position des Fahrzeugs.
        theta (float): Orientierung des Fahrzeugs.

    Returns:
        tuple: Geschwindigkeit des rechten und linken Rads.
    """
    # Basisgeschwindigkeit
    base_speed = 0.5

    # Hindernisvermeidung mittels Potentialfeld
    force_x, force_y = potential_field(x, y)

    # Wenn keine Kräfte wirken, fährt das Fahrzeug geradeaus
    if force_x == 0 and force_y == 0:
        desired_direction = theta
    else:
        # Berechnung der gewünschten Richtung
        desired_direction = np.arctan2(force_y, force_x)

    # Berechnung der Winkeldifferenz
    angle_diff = desired_direction - theta
    angle_diff = (angle_diff + np.pi) % (2 * np.pi) - np.pi  # Normalisierung

    # Anpassung der Radgeschwindigkeiten
    v_right = base_speed + angle_diff
    v_left = base_speed - angle_diff

    # Begrenzung der Radgeschwindigkeiten
    max_speed = 1.0
    v_right = np.clip(v_right, -max_speed, max_speed)
    v_left = np.clip(v_left, -max_speed, max_speed)

    return v_right, v_left


# Parameter
wheelbase = 0.4
track_width = 0.4
sensor_distance = 0.23
vehicle_width = 0.5
vehicle_length = 0.6
initial_state = [0, 0.5, 0, 0, 0.5 + sensor_distance]

# Zeitvektor mit adaptiver Schrittweite
t = np.linspace(0, 40, 1000)

# Modell erstellen und simulieren
vehicle = VehicleModel(
    wheelbase, track_width, sensor_distance, vehicle_width, vehicle_length
)
solution = vehicle.simulate(t, control_inputs, initial_state)

# Überprüfen, ob die Simulation erfolgreich war
if solution is None:
    raise SystemExit("Simulation fehlgeschlagen.")

# Ergebnisse extrahieren
x, y, theta, x_d, y_d = solution.T


# Animation
def animate_simulation(x, y, theta):
    """
    Führt die Animation der Simulation durch.

    Args:
        x (array): X-Positionen des Fahrzeugs.
        y (array): Y-Positionen des Fahrzeugs.
        theta (array): Orientierungen des Fahrzeugs.
    """
    # Hindernisse zeichnen
    obstacle_patches = PatchCollection(obstacles, facecolor="gray")
    ax.add_collection(obstacle_patches)

    # Fahrzeugdarstellung initialisieren
    vehicle_patch = Rectangle(
        (0, 0), vehicle_length, vehicle_width, fc="blue", ec="black"
    )
    ax.add_patch(vehicle_patch)
    (sensor_plot,) = ax.plot([], [], "ro", markersize=5)
    (path_plot,) = ax.plot([], [], "g-", lw=1, alpha=0.5)

    # Legende hinzufügen
    ax.legend(["Sensor", "Pfad", "Hindernisse"])

    def init():
        vehicle_patch.set_xy((-vehicle_length / 2, -vehicle_width / 2))
        vehicle_patch.angle = 0
        sensor_plot.set_data([], [])
        path_plot.set_data([], [])
        return vehicle_patch, sensor_plot, path_plot

    def animate(i):
        # Fahrzeugposition und -orientierung aktualisieren
        vehicle_patch.set_xy((x[i] - vehicle_length / 2, y[i] - vehicle_width / 2))
        vehicle_patch.angle = np.degrees(theta[i])

        # Sensorposition aktualisieren
        sensor_x = x[i] + sensor_distance * np.cos(theta[i])
        sensor_y = y[i] + sensor_distance * np.sin(theta[i])
        sensor_plot.set_data([sensor_x], [sensor_y])

        # Pfad aktualisieren
        path_plot.set_data(x[:i], y[:i])

        return vehicle_patch, sensor_plot, path_plot

    FuncAnimation(fig, animate, init_func=init, frames=len(t), interval=20, blit=True)
    plt.title("ArduMower Bewegungssimulation mit Hindernissen")
    plt.xlabel("X-Position (m)")
    plt.ylabel("Y-Position (m)")
    plt.show()


# Animation starten
animate_simulation(x, y, theta)
