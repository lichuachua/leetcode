class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        m = {}
        for i in range(len(nums)):
            if nums[i] in m:
                res.append(nums[i])
            else:
                m[nums[i]] = 1
        return res


"""
Solution：哈希表
遍历保存元素在哈希表：
    若元素存在，说明元素重复
    否则将元素存入hash
"""
