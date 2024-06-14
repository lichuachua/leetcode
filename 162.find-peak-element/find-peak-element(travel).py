class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            if nums[i] > nums[res]:
                res = i
        return res

"""
Solution：遍历找最大值
最大值肯定是峰值
"""