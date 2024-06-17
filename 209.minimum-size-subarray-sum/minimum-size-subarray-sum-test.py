from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        ans = n + 1
        left, right = 0, 0
        window_sum = 0
        while right < n:
            window_sum += nums[right]
            while window_sum >= target:
                ans = min(ans, right - left + 1)
                window_sum -= nums[left]
                left += 1
            right += 1
        return 0 if ans == n + 1 else ans


re = Solution()

print(re.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
