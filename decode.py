# | decode.py

import sys


if __name__ == '__main__':
    f = 'text.txt.huf'

    s = ''
    with open(f, 'r') as file:
        s = file.read()

    hc, tree = s.split('tree:')

    print(hc)
    print(tree)

