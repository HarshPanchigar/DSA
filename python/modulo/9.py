# Print All Factors of a Given Number

n = 36
fact = []

for i in range(1,n+1):
    if n % i == 0:
        fact.append(i)

print(fact)

res = []

for i in range(1 , n // 2+1):
    if n % i == 0:
        res.append(i)

res.append(n)

print(res)

