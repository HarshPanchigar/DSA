from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hash = {}

        for i in strs:
            key = "".join(sorted(i))
            if key not in hash:
                hash[key] = []                
            hash[key].append(i)
        return list(hash.values())

obj = Solution()

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# ["bat"],["nat","tan"],["ate","eat","tea"]
print(obj.groupAnagrams(strs))