class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        res = [''] * len(s)
        temp = numRows * 2 - 2
        for i in range(len(s)):
            index = i % temp
            if index < numRows:
                res[index] += s[i]
            else:
                res[temp - index] += s[i]
        return ''.join(res)
