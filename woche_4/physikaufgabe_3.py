import numpy as np
import matplotlib.pyplot as plt


def projectile_motion(initial_velocity, theta, castle_distance=500, castle_height=50, g=9.81):
    angle_radians = np.radians(theta)

    initial_velocity_x = initial_velocity * np.cos(angle_radians)
    initial_velocity_y = initial_velocity * np.sin(angle_radians)

    time_to_peak = initial_velocity_y / g
    total_flight_time = 2 * time_to_peak

    time_intervals = np.linspace(0, total_flight_time, num=500)

    x_positions = initial_velocity_x * time_intervals
    y_positions = initial_velocity_y * time_intervals - 0.5 * g * time_intervals ** 2

    hit = False
    for i in range(len(x_positions)):
        if castle_distance - 10 <= x_positions[i] <= castle_distance + 10 and castle_height - 30 <= y_positions[i] <= castle_height:
            hit = True
            x_positions = x_positions[:i + 1]
            y_positions = y_positions[:i + 1]
            break

    fig, ax = plt.subplots()
    ax.set_xlim(0, max(castle_distance + 50, max(x_positions)))
    ax.set_ylim(0, max(castle_height + 20, max(y_positions)))

    color = 'red' if hit else 'black'
    ax.add_patch(plt.Rectangle((castle_distance - 10, castle_height - 30), 20, 30, color=color, alpha=0.5))

    ax.plot(x_positions, y_positions, label="Flugbahn")
    ax.set_xlabel("Distanz (m)")
    ax.set_ylabel("Höhe (m)")
    ax.set_title("Kanonenschuss auf die Burg")
    ax.legend()

    plt.show()


projectile_motion(initial_velocity=150, theta=10)
