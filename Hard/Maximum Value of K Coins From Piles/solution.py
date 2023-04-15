#!/usr/bin/env python

"""solution.py: This python file contains my solution to the 'Maximum Value of K Coins From Piles' problem on LeetCode."""

__author__      = "Giordan Andrew"
__copyright__   = "April 15, 2023"
from collections import deque

class Solution:
    def maxValueOfCoins(self, piles, k: int):
        # Case 1: Only 1 pile
        if len(piles) == 1:
            max_value = 0
            for i in range(0, k):
                max_value += piles[0][i]
            return max_value

        # Case 2: More than 1 pile
        # Create stack for piles
        dict_of_stacks = {}
        for i in range(0, len(piles)):
            dict_of_stacks[i] = deque()
            for j in range(0, len(piles[i])):
                dict_of_stacks[i].append(piles[i][j])

        # Determine the max value for coins
        current_num_coins = 0
        temp_max = 0
        while current_num_coins != k:
            temp_max += max(dict_of_stacks[0], dict_of_stacks[1])


        
        pass


def main():
    solutionObj = Solution()
    piles = [ [1, 100, 3], [7, 8, 9]]
    k = 2
    output = solutionObj.maxValueOfCoins(piles, k)
    print("The maximum value is {} for {} coins".format(output, k))

main()