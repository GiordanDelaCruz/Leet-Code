#!/usr/bin/env python

"""solution.py: This python file contains my solution to the 'Maximum Subsquence Score' problem on LeetCode."""

__author__      = "Giordan Andrew"
__copyright__   = "May 24, 2023"
from itertools import combinations
class Solution:
    def maxScore(self, nums1, nums2, k):
        max_score = 0

        # Get combinations of both integer arrays
        combin_1 = combinations(nums1, k)
        combin_2 = combinations(nums2, k)

        # Covert combinations into lists
        list_1, list_2 = [], []
        list_1.extend(combin_1)
        list_2.extend(combin_2)

        # Calculate max score 
        temp_score = 0
        for i in range(0, len(list_1)):  
            temp_score = sum(list_1[i]) * min(list_2[i])  
            
            # Update max score
            if temp_score > max_score:
                max_score = temp_score

        return max_score

            

def main():
    solutionObj = Solution()
    list_1 = [1, 3, 3, 2]
    list_2 = [2, 1, 3, 4]
    k = 3
    output = solutionObj.maxScore(list_1, list_2, k)

    print("The maximum subsquence score is {}".format(output))
main()