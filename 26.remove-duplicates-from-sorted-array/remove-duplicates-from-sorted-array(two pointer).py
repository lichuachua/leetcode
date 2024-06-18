class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        slow, fast = 0, 1
        while fast < len(nums):
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
        return slow + 1


"""
Solution：双指针
因为数组是有序的，那么重复的元素一定会相邻。删除重复元素，实际上就是将不重复的元素移到数组左侧。
定义两个快慢指针 slow，fast。其中 slow 指向去除重复元素后的数组的末尾位置。fast 指向当前元素。
"""
