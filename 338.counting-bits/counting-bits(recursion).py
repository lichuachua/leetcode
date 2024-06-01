class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)
        for i in range(n + 1):
            res[i] = self.lcc(i)
        return res

    def lcc(self, x: int) -> int:
        if x == 0:
            return 0
        return self.lcc(x & (x - 1)) + 1
