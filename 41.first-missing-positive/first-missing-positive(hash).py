class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        size = len(nums)

        # 第一步：将每个正整数放到它应该在的位置上
        for i in range(size):
            # 当 nums[i] 在 [1, size] 范围内，并且 nums[i] 不在正确的位置上时
            while 1 <= nums[i] <= size and nums[i] != nums[nums[i] - 1]:
                # 交换 nums[i] 和 nums[nums[i] - 1]
                index1 = i
                index2 = nums[i] - 1
                nums[index1], nums[index2] = nums[index2], nums[index1]

        # 第二步：遍历数组，找到第一个不在正确位置上的元素
        for i in range(size):
            if nums[i] != i + 1:
                return i + 1

        # 如果所有位置上的元素都在正确的位置上，则缺失的正整数是 size + 1
        return size + 1


"""
Solution：哈希表(原地哈希)
遍历数组，将每个正整数放到它应该在的位置上，0和负数不用管
再次遍历数组，找到第一个不在正确位置上的元素
"""
