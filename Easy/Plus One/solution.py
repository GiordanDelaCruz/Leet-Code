#!/usr/bin/env python

"""solution.py: This python file contains my solution to the 'Plus One' problem on LeetCode."""

__author__      = "Giordan Andrew"
__copyright__   = "Nov 26, 2022"
class Solution:
    def plusOne(self, digits):
        num = 0
        for idx, val in enumerate(digits):
            num += val * pow(10, len(digits)-(idx+1))

        num += 1
        new_list = []
        for idx, val in enumerate(str(num)):
            new_list.append(int(val))

        return new_list
def main():
    solutionObj = Solution()
    input = [1,2,3]
    # input = [9]
    input = [2, 9, 9]
    output = solutionObj.plusOne(input)
    print("The output is {}".format(output))

main()
