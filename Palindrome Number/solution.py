#!/usr/bin/env python

"""solution.py: This python file contains my solution to the 'Palindrome Number' problem on LeetCode."""

__author__      = "Giordan Andrew"
__copyright__   = "April 10, 2022"

import math

class Solution:
    def isPalindrome(self, x: int) -> bool:
        palinFlag = True
        
        # Negative case
        if x < 0:
            palinFlag = False

        # Single digit case
        elif x < 10 and x > 0:
            pass
        
        # Muli-digit case
        else:
            # Get num of digits
            numOfDigits = self.getNumOfDigits(x)
            
            # Calculate the reverse number
            reverseNum = 0
            counter = numOfDigits - 1
            prevRemainder = 0
            cpyX = x
            for i in range(1, numOfDigits + 1):
                remainder = x % 10 ** i
                print("i = {}, remainder = {}".format(i, remainder))
                cpyX = cpyX - (remainder - prevRemainder)
                print("prevRemainder = {}".format(prevRemainder))
                prevRemainder = remainder
                print(cpyX)
            
            # Check if Palindrome
            if( cpyX != 0):
                print("x = {}\nreverseNum = {}".format(x, reverseNum))
                palinFlag = False
                
        return palinFlag

    def getNumOfDigits(self, x:int) -> int:
        
        # For positive values only
        numOfDigits = int(math.log10(x))+1
        
        return numOfDigits

#----------------------------------------------------------------------------------------------------
#------------------                   TESTING & DEBUGGING                               -------------
#----------------------------------------------------------------------------------------------------   
def main():
    solutionObj = Solution()
    solutionObj.isPalindrome(121)

main()
        