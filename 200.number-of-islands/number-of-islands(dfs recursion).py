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


"""
Solution：递归+深度搜索
同695
当找到一个岛屿的起点（一个值为 '1' 的单元格）时，递归地遍历与其相连的所有陆地单元格，直到岛屿的所有部分都被访问并标记为 '0'

实现：
遍历 grid。
对于每一个字符为 '1' 的元素，遍历其上下左右四个方向，并将该字符置为 '0'，保证下次不会被重复遍历。
如果超出边界，则返回 0。
对于 (i,j) 位置的元素来说，递归遍历的位置就是 (i−1,j)、(i,j−1)、(i+1,j)、(i,j+1) 四个方向。每次遍历到底，统计数记录一次。
最终统计出深度优先搜索的次数就是我们要求的岛屿数量。

"""
