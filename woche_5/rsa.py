publicKey = (5, 91)
privateKey = (29, 91)


# Verschlüsselung eines Textes
def encode(plaintext):
    plainAsAscii = []
    for c in plaintext:
        plainAsAscii.append(ord(c))
    e, n = publicKey
    cipherAsInt = []
    for m in plainAsAscii:
        c = (m ** e) % n
        cipherAsInt.append(c)
    cipherAsAsci = []
    for c in cipherAsInt:
        cipherAsAsci.append(chr(c))

    return ''.join(cipherAsAsci)

# Entschlüsselung eines verschlüsselten Texts
def decode(cipher):
    d, n = privateKey
    cipherAsAscii = []
    for c in cipher:
        cipherAsAscii.append(ord(c))
    plaintextAsInt = []
    for m in cipherAsAscii:
        plaintextAsInt.append((m ** d) % n)
    plaintextAsChar = []
    for c in plaintextAsInt:
        plaintextAsChar.append(chr(c))

    return ''.join(plaintextAsChar)


plaintext = "HALLO BOB"
print(plaintext)
cipher = encode(plaintext)
print(cipher)
plaintextDec = decode(cipher)
print(plaintextDec)
