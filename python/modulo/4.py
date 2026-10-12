# Problem 1 — Complete Triangle Analyzer
#
# Take three sides a, b, c.
#
# Your program should:
#
# Check whether they form a valid triangle.
# If valid:
# Equilateral → all 3 sides equal
# Isosceles → exactly 2 sides equal
# Scalene → all sides different
# Also print whether the triangle is right-angled if applicable.
#
# Covers PDF:
#  Q1 — Valid triangle
#  Q2 — Equilateral / Isosceles / Scalene
#  Right-triangle check is extra practice



def is_valid_triangle(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
        return  False

    return (a + b > c) and (a + c > b) and (b + c > a)

a, b, c = 12 ,14, 15
is_valid = is_valid_triangle(a,b,c)
print(is_valid)

if is_valid:
    if a == b and b == c and c == a:
        print("Equilateral")
    if a == b or b == c or a == c:
        print("Isosceles")
    if a != b or b != c or a != c:
        print("Scalene")