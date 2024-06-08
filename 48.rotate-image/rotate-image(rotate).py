class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # 起始点范围为 0 <= i < n // 2 , 0 <= j < (n + 1) // 2

        for i in range(n // 2):
            for j in range((n + 1) // 2):
                matrix[i][j], matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1] = \
                matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1], matrix[i][j]


"""
Solution:找规律，交换旋转
找规律，可以发现示例1中，2 6 8 4的位置按照顺时针旋转了（2 到了6 的位置，6 到了8 的位置等）
对于矩阵中第 i 行的第 j 个元素，在旋转后，它出现在倒数第 i 列的第 j 个位置。
matrixnew[j][n−i−1]=matrix[i][j]。
matrixnew[j][n−i−1] 的点经过旋转移动到了matrix[n−i−1][n−j−1] 的位置。
matrix[n−i−1][n−j−1] 位置上的点经过旋转移动到了matrix[n−j−1][i] 的位置。
matrix[n−j−1][i] 位置上的点经过旋转移动到了最初的matrix[i][j] 的位置。
形成了一个闭合的循环
"""
