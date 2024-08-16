from typing import List


class Solution:
    def dfs(self, grid, i: int, j: int):
        # 获取网格的行数和列数
        m = len(grid)
        n = len(grid[0])

        # 判断是否超出网格边界或者当前格子是否为水（'0'）
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == '0':
            return 0

        # 将当前格子标记为已访问过的水（'0'），防止重复访问
        grid[i][j] = '0'

        # 递归地对当前格子的上下左右四个方向进行DFS
        self.dfs(grid, i + 1, j)  # 向下探索
        self.dfs(grid, i, j + 1)  # 向右探索
        self.dfs(grid, i - 1, j)  # 向上探索
        self.dfs(grid, i, j - 1)  # 向左探索

    def numIslands(self, grid: List[List[str]]) -> int:
        # 初始化岛屿数量计数器
        count = 0

        # 遍历整个网格
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # 如果发现未访问过的陆地（'1'）
                if grid[i][j] == '1':
                    # 进行DFS，将整个岛屿标记为已访问
                    self.dfs(grid, i, j)
                    # 每发现一个新的岛屿，计数器加一
                    count += 1

        # 返回最终的岛屿数量
        return count


re = Solution()
res = re.numIslands([
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
])
print(res)
