#!/usr/bin/env python

"""solution.py: This python file contains my solution to the 'Climbing Stairs' problem on LeetCode."""

__author__      = "Giordan Andrew"
__copyright__   = "Nov 29, 2022"

steps_memory = {1:1, 2:2}
class Solution:
    def climbStairs(self, n):
        if n in steps_memory:
            return steps_memory[n]
        else:
            steps_memory[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
            return steps_memory[n]

def main():
    solutionObj = Solution()
    input = 8
    output = solutionObj.climbStairs(input)
    print("The output is {}".format(output))
    print(steps_memory)

main()