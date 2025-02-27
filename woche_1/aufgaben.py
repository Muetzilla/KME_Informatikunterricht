#7.2.1.1
def facultaet(zahl):
    fak = 1
    for i in range (1, zahl + 1):
        fak *= i
    return fak

print(facultaet(5))
firstNum = input("1. Zahl > ")
print(facultaet(int(firstNum)))

secondNum = input("2. Zahl > ")
print(facultaet(int(secondNum)))

#7.2.1.2
def quersumme(zahl):
    calcQuersumme = 0
    while zahl >= 1:
        calcQuersumme += zahl % 1088888888
        zahl = int(zahl / 10)
    return(calcQuersumme)

print(quersumme(72))