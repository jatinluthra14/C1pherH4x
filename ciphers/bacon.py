table = {'A':'AAAAA', 'B':'AAAAB', 'C':'AAABA', 'D':'AAABB', 'E':'AABAA', 'F':'AABAB',
            'G':'AABBA', 'H':'AABBB', 'I':'ABAAA', 'J':'ABAAB', 'K':'ABABA', 'L':'ABABB', 
            'M':'ABBAA', 'N':'ABBAB', 'O':'ABBBA', 'P':'ABBBB', 'Q':'BAAAA', 'R':'BAAAB', 
            'S':'BAABA', 'T':'BAABB', 'U':'BABAA', 'V':'BABAB', 'W':'BABBA', 'X':'BABBB', 
            'Y':'BBAAA', 'Z':'BBAAB'}
table2 = {'A':'AAAAA', 'B':'AAAAB', 'C':'AAABA', 'D':'AAABB', 'E':'AABAA', 'F':'AABAB',
            'G':'AABBA', 'H':'AABBB', 'J':'ABAAA', 'I':'ABAAA', 'K':'ABAAB', 'L':'ABABA', 'M':'ABABB', 
            'N':'ABBAA', 'O':'ABBAB', 'P':'ABBBA', 'Q':'ABBBB', 'R':'BAAAA', 'S':'BAAAB', 
            'T':'BAABA', 'V':'BAABB', 'U':'BAABB', 'W':'BABAA', 'X':'BABAB', 'Y':'BABBA', 'Z':'BABBB', }
dec_table = {v: k for k, v in table.items()} 
dec_table2 = {v: k for k, v in table2.items()} 

def encode(plaintext, **kwargs):
    plaintext = plaintext.upper()
    ciphertext = ['By 24 letter Bacon: ']
    ciphertext2 = ['By 26 letter Bacon: ']
    for char in plaintext:
        ciphertext.append(table[char])
        ciphertext2.append(table2[char])
    ciphertexts = ["".join(ciphertext), "".join(ciphertext2)]
    return "\n".join(ciphertexts)


def decode(ciphertext, **kwargs):
    ciphertext = ciphertext.upper()
    length = len(ciphertext)
    curr = 0
    plaintext = ['By 24 letter Bacon: ']
    plaintext2 = ['By 26 letter Bacon: ']
    while curr in range(length):
        if ciphertext[curr] == " ":
            plaintext.append(" ")
            plaintext2.append(" ")
            curr += 1
        else:
            char = ciphertext[curr:curr+5]
            plaintext.append(dec_table[char])
            plaintext2.append(dec_table2[char])
            curr += 5
    plaintexts = ["".join(plaintext), "".join(plaintext2)]
    return "\n".join(plaintexts)
