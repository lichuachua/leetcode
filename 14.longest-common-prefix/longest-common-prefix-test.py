from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        longest, shortest = strs[0], strs[len(strs) - 1]
        i = 0
        while i < len(shortest) and i < len(longest):
            if longest[i] != shortest[i]:
                return longest[:i]
            i += 1
        return longest[:i]


re = Solution()
print(re.longestCommonPrefix(["aaab", "aaa"]))
