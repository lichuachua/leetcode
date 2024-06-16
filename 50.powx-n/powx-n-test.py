class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0.0:
            return 0.0
        if n < 0:
            x = 1 / x
            n = -n
        res = 1
        while n:
            if n % 2 == 1:
                res *= x
            x *= x
            n //= 2

        return res


re = Solution()
print(re.myPow(2.00000, 10))
