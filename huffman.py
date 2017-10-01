# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 12:36:47 2017

@author: brett
"""

from HuffmanNode import HuffmanNode
from HuffmanNode import HuffmanTree

import heapq as hq

# reads characters from a file and creates and inputs them into a list
# containing the frequency of each character.
def countChars(file, countList):

    while True:

        char = file.read(1)

        if not char:
            break
        else:
            tempNode = HuffmanNode(char)

            # if the list is empty, add the first node
            if len(countList) == 0:
                tempNode.freq = 1
                countList.append(tempNode)
            else:
                for i in range(0, len(countList)):
                    if countList[i] == tempNode:
                        countList[i].freq += 1
                        break
                    elif i == len(countList)-1:
                        tempNode.freq = 1
                        countList.append(tempNode)

def main():


    print("\nHuffman Encoding\nBrett Gedvilas")

    # open file to read
    inFile = open("testFile.txt", "r")

    charList = [] # List that holds the huffmanNode objects from the file
    charHeap = [] # create a heap to store char/value pairs

    # call function to read in all characters
    countChars(inFile, charList)
    charList.sort()


    tree = HuffmanTree(charList)

    # print("Initial Huffman List")
    # print(tree)


    tree.buildTree()

    print("\n")

    print("After building tree")
    tree.printTree(tree.root)

    # for node in charList:
    #     print(node)

    # create a max heap from the list of characters
    # for nodes in charList:
    #     hq.heappush(charHeap, nodes)

    # should print in heap order
    # while charHeap:
    #     print(hq.heappop(charHeap))

if __name__ == '__main__':
    main()
