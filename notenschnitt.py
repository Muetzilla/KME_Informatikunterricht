import math
import random
def informatikNote(note1, note2, mitarbeit):
    pruefungsnote = (note1 + note2) / 2
    if pruefungsnote * 0.8 + mitarbeit *  0.2 > pruefungsnote:
        return 0.5 * math.ceil(2.0 * (pruefungsnote * 0.8 + mitarbeit * 0.2))
    else:
        return 0.5 * math.ceil(2.0 * pruefungsnote)


for i in range(1,20):
    pruefungsNote1 = random.randrange(6,12,1) / 2
    pruefungsNote2 = random.randrange(6,12,1) / 2
    mitarbeit = random.randrange(8,12,1) / 2

    print("Der Schnitt von Schüler " + str(i)+ " ist: "
        "" + str(informatikNote(pruefungsNote1, pruefungsNote2, mitarbeit))
        +   "\nDie Noten dazu sind: \n" +
            "1. Prüfungsnote: " + str(pruefungsNote1) +
            "\n2. Prüfungsnote: " + str(pruefungsNote2) +
            "\nMitarbeit: " + str(mitarbeit) + "\n")