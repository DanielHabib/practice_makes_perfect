""" 1.4 """

"""
    Problem:
        Given a string return all permutations that are palindromes

    BCR: O(N)

    Steps:
        Prelim: ASCII or Unicode? assume Unicode
                Does WhiteSpace Matter? assume no
        1. Loop through once and put the amount of each letter into a
            dictionary
        2. loop through all values in dictionary making sure that all
            values are even except for one, keep note of that pivot value
            2.5. The value can be any odd value as long as there is only 1
                odd value
        3. place the pivot value in the middle
        4. Then we want to take stock, create an array of half of the values
            we have recorded in the dictionary.
        4. Now we must find all the permutations of half the array.
        5. Whats the fastest way to find all of the permutations of an
            the array? O((N-1/2)!)
        That isn't O(N) time but it is definitely an improvement over 
"""

