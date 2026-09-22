# Sum of Digits
# Given an integer n, return the sum of all its digits.
# Example: 12345 → 15

def sum_of_degit(n):
    total = 0
    while n > 0:
        total += n % 10
        n = n // 10

    return total

num = int(input("Enter number: "))
print(sum_of_degit(num))