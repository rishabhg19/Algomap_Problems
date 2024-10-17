class Solution:
    def fib(self, n: int) -> int:
        prev1 = 0
        prev2 = 1
        if n == 0:
            return 0
        if n == 1:
            return 1
        fibo = 0
        for i in range(2,n+1):
            fibo = prev1 + prev2
            prev1 = prev2
            prev2 = fibo
        return fibo
        