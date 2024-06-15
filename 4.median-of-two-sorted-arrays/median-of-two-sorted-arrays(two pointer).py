class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)

        k = (n1 + n2 + 1) // 2
        left = 0
        right = n1
        while left < right:
            m1 = left + (right - left) // 2  # 在 nums1 中取前 m1 个元素，m1为nums1的中点
            m2 = k - m1  # 在 nums2 中取前 m2 个元素，m2为取完nums中剩余的部分
            if nums1[m1] < nums2[m2 - 1]:  # nums1的中点和nums2的值比较，说明 nums1 中所元素不够多，
                left = m1 + 1
            else:
                right = m1

        m1 = left
        m2 = k - m1

        c1 = max(float('-inf') if m1 <= 0 else nums1[m1 - 1], float('-inf') if m2 <= 0 else nums2[m2 - 1])
        if (n1 + n2) % 2 == 1:
            return c1

        c2 = min(float('inf') if m1 >= n1 else nums1[m1], float('inf') if m2 >= n2 else nums2[m2])

        return (c1 + c2) / 2


"""
Solution：双指针，二分法
二分查找排除法的思路：排除一定不存在的区间，在剩下区间中继续查找
长度为奇数/偶数时候的结果
"""
