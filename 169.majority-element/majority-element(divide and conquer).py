class Solution:
    # 解决过程，合并左右部分的多数元素
    def conquer(self, left_majority: int, right_majority: int, nums: List[int], lo: int, hi: int) -> int:
        if left_majority == right_majority:
            return left_majority
        left_count, right_count = 0, 0
        for i in range(lo, hi + 1):
            if nums[i] == left_majority:
                left_count += 1
            if nums[i] == right_majority:
                right_count += 1

        return left_majority if left_count > right_count else right_majority

    # 分解过程
    def divide(self, nums: List[int], lo: int, hi: int) -> List[int]:
        # 基准情况：数组长度为1时，直接返回该元素
        if lo == hi:
            return nums[lo]

        mid = (hi - lo) // 2 + lo
        left_majority = self.divide(nums, lo, mid)
        right_majority = self.divide(nums, mid + 1, hi)

        # 合并左右部分的结果
        return self.conquer(left_majority, right_majority, nums, lo, hi)

    def majorityElement(self, nums: List[int]) -> int:
        return self.divide(nums, 0, len(nums) - 1)


"""
Solution:分治法
类似归并排序，我们将 nums 分为两部分，则 num 至少是其中一部分的多数元素。
具体步骤如下：

分解：将数组 nums 递归地将当前序列平均分成左右两个数组，直到所有子数组长度为 1。
解决：长度为 1 的子数组的多数元素就是其本身，将其返回即可。
合并：将两个子数组依次向上两两合并。
    如果两个子数组的多数元素相同，则说明合并后的数组多数元素为：两个子数组的多数元素。
    如果两个子数组的多数元素不同，则需要比较两个多数元素在整个区间的多数元素。
最后返回整个数组的多数元素。
"""
