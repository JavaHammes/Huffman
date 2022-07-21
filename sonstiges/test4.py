# | test4.py

def string2bits(s=''):
    return [bin(ord(x))[2:].zfill(8) for x in s]


def bits2string(b=None):
    return ''.join([chr(int(x, 2)) for x in b])

def split_string_to_list(string, n=8):
    return[string[i:i+n] for i in range(0, len(string), n)]

code = ['H', '100', 'u', '101', 'm', '110', 'a', '111', 'n', '00', 'f', '01']
code = ['H', '0100', 'm', '0101', 's', '0110', 'c', '0111', 'e', '1000', 'g', '1001', 'y', '1010', 'u', '1011', 'f', '1110', 'a', '1111', 'n', '000', 'i', '001', ' ', '110']
code = ['x', '0100100', 'B', '0100101', 'z', '0100110', 'P', '0100111', 'D', '0101000', 'H', '0101001', 'y', '0101010', 'v', '0101011', 'S', '0101100', 'p', '0101101', 'ß', '0101110', 'w', '0101111', 'ü', '1010100', ',', '1010101', '!', '1110110', 'A', '1110111', 't', '010000', 'I', '010001', 'o', '101011', '.', '111010', 'd', '00100', 'g', '00101', 'u', '00110', 'c', '00111', 'l', '10010', 'm', '10011', 'b', '10100', 'h', '11100', 's', '11110', 'i', '11111', 'r', '1000', 'a', '1011', 'n', '000', 'e', '011', ' ', '110']



letters = ""
bits = []

for i in range(len(code)):
    if i % 2 == 0:
        letters += code[i]
    else:
        bits.append(code[i])

letters_bin = string2bits(letters)


mlb = 0
new_bits = []
for b in bits:
    b = b + "1"
    if len(b) > mlb:
        mlb = len(b)

    new_bits.append(b)


nn_bits = []
for b in new_bits:
    if len(b) < mlb:
        b = b + "0" * (mlb - len(b))
    nn_bits.append(b)

LETTERS_AMOUNT = len(letters_bin)

BITS_LENGTH = mlb

LETTERS_LENGTH = 8


bit_message_header_list = [format(LETTERS_AMOUNT, '08b'),format(BITS_LENGTH, '08b')]

bit_message_body_list = letters_bin + nn_bits

bit_message = bit_message_header_list + bit_message_body_list

bit_message_string = ""
for b in bit_message:
    bit_message_string += b


print("letters_amount: ", LETTERS_AMOUNT)
print("letters_length: ", LETTERS_LENGTH)
print("bits_length: ", BITS_LENGTH)
print("letters: ", letters)
print("nn_bits: ", nn_bits)
print("ss: ", code)

######################################################################################################################################################



# DECODE

bm = bit_message_string

BITS_AMOUNT = LETTERS_AMOUNT = int(bm[:8], 2)

LETTERS_LENGTH = 8

BITS_LENGTH = int(bm[8:16], 2)



# bits amount = letters amount
# letters length is always 8

letter_bits_amount = LETTERS_LENGTH * LETTERS_AMOUNT

path_bits_amount = BITS_LENGTH * BITS_AMOUNT

letter_bits = bm[16:16 + letter_bits_amount]

path_bits = bm[16+letter_bits_amount:16 + letter_bits_amount + path_bits_amount+1]

letter_bits_list = split_string_to_list(letter_bits, 8)
path_bits_list = split_string_to_list(path_bits, BITS_LENGTH)

letters = bits2string(letter_bits_list)

'''
np = []
for b in path_bits_list:
    new_b = ""
    nn_b = b
    for i in reversed(range(len(b))):
        if b[i] == "0":
            new_b = nn_b[:-1]
            nn_b = new_b
        if b[i] == "1":
            np.append(nn_b[:-1])
            break

'''

nl = []
for b in path_bits_list:
    for i in reversed(range(len(b))):
        if b[i] == "0":
            b = b[:-1]
        elif b[i] == "1":
            b = b[:-1]
            nl.append(b)
            break


path_bits_list = nl

letters_list = []
for i in range(len(letters)):
    letters_list.append(letters[i])

test = zip(letters_list, path_bits_list)

ss = []
for c, v in test:
    ss.append(c)
    ss.append(v)


print(' # ' * 80)
print("LETTERS_AMOUNT: ", LETTERS_AMOUNT)
print("LETTERS_LENGTH: ", LETTERS_LENGTH)
print("BITS_AMOUNT: ", BITS_AMOUNT)
print("BITS_LENGTH: ", BITS_LENGTH)
print("LETTERS: ", letters)
print("NN_BITS: ", path_bits_list)
print("SS: ", ss)
print("CORRECT: ", ss == code)
