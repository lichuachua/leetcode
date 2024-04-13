from typing import List
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            index = nums[i]
            if nums[i]<0:
                index = -nums[i]
            if nums[index-1]>0:
                nums[index-1] = -nums[index-1]
        for i in range(len(nums)):
            if nums[i]>0:
                res.append(i+1)
        return res

re = Solution()
print(re.findDisappearedNumbers([4,3,2,7,8,2,3,1]))