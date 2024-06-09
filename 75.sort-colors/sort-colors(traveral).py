class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        end = 0
        for i in range(n):
            if nums[i] == 0:
                nums[i], nums[end] = nums[end], nums[i]
                end += 1

        for i in range(end, n):
            if nums[i] == 1:
                nums[i], nums[end] = nums[end], nums[i]
                end += 1


"""
Solution:遍历
需要划分三个类别，所以需要筛选两次（剩下的就是最后一种）
第一次遍历，选出0，并且标记0的最后一个下标
第二次遍历，选出1，放到0的最后一个下标之后
"""
