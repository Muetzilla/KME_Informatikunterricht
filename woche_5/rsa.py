publicKey = (5, 91)
privateKey = (29, 91)


# Verschlüsselung eines Textes
def encode(plaintext):
    e, n = publicKey
    cipherAsAsci = []
    for c in plaintext:
        cipherAsAsci.append(chr((ord(c) ** e) % n))
    return ''.join(cipherAsAsci)

# Entschlüsselung eines verschlüsselten Texts
def decode(cipher):
    d, n = privateKey
    plaintextAsChar = []
    for c in cipher:
        plaintextAsChar.append(chr((ord(c) ** d) % n))
    return ''.join(plaintextAsChar)


plaintext = "HALLO BOB"
print(plaintext)
cipher = encode(plaintext)
print(cipher)
plaintextDec = decode(cipher)
print(plaintextDec)
