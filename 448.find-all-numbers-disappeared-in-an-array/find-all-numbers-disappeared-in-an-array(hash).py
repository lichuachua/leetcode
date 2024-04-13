class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        m = {}
        res = []
        for i in range(len(nums)):
            m[nums[i]] = True
        for i in range(len(nums)):
            if not i + 1 in m:
                res.append(i + 1)
        return res
