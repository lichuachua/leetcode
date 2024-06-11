class Solution:
    def quicksort(self, nums: List[str]) -> List[str]:
        if len(nums) <= 1:
            return nums
        else:
            pivot = nums[len(nums) // 2]
            left, middle, right = [], [], []
            for num in nums:
                if num + pivot < pivot + num:
                    left.append(num)
                elif num + pivot > pivot + num:
                    right.append(num)
                else:
                    middle.append(num)
        return self.quicksort(left) + middle + self.quicksort(right)

    def crackPassword(self, password: List[int]) -> str:
        nums = [str(num) for num in password]
        # 快速排序
        sorted_nums = self.quicksort(nums)
        return ''.join(sorted_nums)


"""
类似 179题
Solution: 贪心算法、排序
贪心策略
    若拼接字符串x+y>y+x，则x"大于"y
    反之，若x+y<y+x ，则x"小于"y
步骤：
    初始化： 字符串列表 strs ，保存各数字的字符串格式。
    列表排序： 根据贪心策略对 strs 进行从大到小排序。
    返回值： 拼接 strs 中的所有字符串，并返回。
"""
