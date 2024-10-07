#!/usr/bin/env python
"""solution.py: This python file contains my solution to the 'Permutation in String' problem on LeetCode.
                
                Note: A solution from with [USER] on [PLATFORM] helped me understand and solve the problem.   

                Link to video: [URL_LINK]
"""
__author__      = "Giordan Andrew"
__copyright__   = "October 4, 2024"

class Solution:
    def convertToHash(self, string):
        # Map chracters of s1
        string_characters = {}
        for idx, char in enumerate(string):
            if char not in string_characters:
                string_characters[char] = 1
            else:
                string_characters[char] += 1
        return string_characters
    def checkInclusion(self, s1, s2):
        solultionObj = Solution()
        n1 = len(s1)
        n2 = len(s2)

        if n2<n1: 
            return False
        
        freq1 = solultionObj.ConvertToHash(s1)
        freq2 =  solultionObj.ConvertToHash(s2[0:n1])
        
        if freq1==freq2: return True
        l = 1
        r = n1
        while r<n2:
            freq2[s2[l-1]]-=1
            freq2[s2[r]]+=1
            if freq1==freq2: return True
            r+=1
            l+=1
        return False

        # solObj1 = Solution()
        # # Map chracters of s1
        # s1_characters = solObj1.convertToHash(s1)
        # s2_characters = solObj1.convertToHash(s2)
        # print("\n[s1_chracters] = {}".format(s1_characters))
        # print("[s2_chracters] = {}".format(s2_characters))
        # print("[s2] = {}".format(s2))

        # # Check if characters from s1 are in sequence with s2
        # contigous_counter = 0   # Keep track of sequent characters
        # og_s1_characters = s1_characters    # Copy of original s1 characters 
        # for idx, char in enumerate(s2):
        #     print("[char] = {}".format(char))

        #     if char in s1_characters and s1_characters[char] > 0:
        #         # Start to count letters
        #         contigous_counter += 1
        #         s1_characters[char] -= 1
        #         print("*[s1_chracters] = {}".format(s1_characters))
        #     else:
        #         if contigous_counter >= 1:
        #             # Reset everything
        #             contigous_counter = 0
        #             s1_characters = og_s1_characters

        #     print("[contigous_counter] = {}".format(contigous_counter))
            
        #     # Exit loop if all permutation of s1 was found in s2 
        #     if contigous_counter == len(s1):
        #         return True
            
        # return False

def main():
    solutionObj = Solution()

    # Test Data
    sa_1 = "ab"
    sa_2 = "eidbaooo"

    sb_1 = "ab"
    sb_2 = "eidboaoo"

    sc_1 = "hello"
    sc_2 = "ooolleoooleh"

    sd_1 = "adc"
    sd_2 = "dcda"
    # Outputs
    output1 = solutionObj.checkInclusion(sa_1, sa_2)
    output2 = solutionObj.checkInclusion(sb_1, sb_2)
    # output3 = solutionObj.checkInclusion(sc_1, sc_2)
    output4 = solutionObj.checkInclusion(sd_1, sd_2)

    # Display Results
    print("\n[OutputA]: For s1 = {} and s2 = {}, s1 contains permutations is a substring of s2 {}".format(sa_1, sa_2, output1))
    print("[OutputB]: For s1 = {} and s2 = {}, s1 contains permutations is a substring of s2 {}".format(sb_1, sb_2, output2))
    # print("[OutputC]: For s1 = {} and s2 = {}, s1 contains permutations is a substring of s2 {}".format(sc_1, sc_2, output3))
    print("[OutputD]: For s1 = {} and s2 = {}, s1 contains permutations is a substring of s2 {}".format(sd_1, sd_2, output4))

main()
