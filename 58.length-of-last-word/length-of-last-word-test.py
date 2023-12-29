class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count, i = 0, len(s) - 1
        for i in range(len(s) - 1, -1, -1):
            if s[i] != ' ':
                count += 1
            elif s[i] == ' ' and count != 0:
                break
        return count


re = Solution()
print(re.lengthOfLastWord("Hello World"))
