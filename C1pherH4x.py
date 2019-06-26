import base64
import argparse
import re
from ciphers import bacon, morse

ciphers_list = {'bacon': bacon, 'morse':morse}

class C1pherH4x:
    def __init__(self, plaintext=None, ciphertext=None, flag_format=None, cipher=None):
        self.plaintext = plaintext
        self.ciphertext = ciphertext
        self.flag_format = flag_format
        self.cipher = cipher

    def encode(self):
        if self.cipher:
            if self.cipher in ciphers_list:
                self.ciphertext = ciphers_list[self.cipher].encode(self.plaintext)
                if self.ciphertext:
                    print("Ciphertext:")
                    print(self.ciphertext)
            else:
                print(f"Cipher {self.cipher} does not exist!")
                exit(0)
        else:
            print("No Cipher provided to encode")
            exit(0)
            
    def decode(self):
        if self.cipher:
            if self.cipher in ciphers_list:
                self.plaintext = ciphers_list[self.cipher].decode(self.ciphertext)
                if self.plaintext:
                    print("Found Plaintext: ")
                    print(self.plaintext)
            else:
                print(f"Cipher {self.cipher} does not exist!")
                exit(0)
        else:
            print("Detecting Cipher")
            self.detect_ciphers()

    def detect_ciphers(self):
        if re.match('[A|a]+[B|b]+' , self.ciphertext):
            print("Seems like Bacon Cipher")
            self.plaintext = bacon.decode(self.ciphertext)
        elif re.match('[\.\-\s]+' , self.ciphertext):
            print("Seems like Morse Code")
            self.plaintext = morse.decode(self.ciphertext)
        if self.plaintext:
            print("Found Plaintext: ")
            print(self.plaintext)
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-ct', '--ciphertext', help='The ciphertext to decode')
    parser.add_argument('-cf', '--cipherfile', help='The file which contains the ciphertext to decode')
    parser.add_argument('-pt', '--plaintext', help='The plaintext to encode')
    parser.add_argument('-pf', '--plainfile', help='The file which contains the plaintext to encode')
    parser.add_argument('-ff', '--flag-format', help='The known flag format(regex) to search for, otherwise displays everything')
    parser.add_argument('-c', '--cipher', help='Ciphers to implement, Available: base64, brutexor, morse')
    parser.add_argument('-e', '--encode', help='Use to encode plaintext with given cipher', action='store_true')
    parser.add_argument('-d', '--decode', help='Use to decode ciphertext with given cipher or detect cipher', action='store_true')
    args = parser.parse_args()

    if args.encode:
        if args.plainfile:
            plaintext = open(args.plainfile, 'r').read()
        elif args.plaintext:
            plaintext = args.plaintext
        else:
            print('Please mention plaintext/plainfile')
            exit(0)
        plain = C1pherH4x(plaintext=plaintext, cipher=args.cipher)
        plain.encode()
    elif args.decode:
        if args.cipherfile:
            ciphertext = open(args.cipherfile, 'r').read()
        elif args.ciphertext:
            ciphertext = args.ciphertext
        else:
            print('Please mention ciphertext/cipherfile')
            exit(0)
        cipher = C1pherH4x(ciphertext=ciphertext, flag_format=args.flag_format, cipher=args.cipher)
        cipher.decode()
    else:
        print('Encode/Decode not mentioned')
        exit(0)
    