from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = float('inf')
        n = len(nums)
        for i in range(2, n):
            left, right = 0, i - 1
            while left < right:
                total = nums[left] + nums[right] + nums[i]
                if abs(total - target) < abs(ans - target):
                    ans = total
                if total < target:
                    left += 1
                else:
                    right -= 1
        return ans


re = Solution()
print(re.threeSumClosest([-1, 2, 1, -4], 1))
