#!/usr/bin/env python

"""solution.py: This python file contains my solution to the 'Minimum Number of Operations to Make Array Empty' problem on LeetCode."""

__author__      = "Giordan Andrew"
__copyright__   = "January 4, 2024"
class Solution:
    def minOperations(self, nums):

        # Determine frequency for each number
        num_of_occurance = {}
        for idx, val in enumerate(nums):
            if val not in num_of_occurance:
                num_of_occurance[val] = 1
            else:
                num_of_occurance[val] += 1

        # DEBUGGING
        print("\ndict :{}".format(num_of_occurance))

        # Attempt to make array empty
        counter = 0
        while len(nums) != 0:
            for idx, val in enumerate(nums):
                print("num_of_occurance[{}] = {}".format(val, num_of_occurance[val]))
               
                # Remove key-value pair in num_of_occurance
                if num_of_occurance[val] == 0:
                    num_of_occurance.pop(idx)

                # Remove elements
                if num_of_occurance[val]%3 == 0 or ( (num_of_occurance[val] - 3)%2 == 0 and (num_of_occurance[val] - 3) >0) :
                    counter += 1
                    nums.remove(val)
                    nums.remove(val)
                    nums.remove(val)
                    num_of_occurance[val] -= 3
                    print("[3 elements removed] value = {}".format(val))
                    break
                elif num_of_occurance[val]%2 == 0:
                    counter += 1
                    nums.remove(val)
                    nums.remove(val)
                    num_of_occurance[val] -= 2
                    print("[2 elements removed] value = {}".format(val))
                    break
                else:
                    # Elements are not divisible by the available operations
                    return -1
        return counter
    

def main():
    # Test Data
    nums_a = [2,3,3,2,2,4,2,3,4]
    nums_b = [2,1,2,2,3,3]
    nums_c = [3,3]
    nums_d = [14,12,14,14,12,14,14,12,12,12,12,14,14,12,14,14,14,12,12]
    nums_e = [19,19,19,19,19,19,19,19,19,19,19,19,19]

    solutionObj = Solution()
    output_a = solutionObj.minOperations(nums_a)
    output_b = solutionObj.minOperations(nums_b)
    output_c = solutionObj.minOperations(nums_c)
    output_d = solutionObj.minOperations(nums_d)
    output_e = solutionObj.minOperations(nums_e)

    print("[Test Data A]: Minimum Operations = {}\n".format(output_a))
    print("[Test Data B]: Minimum Operations = {}\n".format(output_b))
    print("[Test Data C]: Minimum Operations = {}\n".format(output_c))
    print("[Test Data D]: Minimum Operations = {}\n".format(output_d))
    print("[Test Data E]: Minimum Operations = {}\n".format(output_e))

main()