class Solution:
    def toLowerCase(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            if ord(s[i]) >= 65 and ord(s[i]) <= 90:
                res += chr(ord(s[i]) + 32)
            else:
                res += s[i]
        return res
