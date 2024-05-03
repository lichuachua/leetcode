class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        m = {}
        for i in range(len(nums)):
            if nums[i] not in m:
                m[nums[i]] = 1
            else:
                m[nums[i]] = m[nums[i]] + 1
        for key, value in m.items():
            if value == 1:
                return key
        return 0
