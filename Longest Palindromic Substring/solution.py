#!/usr/bin/env python

"""solution.py: This python file contains my solution to the 'Longest Palindromic Substring' problem on LeetCode.
    Note: A solution from Nick White helped me in understanding and solving this problem in 
         O(n^(2)) time. 
         
   Link to Video: https://www.youtube.com/watch?v=y2BD4MJqV20"""
__author__      = "Giordan Andrew"
__copyright__   = "Dec 7 - Dec 9, 2022"

class Solution:
    def longestPalindrome(self, s: str) -> str:

        # Edge case
        if len(s) == 1:
            return s
        elif s == None:
            return ''

        start, end = 0, 0

        for i in range(0, len(s)):
            len_1 = expandInMiddle(s, i, i) #even strings
            len_2 = expandInMiddle(s, i, i+1) #odd strings
            max_len = max(len_1, len_2)
            
            if max_len >  end - start:
                start = i - (max_len - 1)//2
                end = i + max_len//2
                print("start = {}".format(start))
                print("end = {}".format(end))

        return s[start:end+1]

def expandInMiddle(s, left, right):
    if(s == None or left > right): return 0

    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left -1


def main(): 
    input = 'babad'
    # input = 'racecar'
    input = 'aacabdkacaa'
    input = 'gjkkjgs'
    solutionObj = Solution()
    output = solutionObj.longestPalindrome(input)
    print("The longest palindromic substring is {}".format(output))

main()