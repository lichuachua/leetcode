class Solution:
    def bfs(self, grid, i: int, j: int):
        queue = [(i, j)]
        while queue:
            x, y = queue.pop(0)
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == '0':
                continue
            grid[x][y] = '0'  # 标记为已访问
            # 将四个方向加入队列
            queue.append((x - 1, y))
            queue.append((x + 1, y))
            queue.append((x, y - 1))
            queue.append((x, y + 1))

    def numIslands(self, grid: List[List[str]]) -> int:
        # 初始化岛屿数量计数器
        count = 0

        # 遍历整个网格
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # 如果发现未访问过的陆地（'1'）
                if grid[i][j] == '1':
                    # 进行DFS，将整个岛屿标记为已访问
                    self.bfs(grid, i, j)
                    # 每发现一个新的岛屿，计数器加一
                    count += 1

        # 返回最终的岛屿数量
        return count


"""
Solution：迭代+广度搜索
同695
与 DFS 类似，BFS 使用队列来遍历所有相连的陆地单元格。
当找到一个岛屿的起点（一个值为 '1' 的单元格）时，递归地遍历与其相连的所有陆地单元格，直到岛屿的所有部分都被访问并标记为 '0'

实现：
遍历 grid。
对于每一个字符为 '1' 的元素，遍历其上下左右四个方向，并将该字符置为 '0'，保证下次不会被重复遍历。
如果超出边界，则返回 0。
对于 (i,j) 位置的元素来说，递归遍历的位置就是 (i−1,j)、(i,j−1)、(i+1,j)、(i,j+1) 四个方向。每次遍历到底，统计数记录一次。
最终统计出深度优先搜索的次数就是我们要求的岛屿数量。

其中        queue = [root]和            node = queue.pop(0)
可以换为        queue = deque([root])  # 使用 deque 作为队列     和            node = queue.popleft()  # 从队列的左端移除节点
"""
