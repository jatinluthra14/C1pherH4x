table = { 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 
        'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 
        'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 
        'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 
        'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 
        'Y':'-.--', 'Z':'--..', '1':'.----', '2':'..---', 
        '3':'...--', '4':'....-', '5':'.....', '6':'-....', 
        '7':'--...', '8':'---..', '9':'----.', '0':'-----', 
        ', ':'--..--', '.':'.-.-.-', '?':'..--..', '/':'-..-.', 
        '-':'-....-', '(':'-.--.', ')':'-.--.-'} 

dec_table = {v: k for k, v in table.items()} 

def encode(plaintext, **kwargs):
    plaintext = plaintext.upper()
    ciphertext = []
    for char in plaintext:
        ciphertext.append(table[char])
    return " ".join(ciphertext)


def decode(ciphertext, **kwargs):
    ciphertext = ciphertext.upper()
    plaintext = []
    for char in ciphertext.split():
        plaintext.append(dec_table[char])
    return "".join(plaintext)
