#!/usr/bin/env python

"""solution.py: This python file contains my solution to the 'Plus One' problem on LeetCode."""

__author__      = "Giordan Andrew"
__copyright__   = "Nov 26, 2022"
class Solution:
    def addBinary(self, a, b):
        int_a = binToInt(a)
        int_b = binToInt(b)
        sum = int_a + int_b

        str_sum = str(bin(sum))
        # print('sum: {} -> {}'.format(str_sum[2:], binToInt(str_sum[2:])))
        return str_sum[2:]

def binToInt(bin_num):
    int_num = 0
    for idx, val in enumerate(bin_num):
        # print('bin_num[{}] = {}'.format(idx, val))
        int_num += int(val) * pow(2, len(bin_num) - (1 + idx))

    # print("int num = {}".format(int_num))
    # print('\n')
    return int_num

def main():
    solutionObj = Solution()
    bin_str_1 = '11'
    bin_str_2 = '1'
    # bin_str_1 = "1010"
    # bin_str_2 = "1011"
    output = solutionObj.addBinary(bin_str_1, bin_str_2)
    print("{} + {} = {}".format(bin_str_1, bin_str_2, output))


main()