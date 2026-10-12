# 14. Longest Common Prefix
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) < 0:
            return ""

        res = ""
        base = strs[0]

        for i in range(len(base)):
            for word in strs:
                if i == len(word) or word[i] != base[i]:
                    return res
            res += base[i]
        return res

obj = Solution()

strs = ["flower", "flow", "flight"]

print(obj.longestCommonPrefix(strs))