#!/usr/bin/env python

"""solution.py: This python file contains my solution to the 'Binary Gap' problem on LeetCode."""

__author__      = "Giordan Andrew"
__copyright__   = "Oct 24, 2022"

class Solution():
    def binaryGap(self, n: int) -> int:
            bin_N = bin(n)
            max_bin_gap = 0
            temp = 0
            count_flag = False

            for i in range(2, len(bin_N)):
                if bin_N[i] == '1' and count_flag == False:
                    count_flag = True
                else:
                    temp = temp + 1
                    if bin_N[i] == '1' and count_flag == True:
                        if temp > max_bin_gap:
                            max_bin_gap = temp
                        temp = 0

            return max_bin_gap

#----------------------------------------------------------------------------------------------------
#------------------                   TESTING & DEBUGGING                               -------------
#----------------------------------------------------------------------------------------------------
def main():
    soultionObj = Solution()
    num = 22
    max_bin_gap = soultionObj.binaryGap(num)
    print("Number = {}".format(num))
    print(("Number in binary: {}\n".format(bin(num))))
    print("The largest binary gap is {}".format(max_bin_gap))


main()
