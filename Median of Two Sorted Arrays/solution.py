#!/usr/bin/env python

"""solution.py: This python file contains my solution to the 'B' problem on LeetCode.
   Note: A solution from Tushar Roy helped me in understanding and solving this problem in 
         O(log(min(x,y))) time. 
         
   Link to Video: https://www.youtube.com/watch?v=LPFhl65R7ww&t=1480s"""

__author__      = "Giordan Andrew"
__copyright__   = "Dec 5, 2022"
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):

        # Ensure nums1 is the smaller of the 2 arguments
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        len_x = len(nums1)
        len_y = len(nums2)
        low = 0
        high = len_x 

        # Use of Binary Search
        while low <= high:
            partition_x = (high + low) // 2
            partition_y =  (len_x + len_y + 1)//2 - partition_x

            # Determine values of 4 middle elements 
            max_left_x = nums1[partition_x-1] if partition_x != 0 else float('-inf')
            min_right_x = nums1[partition_x] if partition_x != len_x else float('inf')
            max_left_y = nums2[partition_y-1] if partition_y != 0 else float('-inf')
            min_right_y = nums2[partition_y] if partition_y != len_y else float('inf')

            # Check if we have partitioned into the middle of a theoretical merged array
            if max_left_x <= min_right_y and max_left_y <= min_right_x:
                # Odd number of elements
                if (len_x + len_y)%2 != 0:
                    return max(max_left_x, max_left_y)
                # Even number of elements
                else:
                    return ( max(max_left_x, max_left_y) + min(min_right_x, min_right_y) )/2

            # Move our partitions more to the left
            elif max_left_x > min_right_y:
                high = partition_x -1

            # Move our partitinon more to the right
            else:
                low = partition_x +1 
def main():
    # Test Case 1
    list_1 = [1, 3]
    list_2 = [2]
    # Test Case 2
    list_1 = [1, 2]
    list_2 = [3, 4]
    solutionObj = Solution()
    output = solutionObj.findMedianSortedArrays(list_1, list_2)
    print("The median of the merged lists is {}".format(output))

main()