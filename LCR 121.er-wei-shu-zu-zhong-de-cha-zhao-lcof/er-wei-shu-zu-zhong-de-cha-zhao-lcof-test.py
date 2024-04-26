from typing import List


class Solution:
    def findTargetIn2DPlants(self, plants: List[List[int]], target: int) -> bool:
        # 对角线查询：从右上角开始查询，target<当前值，列值--，target>当前值，行值++
        if len(plants) == 0:
            return False
        n = len(plants)
        m = len(plants[0])
        i, j = 0, m - 1  # i-行，j-列
        while i < n and j >= 0:
            if target == plants[i][j]:
                return True
            elif target < plants[i][j]:
                j -= 1
            else:
                i += 1
        return False


re = Solution()
print(re.findTargetIn2DPlants([[2, 3, 6, 8], [4, 5, 8, 9], [5, 9, 10, 12]], 8))
