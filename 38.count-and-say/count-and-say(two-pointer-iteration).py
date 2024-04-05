class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        result = "1"
        for _ in range(n - 1):
            result = self.generateNext(result)
        return result

    def generateNext(self, s: str) -> str:
        result = ""
        count = 1
        i = 0
        while i < len(s):
            if i < len(s) - 1 and s[i] == s[i + 1]:
                count += 1
            else:
                result += str(count) + s[i]
                count = 1
            i += 1
        return result
