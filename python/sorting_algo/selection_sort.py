class Solution:
    def selectionSort(self, nums):
        n = len(nums)
        for i in range(n):
            mini_index = i
            for j in range(i+1,n):
                if nums[j] < nums[mini_index]:
                    mini_index = j
            nums[i] , nums[mini_index] = nums[mini_index] , nums[i]
        return nums
        

# Test your code
nums = [2,0,2,1,1,0]

sol = Solution()
print(sol.selectionSort(nums))