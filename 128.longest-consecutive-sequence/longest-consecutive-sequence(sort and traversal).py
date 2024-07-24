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


"""
Solution：排序后双指针遍历
和674是相似的，只不过674是排好序的，且不要求连续，且中间数字重复只能算一次
按照674思想先排序，排序完成后，使用双指针遍历数组，注意坚持连续，且处理数字重复。
"""
