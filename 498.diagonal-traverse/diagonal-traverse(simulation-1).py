class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        res = []
        diagonals = []
        for j in range(n):
            i, k = 0, j
            diagonal = []
            while i < m and k >= 0:
                diagonal.append(mat[i][k])
                i += 1
                k -= 1
            diagonals.append(diagonal)

        for i in range(1, m):
            j, k = i, n - 1
            diagonal = []
            while j < m and k >= 0:
                diagonal.append(mat[j][k])
                j += 1
                k -= 1
            diagonals.append(diagonal)

        for idx, diagonal in enumerate(diagonals):
            if idx % 2 == 0:
                res.extend(diagonal[::-1])
            else:
                res.extend(diagonal)
        return res


"""
Solution：找规律
遍历：
    第一行遍历：从第一行的每个元素开始，向下和向左遍历，收集对角线上的所有元素。
    最后一列遍历：从最后一列的第二个元素开始（从第二行开始，避免重复第一个元素），向下和向左遍历，收集对角线上的所有元素。
反转偶数索引的对角线
合并结果
"""
