from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        rowIndex += 1
        res = []
        for i in range(rowIndex):
            resTmp = [0] * (i + 1)
            resTmp[0] = 1
            resTmp[i] = 1
            for j in range(1, i):
                resTmp[j] = res[i - 1][j] + res[i - 1][j - 1]
            res.append(resTmp)
        return res[rowIndex - 1]


re = Solution()
print(re.getRow(5))
