class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]


"""
Solution: 排序
先堆数组元素进行排序，
存在多数元素，则所找的那个值一定是有序数组的中间元素
"""
