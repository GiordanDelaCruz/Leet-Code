#!/usr/bin/env python
"""solution.py: This python file contains my solution to the 'Maximum Sum of Distinct Subarrays With Length K' problem on LeetCode.
                
                Note: A solution from with NeetCode on YouTube helped me understand and solve the problem.   

                Link to video: https://www.youtube.com/watch?v=pT-lOE1on3M&t=622s
"""
__author__      = "Giordan Andrew"
__copyright__   = "November 28, 2024"

from collections import defaultdict


class Solution:
    def maximumSubarraySum(self, nums, k) -> int:
        res = 0
        curr_sum = 0
        freq = defaultdict(int) # Keep track of numbers

        # Sliding window
        l = 0
        for r in range(len(nums)):
            w_size = r - l + 1  # window size
            curr_sum += nums[r]
            freq[nums[r]] += 1  
            
            # Update sum, freq -> window
            if w_size > k:
                curr_sum -= nums[l]  # Remove previous num
                
                # Update freq
                freq[nums[l]] -= 1  
                if freq[nums[l]] == 0:
                    freq.pop(nums[l])
                l += 1 

            # Check for duplicated nums & proper window size
            w_size = r - l + 1 
            if len(freq) == k and w_size == k:
                res = max(res, curr_sum)
            
        return res
          
def main():
    solutionObj = Solution()

    # Test Data
    nums_1 = [1,5,4,2,9,9,9]
    k_1 = 3
    nums_2 = [4, 4, 4]
    k_2 = 3


    # Outputs
    output1 = solutionObj.maximumSubarraySum(nums_1, k_1)
    output2 = solutionObj.maximumSubarraySum(nums_2, k_2)

    # Display Results
    print("\n[Output1]: For array = {} with k = {} is {}".format(nums_1, k_1,  output1))
    print("\n[Output1]: For array = {} with k = {} is {}".format(nums_2, k_2,  output2))

main()


