"""Class for nodes of the binary huffman tree

[description]
"""


class huffmanNode():

    def __init__(self, char):

        self.char = char  # character value
        self.freq = 0
        
    # overloaded comparison operators
    def __lt__(self, other): 
         return self.freq > other.freq
            
    def __eq__(self, other):
        return self.char == other.char     
        
    # overload to print a node
    def __str__(self):
        return (str(ord(self.char)) + ": " + str(self.freq))
#        print(self.char + ": " + str(self.freq))