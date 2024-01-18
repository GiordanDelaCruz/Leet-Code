#!/usr/bin/env python

"""solution.py: This python file contains my solution to the 'Unique Number of Occurrences' problem on LeetCode."""

__author__      = "Giordan Andrew"
__copyright__   = "January 17, 2024"
class Solution:
    def uniqueOccurrences(self, arr):
        # Determine number of occurances for each number
        nums_counted = []
        num_of_occurances = []
        for idx, val in enumerate(arr):
            if val not in nums_counted:
                nums_counted.append(val)

                # Check if occurances of each value is unique
                curr_occurance = arr.count(val)
                if curr_occurance in num_of_occurances:
                    return False
                else:
                    # Add total number of occrances to list
                    num_of_occurances.append(curr_occurance)
        return True
    
def main():
    # Test Data
    arr_a = [1,2,2,1,1,3]
    arr_b = [1,2]
    arr_c = [-3,0,1,-3,1,1,1,-3,10,0]  

    solutionObj = Solution()
    output_a = solutionObj.uniqueOccurrences(arr_a)
    output_b = solutionObj.uniqueOccurrences(arr_b)
    output_c = solutionObj.uniqueOccurrences(arr_c)

    print("[Test Data A]: {}".format(output_a))
    print("[Test Data B]: {}".format(output_b))
    print("[Test Data C]: {}".format(output_c))

main()