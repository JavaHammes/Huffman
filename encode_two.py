# | encode_two.py

from encode import Tree
from encode import Node

s = "Huffman"

tree = Tree()

def convert_string_to_dict(s):
    d = {}

    for c in s:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1

    d = dict(sorted(d.items(), key=lambda item: item[1]))

    return d


d = convert_string_to_dict(s)

def convert_dict_to_leaf_nodes(d):
    leaf_nodes = []
    for k, v in d.items():
        leaf_nodes.append(Node({k: v}, None, None))

    leaf_nodes.sort(key=lambda x: x.value)

    return leaf_nodes


leaf_nodes = convert_dict_to_leaf_nodes(d)

for n in leaf_nodes:
    tree.addNode(n)
    print(n)

print('#' * 80)

i = 0
j = 1

tree.sort()
for _ in range(1):
    if tree.nodes[j] != None:
        new_node = Node(tree.nodes[i].value + tree.nodes[j].value, tree.nodes[i], tree.nodes[j])
        tree.removeTwoFront()
        #tree.removeNode(tree.nodes[i])
        #tree.removeNode(tree.nodes[j])
        tree.addNode(new_node)
        tree.sort()

for n in tree.nodes:
    print(n)



