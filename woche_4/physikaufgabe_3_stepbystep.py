# Wurfbewegung 3
import math
import matplotlib.pyplot as plt
from math import radians


def drawCastle(x, y, tiefe, hoehe, color):
    x = [x, x + tiefe, x + tiefe, x, x]
    y = [y, y, y + hoehe, y + hoehe, y]
    plt.plot(x, y, color, linewidth=2, label='Burg')


def drawCanon(x, y):
    plt.plot(x, y, "o-r", label="Kanone")


tiefen = [30, 50]
hoehen = [10, 20]
dburgen = [500, 750]
hburgen = [50, 150]
hoehe_kanone = 10
g = 9.81
v0 = 0
simulationszeit = 13
N = 10_000
theta = 0


while True:
    v0 = float(input("Anfangsgeschwindigkeit > "))
    theta = float(input("Abschusswinkel > "))

    theta_bm = radians(theta)
    x_canonball = []
    y_canonball = []

    plt.figure(figsize=(8, 5))

    castle_color = "-k"

    for i in range(0, N + 1):
        t = i * simulationszeit / N
        x_wert = v0 * math.cos(theta_bm) * t
        y_wert = v0 * math.sin(theta_bm) * t + (-1 / 2 * g * t ** 2) + hoehe_kanone
        for i in range(0, len(dburgen)):
            if (dburgen[i] <= x_wert <= dburgen[i] + tiefen[i]) and (hburgen[i] <= y_wert <= hburgen[i] + hoehen[i]):
                castle_color = "-r"
                break
        x_canonball.append(x_wert)
        y_canonball.append(y_wert)
        if y_wert < 0:
            break

    for i in range(0, len(dburgen)):
        drawCastle(dburgen[i], hburgen[i], tiefen[i], hoehen[i], castle_color)
    drawCanon(0, hoehe_kanone)

    plt.plot(x_canonball, y_canonball, '-b', linewidth=1.5, label=f'Flugbahn Kanonankugel')
    plt.xlabel('Entfernung m')
    plt.ylabel('Höhe (m)')
    plt.title('Kanone schiesst auf Burg')
    plt.legend()
    plt.axis('equal')
    plt.show()
