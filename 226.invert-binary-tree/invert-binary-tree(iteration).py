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
Solution：迭代
使用队列存储结点。
遍历 反转当前结点的左右结点，之后将当前结点的左右结点入队。
其中        queue = [root]和            node = queue.pop(0)
可以换为        queue = deque([root])  # 使用 deque 作为队列     和            node = queue.popleft()  # 从队列的左端移除节点
"""
