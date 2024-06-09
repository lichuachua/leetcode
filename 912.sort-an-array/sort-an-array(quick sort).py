class Solution:
    def quicksort(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        else:
            pivot = nums[len(nums) // 2]
            left, middle, right = [], [], []
            for num in nums:
                if num < pivot:
                    left.append(num)
                elif num > pivot:
                    right.append(num)
                else:
                    middle.append(num)
        return self.quicksort(left) + middle + self.quicksort(right)

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.quicksort(nums)


"""
Submit Result:超出时间限制
"""
