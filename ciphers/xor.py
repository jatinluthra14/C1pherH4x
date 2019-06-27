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

def encode(s):
    st = s.split()
    if len(st) != 2:
        print(f"Error found {len(st)} string(s), expected 2")
    a, b = st
    print(a,b)
    if a.startswith('0x'):
        a = int(a[2:],16)
    if b.startswith('0x'):
        b = int(b[2:],16)
    if isint(a) and isint(b):
        result = xor_int(a, b)
    else:
        result = xor_strings(a, b)
    f"-----------\nDEC : f{result}\nHEX : f{hex(result)}\nASCII : f{long_to_bytes(result)}"

def decode(s):
    print("Bruteforcing single byte xor")
    plaintexts = []
    for char in range(256):
        plaintexts.append(str(long_to_bytes(xor_strings(s, chr(char)))))
    return "\n".join(plaintexts)
