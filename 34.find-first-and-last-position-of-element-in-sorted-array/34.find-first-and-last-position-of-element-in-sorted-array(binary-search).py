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


"""
Solution：折半查找，二分查找
两次二分查找，找对应的左右边界，一般的二分法找的是左边界，
要找右边界，可以在nums[mid] == target的时候也进行右移操作




在折半查找（二分查找）中mid的选择【此处没有使用】：
选择使用哪种mid计算方法取决于具体的需求和边界条件：
mid = left + (right - left) // 2：偏向左侧，适合一般情况，防止整数溢出。
mid = left + (right - left + 1) // 2：偏向右侧，适合需要向上取整避免无限循环的情况。
"""
