class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        length = len(strs[0])
        count = len(strs)
        for i in range(length):
            c = strs[0][i]
            for j in range(1, count):
                if len(strs[j]) == i or strs[j][i] != c:
                    return strs[0][:i]
        return strs[0]


"""
Solution：纵向遍历
依次遍历所有字符串的每一列，比较相同位置上的字符是否相同。
如果相同，则继续对下一列进行比较。
如果不相同，则当前列字母不再属于公共前缀，直接返回当前列之前的部分。
"""
