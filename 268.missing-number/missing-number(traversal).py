class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return len(nums)


"""
Solution：排序
先对数组排序，之后进行遍历，查看下标和元素值是否相等，
第一个不相等的元素就是缺失的元素

"""
