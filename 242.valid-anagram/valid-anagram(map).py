class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        m = {}
        for i in s:
            if i in m:
                m[i] += 1
            else:
                m[i] = 1
        for i in t:
            if i not in m:
                return False
            m[i] -= 1
            if m[i] < 0:
                return False
        return True
