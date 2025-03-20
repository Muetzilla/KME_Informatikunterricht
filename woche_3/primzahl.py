import math
import time


def is_prime(eingabe):
    if eingabe < 2:
        return False
    if eingabe == 2:
        return True
    teiler = 1
    while teiler < math.sqrt(eingabe):
        teiler += 2
        if eingabe % teiler == 0:
            return False
    return True


def primzahlen(maxnum):
    primeNumbers = []
    primecounter = 0
    for n in range(1, maxnum + 1):
        if is_prime(n):
            primeNumbers.append(n)
            primecounter += 1

    print("Bis " + str(maxnum) + " gibt es " + str(primecounter) + " Primzahlen")
    return primeNumbers


def primzahlenMaxMin():
    primecounter = 0
    n = 0
    timeout = time.time() + 60
    while True:
        if time.time() > timeout:
            break
            print(n)
        if is_prime(n):
            primecounter += 1
        n += 1
    return primecounter

start_time = time.time()
#print(primzahlen(100_000))
maxnum = 1_000_000
primzahlen(maxnum)

end_time = time.time()
passed_time = end_time - start_time

print("Die Dauer beträgt: " + str(passed_time) + "s")

print("In 60s können " + str(primzahlenMaxMin()) + " Primzahlen berechnet werden.")

# number = 20003
# if is_prime(number):
#    print(number, "ist eine Primzahl")
# else:
#    print(number, "ist keine Primzahl")
