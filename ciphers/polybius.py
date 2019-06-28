from utils import isint, index_2d
import string

table = [
    ['A', 'B', 'C', 'D', 'E'],
    ['F', 'G', 'H', 'I', 'K'],
    ['L', 'M', 'N', 'O', 'P'],
    ['Q', 'R', 'S', 'T', 'U'],
    ['V', 'W', 'X', 'Y', 'Z'],
]


def encode(plaintext, **kwargs):
    ciphertext = []
    for char in plaintext.replace('J', 'I'):
        if char not in string.ascii_uppercase:
            ciphertext.append(char)
            continue
        row, col = index_2d(table, char)
        ciphertext.append(f"{row+1}-{col+1}")
    if kwargs['key']:
        return kwargs['key'].join(ciphertext)
    return " ".join(ciphertext)


def decode(ciphertext, **kwargs):
    plaintext = []
    if kwargs['key']:
        ciphertext = ciphertext.split(kwargs['key'])
    else:
        ciphertext = ciphertext.split()
    for char in ciphertext:
        if '-' in char and len(char) > 1:
            char = char.replace('-', '')
        if not isint(char):
            plaintext.append(char)
            continue
        plaintext.append(table[int(char[0])-1][int(char[1])-1])
    return "".join(plaintext)
