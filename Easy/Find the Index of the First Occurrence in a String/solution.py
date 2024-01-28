#!/usr/bin/env python

"""solution.py: This python file contains my solution to the 'Find the Index of the First Occurrence 
                in a String' problem on LeetCode."""

__author__      = "Giordan Andrew"
__copyright__   = "January 27, 2024"
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1

def main():
    # Test Data
    haystack_a = "sadbutsad"
    needle_a = "sad"
    haystack_b = "leetcode"
    needle_b = "leeto"

    solutionObj = Solution()
    output_a = solutionObj.strStr(haystack_a, needle_a)
    output_b = solutionObj.strStr(haystack_b, needle_b)

    print("[Test Data A]: First occurance = {}".format(output_a))
    print("[Test Data B]: First occurance = {}".format(output_b))

main()