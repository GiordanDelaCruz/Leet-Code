#!/usr/bin/env python

"""solution.py: This python file contains my solution to the 'Longest Increasing Subsquence' problem on LeetCode."""

__author__      = "Giordan Andrew"
__copyright__   = "January 5, 2024"
class Solution:
    def lengthOfLIS(self, nums):
        
        # DEBUGGING
        print("***********************************************")
        print("****           NEW TEST DATA             ******")
        print("***********************************************")

        # Read through the elements in the list
        largestSubLength = 1
        currIdx = 0
        currSubLength = 0
        prevLargestNum = 0
        currSubList = []
        for i in range(0, len(nums) - 1):

            # DEBUGGING
            currSubList.clear()

            # Update index of the current element whose substring is going to be calculated
            # Reset the current strictly increasing substring length
            currSubLength = 1
            currIdx = i+1
            prevLargestNum = nums[i]
            currSubList.append(prevLargestNum)

            # Determine the strictly increasing substring for each element
            while currIdx < len(nums):
                # DEBUGGING
                print("\nCurrent Value = {}".format(prevLargestNum))
                print("Next Value = {}".format(nums[currIdx]))

                if prevLargestNum < nums[currIdx] :
                    print("currSubLength++")

                    prevLargestNum = nums[currIdx]
                    currSubLength += 1
                    
                    # DEBUGGING
                    currSubList.append(prevLargestNum)
                    print("Current Subsquence = {}".format(currSubList))
                
                currIdx += 1
                
            # Determine the length of the largest increasing substring 
            if currSubLength > largestSubLength:
                largestSubLength = currSubLength

        return largestSubLength
    
def main():
    # Test Data
    nums_a = [10,9,2,5,3,7,101,18]
    nums_b = [0,1,0,3,2,3]
    nums_c = [7,7,7,7,7,7,7]

    solutionObj = Solution()
    # output_a = solutionObj.lengthOfLIS(nums_a)
    output_b = solutionObj.lengthOfLIS(nums_b)
    # output_c = solutionObj.lengthOfLIS(nums_c)

    # print("[Test Data A]: The length of the longest increasing substring is {}".format(output_a))
    print("[Test Data B]: The length of the longest increasing substring is {}".format(output_b))
    # print("[Test Data C]: The length of the longest increasing substring is {}".format(output_c))
    
    None

main()