class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i , j = 0 , 0
        res = ""
        while i < len(word1) and j < len(word2):
            res += word1[i]
            i += 1
            res += word2[j]
            j += 1
        
        res += word2[j:]
        res += word1[i:]

        return res