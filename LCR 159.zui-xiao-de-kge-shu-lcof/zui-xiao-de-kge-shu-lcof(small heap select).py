class Solution:
    def heapify(self, arr: List[int], n: int, i: int):
        # 将当前节点设为最小
        smallest = i
        left = 2 * i + 1  # 左子节点
        right = 2 * i + 2  # 右子节点

        # 如果左子节点存在，且左子节点小于最小节点
        if left < n and arr[left] < arr[smallest]:
            smallest = left

        # 如果右子节点存在，且右子节点小于最小节点
        if right < n and arr[right] < arr[smallest]:
            smallest = right

        # 如果最小节点不是根节点
        if smallest != i:
            arr[i], arr[smallest] = arr[smallest], arr[i]  # 交换
            # 递归调整受影响的子树
            self.heapify(arr, n, smallest)

    def heap_sort(self, arr: List[int], cnt: int) -> List[int]:
        n = len(arr)

        # 构建最小堆
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)

        # 从第 n-1 个元素开始，依次将堆顶元素与当前末尾元素交换，并调整堆
        for i in range(n - 1, n - cnt - 1, -1):
            arr[0], arr[i] = arr[i], arr[0]
            self.heapify(arr, i, 0)

        # 返回数组的最后 cnt 个元素（即库存余量最少的 cnt 个元素）
        return arr[n - cnt:]

    def inventoryManagement(self, stock: List[int], cnt: int) -> List[int]:
        if cnt == 0:
            return []
        return self.heap_sort(stock, cnt)


"""
Solution：使用堆选择
相比堆排序，这个好处是在排序过程中就选择最小的cnt个元素，节省后面元素排序的过程
"""
