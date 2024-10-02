#!/usr/bin/env python

"""solution.py: This python file contains my solution to the 'Check If Array Pairs Are Divisible by k' problem on LeetCode.
                Note: A solution from lancertech6 on leetcode helped me understand and solve the problem.       
"""

__author__      = "Giordan Andrew"
__copyright__   = "October 1, 2024"

class Solution:
    def canArrange(self, arr, k) -> bool:
        # Frequency of occurance
        freq = [0] * k
        for idx, elem in enumerate(arr):
            remainder = ((elem%k) + k) % k
            freq[remainder] += 1
        print("freq: {}".format(freq))

        # Check for any odd remainder pairs
        if freq[0] % 2  != 0:
            # Cannot make a pair for one of the elements 
            return False

        # Check for left and right side pairs for a match
        # Note: no need to check for mod0 since we did that already when we 
        #       how many even elements we had
        for i in range(1, (k // 2) + 1):
            if freq[i] != freq[k-i]:
                return False

        return True

#----------------------------------------------------------------------------------------------------
#------------------                   TESTING & DEBUGGING                               -------------
#----------------------------------------------------------------------------------------------------
def main():
    solutionObj = Solution()

    # Test Data
    arr1 = [1,2,3,4,5,10,6,7,8,9]
    arr2 = [1,2,3,4,5,6]
    arr3 = [1,2,3,4,5,6]

    # Outputs
    output1 = solutionObj.canArrange(arr1, 5)
    output2 = solutionObj.canArrange(arr2, 7)
    output3 = solutionObj.canArrange(arr3, 10)

    # Display Results
    print("\n[Output1]: For array = {} is {}".format(arr1, output1))
    print("[Output2]: For array = {} is {}".format(arr2, output2))
    print("[Output3]: For array = {} is {}".format(arr3, output3))



main()
