class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        list = []

        for i in range(2):
            for j in nums:
                list.append(j)
        return list