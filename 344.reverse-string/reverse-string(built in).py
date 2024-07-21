class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # s[:] = s[::-1] 是对原始字符串就地修改
        # 而 s = s[::-1] 则是创建一个新的反转字符串并赋值给变量 s
        s[:] = s[::-1]
