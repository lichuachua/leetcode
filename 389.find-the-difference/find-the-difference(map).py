class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        m = {}
        for char in s:
            if char in m:
                m[char] += 1
            else:
                m[char] = 1
        for char in t:
            if char not in m or m[char] == 0:
                return char
            else:
                m[char] -= 1
        return ''
