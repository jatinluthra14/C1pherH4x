import string

table = string.ascii_lowercase
table_upper = string.ascii_uppercase


def rot(s, shift, key=None):
    text = []
    if not key:
        for i in range(len(s)):
            if s[i] not in table and s[i] not in table_upper:
                text.append(s[i])
            else:
                if s[i].islower():
                    index = table.index(s[i]) + shift
                    text.append(table[index % 26])
                else:
                    index = table_upper.index(s[i]) + shift
                    text.append(table_upper[index % 26])
    else:
        for i in range(len(s)):
            if s[i] not in key:
                text.append(s[i])
            else:
                index = key.index(s[i]) + shift
                text.append(key[index % len(key)])
    return "".join(text)


def encode(s, **kwargs):
    if 'shift' in kwargs:
        shift = kwargs['shift']
    else:
        if not kwargs['silent']:
            print("No Shift provided!")
    key = None
    if 'key' in kwargs:
        key = kwargs['key']
    if int(shift) == 47:
        key = ''.join([chr(i) for i in range(33, 127)])
    return rot(s, shift, key=key)


def decode(s, **kwargs):
    key = None
    if 'key' in kwargs:
        key = kwargs['key']
    if 'shift' in kwargs:
        shift = kwargs['shift']
        if int(shift) == 47:
            key = ''.join([chr(i) for i in range(33, 127)])
        return rot(s, shift, key=key)
    plaintexts = []
    if not key:
        len_key = 26
    else:
        len_key = len(key)
    for i in range(len_key):
        plaintexts.append(f"ROT {i}: {rot(s,i, key=key)}")
    return "\n".join(plaintexts)
