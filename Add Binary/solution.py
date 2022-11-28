#!/usr/bin/env python

"""solution.py: This python file contains my solution to the 'Plus One' problem on LeetCode."""

__author__      = "Giordan Andrew"
__copyright__   = "Nov 26, 2022"
class Solution:
    def addBinary(self, a, b):
        idx_1 = len(a) - 1
        idx_2 = len(b) - 1
        col_sum = 0
        carry = 0
        str_sum = ''

        while idx_1 >= 0 or idx_2 >= 0:
            num_1 = int(a[idx_1]) if idx_1 >= 0 else 0
            num_2 = int(b[idx_2]) if idx_2 >= 0 else 0

            col_sum = (num_1 + num_2 + carry) % 2
            carry = 1 if (num_1 + num_2 + carry) > 1 else 0
            str_sum += str(col_sum)
            idx_1 -= 1
            idx_2 -= 1

        # Check if the last carry should be added to the sum
        if carry == 1: 
            str_sum += str(carry)

        return str_sum[::-1]


def main():
    solutionObj = Solution()
    bin_str_1 = '11'
    bin_str_2 = '1'
    bin_str_1 = "1010"
    bin_str_2 = "1011"
    output = solutionObj.addBinary(bin_str_1, bin_str_2)
    print("{} + {} = {}".format(bin_str_1, bin_str_2, output))


main()