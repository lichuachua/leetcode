class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                res.append(nums[i])
        return res


"""
Solution：排序+遍历
先对数组进行排序
之后遍历相邻两元素，如果相等则认为是重复元素
"""
