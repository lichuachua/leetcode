class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for index in range(len(nums)):
            if target - nums[index] in m:
                return m[target - nums[index]], index
            else:
                m[nums[index]] = index
