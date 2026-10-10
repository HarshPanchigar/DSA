class Solution:
    def fun(self,num):
        if num == 0 or num == 1:
            return num
        return self.fun(num - 1) + self.fun(num - 2)

    def fib(self, n: int) -> int:
        ans = self.fun(n)
        return ans
        