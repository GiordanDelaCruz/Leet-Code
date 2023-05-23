#!/usr/bin/env python

"""solution.py: This python file contains my solution to the 'Kth Largest Element in a Stream' problem on LeetCode."""

__author__      = "Giordan Andrew"
__copyright__   = "May 22, 2023"
class KthLargest: 

    def __init__(self, k, nums):
        self.k_largest_elem = k #Determine what element to find
        self.int_stream = sorted(nums) #Sort elements in ascending order
        self.int_to_find = self.int_stream[len(self.int_stream) - self.k_largest_elem]

    def add(self, val): 
        self.int_stream.append(val) #Add element into the integer data stream
        self.int_stream = sorted(self.int_stream) #Sort new integer data stream
        self.int_to_find = self.int_stream[len(self.int_stream) - (self.k_largest_elem)]
        #DEBUGGING
        # print("Adding {} to list:\n{}".format(val, self.int_stream))

        #Check if we need to sort the new array
        # if val > self.int_to_find:
            #DEBUGGING
            # print("val = {}, int_to_find = {}".format(val, self.int_to_find))

            # self.int_stream = sorted(self.int_stream) #Sort new integer data stream
            #DEBUGGING
            # print("After sorting:\n{}".format(self.int_stream))
            # self.int_to_find = self.int_stream[len(self.int_stream) - (self.k_largest_elem)]
        
        return self.int_to_find


def main():
    solutionObj = KthLargest( 3, [4, 5, 8, 2])
    print("Third largest element = {}".format(solutionObj.add(3)))
    print("Third largest element = {}".format(solutionObj.add(5)))
    print("Third largest element = {}".format(solutionObj.add(10)))
    print("Third largest element = {}".format(solutionObj.add(9)))
    print("Third largest element = {}".format(solutionObj.add(4)))

main()