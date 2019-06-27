from Crypto.Util.number import bytes_to_long, long_to_bytes
from utils import extend_string, isint, format_result

def xor_strings(a, b):
    len_a = len(a)
    len_b = len(b)
    if len_a > len_b:
        b = extend_string(b, len_a)
    elif len_b > len_a:
        a = extend_string(a, len_b)
    long_a = bytes_to_long(a.encode())
    long_b = bytes_to_long(b.encode())
    result = long_a ^ long_b
    return result

def xor_int(a, b):
    return int(a) ^ int(b)

def encode(s, **kwargs):
    if not kwargs['key']:
        print("Key not provided")
        return None
    if s.startswith('0x'):
        s = int(s[2:],16)
    key = kwargs['key']
    if key.startswith('0x'):
        key = int(key[2:],16)
    if isint(s) and isint(key):
        result = xor_int(s, key)
    else:
        result = xor_strings(s, key)
    return format_result(result, hex(result), str(long_to_bytes(result)))

def decode(s, **kwargs):
    if not kwargs['silent']:
        print("Bruteforcing single byte xor")
    plaintexts = []
    for char in range(256):
        plaintexts.append(str(long_to_bytes(xor_strings(s, chr(char)))))
    return "\n".join(plaintexts)
