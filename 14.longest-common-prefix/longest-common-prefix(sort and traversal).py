class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        longest, shortest = strs[0], strs[len(strs) - 1]
        i = 0
        while i < len(shortest) and i < len(longest):
            if longest[i] != shortest[i]:
                return longest[:i]
            i += 1
        return longest[:i]


"""
Solution：排序，遍历
先对数组进行排序（按照字母顺序）
之后遍历第一个元素和最后一个元素，找到找到他们最长的前缀
"""
