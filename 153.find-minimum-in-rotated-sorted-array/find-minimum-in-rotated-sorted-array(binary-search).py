class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        # 注意
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                # 注意
                right = mid
        return nums[left]


"""
数组经过「旋转」之后，会有两种情况，第一种就是原先的升序序列，另一种是两段升序的序列。

第一种的最小值在最左边。第二种最小值在第二段升序序列的第一个元素。
创建两个指针left、right，分别指向数组首尾。
让后计算出两个指针中间值 mid。将 mid 与 right 做比较。
如果nums[mid]>nums[right]，则最小值一定在 mid 右侧(mid在第一个升序数组上，最小的值应该是第二个升序数组的开头)，则将left 移动到mid+1 位置，继续查找右侧区间。
如果nums[mid]≤nums[right]，则最小值一定在 mid 左侧（第一种情况或者mid在第二个升序数组的非第一个元素上），或者 mid 位置，将right 移动到mid 位置上，继续查找左侧区间。
"""
