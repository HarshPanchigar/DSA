class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i , j = 0 , 0
        res = ""
        while i < len(word1) and j < len(word2):
            res += word1[i]
            res += word2[j]
            i += 1
            j += 1

        res += word1[i:]
        res += word2[j:]

        return res
    
word1 = "abcd"
word2 = "pq"
sol = Solution()
print(sol.mergeAlternately(word1,word2))
# Output: "apbqcr"