#!/usr/bin/env python

"""solution.py: This python file contains my solution to the 'Valid Parentheses' problem on LeetCode."""

__author__      = "Giordan Andrew"
__copyright__   = "July 29, 2022"

class Solution:
    def isValid(self, s: str) -> bool:
        # Declare variables
        isValid = True

        # Check initial constraints
        strLen = len(s)
        if strLen <= 1 or strLen > 10**4 or s.isalpha() == True or s.isdigit() == True:
            isValid = False
            return isValid

        # Check if string is valid
        stackOfBrackets = []
        entryChars = ['(', '{', "["]
        for char in s:
            if char in entryChars:
                stackOfBrackets.append(char)
            else:
                # Check if last item in the stack matches the current character in the string
                # Check if stack is not empty
                if len(stackOfBrackets) < 1:
                    isValid = False
                    return isValid

                # Pop element from stack
                stackPop = stackOfBrackets.pop()
                if stackPop == '(' and char != ")":
                    isValid = False
                    return isValid
                elif stackPop == '{' and char != "}":
                    isValid = False
                    return isValid
                elif stackPop == '[' and char != "]":
                    isValid = False
                    return isValid

        # Check if stack is empty
        if len(stackOfBrackets) != 0:
            isValid = False
            return isValid

        return isValid

def main():
    solutionObj = Solution()
    inputStr = "()[]{}"
    inputStr = "(("
    validFlag = solutionObj.isValid(inputStr)
    print("Input of {} is {}".format(inputStr, validFlag))


main()
