# Problem 2 — Student & Year Analyzer
#
# Take:
#
# Three numbers a, b, c
# A year
#
# Print:
#
# The largest of the three numbers
# Whether the year is a leap year
#
# Concepts covered: 5, 6, 7

num1 = 10
num2 = 15
num3 = 20
year = 2032

if num1 > num2 and num1 > num3:
    print(f"{num1} is Largest")

elif num2 > num1 and num2 > num3:
    print(f"{num2} is Largest")

else:
    print(f"{num3} is Largest")

if year % 4 == 0 or year % 400 == 0:
    print(f"{year} is leap year.")
else:
    print(f"{year} is Not a leap year.")