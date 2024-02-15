class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        "nums1 的初始长度为 m + n，从后往前排序，选最大的"
        i, j, k = m - 1, n - 1, 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[m + n - k] = nums1[i]
                i -= 1
            else:
                nums1[m + n - k] = nums2[j]
                j -= 1
            k += 1
        if j >= 0:
            nums1[:j + 1] = nums2[:j + 1]