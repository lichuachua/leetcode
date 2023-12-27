class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            resTmp = [0] * (i + 1)
            resTmp[0] = 1
            resTmp[i] = 1
            for j in range(1, i):
                resTmp[j] = res[i - 1][j] + res[i - 1][j - 1]
            res.append(resTmp)
        return res
