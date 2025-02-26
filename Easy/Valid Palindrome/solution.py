#!/usr/bin/env python
"""solution.py: This python file contains my solution to the 'Valid Palindrome' problem on LeetCode.
                
                Note: A solution from with [USER] on [PLATFORM] helped me understand and solve the problem.   

                Link to video: [URL_LINK]
"""
__author__ = "Giordan Andrew"
__date__   = "February 26, 2025"
import math
class Solution:
    def validPalindrome(self, s):
        # Iterate through all the characters and replace any non-alphanumeric characters
        lower_str = s.lower()
        for idx, char in enumerate(lower_str):
            if not char.isalnum():
                lower_str = lower_str.replace(char, "")


        # Check if string is a palindrome
        leftIdx = 0
        rightIdx = len(lower_str) -1
        while( leftIdx < rightIdx):
            if lower_str[leftIdx] != lower_str[rightIdx]:
                return False
            leftIdx += 1
            rightIdx -= 1

        return True

def main():
    solutionObj = Solution()

    # Test Data
    s1 = "A man, a plan, a canal: Panama"
   
    # Outputs
    output1 = solutionObj.validPalindrome(s1)

    # Display Results
    print("\n[Output1]: For s1 = {}, for it being a valid palindrome, that answer is {}".format(s1, output1))

main()