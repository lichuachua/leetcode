from typing import List


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
        print(matrix)


re = Solution()

print(re.rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
