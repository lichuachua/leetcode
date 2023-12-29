class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        a, b = 0, 1
        i = 2
        while i <= n:
            a, b = b, (a + b) % 1000000007
            i += 1
        return b
