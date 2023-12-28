class Solution:
    def countSegments(self, s: str) -> int:
        res = 0
        if s == '':
            return res
        elif s[0] != ' ':
            res = 1
        for i in range(1, len(s)):
            if s[i - 1] == ' ' and s[i] != ' ':
                res += 1
        return res
