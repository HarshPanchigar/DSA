# 344. Reverse String

# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

def rev(s):
    left = 0
    right = len(s) - 1

    while left <= right:
        s[left] , s[right] = s[right], s[left]

        left += 1
        right -= 1
    return s

s = ["h","e","l","l","o"]
print(rev(s))