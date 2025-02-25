#!/usr/bin/env python
"""solution.py: This python file contains my solution to the 'Two Sum' problem on LeetCode.
"""
__author__ = "Giordan Andrew"
__date__   = "February 4, 2025"

class Solution:
    def twoSum(self, nums, target):
        # Keep track of seen values
        seen = {}

        for idx, elem in enumerate(nums):
            required_num = target - elem 

            if required_num not in seen:
                # Save num and its index
                seen[elem] = idx 
            else: 
                return [seen[required_num], idx]

def main():
    soluObj = Solution()

    nums = [3,2,4]
    target = 6
    result = soluObj.twoSum(nums, target)
    print("Output: {}".format(result))


main()
