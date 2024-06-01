class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)
        for i in range(n + 1):
            tmp = self.tenToTwo(i)
            res[i] = tmp.count(1)
        return res

    def tenToTwo(self, x: int) -> List[int]:
        res = []
        while x != 0:
            res.append(x % 2)
            x = x // 2
        res.reverse()
        return res
