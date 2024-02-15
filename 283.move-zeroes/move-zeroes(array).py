class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero_index = 0

        # 将非零元素移到数组前面
        for num in nums:
            if num != 0:
                nums[non_zero_index] = num
                non_zero_index += 1

        # 在末尾补充零
        while non_zero_index < len(nums):
            nums[non_zero_index] = 0
            non_zero_index += 1