class Solution:
    def binaryInsertionSort(self, nums: List[int]) -> List[int]:
        # 遍历无序区间
        for i in range(1, len(nums)):
            key = nums[i]  # 当前要插入的元素
            left, right = 0, i - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > key:
                    right = mid - 1
                else:
                    left = mid + 1
            for j in range(i - 1, left - 1, -1):
                nums[j + 1] = nums[j]
            nums[left] = key
        return nums

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.binaryInsertionSort(nums)


"""
Submit Result:超出时间限制
"""
