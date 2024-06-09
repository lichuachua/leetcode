class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2
        nums1.sort()


"""
Solution:数组合并，再排序
将nums1数组m之后的元素置为nums2
使用内置函数进行排序
"""
