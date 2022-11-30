#!/usr/bin/env python

"""solution.py: This python file contains my solution to the 'Climbing Stairs' problem on LeetCode."""

__author__      = "Giordan Andrew"
__copyright__   = "Nov 29, 2022"
class Solution:
    def climbStairs(self, n):
        # Edge cases
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return self.climbStairs(n-1) + self.climbStairs(n-2)

def main():
    solutionObj = Solution()
    input = 4
    output = solutionObj.climbStairs(input)
    print("The output is {}".format(output))