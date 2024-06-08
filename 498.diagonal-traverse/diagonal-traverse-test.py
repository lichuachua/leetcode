from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows, cols = len(mat), len(mat[0])
        x, y = 0, 0
        ans = []

        for i in range(rows * cols):
            ans.append(mat[x][y])

            if (x + y) % 2 == 0:
                # 最后一列
                if y == cols - 1:
                    x += 1
                # 第一行
                elif x == 0:
                    y += 1
                # 右上方向
                else:
                    x -= 1
                    y += 1
            else:
                # 最后一行
                if x == rows - 1:
                    y += 1
                # 第一列
                elif y == 0:
                    x += 1
                # 左下方向
                else:
                    x += 1
                    y -= 1
        return ans

res = Solution()
print(res.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]))