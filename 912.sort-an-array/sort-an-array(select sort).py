class Solution:
    def selectionSort(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            # 记录第i次排序需要找到值的位置
            min_i = i
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[min_i]:
                    min_i = j
            # 如果找到最小值的位置，将 i 位置上元素与最小值位置上的元素进行交换
            if i != min_i:
                nums[i], nums[min_i] = nums[min_i], nums[i]
        return nums

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.selectionSort(nums)


"""
Submit Result:超出时间限制
"""
