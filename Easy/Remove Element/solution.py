#!/usr/bin/env python

"""solution.py: This python file contains my solution to the 'Adding Two Numbers' problem on LeetCode."""

__author__      = "Giordan Andrew"
__copyright__   = "Nov 23, 2022"

class Solution:
    def removeElement(self, nums, val):

        # Rewrite the elements inside nums to only contain the values that are
        # not the ones to be removed in the first k places, where k represents
        # the number of accepted elements
        val_occurance = 0
        modify_idx = 0
        for idx, elem in enumerate(nums):
            if elem != val:
                nums[modify_idx] = elem
                modify_idx += 1
            else:
                val_occurance += 1

        length_nums = len(nums) - val_occurance
        return length_nums

def main():
    solutionObj = Solution()
    list_1 = [3, 2, 2, 3]
    list_1= [0,1,2,2,3,0,4,2]
    list_1 = [0,1,2,2,3,0,4,2]
    output = solutionObj.removeElement(list_1, 2)
    print(list_1[0:output])
    print("The output is {}".format(output))
main()