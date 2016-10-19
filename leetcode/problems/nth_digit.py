'''
Find the nth digit of the infinite integer sequence: 1,2,3,4,5,6,7.....

3 -> 3
1,2,3

11 -> 0
1,2,3,4,5,6,7,8,9,10.....
0 is the eleventh element

Axiums: n < 2**31, sequence continues perfectly,
Assumptions: type int not strings, memory is not an issue

Notes:
    We could start at the beginning of the sequence, maintaining how many digits we have seen so far. 
    Once we know the next number will contain the digit, we can walk through it in reverse and find the digit we are looking for. Runtime will be linear: O(N). 
    Since we know that n could be as large as n^31 ~ 2 Billion bits 2/8 Gigabytes.


    Can we skip any values when computing the nth digit?

    how many digits are between:
         1-9 => 9, 
         10-99 => 89 * 2 + 9,
         100-999 => 899 * 3 + (187)= 2884,
         1000-9999 => 8999* 4,
         10000-99999 => 89999 * 5,
         ....... => ............,
         xxxxx-yyyyy => 899999999 * 8    
     n = 10,000 => 8999 + 899

n = 500
1,2,3,4,5,6,7,8,9,10    
       
n > 9, n > 187, n < 2884

Range = ~~187 - 2884~~ = range actually = 100 - 1000
everyNumberHas 3 Digits
check mid: 550. (550 - 100) * 3 + 187 = 1537  |||| Repeat Binary Search but looking lower the ceil to 550


    1. Build The range Array: Constant Time/Space Since there is an upper bound on the digit we are looking for (2^31) O(1)
    2. Find the Range: Constant Time/Space This step doesnt use any extra space and traverses an container of constant size
    3. Binary Search for solution.: Runs in logarithmic time since we are conducting binary search between a fixed interval, and constant space because the number of variables we are mainting is fixed
        a. Stop Criteria would be when the value is less than everyNumberHasXDigits below  n =500 if x> 497 and x <= 499 In this case
    
Variables to keep track of: 
     n = input
     rangeMap = Dictionary that maps a range to the number of digits prior to it
     floor, ceil = for conducting binary search
     numberOfDigitsInEveryNumber = This will allow us to know the number of digits in every number in a specific range
 


EX: 
14 => 1,2,3,4,5,6,7,8,9,10,11,12   



Errors:
    Bsearch issues
	Improperly updated variables on every iteration
        Inequalities weren't correct
    Generating the Range
        I messed up the terms that I could generate the range with. I was basing my range off of certain values, but I was supposed to be deciding which range to take off of different values


    I think there is a much fast way to do this using bits and leveraging that 8 bits have 2^8 possibilities

'''
from collections import deque
class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 10: return n

        floor, ceil, digits, digitsToFloor = self.generateRange(n)

        number, remainingDigits = self.bsearch(n, floor, ceil, digits, digitsToFloor)

        resultingDigit = self.extractDigitFromNumber(number, remainingDigits)

        return resultingDigit

    @staticmethod
    def extractDigitFromNumber(number, remainingDigits):
        # number += 1
        digits = deque()
        x = 1
        while number >= 1:
            digits.appendleft(number % 10)
            number = number //  10
        return digits[remainingDigits - 1]

    @staticmethod
    def generateRange(n):
        floor, ceil = 1, 10
        c = 0
        numberOfDigits = 1     
        digitsInRangeOfFloor = 0
        digitsInRangeOfCeil = 0
        while n >= digitsInRangeOfCeil:
            digitsInRangeOfFloor += numberOfDigits * (floor * 9 - c)
            floor = int(ceil)
            numberOfDigits += 1
            ceil *= 10
            c = 1
 	    digitsInRangeOfCeil = digitsInRangeOfFloor + numberOfDigits * (ceil - floor)
        return floor, ceil, numberOfDigits, digitsInRangeOfFloor
   
    @staticmethod
    def bsearch(n, floor, ceil, digits, digitsToFloor):
        while floor <= ceil: # Check This
            mid = (ceil + floor) // 2
            digitsToMid = (mid - floor) * digits + digitsToFloor
            remainingDigits = n - digitsToMid

            if remainingDigits > 0 and remainingDigits <= digits:
                return mid, remainingDigits
            elif remainingDigits > 0:
                digitsToFloor = digitsToMid + digits
                floor = mid + 1
            else:
                ceil = mid - 1

        raise Exception('Shouldnt ever Hit this')


