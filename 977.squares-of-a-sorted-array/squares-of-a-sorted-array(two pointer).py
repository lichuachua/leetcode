class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        res = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            if nums[left] * nums[left] > nums[right] * nums[right]:
                res[i] = nums[left] * nums[left]
                left += 1
            else:
                res[i] = nums[right] * nums[right]
                right -= 1
        return res
