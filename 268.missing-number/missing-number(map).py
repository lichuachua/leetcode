class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        m = {}
        for i in range(len(nums)):
            m[nums[i]] = True
        for i in range(len(nums)):
            if i not in m:
                return i
        return len(nums)
