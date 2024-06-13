from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        # 注意
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                # 注意
                right = mid
            else:
                # 注意
                right = right - 1
        return nums[left]


re = Solution()
print(re.findMin([3, 3, 1, 3]))
