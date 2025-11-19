#!/usr/bin/env python
"""solution.py: This python file contains my solution to the 'Keep Multiplying Found Values by Two' problem on LeetCode.
"""
__author__ = "Giordan Andrew"
__date__   = "November 18, 2024"

class Solution:
    def findFinalValue(self, nums, original):
        # Create a map of the valyes
        numsHash = {}
        for idx, elem in enumerate(nums):
            if elem not in numsHash:
                numsHash[elem] = 1
            else:
                numsHash[elem] += 1

        # Calculate the original value
        isCalculationComplete = False
        while not isCalculationComplete:
            if original in numsHash:
                original *= 2
            else:
                isCalculationComplete = True
        
        return original 
    
def main():
    solutionObj = Solution()

    # Test Data
    arr1 = [5,3,6,1,12]
    original1 = 3

    # Outputs
    output1 = solutionObj.findFinalValue(arr1, original1)

    # Display Results
    print("\n[Output1]: For array = {} with p = {} is {}".format(arr1, original1, output1))

main()
