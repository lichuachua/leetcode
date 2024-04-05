class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        num = []
        count = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                count += 1
            else:
                num.append(count)
                count = 1
        num.append(count)
        return max(num)
