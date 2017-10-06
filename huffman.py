# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 12:36:47 2017

@author: brett

Brett Gedvilas and David Ward
CSCI 5451
Last Updated: 10/1/2017

Huffman Encoding Program
"""

from huffmannode import HuffmanNode
from huffmannode import HuffmanTree


def count_chars(file, count_list):
    """
    Reads characters from a file and creates and inputs them into a list
    containing the frequency of each character.
    """

    while True:

        char = file.read(1)

        if not char:
            break
        else:
            temp_node = HuffmanNode(char)

            # if the list is empty, add the first node
            if len(count_list) == 0:
                temp_node.freq = 1
                count_list.append(temp_node)
            else:
                for i in range(0, len(count_list)):
                    if count_list[i] == temp_node:
                        count_list[i].freq += 1
                        break
                    elif i == len(count_list)-1:
                        temp_node.freq = 1
                        count_list.append(temp_node)


def encode(inputfile, outputfile, chardict):
    """
    Uses calculate dictionary to write encoded characters to a new file
    """

    while True:

        # read in characters one at a time from input file
        char = inputfile.read(1)
        if not char:
            break

        else:
            # retrieve the encoded value from the dictionary and write it to the
            # output file
            outputfile.write(chardict[char])

# def build_visual(hufftree, visual):
#
#     temp_node = hufftree.root


def main():
    """
    Main program driver for the huffman tree program.
    """

    print("\nHuffman Encoding\nBrett Gedvilas and David Ward")

    # open the file we want to encode and an output file showing the string
    # encoding
    in_file = open("testFile.txt", "r")
    out_file = open("encoded.txt", "w")

    char_list = [] # List that holds the huffmanNode objects from the file

    # call function to read in all characters
    count_chars(in_file, char_list)
    in_file.close()

    # sort list of nodes into ascending order so nodes with highest priority
    # are at the front (lowest frequency at front)
    char_list.sort()

    # for node in char_list:
    #
    #     print(node)

    # create a instance of the huffman tree class
    tree = HuffmanTree(char_list)

    # call function to build up the tree
    tree.build_tree()

    # print("codes")
    temp_code_string = ""
    huff_code_dict = {}
    tree.get_codes(tree.root, temp_code_string, huff_code_dict)

    for node in huff_code_dict:
        print(node + ": " + huff_code_dict[node])
    # print(huff_code_dict)
    in_file = open("testFile.txt", "r")
    encode(in_file, out_file, huff_code_dict)

    # close files
    in_file.close()
    out_file.close()

    # tree.print_tree(tree.root)

    # export graph to a neat picture
    tree.pygraph.write('hufftreepic.dot')
    tree.pygraph.layout(prog='dot')
    tree.pygraph.draw('treePic.png')


if __name__ == '__main__':
    main()
