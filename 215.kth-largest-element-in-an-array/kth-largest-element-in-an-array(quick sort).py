class Solution:

    def quicksort(self, arr):
        if len(arr) <= 1:
            return arr
        else:
            pivot = arr[len(arr) // 2]
            left, middle, right = [], [], []
            for num in arr:
                if num < pivot:
                    left.append(num)
                elif num > pivot:
                    right.append(num)
                else:
                    middle.append(num)
        return self.quicksort(left) + middle + self.quicksort(right)

    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = self.quicksort(nums)
        return nums[len(nums) - k]


"""
Solution：先进行快速排序，再选择最大的第K个元素
quick sort
1.选择列表的中间元素作为枢纽
2.根据枢纽对列表进行for循环选择左右区间
"""
