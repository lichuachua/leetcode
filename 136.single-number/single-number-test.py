from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            res = res ^ nums[i]
        return res


re = Solution()
print(re.singleNumber([2, 2, 1]))
