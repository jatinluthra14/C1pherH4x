import base64
import argparse

class C1pherH4x:
    def __init__(self, ciphertext, flag_format):
        self.ciphertext = ciphertext
        self.flag_format = flag_format

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-ct', '--ciphertext', help='The ciphertext to use against')
    parser.add_argument('-cf', '--cipherfile', help='The file which contains the ciphertext to use against')
    parser.add_argument('-ff', '--flag-format', help='The known flag format(regex) to search for, otherwise displays everything')
    parser.add_argument('--attacks', help='Attacks to implement, Available: base64, brutexor, morse')
    args = parser.parse_args()

    if args.cipherfile:
        ciphertext = open(args.cipherfile, 'r').read()
    else:
        ciphertext = args.ciphertext

    if not ciphertext:
        print("Please input a ciphertext")
        exit(0)
    
    cipher = C1pherH4x(ciphertext, args.flag_format)