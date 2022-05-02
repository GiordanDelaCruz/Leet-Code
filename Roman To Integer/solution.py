class Solution:
    def romanToInt(self, s: str) -> int:
        # Check if invalid input 
        if len(s) > 15 or len(s) < 0:
            return None

        # Read characters in string 
        intVal= 0
        seenDict = {'I': 0, 'V': 0, 'X': 0, 'L': 0, 'C': 0, 'D': 0, 'M': 0, 
                    'IV': 0, 'IX': 0, 'XL': 0, 'XC': 0, 'CD': 0, 'CM': 0}
        skipFlag = False
        for i in range(0, len(s)):
            # Check if index should skip
            if(skipFlag):
                skipFlag = False
                continue

            # Check for special conditions
            if i != len(s)-1 :
                if s[i] == 'I': 
                    if s[i+1] == 'V':
                        seenDict['IV'] = seenDict['IV'] + 1
                        skipFlag = True
                        continue
                    elif s[i+1] == 'X':
                        seenDict["IX"] = seenDict["IX"] + 1
                        skipFlag = True
                        continue
                elif s[i] == 'X':
                    if s[i+1] == 'L':
                        seenDict['XL'] = seenDict['XL'] + 1
                        skipFlag = True
                        continue
                    elif s[i+1] == 'C':
                        seenDict["XC"] = seenDict["XC"] + 1
                        skipFlag = True
                        continue
                elif s[i] == 'C':
                    if s[i+1] == 'D':
                        seenDict['CD'] = seenDict['CD'] + 1
                        skipFlag = True
                        continue
                    elif s[i+1] == 'M':
                        seenDict["CM"] = seenDict["CM"] + 1
                        skipFlag = True
                        continue
    
            if s[i] == 'I': 
                seenDict['I'] = seenDict['I'] + 1
            elif s[i] == 'V':
                seenDict['V'] = seenDict['V'] + 1
            elif s[i] == 'X':
                seenDict['X'] = seenDict['X'] + 1
            elif s[i] == 'L':
                seenDict['L'] = seenDict['L'] + 1
            elif s[i] == 'C':
                seenDict['C'] = seenDict['C'] + 1
            elif s[i] == 'D':
                seenDict['D'] = seenDict['D'] + 1
            elif s[i] == 'M':
                seenDict['M'] = seenDict['M'] + 1
                
        # Calculate integer equivalent 
        print("seenDict: {}".format(seenDict))
        intVal = (seenDict['I']*1) + (seenDict['V']*5) + (seenDict['X']*10) + (seenDict['L']*50) + (seenDict['C']*100) + (seenDict['D']*500) + (seenDict['M']*1000) + (seenDict['IV']*4) + (seenDict['IX']*9) + (seenDict['XL']*40) + (seenDict['XC']*90) + (seenDict['CD']*400) + (seenDict['CM']*900)
                
        return intVal

def main():
    solutionObj = Solution()
    romanVal = "DCXXI"
    intVal = solutionObj.romanToInt(romanVal)

    print("Roman = {}, Integer = {}".format(romanVal, intVal))

    
main()
                    
