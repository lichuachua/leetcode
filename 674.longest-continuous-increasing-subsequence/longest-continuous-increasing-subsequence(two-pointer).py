class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        slow, fast = 0, 1
        res = 0
        while fast < len(nums):
            if nums[fast] > nums[fast - 1]:
                fast += 1
            else:
                if res < fast - slow:
                    res = fast - slow
                slow, fast = fast, fast + 1
        if res < fast - slow:
            res = fast - slow
        return res
