from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        slow, fast = 0, 0
        while fast < len(nums):
            if nums[fast] == 1:
                fast += 1
            else:
                if res < fast - slow:
                    res = fast - slow
                fast += 1
                slow = fast
        if res < fast - slow:
            res = fast - slow
        return res


re = Solution()
print(re.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
