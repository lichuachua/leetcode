class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return s
        dp = [[False for _ in range(n)] for _ in range(n)]
        max_start = 0
        maxlen = 1
        for j in range(1, n):
            for i in range(j):
                if s[i] == s[j]:
                    if j - i <= 2:
                        dp[i][j] = True
                    else:
                        # False 已经初始化
                        dp[i][j] = dp[i + 1][j - 1]
                if dp[i][j] and (j - i + 1) > maxlen:
                    maxlen = j - i + 1
                    max_start = i
        return s[max_start:max_start + maxlen]


re = Solution()
print(re.longestPalindrome("babad"))
