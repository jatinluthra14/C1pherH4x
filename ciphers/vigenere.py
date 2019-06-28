from Crypto.Util.number import bytes_to_long, long_to_bytes
from utils import extend_string, isint, format_result
import string
from itertools import cycle

table = string.ascii_lowercase
table_upper = string.ascii_uppercase


def encode(s, **kwargs):
    if not kwargs['key']:
        print("Key not provided")
        return None
    len_s = len(s)
    key = extend_string(kwargs['key'], len_s)
    cycle_key = cycle(key)
    ciphertext = []
    for i in range(len_s):
        if s[i] not in table and s[i] not in table_upper:
            ciphertext.append(s[i])
        else:
            if s[i].islower():
                index = table.index(
                    s[i]) + table.index(next(cycle_key).lower())
                ciphertext.append(table[index % 26])
            else:
                index = table_upper.index(
                    s[i]) + table_upper.index(next(cycle_key).upper())
                ciphertext.append(table_upper[index % 26])
    return "".join(ciphertext)


def decode(s, **kwargs):
    plaintext = []
    len_s = len(s)
    key = extend_string(kwargs['key'], len_s)
    cycle_key = cycle(key)
    for i in range(len_s):
        if s[i] not in table and s[i] not in table_upper:
            plaintext.append(s[i])
        else:
            if s[i].islower():
                index = table.index(
                    s[i]) - table.index(next(cycle_key).lower())
                plaintext.append(table[index % 26])
            else:
                index = table_upper.index(
                    s[i]) - table_upper.index(next(cycle_key).upper())
                plaintext.append(table_upper[index % 26])
    return "".join(plaintext)
