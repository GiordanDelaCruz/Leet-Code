#!/usr/bin/env python

"""solution.py: This python file contains my solution to the 'Longest Palindromic Substring' problem on LeetCode."""

__author__      = "Giordan Andrew"
__copyright__   = "Dec 7, 2022"

class Solution:
    def longestPalindrome(self, s: str) -> str:

        substring_list = []
        temp_str = ''
        for i in range(0, len(s)):
            for j in range(i, len(s)):
                temp_str += s[j]
                if temp_str[0] == temp_str[len(temp_str)-1]:
                    substring_list.append(temp_str)
            temp_str =''

        print("substring_list = {}\n".format(substring_list))

        # Determine if substrings are a palindrome
        left_idx = 0
        right_idx = len(s)
        is_palindorme = True
        palindrome_list = []

        for i in range(0, len(substring_list)):
            left_idx = 0
            right_idx = len(substring_list[i]) - 1

            while left_idx <= right_idx:
                # print("left_idx = {}".format(left_idx))
                # print("right_idx = {}".format(right_idx))

                if substring_list[i][left_idx] != substring_list[i][right_idx]:
                    is_palindorme = False
                    break

                left_idx +=1
                right_idx -= 1


            if is_palindorme:
                palindrome_list.append(substring_list[i])
          
            is_palindorme = True
        
        print("palindrome_list = {}".format(palindrome_list))

        max_len = 0
        longest_pal_sub_str = ''
        for idx, val in enumerate(palindrome_list):
            if len(val) > max_len:
                max_len = len(val)
                longest_pal_sub_str = val
        
        return longest_pal_sub_str

def main(): 
    input = 'babad'
    # input = 'racecar'
    input = 'aacabdkacaa'
    solutionObj = Solution()
    output = solutionObj.longestPalindrome(input)
    print("The longest palindromic substring is {}".format(output))

main()