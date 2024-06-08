class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow, fast = 0, 0
        while fast < len(nums):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
            fast += 1


"""
Solution:双指针（快慢指针）
使用两个指针slow，fast。slow 指向处理好的非 0 数字数组的尾部，fast 指针指向当前待处理元素。 
不断向右移动 fast 指针，每次移动到非零数，则将左右指针对应的数交换，交换同时将 slow 右移。 
最终，slow 指针左侧均为处理好的非零数，而从 slow 指针指向的位置开始，fast 指针左边为止都为 0。
"""
