from typing import List


class Solution:
    def bfs(self, grid: List[List[str]], i: int, j: int) -> int:
        queue = [(i, j)]
        area = 0
        while queue:
            x, y = queue.pop(0)
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 0:
                continue
            grid[x][y] = 0  # 标记为已访问
            area += 1  # 每访问到一个陆地，面积+1
            # 将四个方向加入队列
            queue.append((x - 1, y))
            queue.append((x + 1, y))
            queue.append((x, y - 1))
            queue.append((x, y + 1))
        return area

    def maxAreaOfIsland(self, grid: List[List[str]]) -> int:
        max_area = 0

        # 遍历整个网格
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # 如果发现未访问过的陆地（'1'）
                if grid[i][j] == 1:
                    # 进行BFS，将整个岛屿标记为已访问，并更新最大面积
                    max_area = max(max_area, self.bfs(grid, i, j))
        return max_area


re = Solution()
print(re.maxAreaOfIsland([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                          [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                          [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]))
