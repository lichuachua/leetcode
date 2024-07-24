class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        m = {}
        for i in range(len(nums)):
            m[nums[i]] = True
        for i in range(len(nums)):
            if i not in m:
                return i
        return len(nums)


"""
Solution：哈希表
遍历数组，把元素存储在map中
遍历0——len(nums)，找到不存在的那个元素，否则返回len(nums)
"""
