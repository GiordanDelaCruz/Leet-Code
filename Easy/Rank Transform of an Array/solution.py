#!/usr/bin/env python

"""solution.py: This python file contains my solution to the 'Rank Transform of an Array' problem on LeetCode.
                Note: A solution from as_313 on LeetCode helped me understand and solve the problem.
"""

__author__      = "Giordan Andrew"
__copyright__   = "Oct 2, 2024"

class Solution:
    def arrayRankTransform(self, arr):
        # Sort values and remove any duplicates 
        values_to_rank = sorted(list(set(arr)))
        print("[values_to_rank] : {}".format(values_to_rank))
        
        # Calculate rank
        rank = {}
        for idx, elem in enumerate(values_to_rank):
            rank[elem] = idx + 1

        # Create a ranking for each element
        ranking = []   
        for idx, elem in enumerate(arr):
            ranking.append(rank[elem])
        print("[ranking] : {}".format(ranking))

        return ranking
      
def main():
    solutionObj = Solution()

    # Test Data
    arr1 = [40,10,20,30]
    arr2 = [100,100,100]
    arr3 = [37,12,28,9,100,56,80,5,12]

    # Outputs
    output1 = solutionObj.arrayRankTransform(arr1)
    output2 = solutionObj.arrayRankTransform(arr2)
    output3 = solutionObj.arrayRankTransform(arr3)

    # Display results
    print("\n[Output1]: For array = {}, the ranking is {}".format(arr1, output1))
    print("[Output1]: For array = {}, the ranking is {}".format(arr2, output2))
    print("[Output1]: For array = {}, the ranking is {}".format(arr3, output3))


main()