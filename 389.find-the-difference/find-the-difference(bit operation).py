class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        diff = 0
        for i in range(len(s)):
            diff ^= ord(s[i]) ^ ord(t[i])
        return chr(diff ^ ord(t[len(t) - 1]))
