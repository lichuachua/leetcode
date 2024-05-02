class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0 and n & 2863311530 == 0

re =Solution()
print(re.isPowerOfFour(16))