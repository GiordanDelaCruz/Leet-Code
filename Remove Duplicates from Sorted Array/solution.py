class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # Check edge cases
        if len(nums) == 1:
            return len(nums)

        # Determine how many duplicates exist in the list
        # for i in range(len(nums)-2, -1, -1):
        #     # Remove the dulicated element from list
        #     if nums[i] == nums[i+1]:
        #         nums.remove(nums[i])
        # print(nums)

        k=0
        currentInt = -101
        for e in nums:
            if currentInt != e:
                currentInt = e
                nums[k] = e
                k = k + 1
        return k

        # return len(nums)

def main():
    solutionObj = Solution()
    listNums = [1, 1, 1, 2, 3, 3, 5]
    output = solutionObj.removeDuplicates(listNums)
    print("The length of the output arrary is {}".format(output))

main()