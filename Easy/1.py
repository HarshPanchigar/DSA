class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash = {}
        for i , num in enumerate(nums):
            res = target - num
            if res in hash:
                return [hash[res],i]
            hash[num] = i

# Object
obj = Solution()

# Input
nums = [3,2,4]
target = 6

# Call
print(obj.twoSum(nums, target))