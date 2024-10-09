#!/usr/bin/env python
"""solution.py: This python file contains my solution to the '[PROBLEM]' problem on LeetCode.
                
                Note: A solution from with violet_6 on LeetCode helped me understand and solve the problem.   
"""
__author__      = "Giordan Andrew"
__copyright__   = "October 9, 2024"

class Solution:
    def minSwaps(self, s):
        
        count_open = 0 # number of unmatched opening brackets

        # Determine number of unmatched brackets
        for idx, char in enumerate(s):
            if char == '[':
                count_open += 1
            else:
                # Reduce count if open bracket was found, and number of open brackets are not 0
                if count_open > 0:
                    count_open -= 1
        
        # Determine min number of swaps
        min_swap = (count_open + 1) // 2
        return min_swap

def main():
    solutionObj = Solution()

    # Test Data
    s1 = "][]["
    s2 = "]]][[["
    s3 = "[]"

    # Outputs
    output1 = solutionObj.minSwaps(s1)
    output2 = solutionObj.minSwaps(s2)
    output3 = solutionObj.minSwaps(s3)

    # Display Results
    print("\n[Output1]: For string = {}, the min length of swaps is {}".format(s1, output1))
    print("[Output2]: For string = {}, the min length of swaps is {}".format(s2, output2))
    print("[Output3]: For string = {}, the min length of swaps is {}".format(s3, output3))


main()
