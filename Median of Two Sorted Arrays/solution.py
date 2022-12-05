#!/usr/bin/env python

"""solution.py: This python file contains my solution to the 'B' problem on LeetCode."""

__author__      = "Giordan Andrew"
__copyright__   = "Dec 4, 2022"
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        final_list = []
        idx_1 = 0
        idx_2 = 0
        # Merge sorted list
        while idx_1 < len(nums1) or idx_2 < len(nums2):
            try:
                if nums1[idx_1] < nums2[idx_2]:
                    final_list.append(nums1[idx_1])
                    idx_1 += 1
                else:
                    final_list.append(nums2[idx_2])
                    idx_2 += 1
            except:
                if idx_1 < len(nums1):
                    final_list.append(nums1[idx_1])
                    idx_1 += 1
                else:
                    final_list.append(nums2[idx_2])
                    idx_2 += 1

        print("The merged list is {}".format(final_list))

        # Odd number of elements
        if len(final_list)%2 != 0:
            return final_list[len(final_list)//2]
        # Even number of elements
        else:
            l_mid = final_list[(len(final_list)//2) -1]
            r_mid = final_list[(len(final_list)//2)]
            print("{}, {}".format(l_mid, r_mid))
            return (l_mid + r_mid)/2
def main():
    # Test Case 1
    list_1 = [1, 3]
    list_2 = [2]
    # Test Case 2
    list_1 = [1, 2]
    list_2 = [3, 4]
    solutionObj = Solution()
    output = solutionObj.findMedianSortedArrays(list_1, list_2)
    print("The median of the merged lists is {}".format(output))

main()