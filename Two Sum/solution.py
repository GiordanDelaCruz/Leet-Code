# LeetCode
# Question 1: Solution
class Solution:
    def twoSum(self, nums, target):
        
        output = []
        seen = {}

        for idx, value in enumerate(nums):
            required_num = target - value
            
            #DEBUG
            print("current_num = {}".format(value))
            print("required_num = {}".format(required_num))
            print("seen: {}\n".format(seen))

            #check if required num exist in dict. 
            if required_num in seen:
                #return idx of current_num & required_num
                output = [seen[required_num], idx]      
                return output
            else:
                #add current_num into our prev_nums dict
                seen[value] = idx
      

def main():
    soluObj = Solution()

    nums = [3,2,4]
    target = 6
    result = soluObj.twoSum(nums, target)
    print("Output: {}".format(result))


main()