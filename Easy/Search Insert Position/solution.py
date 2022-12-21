#!/usr/bin/env python

"""solution.py: This python file contains my solution to the 'Adding Two Numbers' problem on LeetCode."""

__author__      = "Giordan Andrew"
__copyright__   = "Nov 24, 2022"
class Solution:
    def searchInsert(self, nums, target):

        # Edge case
        if len(nums) == 1:
            return 0 if nums[0] >= target else 1

        m_idx = len(nums)//2
        middle_elem = nums[m_idx]
        print(middle_elem)

        # Case 1: Target is equal to middle element
        if target == middle_elem:
            print("Case 1:")
            return m_idx
        # Case 2: Target is found to the left of the middle element
        elif target < middle_elem:
            print("Case 2:\n")
            for idx in range(0, m_idx):
                if target == nums[idx]:
                    return idx
                elif target < nums[idx] and idx == 0:
                    return 0
                elif target > nums[idx] and target < nums[idx+1]:
                    return idx+1

        # Case 3: Target is found to the right of the middle element
        else:
            print("Case 3:\n")
            # for idx, val in enumerate(nums, m_idx):
            for idx in range(m_idx, len(nums)):
                if target == nums[idx]:
                    return idx
                elif target > nums[idx] and idx == len(nums) - 1:
                    return len(nums)
                elif target > nums[idx] and target < nums[idx+1]:
                    return idx+1

def main():
    solutionObj = Solution()
    list_1 = [1,3,5,6]
    output = solutionObj.searchInsert(list_1, 0)

    print("Returned index = {}.".format(output))
main()