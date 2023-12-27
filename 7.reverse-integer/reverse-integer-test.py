class Solution:
    def reverse(self, x: int) -> int:
        flag = 0
        if x < 0:
            flag = 1
            x = 0 - x
        res = 0
        while x != 0:
            res = res * 10 + x % 10
            x = x // 10
        if res > 2147483647 or res < -2147483648:
            return 0
        if flag == 1:
            res = 0 - res
        return res


re = Solution()
print(re.reverse(-2147483412))
