class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(0, len(nums) - 2, 3):
            if not (nums[i] == nums[i + 1] and nums[i] == nums[i + 2]):
                return nums[i]
        return nums[len(nums) - 1]
