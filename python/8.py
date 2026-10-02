# Input: n = 19
# Output: true
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1

n = 19

while n != 1:
    res = 0

    while n > 0:
        digit = n % 10
        res += digit ** 2
        n //= 10
    n = res

print(res)