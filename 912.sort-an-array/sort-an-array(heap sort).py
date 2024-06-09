class Solution:
    def heapify(self, nums, n, i):
        # 将当前节点设为最大
        largest = i
        left = 2 * i + 1  # 左子节点
        right = 2 * i + 2  # 右子节点

        # 如果左子节点存在，且左子节点大于最大节点
        if left < n and nums[left] > nums[largest]:
            largest = left

        # 如果右子节点存在，且右子节点大于最大节点
        if right < n and nums[right] > nums[largest]:
            largest = right

        # 如果最大节点不是根节点
        if largest != i:
            nums[i], nums[largest] = nums[largest], nums[i]  # 交换
            # 递归调整受影响的子树
            self.heapify(nums, n, largest)

    def heap_sort(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # 构建最大堆
        # 叶子节点不需要进行 heapify 调整。这是因为叶子节点没有子节点，
        # 因此它们天然地满足堆的性质（既最大堆性质或最小堆性质）。

        for i in range(n // 2 - 1, -1, -1):
            self.heapify(nums, n, i)

        # 一个个取出元素进行堆排序
        for i in range(n - 1, 0, -1):
            nums[i], nums[0] = nums[0], nums[i]  # 交换
            self.heapify(nums, i, 0)  # 调整堆
        return nums

    def sortArray(self, nums: List[int]) -> List[int]:
        self.heap_sort(nums)
        return nums


"""
Submit Result:Pass
因为堆排序的过程是在原地进行的，即在给定的数组上进行操作，不需要返回值。
"""
