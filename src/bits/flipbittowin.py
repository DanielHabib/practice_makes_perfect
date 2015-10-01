""" Flip Bit to Win """
"""
    You have an integer and you can flip exactly
        one bit from a 0 to a 1. Write a code to find the length of the
        longest sequence of 1s you could create


    Notes:
        First thing to do is to convert the number to binary
        Then I should iterate through that binary number and record the
        sequences and their starting positions, also, I should record the
        positions of the 0s and find out which ones separate sequences of 1s

        2 situations to handle,
             either a single strain of 1s is the longer
            or two strains of 1s can be connected to form the longest

    EX:
        0000000000
        1111111111
        10011111*0*111111001111111
        00010001011101110*0*111111111

    Steps:
        1. Collapse the 1s into their count, and leave the 0s as 0s
        2. Iterate through the array
            * Checking for longest streak,
            * Keeping track of those streaks that are 1 away
            * Calculating new maximums, while iterating
            * The tricky part here will be when handling that maximum
            * If the values are one away, update the maximum then restart at 
                the next value
"""

def flip_bit_to_win(num):
    """ Flip a bit and win!!!!!! """
    """ Convert to binary """
    binary = int(num, 2)
    collapsedBit = ""
    counter = 0
    for bit in binary:
        """ collapse string """
        if bit == 0:
            if counter != 0:
                collapsedBit += counter
            collapsedBit += "0"
            counter = 0
        else:
            counter = counter + 1
    maximumVal = 0
    flipBit = 0
    space = 0
    for val in collapsedBit:
        if val != 0:
            space = 0
            if val > maximumVal:
                maximumVal = val
        else:
            space = space + 1


    



