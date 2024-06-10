class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for i in range(len(nums) - 1):
            gap = nums[i + 1] - nums[i]
            if gap > res:
                res = gap
        return res


"""
Solution:内置函数先排序，再遍历找最大的gap
"""
