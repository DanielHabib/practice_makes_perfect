"""
Given a rows x cols screen and a sentence represented by a list of words, find how many times the given sentence can be fitted on the screen.

Note:

    A word cannot be split into two lines.
    The order of words in the sentence must remain unchanged.
    Two consecutive words in a line must be separated by a single space.
    Total words in the sentence won't exceed 100.
    Length of each word won't exceed 10.
    1 ≤ rows, cols ≤ 20,000.


Input:
    rows = 2, cols = 8, sentence = ["hello", "world"]

    Output: 
    1

    Explanation:
    hello---
    world---

    The character '-' signifies an empty space on the screen.

Input:
    rows = 3, cols = 6, sentence = ["a", "bcd", "e"]

    Output: 
    2

    Explanation:
    a-bcd- 
    e-a---
    bcd-e-

    The character '-' signifies an empty space on the screen.

Input:
    rows = 4, cols = 5, sentence = ["I", "had", "apple", "pie"]

    Output: 
    1

    Explanation:
    I-had
    apple
    pie-I
    had--

    The character '-' signifies an empty space on the screen.


Input:
    sentence, given as an array of words, if empty print infinitie
    rows, an integer representing the amount of lines
    cols, and integer representing the amount of characters(including whitespace) that can fit on a line

Output:
    an integer, the number of times that the entire sentence can be put into the screen

Strategy:
    Loop Through words, and try to fill the screen with as many words as possible, in order.
Appraoch:
    Maintain a counter that increments every time we fit a full sentence into the screen.
    On loop to loop though the words.
    We will need a variable to maintain what line we are on, terminating the loop if we run out of space on the last line.


    Get the length of a sentence, Take the modulus of the n
"""

class Solution(object):

    def wordsTyping(self,sentence, rows,cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        if len(sentence) == 0:
            return float('inf')
        words = len(sentence)
        length = sum([len(x) for x in sentence])
        sentenceLength = length + words - 1
        
        currentRow = 1
        colsLeft = cols
        currentWordIndex = 0
        sentencesCompleted = 0
        while currentRow <= rows:
            remainder = 0 if currentWordIndex = 0 else sum([len(x) + 1 for x  in range(currentWordIndex, len(sentence))])
            if colsLeft >= remainder:
                colsLeft -= remainder 
                sentencesCompleted += 1
            if colsLeft >= sentenceLength:
                fullSentences = colsLeft // sentenceLength
                
                if fullSentences * sentenceLength + fullSentences - 1 > colsLeft:
                    fullSentences -= 1
            sentencesCompleted += fullSentences
            colsLeft = fullSentences * sentenceLength + fullSentences - 1
            while True:
                if currentWordIndex == len(sentence):
                    currentWordIndex = 0 
                    sentencesCompleted += 1
                if colsLeft >= len(sentence[currentWordIndex]):
                    colsLeft -= (len(sentence[currentWordIndex]) + 1)
                    currentWordIndex += 1
                else:
                    break
            currentRow += 1
            

            
        


        return sentencesCompleted



