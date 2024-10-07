#!/usr/bin/env python
"""solution.py: This python file contains my solution to the 'Minimum String Length After Removing Substrings' problem on LeetCode.
"""
__author__      = "Giordan Andrew"
__copyright__   = "October 5, 2024"

class Solution:
    def minLength(self, s: str) -> int:
        # Remove AB or CD characters
        removeFlag = True
        while removeFlag:
            if 'AB' in s:
                s = s.replace("AB", "")
            elif 'CD' in s:
                s = s.replace("CD", "")      
            else:
                removeFlag = False
        
        return len(s) 

def main():
    solutionObj = Solution()

    # Test Data
    s1 = "ABFCACDB"
    s2 = "ACBBD"

    # Outputs
    output1 = solutionObj.minLength(s1)
    output2 = solutionObj.minLength(s2)

    # Display Results
    print("\n[Output1]: For string = {}, the minimum length after removing 'AB' and 'CD' characters are {}".format(s1, output1))
    print("[Output2]: For string = {}, the minimum length after removing 'AB' and 'CD' characters are {}".format(s2, output2))

main()
