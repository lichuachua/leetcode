class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x, y = self.tenToTwo(x), self.tenToTwo(y)
        res = 0
        print(x, y)
        if len(x) < len(y):
            x = [0] * (len(y) - len(x)) + x
        elif len(y) < len(x):
            y = [0] * (len(x) - len(y)) + y
        print(x, y)
        for i in range(len(x)):
            if x[i] != y[i]:
                res += 1

        return res

    def tenToTwo(self, x: int) -> List[int]:
        res = []
        while x != 0:
            res.append(x % 2)
            x = x // 2
        res.reverse()
        return res
