from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # 对数组进行排序
        nums.sort()

        longest_streak = 1
        current_streak = 1

        # 遍历排序后的数组
        for i in range(1, len(nums)):
            # 如果当前元素和前一个元素连续
            if nums[i] == nums[i - 1] + 1:
                current_streak += 1
            # 如果当前元素与前一个元素相同（避免重复计数）
            elif nums[i] != nums[i - 1]:
                longest_streak = max(longest_streak, current_streak)
                current_streak = 1

        # 最后一次更新最长的子序列长度
        longest_streak = max(longest_streak, current_streak)

        return longest_streak


re = Solution()
print(re.longestConsecutive([100, 4, 200, 1, 3, 2]))
