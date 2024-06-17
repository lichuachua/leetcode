from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        res = 0
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            res = max(area, res)
            # 小的那条边进行移动
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return res


re = Solution()
print(re.maxArea([1,8,6,2,5,4,8,3,7]))