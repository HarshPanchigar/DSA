n = [1, 2, 2, 3, 1, 2, 3]

num = len(n)

freq = {}

for i in range(num):
    freq[n[i]] = freq.get(n[i],0) + 1

print(freq)