from base64 import b64encode, b64decode
from Crypto.Util.number import long_to_bytes, bytes_to_long

def isint(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def encode(s):
    if s.startswith('0x'):
        s = int(s[2:],16)
    if isint(s):
        s = long_to_bytes(s)
    else:
        s = s.encode()
    return str(b64encode(s))

def decode(s):
    bs = b64decode(s)
    long_bs = bytes_to_long(bs)
    return f"-----------\nDEC : {long_bs}\nHEX : {hex(long_bs)}\nASCII : {str(bs)}\n-----------"
