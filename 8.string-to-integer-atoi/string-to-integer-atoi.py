class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if s == "":
            return 0
        result = 0
        flag = 1
        if s[0] == '-':
            flag = -1
        if s[0] == '-' or s[0] == '+':
            s = s[1:]
        for i, v in enumerate(s):
            if v >= '0' and v <= '9':
                result = result * 10 + int(v)
            else:
                break
            if result >= 2 ** 31:
                if flag == -1:
                    return -2 ** 31
                return 2 ** 31 - 1
        return flag * result
