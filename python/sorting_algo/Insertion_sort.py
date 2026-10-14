class Solution:
    def InsertionSort(self, nums):
        n = len(nums)
        for i in range(1,n):
            key = nums[i]
            j = i - 1
            while j >= 0 and nums[j] > key:
                nums[j+1] = nums[j]
                j -= 1

            nums[j+1] = key
        return nums

nums = [3,9,5,6,8,9,10,7,1]

sol = Solution()
print(sol.InsertionSort(nums))
