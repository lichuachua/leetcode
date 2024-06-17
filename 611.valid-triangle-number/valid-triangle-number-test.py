from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        for i in range(2, n):
            left, right = 0, i - 1
            while left < right:
                if nums[left] + nums[right] <= nums[i]:
                    left += 1
                else:
                    ans += (right - left)
                    right -= 1
        return ans


re = Solution()
print(re.triangleNumber([2, 2, 3, 4]))
