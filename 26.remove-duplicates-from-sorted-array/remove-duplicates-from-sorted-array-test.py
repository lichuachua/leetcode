from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return len(nums)
        slow,fast = 0,1
        while fast< len(nums):
            if nums[slow]!=nums[fast]:
                slow+=1
                nums[slow] = nums[fast]
            fast+=1
        return slow+1


re = Solution()
print(re.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))