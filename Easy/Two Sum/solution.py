#!/usr/bin/env python

"""solution.py: This python file contains my solution to the 'Two Sum' problem on LeetCode."""

__author__      = "Giordan Andrew"
__copyright__   = "March 28, 2022"

class Solution:
    def twoSum(self, nums, target):
        
        output = []
        seen = {}

        for idx, value in enumerate(nums):
            required_num = target - value
            
            #DEBUG
            print("current_num = {}".format(value))
            print("required_num = {}".format(required_num))
            print("seen: {}\n".format(seen))

            #check if required num exist in dict. 
            if required_num in seen:
                #return idx of current_num & required_num
                output = [seen[required_num], idx]      
                return output
            else:
                #add current_num into our prev_nums dict
                seen[value] = idx
      
#----------------------------------------------------------------------------------------------------
#------------------                   TESTING & DEBUGGING                               -------------
#----------------------------------------------------------------------------------------------------
def main():
    soluObj = Solution()

    nums = [3,2,4]
    target = 6
    result = soluObj.twoSum(nums, target)
    print("Output: {}".format(result))


main()