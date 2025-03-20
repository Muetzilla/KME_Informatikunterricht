# Wurfbewegung 3
import math
import matplotlib.pyplot as plt
from math import sin, cos, radians

tiefe = 30
hoehe = 10
dburg = 500
hburg = 50
hoehe_kanone = 10
g = 9.81
v0 = 83
simulationszeit = 13
N = 10_000
theta = 30
theta_bm = radians(theta)

x_canonball = []
y_canonball = []


def drawCastle(x, y, tiefe, hoehe, color):
    x = [x, x + tiefe, x + tiefe, x, x]
    y = [y, y, y + hoehe, y + hoehe, y]
    plt.plot(x, y, color, linewidth=2, label='Burg')


def drawCanon(x, y):
    plt.plot(x, y, "o-r", label="Kanone")


plt.figure(figsize=(8, 5))

castle_color = "-k"

for i in range(0, N + 1):
    t = i * simulationszeit / N
    x_wert = v0 * math.cos(theta_bm) * t
    y_wert = v0 * math.sin(theta_bm) * t + (-1 / 2 * g * t ** 2) + hoehe_kanone
    if (dburg <= x_wert <= dburg + tiefe) and (hburg <= y_wert <= hburg + hoehe):
        castle_color = "-r"
        break
    x_canonball.append(x_wert)
    y_canonball.append(y_wert)
    if y_wert < 0:
        break

drawCastle(dburg, hburg, tiefe, hoehe, castle_color)
drawCanon(0, hoehe_kanone)

plt.plot(x_canonball, y_canonball, '-b', linewidth=1.5, label=f'Flugbahn Kanonankugel')
plt.xlabel('Entfernung m')
plt.ylabel('Höhe (m)')
plt.title('Kanone schiesst auf Burg')
plt.legend()
plt.axis('equal')
plt.show()
