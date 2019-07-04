import string
from utils import index_2d


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


def fix_ciphertext(ciphertext):
    return [''.join([ciphertext[i], ciphertext[i+1]]) for i in range(0, len(ciphertext), 2)]


def fix_key(key):
    if len(key) != 26:
        if key.isupper():
            table = string.ascii_uppercase
        else:
            table = string.ascii_lowercase
        for char in table:
            if char.lower() == 'j':
                continue
            if char not in key:
                key += char
    return key


def encode(s, **kwargs):
    if 'key' not in kwargs:
        print("Key not provided")
        return None
    key = fix_key(kwargs['key'])
    plaintext = fix_plaintext(s, key)
    key_arr = gen_keyblock(key)
    ciphertext = []
    for pair in plaintext:
        a, b = pair
        ind_a = index_2d(key_arr, a)
        ind_b = index_2d(key_arr, b)
        if ind_a[0] != ind_b[0] and ind_a[1] != ind_b[1]:
            c = key_arr[ind_a[0]][ind_b[1]]
            d = key_arr[ind_b[0]][ind_a[1]]
        elif ind_a[0] == ind_b[0]:
            c = key_arr[ind_a[0]][(ind_a[1]+1) % len(key_arr[0])]
            d = key_arr[ind_b[0]][(ind_b[1]+1) % len(key_arr[0])]
        elif ind_a[1] == ind_b[1]:
            c = key_arr[(ind_a[0]+1) % len(key_arr[0])][ind_a[1]]
            d = key_arr[(ind_b[0]+1) % len(key_arr[0])][ind_b[1]]
        ciphertext.append(c)
        ciphertext.append(d)
    return ''.join(ciphertext)


def decode(s, **kwargs):
    if 'key' not in kwargs:
        print("Key not provided")
        return None
    key = fix_key(kwargs['key'])
    ciphertext = fix_ciphertext(s)
    key_arr = gen_keyblock(key)
    plaintext = []
    for pair in ciphertext:
        a, b = pair
        ind_a = index_2d(key_arr, a)
        ind_b = index_2d(key_arr, b)
        if ind_a[0] != ind_b[0] and ind_a[1] != ind_b[1]:
            c = key_arr[ind_a[0]][ind_b[1]]
            d = key_arr[ind_b[0]][ind_a[1]]
        elif ind_a[0] == ind_b[0]:
            c = key_arr[ind_a[0]][(ind_a[1]-1) % len(key_arr[0])]
            d = key_arr[ind_b[0]][(ind_b[1]-1) % len(key_arr[0])]
        elif ind_a[1] == ind_b[1]:
            c = key_arr[(ind_a[0]-1) % len(key_arr[0])][ind_a[1]]
            d = key_arr[(ind_b[0]-1) % len(key_arr[0])][ind_b[1]]
        plaintext.append(c)
        plaintext.append(d)
    return ''.join(plaintext)
