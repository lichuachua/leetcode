from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if nums[left] * nums[left] > nums[right] * nums[right]:
                res = nums[right]
                nums[i] = nums[left] * nums[left]
                nums[left] = res
                left += 1
            else:
                res = nums[left]
                nums[i] = nums[right] * nums[right]
                nums[right] = res
                right -= 1
        return nums


re = Solution()
print(re.sortedSquares([-4, -1, 0, 3, 10]))
