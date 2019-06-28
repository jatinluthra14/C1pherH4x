from base64 import b64encode, b64decode
from Crypto.Util.number import long_to_bytes, bytes_to_long
from utils import format_result, isint


def encode(s, **kwargs):
    if s.startswith('0x'):
        s = int(s[2:], 16)
    if isint(s):
        s = long_to_bytes(s)
    else:
        s = s.encode()
    return b64encode(s).decode()


def decode(s, **kwargs):
    bs = b64decode(s)
    long_bs = bytes_to_long(bs)
    return format_result(long_bs, hex(long_bs), str(bs))
