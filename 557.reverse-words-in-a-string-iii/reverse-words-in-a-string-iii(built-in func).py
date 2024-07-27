class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        for i in range(len(s)):
            s[i] = s[i][::-1]
        return " ".join(s)


"""
Solution：内置函数
使用内置方法将字符串切分为单词，之后使用内置方法将每个单词逆转，再将单词合并为字符串
"""
