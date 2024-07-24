class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            res ^= nums[i] ^ i
        return res ^ len(nums)


"""
Solution：位运算，异或运算
对元素及其下标进行异或运算，相当于在数组元素和数组下标的组合元素中找到出现一次的数字（只有缺失的元素是出现一次，其余出现两次）
"""
