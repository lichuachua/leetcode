class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for ch in s:
            if stack and stack[-1] == ch:
                stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)


"""
Solution：栈
类似20括号匹配
使用「栈」，遍历字符串，如果当前字符与栈顶字符相同，则将栈顶所有相同字符删除，否则就将当前字符入栈。
"""
