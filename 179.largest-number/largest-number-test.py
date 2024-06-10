from typing import List


class Solution:
    # 应用贪心策略的快排
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

    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]
        # 快速排序
        sorted_nums = self.quicksort(nums)
        # 解决特殊case
        if sorted_nums[-1] == "0":
            return "0"
        return ''.join(sorted_nums[::-1])


re = Solution()
print(re.largestNumber([3, 30, 34, 5, 9]))
