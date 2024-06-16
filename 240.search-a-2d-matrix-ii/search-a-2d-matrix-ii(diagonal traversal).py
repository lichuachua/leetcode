class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)  # 行数
        m = len(matrix[0])  # 列数
        i, j = 0, m - 1  # 初始化行和列的索引

        while i < n and j >= 0:
            if target == matrix[i][j]:
                return True
            elif target < matrix[i][j]:
                j -= 1  # 目标值小于当前值，向左移动一列
            else:
                i += 1  # 目标值大于当前值，向下移动一行

        return False  # 遍历完所有可能的行和列后仍未找到目标值


"""
Solution:对角线遍历
对角线查询：从右上角开始查询，target<当前值，列值--，target>当前值，行值++
"""
