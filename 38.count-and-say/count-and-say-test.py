class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        else:
            prev = self.countAndSay(n - 1)
            result = ""
            count = 1
            for i in range(len(prev)):
                if i < len(prev) - 1 and prev[i] == prev[i + 1]:
                    count += 1
                else:
                    result += str(count) + prev[i]
                    count = 1
        return result


re = Solution()
print(re.countAndSay(4))
