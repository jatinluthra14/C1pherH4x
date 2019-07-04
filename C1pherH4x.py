import argparse
import re
from ciphers import bacon, base64, binary, caesar, morse, playfair, polybius, vigenere, xor
import textwrap
import pyperclip
from utils import print_not_silent

ciphers_list = {'bacon': bacon, 'base64': base64, 'binary': binary, 'caesar': caesar,
                'morse': morse, 'playfair': playfair, 'polybius': polybius, 'vigenere': vigenere, 'xor': xor}


class C1pherH4x:
    def __init__(self, plaintext=None, ciphertext=None, flag_format=None, cipher=None, key=None, silent=False, no_copy=False):
        self.plaintext = plaintext
        self.ciphertext = ciphertext
        self.flag_format = flag_format
        self.cipher = cipher
        self.key = key
        self.flag = None
        self.silent = silent
        self.no_copy = no_copy

    def encode(self):
        if self.cipher:
            if self.cipher.startswith('rot'):
                self.ciphertext = caesar.encode(self.plaintext, shift=int(
                    self.cipher.replace('rot', '')), key=self.key, silent=self.silent)
            elif self.cipher in ciphers_list:
                self.ciphertext = ciphers_list[self.cipher].encode(
                    self.plaintext, key=self.key, silent=self.silent)
            if self.ciphertext:
                print_not_silent("Ciphertext:", self.silent)
                print(self.ciphertext)
            else:
                print_not_silent(
                    f"Cipher {self.cipher} does not exist!", self.silent)
                exit(0)
        else:
            print_not_silent("No Cipher provided to encode", self.silent)
            exit(0)

    def decode(self):
        if self.cipher:
            if self.cipher.startswith('rot'):
                self.plaintext = caesar.encode(self.ciphertext, shift=int(
                    self.cipher.replace('rot', '')), key=self.key, silent=self.silent)
            elif self.cipher in ciphers_list:
                self.plaintext = ciphers_list[self.cipher].decode(
                    self.ciphertext, key=self.key, silent=self.silent)
            if self.plaintext:
                self.print_plaintext()
            else:
                print_not_silent(
                    f"Cipher {self.cipher} does not exist!", self.silent)
                exit(0)
        else:
            print_not_silent("Detecting Cipher", self.silent)
            self.detect_ciphers()

    def detect_ciphers(self):
        if re.match('[A|a]+[B|b]+', self.ciphertext):
            print_not_silent("Seems like Bacon Cipher", self.silent)
            self.plaintext = bacon.decode(self.ciphertext, silent=self.silent)
        elif re.match('[\.\-\s]+', self.ciphertext):
            print_not_silent("Seems like Morse Code", self.silent)
            self.plaintext = morse.decode(self.ciphertext, silent=self.silent)
        elif re.match('^[01]+$', self.ciphertext):
            print_not_silent("Seems like Binary", self.silent)
            self.plaintext = binary.decode(self.ciphertext, silent=self.silent)
        # Thanks to https://stackoverflow.com/questions/475074/regex-to-parse-or-validate-base64-data
        elif re.match('^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$', self.ciphertext):
            print_not_silent("Seems like Base64", self.silent)
            self.plaintext = base64.decode(self.ciphertext, silent=self.silent)
        if self.plaintext:
            self.print_plaintext()

    def print_plaintext(self):
        if self.flag_format:
            try:
                self.flag = re.search(
                    f"({self.flag_format})", self.plaintext).group(1)
                print_not_silent(
                    f"Found a flag in plaintext:\n------------------", self.silent)
                print(self.flag)
                print_not_silent("------------------", self.silent)
                if not self.silent:
                    opt = input(
                        'Do you still want to see plaintext(s)? (y/N): ')
                    if opt:
                        if opt.lower()[0] == 'y':
                            print_not_silent(
                                "Okay, Printing Plaintext(s)", self.silent)
                            print(self.plaintext)
                            exit(0)
                if not self.no_copy:
                    pyperclip.copy(self.flag)
                    print_not_silent(
                        "Copying the flag to clipboard!", self.silent)
                exit(0)
            except Exception as e:
                print_not_silent(e, silent=self.silent)
        print_not_silent("Found Plaintext(s): ", self.silent)
        print(self.plaintext)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='C1pherH4x',
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     epilog=textwrap.dedent('''\
         Ciphers:
             bacon
             base64
             binary
             caesar   :  Specify custom charset in key or for specific shift, use rot convention eg. rot8 for 8 shift
             morse    :  In . and _ format
             playfair :  Specify key in the key argument
             polybius :  Specify delimiter in the key argument
             vigenere :  Specify key in the key agument
             xor      :  Specify second item in key argument

          Be Sure to report any issues or ideas for this on Github   
         '''))
    parser.add_argument('-ct', '--ciphertext', help='The ciphertext to decode')
    parser.add_argument('-cf', '--cipherfile',
                        help='The file which contains the ciphertext to decode')
    parser.add_argument('-pt', '--plaintext', help='The plaintext to encode')
    parser.add_argument('-pf', '--plainfile',
                        help='The file which contains the plaintext to encode')
    parser.add_argument('-ff', '--flag-format',
                        help='The known flag format(regex) to search for, otherwise displays everything')
    parser.add_argument(
        '-c', '--cipher', help='Ciphers to implement, Available: base64, brutexor, morse')
    parser.add_argument(
        '-e', '--encode', help='Use to encode plaintext with given cipher', action='store_true')
    parser.add_argument(
        '-d', '--decode', help='Use to decode ciphertext with given cipher or detect cipher', action='store_true')
    parser.add_argument(
        '-k', '--key', help='Use to provide second provision for ciphers like vigenere or xor')
    parser.add_argument('-kf', '--keyfile', help='Use to import key from file')
    parser.add_argument(
        '--silent', '-s', help='Silent mode, Prints only final output', action='store_true')
    parser.add_argument(
        '--no-copy', '-nc', help="Don't copy flag if found", action='store_true')
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
        plain = C1pherH4x(plaintext=plaintext,
                          cipher=args.cipher, key=key, silent=args.silent)
        plain.encode()
    elif args.decode:
        if args.cipherfile:
            ciphertext = open(args.cipherfile, 'r').read()
        elif args.ciphertext:
            ciphertext = args.ciphertext
        else:
            print('Please mention ciphertext/cipherfile')
            exit(0)
        cipher = C1pherH4x(ciphertext=ciphertext, flag_format=args.flag_format,
                           cipher=args.cipher, key=key, silent=args.silent, no_copy=args.no_copy)
        cipher.decode()
    else:
        print('Encode/Decode not mentioned')
        exit(0)
