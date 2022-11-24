#!/usr/bin/env python

"""solution.py: This python file contains my solution to the 'Adding Two Numbers' problem on LeetCode."""

__author__      = "Giordan Andrew"
__copyright__   = "July 29, 2022"

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # Check edge cases
        if len(nums) == 1:
            return len(nums)
    
        k=0
        currentInt = -101
        for e in nums:
            if currentInt != e:
                currentInt = e
                nums[k] = e
                k = k + 1
        return k

def main():
    solutionObj = Solution()
    listNums = [1, 1, 1, 2, 3, 3, 5]
    output = solutionObj.removeDuplicates(listNums)
    print("The length of the output arrary is {}".format(output))

main()