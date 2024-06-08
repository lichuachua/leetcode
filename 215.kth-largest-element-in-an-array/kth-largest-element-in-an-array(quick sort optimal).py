class Solution:
    def partition(self, arr, low, high):
        # 使用哨兵划分，选择数组的第一个元素作为枢轴
        pivot = arr[low]
        left = low + 1
        right = high

        while True:
            # 向右移动左指针，直到找到大于枢轴的元素
            while left <= right and arr[left] <= pivot:
                left += 1
            # 向左移动右指针，直到找到小于枢轴的元素
            while right >= left and arr[right] >= pivot:
                right -= 1
            # 如果左指针大于右指针，则停止循环
            if left > right:
                break
            # 交换左右指针所指向的元素
            arr[left], arr[right] = arr[right], arr[left]

        # 将枢轴放置在正确的位置
        arr[low], arr[right] = arr[right], arr[low]
        # 返回枢轴的索引
        return right

    def randomized_partition(self, arr, low, high):
        # 随机选择枢轴
        pivot_index = random.randint(low, high)
        # 将随机选择的枢轴与第一个元素交换位置
        arr[pivot_index], arr[low] = arr[low], arr[pivot_index]
        # 调用哨兵划分函数
        return self.partition(arr, low, high)

    def quicksort(self, arr, low, high):
        if low < high:
            # 使用随机选择的枢轴进行划分
            pivot_index = self.randomized_partition(arr, low, high)
            # 对左右两个子数组进行递归排序
            self.quicksort(arr, low, pivot_index - 1)
            self.quicksort(arr, pivot_index + 1, high)
        return arr

    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = self.quicksort(nums, 0, len(nums) - 1)
        return nums[len(nums) - k]


"""
Solution：先进行快速排序，再选择最大的第K个元素
和quick sort方案没有本质的区别，只不过是优化了快速排序的两个步骤
1.随机选择枢纽（避免了最坏情况的发生，因为每次选择枢轴都是随机的，平均情况下性能较稳定）
2.根据哨兵划分的方式划分左右区间（哨兵划分是使用双指针1.调整小于和大于枢纽的元素，2.返回枢纽的最终位置）
    优点：对于包含大量重复元素的输入数据，哨兵划分的方法可以提高性能，因为它能够将相同的元素分散到两侧，减少递归调用的次数。
    缺点：在某些情况下，可能会因为分区不平衡而导致性能下降，特别是当输入数据中存在大量重复元素，并且分区不平衡时。

LC提交失败原因是哨兵划分的缺点，数据中存在大量重复元素导致。
"""
