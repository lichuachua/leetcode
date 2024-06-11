from typing import List


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


re = Solution()
print(re.crackPassword([15, 8, 7]))
