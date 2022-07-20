# | encode.py
import sys
import struct

class Node:

    def __init__(self, value, left_child, right_child):
        self.__value = value
        self.__left_child = left_child
        self.__right_child = right_child

    def __repr__(self):
        return f'value: {self.__value}, left_child: {self.__left_child}, right_child: {self.__right_child}'

    @property
    def key(self):
        if isinstance(self.__value, dict):
            for k, v in self.__value.items():
                return k
        return None

    @property
    def value(self):
        if isinstance(self.__value, dict):
            for k, v in self.__value.items():
                return v
        return self.__value

    @property
    def left_child(self):
        return self.__left_child

    @property
    def right_child(self):
        return self.__right_child

    @value.setter
    def value(self, new_value):
        self.__value = new_value

    @left_child.setter
    def left_child(self, new_left_child):
        self.__left_child = new_left_child

    @right_child.setter
    def right_child(self, new_right_child):
        self.__right_child = new_right_child


class Tree:

    def __init__(self):
        self.__nodes = []
        self.__path = ""
        self.paths = []

    def addNode(self, node):
        self.__nodes.append(node)

    def removeNode(self, idx):
        self.__nodes.pop(idx)

    def sort(self):
        self.__nodes.sort(key=lambda x: x.value)

    def search_path(self,root, k, d=False):
        if root == None:
            return self.__path

        if d:
            self.__path += "1"
        else:
            self.__path += "0"

        if(root.key == k):
            self.__path = self.__path[1:]
            self.paths.append(self.path)
            return self.__path

        self.search_path(root.left_child, k, False)

        self.search_path(root.right_child, k, True)

        self.__path = self.__path[:-1]

    def __repr__(self):
        for n in self.__nodes:
            print(n)

    @property
    def root(self):
        return self.__root

    @property
    def nodes(self):
        return self.__nodes

    @property
    def path(self):
        return self.__path

    @root.setter
    def root(self, new_root):
        self.__root = new_root

    @nodes.setter
    def set_nodes(self, new_nodes):
        self.__nodes = new_nodes


def get_s(f):
    s = ""

    with open(f, 'r') as fi:
        s = fi.read()

    #assert len(s) > 10
    
    return s


def convert_string_to_dict(s):
    d = {}

    for c in s:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1

    d = dict(sorted(d.items(), key=lambda item: item[1]))

    return d


def convert_dict_to_leaf_nodes(d):
    leaf_nodes = []
    for k, v in d.items():
        leaf_nodes.append(Node({k: v}, None, None))

    leaf_nodes.sort(key=lambda x: x.value)

    return leaf_nodes

def print_to_file(bits, fn):
    n = 31
    bbs = [bits[i:i+n] for i in range(0, len(bits), n)]

    with open(fn, "wb") as f:
        for b in bbs:
            f.write(struct.pack('i', int(b,2)))

def read_from_file(fn):
    bbs = open(fn, "rb").read()

    n, _  = divmod(len(bbs), struct.calcsize('i'))
    t = struct.unpack('i' * n, bbs)

    b_b = ""
    for x in t:
        c = str(bin(x)[2:])
        if len(c) != 31 and x != t[-1]:
            c = (31 - len(c)) * "0" + c
        b_b += c

    return b_b


def encode(s):
    tree = Tree()

    d = convert_string_to_dict(s)

    leaf_nodes = convert_dict_to_leaf_nodes(d)

    for n in leaf_nodes:
        tree.addNode(n)

    v = []
    for n in leaf_nodes:
        v.append(n.key)

    while(tree.nodes[0].value != len(s)):
        tree.sort()
        if tree.nodes[1] != None:
            new_node = Node(tree.nodes[0].value + tree.nodes[1].value, tree.nodes[0], tree.nodes[1])
            tree.removeNode(0)
            tree.removeNode(0)
            tree.addNode(new_node)
            tree.sort()
    
    right_bits = ""
    for c in s:
        tree.search_path(tree.nodes[0], c)

    for b in tree.paths:
        right_bits += b

    tree.paths = []

    for c in v:
        tree.search_path(tree.nodes[0], c)

    test = zip(v, tree.paths)

    ss = []
    for c, v in test:
        ss.append(c)
        ss.append(v)

    return (right_bits, ss)

