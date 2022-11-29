#!/usr/bin/env python

"""solution.py: This python file contains my solution to the 'Sqrt(x)' problem on LeetCode."""

__author__      = "Giordan Andrew"
__copyright__   = "Nov 28, 2022"
class Solution:
    def mySqrt(self, x):
        
        # Edge cases
        if x == 0 or x == 1:
            return x

        low, high = 0, x
        mid = (low + high)//2
        
        while True:
            # Update value of mid 
            mid = (low + high)//2
            
            if mid * mid <= x < (mid+1) * (mid+1):
                return mid
            elif mid * mid > x:
                high = mid -1
            else:
                low = mid + 1
          
            

def main():
    solutionObj = Solution()
    input = 15
    output = solutionObj.mySqrt(input)
    print("The square root of {} is {}".format(input, output))

main()