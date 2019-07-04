def gen_keyblock(key):
    keyblock = []
    ind = 0
    for _ in range(5):
        row = []
        for _ in range(5):
            row.append(key[ind])
            ind += 1
        keyblock.append(row)
    return keyblock


def fix_plaintext(plaintext, key):
    if len(plaintext) % 2 != 0:
        if key.isupper():
            plaintext += "X"
        else:
            plaintext += "x"
    plain = []
    for char in plaintext:
        if char in key:
            plain.append(char)
    plaintext = []
    for i in range(0, len(plain), 2):
        if plain[i] != plain[i+1]:
            plaintext.append(''.join([plain[i], plain[i+1]]))
        else:
            if plain[i].isupper():
                plaintext.append(''.join([plain[i], 'X']))
            else:
                plaintext.append(''.join([plain[i], 'x']))
    return plaintext


print(fix_plaintext('HAMME', 'UNPROBLEMATICDFGHKQSVWXYZ'))
