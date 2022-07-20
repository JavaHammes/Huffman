# | test3.py


def string2bits(s=''):
    return [bin(ord(x))[2:].zfill(8) for x in s]


def bits2string(b=None):
    return ''.join([chr(int(x, 2)) for x in b])



code = ['H', '100', 'u', '101', 'm', '110', 'a', '111', 'n', '00', 'f', '01']


letters = ""
bits = ""

for i in range(len(code)):
    if i % 2 == 0:
        letters += code[i]
    else:
        bits += code[i]

letters_bin = string2bits(letters)

letters_bin_string = ""
for l in letters_bin:
    letters_bin_string += l






llb = len(letters_bin_string)
lb = len(bits)

if llb > lb:
    bits += "1" + "0" * (llb - lb - 1)
else:
    letters_bin_string += "1" + "0" * (lb - llb - 1)



length = len(letters_bin_string) + len(bits)

length_bin = bin(length)[2:]

assert len(length_bin) < 31

length_bin = (31 - len(length_bin)) * "0" + length_bin


print(letters_bin_string)
print(bits)
print(length_bin)
print(len(letters_bin_string), len(bits), length)

result_bit_string = length_bin + letters_bin_string + bits 


print(result_bit_string)


'''

import struct

bits = result_bit_string

n = 31
bytes = [bits[i:i+n] for i in range(0, len(bits), n)]

with open("test.bnr", "wb") as f:
    for b in bytes:
        f.write(struct.pack('i', int(b, 2)))

print('#' * 80)

byte = open("test.bnr", "rb").read()

n, r = divmod(len(byte), struct.calcsize('i'))
t = struct.unpack('i' * n, byte)

bbs = []
for x in t:
    x = bin(x)[2:]
    bbs.append(x)

length = []

for b in bbs:
    print(b)

'''
