# | encode.py
import sys

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
        self.__path = b''
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
            self.__path += b'1'
        else:
            self.__path += b'0'

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

def write_to_file(f, bits, tree):
    file_name = f + '.huf' 
    tree_string = convert_tree_to_string(tree)
    with open(file_name, 'w') as f:
        f.write(bits)
        f.write('tree:')
        f.write(tree_string)

def encode(s):
    tree = Tree()

    d = convert_string_to_dict(s)

    leaf_nodes = convert_dict_to_leaf_nodes(d)

    for n in leaf_nodes:
        tree.addNode(n)

    while(tree.nodes[0].value != len(s)):
        tree.sort()
        if tree.nodes[1] != None:
            new_node = Node(tree.nodes[0].value + tree.nodes[1].value, tree.nodes[0], tree.nodes[1])
            tree.removeNode(0)
            tree.removeNode(0)
            tree.addNode(new_node)
            tree.sort()
    
    bits = b''
    for c in s:
        tree.search_path(tree.nodes[0], c)

    for b in tree.paths:
        bits += b

    #print(bits)
    #print(len(bits))

    return (bits, tree)


def decode(h, tree):
    print(h)
    for n in tree.nodes:
        print(n)


if __name__ == '__main__':
    s = "Huffman"
    f = "text.txt"

    if len(sys.argv) > 1:
        f = sys.argv[1]

    s = get_s(f)

    s = "Huffman"

    decode(    *encode(s)    )

