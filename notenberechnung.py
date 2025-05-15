def notenberechnung(p1, p2, gewicht):
    return 0.5 * (p1/17 + p2/22) / gewicht * 5 + 1

print(notenberechnung(17, 19, 0.9))