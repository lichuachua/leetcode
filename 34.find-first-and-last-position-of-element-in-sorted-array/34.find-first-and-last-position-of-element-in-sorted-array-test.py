from typing import List


class Solution:
    def searchLeft(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        while left <= right:

            mid = left + (right - left) // 2
            # 偏向左侧
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def searchRight(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        while left <= right:

            mid = left + (right - left) // 2
            # 偏向右侧
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return right

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left_index = self.searchLeft(nums, target)
        right_index = self.searchRight(nums, target)

        if left_index <= right_index:
            return [left_index, right_index]
        else:
            return [-1, -1]


re = Solution()
print(re.searchRange([5, 7, 7, 8, 8, 10], 8))
