class Solution:
    def insertionSort(self, nums: List[int]) -> List[int]:
        # 遍历无序区间
        for i in range(1, len(nums)):
            key = nums[i]  # 当前要插入的元素
            j = i - 1  # 已排序部分的最后一个元素的索引

            # 将 key 与已排序部分从后往前比较，找到合适的插入位置
            while j >= 0 and key < nums[j]:
                nums[j + 1] = nums[j]  # 向后移动元素
                j -= 1

            nums[j + 1] = key  # 将 key 插入到合适的位置
        return nums

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.insertionSort(nums)


"""
Submit Result:超出时间限制
"""
