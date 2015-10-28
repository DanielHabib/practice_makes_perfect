class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.dictionary = {}
        for val in dictionary:
            self.dictionary[self._calculate_abbr(val)] = True

    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool

        NOTES: we need a function to calculate the abbrs of all of the dictionary values.
            Maybe it would help to iterate over the dictionary and actually create a dictionary, with the abrcs?
        """
        if self._calculate_abbr(word) in self.dictionary:
            return False
        return True
        
    def _calculate_abbr(self, val):
        """Calc the abbr of a string"""
        length = len(val)
        if length > 2:
            return  "{0}{1}{2}".format(val[0], length, val[-1])
        else:
            return val        
        
        


# Your ValidWordAbbr object will be instantiated and called as such:
# vwa = ValidWordAbbr(dictionary)
# vwa.isUnique("word")
# vwa.isUnique("anotherWord")
