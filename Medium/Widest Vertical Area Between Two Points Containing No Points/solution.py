#!/usr/bin/env python

"""solution.py: This python file contains my solution to the 'Widest Vertical Area Between Two Points Containing No Points' problem on LeetCode."""

__author__      = "Giordan Andrew"
__copyright__   = "December 21, 2023"
class Solution:
    def maxWidthOfVerticalArea(self, points):

        x_list = []
        # Store x values into a list
        for idx, val in enumerate(points):
            x_list.append( val[0] )

        # Sort x values
        sortedList = sorted(x_list)

        # Determine the greatest difference between the x values
        greatest_x_diff = 0
        for i in range(0, len(sortedList)-1):
            curr_x_diff = abs(sortedList[i] - sortedList[i+1])
            if greatest_x_diff < curr_x_diff:
                greatest_x_diff = curr_x_diff

        return greatest_x_diff
    
def main():
    # Test data
    points_a = [[8,7],[9,9],[7,4],[9,7]]
    points_b = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]

    solutionObj = Solution()
    output_a = solutionObj.maxWidthOfVerticalArea(points_a)
    output_b= solutionObj.maxWidthOfVerticalArea(points_b)

    print("Test Case A: Widest vertical area = {}".format(output_a))
    print("Test Case B: Widest vertical area = {}".format(output_b))

main()
