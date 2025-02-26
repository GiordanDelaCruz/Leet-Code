#!/usr/bin/env python
"""solution.py: This python file contains my solution to the 'Pascal's Triangle II' problem on LeetCode.
"""
__author__ = "Giordan Andrew"
__date__   = "February 26, 2025"

class Solution:
    def getRow(self, rowIndex):
        pt = []

        # Base case: static structure
        if rowIndex >= 0:
            pt.append([1])
        if rowIndex >= 1:
            pt.append([1, 1])

        # Calculate inner values
        for row in range(2, rowIndex + 1):
            tempArr = []
            tempArr.append(1)
            for col in range(1, row):
                tempArr.append( pt[row-1][col] + pt[row-1][col-1])
            tempArr.append(1)

            # Update pascal triangle
            pt.append(tempArr)

        return pt[rowIndex]
    
def main():
    solutionObj = Solution()

    # Test Data
    rowIndex = 3

    # Outputs
    output1 = solutionObj.getRow(rowIndex)

    # Display Results
    print("\n[Output1]: For rowIndex = {}, the {}th row in the Pascal's Triangle is the following;\n{}".format(rowIndex, rowIndex, output1))

main()

     # 0 [1]
    # 1 [1, 1]
    # 2 [1, 2, 1]


    # 3 [1, 3, 3, 1]
