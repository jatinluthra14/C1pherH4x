from Crypto.Util.number import long_to_bytes, bytes_to_long
from utils import format_result, isint


def encode(s, **kwargs):
    if s.startswith('0x'):
        s = int(s[2:], 16)
    if not isint(s):
        s = bytes_to_long(s.encode())
    return bin(s)[2:]


def decode(s, **kwargs):
    if s.startswith('0b'):
        s = int(s[2:], 2)
    else:
        s = int(s, 2)
    result = long_to_bytes(s)
    return format_result(s, hex(s), str(result, 'utf-8', errors='backslashreplace'))
