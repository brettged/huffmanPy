"""

Brett Gedvilas and David Ward
CSCI 5451
Last Updated: 10/6/2017

Huffman Encoding Program
"""

from huffmannode import HuffmanNode
from huffmannode import HuffmanTree
# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg

from PIL import Image

def parse_file(file, count_list):
    """
    Reads characters from a file and creates and inputs them into a list
    containing the frequency of each character.
    """
    count_list.clear()

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

def parse_userin(user_input, count_list):
    """ Parses the user input string and records the frequency of each
        character.

    Stores each node frequency in a list
    """

    count_list.clear()

    for let in user_input:
        temp_node = HuffmanNode(let)
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

def get_user_string():
    """
    Gets a string from the user and counts the characters
    """

    print("Enter your string: ", end="")
    user_string = input()
    return user_string

def run_on_file(char_list, filename):
    """ Runs huffman encoding on a given file

    Given a file, parses the contents of the file and creates a huffman tree
    from the characters in the file.
    """

    print("Creating huffman encoding now...")

    input_file = open(filename, "r")
    output_file = open("encoded" + filename, "w")

    # call function to read in all characters
    parse_file(input_file, char_list)
    input_file.close()

    # sort list of nodes into ascending order so nodes with highest priority
    # are at the front (lowest frequency at front)
    char_list.sort()
    # create a instance of the huffman tree class
    tree = HuffmanTree(char_list)

    # call function to build up the tree
    tree.build_tree()

    # variables for generating a dict with the characters and huffman codes
    temp_code_string = ""
    huff_code_dict = {}
    tree.get_codes(tree.root, temp_code_string, huff_code_dict)

    # print out the characters and their codes
    for node in huff_code_dict:
        print(node + ": " + huff_code_dict[node])
        # print(huff_code_dict)
    input_file = open(filename, "r")
    encode(input_file, output_file, huff_code_dict)

    # close files
    input_file.close()
    output_file.close()

    # tree.print_tree(tree.root)

    # export graph to a neat picture
    tree.pygraph.write(filename[:-4] + '.dot')
    tree.pygraph.layout(prog='dot')
    tree.pygraph.draw(filename[:-4] + 'treePic.png')

    # display picture
    img = Image.open(filename[:-4] + 'treePic.png')
    img.show()

def run_on_string(char_list, user_input):
    """ Runs huffman encoding on a string provided by the user.

    Displays a representation of the encoded string and displays tree image
    """

    parse_userin(user_input, char_list)

    char_list.sort()
    # create a instance of the huffman tree class
    tree = HuffmanTree(char_list)

    # call function to build up the tree
    tree.build_tree()

    temp_code_string = ""
    huff_code_dict = {}
    tree.get_codes(tree.root, temp_code_string, huff_code_dict)

    # print out the characters and their codes
    for node in huff_code_dict:
        print(node + ": " + huff_code_dict[node])

    print("\nA string representation of the binary encoding is: ", end="")
    for let in user_input:
        print(huff_code_dict[let], end="")
    print()

    # export graph to a neat picture
    tree.pygraph.write('userinput.dot')
    tree.pygraph.layout(prog='dot')
    tree.pygraph.draw('usertreePic.png')

    # display the generate huffman tree
    img = Image.open('usertreePic.png')
    img.show()

def main():
    """
    Main program driver for the huffman tree program.
    """

    print("\nHuffman Encoding\nBrett Gedvilas and David Ward")

    char_list = [] # List that holds the huffmanNode objects from the file

    menu = True

    # keep looping until user chooses to quit
    while menu:

        print("\nSelect input method for encoding: ")
        print("---------------------------------")
        print("1. Enter a filename")
        print("2. Input a string")
        print("0. Quit")

        menu_option = int(input())

        if menu_option == 1:
            # get filename
            print("File Name: ", end="")
            filename = input()
            run_on_file(char_list, filename)

        elif menu_option == 2:
            # let user input info
            user_string = get_user_string()
            run_on_string(char_list, user_string)

        else:
            menu = False


if __name__ == '__main__':
    main()
