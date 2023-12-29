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


re = Solution()
print(re.isValid("]"))
