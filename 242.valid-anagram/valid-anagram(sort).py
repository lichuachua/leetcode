class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return ''.join(sorted(s)) == ''.join(sorted(t))


"""
Solution：排序
对两个字符串排序，之后对比两个字符串是否相等
"""
