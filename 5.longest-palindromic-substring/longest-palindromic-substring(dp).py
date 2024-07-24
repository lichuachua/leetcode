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


"""
Sloution：动态规划

1. **划分阶段**
   - 按照区间长度进行阶段划分。

2. **定义状态**
   - 定义状态 `dp[i][j]` 表示字符串 `s` 在区间 `[i, j]` 范围内是否是一个回文串。

3. **状态转移方程**
   - 当子串只有 `1` 位或 `2` 位的时候：
     - 如果 `s[i] == s[j]`，则该子串为回文子串，即：`dp[i][j] = (s[i] == s[j])`。
   - 如果子串大于 `2` 位：
     - 如果 `s[i+1...j-1]` 是回文串，并且 `s[i] == s[j]`，则 `s[i...j]` 也是回文串，即：`dp[i][j] = (s[i] == s[j]) and dp[i + 1][j - 1]`。

4. **初始条件**
   - 初始状态下，默认字符串 `s` 的所有子串都不是回文串。

5. **最终结果**
   - 根据之前定义的状态，`dp[i][j]` 表示字符串 `s` 在区间 `[i, j]` 范围内是否是一个回文串。
   - 当判断完 `s[i:j]` 是否为回文串时，同时判断并更新最长回文子串的起始位置 `max_start` 和最大长度 `max_len`。
   - 最终结果为 `s[max_start:max_start + max_len]`。

"""
