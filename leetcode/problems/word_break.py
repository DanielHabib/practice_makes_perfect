

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        

        This is incorrect and requires the use of dynamic programming, we cgab=


        Notes: basically I need to check each "letter" in the word  to see if it can be broken up into a word.
              Iterate through the letters in s, building words, when a word is foubd, wipe the word and continue. if by the
              end there is an issue , then we know it is false,
              a faster option would be to create a trie to search the dictionary.
        WORD DICT => NOT AN DICTIONARY IT IS A SET
        BCR: O(Slog(D) + Dlog(D)) = > O((S + D)logD)        


        Problems: If some strange combination of letters would form a word but a previous letter is used already.
        One option, is to sort and search
        Big
        """
        # Tim Sorted!!!! Mergesort + insertion sort the checks for already sorted sections
        wordList = sorted(wordDict)
        word = ""
        for letter in s:
            word += letter
            if word in wordDict.keys():
                word = ""
                continue
        return not word


