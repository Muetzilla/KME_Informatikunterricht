from math import sqrt
import time
from matplotlib import pyplot as plt


def eratosthenes(num):
    """
    Sieb des Eratosthenes. Suche alle Primzahlen bis `num` mit Hilfe
    des Algorithmus von Eratosthenes

    :param num: `int`
    :return: `list`
    """
    zahlen = [True] * (num + 1)

    # 0 und 1 sind keine Primzahlen
    zahlen[0] = False
    zahlen[1] = False

    for i in range(2, int(sqrt(len(zahlen)))):
        if zahlen[i]:
            j = i * i
            while j < len(zahlen):
                zahlen[j] = False
                j += i

    primzahlen = []
    for i, value in enumerate(zahlen):
        if value:
            primzahlen.append(i)

    return primzahlen


# Beispielcode
zahlenwerte = range(10_000, 1000_000, 1_000)
laufzeiten = []
for i in range(len(zahlenwerte)):
    starting_time = time.time()
    primzahlen = eratosthenes(zahlenwerte[i])
    stop_time = time.time()
    laufzeiten.append(stop_time - starting_time)

plt.plot(zahlenwerte, laufzeiten, ".-b", label="Laufzeit in Sekunden")
plt.title('Laufzeit von Primzahlberechnungen')
plt.xlabel('Primzahlrange')
plt.ylabel('Dauer in Sekunden')
plt.legend()
plt.show()
