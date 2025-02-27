from math import sqrt

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
maximale_zahl = 100
primzahlen = eratosthenes(maximale_zahl)
print(primzahlen)