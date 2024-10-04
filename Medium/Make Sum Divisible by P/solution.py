#!/usr/bin/env python

"""solution.py: This python file contains my solution to the 'Make Sum Divisible by P' problem on LeetCode.
                Note: A solution from with aarzoo on leetcode and a solution from Code Thoughts on 
                      YouTube helped me understand and solve the problem.   

                Link to video: https://www.youtube.com/watch?v=1hjPA6YbulE    
"""

__author__      = "Giordan Andrew"
__copyright__   = "October 3, 2024"

class Solution:
    def minSubarray(self, nums, p):
        print("[nums] = {}".format(nums))
        print("[p] = {}".format(p))
        # [Case 0] : Prefix sum is of all elements is divisible by P
        total_sum = sum(nums)
        total_sum_rem_mod = total_sum % p
        print("[total_sum_rem_mod] = {}".format(total_sum_rem_mod))
        if total_sum_rem_mod == 0:
            return 0  
        else:
            # [Case 1] : Look for a subarray of elements to remove 
            min_length = len(nums) # length of subarray to remove 
            PSM_map = {0: -1}  # Prefix sum mod; used to store the indices
            prefix_sum = 0 
            for idx, num in enumerate(nums):
                prefix_sum += num
                current_PSM = prefix_sum % p # Modulo of current prefix sum
                target_mod = (current_PSM - total_sum_rem_mod + p) % p # Look for end index of the subarray to remove
                # Note: (number + p) % p
                #       This formula is used to removed negative mods

                # DEBUGGING
                print("\n[idx] = {}".format(idx))
                print("[prefix_sum] = {}".format(prefix_sum))
                print("[current_PSM] = {}".format(current_PSM))
                print("[target_mod] = {}".format(target_mod))

                if target_mod in PSM_map:
                    min_length = min(min_length, idx - PSM_map[target_mod]) # Calculate the length of the subarray from the starting index - ending index
                    print("[**min_length] = {}".format(min_length)) # DEBUGGING
                    
                PSM_map[current_PSM] = idx 
                print("[PSM_map] = {}".format(PSM_map)) # DEBUGGING
                 
        return min_length if min_length < len(nums) else -1



        



#----------------------------------------------------------------------------------------------------
#------------------                   TESTING & DEBUGGING                               -------------
#----------------------------------------------------------------------------------------------------
def main():
    solutionObj = Solution()

    # Test Data
    arr1 = [3,1,4,2] 
    arr2 = [6,3,5,2]
    arr3 = [1,2,3]
    arr4 = [1,2,3]
    arr5 = [26,19,11,14,18,4,7,1,30,23,19,8,10,6,26,3]

    p1 = 6
    p2 = 9
    p3 = 3
    p4 = 7
    p5 = 26

    # Outputs
    output1 = solutionObj.minSubarray(arr1, p1)
    # output2 = solutionObj.minSubarray(arr2, p2)
    # output3 = solutionObj.minSubarray(arr3, p3)
    # output4 = solutionObj.minSubarray(arr4, p4)
    # output5 = solutionObj.minSubarray(arr5, p5)

    # Display Results
    print("\n[Output1]: For array = {} with p = {} is {}".format(arr1, p1, output1))
    # print("[Output2]: For array = {} with p = {} is {}".format(arr2, p2, output2))
    # print("[Output3]: For array = {} with p = {} is {}".format(arr3, p3, output3))
    # print("[Output4]: For array = {} with p = {} is {}".format(arr4, p4, output4))
    # print("[Output5]: For array = {} with p = {} is {}".format(arr5, p4, output5))



main()
