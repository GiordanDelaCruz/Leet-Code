#!/usr/bin/env python

"""solution.py: This python file contains my solution to the 'Maximum Score After Splitting a String'."""

__author__      = "Giordan Andrew"
__copyright__   = "December 22, 2023"

class Solution:
    def maxScore(self, s: str) -> int:

        leftScore, rightScore, maxScore = 0, 0, 0

        #  Split up string
        for i in range(1, len(s)):
            leftStr = s[0:i]
            rightStr = s[i:len(s)]

            # Calculte left and right score
            for idx, val in enumerate(leftStr):
                if val == "0":
                    leftScore += 1

            for idx, val in enumerate(rightStr):
                if val == "1":
                    rightScore += 1

            # Determine max score
            maxScore = max(leftScore + rightScore, maxScore)

            # Reset values
            leftScore, rightScore = 0, 0

        return maxScore

def main():
    # Test Data
    test_string = "011101"
    solutionObj = Solution()
    output = solutionObj.maxScore(test_string)

    print("The maximum score is {}".format(output))

main()