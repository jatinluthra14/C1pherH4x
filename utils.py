from itertools import cycle

def isint(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def extend_string(s, length):
    cycle_s = cycle(s)
    return ''.join([next(cycle_s) for x in range(length)])

def format_result(a, b, c):
    return f"-----------\nDEC : {a}\nHEX : {b}\nASCII : {c}\n-----------"

def print_not_silent(s, silent):
        if not silent:
            print(s)