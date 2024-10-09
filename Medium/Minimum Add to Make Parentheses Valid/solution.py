#!/usr/bin/env python
"""solution.py: This python file contains my solution to the 'Minimum Add to Make Parentheses Valid' problem on LeetCode.
"""
__author__      = "Giordan Andrew"
__copyright__   = "October 9, 2024"

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        stack = [] # Keep track of non-matched characters
        for idx, char in enumerate(s):
            # Check if match inside the stack was found
            if stack and stack[-1] == '(' and char == ')':
                stack.pop()
            else:
                stack.append(char)
          
        return len(stack)
    
def main():
    solutionObj = Solution()

    # Test Data
    s1 = "())"
    s2 = "((("

    # Outputs
    output1 = solutionObj.minAddToMakeValid(s1)
    output2 = solutionObj.minAddToMakeValid(s2)

    # Display Results
    print("\n[Output1]: For string = {} the minimum number of brackets needed to make it balanced is {}".format(s1, output1))
    print("[Output2]: For string = {} the minimum number of brackets needed to make it balanced is {}".format(s2, output2))

main()
