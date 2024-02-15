from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, j = 0, 0
        while (i < len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
            i += 1
        return j


re = Solution()
print(re.removeElement([3, 2, 2, 3], 3))