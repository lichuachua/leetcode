class Solution:
    def quick_select(self, nums, k):
        pivot = random.choice(nums)
        # 将小于、等于、 大于pivot的元素划分至 left,middle,right 中
        left, middle, right = [], [], []
        for num in nums:
            if num < pivot:
                left.append(num)
            elif num > pivot:
                right.append(num)
            else:
                middle.append(num)
        if k <= len(right):
            # 第 k 大元素在 right 中，递归划分
            return self.quick_select(right, k)
        if len(nums) - len(left) < k:
            # 第 k 大元素在 left 中，递归划分
            return self.quick_select(left, k - len(nums) + len(left))
        return pivot

    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quick_select(nums, k)


"""
Solution：使用快速选择
相比快速排序，这个好处是在排序过程中就选择最大的第K个值，节省后面元素排序的过程
"""
