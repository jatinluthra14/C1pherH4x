import base64
import argparse
import re
from ciphers import bacon, base64, morse, xor
import textwrap
import pyperclip

ciphers_list = {'bacon': bacon, 'base64': base64, 'morse':morse, 'xor':xor}

class C1pherH4x:
    def __init__(self, plaintext=None, ciphertext=None, flag_format=None, cipher=None, key=None):
        self.plaintext = plaintext
        self.ciphertext = ciphertext
        self.flag_format = flag_format
        self.cipher = cipher
        self.key = key
        self.flag = None

    def encode(self):
        if self.cipher:
            if self.cipher in ciphers_list:
                self.ciphertext = ciphers_list[self.cipher].encode(self.plaintext, self.key)
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
                self.plaintext = ciphers_list[self.cipher].decode(self.ciphertext, self.key)
                if self.plaintext:
                    self.print_plaintext()
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
            print(plaintext)
    
    def print_plaintext(self):
        if self.flag_format:
            try:
                self.flag = re.search(f"({self.flag_format})", self.plaintext).group(1)
                print(f"Found a flag in plaintext:\n------------------\n{self.flag}\n------------------")
                opt = input('Do you still want to see plaintext(s)? (y/N): ')
                if opt:
                    if opt.lower()[0] == 'y':
                        print("Okay, Printing Plaintext(s)")
                        print(self.plaintext)
                        exit(0)
                print("Copying the flag to clipboard!")
                pyperclip.copy(self.flag)
                exit(0)
            except Exception as e:
                print(e)
        print("Found Plaintext(s): ")
        print(self.plaintext)
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='C1pherH4x',
      formatter_class=argparse.RawDescriptionHelpFormatter,
      epilog=textwrap.dedent('''\
         Ciphers:
             bacon
             base64
             morse : In . and _ format
             xor : A space separated string of numbers,hex or strings if want to encode, eg. -e -c 'xor' -pt '111 222'

          Be Sure to report any issues or ideas for this on Github   
         '''))
    parser.add_argument('-ct', '--ciphertext', help='The ciphertext to decode')
    parser.add_argument('-cf', '--cipherfile', help='The file which contains the ciphertext to decode')
    parser.add_argument('-pt', '--plaintext', help='The plaintext to encode')
    parser.add_argument('-pf', '--plainfile', help='The file which contains the plaintext to encode')
    parser.add_argument('-ff', '--flag-format', help='The known flag format(regex) to search for, otherwise displays everything')
    parser.add_argument('-c', '--cipher', help='Ciphers to implement, Available: base64, brutexor, morse')
    parser.add_argument('-e', '--encode', help='Use to encode plaintext with given cipher', action='store_true')
    parser.add_argument('-d', '--decode', help='Use to decode ciphertext with given cipher or detect cipher', action='store_true')
    parser.add_argument('-k', '--key', help='Use to provide second provision for ciphers like vigenere or xor')
    parser.add_argument('-kf', '--keyfile', help='Use to import key from file')
    args = parser.parse_args()

    key = None
    if args.keyfile:
        key = open(args.keyfile, 'r').read()
    if args.key:
        key = args.key
    if args.encode:
        if args.plainfile:
            plaintext = open(args.plainfile, 'r').read()
        elif args.plaintext:
            plaintext = args.plaintext
        else:
            print('Please mention plaintext/plainfile')
            exit(0)
        plain = C1pherH4x(plaintext=plaintext, cipher=args.cipher, key=key)
        plain.encode()
    elif args.decode:
        if args.cipherfile:
            ciphertext = open(args.cipherfile, 'r').read()
        elif args.ciphertext:
            ciphertext = args.ciphertext
        else:
            print('Please mention ciphertext/cipherfile')
            exit(0)
        cipher = C1pherH4x(ciphertext=ciphertext, flag_format=args.flag_format, cipher=args.cipher, key=key)
        cipher.decode()
    else:
        print('Encode/Decode not mentioned')
        exit(0)
    