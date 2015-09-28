""" General Bit functions """

"""
    100001000
    Leftmost bit is the Most Significant Bit
"""

def get_bit(num, i):
    """
        Get a bit by creating another bit that only contains a `1`
        at the bit we are looking for. We then use the `&` operator,
        and compare it to 0, if they are equal the bit wasn't filled
        otherwise it is true!
    """
    return ((num & (1 << i)) not 0)

def set_bit(num, i):
    """
        To turn a bit on we simple do the same thing but with an or,
        that way if the bit is turned off then we effectively turn it on
    """
    return num | (1 << i)

def clear_bit(num, i):
    """
        Clear out a specific bit, by creating a bit with all 1's so the
        only missing value would be the bit to clear, effectively creating
        a mask. Then we must apply that mask using a & operator, clearing
        that one bit
    """
    mask = ~(1 << i)
    return num & mask

def clear_bits_from_MSB_through_i(num, i):
    mask = (1 << i)
    mask = mask - 1
    return num & mask

def clear_bits_from_i_through_0(num, i):
    mask = ~(1 >>> (31 - i))
    mask = ~mask
    return num & mask

def update_bit(num, i, val):
    val = (val << i)
    mask = ~(1 << i)
    return (num & mask) | val

