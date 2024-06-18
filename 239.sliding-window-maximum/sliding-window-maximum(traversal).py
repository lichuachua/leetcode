class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        for i in range(len(nums) - k + 1):
            max_num = float('-inf')
            for j in range(i, i + k):
                if nums[j] > max_num:
                    max_num = nums[j]
            res.append(max_num)
        return res


"""
Solution:暴力求解
Submit Result:超出时间限制
暴力求解的话，需要使用二重循环遍历，其时间复杂度为 O(n * k)。
"""
