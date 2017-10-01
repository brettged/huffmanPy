"""Class for nodes of the binary huffman tree

[description]
"""


class huffmanNode():

    def __init__(self, key):

        self.key = key
        self.freq = 0
        self.bitType = '' # either a 1 or a 0 depending on if this node is a
                          # left or right child

        # references to the nodes left and right children
        self.leftchild = None
        self.rightchild = None

    # overloaded comparison operators
    def __lt__(self, other):
         return self.freq < other.freq

    def __eq__(self, other):
        return self.char == other.char

    # overload to print a node
    def __str__(self):
        return (str(ord(self.char)) + ": " + str(self.freq))


# class huffmanTree():
