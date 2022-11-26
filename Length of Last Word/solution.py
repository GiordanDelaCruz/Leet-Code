#!/usr/bin/env python

"""solution.py: This python file contains my solution to the 'Length of Last WOrd' problem on LeetCode."""

__author__      = "Giordan Andrew"
__copyright__   = "Nov 24, 2022"
class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        word_list = s.split()
    
        return len(word_list[-1])

def main():
    solutionObj = Solution()
    input = "Hello World"
    input = "   fly me   to   the moon  "
    input = "luffy is still joyboy"
    output = solutionObj.lengthOfLastWord(input)
    print("The last word is {}".format(output))

main()
