n = 1634
add = len(str(n))
result = 0
num = n

while n > 0:
    digit = n % 10
    result += digit ** add
    n //= 10

print(result == num)