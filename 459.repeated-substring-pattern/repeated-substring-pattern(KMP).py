class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(1, n // 2 + 1):
            if n % i == 0:
                substring = s[:i]
                if substring * (n // i) == s:
                    return True
        return False


"""
Solution：枚举
遍历字符串，假设字符串是由子字符串组成的，那么n % i == 0，之后比较子字符串*多次能等于字符串
"""
