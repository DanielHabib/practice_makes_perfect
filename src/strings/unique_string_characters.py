"""
    Implement an algorithm to determine 
    if a string has all unique characters.
"""

"""
    Initial Approach:
        My first instinct here would be to create a dictionary to hold the 
        values, and to add the values into this as keys, if a value popped 
        up more than once, then it is a bad value. This would run in O(n) 
        time because we would only need to loop through the array once.
"""

class UniqueCharacters(object):
    """ Check for Unique Characters in a string"""

    @classmethod
    def initial_attempt(cls, string):
        """ Initial Attempt """
        if not string:
            """ Empty String """
            return False

        value_dict = {}
        for ltr in string:
            try:
                value_dict[ltr]
                """ String has a recurring value """
                return False
            except KeyError as err:
                value_dict[ltr] = True
        """ String is completely Unique """
        return True

    @classmethod
    def without_the_try_catch(cls, string):
        """ Attempting the same method as above without the try/catch """
        if not string:
            """ Empty String """
            return False
        value_dict = {}
        for ltr in string:
            result = value_dict.get(ltr, False)
            if result:
                return False
            else:
                value_dict[ltr] = True
        return True

    """ 
        Now solve the problem without using any additional data structures
    """                    
    @classmethod
    def without_using_data_structures(cls):
        """ Solve the problem without using additional data structures """

        """
            Thoughts: 
                Initial reaction here would be to loop through the 
                string comparing each value to each other until either a 
                a duplicate was found or the entire array was compared.
                This would run in O(n!) time which is entirely too slow.

                Looking for an alternative....

                I would think sorting and then searching for a duplicate
                would be an option, but it doesn't seem do-able without any 
                additional data structs.

                I will assume the structure can be reshaped using other 
                strings, allowing me to sort the string then search it
        """




    """
        What has been learned:
            Comparing every element in the string to every other
            element would result in O(n^2) time(a loop in a loop)
            not O(n!), O(n!) is an incredibly long time and those
            examples should be noted.

            Instead of using a dictionary to hold the spots of the
            characters, an array is just as useful and can be applied
            without helper functions or try/catch blocks. Simply using 
            and array as a checker, starting with all 0s and flicking
            the switches to 1 when they are found.

            I missed an initial consideration, whenever you are working
            with strings, think to yourself, and ask, is the string
            unicode or ASCII

            I didnt even consider the space complexity of my solutions.
            This is definitely a topic I will be reading up on.
    """




