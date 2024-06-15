from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1 = nums1+nums2
        nums1.sort()
        if len(nums1)%2==1:
            return nums1[len(nums1)//2]
        else:
            return (nums1[len(nums1)//2]+nums1[len(nums1)//2-1])/2

re = Solution()
print(re.findMedianSortedArrays([1,3],[2]))
"""
合并两个数组并排序，找到中位数
"""