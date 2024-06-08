class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()  # 对列表进行排序
        return nums[len(nums) - k]  # 返回第k个最大元素


"""
Solution：使用python的内置函数进行排序，再选择最大的第K个元素
"""
