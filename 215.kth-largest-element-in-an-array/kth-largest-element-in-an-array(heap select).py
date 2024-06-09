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

    def heap_sort(self, arr, k):
        n = len(arr)

        # 构建最大堆
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)

        # 从第 n-1 个元素开始，依次将元素插入堆中，并调整堆
        for i in range(n - 1, n - k - 1, -1):
            arr[0], arr[i] = arr[i], arr[0]
            self.heapify(arr, i, 0)

        return arr[n - k]

    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.heap_sort(nums, k)


"""
Solution：使用堆选择
相比堆排序，这个好处是在排序过程中就选择最大的第K个值，节省后面元素排序的过程
"""
