from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        up, down, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        res = []
        while True:
            # 向右
            for i in range(left, right + 1):
                res.append(matrix[up][i])
            # 向右完成，更新上边界
            up += 1
            if up > down:
                break
            # 向下
            for i in range(up, down + 1):
                res.append(matrix[i][right])
            # 向下完成，更新右边界
            right -= 1
            if right < left:
                break
            # 向左
            for i in range(right, left - 1, -1):
                res.append(matrix[down][i])
            # 向左完成，更新下边界
            down -= 1
            if down < up:
                break
            # 向上
            for i in range(down, up - 1, -1):
                res.append(matrix[i][left])
            # 向上完成，更新左边界
            left += 1
            if left > right:
                break
        return res

re = Solution()
print(re.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
