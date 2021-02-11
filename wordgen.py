#!/usr/bin/pypy3
import sys
from modules.word import *
from modules.alphabet import *


sys.stderr.write('This product includes software developed by L. Pham-Trong and this guy rocks.\n')
args = sys.argv[1:]
len_min = int(args[0])
len_max = int(args[1])

alphabet = args[2] if len(args) == 3 else None
alphabet = alphabet_gen(alphabet)


start = ''.join([alphabet[0] for i in range(len_min)])
done = False
foo = word(start, alphabet)
while not done:
    print(foo)
    foo.next()
    if len(str(foo)) == len_max+1:
        done = True
