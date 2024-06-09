class Solution:
    def heapify(self, arr, n, i):
        # 将当前节点设为最大
        largest = i
        left = 2 * i + 1  # 左子节点
        right = 2 * i + 2  # 右子节点

        # 如果左子节点存在，且左子节点大于最大节点
        if left < n and arr[left] > arr[largest]:
            largest = left

        # 如果右子节点存在，且右子节点大于最大节点
        if right < n and arr[right] > arr[largest]:
            largest = right

        # 如果最大节点不是根节点
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # 交换
            # 递归调整受影响的子树
            self.heapify(arr, n, largest)

    def heap_sort(self, arr):
        n = len(arr)

        # 构建最大堆
        # 叶子节点不需要进行 heapify 调整。这是因为叶子节点没有子节点，
        # 因此它们天然地满足堆的性质（既最大堆性质或最小堆性质）。

        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)

        # 一个个取出元素进行堆排序
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]  # 交换
            self.heapify(   arr, i, 0)  # 调整堆

    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.heap_sort(nums)
        return nums[len(nums) - k]


"""
Solution：先进行堆排序，再选择最大的第K个元素
"""
