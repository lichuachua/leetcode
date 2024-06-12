class Solution:
    def search(self, nums: List[int], target: int) -> int:
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


"""
Solution:二分查找、折半查找
1. mid = (left + right) // 2
这种方式直接取left和right的平均值来计算中间索引。
这种写法简单直接，但在某些编程语言（特别是C/C++）中，如果left和right非常大，left + right可能会导致整数溢出。

2. mid = left + (right - left) // 2【更推荐】
这种写法通过先计算right - left来避免直接相加left和right，从而防止整数溢出。
尽管在现代编程语言（如Python）中整数溢出问题不明显，但这种方式更加安全和普遍，适合各种编程环境。
"""