def bitgen(x):
    for c in x:
        yield c

def decode(h, ss):
    bg = bitgen(h)
    current_bits = ""
    solution = ""
    for x in bg:
        current_bits += x
        i = 0
        for w in ss:
            if w == current_bits:
                solution += ss[i-1]
                current_bits = ""
            i += 1

    return solution

def string2bits(s=''):
    return [bin(ord(x))[2:].zfill(8) for x in s]

def bits2string(b=None):
    return ''.join([chr(int(x, 2)) for x in b])

def get_tree_bin(ss):
    letters = ""
    bits = ""



    mlb = 0
    for i in range(len(ss)):
        if i % 2 == 1:
            ss[i] += "1"
            l = len(ss[i])
            if l > mlb:
                mlb = l

    for i in range(len(ss)):
        if i % 2 == 0:
            letters += ss[i]
        else:
            l = len(ss[i])
            if l < mlb:
                ss[i] = ss[i] + '0' * (mlb - l)
            bits += ss[i]

    print("maxlength: ", mlb)
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
    result_bit_string = length_bin + letters_bin_string + bits 

    return result_bit_string

def split_string_to_list(string, n=8):
    return[string[i:i+n] for i in range(0, len(string), n)]


def find_teiler(number):
    t = []
    for i in range(3, number):
        if number % i == 0:
            t.append(i)

    return t

def get_ss(dec):
    length = int(dec[0:31], 2)

    ss = ""
    for i in range(31, 32+length):
        ss += dec[i]


    letters = ss[0:length//2]
    bits = ss[length//2:]

    n = 8
    letters_ar = [letters[i:i+n] for i in range(0, len(letters), n)]

    l = bits2string(letters_ar)

    i = len(bits)
    new_bits = ""
    nn_bits = bits
    for i in reversed(range(len(bits))):
        if bits[i] == "0":
            new_bits = nn_bits[:-1]
            nn_bits = new_bits
        if bits[i] == "1":
            break
            

    bits = nn_bits[:-1]

    t = find_teiler(len(bits))

    rt = 0
    for x in t:
        bit_list = split_string_to_list(bits, x)

        for b in bit_list:
            if b == "1" * x:
                rt = x
                break

    print("calculated length: " , rt)
    bit_list = split_string_to_list(bits, rt)

    new_bits_list = []
    for b in bit_list:
        new_b = ""
        nn_b = b
        for i in reversed(range(len(b))):
            if b[i] == "0":
                new_b = nn_b[:-1]
                nn_b = new_b
            if b[i] == "1":
                new_bits_list.append(nn_b[:-1])
                break

    print("bits: ", new_bits_list)

    new_letters_list = []
    for c in l:
        new_letters_list.append(c)
    print("letters: ", new_letters_list)

    test = zip(new_letters_list, new_bits_list)

    ss = []
    for c, v in test:
        ss.append(c)
        ss.append(v)

    print("NEW SS: ", ss)
    return ss

if __name__ == '__main__':
    s = ''
    f = 'text.txt'

    if len(sys.argv) > 1:
        f = sys.argv[1]

    s = get_s(f)

    #s = "Here comes another test"
    bits, ss = encode(s)

    tree_bin = get_tree_bin(ss)

    print_to_file(tree_bin + bits, 'test.txt.huf')

    dec = read_from_file('test.txt.huf')

    x = get_ss(dec)
    length = int(dec[0:31], 2)
    dec = dec[31+length:]

    solution = decode(dec, x) 
    print(solution)

    with open('solution.txt', 'w') as file:
        file.write(solution)
