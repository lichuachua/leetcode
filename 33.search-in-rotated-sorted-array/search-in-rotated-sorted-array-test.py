from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        # 注意
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                # 注意
                right = mid
        return left

    def binary_search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return -1

    def search(self, nums: List[int], target: int) -> int:
        minVal = self.findMin(nums)
        index_1 = self.binary_search(nums[:minVal], target)
        index_2 = self.binary_search(nums[minVal:], target)
        if index_1 != -1:
            return index_1
        elif index_2 != -1:
            return index_2 + minVal
        else:
            return -1


re = Solution()
print(re.search([4, 5, 6, 7, 0, 1, 2], 0))
