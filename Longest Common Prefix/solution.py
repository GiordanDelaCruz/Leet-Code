#!/usr/bin/env python

"""solution.py: This python file contains my solution to the 'Longest Common Prefix' problem on LeetCode."""

__author__      = "Giordan Andrew"
__copyright__   = "May 3, 2022"

class Solution:
    def longestCommonPrefix(self, strs):
        commonPrefix = ''
        # Edge cases
        if len(strs) == 1 or len(strs) == 0:
            commonPrefix = strs[0]
            return commonPrefix

        # Determine the shortest string inside the list 
        shortestStr = strs[0]
        for i in range(1, len(strs)):
            if len(shortestStr) > len(strs[i]):
                shortestStr = strs[i]
        # print('The shortest string is:{}'.format(shortestStr))

        # Save the prefixes of the shortest string
        prefixList = []
        ranking_dict = {}
        temp = ''
        for i in range(0, len(shortestStr)):
            temp = temp + shortestStr[i]
            ranking_dict[temp] = 0
            prefixList.append(temp)
        print("prefixList = {}".format(prefixList))
        print("ranking_dict = {}".format(ranking_dict))

        # Determine the longest prefix 
        commonPrefix = ''
        temp = ''
        lcpFlag = False
        for current_str in strs:
            print("current string = {}".format(current_str))
            for i in range(0, len(shortestStr)):
                print('shortestStr[{i}] = {ss}, currentStr[{i}] = {cs}'.format(ss=shortestStr[i], cs=current_str[i], i = i))
                if i == 0 and shortestStr[i] != current_str[i]:
                    commonPrefix = ''
                    lcpFlag = True
                    break
                elif shortestStr[i] == current_str[i]:
                    temp = temp + shortestStr[i]
                    ranking_dict[temp] = ranking_dict[temp] + 1
                elif shortestStr[i] != current_str[i]:
                    break
            temp = ''
            if lcpFlag == True:
                break
            print("ranking_dict = {}".format(ranking_dict))

        tempVal = 0
        if lcpFlag == False:
            for key in ranking_dict:
                if ranking_dict[key] >= tempVal:
                    commonPrefix = key
                    tempVal = ranking_dict[key]
                            
        return commonPrefix  

#----------------------------------------------------------------------------------------------------
#------------------                   TESTING & DEBUGGING                               -------------
#----------------------------------------------------------------------------------------------------
def main():
    soultionObj = Solution()
    # strs = ["flower","fkow"]
    # strs = ["flower","flow","flight"]
    # strs = ["reflower","flow","flight"]
    # strs = ["flower","flower","flower","flower"]
    # strs = ["cir","car"]
    strs = []
    lcp = soultionObj.longestCommonPrefix(strs)
    print(strs)
    print("The longest common prefix is: {}".format(lcp))


main()