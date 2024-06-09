from typing import List


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
        return self.divide(nums,0,len(nums)-1)

re = Solution()
print(re.majorityElement([2,2,1,1,1,2,2]))