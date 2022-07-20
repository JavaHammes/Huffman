import struct

bits = "10000000011000000001100000000101000000001100000000110000000010"

n = 31
bytes = [bits[i:i+n] for i in range(0, len(bits), n)]

with open("test.bnr", "wb") as f:
    for b in bytes:
        print(b)
        f.write(struct.pack('i', int(b, 2)))

print('#' * 80)


byte = open("test.bnr", "rb").read()

n, r = divmod(len(byte), struct.calcsize('i'))
t = struct.unpack('i' * n, byte)

bbs = []
for x in t:
    x = bin(x)[2:]
    bbs.append(x)

for b in bbs:
    print(b)

