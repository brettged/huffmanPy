"""

Class definitions for HuffmanTree and HuffmanNode

Brett Gedvilas and David Ward
CSCI 5451
Last Updated: 10/6/2017
"""

# use the pygraphviz wrapper to plot the huffman tree
import pygraphviz as pgv


class HuffmanNode():
    """
    HuffmanNode class. This class defines a 'huffman node' which is a datatype
    that defines an individual node in a huffman tree.
    """
    def __init__(self, key):

        self.key = key
        self.freq = 0
        self.bit_type = '' # either a 1 or a 0 depending on if this node is a
                          # left or right child

        # references to the nodes left and right children
        self.leftchild = None
        self.rightchild = None

    # overloaded comparison operators
    def __lt__(self, other):
        return self.freq < other.freq

    def __eq__(self, other):
        return self.key == other.key

    # overload to print a node
    def __str__(self):
        return self.key + ": " + str(self.freq) # + "Bit: " + self.bit_type


class HuffmanTree():
    """
    HuffmanTree class.
    """

    def __init__(self, node_list):
        """
        Initialize a huffman tree with a list of nodes
        """

        self.node_list = node_list
        self.update_list()
        self.root = None

        self.pygraph = pgv.AGraph() # create a graph within our class for plotting purposes
        self.pygraph.graph_attr['label'] = "Huffman Tree"

    def update_list(self):
        """
        Inserts a new node and sorts the list back into ascending order
        """

        self.node_list.sort()

    def combine_nodes(self):
        """
        Removes the two nodes with the lowest frequency from the list and
        combines them into a new node with combined frequency and string.
        It also sets the two previous nodes to be children of the combined
        node and inserts the new combined node back into the node list.
        """
        node1 = self.node_list[0]
        node2 = self.node_list[1]
        # create a new node thats combines the two lowest frequency nodes
        combo_str = node1.key + node2.key
        new_node = HuffmanNode(combo_str)
        new_node.freq = node1.freq + node2.freq

        # ********* attempt at graphical stuff **************
            # add nodes
        self.pygraph.add_node(node1)
        self.pygraph.add_node(node2)
        self.pygraph.add_node(new_node)

        # set the new nodes children based off of lowest frequency
        if node1 < node2:
            new_node.leftchild = node1
            new_node.rightchild = node2

            # create edges between parent and children nodes
            self.pygraph.add_edge(new_node, node1, label='0', color='red')
            self.pygraph.add_edge(new_node, node2, label='1', color='blue')
        else:
            new_node.leftchild = node2
            new_node.rightchild = node1
            # create edges between parent and children nodes
            self.pygraph.add_edge(new_node, node2, label='0', color='red')
            self.pygraph.add_edge(new_node, node1, label='1', color='blue')

        # set bit type. This corresponds to the encoding path
        new_node.leftchild.bit_type = '0'
        new_node.rightchild.bit_type = '1'

        # pop the two lowest frequency characters off of the list
        self.node_list.pop(0)
        self.node_list.pop(0)

        # put new node into the list and re-sort to give a min heap
        self.node_list.insert(0, new_node)
        self.node_list.sort()


    def build_tree(self):
        """
        This function builds the huffman tree by combining all the nodes from
        the list until there is only one complete node left. This is the root
        of the huffman tree.
        """
        # continue combining nodes together until the list is of size 1
        while len(self.node_list) > 1:
            self.combine_nodes()

        # set root of huffman tree equal to the last 'mega' node we created
        # which contains all chars
        self.root = self.node_list[0]

    def print_tree(self, root_node):
        """
        Traverse the tree and print each node
        """

        if root_node:

            print(root_node)
            # print("\n") # print newline for readability
            self.print_tree(root_node.leftchild)
            self.print_tree(root_node.rightchild)


    def get_codes(self, root_node, code, code_dict):
        """
        This function recursively traverses the tree and calculates the huffman
        code for each leaf in the tree. Each leaf corresponds to an individual
        character. It store the characters and corresponding code in a
        dictionary.
        """

        if root_node:
            code += root_node.bit_type # keep appending values to code

            # if the node has no children then we are at a leaf and we add the
            # key-value pair to the dictionary (key = character, value = huffcode)
            # From how the tree is constructed we know each node has either 2 or
            # 0 childen so we don't need to check to see if both exist
            if not root_node.leftchild:
                code_dict[root_node.key] = code

            # recursively call for the left and right children
            self.get_codes(root_node.leftchild, code, code_dict)
            self.get_codes(root_node.rightchild, code, code_dict)

        return
