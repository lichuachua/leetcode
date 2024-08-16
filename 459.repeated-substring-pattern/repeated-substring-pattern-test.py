class Solution:
    def generateNext(self, p: str):
        m = len(p)
        next = [0 for _ in range(m)]

        left = 0
        for right in range(1, m):
            while left > 0 and p[left] != p[right]:
                left = next[left - 1]
            if p[left] == p[right]:
                left += 1
            next[right] = left

        return next

    def repeatedSubstringPattern(self, s: str) -> bool:
        size = len(s)
        if size == 0:
            return False
        next = self.generateNext(s)
        if next[size - 1] != 0 and size % (size - next[size - 1]) == 0:
            return True
        return False


re = Solution()
print(re.repeatedSubstringPattern("abcabcabcabc"))
