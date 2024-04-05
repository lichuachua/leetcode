from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        # 计算到每一个元 i 素为止，最长连续递增序列的长度，存放到数组num中
        num = [1] * len(nums)
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                num[i] = num[i - 1] + 1
        return max(num)


re = Solution()
print(re.findLengthOfLCIS([1, 3, 5, 4, 7]))
