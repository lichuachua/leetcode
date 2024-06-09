class Solution:
    def radixSort(self, nums: List[int]) -> List[int]:
        # 桶的大小为所有元素的最大位数
        size = len(str(max(nums)))

        # 从最低位（个位）开始，逐位遍历每一位
        for i in range(size):
            # 定义长度为 10 的桶数组 buckets，每个桶分别代表 0 ~ 9 中的 1 个数字。
            buckets = [[] for _ in range(10)]
            # 遍历数组元素，按照每个元素当前位上的数字，将元素放入对应数字的桶中。
            for num in nums:
                buckets[num // (10 ** i) % 10].append(num)
            # 清空原始数组
            nums.clear()
            # 按照桶的顺序依次取出对应元素，重新加入到原始数组中。
            for bucket in buckets:
                for num in bucket:
                    nums.append(num)

        # 完成排序，返回结果数组
        return nums

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.radixSort(nums)


"""
Submit Result:解答错误
基数排序只适合非负数(当然，可以改造)
"""
