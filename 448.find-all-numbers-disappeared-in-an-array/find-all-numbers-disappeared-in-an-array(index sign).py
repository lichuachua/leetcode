'''
加n标记
'''


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            index = (nums[i] - 1) % len(nums)
            nums[index] += len(nums)
        for i in range(len(nums)):
            if nums[i] <= len(nums):
                res.append(i + 1)
        return res
