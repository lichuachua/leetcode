class Solution:
    # 合并过程两个有序数组
    def merge(self, left_nums: List[int], right_nums: List[int]) -> List[int]:
        nums = []
        left_i, right_i = 0, 0
        while left_i < len(left_nums) and right_i < len(right_nums):
            # 将两个有序子数组中较小元素依次插入到结果数组中
            if left_nums[left_i] < right_nums[right_i]:
                nums.append(left_nums[left_i])
                left_i += 1
            else:
                nums.append(right_nums[right_i])
                right_i += 1
        # 如果左子数组有剩余元素，则将其插入到结果数组中
        if left_i < len(left_nums):
            nums.extend(left_nums[left_i:])
        # 如果右子数组有剩余元素，则将其插入到结果数组中
        if right_i < len(right_nums):
            nums.extend(right_nums[right_i:])
        # 返回合并后的结果数组
        return nums

    # 分解过程

    def mergeSort(self, nums: List[int]) -> List[int]:
        # 数组元素个数小于等于 1 时，直接返回原数组
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2  # 将数组从中间位置分为左右两个数组
        left_nums = self.mergeSort(nums[0: mid])  # 递归将左子数组进行分解和排序
        right_nums = self.mergeSort(nums[mid:])  # 递归将右子数组进行分解和排序
        return self.merge(left_nums, right_nums)  # 把当前数组组中有序子数组逐层向上，进行两两合并

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums)


"""
Submit Result:Pass
"""
