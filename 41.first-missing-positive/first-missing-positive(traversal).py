class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        # 第一步：将不在范围 [1, n] 的元素设置为 n + 1
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1

        # 第二步：通过标记元素的存在性
        for i in range(n):
            num = abs(nums[i])
            if 1 <= num <= n:
                nums[num - 1] = -abs(nums[num - 1])

        # 第三步：查找第一个缺失的正整数
        for i in range(n):
            if nums[i] > 0:
                return i + 1

        # 如果所有位置的值都是负数，则缺失的正整数是 n + 1
        return n + 1


"""
Solution：遍历
# 第一步：将不在范围 [1, n] 的元素设置为 n + 1
# 第二步：通过标记元素的存在性---------通过将对应索引的元素变为负数来标记某个正整数是否存在。
# 第三步：查找第一个缺失的正整数
# 如果所有位置的值都是负数，则缺失的正整数是 n + 1
"""
