# Take one integer n and print:
#
# Whether it is positive, negative, or zero
# Whether it is even or odd
# Whether it is divisible by 5
# Whether it is divisible by both 3 and 5
#
# Concepts covered: 1, 2, 3, 4


num = int(input('Enter A Number : '))

print("\nWhether it is positive, negative, or zero : ")
if num > 0 :
    print('number is positive')
elif num < 0:
    print('number is negative')
else:
    print('number is zero')

print("\nWhether it is even or odd : ")
if num % 2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")

print("\nWhether it is divisible by 5 : ")
if num % 5 == 0:
    print("Yes")
else:
    print("NO")

print("\nWhether it is divisible by both 3 and 5 :")
if num % 3 == 0 and num % 5 == 0:
    print("Yes")
else:
    print("No")