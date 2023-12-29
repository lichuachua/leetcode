from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r * c != len(mat) * len(mat[0]):
            return mat
        res = [0] * r
        for i in range(r):
            res[i] = [0] * c
            for j in range(c):
                res[i][j] = mat[(i * c + j) // len(mat[0])][(i * c + j) % len(mat[0])]
        return res


print(Solution().matrixReshape([[1, 2], [3, 4]], 1, 4))
