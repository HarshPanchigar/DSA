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
nums = [64, 25, 12, 22, 11]
sol = Solution()
print(sol.selectionSort(nums))