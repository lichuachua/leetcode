class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_len = 0
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    max_len = max(max_len, i - stack[-1])
                else:
                    stack.append(i)
        return max_len


"""
Solution：栈
栈主要用于保存未匹配的左括号和 最后一个没有被匹配的右括号的下标【上一次失效的错误的括号，是一个分水岭】。

初始化一个栈，栈底放置一个初始值 -1，表示最后一个没有被匹配的右括号的下标。
遍历字符串：
如果当前字符是 (，将其下标压入栈。
如果当前字符是 )，弹出栈顶元素。如果栈为空，将当前下标压入栈；否则计算有效括号的长度并更新最大长度。
"""
