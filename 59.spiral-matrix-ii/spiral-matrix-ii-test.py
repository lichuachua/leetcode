from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        up, down, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        index = 1
        while True:
            # 向右
            for i in range(left, right + 1):
                # 填充上边界
                matrix[up][i] = index
                index += 1
            # 向右完成，更新上边界
            up += 1
            if up > down:
                break
            # 向下
            for i in range(up, down + 1):
                # 填充右边界
                matrix[i][right] = index
                index += 1
            # 向下完成，更新右边界
            right -= 1
            if right < left:
                break
            # 向左
            for i in range(right, left - 1, -1):
                # 填充下边界
                matrix[down][i] = index
                index += 1
            # 向左完成，更新下边界
            down -= 1
            if down < up:
                break
            # 向上
            for i in range(down, up - 1, -1):
                # 填充左边界
                matrix[i][left] = index
                index += 1
            # 向上完成，更新左边界
            left += 1
            if left > right:
                break
        return matrix


re = Solution()
print(re.generateMatrix(3))
