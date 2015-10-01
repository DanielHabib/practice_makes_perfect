""" Binary to string 5.2 """
"""
    Given:
        Real number between 0 and 1 (decimal) passed in as a double
    Action:
        print binary representation otherwise throw error
        Turn a float between 0 and 1 into binary
    Output:
        At most 32 Characters

"""
class InvalidNumberError(Exception):
    """ The number provided wasn't between 0 and 1 Exclusive """


class CannotRepresentAsBinaryError(Exception):
    """ The number can't be represented in
        32 bits or less
    """


def convert_float_into_bin1(num):
    if num >= 1 or num <= 0:
        raise InvalidNumberError

    binary = ""
    binary += "."
    while num > 0:
        """ Set a limit on the length of the str, 32 chars"""
        if binary.length >= 32:
            raise CannotRepresentAsBinaryError

        r = num * 2
        if (r >= 1):
            binary = binary + 1
            num = r - 1
        else:
            binary = binary + 0
            num = r
    return binary


def convert_float_into_bin2(num):
    if num >= 1 or num <= 0:
        raise InvalidNumberError
    binary = ""
    frac = .5
    binary += .
    while num > 0:
        """ Set the limit on the 32 chars """
        if binary.length > 32:
            raise CannotRepresentAsBinaryError
        if num >= frac:
            binary += 1
            num -= frac
        else:
            binary += 0
        frac /= 2
    return binary
