#!/usr/bin/env python

"""solution.py: This python file contains my solution to the 'Merge Sorted Array' problem on LeetCode."""

__author__      = "Giordan Andrew"
__copyright__   = "Dec 2, 2022"

class Solution:
    def merge(self, nums1, m, nums2, n):

        write_index = m + n - 1
        idx_1 = m - 1
        idx_2 = n - 1

        while idx_1 >= 0 and idx_2 >= 0:
            if nums1[idx_1] > nums2[idx_2]:
                nums1[write_index] = nums1[idx_1]
                idx_1 -= 1
            else:
                nums1[write_index] = nums2[idx_2]
                idx_2 -= 1
            write_index -= 1

        if idx_2 > -1:
            nums1[0:idx_2+1] = nums2[0:idx_2+1]

        # if n>-1:
        #     nums1[0:n+1] = nums2[0:n+1]
        # temp_nums = []
        # idx_1 = 0
        # idx_2 = 0

        # print("nums_1 = {}".format(nums1))
        # print("nums_2 = {}\n".format(nums2))

        # while idx_1 < m and idx_2 < n:
        #     print("num_1[{}] = {}".format(idx_1, nums1[idx_1]))
        #     print("num_2[{}] = {}".format(idx_2, nums2[idx_2]))
        #     print("temp_nums = {}\n".format(temp_nums))

        #     if len(temp_nums) > 0:
        #         if temp_nums[0] < nums1[idx_1] or nums1[idx_1 == 0]:
        #             temp_nums.append(nums1[idx_1])
        #             nums1[idx_1] = temp_nums[0]
        #             del temp_nums[0]
        #     # Case 1: Compare elements between 2 sorted lists
        #     if nums1[idx_1] > nums2[idx_2] and idx_2 < len(nums2):
        #         temp_nums.append(nums1[idx_1])
        #         nums1[idx_1] = nums2[idx_2]
        #         idx_2 += 1
        #     elif nums1[idx_1] == 0 and idx_2 < len(nums2):
        #         nums1[idx_1] = nums2[idx_2]
        #         idx_2 += 1
        #     # Case 2: No more elements to compare
        #     # else:
        #     #     nums1[idx_1] = 0
        #     idx_1 += 1

def main():
    list_1 = [1, 2, 3, 0, 0, 0]
    list_2 = [2, 5, 6]
    solutionObj = Solution()
    solutionObj.merge(list_1, 3, list_2,  len(list_2))
    print("The output is {}".format(list_1))

main()