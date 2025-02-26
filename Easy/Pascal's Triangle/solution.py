#!/usr/bin/env python
"""solution.py: This python file contains my solution to the 'Pascal's Triangle' problem on LeetCode.
"""
__author__ = "Giordan Andrew"
__date__   = "February 26, 2025"

class Solution:
    def generate(self, numRows):
        pt = []

        # Base Case: static structure
        if numRows >= 1:
            pt.append([1])
        if numRows >= 2: 
            pt.append([1, 1])
        
        # Calculate the inner values in the rows
        for i in range(2, numRows):
            tempRow = []
            tempRow.append(1)
            for j in range(1, i):
                tempRow.append( pt[i-1][j] + pt[i-1][j-1] )
            tempRow.append(1)

            # Update pt
            pt.append(tempRow)

        return pt   

def main():
    solutionObj = Solution()

    # Test Data
    numRows = 5

    # Outputs
    output1 = solutionObj.generate(numRows)

    # Display Results
    print("\n[Output1]: For numRows = {}, the Pascal's Triangle is the following;\n{}".format(numRows, output1))

main()


        # THINKING
        # 0 [1]
        # 1 [1, 1]
        #    0  1

        # 2 [1, 2, 1]
        #    0  1  2 

        # 3 [1, 3, 3, 1]
        #    0  1  2  3

        # 4 [1, 4, 6, 4, 1]