class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        freq = {}
        for i in nums:
            if i in freq:
                return True
            else:
                freq[i] = 1
        return False
            