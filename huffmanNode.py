"""

Class definitions for HuffmanTree and HuffmanNode

Brett Gedvilas and David Ward
CSCI 5451
Last Updated: 10/1/2017
"""


class HuffmanNode():

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
        return self.key == other.key

    # overload to print a node
    def __str__(self):
        return self.key + ": " + str(self.freq) + "Bit: " + self.bitType


class HuffmanTree():

    # initialize tree to use the previously created list of nodes
    def __init__(self, nodeList):
        self.nodeList = nodeList
        self.updateList()
        self.root = None

    # inserts a new node and sorts the list back into ascending order
    def updateList(self):
        self.nodeList.sort()

    def combineNodes(self):
        node1 = self.nodeList[0]
        node2 = self.nodeList[1]
        # create a new node thats combines the two lowest frequency nodes
        comboStr = node1.key + node2.key
        newNode = HuffmanNode(comboStr)
        newNode.freq = node1.freq + node2.freq

        # set the new nodes children based off of lowest frequency
        if node1 < node2:
            newNode.leftchild = node1
            newNode.rightchild = node2
        else:
            newNode.leftchild = node2
            newNode.rightchild = node1

        # set bit type. This corresponds to the encoding path
        newNode.leftchild.bitType = '0'
        newNode.rightchild.bitType = '1'

        # pop the two lowest frequency characters off of the list
        self.nodeList.pop(0)
        self.nodeList.pop(0)

        # put new node into the list and re-sort to give a min heap
        self.nodeList.insert(0, newNode)
        self.nodeList.sort()


    def buildTree(self):
        # continue combining nodes together until the list is of size 1
        while len(self.nodeList) > 1:
            self.combineNodes()

        # set root of huffman tree equal to the last 'mega' node we created
        # which contains all chars
        self.root = self.nodeList[0]


    # traverse the tree and print each node
    def printTree(self, rootNode):

        if rootNode:

            print(rootNode)
            # print("\n") # print newline for readability
            self.printTree(rootNode.leftchild)
            self.printTree(rootNode.rightchild)

    # this function recursively traverses the tree and calculates the huffman code
    # for each leaf in the tree. Each leaf corresponds to an individual character
    def getCodes(self, rootNode, code, codeDict):

        if rootNode:
            code += rootNode.bitType # keep appending values to code

            # if the node has no children then we are at a leaf and we add the
            # key-value pair to the dictionary (key = character, value = huffcode)
            # From how the tree is constructed we know each node has either 2 or
            # 0 childen so we don't need to check to see if both exist
            if not rootNode.leftchild:
                codeDict[rootNode.key] = code

            # recursively call for the left and right children
            self.getCodes(rootNode.leftchild, code, codeDict)
            self.getCodes(rootNode.rightchild, code, codeDict)

        return
