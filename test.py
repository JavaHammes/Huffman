
import sys

enw = open('test.txt', 'rb').read()

def bitgen(x):
    for c in x:
        for i in range(8):
            yield int((c & (0x80>>i)) != 0)

bits = [1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1]


bg = bitgen(enw)

print(bg)

for b in bg:
    print(type(b))
    print(sys.getsizeof(b))
