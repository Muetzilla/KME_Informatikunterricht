def is_prime(eingabe):
    teiler = 2
    while teiler < eingabe:
        if eingabe % teiler == 0:
            return False
        teiler += 1
    return True


number = 200003
if is_prime(number):
    print(number, "ist eine Primzahl")
else:
    print(number, "ist keine Primzahl")
