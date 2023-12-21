#!/usr/bin/env python

"""solution.py: This python file contains my solution to the 'Buy Two Chocolates' problem on LeetCode."""

__author__      = "Giordan Andrew"
__copyright__   = "Dec 21, 2023"

class Solution:
     def buyChoco(self, prices, money):
 
        # Determine the smallest price and remove it
        min1 = min(prices)
        prices.remove(min1)

        # Determine the second smallest price
        min2= min(prices)

        # Determine if you can purchase chocolate
        if (min1 + min2) <= money:
            return money - (min1 + min2)
        else:
            return money

      
def main():
    # Test Data
    prices_a = [1,2,2]
    money_a = 3
    prices_b = [3,2,3]
    money_b = 3

    solutionObj = Solution()
    output_a = solutionObj.buyChoco(prices_a, money_a)
    output_b = solutionObj.buyChoco(prices_b, money_b)
    print("Test Case A: The output of the remaining money is {}".format(output_a))
    print("Test Case B: The output of the remaining money is {}".format(output_b))


main()