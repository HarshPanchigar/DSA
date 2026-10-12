# Count the Number of Digits

n = 5873

count = 0
while n > 0:
    count += 1
    n //= 10

print(count)

