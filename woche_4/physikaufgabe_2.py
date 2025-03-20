#Schiefer Wurf ohne Luftwiederstand
import math

import matplotlib.pyplot as plt
from math import sin, cos, radians

#Modellparameter
g = 9.81
v0 = 8
h0 = 2
simulationszeit = 1
N = 1000
theta = 30
theta_bm = radians(theta)

x = []
y = []


for i in range(0, N + 1):
    t = i * simulationszeit / N
    x_wert = v0 * math.cos(theta_bm) * t
    y_wert = v0 * math.sin(theta_bm) * t + (-1/2 * g * t ** 2) + h0
    x.append(x_wert)
    y.append(y_wert)
    print(i, t, x_wert, y_wert)


plt.figure(figsize=(8,5))
plt.plot(x, y, 'o-r', linewidth=0.01, label=f'Geschwindigkeit v [m/s], h0={h0}m, theta={theta}°')
plt.xlabel('Entfernung m')
plt.ylabel('Höhe (m)')
plt.title('Horizontaler Wurf')
plt.legend()
plt.grid()
plt.show()