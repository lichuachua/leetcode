class Solution:
    def firstUniqChar(self, s: str) -> int:
        queue = [s[0]]
        low, high = 0, 1
        for i in range(1, len(s)):
            if high != low and queue[low] == s[i]:
                low += 1
            else:
                queue.append(s[i])
                high += 1
        if high == low:
            return -1
        return low


re = Solution()
print(re.firstUniqChar("aadadaad"))
