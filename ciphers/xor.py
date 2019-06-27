from Crypto.Util.number import bytes_to_long, long_to_bytes
from itertools import cycle

def isint(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def xor_strings(a, b):
    len_a = len(a)
    len_b = len(b)
    if len_a > len_b:
        cycle_b = cycle(b)
        b = ''.join([next(cycle_b) for x in range(len_a)])
    elif len_b > len_a:
        cycle_a = cycle(a)
        a = ''.join([next(cycle_a) for x in range(len_b)])
    long_a = bytes_to_long(a.encode())
    long_b = bytes_to_long(b.encode())
    result = long_a ^ long_b
    return result

def xor_int(a, b):
    return int(a) ^ int(b)

def encode(s, key=None):
    if not key:
        print("Key not provided")
        return None
    if s.startswith('0x'):
        s = int(s[2:],16)
    if key.startswith('0x'):
        key = int(key[2:],16)
    if isint(s) and isint(key):
        result = xor_int(s, key)
    else:
        result = xor_strings(s, key)
    return f"-----------\nDEC : {result}\nHEX : {hex(result)}\nASCII : {long_to_bytes(result)}\n-----------"

def decode(s, key=None):
    print("Bruteforcing single byte xor")
    plaintexts = []
    for char in range(256):
        plaintexts.append(str(long_to_bytes(xor_strings(s, chr(char)))))
    return "\n".join(plaintexts)
