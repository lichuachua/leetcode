class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)  # 将 k 取模，防止 k 大于数组长度
        nums[:] = nums[::-1]
        nums[:] = nums[:k][::-1] + nums[k:][::-1]


""""
Solution：数组反转—————list切割
先把整个数组翻转一下，逆序。我们再从 𝑘 位置分隔开，
将[0...k−1] 区间上的元素和 [k...n−1] 区间上的元素再翻转一下，
两个反转后的元素合并就得到了最终结果。
"""
