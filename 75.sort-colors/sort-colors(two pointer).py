class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, len(nums) - 1
        index = 0
        while index <= right:
            if index < left:
                index += 1
            elif nums[index] == 0:
                nums[left], nums[index] = nums[index], nums[left]
                left += 1
            elif nums[index] == 2:
                nums[right], nums[index] = nums[index], nums[right]
                right -= 1
            else:
                index += 1


"""
Solution:双指针、快排
使用两个指针（left，right）划分三个区间，left左边是0，right右边是2，left和right中间是1
注意：移动的时候需要判断 index 和 left 的位置，因为 left 左侧是已经处理好的数组，
所以需要判断 index 的位置是否小于 left，小于的话，需要更新 index 位置。
"""
