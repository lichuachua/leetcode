class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0
        nums_set = set(nums)
        for num in nums_set:
            if num - 1 not in nums_set:
                curr_num = num
                curr_streak = 1
                while curr_num + 1 in nums_set:
                    curr_num += 1
                    curr_streak += 1
                longest_streak = max(longest_streak, curr_streak)

        return longest_streak


"""
Solutio：哈希表
将数组存储到集合中进行去重，
遍历nums_set
如果 num - 1 不在集合中，那么 num 就可能是一个连续子序列的起点。只有起始点才会执行接下来的连续序列检查。
进入一个 while 循环，检查 curr_num + 1 是否在集合中。
如果是，说明当前序列还可以扩展，于是 curr_num 和 curr_streak 都需要更新，直到连续序列结束。

"""
