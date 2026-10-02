# Check if a Number is Palindrome or Not
n = 1221
result = 0
num = n

while num > 0:
    digit = num % 10
    result = (result * 10) + digit
    num //= 10

print(n == result)