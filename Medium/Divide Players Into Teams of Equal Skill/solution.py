#!/usr/bin/env python
"""solution.py: This python file contains my solution to the 'Divide Players Into Teams of Equal Skill' problem on LeetCode.
"""
__author__      = "Giordan Andrew"
__copyright__   = "October 4, 2024"

class Solution:
    def dividePlayers(self, skill):
        # Sort the skill of players
        players = sorted(skill)
        print("\n[players] = {}".format(players))

        # Pair up the teams
        left = len(players) - 1
        right = 0
        teams = {}
        while right < left:
            teams[right] = [ players[right], players[left] ]
            right += 1
            left -= 1
        print("[teams] = {}".format(teams))

        # Check if all teams are of equal skill
        total_skill = teams[0][0] + teams[0][1]
        chemistry_arr = []
        print("[total_skill] = {}".format(total_skill))
        for idx, team in enumerate(teams):
            chemistry_arr.append(teams[idx][0] * teams[idx][1])
            current_team_skill = teams[idx][0] + teams[idx][1]
            if current_team_skill != total_skill:
                return -1
        
        # Calcualte total chemistry
        total_chemistry = sum(chemistry_arr)
        return total_chemistry

def main():
    solutionObj = Solution()

    # Test Data
    arr1 = [3,2,5,1,3,4]
    arr2 = [3,4]
    arr3 = [1,1,2,3]

    # Outputs
    output1 = solutionObj.dividePlayers(arr1)
    output2 = solutionObj.dividePlayers(arr2)
    output3 = solutionObj.dividePlayers(arr3)

    # Display Results
    print("\n[Output1]: For array = {} is {}".format(arr1, output1))
    print("[Output2]: For array = {} is {}".format(arr2, output2))
    print("[Output3]: For array = {} is {}".format(arr3, output3))

main()
