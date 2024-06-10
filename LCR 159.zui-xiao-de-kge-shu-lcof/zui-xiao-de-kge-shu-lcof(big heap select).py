class Solution:
    def heapify(self, arr: List[int], n: int, i: int):
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

    def heap_sort(self, arr: List[int], cnt: int) -> List[int]:
        n = len(arr)

        # 构建最大堆
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)

        # 从第 n-1 个元素开始，依次选出最大的n-cnt个元素插入堆中，并调整堆
        for i in range(n - 1, cnt - 1, -1):
            arr[0], arr[i] = arr[i], arr[0]
            self.heapify(arr, i, 0)

        # 返回数组的前 cnt 个元素
        return arr[:cnt]

    def inventoryManagement(self, stock: List[int], cnt: int) -> List[int]:
        return self.heap_sort(stock, cnt)


"""
Solution：使用堆选择
相比堆排序，这个好处是在排序过程中就选择最大的n-cnt个元素，之后返回剩下的元素，节省后面元素排序的过程
"""
