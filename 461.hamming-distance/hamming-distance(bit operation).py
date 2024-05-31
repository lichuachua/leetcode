class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x = x ^ y
        res = 0
        while x > 0:
            if x & 1 == 1:
                res += 1
            x = x >> 1
        return res
