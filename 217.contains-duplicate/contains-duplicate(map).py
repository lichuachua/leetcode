class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        m = {}
        for index in range(len(nums)):
            if nums[index] in m:
                return True
            else:
                m[nums[index]] = index
        return False
