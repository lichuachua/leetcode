class Solution:
    def firstUniqChar(self, s: str) -> int:
        # hash遍历两次
        h = {}
        for i in s:
            h[i] = h.get(i, 0) + 1
        for i, item in enumerate(s):
            if h[item] == 1:
                return i
        return -1
