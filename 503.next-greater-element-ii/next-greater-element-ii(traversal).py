class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n
        stack = []
        for i in range(n):
            for j in range(i + 1, n * 2):
                if nums[j % n] > nums[i]:
                    ans[i] = nums[j % n]
                    break
        return ans


"""
Solution:单调递增栈
类似739
最简单的就是暴力，对于每个温度值，向后依次进行搜索，找到比当前温度更高的值。更好的方式使用「单调递增栈」
遍历 nums 中的每一个元素。对于 nums 的每一个元素 nums[i]，查找 nums[i] 右边第一个比 nums1[i] 大的元素。这种解法的时间复杂度是 O(n^2)
"""
