from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        m = {}
        for index in range(len(nums)):
            if nums[index] in m:
                return True
            else:
                m[nums[index]] = index
        return False


re = Solution()
print(re.containsDuplicate([1, 1, 2, 3, 3]))
