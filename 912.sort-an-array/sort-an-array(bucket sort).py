class Solution:
    def insertionSort(self, nums: List[int]) -> List[int]:
        # 遍历无序区间
        for i in range(1, len(nums)):
            key = nums[i]  # 当前要插入的元素
            j = i - 1  # 已排序部分的最后一个元素的索引

            # 将 key 与已排序部分从后往前比较，找到合适的插入位置
            while j >= 0 and key < nums[j]:
                nums[j + 1] = nums[j]  # 向后移动元素
                j -= 1

            nums[j + 1] = key  # 将 key 插入到合适的位置
        return nums

    def bucketSort(self, nums: List[int], bucket_size=5) -> List[int]:
        # 计算待排序序列中最大值元素 nums_max、最小值元素 nums_min
        nums_min, nums_max = min(nums), max(nums)
        # 定义桶的个数为 (最大值元素 - 最小值元素) // 每个桶的大小 + 1
        bucket_count = (nums_max - nums_min) // bucket_size + 1
        # 定义桶数组 buckets
        buckets = [[] for _ in range(bucket_count)]

        # 遍历待排序数组元素，将每个元素根据大小分配到对应的桶中
        for num in nums:
            buckets[(num - nums_min) // bucket_size].append(num)

        # 对每个非空桶内的元素单独排序，排序之后，按照区间顺序依次合并到 res 数组中
        res = []
        for bucket in buckets:
            self.insertionSort(bucket)
            res.extend(bucket)

        # 返回结果数组
        return res

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.bucketSort(nums)


"""
Submit Result:Pass
"""
