from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, len(nums) - 1
        index = 0
        while index <= right:
            if index < left:
                index += 1
            elif nums[index] == 0:
                nums[left], nums[index] = nums[index], nums[left]
                left += 1
            elif nums[index] == 2:
                nums[right], nums[index] = nums[index], nums[right]
                right -= 1
            else:
                index += 1
        print(nums)


re = Solution()
print(re.sortColors([2, 0, 2, 1, 1, 0]))
