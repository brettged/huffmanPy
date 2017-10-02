# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 12:36:47 2017

@author: brett

Brett Gedvilas and David Ward
CSCI 5451
Last Updated: 10/1/2017

Huffman Encoding Program
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


# uses calculate dictionary to write encoded characters to a new file
def encode(input, output, dict):

    while True:

        # read in characters one at a time from input file
        char = input.read(1)
        if not char:
            break

        else:
            # retrieve the encoded value from the dictionary and write it to the
            # output file
            output.write(dict[char])


def main():


    print("\nHuffman Encoding\nBrett Gedvilas and David Ward")

    # open file to read
    inFile = open("testFile.txt", "r")
    outFile = open("encoded.txt", "w")

    charList = [] # List that holds the huffmanNode objects from the file
    charHeap = [] # create a heap to store char/value pairs

    # call function to read in all characters
    countChars(inFile, charList)
    inFile.close()

    # sort list of nodes into ascending order so nodes with highest priority
    # are at the front (lowest frequency at front)
    charList.sort()

    # create a instance of the huffman tree class
    tree = HuffmanTree(charList)

    # call function to build up the tree
    tree.buildTree()

    print("codes")
    tempCodeString = ""
    huffCodeDict = {}
    tree.getCodes(tree.root, tempCodeString, huffCodeDict)

    # print(codeDict)
    inFile = open("testFile.txt", "r")
    encode(inFile, outFile, huffCodeDict)

    # close files
    inFile.close()
    outFile.close()


if __name__ == '__main__':
    main()
