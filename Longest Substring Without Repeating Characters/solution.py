#!/usr/bin/env python

"""solution.py: This python file contains my solution to the 'Longest Substring Without Repeating Characters' 
                problem on LeetCode."""

__author__      = "Giordan Andrew"
__copyright__   = "Nov 22, 2022"

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen_chars = {}

        # Edge cases
        if len(s) == 1:
            return 1

        # Read characters in string
        left_idx = 0
        longest = 0
        for idx, char in enumerate(s):
            # Save index of seen characters
            if char not in seen_chars:
                seen_chars[char] = idx
                sub_str_len = idx - left_idx + 1
                longest = max(longest, sub_str_len)
            else:
                # Case 1: Seen character is within window
                if seen_chars[char] in range(left_idx, idx + 1):
                    left_idx = seen_chars[char] + 1
                # Case 2: Seen character not within window
                else:
                    sub_str_len = idx - left_idx + 1
                    longest = max(longest, sub_str_len)

                # Update latest placement of seen character
                seen_chars[char] = idx
        # print(seen_chars)
       
        return longest


def main():
    solutionObj = Solution()
    input = 'abcabcbb'
    input = ' '
    input = 'au'
    input = 'dvdf'
    input = 'abcdbacd'
    input = 'abcdaababcde'
    # input = 'pwwkew'
    # input = 'abcabcdb'
    input = 'tmmzuxt'
    longest_sub_str = solutionObj.lengthOfLongestSubstring(input)
    print("The longest substring is {}".format(longest_sub_str))

main()