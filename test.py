from math import sqrt

n = 36
res = []

for i in range(1, int(sqrt(n)) + 1):
    if n % i == 0:
        res.append(i)
        if n // i != i:
            res.append(n//i)

print(sorted(res))