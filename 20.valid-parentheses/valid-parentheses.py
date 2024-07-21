class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        if s[0] == ']' or s[0] == '}' or s[0] == ')':
            return False
        m = {'[': ']', '{': '}', '(': ')'}
        stack = []
        for c in s:
            if len(stack) == 0 and (c == ']' or c == '}' or c == ')'):
                return False
            if c in m:
                stack.append(c)
            elif m[stack.pop()] != c:
                return False
        return len(stack) == 0


"""
Solution：栈模拟
使用栈模拟，使用map存储每一个括号对，遍历字符串
若元素为 '['、'{'、'(' 则入栈，
若元素为']'、'}'、')'，则比较是否是栈中栈顶元素对应的括号，不是则返回false
"""
