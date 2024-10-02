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
        secondLastNum = 0
        lastNum = 0
        currSubList = []
        for i in range(0, len(nums) - 1):

            # Reset values
            currSubList.clear() 
            currSubList.append(nums[i])
            currIdx = i+1

            # Determine the strictly increasing substring for each element
            while currIdx < len(nums):
                
                print("nums[currIdx] = {}".format(nums[currIdx]))

                # Determine last and second last elements in the current subsequence
                if len(currSubList) > 1:
                    secondLastNum = currSubList[len(currSubList) -2]
                lastNum = currSubList[len(currSubList) -1]
                print("secondLastNum = {} & lastNum = {}\n".format(secondLastNum, lastNum))

                if lastNum < nums[currIdx]:
                    # Add some element to current subsquenc
                    currSubList.append(nums[currIdx])
                else:
                    # Check if currNum can be added still
                    if secondLastNum < nums[currIdx]:
                        # Replace the last element in the current subsquence with smaller value 
                        currSubList[ len(currSubList) -1] = nums[currIdx]
                     
                print("Current Subsquence = {}\n".format(currSubList))
                currIdx+=1
                
            # Determine the length of the largest increasing substring 
            currSubLength = len(currSubList)
            if currSubLength > largestSubLength:
                largestSubLength = currSubLength

        return largestSubLength
    
def main():
    # Test Data
    nums_a = [10,9,2,5,3,7,101,18]
    nums_b = [0,1,0,3,2,3]
    nums_c = [7,7,7,7,7,7,7]
    nums_d = [5,7,-24,12,13,2,3,12,5,6,35]

    solutionObj = Solution()
    output_a = solutionObj.lengthOfLIS(nums_a)
    output_b = solutionObj.lengthOfLIS(nums_b)
    output_c = solutionObj.lengthOfLIS(nums_c)
    output_d = solutionObj.lengthOfLIS(nums_d)

    print("[Test Data A]: The length of the longest increasing substring is {}".format(output_a))
    print("[Test Data B]: The length of the longest increasing substring is {}".format(output_b))
    print("[Test Data C]: The length of the longest increasing substring is {}".format(output_c))
    print("[Test Data D]: The length of the longest increasing substring is {}".format(output_d))
    

main()