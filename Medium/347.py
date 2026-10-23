def topKFrequent(nums, k):
    count = {}
    freq = [[] for _ in range(len(nums)+1)]
    for i in nums:
        count[i] = 1 + count.get(i , 0)
    for key , value in count.items():
        freq[value].append(key)

    res = []
    for i in range(len(freq) -1 ,0,-1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res
nums = [1,1,1,2,2,3]
k = 2
print(topKFrequent(nums,k))