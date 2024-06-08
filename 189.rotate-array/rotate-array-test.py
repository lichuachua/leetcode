from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)  # 将 k 取模，防止 k 大于数组长度
        print(nums)
        self.reverse(nums)
        print(nums)
        self.reverse(nums[:k])
        print(nums)
        self.reverse(nums[k:])
        print(nums)

    def reverse(self, nums: List[int]) -> None:
        left, right = 0, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


re = Solution()
print(re.rotate([1, 2, 3, 4, 5, 6, 7], 3))
