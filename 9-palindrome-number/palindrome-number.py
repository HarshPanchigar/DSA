class Solution:
    def isPalindrome(self, x: int) -> bool:
        result = 0
        num = x

        while x > 0 :
            ld = x % 10
            result = ( result * 10 ) + ld
            x //= 10

        return num == result